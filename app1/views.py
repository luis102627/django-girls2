from django.shortcuts import render
from app1.models import Post
from django.views.generic import ListView

def listaPost(request):
	lista = Post.objects.all() 
	return render(request, 'templates/lista.html',{'milista':lista})

def sendid(request, id):
	try:
		detalle = Post.objects.get(id = id)
	except Post.DoesNotExist:
		detalle = "Esta no existe"

	return render(request, 'templates/segundo.html', {'identificador': detalle})

class Lista2(ListView):
	model = Post
	template_name = 'templates/lista.html'
	
