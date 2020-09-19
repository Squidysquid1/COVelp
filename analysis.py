import pandas as pd
import numpy as np
from my_app.models import Business, Review
from my_app import app, db

def analysis(b_place_id=''):
    b = Business.query.filter_by(place_id=b_place_id).first()
