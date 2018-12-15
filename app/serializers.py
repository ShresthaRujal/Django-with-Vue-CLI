from rest_framework import serializers
from app import models

class HelloSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=25)

class UserProfileSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('post','author','text','created_on','approved_on')
        read_only_fields = ('created_on','approved_on',)

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,required=False)
    class Meta:
        model = models.Post
        fields = ('id','user_profile','title','gener','text','created_on','published_on','comments')
        extra_kwargs = {'user_profile':{'read_only':True},'published_on':{'read_only':True},}
