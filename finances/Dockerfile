FROM python:3.9-alpine
ADD ./src /app
WORKDIR /app
RUN apt install buildtools
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
