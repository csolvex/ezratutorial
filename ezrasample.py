#CS50 Ezra example

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    
'''
@app.route('/weather')
def weather():
    return render_template('weather.html')

'''
    
    
if __name__ =="__main__":
    app.run(debug=True)