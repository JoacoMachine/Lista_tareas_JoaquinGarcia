from django.db import models

# Create your models here.
class Tarea(models.Model):
	content = models.CharField(max_length=140, null=False, blank=False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)	

	def __str__(self):
		return '{}: {}'.format(self.user, self.content)

class Guardar(models.Model):
	created = models.DateTimeField(auto_now_add=True)	
	tarea = models.ForeignKey(Tweet, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

