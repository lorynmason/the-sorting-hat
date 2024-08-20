FROM python:3.11
WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /usr/src/requirements.txt \ 
    && pip install fastapi uvicorn
COPY ./app /app