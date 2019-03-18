from rest_framework import serializers
from app import models

class UploadPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UploadPic
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        uploadedPic = models.UploadPic.objects.create(**validated_data)
        return uploadedPic

    def update(self, instance, validated_data):
        instance.image_file = validated_data.get('image_file',instance.image_file)
        instance.save()
        return instance

class UserProfileSerialzer(serializers.ModelSerializer):
    image = UploadPicSerializer(read_only=True,required=False)
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password','image')
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
    id = serializers.IntegerField(required=False)
    class Meta:
        model = models.Comment
        fields = ('id','post','author','text','created_on','approved_on')
        read_only_fields = ('created_on','approved_on',)

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,required=False)
    class Meta:
        model = models.Post
        fields = ('id','user_profile','title','gener','text','created_on','published_on','comments')
        extra_kwargs = {'user_profile':{'read_only':True},'published_on':{'read_only':True},}
        depth = 1


class DraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id','user_profile','title','gener','text','created_on','published_on',)
        extra_kwargs = {'user_profile':{'read_only':True},'published_on':{'read_only':True},}
        depth = 1

    def create(self, validated_data):
        return models.Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.gener = validated_data.get('gener',instance.gener)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
    