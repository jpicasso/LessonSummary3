import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://johnpicasso:1234@{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'This is a test question?',
            'answer': 'yes it is',
            'category': 5,
            'difficulty': 3,
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    #make sure to update the question id being deleted with something that is actually in the database
    def test_delete_question(self):
        question_num = 20
        res = self.client().delete('/questions/{}'.format(question_num))
        data = json.loads(res.data)
        question = Question.query.filter(Question.id == question_num).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], question_num)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertEqual(question, None)

    def test_create_question(self):
        res = self.client().post('/questions', json={'question':'q6', 'answer':'a6', 'category':'3','difficulty':1})
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)

    def test_create_question_fail(self):
        res = self.client().post('/questions', json={'questionFAIL':'q5', 'answer':'a5', 'category':'3','difficulty':1})
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
         
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(data['currentCategory'])
        self.assertTrue(data['categories'])

    # TODO - Create test for search

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()