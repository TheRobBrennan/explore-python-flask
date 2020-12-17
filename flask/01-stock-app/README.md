# Getting started

## Create a virtual environment

This only has to happen once. 🤓 Continue on to "Activate our virtual environment"

```sh
# Create a virtual environment inside an env folder
$ python3 -m venv env

```

## Activate our virtual environment

```sh
# Activate our virtual environment
$ source env/bin/activate

# Install our libraries using the package installer for Python (pip)
% pip install -r requirements.txt
```

## Start our Flask application

```sh
# Define your environment variables in your terminal
$ export FLASK_APP=server FLASK_ENV=development PORT=5001
```

Your Flask application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)

# Deployment

We're going to deploy our Flask application to [Heroku](https://www.heroku.com).

## Initial setup

### Download and install the Heroku CLI

This guide covers download and installing the Heroku CLI on macOS. For other platforms, please see [https://devcenter.heroku.com/articles/heroku-cli#download-and-install](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

```sh
# Install using Homebrew on macOS
$ brew tap heroku/brew && brew install heroku

# OPTIONAL: To use Heroku CLI's autocomplete
$ heroku autocomplete --refresh-cache
```

### Create a Procfile for Heroku

Our `Procfile` will instruct Heroku on running our application.

It will consist of one line: `web: gunicorn --bind 0.0.0.0:$PORT server:app --log-level "debug"`

First, let's run the `gunicorn --bind 0.0.0.0:$PORT server:app --log-level "debug"` from our local environment to make sure we've defined it correctly:

```sh
# Define our environment variables
% export FLASK_APP=server FLASK_ENV=development PORT=5001

# Run our command
% gunicorn --bind 0.0.0.0:$PORT server:app --log-level "debug"
```

Our web application should be running locally at [http://0.0.0.0:5001](http://0.0.0.0:5001)

### Create a Heroku application

Assuming you have installed the Heroku CLI:

```sh
% heroku create
 ›   Warning: heroku update available from 7.35.0 to 7.47.6.
Creating app... done, ⬢ mysterious-waters-87596
https://mysterious-waters-87596.herokuapp.com/ | https://git.heroku.com/mysterious-waters-87596.git
```

If your application folder is not a git repository already, please initialize an empty one with:

```sh
% git init
```

#### Add the newly created repository to your git remotes

```sh
# Add the new Heroku git repository using the example above
% git remote add heroku https://git.heroku.com/mysterious-waters-87596.git

# CHECKPOINT: List your git remotes. You should see heroku as a remote
% git remote -v
```

## Deploy to Heroku

Make sure that you have committed some code to either the `main` or `master` branch of your repo. Code committed to other branches will not be deployed.

Please note that the default git deployment for Heroku assumes you have a `Procfile` defined in the top level of your project's directory structure.

```sh
% git push heroku `git rev-parse --abbrev-ref HEAD`
```

When deployment has finished, you will see something like:

```sh
remote:        Installing collected packages: itsdangerous, MarkupSafe, Jinja2, click, Werkzeug, Flask, idna, certifi, chardet, urllib3, requests, gunicorn
remote:        Successfully installed Flask-1.1.2 Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 certifi-2020.12.5 chardet-4.0.0 click-7.1.2 gunicorn-20.0.4 idna-2.10 itsdangerous-1.1.0 requests-2.25.1 urllib3-1.26.2
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 46.2M
remote: -----> Launching...
remote:        Released v3
remote:        https://mysterious-waters-87596.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/mysterious-waters-87596.git
 * [new branch]      master -> master
```

In this example, our Flask application is running and available at [https://mysterious-waters-87596.herokuapp.com](https://mysterious-waters-87596.herokuapp.com).

We can verify our stock application is working by browsing to [https://mysterious-waters-87596.herokuapp.com/stocks/AAPL](https://mysterious-waters-87596.herokuapp.com/stocks/AAPL)
