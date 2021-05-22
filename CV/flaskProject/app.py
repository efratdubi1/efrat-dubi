from flask import flaskProject, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/open')
@app.route('/')

@app.route('/main')
def main():
    return render_template('cv.html')

@app.route('/contactMe')
def contact():
    return render_template('CVcontactForm.html')

@app.route('/UserList')
def UsersList():
    return render_template('UsersList.html')

@app.route('/assignment8')
def assignment8_page():
    return render_template('assignment8.html', hobby2='Cooking', name="Efrat", hobbies=['Watching movies','reading','Drawing'])

@app.route('/assignment8_withoutBlock')
def assignment8Block():
    return render_template('assignment8_withoutBlock.html', hobby2='Cooking', name="Efrat", hobbies=['Watching movies','reading','Drawing'])

if __name__ == '__main__':
    app.run(debug=True)
