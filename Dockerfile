FROM python:3.11

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

### Expose ports for FastAPI (8000) and Streamlit (8501) - By default ###
EXPOSE 8000
EXPOSE 8501

# Start both FastAPI and Streamlit using a process manager like `pm2` or `gunicorn` with Streamlit
# For simplicity, we'll use a shell script to start both

CMD ["sh", "-c", "uvicorn backend:app --host 0.0.0.0 --port 8000 & streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0"]
# CMD ["uvicorn backend:app --host 0.0.0.0 --port 8000 & streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0"]
