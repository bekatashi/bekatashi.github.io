from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders import views

router = DefaultRouter()
router.register('orders', views.OrdersViewSet, basename='Order')
urlpatterns = [
    path('', include(router.urls)),
]
