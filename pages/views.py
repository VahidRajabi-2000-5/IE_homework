from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth import get_user_model



class HomeView(generic.TemplateView):
    template_name = 'pages/home.html'
    
    


class ProfileView(generic.ListView):
    model = get_user_model()
    template_name = 'pages/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pro'] = get_object_or_404(
            get_user_model(), username=self.request.user)
        return context
   
