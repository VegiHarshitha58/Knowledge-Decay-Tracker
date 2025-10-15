from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from datetime import datetime, timedelta
import os
import json # New import for persistence

# --- Configuration and Persistence Setup ---
DATA_FILE = "data.json"

def load_data():
    """Loads employee data from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    # Default sample data if file doesn't exist (NOTE: Added decay_days to employee)
    return [
        {
            "id": 1,
            "name": "Harshitha",
            "role": "IT Support Engineer",
            "decay_days": 60, # Higher decay threshold for junior roles
            "join_date": "2023-05-01",
            "problems_solved": [
                {"problem": "Server Down", "solution": "Restarted Apache Service", "last_used": "2025-06-01"},
                {"problem": "Network Latency", "solution": "Reconfigured DNS", "last_used": "2025-05-20"}
            ]
        },
        {
            "id": 2,
            "name": "Kiran",
            "role": "SME | Senior MSP Engineer",
            "decay_days": 30, # Lower decay threshold for critical senior roles
            "join_date": "2024-02-10",
            "problems_solved": [
                {"problem": "Email Outage", "solution": "Reset SMTP configuration", "last_used": "2025-07-12"}
            ]
        }
    ]

def save_data(data):
    """Saves employee data back to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

employees = load_data()

# --- Flask App Setup ---
app = Flask(__name__, static_folder="../frontend")
CORS(app)

# Serve frontend index.html and static files (No change here)
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# --- API Endpoints ---

# Get all employees
@app.route('/employees')
def get_employees():
    return jsonify(employees)

# Check knowledge decay (Updated with configurable decay_days)
@app.route('/knowledge_decay')
def check_decay():
    today = datetime.now()
    decay_alerts = []

    for emp in employees:
        decay_threshold = timedelta(days=emp.get("decay_days", 60)) # Use role-based days
        for i, p in enumerate(emp["problems_solved"]):
            last_used = datetime.strptime(p["last_used"], "%Y-%m-%d")
            if today - last_used > decay_threshold:
                decay_alerts.append({
                    "employee": emp["name"],
                    "emp_id": emp["id"],
                    "problem_index": i, # Index is needed to target for revisit
                    "problem": p["problem"],
                    "threshold_days": emp.get("decay_days", 60),
                    "message": f"Knowledge on '{p['problem']}' (Role Threshold: {emp.get('decay_days', 60)} days) may have decayed. Please revisit."
                })
    return jsonify(decay_alerts)

# Add a problem for an employee (No change, but now saves data)
@app.route('/add_problem', methods=['POST'])
def add_problem():
    data = request.json
    emp_id = data.get("id")
    for emp in employees:
        if emp["id"] == emp_id:
            emp["problems_solved"].append({
                "problem": data["problem"],
                "solution": data["solution"],
                "last_used": str(datetime.now().date())
            })
            save_data(employees) # Save the updated data
            return jsonify({"message": "Problem added successfully!"})
    return jsonify({"error": "Employee not found"}), 404

# NEW: Endpoint to reset the decay timer (The core "Revisit Confirmation" edge)
@app.route('/revisit_solution', methods=['POST'])
def revisit_solution():
    data = request.json
    emp_id = data.get("emp_id")
    problem_index = data.get("problem_index")

    if emp_id is None or problem_index is None:
        return jsonify({"error": "Missing emp_id or problem_index"}), 400

    for emp in employees:
        if emp["id"] == emp_id:
            try:
                # Update the last_used date to today
                emp["problems_solved"][problem_index]["last_used"] = str(datetime.now().date())
                save_data(employees) # Save the updated data
                return jsonify({"message": "Solution marked as revisited. Decay timer reset."})
            except IndexError:
                return jsonify({"error": "Problem index out of range"}), 404

    return jsonify({"error": "Employee not found"}), 404


# NEW: Simple Search Endpoint (The "Search Functionality" edge)
@app.route('/search_knowledge', methods=['GET'])
def search_knowledge():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify(employees) # Return all if no query

    results = []
    for emp in employees:
        emp_copy = emp.copy()
        matched_problems = []
        for p in emp["problems_solved"]:
            # Search by problem title or solution text
            if query in p["problem"].lower() or query in p["solution"].lower():
                matched_problems.append(p)

        if matched_problems:
            emp_copy["problems_solved"] = matched_problems
            results.append(emp_copy)

    return jsonify(results)


if __name__ == '__main__':
    # Make sure to create an empty data.json file in the same directory initially
    if not os.path.exists(DATA_FILE):
        save_data(load_data())

    app.run(debug=True)