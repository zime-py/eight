
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Nidinfo

@api_view()
def check_nid(request, nid_number):
    is_exist = Nidinfo.objects.filter(nid_number=nid_number).exists()
    return Response({'status': is_exist})