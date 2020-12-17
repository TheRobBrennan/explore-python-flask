This project explores creating applications using [Python 3.8.6 or newer](https://www.python.org) to develop [Flask](https://flask.palletsprojects.com/en/1.1.x/) applications.

# Getting started

## Install Python on macOS Catalina

First, let's verify that we are using Python 3.8.6 or higher:

```sh
$ python3 -V
Python 3.8.6
```

If you have Python 3.5 or higher, you can then install [virtualenv](https://virtualenv.pypa.io/en/latest/):

```sh
$ sudo pip3 install virtualenv
```

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

## CHALLENGE: How do we deploy multiple apps to Heroku from a single repository?

Heroku applications assume one repo to one application. In this case, we are going to have many example applications that we want to deploy.

Imagine the nightmare of having individual repositories for all of the example apps we're creating 🤯 That would truly be a pain in the ass to manage and maintain, wouldn't it?

We will use [Heroku Multi Procfile buildpack](https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-multi-procfile) to solve this problem.

```sh
# Create applications (-a <application-name>) and their git remotes (-r <remote-name>) on Heroku
$ heroku create -a rb-flask-00 -r heroku-example-00
$ heroku create -a rb-flask-01 -r heroku-example-01

# Add the Heroku Multi Procfile buildpack to each application
$ heroku buildpacks:add -a rb-flask-00 heroku-community/multi-procfile
$ heroku buildpacks:add -a rb-flask-01 heroku-community/multi-procfile

# Specify the location of each application's Procfile
$ heroku config:set -a rb-flask-00 PROCFILE=flask/00-first-flask-app/Procfile
$ heroku config:set -a rb-flask-01 PROCFILE=flask/01-stock-app/Procfile

# Add Heroku Buildpack: Python - https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-python
$ heroku buildpacks:add -a rb-flask-00 heroku/python
$ heroku buildpacks:add -a rb-flask-01 heroku/python

# Deploy each application
$ git push heroku-example-00 HEAD:master
$ git push heroku-example-01 HEAD:master

# TROUBLESHOOTING: Tail the logs of your application on Heroku
$ heroku logs --tail -a rb-flask-00
$ heroku logs --tail -a rb-flask-01
```

Assuming you have followed the steps above, you should be able to view:

- [Example 00 - Heroku Application: `rb-flask-00` - Dice roll ](https://rb-flask-00.herokuapp.com)
- [Example 01 - Heroku Application: `rb-flask-01` - Stocks app](https://rb-flask-01.herokuapp.com/stocks/AAPL)
