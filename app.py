from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
     return "Hello World!"

@app.route('/template')
def show_template():
     return render_template("index.html")
    
    
if __name__ == '__main__':
    app.run(debug=True) 
  