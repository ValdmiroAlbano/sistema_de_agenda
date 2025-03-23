from rest_framework import serializers


class AgendamentoSerializers(serializers.Serializer):
    data_horario = serializers.DateTimeField()
    nome_cliente = serializers.CharField(max_length = 200)
    email_cliente = serializers.CharField(max_length = 200)
    telefone = serializers.CharField(max_length = 20)