import os
from app import create_app
from app import db
from app.games import Game
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    with app.app_context():
        db.create_all()
        for rule in app.url_map.iter_rules():
            print(rule)
