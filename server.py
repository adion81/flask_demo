from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/repeat/<string:name>/<int:number>')
def repeat(name,number):

    return render_template('repeat.html',banana=name,times=number)


@app.route('/change')
def change():
    return "We made this change"

if __name__=="__main__": 
    app.run(debug=True)