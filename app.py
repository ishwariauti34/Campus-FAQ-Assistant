
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# College FAQ Database
faqs = {

    "admission": {
        "keywords": ["admission", "apply", "enrollment", "eligibility"],
        "answer": "For admission information and eligibility criteria, please contact the college admission office."
    },

    "fees": {
        "keywords": ["fees", "fee", "payment", "tuition"],
        "answer": "For details about tuition fees and payment methods, please contact the accounts department."
    },

    "library": {
        "keywords": ["library", "books", "book", "reading"],
        "answer": "For library timings and book availability, please contact the college library."
    },

    "exams": {
        "keywords": ["exam", "examination", "result", "marks", "semester"],
        "answer": "For examination schedules and results, please check the college examination notice."
    },

    "timetable": {
        "keywords": ["timetable", "schedule", "class", "lecture"],
        "answer": "Please check your department notice board or student portal for the latest timetable."
    },

    "hostel": {
        "keywords": ["hostel", "accommodation", "room"],
        "answer": "For hostel availability and accommodation details, please contact the college hostel office."
    },

    "scholarship": {
        "keywords": ["scholarship", "financial aid", "scholarships"],
        "answer": "For scholarship information and eligibility, please contact the college scholarship department."
    },

    "contact": {
        "keywords": ["contact", "phone", "email", "office"],
        "answer": "You can contact the college administrative office for assistance."
    },

    "attendance": {
        "keywords": ["attendance", "absent", "present"],
        "answer": "For attendance records and attendance requirements, please contact your department."
    },

    "documents": {
        "keywords": ["documents", "certificate", "marksheet", "document"],
        "answer": "For information about required documents, please contact the college admission office."
    },

    "placement": {
        "keywords": ["placement", "placements", "job", "recruitment"],
        "answer": "For placement opportunities and recruitment information, please contact the college placement cell."
    },

    "transport": {
        "keywords": ["transport", "bus", "bus facility"],
        "answer": "For college bus routes and transport facilities, please contact the college transport department."
    },

    "id_card": {
        "keywords": ["id card", "identity card", "student card"],
        "answer": "For a new or replacement student ID card, please contact the college administration office."
    }

}


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Chatbot Question Handler
@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get("question", "").lower().strip()

    if not question:
        return jsonify({
            "answer": "Please enter a question."
        })

    # Find matching FAQ
    for faq in faqs.values():

        for keyword in faq["keywords"]:

            if keyword in question:

                return jsonify({
                    "answer": faq["answer"]
                })

    # Default Response
    return jsonify({
        "answer": "Sorry, I don't have an answer for that question. Please contact your college office."
    })


# Run Application
if __name__ == "__main__":
    app.run(debug=True)
