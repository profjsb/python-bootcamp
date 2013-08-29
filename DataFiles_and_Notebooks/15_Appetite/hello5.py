# We're going to try to add some style to our website
# but if we continue to deal with just strings, it's going to get messy

from flask import Flask, url_for, render_template
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


run_on_public_interface = True

@app.route("/")
def hello():
    return "Hello World!"

# read more about using variables here:
# http://flask.pocoo.org/docs/quickstart/#variable-rules
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    # Let's just hardcode some tweets for now
    tweets = ["Something awesome happened at #pyboot", 
            "The first rule of #pyboot is you must tell everyone about #pyboot",
            "The second rule of #pyboot is: you must endure memes and pop culture references" 
            ]
    return render_template('user_dummy.html', username=username, tweets=tweets)

@app.route('/tweet/<int:tweet_id>')
def show_tweet(tweet_id):
    # show the tweet with the given id, the id is an integer
    username = 'ivanov'
    user_url = url_for('show_user_profile', username=username)
    # We've hidden away the string logic in the file templates/tweet.html
    tweet_text = 'this is some test test #' + str(tweet_id) 
    return render_template('tweet.html', user_url=user_url, username=username,
                           tweet=tweet_text)

if __name__ == "__main__":
    if run_on_public_interface:
        app.run(debug=True,host='0.0.0.0')
    else:
        app.run()
