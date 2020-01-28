from flask import Flask,render_template

app=Flask(__name__)

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
def index():
    return render_template("home.html",posts=posts)


@app.route("/about")
def about():
     return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)