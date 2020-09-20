from my_app import db
import json

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

	score = db.Column(db.Float)

	reviews = db.relationship('Review', backref='Business', lazy=True)

	def __repr__(self): #returns json object for javascript
		b = {'business_name' : self.business_name,
			 'avg_mask_required' : self.avg_mask_required,
			 'avg_busy' : self.avg_busy,
			 'avg_mask_enforced' : self.avg_mask_enforced,
			 'avg_social_distance' : self.avg_social_distance,
			 'score' : self.score}

		return json.dumps(b)

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

	def __repr__(self): #returns json object for javascript
		r = {'author_name' : self.author_name,
			 'mask_required' : self.mask_required,
			 'social_distance' : self.social_distance,
			 'busy' : self.busy,
			 'text' : self.text,
			 'time' : self.time}
		return json.dumps(r)

@app.route('')
