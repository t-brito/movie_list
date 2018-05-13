from app.main import bp
from app import mongo
from flask import render_template, abort, url_for, g
from flask_babel import _, get_locale

MOVIES = [
  {
    '_id': 'tt0169547',
    'or_title': 'American Beauty',
    'pt_title': 'Beleza Americana',
    'year': '1999',
    'director': {'id': 'nm0005222', 'name': 'Sam Mendes'},
    'actors': [
      {'id': 'nm0000228', 'name': 'Kevin Spacey'},
      {'id': 'nm0000906', 'name': 'Annette Bening'}
    ]
  },
  {
    '_id': 'tt0120586',
    'or_title': 'American History X',
    'pt_title': 'América Proibida',
    'year': '1998',
    'director': {'id': 'nm0443411', 'name': 'Tony Kaye'},
    'actors': [
      {'id': 'nm0001570', 'name': 'Edward Norton'}
    ]
  },
  {
    '_id': 'tt0114814',
    'or_title': 'The Usual Suspects',
    'pt_title': 'Os Suspeitos do Costume',
    'year': '1995',
    'director': {'id': 'nm0001741', 'name': 'Bryan Singer'},
    'actors': [
      {'id': 'nm0000228', 'name': 'Kevin Spacey'},
      {'id': 'nm0000321', 'name': 'Gabriel Byrne'},
      {'id': 'nm0001125', 'name': 'Benicio Del Toro'}
    ]
  },
]

# @bp.before_request
# def before_request():
#   g.locale = str(get_locale())

@bp.route('/')
@bp.route('/index')
def index():
  # movies=MOVIES
  movies = mongo.db.movies.aggregate([{'$sample': {'size': 10}}])
  # for m in movies:
  #   print(m)
  return render_template('index.html', movies=movies)

@bp.route('/new')
def new():
  return render_template('new.html')

@bp.route('/movie/<movie_id>')
def movie(movie_id):
  movie = {}
  for m in MOVIES:
    if m['_id'] == movie_id:
      movie = m
      break
  return render_template('movie.html', movie=movie)

@bp.route('/person/<person_id>')
def person(person_id):
  person = {}
  movies = []
  for m in MOVIES:
    for a in m['actors']:
      if a['id'] == person_id:
        movies.append(m)
        if not person:
          person = a
        break
    if m['director']['id'] == person_id:
      movies.append(m)
      if not person:
        person = m['director']
      break
  if not person:
    abort(404)
  print(person)
  return render_template('person.html', person=person, movies=movies)

@bp.route('/year/<year>')
def year(year):
  year = year
  movies = []
  for m in MOVIES:
    if m['year'] == year:
      movies.append(m)
  return render_template('year.html', year=year, movies=movies)
