FROM python:3.9.7
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "application.app:app"]

# 注意docker run的指令如下
# docker container run -d -p 80:8000 flask (後面不用加入bin/bash)
