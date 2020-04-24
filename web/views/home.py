from flask import render_template
from web import blueprint_web as web


@web.route("/", methods=['GET', 'POST'])
def index():
    return render_template('home.html')

