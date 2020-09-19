import pandas as pd
import numpy as np
from my_app.models import Business, Review
from my_app import app, db

def analysis(b_place_id=''):
    b = Business.query.filter_by(place_id=b_place_id).first()
    reviews = get_reviews(b.id)
    for review in reviews:
        review.

def get_reviews(business_id):
    return Review.query.filter(Business.id==business_id)
