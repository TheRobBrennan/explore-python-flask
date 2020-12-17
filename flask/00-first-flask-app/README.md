If this is your first time running this application, please follow the steps outlined in "Initial setup" to create a virtual environment and install the required libraries.

If you have already defined a virtual environment, please skip ahead to "Start the application"

# Initial setup

```sh
# Create a virtual environment inside an env folder
$ python3 -m venv env

# Activate our virtual environment
$ source env/bin/activate
(env) rob@rb 00-first-flask-app %

# Install our libraries using the package installer for Python (pip)
% pip install -r requirements.txt
```

# Start the application

```sh
# Activate our virtual environment
$ source env/bin/activate
(env) rob@rb 00-first-flask-app %

# Define your environment variables in your terminal
% export FLASK_APP=server FLASK_ENV=development PORT=5001

# Run the application
% gunicorn --bind 0.0.0.0:$PORT server:app --log-level "debug"
```

Assuming you have followed the steps above, you should be able to view:

- Your Flask application at [http://0.0.0.0:5001](http://0.0.0.0:5001)
