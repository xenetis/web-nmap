FROM python:3.10

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY requirements.txt  /src/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r  /src/requirements.txt

COPY ./apps /src/apps
COPY .env /src/.env
COPY run.py /src/run.py
COPY gunicorn.py /src/gunicorn.py

RUN mkdir -p /src/_datas \
    && chmod 755 /src/_datas

#CMD ["gunicorn", "--config", "gunicorn.py", "run:app"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

EXPOSE 5000/tcp