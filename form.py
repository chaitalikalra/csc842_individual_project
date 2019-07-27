from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route('/')
def display_form():
    return render_template('form.html')


@app.route('/results', methods=['POST'])
def results():
    data = {}
    firstname = request.form.get('firstname', '')
    lastname = request.form.get('lastname', '')
    data['name'] = firstname + ' ' + lastname
    data['email'] = request.form.get('email', '')
    data['address'] = ' '.join([
        request.form.get('address1', ''),
        request.form.get('address2', ''),
        request.form.get('city', ''),
        request.form.get('state', ''),
        request.form.get('zip', ''),
    ])

    data['map_address'] = ' '.join([
        request.form.get('address1', ''),
        request.form.get('city', ''),
        request.form.get('state', ''),
        request.form.get('zip', ''),
    ])    

    def phone_format(n):
        try:
            return format(int(n[:-1]), ",").replace(",", "-") + n[-1]
        except ValueError:
            return ""

    data['phone'] = phone_format(request.form.get('phoneno', ''))
    education = request.form.get('education', '')
    if len(education) == 0:
        education = 'N/A'
    data['education'] = education
    income = request.form.get('income', '')
    if len(income) == 0:
        income = 'N/A'
    data['income'] = income

    return render_template('result.html', data=data)


if __name__ == '__main__':
    app.run()
