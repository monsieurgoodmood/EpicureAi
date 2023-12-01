FROM python:3.8

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./app.py /app/

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
