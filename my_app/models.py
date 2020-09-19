from my_app import db

class Business(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	#google information
	business_name = db.Column(db.String(500))
	place_id = db.Column(db.String(200), unique=True, nullable=False)

	#crowdsourced data
	avg_mask_required = db.Column(db.Boolean) # boolean
	avg_mask_enforced = db.Column(db.Float) #0 to 10
	avg_busy = db.Column(db.Float)
	avg_social_distance = db.Column(db.Float) #0 to 10

class Review(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author_name = db.Column(db.String(250), nullable=False)
    #crowdsourced data
	mask_required = db.Column(db.Boolean) # boolean
	mask_enforced = db.Column(db.Integer) #0 to 10
	social_distance = db.Column(db.Integer) #0 to 10
	busy = db.Column(db.Integer)
	text = db.Column(db.String(500))
	time = db.Column(db.DateTime, nullable=False)

	business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
