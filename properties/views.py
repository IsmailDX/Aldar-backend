from django.shortcuts import render
from rest_framework import status
from .models import PropertiesDetails
from .serializers import PropertySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
# Create your views here.
def property_list(request):
    if request.method == "GET":
        properties = PropertiesDetails.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response({"properties": serializer.data})


@api_view(["GET"])
def property_list_by_id(request, id):
    try:
        if request.method == "GET":
            properties = PropertiesDetails.objects.filter(id=id)
            serializer = PropertySerializer(properties, many=True)
            return Response({"properties": serializer.data})
    except PropertiesDetails.DoesNotExist:
        return Response(
            {"error": "Property not found"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
def property_list_by_location(request, location):
    if request.method == "GET":
        properties = PropertiesDetails.objects.filter(location=location)
        serializer = PropertySerializer(properties, many=True)
        return Response({"properties": serializer.data})


@api_view(["GET"])
def property_list_by_project(request, project):
    if request.method == "GET":
        properties = PropertiesDetails.objects.filter(project=project)
        serializer = PropertySerializer(properties, many=True)
        return Response({"properties": serializer.data})


@api_view(["GET"])
def property_list_by_bedrooms(request, bedrooms):
    if request.method == "GET":
        properties = PropertiesDetails.objects.filter(bedrooms=bedrooms)
        serializer = PropertySerializer(properties, many=True)
        return Response({"properties": serializer.data})


@api_view(["GET"])
def property_list_by_bedrooms_and_project(request, bedrooms, project):
    if request.method == "GET":
        properties = PropertiesDetails.objects.filter(
            bedrooms=bedrooms, project=project
        )
        serializer = PropertySerializer(properties, many=True)
        return Response({"properties": serializer.data})


@api_view(["GET"])
def property_list_by_bedrooms_and_location(request, bedrooms, location):
    if request.method == "GET":
        properties = PropertiesDetails.objects.filter(
            bedrooms=bedrooms, location=location
        )
        serializer = PropertySerializer(properties, many=True)
        return Response({"properties": serializer.data})
