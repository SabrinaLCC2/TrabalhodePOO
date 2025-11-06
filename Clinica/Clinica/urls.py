from django.contrib import admin
from django.urls import path
from app.views import index,home,pagina_estatica,paciente,medico,atendente,consulta,detalhamento_paciente,detalhamento_medico,detalhamento_consulta


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/<int:identificador>',index),
    path('pagina_estatica',pagina_estatica),
    path('',home,name='home'),
    path('paciente',paciente,name='paciente'),
    path('paciente/detalhamento/<int:id>',detalhamento_paciente,name='detalhamento_paciente'),
    path('medico',medico,name='medico'),
    path('medico/detalhamento/<int:id>',detalhamento_medico,name='detalhamento_medico'),
    path('atendente',atendente,name='atendente'),
    path('consulta',consulta,name='consulta'),
    path('consulta/detalhamento/<int:id>',detalhamento_consulta,name='detalhamento_consulta'),
]

