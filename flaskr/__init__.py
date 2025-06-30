import os
from flask import Flask

def create_app(test_config=None):
    # アプリを作成して設定する
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # 開発用の設定を読み込む
        app.config.from_pyfile('config.py', silent=True)
    else:
        # テスト用の設定を読み込む
        app.config.from_mapping(test_config) 
    
    # インスタンスフォルダを作成する
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass 
    
    #hello worldのルートを登録する
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    return app