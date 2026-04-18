from django.shortcuts import render
from .models import Banner, SecaoHome

def home(request):
    banners = Banner.objects.filter(ativo=True).order_by('ordem')
    secoes_home = (
        SecaoHome.objects.filter(ativa=True)
        .prefetch_related('produtos')
        .order_by('ordem', 'id')
    )

    return render(request, 'home.html', {
        'banners': banners,
        'secoes_home': secoes_home,
    })