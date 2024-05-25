# flask_intro
learning about flask

### Variables.py

We can use variables in a flask web app, well you  might be thinking about how it helps, it will help in building a URL dynamically.

```python
from flask import Flask
app =  Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello {}'.format(name)

if __name__ == '__main__':
    app.run()


Then go to the URL given there you will see your first webpage displayinh hello on your local sever.

The route() decorator in flask is used to bind a URL to a function.