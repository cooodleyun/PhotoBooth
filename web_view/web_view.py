#!/usr/bin/env python
#
# Copyright (C) 2013 Federico Ceratto and others, see AUTHORS file.
# Released under GPLv3+ license, see LICENSE.txt
#
# Cork example web application
#
# The following users are already available:
#  admin/admin, demo/demo

import bottle
from beaker.middleware import SessionMiddleware
from cork import Cork
from cork.backends import SQLiteBackend
import logging
from bottle import template
import os
import sqlite3
import RPi.GPIO as GPIO
import time
import picamera
from datetime import datetime

logging.basicConfig(format='localhost - - [%(asctime)s] %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)
bottle.debug(True)

def populate_backend():
    b = SQLiteBackend('webUser.db', initialize=False)

    b.connection.executescript("""
       
    """)
    return b

b = populate_backend()
aaa = Cork(backend=b, email_sender='sucuvu@gmail.com', smtp_url='starttls://sucuvu:2thfdutls@smtp.gmail.com:587')


app = bottle.app()
session_opts = {
    'session.cookie_expires': True,
    'session.encrypt_key': 'please use a random key and keep it secret!',
    'session.httponly': True,
    'session.timeout': 3600 * 24,  # 1 day
    'session.type': 'cookie',
    'session.validate_key': True,
}
app = SessionMiddleware(app, session_opts)

## image db ##
conn = sqlite3.connect('webUser.db')
c=conn.cursor()
#c.execute("CREATE TABLE img(_id INTEGER, name TEXT, image BLOB)")
print "db make success"

# #  Bottle methods  # #

def postd():
    return bottle.request.forms


def post_get(name, default=''):
    return bottle.request.POST.get(name, default).strip()


@bottle.post('/login')
def login():
    """Authenticate users"""
   # os.system("sh /home/pi/Desktop/web_view/start_stream.sh")
    username = post_get('username')
    password = post_get('password')
    aaa.login(username, password, success_redirect='/', fail_redirect='/login')

@bottle.route('/user_is_anonymous')
def user_is_anonymous():
    if aaa.user_is_anonymous:
        return 'True'

    return 'False'

@bottle.route('/logout')
def logout():
    aaa.logout(success_redirect='/login')

@bottle.post('/join_btn')
def join_btn():
    return template('join_form.tpl')

@bottle.post('/register')
def register():
    """Send out registration email"""
    aaa.register(post_get('username'), post_get('password'), post_get('email_address'))
    return template('register.tpl')


@bottle.route('/validate_registration/:registration_code')
def validate_registration(registration_code):
    """Validate registration, create user account"""
    aaa.validate_registration(registration_code)
    return 'Thanks. <a href="/login">Go to login</a>'


@bottle.post('/reset_passwd')
def reset_passwd():
    return template('reset_passwd.tpl')

@bottle.post('/reset_password')
def send_password_reset_email():
    """Send out password reset email"""
    aaa.send_password_reset_email(
        username=post_get('username'),
        email_addr=post_get('email_address')
    )
    return 'Please check your mailbox.'


@bottle.route('/change_password/:reset_code')
@bottle.view('password_change_form')
def change_password(reset_code):
    """Show password change form"""
    return dict(reset_code=reset_code)


@bottle.post('/change_password')
def change_password():
    """Change password"""
    aaa.reset_password(post_get('reset_code'), post_get('password'))
    return 'Thanks. <a href="/login">Go to login</a>'


@bottle.route('/')
def index():
    """Only authenticated users can see this"""
    aaa.require(fail_redirect='/login')
    return template('camera_form.tpl')

#Button
@bottle.post('/ppic')
def btnClick():
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(18, GPIO.IN) #button
  GPIO.setup(23, GPIO.OUT) #green
  GPIO.setup(14, GPIO.OUT) #yellow
  GPIO.setup(25, GPIO.OUT) #red

  with picamera.PiCamera() as camera:
    camera.resolution=(400, 300)
    camera.start_preview()
    GPIO.wait_for_edge(18, GPIO.FALLING)
    try:  
        input_value = GPIO.input(18)

        if input_value == False:
            # print "picture~"
             GPIO.output(23, True)
             time.sleep(1)
             GPIO.output(14, True)
             time.sleep(1)
             GPIO.output(25, True)
             time.sleep(1)
             camera.capture('/var/www/html/temp/pic.jpg')
             camera.stop_preview()
             camera.close()    
             GPIO.output(23, False)
             GPIO.output(14, False)
             GPIO.output(25, False)
        else :
            GPIO.output(23, False)
            time.sleep(1)
            GPIO.output(14, False)
            time.sleep(1)
            GPIO.output(25, False)
            time.sleep(1)

    except KeyboardInterrupt:
     GPIO.cleanup()
    return template('print_form.tpl')
     
@bottle.post('/camera')
def camera():
    return template('camera_form.tpl')

@bottle.post('/printOption')
def printOption():
    return template('print_form.tpl')

@bottle.post('/gall')
def gall():
    os.system("sh /home/pi/Desktop/web_view/print.sh")
    return template('gall_form.tpl')

@bottle.route('/restricted_download')
def restricted_download():
    """Only authenticated users can download this file"""
    aaa.require(fail_redirect='/login')
    return bottle.static_file('static_file', root='.')


@bottle.route('/my_role')
def show_current_user_role():
    """Show current user role"""
    session = bottle.request.environ.get('beaker.session')
    print "Session from simple_webapp", repr(session)
    aaa.require(fail_redirect='/login')
    return aaa.current_user.role


# Admin-only pages

@bottle.route('/admin')
@bottle.view('admin_page')
def admin():
    """Only admin users can see this"""
    aaa.require(role='admin', fail_redirect='/sorry_page')
    return dict(
        current_user=aaa.current_user,
        users=aaa.list_users(),
        roles=aaa.list_roles()
    )

#create user
@bottle.post('/create_user')
def create_user():
    try:
        aaa.create_user(postd().username, postd().role, postd().password)
        return dict(ok=True, msg='')
    except Exception, e:
        return dict(ok=False, msg=e.message)


@bottle.post('/delete_user')
def delete_user():
    try:
        aaa.delete_user(post_get('username'))
        return dict(ok=True, msg='')
    except Exception, e:
        print repr(e)
        return dict(ok=False, msg=e.message)


@bottle.post('/create_role')
def create_role():
    try:
        aaa.create_role(post_get('role'), post_get('level'))
        return dict(ok=True, msg='')
    except Exception, e:
        return dict(ok=False, msg=e.message)


@bottle.post('/delete_role')
def delete_role():
    try:
        aaa.delete_role(post_get('role'))
        return dict(ok=True, msg='')
    except Exception, e:
        return dict(ok=False, msg=e.message)


# Static pages

@bottle.route('/login')
@bottle.view('login_form')
def login_form():
    """Serve login form"""
    return {}


@bottle.route('/sorry_page')
def sorry_page():
    """Serve sorry page"""
    return '<p>Sorry, you are not authorized to perform this action</p>'


# #  Web application main  # #

def main():

    # Start the Bottle webapp
    bottle.debug(True)
    bottle.run(app=app, quiet=False, reloader=False)

if __name__ == "__main__":
    main()


