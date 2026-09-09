from flask import Flask;

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Project 1 Success! Docker Working!</h1><p>Hello ibu!</p>"

@app.route('/about')
def about():
    return "<h2>About Page</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True