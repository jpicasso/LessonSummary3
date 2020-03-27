# Basic Flask Auth - Follow Along

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within this directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API


### Getting a JWT Token or bearer token
https://www.youtube.com/watch?time_continue=242&v=_Fb0HKn0U2I&feature=emb_logo

Hosted log in screen flow for auth0

Insert values into this
https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}

With values:
https://udacity-picasso.auth0.com/authorize?audience=image&response_type=token&client_id=359Yy80OCx5AzBqy8NAkOTfRXEdOTVyP&redirect_uri=http://localhost:8080/login-results

result should look like the below:

http://localhost:8080/login-results#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJEZEdNelZCUWtFMlJVWkZRVFUzT0RRMlJrTkJNREl4TWpWRVJqSTJNVVUwUWpNME5EY3pNUSJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktcGljYXNzby5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU1ZGExYzRjZDc4MzYwZDZmODNhZjAxIiwiYXVkIjoiaW1hZ2UiLCJpYXQiOjE1ODMyNzYzNzAsImV4cCI6MTU4MzI4MzU3MCwiYXpwIjoiNFN4OEl5SFJobnhKRWVJVVJxQ21CZEQybHRHeTd0MlEiLCJzY29wZSI6IiJ9.Piss4NoaI0Zv4jhc3QJR2x98e0exkh9yawde9IG_8B0y2YRG2cFbFb8wygraIChS1FBLU6BZ7TleatX9nF-y0Qyyh8mnOwkZMWyjlNy10_HSwBi1bhBRaooX5SrbZUk4EjPZMfZazDjXzH72qRozPIIgslsLVaaVH3FCY3MleZ9RUYP8bO2S4GhfZt_AxDeZX2iHzw2DVEIJ8VfxarMf-MxgF5DOtPKV5m1ttiYTE9wRXINVlGt8oEVFLrk9riZzmGunXJdmHZ2369aOQJd1iA5w0jMb3Gk0GYOTAnQy4HbLF0bgYeVzoSVXGLNC-NDDIWpHhTf085TYomRNXcCjyA&expires_in=7200&token_type=Bearer

the token is below and can be checked out on jwt.io

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJEZEdNelZCUWtFMlJVWkZRVFUzT0RRMlJrTkJNREl4TWpWRVJqSTJNVVUwUWpNME5EY3pNUSJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktcGljYXNzby5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU1ZGExYzRjZDc4MzYwZDZmODNhZjAxIiwiYXVkIjoiaW1hZ2UiLCJpYXQiOjE1ODMyNzYzNzAsImV4cCI6MTU4MzI4MzU3MCwiYXpwIjoiNFN4OEl5SFJobnhKRWVJVVJxQ21CZEQybHRHeTd0MlEiLCJzY29wZSI6IiJ9.Piss4NoaI0Zv4jhc3QJR2x98e0exkh9yawde9IG_8B0y2YRG2cFbFb8wygraIChS1FBLU6BZ7TleatX9nF-y0Qyyh8mnOwkZMWyjlNy10_HSwBi1bhBRaooX5SrbZUk4EjPZMfZazDjXzH72qRozPIIgslsLVaaVH3FCY3MleZ9RUYP8bO2S4GhfZt_AxDeZX2iHzw2DVEIJ8VfxarMf-MxgF5DOtPKV5m1ttiYTE9wRXINVlGt8oEVFLrk9riZzmGunXJdmHZ2369aOQJd1iA5w0jMb3Gk0GYOTAnQy4HbLF0bgYeVzoSVXGLNC-NDDIWpHhTf085TYomRNXcCjyA