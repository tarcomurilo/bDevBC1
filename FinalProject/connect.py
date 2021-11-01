import sqlalchemy as sqla
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from flask import Flask
import requests
from flask import request as flaskreq
from sqlalchemy.sql.expression import column
from werkzeug.utils import redirect
from bs4 import BeautifulSoup as htmlparser
import feedparser as feed
import datetime

# init configuring flask
app = Flask(__name__)
port = 5300

decBase = declarative_base()

# engine to connect to the file (echo to see the string parsing)


class News(decBase):  # class to create a table
    __tablename__ = 'news'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String)
    summary = Column('summary', String)
    clicks = Column('clicks', Integer)
    url = Column('url', String, unique=True)


def addNewsRow(title, summary, url):
    news = News()
    news.title = title
    news.summary = summary
    news.clicks = 0
    news.url = url
    return news


eng = sqla.create_engine('sqlite:///c:\\sqlite\\database.db', echo=False)
decBase.metadata.create_all(bind=eng)  # bind the base to the engine
Session = sessionmaker(bind=eng)


@app.route("/")
def aggregator():

    def catchRSS(feedUrl):
        feeding = feed.parse(feedUrl)
        articles = feeding['entries']

        for article in articles:
            session = Session()

            inTitle = article.get("title")
            inSum = article.get("description")
            inUrl = article.get("link")
            try:
                session.add(addNewsRow(inTitle, inSum, inUrl))
                session.commit()
            except:
                pass

            session.close()

    def catchHTML(HTMLURL):
        content = requests.get(HTMLURL)

        content = htmlparser(content.text, 'html.parser')

        allH3 = content.find_all('h3')

        for title in allH3:

            link = title.find_previous('a')
            print(link.get('href'), ' - ', title.text)

            # try
            session = Session()

            inTitle = title.text
            inSum = title.text
            inUrl = link.get('href')
            try:
                session.add(addNewsRow(inTitle, inSum, inUrl))
                session.commit()
            except:
                pass

            session.close()
            # end try

    FEEDURL = "http://rss.uol.com.br/feed/tecnologia.xml"
    # catchRSS(FEEDURL)
    FEEDURL = "https://www.inovacaotecnologica.com.br/boletim/rss.xml"
    catchRSS(FEEDURL)
    FEEDURL = "https://www.theverge.com/rss/index.xml"
    catchRSS(FEEDURL)
    FEEDURL = "https://techcrunch.com/feed/"
    catchRSS(FEEDURL)
    FEEDURL = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
    catchRSS(FEEDURL)
    FEEDURL = "https://mashable.com/feeds/rss/all"
    catchRSS(FEEDURL)
    HTMLURL = 'https://www.uol.com.br/tilt/'
    catchHTML(HTMLURL)

    session = Session()

    news = session.query(News).all()

    retString = '<html><style>img { max-width: 200px; height:auto}</style></html<body>'
    retString = retString + '<h1>Latest news - Tarço aggregator - ' + \
        format(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')+'</h1>'

    for titles in news:
        retString = retString + '<p><hr>Title: ' + titles.title + \
            '<br><br>Summary: ' + titles.summary + '</p><br>'
        retString = retString + '<p>Address: <a href="click?addr=' + titles.url + \
            '">'+titles.url+'"</a> - Clicks: ' + \
            str(titles.clicks)+'</p><p></p><br><br><br>'

    retString = retString + '</body></html>'
    session.close()

    return retString


@app.route('/click', methods=['GET'])
def clickCounter():

    session = Session()
    entrie = session.query(News).filter_by(
        url=flaskreq.args.get('addr')).first()

    try:
        entrie.clicks = entrie.clicks + 1
        retString = entrie.url
        session.commit()

    except:
        retString = flaskreq.args.get('addr')
        print(retString)

    session.close()
    return redirect(retString)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
