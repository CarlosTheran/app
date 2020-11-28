from flask import render_template, request
from app import app
import subprocess
from subprocess import Popen
import sys
import cgi, cgitb
import pdb

@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
@app.route('/static/assets/vendor/bootstrap/css/bootstrap.min.css')
@app.route('/static/assets/vendor/jquery/jquery.min.js')
@app.route('/static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js')
@app.route('/static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js')
@app.route('/static/assets/vendor/counterup/counterup.min.js')
@app.route('/static/assets/vendor/php-email-form/validate.js')
@app.route('/static/assets/vendor/waypoints/jquery.waypoints.min.js')
@app.route('/static/assets/vendor/jquery.easing/jquery.easing.min.js')
@app.route('/static/assets/vendor/isotope-layout/isotope.pkgd.min.js')
@app.route('/static/assets/vendor/venobox/venobox.min.js')
@app.route('/static/assets/vendor/owl.carousel/owl.carousel.min.js')
@app.route('/static/assets/js/main.js')
@app.route('/static/assets/vendor/icofont/icofont.min.css')
@app.route('/static/assets/vendor/boxicons/css/boxicons.min.css')
@app.route('/static/assets/vendor/venobox/venobox.css')
@app.route('/static/assets/vendor/owl.carousel/assets/owl.carousel.min.css')
@app.route('/static/assets/css/style.css')
@app.route('/static/assets/img/about.png')
@app.route('/static/assets/img/hero-img.png')
@app.route('/static/assets/vendor/jquery.easing/jquery.easing.min.js')
@app.route('/static/assets/vendor/php-email-form/validate.js')
@app.route('/static/assets/vendor/waypoints/jquery.waypoints.min.js')
@app.route('/static/assets/vendor/isotope-layout/isotope.pkgd.min.js')
@app.route('/static/assets/vendor/venobox/venobox.min.js')
@app.route('/static/assets/vendor/owl.carousel/owl.carousel.min.js')
@app.route('/static/assets/js/main.js')
@app.route('/static/assets/img/apple-touch-icon.png')
@app.route('/static/assets/img/about.png')
@app.route('/static/assets/img/favicon.png')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    #render_template('index.html', title='Home', user=user, posts=posts)
    return render_template('index.html')
@app.route('/hadoop_new_folder', methods=['POST','GET'])    
def hadoop_new_folder():
    #the parameter path must start with the simbol /, e.x /path
    #form = cgi.FieldStorage()
    #if "fpath" not in form:
    #    print("<H1>Error</H1>")
    #    print("Please fill in the full path fields.")

    #print("<p>name:", form["fpath"].value)
    #path = form.getvalue('fpath')
    path = '/test_new_delete'
    #pdb.set_trace()
    #path = request.files['fpath']
    full_command = 'hadoop dfs -mkdir '+ path
    p = Popen(full_command , shell=True)
    #p.wait()
    #p = Popen('hadoop dfs -ls /' , shell=True)
    #output = p.stdout
    #return output