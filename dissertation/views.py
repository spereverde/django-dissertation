from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Dissertation, Cluster


def dissertation_detail(request, diss_id):
    diss = get_object_or_404(Dissertation, pk=diss_id)
    return render(request, 'dissertation/detail.html', {'diss': diss})

def cluster_detail(request, cluster_id):
    cluster = get_object_or_404(Cluster, pk=cluster_id)
    # import pdb; pdb.set_trace()
    return render(request, 'cluster/detail.html', {'cluster': cluster})

# def dissertation_list(request):
#     dlist = Dissertation.objects.order_by('title')
#     context = {'dlist': dlist}
#     return render(request, 'dissertation/index.html', context)

# def cluster_list(request):
#     clist = Cluster.objects.order_by('name')
#     context = {'clist': clist}
#     return render(request, 'cluster/index.html', context)

class DissertationCreate(CreateView):
    model = Dissertation
    fields = ['title', 'description']


class DissertationList(ListView):
    model = Dissertation



class ClusterList(ListView):
    model = Cluster

