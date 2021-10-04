from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class SongList(APIView):

    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)

class SongNew(APIView):

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    def get(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self, request, pk):
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        song = self.get_object(pk)
        song.delete()
        return Response(status.HTTP_200_OK) 
    
class getLikes(APIView):
    
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def put(self, request, pk):
        song = self.get_object(pk)
        song.like_counter+=1
        song.save()
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_200_OK)