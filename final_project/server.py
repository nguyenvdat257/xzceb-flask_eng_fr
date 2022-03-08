from flask import Flask, render_template, request
import machinetranslation
import json

app = Flask("Web Translator")


@app.route("/englishToSpanish")
def englishToSpanish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = machinetranslation.translator.english_to_french(textToTranslate)
    return translated_text


@app.route("/spanishToEnglish")
def spanishToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = machinetranslation.translator.french_to_english(textToTranslate)
    return translated_text


@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8080)
    # app.run(host="0.0.0.0", port=8080)
    app.run(debug=True)
