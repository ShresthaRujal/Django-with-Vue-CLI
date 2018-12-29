from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register('login',views.LoginViewSet,base_name='login')
router.register('feed',views.UserProfileFeedViewSet)
router.register('profile',views.UserProfileViewSet)
router.register('post',views.PostViewSet)
router.register('comment',views.CommentViewSet)
router.register('draft',views.DraftViewSet)

from django.urls import path,include

urlpatterns = [
    path('', include(router.urls)),
]
