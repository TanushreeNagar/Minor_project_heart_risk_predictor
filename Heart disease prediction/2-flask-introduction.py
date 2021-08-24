from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return "hello this is my website"
    
@app.route('/page1')
def page1():
    return "this is my first page"

@app.route('/page2')
def page2():
    return  render_template('page2.html')
    
	
app.run(debug=True)