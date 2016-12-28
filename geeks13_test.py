import unittest

from flask import Flask
from flask_testing import TestCase

from geeks13 import db
from geeks13.models import User


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
    def test_something(self):
        user = User('lily', 'lily@gail.com')
        db.session.add(user)
        db.session.commit()

        assert user in db.session
        response = self.client.get("/")
        assert user in db.session

if __name__ == '__main__':
    unittest.main()
