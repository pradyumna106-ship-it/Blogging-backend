from django.urls import path
from .views import get_data, add_post, update_post, delete_post, get_single_post

urlpatterns = [
    path('', get_data),                      # GET all posts
    path('<int:pk>/', get_single_post),      # GET single post
    path('add/', add_post),                  # POST create
    path('update/<int:pk>/', update_post),   # PUT / PATCH update
    path('delete/<int:pk>/', delete_post),   # DELETE
]