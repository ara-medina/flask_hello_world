from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello world!"

@app.route("/hello/<name>")
def hi_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p> 
            kitten pic 
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    
    return html.format(name.title())
    
@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    jedi_first = first[0] + first[1] 
    jedi_last = last[0] + last[1] + last[2]
    jedi_full = jedi_last + jedi_first
    return jedi_full
    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
