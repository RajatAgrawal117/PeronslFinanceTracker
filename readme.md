# Personal Finance Tracker

A Django-based web application to track personal finances, including transactions and weekly reports.

## Features

- Add and view financial transactions
- View a report of transactions for the past week
- Simple and clean UI with Bootstrap integration

## Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (Recommended)

## Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/your-username/personal-finance-tracker.git
    cd personal-finance-tracker
    ```

2. **Create and Activate a Virtual Environment**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply Migrations**

    ```sh
    python manage.py migrate
    ```

5. **Create a Superuser**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the Development Server**

    ```sh
    python manage.py runserver
    ```

7. **Open the Application**

    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

1. **Enter Transactions**

    - Navigate to the home page.
    - Use the form to enter the date, amount, details, and whether the transaction is a spend or receive.

2. **View Transactions**

    - The entered transactions are displayed in a table below the form.
    - Amounts are color-coded (green for positive amounts, red for negative amounts).

3. **View Weekly Report**

    - Click on "View Weekly Report" to see the transactions from the past week and the total amount spent or received.

## Project Structure

```plaintext
personal-finance-tracker/
│
├── finance_app/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── personal_finance_tracker/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
└── .gitignore
