from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import ToDoForm

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

from models import ToDo

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ToDoForm()
    if form.validate_on_submit():
        new_todo = ToDo(description=form.description.data)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('index'))
    todos = ToDo.query.all()
    return render_template('index.html', form=form, todos=todos)

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todo = ToDo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
