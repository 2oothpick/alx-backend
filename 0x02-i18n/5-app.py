#!/usr/bin/env python3
"""
i18n: Mock logging in
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict

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

# mock user logins
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Retrieves the user's login ID
    """
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """
    use get_user to find a user if any.
    """
    g.user = get_user()


@babel.localeselctor
def get_locale() -> str:
    """
    Determines the best language
    match
    """
    locale = request.args.get("locale", "")
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """
    Returns the homepage
    """
    return render_template(
        "5-index.html",
    )


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
