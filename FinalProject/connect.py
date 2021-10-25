import sqlalchemy as sqla
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from flask import Flask
from flask import request as flaskreq
from sqlalchemy.sql.expression import column
from werkzeug.utils import redirect
from werkzeug.wrappers import request
import feedparser as feed
import datetime

# init configuring flask
app = Flask(__name__)
port = 5300

decBase = declarative_base()

# engine to connect to the file (echo to see the string parsing)

class News(decBase):  # class to create a table
    __tablename__ = 'news'

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String)
    summary = Column('summary', String)
    clicks = Column('clicks', Integer)
    url = Column('url', String, unique=True)

def addNewsRow(id, title, summary, url):
    news = News()
    news.id = id
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

            news = session.query(News).all()
            lastId = -1
            for id in news:
                if id.id >= lastId:
                    lastId = id.id + 1

            inTitle = article.get("title")
            inSum = article.get("description")
            inUrl = article.get("link")
            try:
                session.add(addNewsRow(lastId, inTitle, inSum, inUrl))
                session.commit()
            except:
                pass

            session.close()

    FEEDURL = "http://rss.uol.com.br/feed/tecnologia.xml"
    catchRSS(FEEDURL)  
    FEEDURL = "https://www.inovacaotecnologica.com.br/boletim/rss.xml"
    catchRSS(FEEDURL)
    #FEEDURL = "https://www.theverge.com/rss/index.xml"
    #catchRSS(FEEDURL)
    #FEEDURL = "https://techcrunch.com/feed/"
    #catchRSS(FEEDURL)
    #FEEDURL = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
    #catchRSS(FEEDURL)
    #FEEDURL = "https://mashable.com/feeds/rss/all"
    #catchRSS(FEEDURL) 

    session = Session()

    news = session.query(News).all()
    
    retString = '<html><style>img { max-width: 200px; height:auto}</style></html<body>'
    retString = retString + '<h1>Latest news - Tarço aggregator - '+ format(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')+'</h1>'

    for titles in news:
        retString = retString + '<p><hr>Title: ' + titles.title +  '<br><br>Summary: ' +  titles.summary + '</p><br>'
        retString = retString + '<p>Address: <a href="click?addr=' + titles.url + '">'+titles.url+'"</a> - Clicks: '+str(titles.clicks)+'</p><p></p><br><br><br>'
    
    retString = retString + '</body></html>'
    session.close()

    return retString
    
@app.route('/click', methods=['GET'])
def clickCounter():

    session = Session()
    entrie = session.query(News).filter_by(url=flaskreq.args.get('addr')).first()
    
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

# gui
its_on = True

while its_on:
    if its_on == False:
        exit()

    print('Type a number of command:')
    print('1: Input data in news table')
    print('2: consult the table')
    print('0: to exit the program')

    intext = input('> ')

    if intext == '0':
        its_on == False
        session.close()
        exit()

    elif intext == '1':
        session = Session()
        news = session.query(News).all()
        lastId = 0

        for id in news:
            if id.id >= lastId:
                lastId = id.id + 1

        print('Put the title')
        inTitle = input('> ')
        print('Put the summary')
        inSum = input('> ')
        print('Put the url')
        inUrl = input('> ')
        session.add(addNewsRow(lastId, inTitle, inSum, inUrl))
        session.commit()

    elif intext == '2':
        session = Session()
        print('Which ID do you want to see (a integer):')
        idIn = int(input('ID: '))
        news = session.query(News).all()
        for titles in news:
            print('Titles: ', titles.title, '- Summary: ', titles.summary)

    session.close()
