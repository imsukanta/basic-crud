from flask import Blueprint,render_template,request,redirect,url_for
from flaskr.models.user import User
from flaskr import db
bp=Blueprint('home',__name__)

@bp.route('/',methods=['GET','POST'])
def index():
    user=User.query.all()
    if request.method=='POST':
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        email=request.form['email']
        roll_no=request.form['roll_no']
        user=User(first_name=first_name,last_name=last_name,email=email,roll_no=roll_no)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template('index.html',user=user)

@bp.route('/update/<int:id>',methods=['POST','GET'])
def update_user(id):
    user=User.query.get(id)
    if request.method=="POST":
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        email=request.form['email']
        roll_no=request.form['roll_no']
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.roll_no=roll_no
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template("update.html",user=user)
@bp.route('/delete/<int:id>')
def delete_user(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home.index'))