from django.urls import path
from . import views

urlpatterns = [
    path('consulta/', views.ViaCepFormView.as_view(), name='consulta'),
    path('listagem/', views.ViaCepListView.as_view(), name='listagem'),
    path('deletar', views.ViaCepDeleteView.as_view(), name='deletar'),
    path('detalhar', views.ViaCepDetailView.as_view(), name='detalhar')
]
