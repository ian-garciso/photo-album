from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import cloudinary.uploader

from .forms import RecipePhotoForm
from .models import RecipePhoto


class GalleryListView(ListView):
    model = RecipePhoto
    template_name = 'gallery/home.html'
    context_object_name = 'photos'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        queryset = RecipePhoto.objects.all().order_by('-uploaded_at')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class RecipePhotoCreateView(LoginRequiredMixin, CreateView):
    model = RecipePhoto
    form_class = RecipePhotoForm
    template_name = 'gallery/upload.html'
    permission_required = 'gallery.add_recipephoto'
    success_url = reverse_lazy('gallery_home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"'{self.object.title}' has been added to the album.")
        return response


class RecipePhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = RecipePhoto
    form_class = RecipePhotoForm
    template_name = 'gallery/edit.html'
    permission_required = 'gallery.change_recipephoto'
    success_url = reverse_lazy('gallery_home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"'{self.object.title}' was updated successfully.")
        return response


class RecipePhotoDeleteView(LoginRequiredMixin,  DeleteView):
    model = RecipePhoto
    template_name = 'gallery/delete.html'
    permission_required = 'gallery.delete_recipephoto'
    success_url = reverse_lazy('gallery_home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        title = self.object.title
        if self.object.image:
            try:
                cloudinary.uploader.destroy(self.object.image.public_id)
            except Exception:
                pass
        messages.success(request, f"'{title}' was deleted from the album.")
        return super().delete(request, *args, **kwargs)

class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'gallery/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your account was created successfully. Please log in.')
        return response
