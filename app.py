# import necessary libraries
import os
import numpy as np
import os

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
# postgres:postgres://avsrkdqtegxzjr:83afd61ef5b5b621120d83a053790a28f83ee6d60be17f55c4b19410737f0771@ec2-52-22-238-188.compute-1.amazonaws.com:5432/dcve1h312v0e62
try:
    db_uri = os.environ['DATABASE_URL']
except KeyError:
    db_uri = "postgres://postgres:PASSWORD@localhost:5432/DrugStudy_db"

print(db_uri)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)

# create class to frame each drug instance:

class Drug(db.Model):
    __tablename__="drug_data"

    state=db.Column(db.String(64))
    year=db.Column(db.String(64))
    month=db.Column(db.String(64))
    drug_name=db.Column(db.String(64))
    death_count=db.Column(db.Float)
    id = db.Column(db.Integer, primary_key=True)

    def  __repr__(self):
        return '<Drugs %r>' % (self.state)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/state<br/>"
        f"/api/v1.0/year<br/>"
        f"/api/v1.0/month<br/>"
        f"/api/v1.0/drug_name<br/>"
        f"/api/v1.0/death_count<br/>")
#################################################
# Rendering the Template
#################################################
# @app.route("/")     
# def enter_data(): 
#     return render_template("dataentry.html")

#################################################
# State Route
#################################################
@app.route("/api/v1.0/state")

def state():
    # Open a communication session with the database
    states_query= db.session.query(Drug.state).all()
    all_states=list(np.ravel(states_query))
    return jsonify(all_states)

#################################################
# Year Route
#################################################
@app.route("/api/v1.0/year")

def year():
    years_query= db.session.query(Drug.year).all()
    
    all_years=list(map(str,list(np.ravel(years_query))))
    return jsonify(all_years)
    

#################################################
# Month Route
#################################################
@app.route("/api/v1.0/month")

def month():
    months_query= db.session.query(Drug.month).all()
    all_months=list(np.ravel(months_query))
    return jsonify(all_months)
    
#################################################
# drug_name Route
#################################################
@app.route("/api/v1.0/drug_name")

def durgname():

    drugname_query= db.session.query(Drug.drug_name).all()
    
    all_years=list(np.ravel(drugname_query))
    return jsonify(all_years)
    
#################################################
# death_count Route
#################################################
@app.route("/api/v1.0/death_count")

def state_name():

    deathcount_query= db.session.query(Drug.death_count).all()
    deathcount=list(np.ravel(deathcount_query))
    return jsonify(deathcount)

if __name__ == "__main__":
    app.run(debug=True)
























