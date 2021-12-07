from django.forms import ModelForm
from .models import Avaliacao

class AvaliacaoForm(ModelForm):
    class Meta:
        model = Avaliacao
        fields = [
            'nota_1',
            'nota_2',
            'nota_3',
            'nota_4', 
        ]
        labels = {
            'nota_1': 'Ensino',
            'nota_2': 'Material Didático:',
            'nota_3': 'Avaliações:',
            'nota_4': 'Dificuldade:' 
        }