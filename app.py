#from readit import *
from flask import Flask, render_template
import markovify
from datetime import datetime
from datetime import timedelta

app = Flask(__name__)

# Print three randomly-generated sentences of no more than 140 characters
# for i in range(3):
#     print(text_model.make_short_sentence(140))
def make_horror():
    with open("dumbhorror.txt") as f:
        text = f.read()
    with open("horror.json") as g:
        text2 = g.read()
    with open("hor.json") as e:
        text3 = e.read()
    text = text + text2 + text3
    # Build the model.
    text_model = markovify.Text(text)
    sents = ""
    # Print five randomly-generated sentences
    for i in range(2):
        sents = sents + " " + text_model.make_sentence()
    return sents
        #return text_model.make_sentence()


def add_month(changemonth):
    thismonth = datetime.now().strftime('%B')
    months = 'October', 'November', 'December'
    for months in months:
        changemonth = changemonth.replace(months, thismonth)
    return changemonth

@app.route("/")
def displayhorror():
    #horoscopetoprint = generate()
    horrorscope = make_horror()
    horrorscope = add_month(horrorscope)
    return render_template("index.html", print=horrorscope)


@app.route("/about")
def displayabout():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
