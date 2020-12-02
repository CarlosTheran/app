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
@app.route('/hadoop_new_folder', methods=['POST'])    
def hadoop_new_folder():
    # Example: /new_folder or /path/new_folder
    path = request.form['fpath']
    full_command = 'hadoop dfs -mkdir '+ path
    p = Popen(full_command , shell=True)
    return render_template('index.html')

@app.route('/hadoop_delete_folder', methods=['POST'])    
def hadoop_delete_folder():
    # Example: /new_folder or /path/new_folder
    path = request.form['fpath_delte']
    full_command = 'hadoop dfs -rm -r '+ path
    p = Popen(full_command , shell=True)
    return render_template('index.html')

@app.route('/hadoop_upload_data', methods=['POST'])    
def hadoop_upload_data():
    # Example: /ocal_path/new_data  /hdfs_path
    # hadoop dfs -put /home/ubuntu/data_covid/csv_covi19 /test_new_delete
    local_path = request.form['fpath_localFile']
    hdfs_path = request.form['fpath_hdfsFile']
    full_command = 'hadoop dfs -put '+ local_path + ' ' + hdfs_path
    p = Popen(full_command , shell=True)
    return render_template('index.html')  

@app.route('/hadoop_download_folder', methods=['POST'])    
def hadoop_download_folder():
    # Example: /ocal_path/new_data  /hdfs_path
    # hadoop dfs -get /test_new_delete/csv_covi19  /home/ubuntu
    #local_path = request.form['dpath_localFile']
    #hdfs_path = request.form['dpath_hdfsFile']
    full_command = 'hadoop dfs -get '+ hdfs_path + ' ' + local_path
    p = Popen(full_command , shell=True)
    return render_template('index.html')

@app.route('/ElemNet_code', methods=['POST'])    
def ElemNet_code():
    # Example: remember to have the corret path, <full_path>/name_file.py e.i. ~/ElemNet/elemnet/dl_regressors.py
    # and <initial_path>/sample/sample-run.config   e.i. ~/ElemNet/elemnet/sample/sample-run.config 
    #local_path = request.form['dpath_localFile']
    #hdfs_path = request.form['dpath_hdfsFile']
    full_command = 'spark-submit --master yarn --deploy-mode client ~/ElemNet/elemnet/dl_regressors.py --config_file ~/ElemNet/elemnet/sample/sample-run.config'
    p = Popen(full_command , shell=True)
    return render_template('index.html') 

@app.route('/IrNet_code', methods=['POST'])    
def IrNet_code():
    # Example: /ocal_path/new_data  /hdfs_path
    # hadoop dfs -get /test_new_delete/csv_covi19  /home/ubuntu
    #local_path = request.form['dpath_localFile']
    #hdfs_path = request.form['dpath_hdfsFile']
    full_command = 'spark-submit --master yarn --deploy-mode client ~/ElemNet/elemnet/dl_regressors_irnet.py --config_file ~/ElemNet/elemnet/sample/sample-run.config'
    p = Popen(full_command , shell=True)
    return render_template('index.html') 

@app.route('/SVM_code', methods=['POST'])    
def SVM_code():
    # Example: /ocal_path/new_data  /hdfs_path
    # hadoop dfs -get /test_new_delete/csv_covi19  /home/ubuntu
    #local_path = request.form['dpath_localFile']
    #hdfs_path = request.form['dpath_hdfsFile']
    full_command = 'spark-submit --master yarn --deploy-mode client ~/ElemNet/elemnet/dl_regressors_svm_spark.py --config_file ~/ElemNet/elemnet/sample/sample-run.config'
    p = Popen(full_command , shell=True)
    return render_template('index.html')                