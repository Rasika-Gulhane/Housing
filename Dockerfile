FROM python:3.7
COPY . /application
WORKDIR /application
RUN pip install -r requirements.txt
RUN pip install gunicorn
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT application:app