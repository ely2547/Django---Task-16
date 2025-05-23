from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Photo
from .forms import PhotoForm

class PhotoListView(ListView):
    model = Photo
    template_name = 'photo_list.html'
    context_object_name = 'photos'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'

class PhotoCreateView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photo_form.html'
    success_url = reverse_lazy('photo-list')
