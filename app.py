from flask import Flask, request, render_template
import pandas as pd
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Sample candidate preferences (can be extended)
candidate_preferences = {
    'Location': 'Bengaluru',
    # Other preferences like position, company, etc.
}

# Load job openings dataset
jobs_df = pd.read_csv('job_final.csv')

# Function to recommend jobs based on a candidate's resume
def recommend_jobs(candidate_resume_path, jobs_df, candidate_preferences):
    # Extract text from candidate's resume PDF
    candidate_resume_text = extract_text_from_pdf(candidate_resume_path)
    
    # Preprocess job descriptions
    vectorizer = TfidfVectorizer(stop_words='english')
    job_descriptions = vectorizer.fit_transform(jobs_df['Job_Description'].values.astype('U'))
    
    # Preprocess candidate resume
    candidate_desc = vectorizer.transform([candidate_resume_text])
    
    # Calculate similarity between candidate resume and job descriptions
    similarity_scores = cosine_similarity(job_descriptions, candidate_desc)
    
    # Combine similarity scores with job openings
    jobs_df['SimilarityScore'] = similarity_scores
    
    # Filter job openings based on candidate preferences
    matched_jobs = jobs_df[(jobs_df['Location'] == candidate_preferences['Location']) & (jobs_df['SimilarityScore'] > 0.1)]
    
    # Sort matched jobs by similarity score (optional)
    matched_jobs = matched_jobs.sort_values(by='SimilarityScore', ascending=False)
    
    return matched_jobs[['Position', 'Company', 'Location', 'Job_Description', 'SimilarityScore']]

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            # Save the uploaded file to a temporary location
            temp_path = os.path.join('temp', file.filename)
            file.save(temp_path)
            
            # Process the file and get matched jobs
            matched_jobs = recommend_jobs(temp_path, jobs_df, candidate_preferences)
            
            # Delete the temporary file
            os.remove(temp_path)
            
            return render_template('results.html', tables=[matched_jobs.to_html(classes='data')], titles=matched_jobs.columns.values)
    return render_template('upload.html')

if __name__ == '__main__':
    os.makedirs('temp', exist_ok=True)
    app.run(debug=True)
