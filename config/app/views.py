from django.shortcuts import render
from .models import Book
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"

class CreateBook(CreateView):
    model = Book
    fields = '__all__'
    template_name = "book_form.html"
    success_url = reverse_lazy('main')

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    template_name = "book_form.html"
    success_url = reverse_lazy('main')

class DeleteBook(DeleteView):
    model = Book
    template_name = "confirm_del.html"
    success_url = reverse_lazy('main')

