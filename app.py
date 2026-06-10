"""
JANOS Academy Web Application
A Flask-based web version of the interactive quiz game
"""

from flask import Flask, render_template, request, jsonify, session
from functools import wraps
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

PASS_SCORE = 35

# Question data for all classes
QUIZ_DATA = {
    "algebra": {
        "title": "Algebra",
        "description": "Test your algebra skills with equation solving!",
        "questions": [
            {"prompt": "Solve: 2x = 10:", "answer": 5, "points": 10},
            {"prompt": "Solve: x + 7 = 12:", "answer": 5, "points": 10},
            {"prompt": "Solve: 3x = 21:", "answer": 7, "points": 10},
            {"prompt": "Solve: x - 4 = 6:", "answer": 10, "points": 10},
            {"prompt": "Solve: 5x = 25:", "answer": 5, "points": 10},
        ]
    },
    "english": {
        "title": "English",
        "description": "Enhance your English language knowledge!",
        "questions": [
            {
                "prompt": "Synonym of 'happy':",
                "answer": ["glad", "joyful", "cheerful", "content", "pleased", "elated",
                          "overjoyed", "thrilled", "ecstatic", "delighted", "serene",
                          "satisfied", "fulfilled", "at ease", "giddy", "buoyant",
                          "sunny", "upbeat", "jubilant", "festive", "merry"],
                "points": 10
            },
            {"prompt": "Antonym of 'big':", "answer": "small", "points": 10},
            {"prompt": "Plural of 'child':", "answer": "children", "points": 10},
            {"prompt": "Correct spelling (recieve or receive):", "answer": "receive", "points": 10},
            {"prompt": "Opposite of 'fast':", "answer": "slow", "points": 10},
        ]
    },
    "oceanography": {
        "title": "Oceanography",
        "description": "Explore the wonders of the ocean!",
        "questions": [
            {"prompt": "What is the largest ocean:", "answer": "pacific", "points": 10},
            {"prompt": "Salt water covers about what % of the earth:", "answer": 70, "points": 10},
            {"prompt": "What is the world's deepest trench:", "answer": "mariana", "points": 10},
            {"prompt": "What do sea animals breathe with:", "answer": "gills", "points": 10},
            {"prompt": "Which tool is used to measure water depth:", "answer": "sonar", "points": 10},
        ]
    },
    "history": {
        "title": "History",
        "description": "Journey through historical events!",
        "questions": [
            {"prompt": "First US President:", "answer": "george washington", "points": 10},
            {"prompt": "Where is the Great Wall located:", "answer": "china", "points": 10},
            {"prompt": "When did the US gain independence:", "answer": 1776, "points": 10},
            {"prompt": "When did the Civil War end:", "answer": 1865, "points": 10},
            {"prompt": "Where are the Pyramids located:", "answer": "egypt", "points": 10},
        ]
    },
    "health": {
        "title": "Health",
        "description": "Learn about human anatomy and wellness!",
        "questions": [
            {"prompt": "How many bones are in the adult body:", "answer": 206, "points": 10},
            {"prompt": "Which organ pumps blood throughout the body:", "answer": "heart", "points": 10},
            {"prompt": "What does BMI stand for:", "answer": "body mass index", "points": 10},
            {"prompt": "What are muscles connected by:", "answer": "tendons", "points": 10},
            {"prompt": "What do we breathe in:", "answer": "oxygen", "points": 10},
        ]
    }
}


def check_answer(user_answer, correct_answer):
    """Check if user answer matches correct answer (handles strings, ints, and lists)"""
    # Handle list answers (multiple correct answers)
    if isinstance(correct_answer, list):
        user_lower = str(user_answer).lower().strip()
        return user_lower in [str(ans).lower() for ans in correct_answer]
    
    # Handle integer answers
    if isinstance(correct_answer, int):
        try:
            return int(user_answer) == correct_answer
        except (ValueError, TypeError):
            return False
    
    # Handle string answers
    return str(user_answer).lower().strip() == str(correct_answer).lower().strip()


@app.route('/')
def index():
    """Home page with class selection"""
    session.clear()
    return render_template('index.html', classes=QUIZ_DATA)


@app.route('/quiz/<class_name>')
def quiz(class_name):
    """Start a quiz for a specific class"""
    if class_name not in QUIZ_DATA:
        return "Class not found", 404
    
    session['current_class'] = class_name
    session['current_question'] = 0
    session['score'] = 0
    
    class_data = QUIZ_DATA[class_name]
    return render_template('quiz.html', 
                          class_name=class_name,
                          title=class_data['title'],
                          total_questions=len(class_data['questions']))


@app.route('/api/question/<class_name>')
def get_question(class_name):
    """Get the current question"""
    if class_name not in QUIZ_DATA:
        return jsonify({"error": "Class not found"}), 404
    
    current_q = session.get('current_question', 0)
    questions = QUIZ_DATA[class_name]['questions']
    
    if current_q >= len(questions):
        return jsonify({"error": "Quiz complete"}), 400
    
    question = questions[current_q]
    return jsonify({
        "question_number": current_q + 1,
        "total_questions": len(questions),
        "prompt": question['prompt'],
        "points": question['points']
    })


@app.route('/api/submit-answer', methods=['POST'])
def submit_answer():
    """Submit an answer and get feedback"""
    data = request.json
    class_name = data.get('class_name')
    user_answer = data.get('answer')
    
    if class_name not in QUIZ_DATA:
        return jsonify({"error": "Class not found"}), 404
    
    current_q = session.get('current_question', 0)
    questions = QUIZ_DATA[class_name]['questions']
    
    if current_q >= len(questions):
        return jsonify({"error": "Quiz complete"}), 400
    
    question = questions[current_q]
    correct = check_answer(user_answer, question['answer'])
    
    # Update score
    if correct:
        session['score'] = session.get('score', 0) + question['points']
        points_earned = question['points']
    else:
        session['score'] = max(0, session.get('score', 0) - 5)
        points_earned = -5
    
    # Move to next question
    session['current_question'] = current_q + 1
    session.modified = True
    
    # Check if quiz is complete
    quiz_complete = session['current_question'] >= len(questions)
    
    return jsonify({
        "correct": correct,
        "correct_answer": question['answer'] if isinstance(question['answer'], list) else str(question['answer']),
        "points_earned": points_earned,
        "current_score": session['score'],
        "quiz_complete": quiz_complete,
        "next_question_number": session['current_question'] + 1
    })


@app.route('/results/<class_name>')
def results(class_name):
    """Display quiz results"""
    if class_name not in QUIZ_DATA:
        return "Class not found", 404
    
    score = session.get('score', 0)
    passed = score >= PASS_SCORE
    
    class_data = QUIZ_DATA[class_name]
    
    return render_template('results.html',
                          class_name=class_name,
                          title=class_data['title'],
                          score=score,
                          pass_score=PASS_SCORE,
                          passed=passed)


@app.route('/leaderboard')
def leaderboard():
    """Display a simple leaderboard page"""
    return render_template('leaderboard.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
