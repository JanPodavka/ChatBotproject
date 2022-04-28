# imports
import locale
from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


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
    if question.lower() == "Jaký je čas?".lower():
        now = datetime.now()
        return now.strftime("%H:%M:%S")

    else:
        return "nerozumím"


if __name__ == "__main__":
    app.run()
