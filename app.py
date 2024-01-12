from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
async def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
async def predict():
    file = request.files['file']

if __name__ == '__main__':
    app.run(debug=True)
