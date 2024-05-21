from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index_class/', views.ClassBasedIndex.as_view(), name='index_class'),
    path('user/', views.Userlist.as_view(), name='user'),
    path('post/', views.Postlist.as_view(), name='post'),
    path('redirect/', views.Redirect.as_view(), name='redirect'),
    path('datetime/', views.current_datetime, name='datetime'),
]
