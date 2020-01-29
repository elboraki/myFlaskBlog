from flask import Flask,render_template,url_for,flash,redirect
from forms import LoginForm,RegistrationForm
app=Flask(__name__)

app.config['SECRET_KEY']="e3bb04e3fcf9d0e6f0df7feaeed28f96"
posts=[
    {
        'author':"younes",
        'title':'Blog title 1',
        'content':"content blog 1",
        'date_posted':"april 20,2018",
    },
        {
        'author':"Hicham",
        'title':'Blog title 2',
        'content':"content blog 2",
        'date_posted':"june 20,2018",
    },
]
@app.route("/")
def home():
    return render_template("home.html",posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html",title="Registration",form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='younes@self.me' and form.password.data=='123123':
            flash('You have been looged in',"success")
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html",title="Login",form=form)

if __name__ == "__main__":
    app.run(debug=True)