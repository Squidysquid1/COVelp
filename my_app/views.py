# Views at the end of Workshop 2

from my_app import app, db
from flask import render_template, request, redirect
from my_app.models import Business, Review
from flask_googlemaps import GoogleMaps


# you can also pass the key here if you prefer
GoogleMaps(app, key="AIzaSyBt5Lfhuje_b-vNxcIEbkOvaRrhoP-M6pE")

name=""
facts = {"Birthday":"August 29th, 2001", "Favorite Color": "blue", "Favorite Hackathon": "HackMIT"}
posts = [{"title": "This is my 1st post!", "description": "this is my first description!"}]

db.create_all()

@app.route("/")
def index():
    #db_facts = Fact.query.all()
    #fact_dict = {fact.name: fact.value for fact in db_facts}

    #db_posts = Post.query.all()
    #post_list = [{"title": post.title, "description": post.description} for post in db_posts]
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template("index.html", mymap=mymap, sndmap=sndmap)

# @app.route("/change_name")
# def change_name():
#     global name
#     new_name = request.args.get('name')
#     name = new_name
#     return redirect("/")
#
# @app.route("/post", methods=["POST"])
# def post():
#     if request.method == "POST":
#         print(request)
#         post_info = request.get_json()
#         new_post = Post(title=post_info['title'], description=post_info['description'])
#         db.session.add(new_post)
#         db.session.commit()
#    return redirect("/")

# @app.route("/change_facts", methods=["POST"])
# def change_facts():
#     if request.method == "POST":
#         change_facts = request.get_json()
#         for key, value in change_facts.items():
#             if Fact.query.filter(Fact.name == key).first() is None:
#                 new_fact = Fact(name=key, value=value)
#                 db.session.add(new_fact)
#         db.session.commit()
#     return redirect("/")
