FROM python:3.10

EXPOSE 8000

WORKDIR /app/

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0:8000"]
