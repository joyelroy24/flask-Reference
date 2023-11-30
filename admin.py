from flask import *
from database import *


admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def adminhome():
    return render_template('adminhome.html')

@admin.route('/manage_courses',methods=['get','post'])
def manage_courses():
    data={}
    if 'submit' in request.form:
        cname=request.form['cname']
        upload=request.files['upload']
        imgpath='static/'+str(upload.filename)
        upload.save(imgpath)
        q="insert into courses values(NULL,'%s','%s')"%(cname,imgpath)
        insert(q)
        return redirect(url_for('admin.manage_courses'))

    course="select * from courses"
    res=select(course)
    data['course']=res
    print(res)
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='delete':
        q="delete from courses where course_id='%s'"%(id)
        delete(q)
        return redirect(url_for('admin.manage_courses'))
    if action=='update':
        q="select * from courses where course_id='%s'"%(id)
        res=select(q)
        data['updater']=res

    if 'update' in request.form:
        cname=request.form['cname']
        upload=request.files['upload']

        path='static/'+str(upload.filename)
        upload.save(path)
        q="update courses set course_name='%s',image='%s' where course_id='%s'"%(cname,path,id)
        print(q)
        update(q)
        return redirect(url_for('admin.manage_courses'))
    

    return render_template('manage_courses.html',data=data)

