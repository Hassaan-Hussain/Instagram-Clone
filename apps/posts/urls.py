from django.urls import path
from . import views


urlpatterns = [
    path('upload_post/', views.upload_post, name='upload_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
]