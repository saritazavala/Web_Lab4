from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from Permissions.services import APIPermissionClassFactory 
from guardian.shortcuts import assign_perm
from Events.models import Event
from Events.serializers import EventSerializer


from Babies.models import Baby
from Babies.serializers import BabySerializer

def is_parent(user, obj, request):    
     return user.username == obj.parent.user


class BabyViewSet(viewsets.ModelViewSet):

    queryset = Baby.objects.all()
    serializer_class = BabySerializer
    permission_classes = (         
    APIPermissionClassFactory(             
        name='BabyPermission',             
        permission_configuration={                 
            'base': {                     
                'create': True,                     
                'list': True,                     

                },                 
                'instance': {                    
                    'retrieve': is_parent,                    
                    'destroy': False,                    
                    'update': is_parent,                    
                    'partial_update': is_parent, 
                    'events': is_parent, 
                }  
            }   
        ),    
     )

    def perform_create(self, serializer):
        user = self.request.user 
        baby = serializer.save()      
        assign_perm('baby.change_baby', user, baby)            
        assign_perm('baby.view_baby', user, baby)             
        return Response(serializer.data)

    @action(detail=True, methods=['get'])     
    def events(self, request, pk=None):        
        baby = self.get_object()         
        queryset = Event.objects.filter(baby = baby)        
        events = EventSerializer(queryset, many = True).data         
        return Response(events)


