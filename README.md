# Epicure AI: Advanced Data Science Project

# 🚀 Description
Epicure AI is an advanced, AI-driven culinary application designed to revolutionize cooking experiences. By utilizing AI to analyze photographs of available ingredients, the app crafts personalized recipes that cater to the user's dietary needs, allergies, intolerances, and available kitchen equipment. This innovative project features a FastAPI backend, YOLO-based ingredient recognition, and a sleek Streamlit user interface.

# 📋 Prerequisites
- **Python 3.8+**
- **Key Libraries:** FastAPI, OpenCV, Ultralytics, Streamlit (see `requirements.txt` for full details)
- **Google Cloud account** for model training and API hosting

# 🛠 Installation
1. **Clone the Repository:**
   ```shell
   git clone https://github.com/monsieurgoodmood/epicureai.git

# Install Dependencies:
pip install -r requirements.txt

# Epicure AI Project Configuration :
Create a .env file at the root with necessary keys

- OPENAI_KEY=your_openai_api_key_here
- ROBOFLOW_APIKEY=your_roboflow_api_key_here
- COMET_API_KEY=your_comet_ml_api_key_here
- COMET_PROJECT_NAME=your_comet_ml_project_name_here
- COMET_MODEL_NAME=your_comet_ml_model_name_here
- COMET_WORKSPACE_NAME=your_comet_ml_workspace_name_here
- NUM_EPOCHS=desired_number_of_epochs

## Google Cloud Configuration (optional, if used for training or hosting)
- GOOGLE_CLOUD_PROJECT_ID=your_google_cloud_project_id_here
- GOOGLE_CLOUD_COMPUTE_ZONE=your_google_cloud_compute_zone_here
- GOOGLE_CLOUD_GPU_TYPE=your_desired_gpu_type_here

## Database Configuration (if applicable)
- DATABASE_URL=your_database_url_here

## Other Configuration
**Add any additional configuration variables that your application requires** 

**Note: Never commit this file to version control. It should remain local/private.**
Configure Google Cloud for training and API hosting, ensuring GPU setup for training and FastAPI deployment using Google Cloud Run and Docker.

# 🖥 Usage
1. Launch FastAPI:
uvicorn epicureai.api.main:app --reload

2. Streamlit Interface:
streamlit run epicureai/app/app.py

3. Train the Model:
Utilize dockerfile.training on a Google Cloud GPU.

# 📁 Project Structure
epicureai/
- api                 # FastAPI backend
- app                 # Streamlit UI
- data                # Data scripts
- interface           # Model training interface
- ml_logic            # ML logic and params
- notebook            # Jupyter notebooks
- raw_data            # Data sets

Root Files: .env, dockerfile, makefile, requirements.txt, setup.py, .gitignore, .env.yaml

# 🤝 Contribution
1. Fork the repository
2. Create a feature branch
3. Submit a detailed PR

# 📬 Contact
Questions or suggestions? Contact Arthur Choisnet at arthur.choisnet74@gmail.com
