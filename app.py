from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story
app = Flask(__name__)



app.config['SECRET_KEY'] = "SECRET_KEY_BRO"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    prompts = story.prompts
    return render_template('home.html', prompts=prompts)


@app.route('/madlibs')
def get_madlib():
    # place = request.args["place"]
    # noun = request.args["noun"]
    # verb = request.args["verb"]
    # adjective = request.args["adjective"]
    # plural_noun = request.args["plural_noun"]
    # return render_template("madlibs.html", place = place, noun= noun, verb = verb, adjective = adjective, plural_noun = plural_noun)
    text = story.generate(request.args)
    return render_template("madlibs.html", text=text)