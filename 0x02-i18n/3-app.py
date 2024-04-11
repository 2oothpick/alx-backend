#!/usr/bin/env python3
"""
Getting local from request
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


# babel configuration
class Config:
    """Represents a Flask Babel configuration."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselctor
def get_locale() -> str:
    """
    Determines the best language
    mathc
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """
    Returns the homepage
    """
    return render_template(
        "3-index.html",
    )


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
