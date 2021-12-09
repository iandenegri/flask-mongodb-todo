# Third Party
from flask import Blueprint, render_template, redirect, url_for, request

# Local

main = Blueprint("main", __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/add_todo', methods=['POST'])
def add_todo():
    todo_item = request.form.get('new-todo')
    return redirect(url_for('main.index'))