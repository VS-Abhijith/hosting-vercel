from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load the data from the JSON file
with open('q-vercel-python.json') as f:
    data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = []
    for name in names:
        mark = next((student['marks'] for student in data if student['name'] == name), None)
        marks.append(mark)
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run()
