# Welcome

## Getting started

To run this example from the command line:

```sh
# Run the Python interpreter in interactive mode
$ python3 -i server.py
>>> roll_dice()
'The dice rolled: 1'
>>> roll_dice()
'The dice rolled: 3'
>>> roll_dice()
'The dice rolled: 3'
>>> quit()
```

## Create a virtual environment

```sh
# Create a virtual environment inside an env folder
$ python3 -m venv env

# Activate our virtual environment
$ source env/bin/activate

# Now if we run Python, we'll see we're in the right environment
(env) rob@rb 00-first-flask-app % python

# Verify that we are using the Python version for our environment
% which python

# Install Flask using the package installer for Python (pip)
% pip install flask

```

## Start our Flask application

```sh
# Define our environment variables
% export FLASK_APP=server FLASK_ENV=development
```

Your Flask application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)
