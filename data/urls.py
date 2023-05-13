from django.urls import path
from rest_framework import routers
from .api import DataViewSet
from .views import UserDataList,CreateUserView
router = routers.DefaultRouter()
router.register('api/data', DataViewSet, 'data')


urlpatterns = [
    path('users/', UserDataList.as_view(), name='user-list'),
    path('api/create-user', CreateUserView.as_view(), name='create-user')
]

urlpatterns = router.urls