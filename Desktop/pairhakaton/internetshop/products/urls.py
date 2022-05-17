from django.urls import path

from products import views

urlpatterns = [
    path('products/', views.ProductListView.as_view()),
    path('products/create/', views.ProductCreateView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view()),

    # Comment urls
    path('comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]
