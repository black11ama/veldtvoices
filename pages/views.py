from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from books.models import Book
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomePageView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'