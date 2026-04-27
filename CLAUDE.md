# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Quiz HTML Slide Generator — a Flask web app that reads Excel files containing quiz questions and generates timed HTML presentation slides. Users select topics, set per-question timer duration, and navigate through slides with keyboard/button controls.

## Running the Application

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Application Flow

1. **Upload** (`/`) — User uploads an Excel file with quiz data
2. **Topic Selection** (`/upload` POST) — Shows all unique topics from the file; user selects which topics to include and how many questions per topic
3. **Quiz** (`/generate` POST) — Renders the quiz slide template with timed questions
4. **Answers** (final slide) — Shows all correct answers after the last question

## Architecture

**Flask Routes (app.py)**
- `GET /` — renders `index.html`
- `POST /upload` — parses Excel, extracts topics, renders `select_topics.html`
- `POST /generate` — filters questions by selected topics, renders `quiz.html`

**Templates**
- `templates/index.html` — file upload form
- `templates/select_topics.html` — topic/timer configuration form
- `templates/quiz.html` — the quiz slide UI (heavily styled, includes all JS for timer/navigation logic client-side)

**Data Flow**
Excel → pandas DataFrame → JSON (hidden form field) → `/generate` route → Flask renders quiz.html with questions/answers passed as template variables.

**Excel Expected Columns** (14 total): Subject Code, Description, Exam Period, Learning Outcome, Topic, QUESTION, Type of Question, Taxonomy, Choice A, Choice B, Choice C, Choice D, Answer, Correct answer in Words

## Dependencies

- flask
- pandas
- openpyxl

## File Structure

```
Quiz HTML Maker/
├── app.py                  # Flask app with 3 routes
├── requirements.txt       # Dependencies
├── uploads/               # Temporary file storage (git-ignored)
└── templates/
    ├── index.html         # Upload page
    ├── select_topics.html # Topic selection page
    └── quiz.html          # Quiz presentation slides
```