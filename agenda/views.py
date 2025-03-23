from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializers


# Create your views here.
def agendamento_detail(request, id):
    obj = get_object_or_404(Agendamento, id = id)
    serializers = AgendamentoSerializers(obj)
    return JsonResponse(serializers.data)

def agendamento_list(request):
    qs = Agendamento.objects.all()
    serializers = AgendamentoSerializers(qs, many = True)
    return JsonResponse(serializers.data, safe = False)