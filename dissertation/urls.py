from django.urls import path, include
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import views as auth_views

from . import views
from dissertation.views import DissertationList, ClusterList, DissertationCreate, ClusterWithActiveDiss

urlpatterns = [
    # ex: /diss/
    # path('diss/', views.dissertation_list, name='dissertation_list'),
    # ex: /diss/5/
    path('diss/<int:diss_id>', views.dissertation_detail, name='dissertation-detail'),
    path('diss/add/', login_required(DissertationCreate.as_view()), name='dissertation-add'),
    path('disslist/', DissertationList.as_view(), name='disslist'),

    # ex: /cluster/5/
    path('cluster/<int:cluster_id>/', views.cluster_detail, name='detail'),
    path('clusterlist/', ClusterList.as_view(), name='clusterlist'),
    path('cluster/active', ClusterWithActiveDiss.as_view(), name='activediss')

 ]

 #Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]