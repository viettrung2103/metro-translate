### ENG-FIN TRANSLATOR

## Description
- This app is a translator app, which translates words/ sentences/ paragraphs from English to Finnish.
## How it work
- By using the [Helsinki-NLP/opus-mt-en-fi ](https://huggingface.co/Helsinki-NLP/opus-mt-en-fi) pipeline from the [HuggingFace](https://huggingface.co/)
- The user will type in the words/sentences/paragraphs that the user wants to translate.
- The app will input that text into the pipeline
- The result result is a array that has one element. This element is a dictionary, and the translated result is the value of this dictionary
- The translated result is then displayed in the browser.

## How to set up
- Clone this repository to your machine
- cd to this repository's folder in your machine.
- Run the following commands in the terminal
  - `pip install -r requirements.txt`
  - `python app.py`

