# JANOS Academy

JANOS Academy is an interactive terminal‑based quiz game where players choose from five school subjects and complete short quizzes to test their knowledge. Each class contains five questions worth ten points each, and players must score at least 35 points to pass. The program includes retry options, scoring summaries, and a reusable quiz engine that makes adding new subjects simple.

---

## Features

### Available Subjects
- Algebra  
- English  
- Oceanography  
- History  
- Health  

### Quiz System
All subjects use a shared quiz engine that:
- Displays questions  
- Checks answers  
- Awards points  
- Applies penalties  
- Shows a final score summary  
- Allows retrying the class  
- Returns to the main menu  

### Scoring
- **+10 points** for each correct answer  
- **–5 points** for incorrect answers  
- **35 points** required to pass  

### User Experience
- Clean screen transitions  
- Friendly prompts  
- Retry options  
- Easy navigation  

---

## How to Run

1. Install Python 3.
2. Save the program as:

```
janos_academy.py
```

3. Run it from your terminal:

```
python janos_academy.py
```

---

## Project Structure
```
janos_academy.py
README.md
```

---

## Adding New Classes

To add a new subject, create a list of question dictionaries and pass it to:

```
python
run_quiz("Class Name", questions)
```
Each question uses this format:
```
{
    "prompt": "Your question here:",
    "answer": correct_answer,
    "points": 10
}
```

You can use:

- strings

- integers

- lists (for multiple acceptable answers)

# License
This project is free to use, modify, and expand for educational or personal purposes.
