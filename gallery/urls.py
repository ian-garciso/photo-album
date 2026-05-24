from django.urls import path
from .views import (
    GalleryListView,
    RecipePhotoCreateView,
    RecipePhotoUpdateView,
    RecipePhotoDeleteView,
)

urlpatterns = [
    path('', GalleryListView.as_view(), name='gallery_home'),
    path('upload/', RecipePhotoCreateView.as_view(), name='photo_upload'),
    path('recipe/<int:pk>/edit/', RecipePhotoUpdateView.as_view(), name='edit_recipe'),
    path('recipe/<int:pk>/delete/', RecipePhotoDeleteView.as_view(), name='delete_recipe'),
]

