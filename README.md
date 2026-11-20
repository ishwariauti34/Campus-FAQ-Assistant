# Campus FAQ Assistant

## About the Project
Campus FAQ Assistant is a simple web-based chatbot designed to answer frequently asked questions about college information.

Students can type questions or select suggested questions to receive quick responses about different college services.

## Features
- Interactive chatbot interface
- Answers questions about college facilities and services
- Suggested questions for quick access
- Clear Chat option
- Displays sender names and message timestamps
- Supports pressing Enter to send a message
- Responsive design

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript

## FAQ Categories
The chatbot currently supports questions related to:
- Admissions
- Fees
- Library
- Examinations
- Timetable
- Hostel
- Scholarships
- Contact Information
- Attendance
- Documents
- Placements
- Transportation
- Student ID Cards

## How to Run the Project

### 1. Install Python
Make sure Python is installed on your computer.

### 2. Install Flask

Open the terminal in the project folder and run:

```bash
py -m pip install flask
```

### 3. Run the Application

Execute:

```bash
py app.py
```

### 4. Open in Browser

Visit:

http://127.0.0.1:5000

## Project Structure

```text
Campus_FAQ_Assistant/
│
├── app.py
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## How It Works
The application uses Flask as its backend. When a student submits a question, JavaScript sends it to the Flask application. The Python program checks the question against predefined keywords and returns the matching FAQ response.

## Future Improvements
- Add more college-related questions and answers.
- Connect the chatbot to a database.
- Add an admin panel to manage FAQs.
- Improve question matching.

## Author
Student Project – Campus FAQ Assistant
