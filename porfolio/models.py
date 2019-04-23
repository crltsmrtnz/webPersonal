from django.db import models

# Create your models here.

class project(models.Model):
	"""creando la app de porfolio"""

	title = models.CharField(max_length=200, verbose_name='Titulo')
	descriptions = models.TextField(verbose_name='Descripcion')
	image = models.ImageField(verbose_name='Image', upload_to='projects')
	link = models.URLField(verbose_name='Direccion Web', null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
	updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

	#MetaDatos para traducir las aplicaciones
	class Meta:
		verbose_name='proyecto'
		verbose_name_plural='proyectos'
		#guion (-) para ondenar y salgan primero las ultimas publicaciones
		ordering = ['-created']

	#devuelve el nombre del titulo de proyecto
	def __str__(self):
		return self.title

		