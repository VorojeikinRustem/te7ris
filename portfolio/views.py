from django.shortcuts import render
from .models import Section


def portfolio(request):
    context = {}
    context['sections'] = Section.objects.all()
    return render(request, 'portfolio_base.html', context)


def section(request, section):
    context = {}
    if section == "magazine":
        context['section'] = Section.objects.get(title="Internet Magazine")
    elif section == "auction":
        context['auction'] = Section.objects.get(title="Auction")
    return render(request, 'section.html', context)
