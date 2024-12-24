from app.db.elastic_db import elastic_search_client
from flask import Blueprint, render_template

from app.repository.elastic_repo import search_historical_data, search_new_data, search_all_data, search_by_date_range
from app.services.elastic_mups import elastic_search_to_mup

elastic_queries_bluprint = Blueprint("elastic_queries", __name__)

client = elastic_search_client()
index_name = "terror"


# חיפוש במידע היסטורי עם טקסט
@elastic_queries_bluprint.route("/history/<txt>", methods=["GET"])
def get_historical_data(txt):
    historical_data = search_historical_data(client, index_name, txt)
    elastic_search_to_mup(historical_data)
    return render_template('elastic.html')


# חיפוש במידע חדש עם טקסט
@elastic_queries_bluprint.route("/news/<txt>", methods=["GET"])
def get_new_data(txt):
    news_data = search_new_data(client, index_name, txt)
    elastic_search_to_mup(news_data)
    return render_template('elastic.html')


# חיפוש בכל המידע עם טקסט
@elastic_queries_bluprint.route("/all/<txt>", methods=["GET"])
def get_all_data(txt):
    all_data = search_all_data(client, index_name, txt)
    print(len(all_data))
    elastic_search_to_mup(all_data)
    return render_template('elastic.html')


# חיפוש לפי טווח תאריכים עם טקסט
@elastic_queries_bluprint.route("/from/<start>/to/<end>/<txt>", methods=["GET"])
def get_by_date_range(start, end, txt):
    date_range = search_by_date_range(client, index_name, txt, start, end)
    elastic_search_to_mup(date_range)

    return render_template('elastic.html')
