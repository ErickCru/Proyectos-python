from django.urls import path
from .views import ListPost, DetailPost


urlpatterns = [
    path('', ListPost.as_view(), name='posts'),
    path('post/<str:pk>', DetailPost.as_view(), name='detail_post'),
]
