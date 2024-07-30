from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import threading
from similarity import get_similarity_matrix, recommend_spaces
import os

app = Flask(__name__)
CORS(app)


@app.route('/recommendations/<int:emp_id>', methods=['GET'])
def get_recommendations(emp_id):
    similarity_matrix, emp_ids, employee_spaces, = get_similarity_matrix()
    recommendations = recommend_spaces(emp_id, similarity_matrix, emp_ids, employee_spaces)
    return jsonify(recommendations)


@app.route('/')
def serve_index():
    return send_from_directory('templates', 'index.html')


def run_flask():
    app.run(port=5002)


if __name__ == "__main__":
    thread = threading.Thread(target=run_flask)
    thread.start()
