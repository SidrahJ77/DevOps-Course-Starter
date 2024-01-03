from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import get_items
from todo_app.data.Trello_items import add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template("index.html", items = items)

@app.route('/add_todo', methods=["post"])
def add_todo():
    new_todo_title = request.form.get('title')
    add_item(new_todo_title)
    return redirect('/')