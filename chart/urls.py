from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='Home/'),
    path('post/<str:key>/', views.detail, name='detail/'),
    #path('share', views.share, name='share'),
]
