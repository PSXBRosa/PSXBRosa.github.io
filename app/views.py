from .models import *
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views import generic

class DisciplinaListView(generic.ListView):
    paginate_by = 2
    model = Disciplina
    template_name = 'list.html'
    context_object_name = 'lista_disciplinas'

    def get_queryset(self):
        queryset = Disciplina.objects.all()
        if self.request.GET.get("query", False):
            search_term = self.request.GET['query'].lower()
            queryset = queryset.filter(nome__icontains=search_term)
        return queryset        

class DisciplinaDetailView(generic.DetailView):
    model = Disciplina
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comentarios"] = Comentario.objects.filter(disciplina=self.object.id).order_by('-data_de_criacao')
        return context

def index(request):
    context = {}
    return render(request, 'index.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contato(request):
    context = {}
    return render(request, 'contato.html', context)

def cadastro(request):
    context = {}
    return render(request, 'cadastro.html', context)