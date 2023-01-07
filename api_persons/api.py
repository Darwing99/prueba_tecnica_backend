from .models import Person
from .serializers import PersonSerializer

from rest_framework import viewsets,permissions

class PersontViewSet(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=PersonSerializer
