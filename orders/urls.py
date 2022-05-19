from django.urls import path
from orders import views

urlpatterns = [
    path('order/', views.BasketApiView.as_view()),
]
