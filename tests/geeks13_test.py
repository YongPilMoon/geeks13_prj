import sys
import unittest
from os import path

from flask import Flask
from flask_testing import TestCase

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from geeks13 import User
from geeks13 import db


class BaseTest(TestCase):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    TESTING = True

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class UserTest(BaseTest):
    def test_signup(self):
        response = self.client.get("/register")
        user = User('lily', 'lily@gail.com')
        db.session.add(user)
        db.session.commit()

        assert user in db.session
        response = self.client.get("/")
        assert user in db.session

if __name__ == '__main__':
    unittest.main()
