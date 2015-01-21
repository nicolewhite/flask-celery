from webapp import app
from models import create_node
from flask import request

@app.route('/add_stuff', methods=['POST'])
def add_stuff():
    name = request.json['name']
    create_node.delay(name)
    return 'yay', 200