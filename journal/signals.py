from .models import Entry
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save,sender=Entry)
def notification(sender,instance,created,**kwargs):
    if created == True:
        utilisateur = instance.utilisateur
        categorie = instance.categorie
        titre = instance.titre
        print(f' L utilisateur :{utilisateur} -- a ajouté une activité de type :{categorie} --  ayant comme titre:{titre}')