from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple list to store tasks
tasks = []


# POST /tasks - Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()

    task = {
        "title": data["title"],
        "status": data["status"]
    }

    tasks.append(task)

    return jsonify({
        "message": "Task added successfully",
        "task": task
    }), 201


# GET /tasks - View all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


if __name__ == '__main__':
    app.run(debug=True)
