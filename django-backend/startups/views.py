from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.mongo import db

@api_view(["GET"])
def health_check(request):

    collections = db.list_collection_names()

    return Response({
        "status": "MongoDB Connected Successfully",
        "database": "venturepulse",
        "collections": collections
    })