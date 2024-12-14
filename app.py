from flask import Flask, render_template, request, jsonify
from transformers import pipeline
from multiprocessing import freeze_support

app = Flask(__name__)

# Initialize translation pipeline
def load_translator():
    return pipeline("translation", model="Helsinki-NLP/opus-mt-en-fi")

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/translate', methods=['POST'])
def translate():
    text = request.json['text']
    # the translator(text) return a array which has only one element, which a disctionary with key 'translation_text'
    # print(translator(text));
    translation = translator(text)[0]['translation_text']
    return jsonify({'translation': translation})

if __name__ == '__main__':
    ## might need to uncomment this if running into issues on Windows, in order to run in different platforms
    # freeze_support()
    translator = load_translator()
    app.run(debug=True)

