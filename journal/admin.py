from django.contrib import admin
from .models import Categorie,Entry
# Register your models here.

class MesCategories(admin.ModelAdmin):
    fields = ['nom_categorie','description_categorie']
    list_display = ['nom_categorie','description_categorie']
    search_fields = ['nom_categorie']
    list_filter = ['nom_categorie']
admin.site.register(Categorie,MesCategories)
class MesEntrees(admin.ModelAdmin):
    fields = ['titre', 'categorie', 'utilisateur','description','image']
    list_display = ['titre', 'categorie', 'utilisateur', 'description','date','image']
    search_fields = ['titre']
    list_filter = ['date']
admin.site.register(Entry,MesEntrees)