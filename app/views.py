from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework import filters
from rest_framework.decorators import action

from app import serializers
from app import models
from app import permissions
from app.authtoken import CustomAuthToken


# Create your views here.
class LoginViewSet(viewsets.ViewSet):
    """checks email and password and return auth token"""
    print('hllo')
    serializer_class = AuthTokenSerializer

    def create(self,request):
        """use the ObtainAuthToken to validate and crate a token."""
        return CustomAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset =  models.ProfileFeedItem.objects.all()

    def perform_create(self, serilizer):
        serilizer.save()

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerialzer
    queryset = models.UserProfile.objects.all()
    authentication_classes =(TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.exclude(published_on__isnull=True).order_by('-published_on')
    authentication_classes = (TokenAuthentication,)
    permission_classes=(IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('author','gener',)
    lookup_field = 'id'
    # http_method_names = ['get', 'put', 'delete','patch']

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user_profile=self.request.user)

    @action(detail=True,methods=['GET'])
    def comments(self, request,id=None):
        post = self.get_object()
        comments = models.Comment.objects.filter(post=post)
        serializer = serializers.CommentSerializer(comments)
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


class DraftViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DraftSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = models.Post.objects.filter(published_on__isnull=True).filter(user_profile_id=user_id).order_by('-created_on')
        return queryset
    
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user_profile=self.request.user)

    @action(detail=True,methods=['GET'])
    def publish(self, request,id=None):
        draft = self.get_object()
        draft.publish()
        serializer = serializers.DraftSerializer(draft)
        return Response(serializer.data,status=200)

    # http_method_names = ['get', 'put', 'delete','patch']
    # serializer_class = serializers.PostSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes=(IsAuthenticated,)

    # def list(self, request):
    #     print(request.data)
    #     queryset = models.Post.objects.filter(published_on__isnull=True)
    #     serializer = serializers.PostSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = models.Post.objects.get(pk=pk)
    #     serializer = serializers.PostSerializer(queryset)
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     instance = models.Post.objects.get(pk=pk)
    #     serializer = serializers.PostSerializer(instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    # def partial_update(self, request, pk=None):
    #     instance = models.Post.objects.get(pk=pk)
    #     print()
    #     pass

    # def destroy(self, request, pk=None):
    #     instance = models.Post.objects.get(pk=pk)
    #     instance.delete()    
    #     return Response(status=202)