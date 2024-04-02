from flask import render_template
from webapp import create_app
from webapp.model import News
from webapp.forms import LoginForm


app = create_app()
@app.route('/')
def index():
        title = "#without5minutescinema"
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template("index.html", page_title=title, news_list=news_list)

@app.route('/login')
def login():
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)