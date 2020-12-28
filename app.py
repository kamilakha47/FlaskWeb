from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("public_index.html")

# Register Student #
@app.route("/register-student")
def register():
    return render_template("register_student.html")

@app.route("/register/student", methods=["GET", "POST"])
def register_students():
    if request.method == "POST":
        req = request.get_json()
        print(req)
        res = make_response(jsonify(req), 200)
        return res
    return "OK"

# Register Instructor #
# @app.route("/register")
# def register():
#     return render_template("register_student.html")

# @app.route("/register/student", methods=["GET", "POST"])
# def register_student():
#     if request.method == "POST":
#         req = request.get_json()
#         print(req)
#         res = make_response(jsonify(req), 200)
#         return res
#     return "OK"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=6000)