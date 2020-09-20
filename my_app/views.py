from my_app import app, db
from flask import render_template, request, redirect, url_for, flash, session
from my_app.models import Business, Review
import json
#from analysis import analysis_of_b
db.create_all()

@app.route("/")
def index():
    b = []
    rs = []
    # if request.args['messages']:
    #     data = request.args['messages']
    #     data = session['messages']
    #     place_name = data[0]
    #     place_id = data[1]
    #     b = [Business.query.filter(Business.place_id == place_id).first()]
    #     rs = Review.query.filter_by(business_id=place_id).all() # all reviews
    #     return render_template("index.html", reviews=r, business=bs)

    return render_template("index.html", reviews=rs, business=b)

@app.route('/api', methods = ['POST'])
def review():
    b = []
    rs = []
    if request.method == 'POST':
        data = request.form["name"].split('.')
        place_name = data[0]
        place_id = data[1]

        search_b = Business.query.filter(Business.place_id == place_id).first()

        if not search_b:
            b = Business(place_id=place_id, business_name=place_name)
            db.session.add(b)
            db.session.commit()

        analysis_of_b(place_id)
        b = [Business.query.filter(Business.place_id == place_id).first()]
        rs = Review.query.filter_by(business_id=place_id).all() # all reviews

        return redirect(render_template("index.html", reviews=rs, business=b))
        # db.session.commit()
        # return place_name
        #return data #render_template("index.html", reviews=rs, business=b)
    #return render_template("index.html", reviews=rs, business=b)

def analysis_of_b(b_place_id):
    b = Business.query.filter_by(place_id=b_place_id).first()
    reviews = Review.query.filter_by(business_id=b_place_id).all()
    if type(reviews) is None:
        b.avg_mask_enforced = 0
        b.avg_mask_required = 0
        b.avg_social_distance = 0
        b.score = 0
    else:
        b.avg_mask_enforced = get_mask_enforced(reviews)
        b.avg_mask_required = get_required(reviews)
        b.avg_social_distance = get_social_distance(reviews)
        b.busy = get_busy(reviews)

        b.score = get_score(reviews, a=1, b=1, c=1, d=1.3) #a, b, c, d are parameters

    db.session.commit()


def get_required(reviews):
    count = 0
    for review in reviews:
        if review.mask_required:
            count += 1
        else:
            count -= 1

    return count > 0

def get_social_distance(reviews):
    total = 0
    if reviews:
        for review in reviews:
            total += review.mask_enforced

        return total / len(reviews)
    else:
        return 0

def get_mask_enforced(reviews):
    total = 0
    if reviews:
        for review in reviews:
            total += review.mask_enforced

        return total / len(reviews)
    else:
        return 0

def get_busy(reviews):
    total = 0
    if reviews:
        for review in reviews:
            if review:
                total += review.busy

        return total / len(reviews)
    else:
        return 0

def get_score(reviews, a=1, b=1, c=1, d=1):
    score = 0
    if reviews:
        for r in reviews:
            mask_enforced = 4
            social_distance = 5
            mask_required = 3
            busy = 1
            score += a*(r.mask_enforced + r.social_distance + (10 - r.busy)) / 4 +\
               b*(int(r.mask_required) * (r.social_distance + (10 - r.busy)))/(11 - r.mask_enforced) +\
               c*(int(r.mask_required)*(r.social_distance*1.15 + r.mask_enforced))/(r.busy+1) +\
               d*(int(r.mask_required)*(r.mask_enforced + (10 - r.busy)))/(11 - r.social_distance)

        return min((score / 3) / len(reviews), 10)
    else:
        return 0




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
