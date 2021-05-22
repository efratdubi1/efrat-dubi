from flask import flaskProject, redirect, url_for, render_template, request, session, jsonify

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


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    username = ''
    if session['Logged_in']:
        username = session['username']
    users = [
        {'id': 1, 'firstName': "efrat", 'lastName': "dubi", 'age': 25},
        {'id': 2, 'firstName': "Michael", 'lastName': "Lawson", 'age': 22},
        {'id': 3, 'firstName': "Lindsay", 'lastName': "Ferguson", 'age': 25},
        {'id': 4, 'firstName': "Tobias ", 'lastName': "Funke", 'age': 18},
        {'id': 5, 'firstName': "Byron", 'lastName': "Fields", 'age': 20},
        {'id': 6, 'firstName': "George", 'lastName': "Edwards", 'age': 22},
        {'id': 6, 'firstName': "Rachel", 'lastName': "Howell", 'age': 41},
    ]
    firstname = ''
    if request.method == 'GET':
        if 'firstname' in request.args:
            firstname = request.args['firstname']
    if request.method == 'POST':
        if request.form["btn"] == "log out":
            session['Logged_in'] = False
            session['username'] = ''
            username = ''
        else:
            username = request.form['username']
            session['Logged_in'] = True
            session['username'] = username
    return render_template('assignment9.html',
                           request_method=request.method, username=username,
                           firstname=firstname, users=users)
