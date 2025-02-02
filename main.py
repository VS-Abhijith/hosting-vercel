from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Load the data from the JSON file
json_file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
with open(json_file_path) as f:
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
