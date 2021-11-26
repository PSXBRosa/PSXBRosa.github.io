from .models import *
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views import generic

class DisciplinaListView(generic.ListView):
    model = Disciplina
    template_name = 'list.html'

class DisciplinaDetailView(generic.DetailView):
    model = Disciplina
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comentarios"] = Comentario.objects.filter(disciplina=self.object.id).order_by('-created_on')
        return context

def index(request):
    context = {}
    return render(request, 'index.html', context)

