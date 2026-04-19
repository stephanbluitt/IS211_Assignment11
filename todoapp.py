from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Global list to store To-Do items
todo_list = []

# Email validation (simple regex)
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# ---------------------------
# Main Controller ('/')
# ---------------------------
@app.route('/')
def index():
    return render_template('index.html', todos=todo_list)

# ---------------------------
# Submit Controller ('/submit')
# ---------------------------
@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get('task')
    email = request.form.get('email')
    priority = request.form.get('priority')

    # Validation
    if not task or not email or not priority:
        return redirect(url_for('index'))

    if not is_valid_email(email):
        return redirect(url_for('index'))

    if priority not in ['Low', 'Medium', 'High']:
        return redirect(url_for('index'))

    # Add item
    todo_list.append({
        'task': task,
        'email': email,
        'priority': priority
    })

    return redirect(url_for('index'))

# ---------------------------
# Clear Controller ('/clear')
# ---------------------------
@app.route('/clear', methods=['POST'])
def clear():
    global todo_list
    todo_list = []
    return redirect(url_for('index'))

# ---------------------------
# Run App
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)
