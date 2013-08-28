from flask import Flask
app = Flask(__name__)

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
    return 'tweet_id %d' % tweet_id

if __name__ == "__main__":
    if run_on_public_interface:
        app.run(host='0.0.0.0')
    else:
        app.run()
