from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from rest_framework.decorators import action

from app import serializers
from app import models
from app import permissions
from app.authtoken import CustomAuthToken


# Create your views here.
class LoginViewSet(viewsets.ViewSet):
    """checks email and password and return auth token"""
    serializer_class = AuthTokenSerializer

    def create(self,request):
        """use the ObtainAuthToken to validate and crate a token."""
        return CustomAuthToken().post(request)

class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerialzer
    queryset = models.UserProfile.objects.all()
    authentication_classes =(TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes=(IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('author','gener',)
    lookup_field = 'id'

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user_profile=self.request.user)

    @action(detail=True,methods=['GET'])
    def comments(self, request,id=None):
        post = self.get_object()
        comments = models.Comment.objects.filter(post=post)
        serializer = serializers.CommentSerializer()
        return Response(serializer.data,status=200)

    @action(detail=True,methods=['POST'])
    def comment(self, request,id=None):
        post = self.get_object()
        data = request.data
        data['post'] = post.id
        serializer = serializers.CommentSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.data,status=200)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('author',)