import pandas as pd
import numpy as np
from my_app.models import Business, Review
from my_app import app, db

def analysis(b_place_id=''):
    b = Business.query.filter_by(place_id=b_place_id).first()
    reviews = get_reviews(b.id)

    get_score()

    b.score =

    db.session.commit()

'''
mask_required = db.Column(db.Boolean) # boolean
mask_enforced = db.Column(db.Integer) #0 to 10
social_distance = db.Column(db.Integer) #0 to 10
busy = db.Column(db.Integer)
'''

def get_score(reviews):
    score = 0
    for review in reviews:
        review.mask_required
        review.mask_enforced
        review.social_distance
        review.busy

    return score


def get_reviews(business_id):
    return Review.query.filter(Business.id==business_id)
