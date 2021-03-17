# Longest Palindrome API

API to get the longest subpalindrome in a string.

## Requirements
You have to have mysql on your local machine.
To run the django app use the python package manager [pipenv](https://pipenv-es.readthedocs.io/es/latest/).
It is recommended to use the API with [Postman](https://www.postman.com/).

## Installation

Install the dependencies:

```bash
pipenv install
```

Configure mysql database:
```bash
pipenv run python configDB.py 
```

And then run the django server:

```bash
pipenv run migrate
pipenv run server
```
Note: The migrate and server commands are set in the Pipfile.

## Usage
First go to the /register endpoint and register some user. Then go to the /login api login with the user you created and copy the token in order to use the /palindrome endpoint