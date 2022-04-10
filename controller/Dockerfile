FROM python:3.9
ADD ./src /app/src
ADD __init__.py /app
WORKDIR /app/src
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
