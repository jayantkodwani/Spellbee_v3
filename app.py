from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# List of words for the spelling bee practice
word_list = ["ship", "gems", "tank","egg","escalator","lion","apple","speech","trophy","dubai","triumph","television","phone","mobile","toy","tower","car","bike","hut","school","cycle","cat","tiger","play","plant","google","block","pizza","burger","tea","glass","wood","lamp","lego","cop","book","pen","blanket","puzzle"]

# Route to serve the web page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get a random word
@app.route('/get_word')
def get_word():
    word = random.choice(word_list)
    return jsonify({"word": word})

if __name__ == '__main__':
    app.run(debug=True)
    
#if __name__ == '__main__':
    # Bind to all interfaces (0.0.0.0) and use the port defined in the environment variable, default to 8000
 #   import os
    #port = int(os.environ.get('PORT', 8000))
  #  app.run()
    #app.run(host='0.0.0.0', port=port)
