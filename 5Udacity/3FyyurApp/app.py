#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
import time
import datetime
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
from config import SQLALCHEMY_DATABASE_URI

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)             
app.config.from_object('config')
print ("this is the URI: " + SQLALCHEMY_DATABASE_URI)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.String(120))
    seeking_description = db.Column(db.String(120))
    
class Artist(db.Model):
    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(500))
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.String(120))
    seeking_description = db.Column(db.String(120))
    
class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    start_time = db.Column(db.String(120))

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------
#  ----------------------------------------------------------------
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  venue_objects = Venue.query.order_by('id').all()
  
  data = []
  for v in venue_objects:             
    if data == []:    
      new_dictionary = {"city": v.city, "state": v.state, "venues":[]}
      data.append(new_dictionary)
    in_set = 0
    for c in data:
      if c["city"] == v.city:
        in_set += 1
    if in_set == 0:
      new_dictionary = {"city": v.city, "state": v.state, "venues":[]}
      data.append(new_dictionary)
  
  for v in venue_objects:               
    x = 0
    for c in data:
      if c["city"] == v.city:    
        new_dictionary = { "id": v.id, "name": v.name,}
        data[x]["venues"].append(new_dictionary)
      x = x +1

  return render_template('pages/venues.html', areas=data);

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  v = Venue.query.get(venue_id)
  upcoming_shows = []
  past_shows = []
  upcoming_shows_count = 0
  past_shows_count = 0
  show_objects = Show.query.filter_by(venue_id=venue_id)
  
  for s in show_objects:
    artist = Artist.query.get(s.artist_id)
    new_dictionary = {"artist_id":s.artist_id, "artist_name":artist.name, "artist_image_link":artist.image_link, "start_time":s.start_time}
    
    show_datetime_obj = datetime.strptime(s.start_time, '%Y-%m-%d %H:%M:%S')
    current_time = datetime.now()
    if show_datetime_obj > current_time:
      upcoming_shows.append(new_dictionary)
      upcoming_shows_count += 1
    else: 
      past_shows.append(new_dictionary)
      past_shows_count += 1

  data = {"id":v.id, "name":v.name, "genres": [v.genres], "city": v.city, "state": v.state, "phone": v.phone, "website": v.website,"facebook_link": v.facebook_link, "seeking_talent": v.seeking_talent, "seeking_description": v.seeking_description,"image_link": v.image_link, "past_shows": past_shows, "upcoming_shows": upcoming_shows, "past_shows_count": past_shows_count,"upcoming_shows_count": upcoming_shows_count}
  
  return render_template('pages/show_venue.html', venue=data)

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  venue_name = request.form['name']
  venue_city = request.form['city']
  venue_state = request.form['state']
  venue_address = request.form['address'] 
  venue_phone = request.form['phone'] 
  venue_genres = request.form['genres'] 
  venue_facebook_link = request.form['facebook_link'] 
  venue_image_link = request.form['image_link'] 
  
  venue = Venue(name=venue_name, city=venue_city,state=venue_state, address=venue_address, phone=venue_phone, facebook_link=venue_facebook_link, image_link=venue_image_link, genres=venue_genres)
  db.session.add(venue)
  db.session.commit()
  
  flash('Venue ' + request.form['name'] + ' was successfully listed!')
  return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  try:
    # TODO - delete all shows that the are associated with Venue
    Venue.query.filter_by(id=venue_id).delete()
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return jsonify({ 'success': True })

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  v = Venue.query.get(venue_id)
  
  form.name.data = v.name
  form.city.data  = v.city
  form.state.data  = v.state 
  form.address.data  = v.address 
  form.phone.data  = v.phone 
  form.genres.data = v.genres 
  form.facebook_link.data = v.facebook_link  
  form.image_link.data = v.image_link

  v = Venue.query.get(venue_id)
  venue = {"id":v.id, "name":v.name, "genres": [v.genres], "city": v.city, "state": v.state, "phone": v.phone, "website": v.website,"facebook_link": v.facebook_link, "seeking_talent": v.seeking_talent, "seeking_description": v.seeking_description,"image_link": v.image_link, "past_shows": [], "upcoming_shows":[], "past_shows_count": 0,"upcoming_shows_count":0}

  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  venue = Venue.query.get(venue_id)
  
  venue.name = request.form['name']
  venue.city = request.form['city']
  venue.state = request.form['state']
  venue.phone = request.form['phone'] 
  venue.genres = request.form['genres'] 
  venue.facebook_link = request.form['facebook_link'] 
  venue.image_link = request.form['image_link'] 

  db.session.commit()

  flash('Venue ' + request.form['name'] + ' was successfully updated!')
  
  return redirect(url_for('show_venue', venue_id=venue_id))

@app.route('/venues/search', methods=['POST'])
def search_venues():
  user_search = request.form['search_term']
  user_search = user_search.upper()
  
  response = {"count":0, "data":[]}
  venue_objects = Venue.query.order_by('id').all()
  for v in venue_objects:
    venue_name = v.name
    venue_name = venue_name.upper()
    if searchForWord(user_search, venue_name):
          new_dictionary = {"id":v.id, "name":v.name,"num_upcoming_shows":0,}
          response["data"].append(new_dictionary)
          response["count"] = response["count"]+1
  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

#  Artists
#  ----------------------------------------------------------------
#  ----------------------------------------------------------------
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  data2 =[]
  artist_objects = Artist.query.order_by('id').all()
  for a in artist_objects:
        new_dictionary = {"id":a.id, "name":a.name}
        data2.append(new_dictionary)
  return render_template('pages/artists.html', artists=data2)

@app.route('/artists/<artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
  try:
    # TODO - delete all shows that the are associated with Artist
    Artist.query.filter_by(id=artist_id).delete()
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return jsonify({ 'success': True })

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  a = Artist.query.get(artist_id)
  
  upcoming_shows = []
  past_shows = []
  upcoming_shows_count = 0
  past_shows_count = 0
  show_objects = Show.query.filter_by(artist_id=artist_id)
  
  for s in show_objects:
    venue = Venue.query.get(s.venue_id)
    new_dictionary = {"venue_id":s.venue_id, "venue_name":venue.name, "venue_image_link":venue.image_link, "start_time":s.start_time}
    
    show_datetime_obj = datetime.strptime(s.start_time, '%Y-%m-%d %H:%M:%S')
    current_time = datetime.now()
    if show_datetime_obj > current_time:
      upcoming_shows.append(new_dictionary)
      upcoming_shows_count += 1
    else: 
      past_shows.append(new_dictionary)
      past_shows_count += 1
  
  data = {"id":a.id, "name":a.name, "genres": [a.genres], "city": a.city, "state": a.state, "phone": a.phone, "website": a.website,"facebook_link": a.facebook_link, "seeking_venue": a.seeking_venue, "seeking_description": a.seeking_description,"image_link": a.image_link, "past_shows": past_shows, "upcoming_shows": upcoming_shows, "past_shows_count": past_shows_count,"upcoming_shows_count": upcoming_shows_count}
  return render_template('pages/show_artist.html', artist=data)

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  artist_name = request.form['name']
  artist_city = request.form['city']
  artist_state = request.form['state']
  artist_phone = request.form['phone'] 
  artist_genres = request.form['genres'] 
  artist_facebook_link = request.form['facebook_link'] 
  artist_image_link = request.form['image_link'] 
  
  artist = Artist(name=artist_name, city=artist_city,state=artist_state, phone=artist_phone, facebook_link=artist_facebook_link, image_link=artist_image_link, genres=artist_genres)
  db.session.add(artist)
  db.session.commit()

  flash('Artist ' + request.form['name'] + ' was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  return render_template('pages/home.html')

@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  a = Artist.query.get(artist_id)
  
  form.name.data = a.name
  form.city.data  = a.city
  form.state.data  = a.state 
  form.phone.data  = a.phone 
  form.genres.data = a.genres 
  form.facebook_link.data = a.facebook_link  
  form.image_link.data = a.image_link

  artist = {"id":a.id, "name":a.name, "genres": [a.genres], "city": a.city, "state": a.state, "phone": a.phone, "website": a.website,"facebook_link": a.facebook_link, "seeking_venue": a.seeking_venue, "seeking_description": a.seeking_description,"image_link": a.image_link, "past_shows": [],"upcoming_shows":[], "past_shows_count": 0,"upcoming_shows_count": 0}
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  artist = Artist.query.get(artist_id)
  
  artist.name = request.form['name']
  artist.city = request.form['city']
  artist.state = request.form['state']
  artist.phone = request.form['phone'] 
  artist.genres = request.form['genres'] 
  artist.facebook_link = request.form['facebook_link'] 
  artist.image_link = request.form['image_link'] 

  db.session.commit()

  flash('Artist ' + request.form['name'] + ' was successfully updated!')
 
  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/artists/search', methods=['POST'])
def search_artists():
  user_search = request.form['search_term']
  user_search = user_search.upper()
  
  response = {"count":0, "data":[]}
  artist_objects = Artist.query.order_by('id').all()
  for a in artist_objects:
    artist_name = a.name
    artist_name = artist_name.upper()
    if searchForWord(user_search, artist_name):
          new_dictionary = {"id":a.id, "name":a.name,"num_upcoming_shows":0,}
          response["data"].append(new_dictionary)
          response["count"] = response["count"]+1

  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

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

#  Shows
#  ----------------------------------------------------------------
#  ----------------------------------------------------------------
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  data=[]
  show_objects = Show.query.order_by('id').all()
  for s in show_objects:
        artist = Artist.query.get(s.artist_id)
        venue = Venue.query.get(s.venue_id)
  
        new_dictionary = {"artist_id":s.artist_id, "artist_name":artist.name, "venue_id":s.venue_id, "venue_name":venue.name,"artist_image_link": artist.image_link, "start_time": s.start_time}
        data.append(new_dictionary)

  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  show_artist_id = request.form['artist_id']
  show_venue_id = request.form['venue_id']
  show_start_time = request.form['start_time']
  
  show = Show(artist_id=show_artist_id, venue_id=show_venue_id,start_time=show_start_time)
  db.session.add(show)
  db.session.commit()

  flash('Show was successfully listed!')
  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':    #this runs the app
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''

db.create_all()
