FROM python:3.10

RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential gcc && apt-get clean

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /code
USER appuser

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
