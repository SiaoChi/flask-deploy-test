from flask import Flask
from application.app import app
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'))
