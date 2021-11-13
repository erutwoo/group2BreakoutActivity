from python:3.8.10

workdir /app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY . .

EXPOSE 8000 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

