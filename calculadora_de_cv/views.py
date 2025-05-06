from django.shortcuts import render
from rest_framework import viewsets

from .calcs import calcular_valor_critico
from .forms import CalculadoraForm
from .models import Artefato
from .serializers import ArtefatoSerializer

class ArtefatoViewSet(viewsets.ModelViewSet):
    queryset = Artefato.objects.all()
    serializer_class = ArtefatoSerializer


def home(request):
    artefatos = Artefato.objects.all().order_by('-created_at')[:10]

    if request.method == 'POST':
        form = CalculadoraForm(request.POST)
        if form.is_valid():
            dano_critico = form.cleaned_data['dano_critico']
            taxa_critica = form.cleaned_data['taxa_critica']

            valor_critico = calcular_valor_critico(dano_critico=dano_critico, taxa_critica=taxa_critica)

            # Save to database
            calculo_completo = Artefato(
                dano_critico=dano_critico,
                taxa_critica=taxa_critica,
                valor_critico=valor_critico
            )

            calculo_completo.save()

            return render(request, 'home.html', {'form': form, 'artefatos': artefatos})
    else:
        form = CalculadoraForm()

    return render(request, 'home.html', {'form': form, 'artefatos': artefatos})