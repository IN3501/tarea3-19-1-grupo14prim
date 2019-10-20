from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('inputs/', inputs, name='inputs'),
	path('contacto/', contacto, name='contacto'),
	path('creacion/', creacion, name='creacion'),
	path('inicio/', inicio, name='inicio'),
	path('testimonios/', testimonios, name= 'testimonios'),
	path('exitocreacion', cuenta, name= 'exitocreacion'),
	path('exitoinicio', iniciar, name= 'exitoinicio'),
	path('exitoinputs', consulta, name= 'exitoinputs'),
	path('exitotestimonio', guardar, name= 'exitotestimonio'),
	path('cuenta',cuenta, name='cuenta'),
	path('iniciar', iniciar, name='iniciar'),
	path('consulta', consulta, name='consulta'),
	path('guardar', guardar, name='guardar'),
]