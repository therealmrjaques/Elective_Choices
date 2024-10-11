from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#Electives List
ELECTIVES = ["Commerce", "Computing Technology", "Drama"]

elective_dict = {}

@app.route('/')
def index():
    return render_template("index.html", electives = ELECTIVES)

@app.route('/register', methods=["POST"])
def register():
    name = request.form.get("name")
    elective = request.form.get("electives")
    if not request.form.get("name") or not request.form.get("electives"):
        return render_template("failure.html", message="Check you have entered a name or selected an elective")
    
    elective_dict[name] = elective

    return redirect("/registrants")

@app.route('/registrants')
def registrants():
    return render_template("registrants.html", registrants=elective_dict)
