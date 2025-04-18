from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import whisper
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = whisper.load_model("base")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word')
def get_word():
    import random
    word_list = ["ship", "gems", "tank","egg","escalator","lion","apple","speech","trophy","dubai","triumph","television","phone","mobile","toy","tower","car","bike","hut","school","cycle","cat","tiger","play","plant","google","block","pizza","burger","tea","glass","wood","lamp","lego","cop","book","pen","blanket","puzzle"]
    
    return jsonify({"word": random.choice(word_list)})

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file'}), 400

    file = request.files['audio']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    result = model.transcribe(filepath)
    os.remove(filepath)

    return jsonify({'transcription': result['text']})

if __name__ == '__main__':
    app.run(debug=True)
