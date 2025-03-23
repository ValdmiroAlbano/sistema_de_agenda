from django.db import models

# Create your models here.
class Agendamento(models.Model):
    data_horario = models.DateTimeField()
    nome_cliente = models.CharField(max_length = 200)
    email_cliente = models.CharField(max_length = 200)
    telefone = models.CharField(max_length = 20)