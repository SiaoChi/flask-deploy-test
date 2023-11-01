gunicorn -w 4 -b 0.0.0.0:8000 application.app:app
# 以下為執行run.sh的檔案方式
# $ chmod +x run.sh
# $./run.sh