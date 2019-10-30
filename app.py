from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('form.html')


@app.route('/poster')
def create_poster(title="EVENT TITLE HERE", date="DATEHERE", time="TIMEHERE", location = "LOCATION HERE"):

    title = request.args.get('title') or title
    date = request.args.get('date') or date
    time = request.args.get('time') or time
    location = request.args.get('location') or location

    return render_template('study-jam.html', title=title, date=date, time=time, location=location)

if __name__ == '__main__':
    app.run(debug=True)
