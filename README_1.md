# Git & GitHub - DevOps Assignment

Name: Aditya Kundu
Course: TutDude DevOps
Tools used: Git, GitHub (SSH), VS Code, PowerShell, Python 3, Flask, MongoDB Atlas

GitHub repo: https://github.com/kunduaditya758-prog/Git_and_GitHub_AdityaKundu

## About
In this assignment I practised the full Git workflow on my Flask project:
- cloning a GitHub repository with SSH
- creating branches and merging them (fast-forward and 3-way merge)
- creating and resolving a merge conflict
- parallel feature work on two branches (frontend To-Do page and backend API)
- separate commits for each change, git reset --soft, and git rebase

## Branches
- main - final code
- AdityaKundu - first branch with the Flask project files (Task 1)
- AdityaKundu_new - updated JSON data for /api (Task 2)
- master_1 - To-Do page and the Item ID, Item UUID and Item Hash fields (Task 3 and 4)
- master_2 - /submittodoitem backend route (Task 3)

## Files
- app.py - Flask app with /api, the details form, /todo and /submittodoitem
- data.json - data file used by /api
- templates/form.html - details form (name and email)
- templates/success.html - success page
- templates/todo.html - To-Do form
- requirements.txt - libraries needed
- .env.example - format of the MongoDB connection string
- .gitignore - keeps .env out of GitHub
- Git_and_GitHub_AdityaKundu.docx - commands, screenshots and explanation of every task

## How to run
1. Copy .env.example to .env and put your own MongoDB Atlas connection string in it.
2. Install the libraries:
```
pip install -r requirements.txt
```
3. Start the app:
```
python app.py
```
4. Open these pages:
- http://127.0.0.1:5000/api - JSON list
- http://127.0.0.1:5000/todo - To-Do form, saves items in the todo_items collection

The real .env file is not uploaded because it has the database password.
