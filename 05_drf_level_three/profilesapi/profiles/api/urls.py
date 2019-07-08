from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles.api.views import ProfileViewSet


# profile_list = ProfileViewSet.as_view({'get': 'list'})
# profile_detail = ProfileViewSet.as_view({'get': 'retrieve'})

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)


urlpatterns = [
    # path('profiles/', profile_list, name='profile-list'),
    # path('profiles/<int:pk>', profile_detail, name='profile-detail'),
    path('', include(router.urls)),
]
