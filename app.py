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
            {'$count': 1}
        )
    else:
        languages_collection.insert_one({'name': language, 'count': 1})

    return jsonify({'message': 'Success'}), 200


@app.route('/languages', methods=['GET'])
def get_languages():
    pipeline = [
        {'$group': {'_id': '$language', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}}
    ]
    result = list(languages_collection.aggregate(pipeline))
    data = {doc['_id']: doc['count'] for doc in result if doc['_id'] is not None}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
