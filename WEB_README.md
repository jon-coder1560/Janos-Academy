# Flask Web Version - JANOS Academy

A modern web-based version of the JANOS Academy quiz game built with Flask and Jinja2.

## Features

✨ **Interactive Web Interface**
- Beautiful gradient-themed design
- Responsive layout for all devices
- Real-time score tracking
- Progress bar for quiz completion
- Instant feedback on answers

🎯 **All Original Classes**
- Algebra
- English
- Oceanography
- History
- Health

📊 **Quiz Mechanics**
- +10 points for correct answers
- -5 points for incorrect answers
- 35 points needed to pass
- Retry any class unlimited times
- Results page with pass/fail status

## Installation

1. **Clone or navigate to the repository**
   ```bash
   cd Janos-Academy
   ```

2. **Install Flask**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the web app**
   Open your browser and go to:
   ```
   http://localhost:5000
   ```

## File Structure

```
Janos-Academy/
├── app.py                 # Flask application and routes
├── templates/
│   ├── base.html         # Base template with styling
│   ├── index.html        # Home page with class selection
│   ├── quiz.html         # Quiz interface
│   ├── results.html      # Results page
│   └── leaderboard.html  # Leaderboard page (coming soon)
└── school.py             # Original console version
```

## How to Use

1. **Start the quiz** - Click on any subject from the home page
2. **Answer questions** - Type your answer and click Submit (or press Enter)
3. **Get feedback** - See if you're correct or incorrect immediately
4. **View results** - After 5 questions, see your final score and pass/fail status
5. **Retry** - Choose to retry the same class or select a different one

## Scoring System

- **Correct Answer**: +10 points
- **Incorrect Answer**: -5 points
- **Pass Score**: 35 points minimum
- **Perfect Score**: 50 points (5 questions × 10 points each)

## Technical Stack

- **Backend**: Python with Flask web framework
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Session Management**: Flask sessions for tracking progress
- **API**: RESTful endpoints for quiz operations

## Future Enhancements

- User authentication and accounts
- Leaderboard with personal records
- Achievement badges
- More subjects
- Difficulty levels
- Timed quizzes
- Export scores as PDF

## License

MIT License - Feel free to use, modify, and expand for educational or personal purposes.
