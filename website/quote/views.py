from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import Quote, Image
from .serializers import QuoteSerializer, ImageSerializer
from rest_framework import viewsets

def index(request):
    latest_quotes_list = Quote.objects.order_by('-pub_date')
    context = {'latest_quotes_list': latest_quotes_list}

    return render(request, 'quote/index.html', context)

def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quote/detail.html', {'quote': quote})

class QuoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that show all the quotes ordered by date.
    """
    queryset = Quote.objects.all().order_by('-pub_date')
    serializer_class = QuoteSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that show the image url.
    """
