FROM tiangolo/uvicorn-gunicorn:python3.11

EXPOSE 8000

WORKDIR /usr/src/app

COPY config/requirements.txt /usr/requirements.txt
RUN pip install --no-cache-dir -r /usr/requirements.txt

COPY ./app /usr/src/app

CMD [ "fastapi", "run", "main.py", "--port", "8000"]