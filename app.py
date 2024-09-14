from flask import Flask, request, jsonify, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home route for uploading text file
@app.route('/')
def home():
    return render_template('index.html')

# Upload text file route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file found", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return "File uploaded successfully", 200

# Data analysis and visualization route
@app.route('/analyze', methods=['POST'])
def analyze():
    file_path = os.path.join(UPLOAD_FOLDER, os.listdir(UPLOAD_FOLDER)[0])  # Get the first uploaded file
    try:
        with open(file_path, 'r') as f:
            content = f.readlines()

        # Example analysis: count lines and words
        num_lines = len(content)
        num_words = sum(len(line.split()) for line in content)

        # Visualization: Word count histogram
        word_counts = [len(line.split()) for line in content]
        img = io.BytesIO()
        plt.hist(word_counts, bins=range(max(word_counts) + 1))
        plt.xlabel('Number of Words')
        plt.ylabel('Frequency')
        plt.title('Word Count Histogram')
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        stats = {
            'Number of Lines': num_lines,
            'Number of Words': num_words
        }

        return render_template('analysis.html', stats=stats, plot_url=plot_url)
    except Exception as e:
        return str(e), 500

# Load Sample Data
@app.route('/load_sample', methods=['GET'])
def load_sample():
    sample_file_path = os.path.join(UPLOAD_FOLDER, 'sample_data.txt')
    if not os.path.exists(sample_file_path):
        return "Sample data not found", 404

    return send_file(sample_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
