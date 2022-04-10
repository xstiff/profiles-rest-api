from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello! :D', 'an_apiview':an_apiview})

    def post(self, request, format=None):
        """Hello message with our name :D"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
             )

    def put(self, request, pk=None):
        """Update an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Partial update of object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test Api ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """ return message """
        a_viewset= [

            'Uses action (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'

        ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})

    def create(self, request):
        """ Create new hello message """
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
             name = serializer.validated_data.get('name')
             message = f'Hello {name}'
             return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handle getting an object by pk """
        return Response({'http_method':"GET"})


    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({"http_method":"UPDATE"})

    def partial_update(self,request, pk=None):
        """Handle updating part of object"""
        return Response({'http_method':"patch"})

    def destroy(self,request,pk=None):
        """destroy an object"""
        return Response({'http_method':"destroy"})
