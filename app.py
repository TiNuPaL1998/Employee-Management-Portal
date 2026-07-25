from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "employee_portal_secret_key"

# -----------------------------
# Users (Temporary - No Database)
# -----------------------------
users_list = [
    {
        "username": "admin",
        "password": "admin123"
    }
]

# -----------------------------
# Employees (Temporary - No Database)
# -----------------------------
employees_list = [
    {
        "emp_id": "EMP001",
        "name": "John Doe",
        "department": "IT",
        "email": "john@example.com"
    },
    {
        "emp_id": "EMP002",
        "name": "Alice Smith",
        "department": "HR",
        "email": "alice@example.com"
    }
]


# =============================
# Login
# =============================
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        for user in users_list:

            if (
                user["username"] == username and
                user["password"] == password
            ):

                session["username"] = username
                return redirect("/dashboard")

        return render_template(
            "login.html",
            error="Invalid Username or Password"
        )

    return render_template("login.html")

# =============================
# Register
# =============================
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            return render_template(
                "register.html",
                error="Passwords do not match."
            )

        # Check if username already exists
        for user in users_list:
            if user["username"] == username:
                return render_template(
                    "register.html",
                    error="Username already exists."
                )

        # Add new user
        users_list.append({
            "username": username,
            "password": password
        })

        return redirect("/")

    return render_template("register.html")
# =============================
# Dashboard
# =============================
# =============================
# Dashboard
# =============================
@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect("/")

    total_employees = len(employees_list)
    total_users = len(users_list)

    departments = set()
    
    for employee in employees_list:
        departments.add(employee["department"])

    total_departments = len(departments)

    recent_employees = employees_list[-5:]

    return render_template(
        "dashboard.html",
        username=session["username"],
        total_employees=total_employees,
        total_users=total_users,
        total_departments=total_departments,
        recent_employees=recent_employees
    )


# =============================
# Employees
# =============================
@app.route("/employees")
def employees():

    if "username" not in session:
        return redirect("/")

    return render_template(
        "employees.html",
        employees=employees_list
    )


# =============================
# Add Employee
# =============================
@app.route("/add_employee", methods=["GET", "POST"])
def add_employee():

    if "username" not in session:
        return redirect("/")

    if request.method == "POST":

        employee = {
            "emp_id": request.form["emp_id"],
            "name": request.form["name"],
            "department": request.form["department"],
            "email": request.form["email"]
        }

        employees_list.append(employee)

        return redirect("/employees")

    return render_template("add_employee.html")


# =============================
# Edit Employee
# =============================
@app.route("/edit_employee/<emp_id>", methods=["GET", "POST"])
def edit_employee(emp_id):

    if "username" not in session:
        return redirect("/")

    employee = None

    for emp in employees_list:
        if emp["emp_id"] == emp_id:
            employee = emp
            break

    if employee is None:
        return redirect("/employees")

    if request.method == "POST":

        employee["name"] = request.form["name"]
        employee["department"] = request.form["department"]
        employee["email"] = request.form["email"]

        return redirect("/employees")

    return render_template(
        "edit_employee.html",
        employee=employee
    )


# =============================
# Delete Employee
# =============================
@app.route("/delete_employee/<emp_id>")
def delete_employee(emp_id):

    if "username" not in session:
        return redirect("/")

    global employees_list

    employees_list = [
        employee
        for employee in employees_list
        if employee["emp_id"] != emp_id
    ]

    return redirect("/employees")


# =============================
# Logout
# =============================
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# =============================
# Run Application
# =============================
if __name__ == "__main__":
    app.run(debug=True)