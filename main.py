from flask import *
from public import public
from admin import admin
from user import user

app=Flask(__name__)
app.secret_key='heyy'
app.register_blueprint(public,url_prefic='/public')
app.register_blueprint(admin)
app.register_blueprint(user)


app.run(debug=True)