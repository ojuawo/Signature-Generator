# app/routes.py
from flask import render_template
from app import app
from your_module import generate_html_signature, Employee
import pandas as pd

@app.route('/')
def index():
    # Your pandas and signature generation logic here
    # ...

    employee_signature = generate_html_signature(employee, company_logo_url)

    return render_template('email_signature.html', employee_signature=employee_signature)
