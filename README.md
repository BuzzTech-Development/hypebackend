# HYPE Backend

## About

- RESTful API for the HYPE (Hope for Youth) project.

- Written in Python using Django.

## Development Instructions

### Correct project structure

1. Create a directory named "hype" and clone the
   "hypebackend" and "hypefrontend" git repos into it.
   
2. Open the "hype" project folder in PyCharm.

### Creating a virtual environment in PyCharm

1. Go to PyCharm preferences.
   
2. Click on "Project: hype" in the sidebar and select
   "Python Interpreter".

3. Click the gear icon on the right and press "Add".

4. Keep the default settings and click ok. (Make sure
   you are running Python 3.9 or above)

5. Open a terminal and cd into the "hypebackend" folder.

6. Enter the command `pip install -r requirements.txt`
   to install Django and other dependencies into your
   virtual environment.
   
### Running the Django server

1. Open a terminal and cd to the "hypebackend" top folder.

2. Execute the command `python manage.py runserver`
   to start up the server.
