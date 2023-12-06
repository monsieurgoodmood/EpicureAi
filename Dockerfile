FROM python:3.10-buster

# Mettre à jour la liste des packages et installer les dépendances requises pour OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx

WORKDIR /app

# Copier les fichiers requirements.txt dans le répertoire de travail
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'ensemble du dossier du projet dans le conteneur
COPY . .

EXPOSE 8000

CMD ["uvicorn", "epicureai.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
