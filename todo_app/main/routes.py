# Third Party
from flask import Blueprint, render_template, redirect, url_for, request

# Local
from ..extensions import mongo

main = Blueprint("main", __name__)

@main.route('/')
def index():
    todos_collection = mongo.db.todo
    todo_items = todos_collection.find()
    return render_template("index.html", todos=todo_items)

@main.route('/add_todo', methods=['POST'])
def add_todo():
    todos_collection = mongo.db.todo
    print(todos_collection)
    todo_item = request.form.get('new-todo')
    if todo_item:
        todos_collection.insert_one(
            {
                'text': todo_item,
                'complete': False
            }
        )
    return redirect(url_for('main.index'))

@main.route('/finish_todo', methods=['POST'])
def complete_todo():
    pass
