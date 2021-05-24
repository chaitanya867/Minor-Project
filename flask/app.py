from flask import Flask, render_template, request

app = Flask("heart-disease-prediction")


from keras.models import load_model

model = load_model('heartdisease_predicting_model.h5')

@app.route("/")
def home():
    return render_template("form.html")



@app.route("/result" , methods=[ 'GET' ])
def result():
        x1 = int(request.args.get("x1"))
        x2 = int(request.args.get("x2"))
        x3 = int(request.args.get("x3"))
        x4 = int(request.args.get("x4"))
        x5 = int(request.args.get("x5"))
        x6 = float(request.args.get("x6"))
        x7 = float(request.args.get("x7"))
        x8 = int(request.args.get("x8"))
        result = model.predict([[ x1 , x2 , x3 , x4 , x5 , x6 , x7 , x8 ]])
        result=round(result[0][0])
        if round(result) == 0:
            return render_template("b.html")
        else:
            return render_template("a.html")

app.run(port=1234, host='0.0.0.0')

