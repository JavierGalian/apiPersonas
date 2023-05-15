from django.urls import path
from .api import data_api_view, user_detail_view
#from .views import UserDataList
urlpatterns = [
    path('users/', data_api_view, name='usuario-api'),
    path('users/<int:pk>/', user_detail_view, name='usuario-detail-api-view')
    #path('users/', UserDataList.as_view(), name='user-list'),
    #path('api/create-user', CreateUserView.as_view(), name='create-user')
]