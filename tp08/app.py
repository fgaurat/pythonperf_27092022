from flask import Flask,render_template

from TodoDAO import TodoDAO

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/todos")
def get_todos():
    dao = TodoDAO('./todos_db.sqlite')
    todos = dao.find_all()

    return render_template('todos.html',todos=list(todos))








    

# @app.route("/todosold")
# def get_todos_old():
#     dao = TodoDAO('./todos_db.sqlite')
#     todos = dao.find_all()
#     html = "<table>"
#     for todo in todos:
#         html+=f"""
#         <tr>
#         <td>{todo.id}</td>
#         <td>{todo.title}</td>
#         <td>{todo.completed}</td>
#         </tr>""" 
    
#     html+="</table>"
#     return html
