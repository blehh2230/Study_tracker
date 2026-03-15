# Smart Study Tracker 📚

A simple command-line based study tracker built using Python.
This program allows users to record study sessions, track their progress using an XP and level system, and maintain study streaks.

This project stores data using a JSON file, making it easy to save and retrieve study history.

## Features 🚀

* Record study sessions with subject and duration
* XP system to gamify studying
* Automatic level calculation
* Track total study hours
* Identify the most studied subject
* Maintain current and longest study streaks
* Data persistence using JSON
* Simple command-line interface

## Project Structure 📂

```
study_tracker
│
├── study_tracker.py   # Main Python program
├── data.json          # Stores all study data
└── README.md          # Project documentation
```

## How It Works ⚙️

When the program runs, the user is presented with a menu:

```
1. Start Study Session
2. View Statistics
3. View Streaks
4. Exit
```

### 1. Start Study Session

* User enters subject name and study duration.
* XP is awarded based on study time.

```
XP Earned = duration // 10
```

* Study session is saved in the JSON file.

---

### 2. View Statistics

Displays:

* Total hours studied
* Total XP earned
* Current level
* Total study sessions
* Most studied subject

---

### 3. View Streaks

Tracks study consistency:

* Current streak (consecutive study days)
* Longest streak

The streak is updated based on the difference between today's date and the last recorded study session.

---

## Example Output 💻

```
Welcome to Study Tracker!!

1. Start Study Session
2. View Statistics
3. View Streaks
4. Exit
```

Example statistics:

```
Total hours studied: 5
Total XP earned: 120
Current Level: 2
Total number of sessions completed: 4
Most studied subject is: Python
```

Example streak output:

```
Your study streak:
Current streak: 3 days
Longest streak: 5 days
```


## Technologies Used 🛠

* Python
* JSON
* datetime module


## Future Improvements 🌟

Possible improvements for the project:

* Add recent session history
* Add graphical statistics
* Build a GUI version
* Add weekly/monthly study reports
* Add reminders or timers

## Author ✍️

Created by **Risha Deepak** as a Python practice mini-project.
