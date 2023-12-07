FROM python:3.10-buster

# Mettre à jour la liste des packages et installer les dépendances requises pour OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN apt-get install \
  'ffmpeg'\
  'libsm6'\
  'libxext6'  -y

# Copier les fichiers requirements.txt dans le répertoire de travail
COPY requirements.txt requirements.txt

# Installer les dépendances
COPY setup.py setup.py
RUN pip install .

# Copier l'ensemble du dossier du projet dans le conteneur
COPY epicureai epicureai/
COPY epicureai/data/models/best-113.pt /home/.epicureai_data/models/best-113.pt

CMD uvicorn epicureai.api.main:app --host 0.0.0.0 --port $PORT
