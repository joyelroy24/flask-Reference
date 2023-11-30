from flask import *
from database import *


public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():
    return render_template('home.html')


@public.route('/login',methods=['get','post'])
def login():
    if 'submit' in request.form:
        uname=request.form['uname']
        password=request.form['password']
        q="select * from login where user_name='%s' and password='%s'"%(uname,password)
        res=select(q)
        print(res)
        if res:
            session['lid']=res[0]['login_id']
        
            if res[0]['user_type']=='admin':
                return redirect(url_for('admin.adminhome'))
            elif res[0]['user_type']=='student':
                q="select * from login inner join students using(login_id) where login_id='%s'"%(session['lid'])
                res=select(q)
                session['name']=res[0]['first_name']
                return redirect(url_for('user.userhome'))
    return render_template('login.html')