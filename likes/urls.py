from django.urls import path
from . import views
urlpatterns = [
    path('likes/', views.LikesView.as_view()),
    path('likes/create/', views.LikesCreateView.as_view()),
    path('likes/delete/', views.LikesDeleteView.as_view())
]
