from flask import Flask,render_template,request
import pickle

def prediction(lst):
    filename = "Model/model.pickle"
    with open(filename,"rb") as file:
        model = pickle.load(file)

    pred_value = model.predict([lst])
    return pred_value


app = Flask(__name__)

@app.route('/',methods=["POST","GEt"])
def index():
    pred = 0
    if request.method == "POST":

        aut = request.form["aut"]
        sot = request.form["sot"]
        bd = request.form["bd"]
        noai = request.form["noai"]
        du = request.form["du"]
        age = request.form["age"]
        os = request.form.get("devicemodel")
        gender = request.form.get("gender")

        values = []


        if os == "Android":
            values.append(0)
        else:
            values.append(1)

        values.append(float(aut))
        values.append(float(sot))
        values.append(float(bd))
        values.append(int(noai))
        values.append(float(du))
        values.append(int(age))

        if gender == "Male":
            values.append(0)
        else:
            values.append(1)

        pred = prediction(values)
        pred = pred[0]

        
    return render_template("index.html",pred = pred)


if __name__ == "__main__":
    app.run(debug=True)