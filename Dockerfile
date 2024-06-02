FROM tiangolo/uvicorn-gunicorn:python3.11

EXPOSE 8000

WORKDIR /usr/src

COPY config/requirements.txt /usr/src/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/requirements.txt

COPY ./app /usr/src/app
COPY ./tests /usr/src/tests

CMD [ "fastapi", "run", "app/main.py", "--port", "8000"]