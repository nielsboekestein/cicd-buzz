import os
from flask import Flask
from buzz import generator

application = Flask(__name__)

@application.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))