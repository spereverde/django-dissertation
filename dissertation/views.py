from django.http import HttpResponse
from django.template import loader

from .models import Dissertation

def dissertation_list(request):
    dlist = Dissertation.objects.order_by('title')
    template = loader.get_template('index.html')
    context = {
        'dlist': dlist,
    }
    return HttpResponse(template.render(context, request))

# def dissertation_list(request):
#     dlist = Dissertation.objects.order_by('title')
#     output = ', '.join([d.title for d in dlist])
#     return HttpResponse(output)
    
def detail(request, diss_id):
    diss = Dissertation.objects.filter(id=diss_id)
    # import pdb; pdb.set_trace()
    dtitle = [d.__str__() for d in diss]
    # dtitle = [d.title for d in diss][0]
    output = "You're looking at dissertation {}. The title is {}".format(
        diss_id, dtitle)
    return HttpResponse(output)

def results(request, diss_id):
    response = "You're looking at the results of dissertation {}.".format(diss_id)
    return HttpResponse(response)
    

def vote(request, diss_id):
    return HttpResponse("You're voting on dissertation {}.".format(diss_id))
