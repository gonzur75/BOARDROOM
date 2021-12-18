from django.shortcuts import render, redirect
from home.models import Boardrooms
from home.forms import BoardroomForm


def new_room(request):
    # if request.method == 'POST':
    #     br_form = BoardroomForm(request.POST)
    #
    #     if br_form.is_valid():
    #         br_form.save()
    #         name = br_form.cleaned_data['name']
    #         db_name = Boardrooms.objects.filter(name__contains=name) == False
    #         capacity = br_form.cleaned_data['capacity']
    #         projector = br_form.cleaned_data['projector']
    #         if db_name and capacity > 0:
    #             new_boardroom = Boardrooms(name='name', capacity='capacity', projector=projector)
    #             new_boardroom.save()
    #     return redirect('')
    # else:
    br_form = BoardroomForm()
    return render(request, 'home/new_room.html', {'br_form': br_form})

