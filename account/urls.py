from django.urls import path, include
from . import views
urlpatterns = [
    path('accounts/register/', views.RegistrationView.as_view()),
    path('accounts/', include('rest_auth.urls')),
    path('accounts/logout/', views.LogoutView.as_view()),
    path('accounts/activate/<uuid:activation_code>', views.ActivationView.as_view())
]
