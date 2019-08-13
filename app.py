from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

from model import ProcessForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'this is a super secret key you should change'

csrf = CSRFProtect(app)

# Add a blueprint for routes in the /api/v1 folder
from api.v1 import bp as api_v1_bp    # NOQA
app.register_blueprint(api_v1_bp, url_prefix='/api/v1')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ProcessForm()
    if form.validate_on_submit():
        #Run function
        for i in range(10):
            print(i)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=False, port=5001)
