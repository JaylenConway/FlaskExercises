from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}

orgs = ["Jedi Order", "Mandalorians", "Rebel Alliance", "Hutts", "Trade Federation"]

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':

        name = request.form['name']
        organization = request.form['organization']

        if not name:
            error = 'Name is required.'
        elif not organization:
            error = 'Organization is required.'
        elif organization not in orgs:
            error = 'Invalid organization.'
        elif name in users:
            rror = 'This name has already been registered for an organization.'
        else:
             users[name] = organization
             return redirect(url_for('registered_users'))

    return render_template('home.html', error=error, organizations=orgs) 

@app.route('/registered_users')
def registered_users():   
    return render_template('registered_users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)