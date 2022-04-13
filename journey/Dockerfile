FROM python:3.9
ADD ./src /app/src
ADD main.py /app
WORKDIR /app
RUN pip install -r src/requirements.txt
ENV FLASK_ENV=development
CMD ["python", "main.py"]
