import pandas as pd
import numpy as np
from my_app.models import Business, Review
from my_app import app, db

def analysis(b_place_id=''):
    b = Business.query.filter_by(place_id=b_place_id).first()
    reviews = get_reviews(b.id)

    b.avg_busy = get_busy(reviews)
    b.avg_mask_enforced = get_mask_enforced(reviews)
    b.avg_mask_required = get_required(reviews)
    b.avg_social_distance = get_social_distance(reviews)

    b.score = get_score(reviews, a=1, b=1, c=1, d=1.3) #a, b, c, d are parameters

    db.session.commit()

'''
mask_required = db.Column(db.Boolean) # boolean
mask_enforced = db.Column(db.Integer) #0 to 10
social_distance = db.Column(db.Integer) #0 to 10
busy = db.Column(db.Integer)
'''


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
    for review in reviews:
        total += review.mask_enforced

    return total / len(reviews)

def get_mask_enforced(reviews):
    total = 0
    for review in reviews:
        total += review.mask_enforced

    return total / len(reviews)

def get_busy(reviews):
    total = 0
    for review in reviews:
        total += review.busy

    return total / len(reviews)

def get_score(reviews, a=1, b=1, c=1, d=1):
    score = 0
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


def get_reviews(business_id):
    return Review.query.filter(Business.id==business_id)
