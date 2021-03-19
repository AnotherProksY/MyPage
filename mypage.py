"""Bottle web-server."""

from bottle import Bottle
from bottle import template, static_file
from os.path import dirname, abspath
from datetime import date, timedelta

app = Bottle()

BASE_DIR = dirname(abspath(__file__))


@app.route('/static/<filename:path>')
def server_static(filename):
    """Serve all static files which used in HTML."""
    return static_file(filename, root=f'{BASE_DIR}/static')


@app.route("/")
def main():
    """Load main page."""
    age = (date.today() - date(1999, 11, 11)) // timedelta(days=365.2425)

    return template(f'{BASE_DIR}/views/main.html', age=age)


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
