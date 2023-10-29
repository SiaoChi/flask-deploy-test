
from flask import Flask, redirect, render_template, request, url_for
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from .views import view_blueprint

load_dotenv()

#  取得啟動文件資料夾路徑
pjdir = os.path.abspath(os.path.dirname(__file__))

# export FLASK_DEBUG=1 調整debug模式 in terminal

app = Flask(__name__)
# app.register_blueprint
app.register_blueprint(view_blueprint)
app.config["MONGO_URI"] = os.getenv('MONGODB_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
mongo = PyMongo(app)


try:
    test_document = mongo.db.history.find_one()
    if test_document:
        print("Successfully connected to MongoDB")
    else:
        print(
            "Connected to MongoDB, but couldn't find any documents in the collection.")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")


'''
補充：以下是使用python module pymongdb直接創造client，跟flask_pymongo的指令會有點不一樣，連線的URI也會不同。
flask_pymongo: 以帳號密碼+IP連線網址組成
pymongdb: 以官網提供的連線網址組成

MONGODB_URI = os.getenv('MONGODB_URI')
client = pymongo.MongoClient(MONGODB_URI)
print(client)
db = client["stylish_chat"]
print(db)
'''

if __name__ == '__main__':
    app.run(debug=True)
