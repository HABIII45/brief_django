from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=80)
    description_categorie = models.TextField()
    
    def __str__(self):
        return self.nom_categorie
    
class Entry(models.Model):
    titre = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    
    