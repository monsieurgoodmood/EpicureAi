from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
import cv2
import uvicorn
import numpy as np
from typing import Optional
import os

# Importer les fonctions depuis recipes_chatgpt
from epicureai.api.recipes_chatgpt import generate_recipe, mock_yolo_model

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
async def upload_image(
    file: UploadFile = File(...),
    diet: Optional[str] = Form(None),
    allergies: str = Form(""),
    intolerances: str = Form(""),
    time_available_in_minutes: Optional[int] = Form(None),
    kitchen_equipment: str = Form("")
):
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Le fichier envoyé n'est pas une image valide ou n'a pas pu être décodée.")

        allergies_list = allergies.split(",") if allergies else []
        intolerances_list = intolerances.split(",") if intolerances else []
        kitchen_equipment_list = kitchen_equipment.split(",") if kitchen_equipment else []

        ingredients = mock_yolo_model(img)
        recipe = generate_recipe(ingredients, diet, allergies_list, intolerances_list, time_available_in_minutes, kitchen_equipment_list)
        print("Recipe from generate_recipe:", recipe)  # Débogage

        return JSONResponse(content={"ingredients": ingredients, "recipe": recipe})

    except Exception as e:
        print(f"Erreur lors du traitement de la requête: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
