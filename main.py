from flask import Flask
from flask import request
from flask import render_template
import config
from models import Assistant
from utils import handle_dates

app = Flask(__name__)


@app.route("/")
def index():
    html = "<br>".join(
        ["<a href='{0}''>{0}".format(i) for i in config.EDITIONS.keys()]
    )
    return html


@app.route("/<year>", methods=["GET", "POST"])
def hello(year):
    flash_message = ""
    assistants_handler = Assistant(year)
    if request.method == "POST":
        try:
            assistants_handler.write([
                request.form["name"],
                request.form["email"],
                request.form["phone"],
                request.form["favproglang"],
                request.form["book"],
            ])
        except Exception as e:
            flash_message = "Ups! Algo ha ido mal :( " + str(e)
        else:
            flash_message = "Enhorabuena! Ya formas parte de CSI"

    days_to_go, event_datetime_as_string, limitdate_signup_as_string = \
        handle_dates(year)
    assistants = assistants_handler.get_assistants()
    num_assistants = len(assistants)
    books = assistants_handler.get_books()
    num_books = len(books)
    favproglang_stats = assistants_handler.favproglang_stats()
    num_favproglangs = len(favproglang_stats)

    return render_template(
        "main.html",
        year=year,
        days_to_go=days_to_go,
        event_datetime_as_string=event_datetime_as_string,
        limitdate_signup_as_string=limitdate_signup_as_string,
        flash_message=flash_message,
        embedmap_src=config.EDITIONS[year]["EMBEDMAP_SRC"],
        assistants=assistants,
        num_assistants=num_assistants,
        books=books,
        num_books=num_books,
        favproglang_stats=favproglang_stats,
        num_favproglangs=num_favproglangs
    )


if __name__ == "__main__":
    app.debug = True
    app.run()
