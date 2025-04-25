from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route("/real_para_dolar", methods=["POST"])
def real_para_dolar():
    taxa = 5.20
    real = float(request.form["real"])
    resultado = round(real / taxa,2)
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)