# http-server

**Author**: Chris Ball & Evy Haan
**Version**: 1.0.0

## Overview
This is a simple HTTP server with get routes on '/' and '/cow'. The functionality of the server allows a client to append a query string to the '/cow' path to produce a string that will populate the word bubble of a cowsay drawing. The server will also return a JSON object with a key of 'msg' and a value of a string of a new cowpie drawing with a user's params from a POST request.

## Getting Started
To run the application, you will want to create a virtual environment with `pipenv shell` and run `pipenv install` to install the dependencies. From there, you can fire up the server by running `python server.py`.

To start, a user can navigate to the index page. For our purposes, we used localhost and port 5000. On that index page, we have a cowsay drawing with a link to take them to the '/cow' route. Once there, they have a set of instructions showing them how to append a query string to the end of the url. When they submit the updated url, the get route will take their query string and convert it to a string that gets passed in to a new cow instance and will return the cowsay drawing with their query string as the text in the word bubble.

## Architecture
We are using Python version 3.7 for this application and utilizing the cowpy, httpie, urllib, json and requests libraries. Please refer to the Pipfile for a list of dependencies.

## API
cowpy
requests
httpie

