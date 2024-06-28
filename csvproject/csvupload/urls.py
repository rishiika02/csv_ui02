from django.urls import path
from . import views  # Ensure this import is correct

urlpatterns = [
    path('upload/', views.upload_csv, name='upload_csv'),
]