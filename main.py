from flask import *
from public import public

app=Flask(__name__)
app.register_blueprint(public,url_prefic='/admi')


app.run(debug=True)