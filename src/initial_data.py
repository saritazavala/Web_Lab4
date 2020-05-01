from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm, remove_perm
from Parents.models import Parent
from Babies.models import Baby  
from Events.models import Event



Pablo = Parent()
Pablo.user = "Pablo"
Pablo.name = "Pablo"
Pablo.lastName = "Juarez"
Pablo.save()

Maria = Parent()
Maria.user = "Maria"
Maria.name = "Maria"
Maria.lastName = "Escobar"
Maria.save()

Daniel = Parent()
Daniel.user = "Daniel"
Daniel.name = "Daniel"
Daniel.lastName = "Bedoya"
Daniel.save()
##################################################################
Diego = Baby()
Diego.name = "Diego"
Diego.lastName = "Juarez"
Diego.gender = "Masculino"
Diego.parent = Pablo
Diego.save()

Emma = Baby()
Emma.name = "Emma"
Emma.lastName = "Juarez"
Emma.gender = "Femenino"
Emma.parent = Pablo
Emma.save()

David = Baby()
David.name = "David"
David.lastName = "Escobar"
David.gender = "Masculino"
David.parent = Maria
David.save()

sarita = Baby()
sarita.name = "Sarita"
sarita.lastName = "Bedoya"
sarita.parent = Daniel
sarita.gender = "Femenino"
sarita.save()

event_diego = Event(description = "No le gusta de zanahoria",type="Pacha", baby=Diego)
event_diego.save()    

event_emma = Event(description = "Duerme durante el dia", type="Siesta", baby=Emma)
event_emma.save()    

event_david2= Event(  description = "Duerme por lapsos pequenios ",type="Siesta", baby=David)
event_david2.save()   

event_david = Event(description = "Comprar medicina ",type="Popo",   baby=David)
event_david.save()