from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def cat_view(request):
    return Response({"GATOO": "MAIO MAIO MIAO"})
# Create your views here.
