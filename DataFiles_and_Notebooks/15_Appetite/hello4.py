# We're going to try to add some style to our website
# but if we continue to deal with just strings, it's going to get messy

from flask import Flask, url_for
app = Flask(__name__)


import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

import os
import sys
import IPython.html as ipynb

if not os.path.exists('static') :
    if sys.platform == 'win32':
        import shutil
        shutil.copytree(ipynb.DEFAULT_STATIC_FILES_PATH, 'static')
    else:
        # the next line won't work on windows
        os.symlink(ipynb.DEFAULT_STATIC_FILES_PATH, 'static')


header = """
<head>
    <link rel="stylesheet" href="/static/components/jquery-ui/themes/smoothness/jquery-ui.min.css" type="text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="/static/style/style.min.css" type="text/css"/>
</head>
"""
run_on_public_interface = True

@app.route("/")
def hello():
    return "Hello World!"

# read more about using variables here:
# http://flask.pocoo.org/docs/quickstart/#variable-rules
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/tweet/<int:tweet_id>')
def show_tweet(tweet_id):
    # show the tweet with the given id, the id is an integer
    username = 'ivanov'
    user_url = url_for('show_user_profile', username=username)
    link = '<div class="prompt"><a href="{url}">{text}</a></div>'
    s = ''
    s += "<div class='container' id='notebook-container'>" 
    s += "<div class='cell border-box-sizing selected' >"
    s += link.format(url=user_url, text=username)
    s += "<div class='input_area' style='padding:20px'> <p>let's see how this looks</p></div>" 
    s += "</div>" 
    s += "</div>" 
    s += "</div>" 
    return header + s + 'tweet_id %d' % tweet_id

if __name__ == "__main__":
    if run_on_public_interface:
        app.run(debug=True,host='0.0.0.0')
    else:
        app.run()
