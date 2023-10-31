# flask-deploy-test

## 專案結構
1. 使用docker手動 run container 搭配 dockerfile
2. nginx - gunicorn - flask(python)
![flask-structure](https://github.com/SiaoChi/flask-deploy-test/assets/98171354/38d2d3eb-a29d-48ee-9869-b33b46b7949c)

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
6. run container : `docker container run -it -p 8000:8000 flask`
7. `control p control q`退出container
8. run container : nginx -p 80:80
9. 修改 nginx.config檔案設定，包含proxy IP
10. 設定完成重新reload檔案指令 `docker exec -it your_nginx_container_name nginx -s reload`
11. 完成

### deploy notice
原本run container為`docker container run -it -p 80:8000 flask /bin/bash`，後方加入/bin/bash導致沒有成功部署，查詢原因flask本身就是一個process，如果/bin/bash被執行flask這個process就不會執行。＊不放的/bin/bash就是預設的CMD

### 成果畫面
記得是http, 除非有設定ssl才是https
![http](https://github.com/SiaoChi/flask-deploy-test/assets/98171354/ed0f990b-2dd6-49b9-bf14-1476af54f4cb)

