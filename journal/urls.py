from django.urls import path
from .views import AjoutEntry,LesEntrees,ModifierEntry,SupprimerEntry,DetailEntree,Inscription,MesActivites,Historique


urlpatterns = [
    path('register/',Inscription.as_view() , name='inscription'),
    path('ajout_entree/',AjoutEntry.as_view() , name='liste_entry'),
    path('lesentrees/',LesEntrees.as_view() , name='liste_entry2'),
    path('detail/<int:pk>',DetailEntree.as_view() , name='detail_entree'),
    path('<int:pk>/update/',ModifierEntry.as_view() , name='modifier_entree'),
    path('<int:pk>/delete/',SupprimerEntry.as_view() , name='supprimer_entree'),
    path('mes_activites/',MesActivites.as_view() , name='mes_activites'),
    path('activites_modifiees/',Historique.as_view() , name='activites_modifiees'),
  
    
    ]