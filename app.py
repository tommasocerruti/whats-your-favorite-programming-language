from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['languagesDB']
languages_collection = db['languages']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    language = request.json.get('language')
    if not language:
        return jsonify({'error': 'No language provided'}), 400

    existing_language = languages_collection.find_one({'name': language})

    if existing_language:
        languages_collection.update_one(
            {'name': language},
            {'$inc': {'count': 1}}
        )
    else:
        languages_collection.insert_one({'name': language, 'count': 1})

    return jsonify({'message': 'Success'}), 200

@app.route('/languages', methods=['GET'])
def get_languages():
    languages = languages_collection.find()
    data = {}
    for lang in languages:
        if 'name' in lang and 'count' in lang:
            data[lang['name']] = lang['count']
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
