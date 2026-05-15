from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import Categorie, Entry
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import EntryForm,InscriptionForm


class AjoutEntry(LoginRequiredMixin,CreateView):
    model = Entry
    template_name = 'entry.html'
    form_class = EntryForm
    
    def form_valid(self, form):
       form.instance.utilisateur = self.request.user
       return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('liste_entry2')
 
        
    
    
class LesEntrees(LoginRequiredMixin,ListView):
    model = Entry
    template_name = 'liste_entree.html'
    context_object_name = 'entree'
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context['categories'] = Categorie.objects.all()
     return context
    
    def get_queryset(self):

     queryset = Entry.objects.all()

     categorie = self.request.GET.get('categorie')

     if categorie:
        queryset = queryset.filter(categorie_id=categorie)

     return queryset
 
 
class  ModifierEntry(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Entry
    template_name = 'modifier_entry.html'
    form_class = EntryForm
    def get_success_url(self):
        return reverse('liste_entry',kwargs={'pk':self.object.pk})
    def test_func(self):
     entry = self.get_object()
     return self.request.user == entry.utilisateur
    
    
    
class  SupprimerEntry(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Entry
    template_name = 'supprimer_entry.html'
    success_url = reverse_lazy('liste_entry2')
    def test_func(self):
      obj = self.get_object()
      return self.request.user == obj.utilisateur
    
class DetailEntree(DetailView):
    model = Entry
    template_name = 'detail_entree.html'
    context_object_name = 'detail'
    
    
class Inscription(CreateView):
    
    template_name = 'registration/register.html'
    form_class = InscriptionForm
    def get_success_url(self):
       return reverse('login')

   