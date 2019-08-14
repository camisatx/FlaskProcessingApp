from flask import abort, Flask, jsonify, render_template
from flask_wtf.csrf import CSRFProtect

from model import ProcessForm


#--------------------- Initialize the Flask app ------------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a super secret key you should change'
csrf = CSRFProtect(app)


#----------------- Example of loading a blueprint route ----------------------
# Add a blueprint for routes in the /api/v1 folder
from api.v1 import bp as api_v1_bp    # NOQA
app.register_blueprint(api_v1_bp, url_prefix='/api/v1')


#------------------- Non-API route that retuns an html object ----------------
@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page. Show the process form and validate it on POST request."""
    form = ProcessForm()
    if form.validate_on_submit():
        #Run function
        for i in range(10):
            print(i)
    return render_template('index.html', form=form)


#---------------------- API route that retuns a json object ------------------
# Example data object. This could originate from a file, database, or process.
planets_data = {
    'mercury': {'name': 'Mercury', 'radius': 2440},
    'venus': {'name': 'Venus', 'radius': 6052},
    'earth': {'name': 'Earth', 'radius': 6371},
    'mars': {'name': 'Mars', 'radius': 3390},
    'jupiter': {'name': 'Jupiter', 'radius': 69911},
    'saturn': {'name': 'Saturn', 'radius': 58232},
    'uranus': {'name': 'Uranus', 'radius': 25362},
    'neptune': {'name': 'Neptune', 'radius': 24622},
}


@app.route('/planets', methods=['GET'])
def planets():
    return jsonify(planets_data)


@app.route('/planets/<name>', methods=['GET'])
def planet(name):
    if planets_data.get(name):
        return jsonify(planets_data[name])
    else:
        abort(404)


#--------------------- Required to make the app run! -------------------------
if __name__ == '__main__':
    app.run(debug=False, port=5001)
