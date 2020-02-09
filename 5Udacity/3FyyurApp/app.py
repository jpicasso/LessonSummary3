#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
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

app = Flask(__name__)             # pulls a special variable that gets as value the string "__main__" when you're executing the script to eventually launch app
app.config.from_object('config')
print ("this is the URI: " + SQLALCHEMY_DATABASE_URI)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://johnpicasso:1234@localhost:5432/fyyurapp'
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

    # DONE - TODO: implement any missing fields, as a database migration using Flask-Migrate

    genres = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.String(120))
    seeking_description = db.Column(db.String(120))
    # Might need to make these lists of show objects with foreign keys?
    shows = db.relationship('Show',backref='venue', lazy=True)
    past_shows = db.Column(db.String(120))
    upcoming_shows = db.Column(db.String(120))

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

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    # Notes on SQL Alchemy one to many relationships - https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.String(120))
    seeking_description = db.Column(db.String(120))
    shows = db.relationship('Show',backref='artist', lazy=True)
    past_shows = db.Column(db.String(120))
    upcoming_shows = db.Column(db.String(120))
    

# DONE - TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    venue_name = db.Column(db.String(120))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    artist_name = db.Column(db.String(120))
    artist_image_link = db.Column(db.String(120))
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

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
  data=[{
    "city": "San Francisco",
    "state": "CA",
    "venues": [{
      "id": 1,
      "name": "The Musical Hop",
      "num_upcoming_shows": 0,
    }, {
      "id": 3,
      "name": "Park Square Live Music & Coffee",
      "num_upcoming_shows": 1,
    }]
  }, {
    "city": "New York",
    "state": "NY",
    "venues": [{
      "id": 2,
      "name": "The Dueling Pianos Bar",
      "num_upcoming_shows": 0,
    }]
  }]
  return render_template('pages/venues.html', areas=data);

@app.route('/venues/search', methods=['POST'])
def search_venues():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
  response={
    "count": 1,
    "data": [{
      "id": 2,
      "name": "The Dueling Pianos Bar",
      "num_upcoming_shows": 0,
    }]
  }
  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id

  v = Venue.query.get(venue_id)
  data2 = {"id":v.id, "name":v.name, "genres": [v.genres], "city": v.city, "state": v.state, "phone": v.phone, "website": v.website,"facebook_link": v.facebook_link, "seeking_talent": v.seeking_talent, "seeking_description": v.seeking_description,"image_link": v.image_link, "past_shows": [{
      "artist_id": 1,
      "artist_name": "Guns N Petals",
      "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
      "start_time": "2019-05-21T21:30:00.000Z"
    }], "upcoming_shows":[], "past_shows_count": 0,"upcoming_shows_count":0}
  # TO DO ADD PAST SHOWS AND UPCOMING SHOWS 
  return render_template('pages/show_venue.html', venue=data2)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # DONE - TODO: insert form data as a new Venue record in the db, instead
  
  #collect data
  venue_name = request.form['name']
  venue_city = request.form['city']
  venue_state = request.form['state']
  venue_address = request.form['address'] 
  venue_phone = request.form['phone'] 
  venue_genres = request.form['genres'] 
  venue_facebook_link = request.form['facebook_link'] 
  
  # create new object and add to the db
  venue = Venue(name=venue_name, city=venue_city,state=venue_state, address=venue_address, phone=venue_phone, facebook_link=venue_facebook_link, genres=venue_genres)
  db.session.add(venue)
  db.session.commit()
  
  # on successful db insert, flash success
  flash('Venue ' + request.form['name'] + ' was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  try:
    Venue.query.filter_by(id=venue_id).delete()
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return jsonify({ 'success': True })

  # DONE - BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  
#  Artists
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
    Artist.query.filter_by(id=artist_id).delete()
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return jsonify({ 'success': True })

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the venue page with the given venue_id
  a = Artist.query.get(artist_id)
  data2 = {"id":a.id, "name":a.name, "genres": [a.genres], "city": a.city, "state": a.state, "phone": a.phone, "website": a.website,"facebook_link": a.facebook_link, "seeking_venue": a.seeking_venue, "seeking_description": a.seeking_description,"image_link": a.image_link, "past_shows": [{
      "venue_id": 1,
      "venue_name": "The Musical Hop",
      "venue_image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
      "start_time": "2019-05-21T21:30:00.000Z"
    }], "upcoming_shows":[], "past_shows_count": 0,"upcoming_shows_count":0}
  # TO DO ADD PAST SHOWS AND UPCOMING SHOWS 
  
  return render_template('pages/show_artist.html', artist=data2)


@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
  response={
    "count": 1,
    "data": [{
      "id": 4,
      "name": "Guns N Petals",
      "num_upcoming_shows": 0,
    }]
  }
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))


#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  a = Artist.query.get(artist_id)
  artist = {"id":a.id, "name":a.name, "genres": [a.genres], "city": a.city, "state": a.state, "phone": a.phone, "website": a.website,"facebook_link": a.facebook_link, "seeking_venue": a.seeking_venue, "seeking_description": a.seeking_description,"image_link": a.image_link, "past_shows": [{
      "venue_id": 1,
      "venue_name": "The Musical Hop",
      "venue_image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
      "start_time": "2019-05-21T21:30:00.000Z"
    }], "upcoming_shows":[], "past_shows_count": 0,"upcoming_shows_count":0}
  return render_template('forms/edit_artist.html', form=form, artist=artist)
  # TODO: populate form with fields from artist with ID <artist_id>

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes
  artist = Artist.query.get(artist_id)
  
  artist.name = request.form['name']
  artist.city = request.form['city']
  artist.state = request.form['state']
  artist.phone = request.form['phone'] 
  artist.genres = request.form['genres'] 
  artist.facebook_link = request.form['facebook_link'] 
  artist.image_link = request.form['image_link'] 

  db.session.commit()

  # on successful db insert, flash success
  flash('Artist ' + request.form['name'] + ' was successfully updated!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')

  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  #TODO
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  artist_name = request.form['name']
  artist_city = request.form['city']
  artist_state = request.form['state']
  artist_phone = request.form['phone'] 
  artist_genres = request.form['genres'] 
  artist_facebook_link = request.form['facebook_link'] 
  artist_image_link = request.form['image_link'] 
  
  # create new object and add to the db
  artist = Artist(name=artist_name, city=artist_city,state=artist_state, phone=artist_phone, facebook_link=artist_facebook_link, image_link=artist_image_link, genres=artist_genres)
  db.session.add(artist)
  db.session.commit()

  # on successful db insert, flash success
  flash('Artist ' + request.form['name'] + ' was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
  return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.
  #       num_shows should be aggregated based on number of upcoming shows per venue.
  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead
  show_artist_id = request.form['artist_id']
  show_venue_id = request.form['venue_id']
  show_start_time = request.form['start_time']
  
  # create new object and add to the db
  show = Show(artist_id=show_artist_id, venue_id=show_venue_id,start_time=show_start_time)
  db.session.add(show)
  db.session.commit()

  # on successful db insert, flash success
  flash('Show was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
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
