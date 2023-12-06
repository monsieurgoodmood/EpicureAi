from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
import cv2
import numpy as np
from typing import Optional
import traceback

# Importer les fonctions depuis recipes_chatgpt
from epicureai.api.recipes_chatgpt import generate_recipe
from epicureai.ml_logic.predict import yolo_predict_ingedients


app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les origines
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes
    allow_headers=["*"],  # Autorise tous les en-têtes
)

@app.post("/upload_image")
async def upload_image(file: UploadFile = File(...), diet: Optional[str] = Form(None), allergies: str = Form(""), intolerances: str = Form(""), time_available_in_minutes: Optional[int] = Form(None), kitchen_equipment: str = Form("")):
    try:
        contents = await file.read()
        img = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Invalid image file.")

        allergies_list = allergies.split(",") if allergies else []
        intolerances_list = intolerances.split(",") if intolerances else []
        kitchen_equipment_list = kitchen_equipment.split(",") if kitchen_equipment else []

        ingredients, annotations = yolo_predict_ingedients(img)
        recipe = generate_recipe(ingredients, diet, allergies_list, intolerances_list, time_available_in_minutes, kitchen_equipment_list)  # Doit être une fonction dans le module recipes_chatgpt

        assert isinstance(ingredients, list)
        assert isinstance(annotations, list)

        return JSONResponse(content={"ingredients": ingredients, "annotations": annotations, "recipe" : recipe})
    except AssertionError:
        return JSONResponse(content={"error": "Non-serializable data"}, status_code=500)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(content={"error": str(e)}, status_code=500)
