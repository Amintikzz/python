from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Салам алейкум</h1>'


@app.route('/TB')
def TB():
    return '<button>Buy</button>'
    

if __name__ == '__main__':
    app.run(debug=True)
