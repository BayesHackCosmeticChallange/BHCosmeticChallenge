from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.


def main(request):
    context = RequestContext(request)
    return render_to_response('index.html', None, context)