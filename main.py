from flask import Flask

# Instantiate the Flask object
app = Flask(__name__)

# The route() function of flask class isa  decorator
# it tells the apk whicj URL should call

@app.route('/')
def HomePage():
    return 'Welcome :smile:'


# The main driver code the below will work only in the current file
# but not when imported as a module to another file

if __name__ == '__main__':
    # The run() method of flask class runs the application
    # on the local dev server
    
    app.run(port=5000, debug=True)

