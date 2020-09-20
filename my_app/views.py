# Views at the end of Workshop 2

from my_app import app, db
from flask import render_template, request, redirect, url_for
from my_app.models import Business, Review

db.create_all()

@app.route("/")
def index():
    return render_template("index.html", reviews=[], business=[])

@app.route('/api', methods = ['GET'])
def review():
    if request.method == 'GET':

        place_id = request.args.get('id')
        b = [Business.query.filter(Business.place_id == place_id).first()] #all businesses
        rs = Review.query.filter(Business.place_id == place_id).all() # all reviews

        return render_template("index.html", reviews=rs, business=b)






# @app.route('/review-post', methods=['GET'])
# def post():
#     # if request.method == 'GET':
#     #     r = request.get_json()
#     #     review = Review(author_name=r[''], mask_required=r['reqScore'], mask_enforced=r['maskScore'], social_distance=r['sdScore'], busy=r['busyScore'])
#     #     db.session.add(review)
#     #     db.session.commit()
#
#     return redirect(url_for('index'))




'''
 @app.route("/review-business")
 def review_business():
     global name
     new_name = request.args.get('name')
     name = new_name
     return redirect("/")

 @app.route("/post", methods=["POST"])
 def post():
     if request.method == "POST":
         print(request)
         post_info = request.get_json()
         new_post = Post(title=post_info['title'], description=post_info['description'])
         db.session.add(new_post)
         db.session.commit()
    return redirect("/")

 @app.route("/change_facts", methods=["POST"])
 def change_facts():
     if request.method == "POST":
         change_facts = request.get_json()
         for key, value in change_facts.items():
             if Fact.query.filter(Fact.name == key).first() is None:
                 new_fact = Fact(name=key, value=value)
                 db.session.add(new_fact)
         db.session.commit()
     return redirect("/")
'''
