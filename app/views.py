from django.shortcuts import render
from .models import Book
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')


class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book-list')