# flask-deploy-test

## 部署流程

### local application config
1. install gunicorn
2. 執行run.sh於本地端，確認gunicorn可以跑
3. 更新所需module version `$ pip freeze > requirements.txt`
4. git push (待處理gitAction)

### ec2 config
1. 確認 security group port 有 80（http) or 443(https)
2. install docker
3. git pull 資料
4. touch .env 並把環境變數更新
5. build image : 於project資料夾中run build Dockerfile `docker build -t {image name} .` 
6. run container : `docker container run -it -p 80:8000 flask`
7. `control p control q`退出container
8. 透過EC2 IP應該就可以進去網站

### deploy notice
原本run container為`docker container run -it -p 80:8000 flask /bin/bash`，後方加入/bin/bash導致沒有成功部署，查詢原因flask本身就是一個process，如果/bin/bash被執行flask這個process就不會執行。
