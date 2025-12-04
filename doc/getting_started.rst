Getting Started
===============

To begin using the application, follow these steps:

1. **Install required packages:**
   Install all dependencies listed in the requirements file by running::

       pip install -r requirements.txt

2. **Apply database migrations:**
   Set up the database schema according to the defined models::

       python manage.py migrate

3. **Launch the development server:**
   Start the application locally with::

       python manage.py runserver

   The application will be accessible at: http://127.0.0.1:8000/.

4. **Stop the server:**
   To stop the server, press ``Ctrl + C`` in the terminal.



