from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware

import cv2
import numpy as np
from io import BytesIO

app = FastAPI()

# Configuration CORS pour permettre au frontend de communiquer avec l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les origines
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes
    allow_headers=["*"],  # Autorise tous les en-têtes
)

@app.post("/upload_image")
async def upload_image(file: UploadFile = File(...)):
    # Lire le fichier image
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Traitement de l'image avec votre modèle (à implémenter)
    # result = your_model.process_image(img)

    # Sauvegarder l'image traitée temporairement (exemple)
    output_filename = "temp_output_image.jpg"
    cv2.imwrite(output_filename, img)  # Remplacer img par votre image traitée

    return FileResponse(output_filename)
