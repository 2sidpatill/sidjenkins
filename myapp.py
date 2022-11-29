from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'you r good!'

if __name__ == '__main__':
    app.run()
