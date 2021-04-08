FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /usr/src/app
COPY ./ ./

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]