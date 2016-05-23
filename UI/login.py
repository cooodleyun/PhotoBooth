from bottle import request, get, post, run, template
import bottle
import bottle_mysql 

#db
app = bottle.Bottle()
plugin = bottle_mysql.Plugin(dbuser='root', dbpass='22_ssol', dbname='test')
app.install(plugin)

#login view
@get('/login')
def login():
   return template('login_.tpl')

def check_login(username, password):
  if username=="aaa" and password=="pass":
	return True
  else:
	return False

#take a picture
@post('/camera')
def do_login():
  username = request.forms.get('username')
  password = request.forms.get('password')
  #login success
  if check_login(username,password):
	return template('login_success.tpl')
  #login fail    
  else:
	return template('login_fail.tpl')

#do join
@post('/join')
def join():
  return template('join_.tpl')

#see picture
@get('/gallery')
def gal() :
      return template('gallery_.tpl')

#passwd search
@post('/search')
def search():
   return template('search.tpl')

def check_pass(janswer):
  if janswer=="a":
	return True
  else:
	return False

#check input join_answer
@post('/pass')
def check_answer():
   janswer = request.forms.get('janswer')
   if check_pass(janswer):
      return template('pass_view.tpl')
   else :
      return template('pass_fail.tpl')

#join success
@get('/joinOk')
def joinOk():
   return template('join_success.tpl')

  
run(host='localhost', port=8080)
