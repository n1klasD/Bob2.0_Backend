FROM python:3.9-alpine
ADD ./src /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]