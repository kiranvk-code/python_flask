from flask import Flask, jsonify
from datetime import date

app = Flask(__name__)

@app.route('/date')
def get_date():
    today_date = date.today().strftime("%Y-%m-%d")
    return jsonify({'date': today_date})

if __name__ == '__main__':
    app.run(port=8080)
