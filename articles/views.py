from django.views.generic import ListView, DetailView, TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

# Create your views here.

from . models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'batman'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'create.html'
    fields = '__all__'


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'edit.html'
    fields = ['title', 'text']


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'delete.html'
    context_object_name = 'batman'
    success_url = reverse_lazy('home')


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'
