# flask-deploy-test

## 專案結構
1. 使用docker手動 run container 搭配 dockerfile
2. nginx - gunicorn - flask(python)
![flask-structure](https://github.com/SiaoChi/flask-deploy-test/assets/98171354/6ffa93f9-5b5b-4715-a4c0-6d4a5206b179)


## 手動部署流程

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
6. run container : `docker container run -it -p 8000:8000 flask`
7. `control p control q`退出container
8. run container : nginx -p 80:80
9. 修改 nginx.config檔案設定，包含proxy IP
10. 設定完成重新reload檔案指令 `docker exec -it your_nginx_container_name nginx -s reload`
11. 完成

### deploy notice
原本run container為`docker container run -it -p 80:8000 flask /bin/bash`，後方加入/bin/bash導致沒有成功部署，查詢原因flask本身就是一個process，如果/bin/bash被執行flask這個process就不會執行。＊不放的/bin/bash就是預設的CMD

## 自動部署流程
1. 依據Dockerfile.nginx ,  Dockerfile.flask 兩個dockerfile部署
2. 因有多個container因此另外使用docker compose  `docker compose up`

### 使用IP連線
記得是http, 除非有設定ssl才是https

