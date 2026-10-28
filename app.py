from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello from GitHub Actions!</h1><p>My automated deployment works.</p>"

if __name__ == '__main__':
    app.run()
