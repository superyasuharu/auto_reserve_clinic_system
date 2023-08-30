from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reservations.db"  # SQLiteデータベースの設定
db = SQLAlchemy(app)
# db.init_app(app)


from . import models

# # ここでデータベースの初期化を行います
with app.app_context():
    db.create_all()
# db.init_app(app)

# ここでルートやビュー関数、拡張機能などを設定します
from . import routes
