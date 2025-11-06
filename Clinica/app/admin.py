from django.contrib import admin
from app.models import Paciente, Atendente, Medico, Sintomas, Consultas

admin.site.register(Paciente)
admin.site.register(Atendente)
admin.site.register(Medico)
admin.site.register(Sintomas)
admin.site.register(Consultas)