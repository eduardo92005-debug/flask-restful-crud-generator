# Flask-RESTFUL CRUD Generator
[![Project Status: WIP](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

Flask-RESTFUL CRUD Generator is an extension for Flask-RESTful, a Flask extension for building REST APIs. It allows you to easily generate models, views, and basic CRUD (create, read, update, delete) operations for a given resource.

With Flask-RESTFUL CRUD Generator, you can quickly scaffold out the necessary components for a resource in your API, similar to how Laravel or Ruby on Rails do with their scaffolding functionality.

## Installation

To install Flask-RESTFUL CRUD Generator, run the following command:

``` pip install flask-restful-crud-generator ```

## Usage

To use Flask-RESTFUL CRUD Generator, import it into your Flask app and use the generate_crud function.

```python
from flask import Flask
from flask_restful import Api
from flask_restful_crud_generator import generate_crud

app = Flask(__name__)
api = Api(app)

# Generate CRUD operations for the 'users' resource
generate_crud(api, 'users')

if __name__ == '__main__':
    app.run()
```

## Additional Options
You can also pass in additional options to customize the generated CRUD operations. For example, you can specify which fields should be included in the POST and PUT requests by passing in a fields argument:

``` generate_crud(api, 'users', fields=['name', 'email', 'password']) ```

For a full list of options, see the documentation for the generate_crud function.


## Resources
- [Flask-RESTFUL-CRUD-GENERATOR](#)
- [PyPi](https://pypi.org/project/)
