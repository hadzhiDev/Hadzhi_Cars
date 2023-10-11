from django.urls import path
from . import views
from workspace.views import workspace


urlpatterns = [
    path('', views.main, name='main'),
    path('cars/<int:id>/', views.detail, name='detail'),
    path('cars/brands/<int:id>/', views.cars_by_brand, name='cars_by_brand'),
    path('login/', views.login_profile, name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('logout/', views.logout_profile, name='logout'),
    path('profile/', views.profile, name='profile'),
]