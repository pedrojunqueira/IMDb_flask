from flask import render_template, url_for
from imdb import app
from imdb.ml import clf, vect
from imdb.forms import ReviewForm
from imdb.app_utils import string_list
from imdb.models import Review
from imdb import db
from sqlalchemy import desc

label = {0: 'negative', 1: 'positive'}

@app.route('/', methods=['POST', 'GET'])
def newreview():
    form = ReviewForm()
    if form.validate_on_submit():
        review = string_list(form.content.data)
        X = vect.transform(review)
        prediction = label[clf.predict(X)[0]]
        probability = clf.predict_proba(X).max()*100
        review_label = form.label.data
        r = Review(body=form.content.data,prediction=prediction,probability=probability,label=review_label)
        db.session.add(r)
        db.session.commit()
        return render_template('result.html', review=review, prediction=prediction, probability=probability,
                               review_label=review_label)
    reviews = db.session.query(Review).order_by(desc(Review.timestamp)).limit(10)
    return render_template('new_review.html', form=form, reviews=reviews)
