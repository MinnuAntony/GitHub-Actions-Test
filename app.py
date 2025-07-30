
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

expenses = []

html = """
<!doctype html>
<html>
<head>
    <title>Expense Tracker</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

<h1>My Expenses</h1>
<ul>
{% for expense in expenses %}
    <li>{{ expense.date }} - {{ expense.description }}: ₹{{ expense.amount }}</li>
{% endfor %}
</ul>

<h2>Add New Expense</h2>
<form method="post" action="/add">
    Date: <input type="date" name="date" required><br>
    Description: <input type="text" name="description" required><br>
    Amount: <input type="number" name="amount" required><br>
    <input type="submit" value="Add Expense">
</form>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html, expenses=expenses)

@app.route('/add', methods=['POST'])
def add():
    date = request.form['date']
    description = request.form['description']
    amount = request.form['amount']
    expenses.append({
        "date": date,
        "description": description,
        "amount": amount
    })
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

