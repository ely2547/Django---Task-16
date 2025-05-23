from django.urls import path
from .views import PhotoListView, PhotoDetailView, PhotoCreateView

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo-list'),
    path('upload/', PhotoCreateView.as_view(), name='photo-upload'),
    path('<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
]
