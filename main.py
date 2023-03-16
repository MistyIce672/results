from flask import Flask,render_template

app = Flask(__name__)

@app.route("/results")
def results():
    return(render_template('result.html'))

@app.route("/perfume")
def perfume():
    return(render_template('perfume.html'))

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8124)