FROM python:3.9
ADD ./src /app/src
ADD __init__.py /app
WORKDIR /app
RUN pip install -r src/requirements.txt
CMD ["python", "src/app.py"]
