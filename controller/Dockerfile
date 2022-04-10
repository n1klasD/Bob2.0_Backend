FROM python:3.9
ADD ./src /app
ADD __init__.py /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
