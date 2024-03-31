from flask import render_template
from webapp import create_app
from webapp.model import News


app = create_app()
@app.route('/')
def index():
        title = "#without5minutescinema"
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template("index.html", page_title=title, news_list=news_list)
