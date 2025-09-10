from django.urls import path
from . import views

urlpatterns = [
    path('consulta/', views.ViaCepFormView.as_view(), name='consulta'),
    path('listagem/', views.ViaCepListView.as_view(), name='listagem'),
    path('deletar/<int:pk>/', views.ViaCepDeleteView.as_view(), name='deletar'),
    path('detalhar/<int:pk>/', views.ViaCepDetailView.as_view(), name='detalhar')
]
