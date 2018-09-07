from django.shortcuts import render

# Create your views here.
def index(request):
	tareas = Tarea.objects.all()[::-1]
	ctx = {'work_to_do': tareas}
	return render(request, 'index.html', ctx)