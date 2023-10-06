from django.shortcuts import render
from.models import Place
from.models import Team


def demo(request):
   obj=Place.objects.all()
   tem=Team.objects.all()
   return render(request,'new.html',{'result':obj,'value':tem})