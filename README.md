 # Candidate Job Matching System
 ### A Recommendation System using Machine Learning Techniques to match candidates to job openings

## Project Overview

This project aims to recommend job openings to candidates based on the similarity between their resume and job descriptions. It utilizes text extraction, TF-IDF vectorization, and cosine similarity to find the best matches for a candidate's profile.

## Features

- Extract text from candidate resume PDF files.
- Vectorize job descriptions and resumes using TF-IDF.
- Calculate similarity scores between resumes and job descriptions.
- Filter and rank job openings based on candidate preferences and similarity scores.
- Web interface for uploading resumes and viewing matched jobs.

## Technologies Used

- Python
- Flask
- PyMuPDF (fitz)
- scikit-learn
- pandas

## Explanation of Methods Used in Candidate Matching Project

### 1. Text Extraction from PDF:

* Library: PyMuPDF (fitz).
* Function: extract_text_from_pdf(pdf_path)
 * Input: Path to the PDF file.
 * Process: Opens the PDF and iterates through each page, extracting the text.
 * Output: Combined text from all pages in the PDF.

### 2. TF-IDF Vectorization:

* Library: scikit-learn (TfidfVectorizer).
* Function: Part of the recommend_jobs function.
* Input: Job descriptions from the dataset and candidate resume text.
* Process: Converts text data into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency) to reflect the importance of terms.
* Output: Numerical vectors representing job descriptions and candidate resume.

### 3. Cosine Similarity Calculation:

* Library: scikit-learn (cosine_similarity).
* Function: Part of the recommend_jobs function.
* Input: TF-IDF vectors of job descriptions and candidate resume.
* Process: Calculates the cosine similarity between the candidate resume vector and each job description vector.
* Output: Similarity scores.

### 4. Job Matching Based on Preferences and Similarity:

* Function: recommend_jobs(candidate_resume_path, jobs_df, candidate_preferences)
* Input: Path to the candidate resume, job openings dataset, and candidate preferences.
* Process:
   1. Extract text from the resume.
   2. Vectorize job descriptions and resume text.
   3. Calculate similarity scores.
   4. Filter jobs based on location and similarity threshold.
   5. Sort jobs by similarity score.
* Output: DataFrame of matched jobs with relevant details and similarity scores.

### 5. Flask Web Application:

* Library: Flask.
* Route: upload_file()
* GET Method: Renders the file upload page.
* POST Method:
   - Handles file upload.
   - Saves the uploaded file temporarily.
   - Calls recommend_jobs to process the file and get matched jobs.
   - Deletes the temporary file.
   - Renders the results page with matched jobs.

## Features and Results:

### 1. Home Page
![image](https://github.com/Pacchu04/Candidate-Matching-App/assets/92878457/3f1ed005-d623-458c-b823-ef29a169a4da)

### 2. Result 
![image](https://github.com/Pacchu04/Candidate-Matching-App/assets/92878457/7cccd2d8-76d9-4438-b86e-db91aa5c3a16)


## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Pacchu04/Candidate-Matching-App.git
    cd candidate-job-matching
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Prepare the job openings dataset**:
    - Place your `job_final.csv` file in the root directory of the project.

## Running the Application

1. **Start the Flask application**:
    ```bash
    python app.py
    ```

2. **Open your web browser and go to**: `http://127.0.0.1:5000`

3. **Upload a candidate resume** and view the matched job openings.

## Project Structure

- `app.py`: Main application file containing Flask routes and core logic.
- `templates/`: Directory containing HTML templates for file upload and results pages.
- `job_final.csv`: Job openings dataset (should be provided by the user).
- `requirements.txt`: List of dependencies required for the project.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Acknowledgments

- Inspired by various job matching and recommendation systems.
- Special thanks to the open-source community for providing useful libraries and tools.


