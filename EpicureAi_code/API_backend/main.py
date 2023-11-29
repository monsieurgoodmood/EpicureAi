from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
import cv2
import numpy as np
from io import BytesIO

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
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Ici, vous appellerez votre vrai modèle YOLO. Pour l'instant, nous utilisons une simulation
    ingredients = mock_yolo_model(img)

    # Retourner les ingrédients simulés
    return JSONResponse(content={"ingredients": ingredients})

def mock_yolo_model(image):
    # Cette fonction est juste un bouchon pour simuler la sortie de votre modèle YOLO
    # Elle retourne une liste d'ingrédients fictifs
    return ["ingrédient1", "ingrédient2", "ingrédient3"]
