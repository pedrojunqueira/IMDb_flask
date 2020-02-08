from flask import render_template, url_for
from imdb import app
from imdb.ml import clf, vect
from imdb.forms import ReviewForm
from imdb.app_utils import string_list

label = {0: 'negative', 1: 'positive'}

stored_predictions = [{'id': 1, 'review': 'This movie was good recommend!', 'prediction': 'positive', 'probability': '70%', 'label': 'positive'},
                      {'id': 2, 'review': 'Hated', 'prediction': 'negative',
                          'probability': '70%', 'label': 'negative'},
                      {'id': 3, 'review': 'Never see again :( horrible', 'prediction': 'positive',
                       'probability': '50%', 'label': 'negative'},
                      {'id': 4, 'review': 'Loved it!', 'prediction': 'positive',
                          'probability': '98%', 'label': 'positive'}
                      ]


@app.route('/', methods=['POST', 'GET'])
def newreview():
    form = ReviewForm()
    if form.validate_on_submit():
        review = string_list(form.content.data)
        X = vect.transform(review)
        prediction = label[clf.predict(X)[0]]
        probability = clf.predict_proba(X).max()*100
        review_label = form.label.data
        return render_template('result.html', review=review, prediction=prediction, probability=probability,
                               review_label=review_label)
    return render_template('new_review.html', form=form, predictions=stored_predictions)
