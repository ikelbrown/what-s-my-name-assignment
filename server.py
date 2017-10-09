from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    {{#name = request.form['name']}}
    return redirect('/')

app.run(debug=True)