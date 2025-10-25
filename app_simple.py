from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# In-memory storage for testing
languages_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        if not data or 'language' not in data:
            return jsonify({'error': 'No language provided'}), 400
        
        language = data['language']
        if not isinstance(language, str) or not re.match(r'^[a-zA-Z+#\-\s]+$', language):
            return jsonify({'error': 'Invalid language format'}), 400
        
        language = language.strip()[:50]
        
        if language in languages_data:
            languages_data[language] += 1
        else:
            languages_data[language] = 1
        
        return jsonify({'message': 'Success'}), 200
    except Exception as e:
        return jsonify({'error': 'Server error'}), 500

@app.route('/languages', methods=['GET'])
def get_languages():
    try:
        return jsonify(languages_data)
    except Exception as e:
        return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)