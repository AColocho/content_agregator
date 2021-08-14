FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app/docker_fastapi

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]