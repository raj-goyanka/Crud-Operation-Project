from enroll.models import *
from enroll.api.serializers import *
from rest_framework import viewsets
from rest_framework.authentication import *
from rest_framework.permissions import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes =  [IsAuthenticatedOrReadOnly]