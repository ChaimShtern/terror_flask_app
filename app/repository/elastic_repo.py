from app.db.elastic_db import elastic_search_client


# פונקציה 1: חיפוש בכל המידע ההיסטורי
def search_historical_data(es_client, index_name, text):
    query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"new": False}},  # מחפש רק מסמכים ישנים
                    {"multi_match": {
                        "query": text,
                        "fields": ["city", "country", "region", "title"]  # שדות לחיפוש
                    }}
                ]
            }
        }
    }
    return es_client.search(index=index_name, body=query)['hits']['hits']


# פונקציה 2: חיפוש בכל המידע החדש
def search_new_data(es_client, index_name, text):
    query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"new": True}},  # מחפש רק מסמכים חדשים
                    {"multi_match": {
                        "query": text,
                        "fields": ["city", "country", "region", "title"]  # שדות לחיפוש
                    }}
                ]
            }
        }
    }
    return es_client.search(index=index_name, body=query)['hits']['hits']


# פונקציה 3: חיפוש בכל המידע (ישן וחדש)
def search_all_data(es_client, index_name, text):
    query = {
        "query": {
            "multi_match": {
                "query": text,
                "fields": ["city", "country", "region", "title"]  # שדות לחיפוש
            }
        }
    }
    return es_client.search(index=index_name, body=query)['hits']['hits']


# פונקציה 4: חיפוש לפי תאריך התחלה וסיום
def search_by_date_range(es_client, index_name, text, start_date, end_date):
    query = {
        "query": {
            "bool": {
                "must": [
                    {"range": {
                        "date": {
                            "gte": start_date,  # תאריך התחלה
                            "lte": end_date  # תאריך סיום
                        }
                    }},
                    {"multi_match": {
                        "query": text,
                        "fields": ["city", "country", "region", "title"]  # שדות לחיפוש
                    }}
                ]
            }
        }
    }
    return es_client.search(index=index_name, body=query)['hits']['hits']
