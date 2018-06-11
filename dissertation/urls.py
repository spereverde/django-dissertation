from django.urls import path

from . import views
from dissertation.views import DissertationList, ClusterList, DissertationCreate

urlpatterns = [
    # ex: /diss/
    # path('diss/', views.dissertation_list, name='dissertation_list'),
    # ex: /diss/5/
    path('diss/<int:diss_id>', views.dissertation_detail, name='dissertation-detail'),
    path('diss/add/', DissertationCreate.as_view(), name='dissertation-add'),
    path('disslist/', DissertationList.as_view()),

    # ex: /cluster/
    # path('cluster/', views.cluster_list, name='cluster_list'),
    # ex: /cluster/5/
    path('cluster/<int:cluster_id>/', views.cluster_detail, name='detail'),
    path('clusterlist/', ClusterList.as_view()),

    # path('dpc/', DissPerClusterList.as_view()),
 ]