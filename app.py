# imports
import locale
import nltk
import unidecode

from datetime import datetime

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

# define app routes
@app.route("/")
def test():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    question = request.args.get('msg')
    answer = get_answer(question)
    return str(answer)


def get_answer(question):
    norm_question = unidecode.unidecode(question.lower())
    if nltk.edit_distance(norm_question, "jaky je cas?") < 2:
        now = datetime.now()
        return now.strftime("%H:%M:%S")
    elif nltk.edit_distance(norm_question, "jaky je kurz?") < 2:
        pass
    elif nltk.edit_distance(norm_question, "jak se jmenujes?") < 2:
        return "Jmenuji se Chatbot"
    else:
        return "nerozumím"


if __name__ == "__main__":
    app.run()
