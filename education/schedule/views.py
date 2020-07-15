from django.shortcuts import render
from .models import Schedule


def index_view(request):
    schedule = Schedule.objects.get(pk=1)
    context = {
        'schedule': schedule,
        'all_schedules': Schedule.objects.all(),
    }
    return render(request, 'schedule/contact.html', context=context)
