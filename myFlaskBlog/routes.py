
from myFlaskBlog import app,bcrypt,db
from flask import  render_template, url_for, flash, redirect,request
from .forms import LoginForm, RegistrationForm
from .models import Post,User
from flask_login import current_user,logout_user,login_required,login_user


posts = [
    {
        'author': "younes",
        'title': 'Blog title 1',
        'content': "content blog 1",
        'date_posted': "april 20,2018",
    },
    {
        'author': "Hicham",
        'title': 'Blog title 2',
        'content': "content blog 2",
        'date_posted': "june 20,2018",
    },
]
@app.route("/")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Registration", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get("next")
            flash('You have been looged in', "success")
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title="Login", form=form)


@app.route("/account")
@login_required
def account():
    return render_template("account.html",title="account")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))
