#!/usr/bin/python3
""" """
import unittest
import MySQLdb
import os
from models.state import State
from models.user import User
from models import storage
from datetime import datetime
import subprocess


class TestCreateStateCommand(unittest.TestCase):

    def setUp(self):
        # Set up a test database connection
        self.db = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                             host=os.getenv('HBNB_MYSQL_HOST'),
                             passwd=os.getenv('HBNB_MYSQL_PWD'),
                             port=3306,
                             db=os.getenv('HBNB_MYSQL_DB'))
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Clean up resources after the test
        self.cursor.close()
        self.db.close()

    def test_create_state_command(self):
        # Get the initial number of records
        initial_count = self.get_state_count()

        # Execute the console command
        # (You might want to use subprocess or another method to simulate running the console command)
        # For example:
        subprocess.run(["./console.py", "create State name=California"])

        # Get the number of records after executing the command
        final_count = self.get_state_count()

        # Assert that the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    def get_state_count(self):
        # Query the database to get the current number of records
        self.cursor.execute("SELECT COUNT(*) FROM states")
        return self.cursor.fetchone()[0]

if __name__ == '__main__':
    unittest.main()

