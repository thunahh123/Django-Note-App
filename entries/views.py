from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Entry
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

# class-based views
class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by('-created_at')


class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(SuccessMessageMixin, CreateView):
    model = Entry
    fields = ['title', 'content']
    success_url = reverse_lazy('entry-list')
    success_message = "Your new note was created!"

class EntryUpdateView(SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ['title', 'content']
    success_message = "Your note was updated!"

    def get_success_url(self):
        return reverse_lazy("entry-detail", kwargs={"pk": self.object.id})

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    # success_message = "Your note was deleted!"

    def delete(self, request, *args, **kwargs):
        entry = self.get_object()
        messages.success(request, f'The note "{entry.title}" was successfully deleted.')
        return super().delete(request, *args, **kwargs)