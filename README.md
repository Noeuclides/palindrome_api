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
![root](https://github.com/Noeuclides/palindrome_api/raw/master/img/root.png)
You nee to register in order to use the palindrome endpoint.
![auth](https://github.com/Noeuclides/palindrome_api/raw/master/img/auth.png)
![register](https://github.com/Noeuclides/palindrome_api/raw/master/img/register.png)

Then go to the login endpoint and copy the token of the response:
![login](https://github.com/Noeuclides/palindrome_api/raw/master/img/login.png)

Put the token on the authorization of type Bearer and make the request to the palindrome endpoint:
![palindrome](https://github.com/Noeuclides/palindrome_api/raw/master/img/palindrome.png)
