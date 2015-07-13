from pymongo import MongoClient
from django.shortcuts import render


def dashboard(request):
    context = {}
    client = MongoClient()
    db = client['Northwind']
    collections = db.collection_names(include_system_collections=False)
    context['collections'] = collections
    context['count_collections'] = []
    for col in collections:
        context['count_collections'].append([col, db[col].count()])

    return render(request, "dashboard.html", context)

def documents(request, collection=None):
    context = {}
    client = MongoClient()
    db = client['Northwind']
    context['collections'] = db.collection_names(include_system_collections=False)
    context['documents'] = db[collection].find()
    context['current_collection'] = collection
    context['document_keys'] = [k for k in db[collection].find_one()]
    return render(request, "dashboard_documents.html", context)