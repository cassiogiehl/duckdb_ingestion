from flask import Flask, request, render_template
import os

app = Flask(__name__, template_folder='views')

@app.route('/')
def read_csv():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def save_file():
    file = request.files['csv_file']
    filename = file.filename
    filepath = os.path.join('data/upload/csv', filename)
    file.save(filepath)
    return render_template("index.html")
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)
