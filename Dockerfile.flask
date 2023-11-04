FROM python:3.9.7
WORKDIR /app
COPY ./requirements.txt  /app
RUN pip install -r requirements.txt 
COPY . /app
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "application.app:app"]

# 注意docker run的指令如下
# docker container run -d -p 8000:8000 flask 有自己的CMD (後面不用加入bin/bash)
