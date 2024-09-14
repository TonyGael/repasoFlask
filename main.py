from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect('/show_information_address'))
    response.set_cookie('user_ip_information', user_ip_information)
    return response

@app.route('/show_information_address')
def show_information_address():
    user_ip = request.cookies.get('user_ip_information')
    return render_template('ip_information.html', user_ip = user_ip)

app.run(host='0.0.0.0', port=8080, debug=True)