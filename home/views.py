from django.shortcuts import render, redirect
from home.models import Boardrooms
from home.forms import BoardroomForm


def br_new(request):
    if request.method == 'POST':
        br_form = BoardroomForm(request.POST)

        if br_form.is_valid():
            br_form.save()
            name = br_form.cleaned_data['name']
            db_name = Boardrooms.objects.filter(name__contains=name) == False
            capacity = br_form.cleaned_data['capacity']
            projector = br_form.cleaned_data['projector']
            if db_name and capacity > 0:
                new_boardroom = Boardrooms(name='name', capacity='capacity', projector=projector)
                new_boardroom.save()
        return redirect('home:br_rooms')
    else:
        br_form = BoardroomForm()
        return render(request, 'home/new_room.html', {'br_form': br_form})


def br_view(request):
    br_rooms = Boardrooms.objects.all()
    return render(request, 'home/br_rooms.html', {'br_rooms': br_rooms} )


def br_del(request, pk):
    room_to_remove = Boardrooms.objects.get(pk=pk)
    room_to_remove.delete()
    return redirect('home:br_rooms')


def br_modify(request, pk):
    if request.method == "POST":
        pass
    else:
        room_to_modify = Boardrooms.objects.get(pk=pk)
        br_form = BoardroomForm(initial={
            'name': room_to_modify.name,
            'capacity': room_to_modify.capacity,
            'projector': room_to_modify.projector,
        })
        render(request, 'home/modify.html', {'br_form': br_form})