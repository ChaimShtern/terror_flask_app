from elasticsearch import Elasticsearch


def elastic_search_client():
    client = Elasticsearch(
        ['http://localhost:9200'],
        basic_auth=("elastic", "123456"),
        verify_certs=False
    )
    return client
