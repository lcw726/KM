from flask import jsonify, render_template, redirect, request, url_for
from flask import current_app as app
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from ..extensions import login_manager, ladp_auth
from . import blueprint
from .forms import LoginForm
from .models import User
import os, json


@blueprint.route('/')
def route_default():
    return redirect(url_for('base_blueprint.login'))


# @blueprint.route('/<template>')
# @login_required
# def route_template(template):
#     if template=='favicon.ico':
#         return redirect(url_for('base_blueprint.login'))

#     return render_template(template + '.html', reports=app.config['REPORTS'])


# @blueprint.route('/fixed_<template>')
# @login_required
# def route_fixed_template(template):
#     return render_template('fixed/fixed_{}.html'.format(template))


@blueprint.route('/page_<error>')
def route_errors(error):
    return render_template('errors/page_{}.html'.format(error))

@blueprint.route('/pdf_viewer')
@login_required
def pdf_viewer():
    cat = request.args.get('cat')
    index = int(request.args.get('ord'))

    file = app.config['REPORTS'][cat][index]['file']

    return render_template('pdf_viewer.html', file=file)

@blueprint.route('/report_list')
@login_required
def report_list(): 
    cat = request.args.get('cat')  
    title = app.config['TITLES'][cat] 
    reports = app.config['REPORTS'][cat]

    return render_template('report_list.html', cat=cat, title=title, reports=reports, len = len(reports))

## Login & Registration


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        username = request.form['username']

        auth = app.config['AUTH']

        if username in auth:
            if True:
                user = User(username)  

                login_user(user, remember=True)
                
                return redirect(url_for('home_blueprint.index'))
            else:
                status = '工號或密碼錯誤 !'
        else:
            status = "使用者未被授權 !"

        return render_template('login/login.html', login_form = login_form, status = status)

    if current_user.is_authenticated:
        return redirect(url_for('home_blueprint.index'))
    return render_template('login/login.html', login_form = login_form, status = '')
   
@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

## Errors


@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('base_blueprint.login'))


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('errors/page_404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/page_500.html'), 500
