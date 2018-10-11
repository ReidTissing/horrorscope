#from readit import *
from flask import Flask, render_template
import markovify

app = Flask(__name__)



# Print three randomly-generated sentences of no more than 140 characters
# for i in range(3):
#     print(text_model.make_short_sentence(140))
def make_horror():
    with open("dumbhorror.txt") as f:
        text = f.read()
    with open("horror.json") as g:
        text2 = g.read()
    text = text + text2
    # Build the model.
    text_model = markovify.Text(text)
    sents = ""
    # Print five randomly-generated sentences
    for i in range(2):
        sents = sents + " " + text_model.make_sentence()
    return sents
        #return text_model.make_sentence()

@app.route("/")
def displayhorror():
    #horoscopetoprint = generate()
    horrorscope = make_horror()
    return render_template("index.html", print=horrorscope)

@app.route("/bg")
def displayrando():
    horrorscope = make_horror()
    return render_template("rando.html", print=horrorscope)

@app.route("/about")
def displayabout():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug = True)
