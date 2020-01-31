from flask import Flask, render_template
from models import clf, vect
from forms import ReviewForm
from app_utils import string_list

app = Flask('__name__')

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba243'

label = {0: 'negative', 1: 'positive'}


@app.route('/', methods=['POST','GET'])
def newreview():
    form = ReviewForm()
    if form.validate_on_submit():
        review = string_list(form.content.data)
        X = vect.transform(review)
        prediction = label[clf.predict(X)[0]]
        probability = clf.predict_proba(X).max()*100
        return render_template('result.html', review=review, prediction=prediction, probability=probability)
    return render_template('new_review.html',form=form)


if __name__ == "__main__":
    app.run(port=5000,debug=True)
