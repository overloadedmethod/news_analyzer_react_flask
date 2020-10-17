__author__ = "Vladimir"

import os

from flask.app import Flask
from app import app as application

PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split("/")[-1]


if __name__ == "__main__":
    application.run(host="localhost", port=5000, debug=True)
