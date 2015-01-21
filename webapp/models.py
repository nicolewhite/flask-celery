from webapp import celery
from py2neo import Graph, Node

@celery.task()
def create_node(name):
    graph = Graph()
    graph.create(Node('Person', name=name))
