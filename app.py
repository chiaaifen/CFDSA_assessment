from flask import Flask, render_template, redirect
import random

app = Flask(__name__)

# Sample list of texts to display
texts = [
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "There are 10 kinds of people. Those who know binary and those who don't.",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
    "It's not that I'm so smart, it's just that I stay with problems longer.",
    "It is pitch dark. You are likely to be eaten by a grue."
]

@app.route('/')
def index():
    # Select a random text from the list
    selected_text = random.choice(texts)
    return render_template('index.html', text=selected_text)

@app.route('/go_outside_flask')
def go_outside_flask_method():
    return redirect("https://github.com/chiaaifen/CFDSA_assessment", code=302)

if __name__ == '__main__':
	app.run(debug=True)
