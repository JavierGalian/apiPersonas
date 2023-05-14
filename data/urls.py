from django.urls import path
from .api import DataApiView
#from .views import UserDataList
urlpatterns = [
    path('users/', DataApiView.as_view(), name='usuario-api')
    #path('users/', UserDataList.as_view(), name='user-list'),
    #path('api/create-user', CreateUserView.as_view(), name='create-user')
]