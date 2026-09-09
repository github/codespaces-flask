from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def random_number():
    number = random.randint(1, 100)
    return jsonify({'random_number': number})

if __name__ == '__main__':
    app.run(debug=True)
