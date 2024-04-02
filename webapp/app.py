from flask import Flask, render_template
from webapp.model import News
from webapp.forms import LoginForm


app = Flask(__name__)
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

if __name__ == '__main__':
    app.run()