from django.urls import path
from . import views

urlpatterns = [
    path('', views.workspace, name='workspace'),
    path('brands/', views.list_of_brands, name='workspace_brands'),
    path('brands/create/', views.create_brand, name='workspace_create_brand'),
    path('brands/<int:id>/update/', views.update_brand, name='workspace_update_brand'),
    path('brands/<int:id>/delete/', views.delete_brand, name='workspace_delete_brand'),
    path('cars/', views.workspace),
    path('cars/<int:id>', views.detail_car, name='workspace_detail_car'),
    path('cars/add', views.add_car, name='workspace_add_car'),
    path('cars/<int:id>/update/', views.update_car, name='workspace_edit_car'),
    path('cars/<int:id>/delete/', views.delete_car, name='workspace_delete_car'),
    path('cars/brand/<int:id>/', views.filter_cars_by_brand, name='workspace_filter_cars_by_brand'),

]