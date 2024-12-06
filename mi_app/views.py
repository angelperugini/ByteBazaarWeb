from django.shortcuts import render
from django_user_agents.utils import get_user_agent # type: ignore

def home(request):
    # Obtener el agente de usuario
    user_agent = get_user_agent(request)
    
    # Pasar el user_agent a la plantilla
    return render(request, 'home.html', {'user_agent': user_agent})
