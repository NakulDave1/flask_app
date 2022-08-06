from flask import Flask,render_template

app=Flask(__name__)

@app.route('/user/<name>')
def main_page(name,password='hpsystem'):
    text=['<h1>',"This", 'is' ,'HP', 'System' ,'Data' ,'</h1>']
    return render_template('index.html',name=name,password=password,text=text)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404
@app.errorhandler(505)
def erro_505():
    return render_template("404.html"),505