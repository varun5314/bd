from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Priya"}
]

@app.route("/students")
def students_list():
    return jsonify({
        "success": True,
        "message": "Students found",
        "data": students
    }), 200


@app.route("/student/<int:id>")
def student(id):
    for student in students:
        if student["id"] == id:
            return jsonify({
                "success": True,
                "message": "Student found",
                "data": student
            }), 200

    return jsonify({
        "success": False,
        "message": "Student not found",
        "data": None
    }), 404


if __name__ == "__main__":
    app.run(debug=True)
