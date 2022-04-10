FROM python:3.9
ADD ./src /controller/src
ADD __init__.py /controller
WORKDIR /controller/src
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
