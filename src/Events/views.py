from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from Babies.models import Baby
from rest_framework.response import Response
from .serializers import EventSerializer
from Permissions.services import APIPermissionClassFactory 
from guardian.shortcuts import assign_perm

def evaluate_user(user, obj, request):
    return user.username == obj.baby.parent.username

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': True,
                    'destroy': True,
                    'update': True,
                    'partial_update': True,
                    'perform_create': True,
                }
            }
        ),
    )
    def perform_create(self, serializer):
        user = self.request.user
        baby = Baby.objects.get(pk=self.request.data['baby'])
        if(baby.parent.username == user.username):
            event = serializer.save()
            assign_perm('events.change_event', user, event)
            assign_perm('events.view_event', user, event)
            return Response(serializer.data)