FROM python:3.9
ADD ./src /controller
ADD __init__.py /controller
WORKDIR /controller
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
