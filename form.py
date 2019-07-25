from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route('/')
def display_form():
    return render_template('form.html')


@app.route('/results', methods=['POST'])
def results():
    firstname = request.form.get('firstname', '')
    lastname = request.form.get('lastname', '')
    email = request.form.get('email', '')
    address = ' '.join([
        request.form.get('address1', ''),
        request.form.get('address2', ''),
        request.form.get('city', ''),
        request.form.get('state', ''),
        request.form.get('zip', ''),
    ])

    def phone_format(n):
        try:
            return format(int(n[:-1]), ",").replace(",", "-") + n[-1]
        except ValueError:
            return ""

    phone = phone_format(request.form.get('phoneno', ''))
    education = request.form.get('education', 'N/A')
    income = request.form.get('income', 'N/A')

    output = ''
    output += 'Name: {}\n'.format(firstname + ' ' + lastname)
    output += 'Email: {}\n'.format(email)
    output += 'Address: {}\n'.format(address)
    output += "Phone: {}\n".format(phone)
    output += "Education: {}\n".format(education)
    output += "Income: {}\n".format(income)

    return output.replace('\n', '<br />')


if __name__ == '__main__':
    app.run()
