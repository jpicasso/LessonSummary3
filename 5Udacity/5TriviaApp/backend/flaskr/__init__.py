import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import os

from models import setup_db, Question, Category

items_per_page = 5

def searchForFirstIndex (element, string):
  for i in range (len(string)):
    if element == string[i]:
      return i
  return -1

def searchForWord (search, string):
  x = searchForFirstIndex (search[0],string)
  if x == -1:
    return False
  for i in range (len(search)):
    if search[i] != string[i+x]:
      return False
  return True

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * items_per_page
    end = start + items_per_page

    question = [question.format() for question in selection]
    current_question = question[start:end]

    return current_question

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  
  # '''
  # @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  # '''
  cors = CORS(app, resources={r"/api/*": {"origins":"*"}})

  # '''
  # @TODO: Use the after_request decorator to set Access-Control-Allow
  # '''
  # CORS Headers 
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
      return response

  # '''
  # @TODO: 
  # Create an endpoint to handle GET requests 
  # for all available categories.
  # '''
  @app.route('/categories', methods=['GET'])
  def retrieve_categoriess():
    categories = Category.query.order_by(Category.id).all()
    if len(categories) == 0:
      abort(404)

    full_list = []
    for c in categories:
      full_list.append(c.type)
    
    return jsonify({
      'success': True, 
      'categories': full_list
    })

  # '''
  # @TODO: 
  # Create an endpoint to handle GET requests for questions, 
  # including pagination (every 10 questions). 
  # This endpoint should return a list of questions, 
  # number of total questions, current category, categories. 

  @app.route('/questions')
  def retrieve_questions():
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)
      
      if len(current_questions) == 0:
          abort(404)

      categories = Category.query.order_by(Category.id).all()
      if len(categories) == 0:
          abort(404)

      full_list = ""
      for c in categories:
            full_list = c.type + ', '+ full_list

      return jsonify({
          'success': True,
          'questions': current_questions,
          'totalQuestions': len(Question.query.all()),
          'categories': full_list,
          'currentCategory': categories[0].type,
      })

  # TEST: At this point, when you start the application
  # you should see questions and categories generated,
  # ten questions per page and pagination at the bottom of the screen for three pages.
  # Clicking on the page numbers should update the questions. 
  # '''

  # '''
  # @TODO: 
  # Create an endpoint to DELETE question using a question ID. 

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()

      if question is None:
        abort(404)

      question.delete()
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      return jsonify({
        'success': True,
        'deleted': question_id,
        'questions': current_questions,
        'total_questions': len(Question.query.all())
      })

    except:
      abort(422)

  # TEST: When you click the trash icon next to a question, the question will be removed.
  # This removal will persist in the database and when you refresh the page. 
  # '''

  # '''
  # @TODO: 
  # Create an endpoint to POST a new question, 
  # which will require the question and answer text, 
  # category, and difficulty score.

  @app.route('/questions', methods=['POST'])
  def create_question():
    body = request.get_json()
    
    question = body["question"]
    answer = body["answer"]
    category = body["category"]
    difficulty = body["difficulty"]
    
    new_question = Question(question=question, answer=answer, category=category, difficulty=difficulty)
    
    new_question.insert()

    return jsonify({
        'success': True,
      })
    # flash('New question was successfully added!')

  # TEST: When you submit a question on the "Add" tab, 
  # the form will clear and the question will appear at the end of the last page
  # of the questions list in the "List" tab.  
  # '''

  # '''
  # @TODO: 
  # Create a POST endpoint to get questions based on a search term. 
  # It should return any questions for whom the search term 
  # is a substring of the question. 

  @app.route('/search', methods=['POST'])
  def search_questions():
    all_questions = Question.query.order_by(Question.id).all()
    user_search = request.json.get('searchTerm', "")
    user_search = user_search.upper()
    response = {"count":0, "data":[]}
    for q in all_questions:
      question_str = q.question
      question_str = question_str.upper()
      if searchForWord(user_search, question_str):
          new_dictionary = {"id": q.id, "question": q.question,"category": q.category, "difficulty": q.difficulty}
          response["data"].append(new_dictionary)
          response["count"] = response["count"]+1

    return jsonify({
      'success': True,
      'questions': response["data"],
      'totalQuestions': response["count"],
      'currentCategory': 1,
    })

  # TEST: Search by any phrase. The questions list will update to include 
  # only question that include that string within their question. 
  # Try using the word "title" to start. 
  # '''

  # '''
  # @TODO: 
  # Create a GET endpoint to get questions based on category. 

  # TEST: In the "List" tab / main screen, clicking on one of the 
  # categories in the left column will cause only questions of that 
  # category to be shown. 
  # '''


  # '''
  # @TODO: 
  # Create a POST endpoint to get questions to play the quiz. 
  # This endpoint should take category and previous question parameters 
  # and return a random questions within the given category, 
  # if provided, and that is not one of the previous questions. 

  # TEST: In the "Play" tab, after a user selects "All" or a category,
  # one question at a time is displayed, the user is allowed to answer
  # and shown whether they were correct or not. 
  # '''

  # '''
  # @TODO: 
  # Create error handlers for all expected errors 
  # including 404 and 422. 
  # '''

  return app

