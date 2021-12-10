# Third Party
from flask import Blueprint, render_template, redirect, url_for, request
from bson.objectid import ObjectId
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
    todo_item = request.form.get('new-todo')
    if todo_item:
        todos_collection.insert_one(
            {
                'text': todo_item,
                'complete': False
            }
        )
    return redirect(url_for('main.index'))

@main.route('/complete_todo/<oid>')
def complete_todo(oid):
    todos_collection = mongo.db.todo
    if oid:
        todo = todos_collection.find_one({
            '_id': ObjectId(oid)
        })
        todo['complete'] = True
        todos_collection.replace_one({'_id': ObjectId(oid)}, todo)
    return redirect(url_for('main.index'))

@main.route('/delete_completed')
def delete_completed():
    todos_collection = mongo.db.todo
    todos_collection.delete_many({'completed': True})
    return redirect(url_for('main.index'))
