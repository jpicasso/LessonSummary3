import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import os

from models import setup_db, Question, Category

items_per_page = 5

def searchForIndexes (element, string):
  index_list = []
  for i in range (len(string)):
    if element == string[i]:
      index_list.append(i)
  return index_list

def searchForWord (search, string):
  index_list = searchForIndexes (search[0],string)
  if index_list == []:
    return False
  for j in range (len(index_list)):
    x = 0
    starting_point = index_list[j]
    for i in range (len(search)):
      if search[i] == string[i+starting_point]:
        x = x + 1
    if x == len(search):
      return True      
  
  return False

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start =  (page - 1) * items_per_page
    end = start + items_per_page

    question = [question.format() for question in selection]
    current_question = question[start:end]

    return current_question

def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  
  cors = CORS(app, resources={r"/api/*": {"origins":"*"}})
  
  # CORS Headers 
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
      return response

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

  @app.route('/questions')
  def retrieve_questions():
    selection = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, selection)
    
    if len(current_questions) == 0:
        abort(404)
    
    categories = Category.query.order_by(Category.id).all()
    if len(categories) == 0:
      abort(404)
    full_list = []
    for c in categories:
      full_list.append(c.type)
  
    return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(full_list),
        'categories': full_list,
        'currentCategory': categories[0].type,
    })
 
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
 
  @app.route('/questions', methods=['POST'])
  def create_question():
    try:
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
      # TODO - flash('New question was successfully added!')
    except:
      abort(422)  
  
  @app.route('/search', methods=['POST'])
  def search_questions():
    all_questions = Question.query.order_by(Question.id).all()
    user_search = request.json.get('searchTerm', "")
    user_search = user_search.upper()
    response = {"count":0, "data":[]}
    # current_cat = 1
    
    for q in all_questions:
      question_str = q.question
      question_str = question_str.upper()
      
      if searchForWord(user_search, question_str):
        new_dictionary = {"id": q.id, "question": q.question,"category": q.category, "difficulty": q.difficulty}
        # current_cat = q.category
        response["data"].append(new_dictionary)
        response["count"] = response["count"]+1
      
    return jsonify({
      'success': True,
      'questions': response["data"],
      'totalQuestions': response["count"],
      # 'currentCategory': current_cat,
    })

  @app.route('/categories/<int:category_id>', methods=['GET'])
  def retrieve_questions_by_categories(category_id):
    all_questions = Question.query.order_by(Question.id).all()
    
    current_category = category_id
    selection = []
    for q in all_questions:
      if q.category == current_category:
        selection.append(q)
    
    current_questions = paginate_questions(request, selection)
    
    return jsonify({
      'success': True, 
      'questions': current_questions,
      'totalQuestions': len(current_questions),
      'currentCategory': current_category,
    })

  @app.route('/quizzes', methods=['POST'])
  def get_quiz_questions():  
    prev_questions = request.json.get('previous_questions', "")
    current_cat = request.json.get('quiz_category', "")
    all_questions = Question.query.order_by(Question.id).all()
    filtered_questions = []
    
    for a in all_questions:
      if a.id in prev_questions:
        pass
      elif current_cat["id"]==0:
        filtered_questions.append(a)
      elif int(a.category) == int(current_cat["id"]):
            filtered_questions.append(a)
        
    if filtered_questions != []:   
      num_of_questions = len(filtered_questions)
      if num_of_questions == 1:
        x = 0
      else: 
        x = random.randint(0,num_of_questions-1)
      q = filtered_questions[x]
      current_question = {"id": q.id , "question": q.question,"category": q.category, "difficulty": q.difficulty, "answer":q.answer}
      prev_questions.append(current_question["id"])
    else:
      current_question = {}

    return jsonify({
      'success': True,
      'previousQuestions': prev_questions,
      'question': current_question,
      'guess': '',
    })

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
    }), 400
  
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 404,
      "message": "resource not found"
    }), 404
  
  @app.errorhandler(405)
  def method_not_allowed(error):
        return jsonify({
      "success": False, 
      "error": 405,
      "message": "method not allowed"
    }), 405
  
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable error"
  }), 422

  @app.errorhandler(500)
  def internal_server_error(error):
    return jsonify({
      "success": False, 
      "error": 500,
      "message": "internal server error bud"
    }), 500

  return app

