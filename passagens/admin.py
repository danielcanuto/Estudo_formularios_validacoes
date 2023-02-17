from django.contrib import admin
from passagens.models.pessoa import Pessoa
# from passagens.models.classe_viagem import ClasseViagem
from passagens.models.passagem import Passagem

admin.site.register(Pessoa)
# admin.site.register(ClasseViagem)
admin.site.register(Passagem)