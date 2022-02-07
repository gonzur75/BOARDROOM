
from django.shortcuts import render, redirect
from django.utils import timezone

from home.models import Boardrooms, Reservations
from home.forms import BoardroomForm, BrModify, BrReserveForm


def br_new(request):
    if request.method == 'POST':
        br_form = BoardroomForm(request.POST)
        if br_form.is_valid():
            br_form.save()
            return redirect('home:br_rooms')
        else:
            return render(request, "home/new_room.html", {'br_form': br_form})

    else:
        br_form = BoardroomForm()
        return render(request, 'home/new_room.html', {'br_form': br_form})


def br_view(request):
    today_date = timezone.now()
    br_rooms = Boardrooms.objects.all()
    for room in br_rooms:
        if today_date.date() in room.reservations.all():
            is_booked = True
        else:
            is_booked = False

    return render(request, 'home/br_rooms.html', {'br_rooms': br_rooms, "is_booked": is_booked})


def br_del(request, pk):
    room_to_remove = Boardrooms.objects.get(pk=pk)
    room_to_remove.delete()
    return redirect('home:br_rooms')


def form_render(request, error_message, pk):
    room_to_modify = Boardrooms.objects.get(pk=pk)
    br_form = BrModify(initial={
        'name': room_to_modify.name,
        'capacity': room_to_modify.capacity,
        'projector': room_to_modify.projector,
    })
    context = {'br_form': br_form, 'pk': pk, 'error_message': error_message}
    return render(request, 'home/modify.html', context)


def br_modify(request, pk):
    if request.method == "POST":
        br_form = BrModify(request.POST)
        if br_form.is_valid():
            name = request.POST.get('name')
            capacity = request.POST.get('capacity')
            projector = request.POST.get('projector')
            db_room = Boardrooms.objects.get(pk=pk)
            if name != db_room.name and Boardrooms.objects.filter(name=name).first():
                return form_render(request, 'This name already exist!', pk)
            else:
                db_room.capacity = capacity
                db_room.projector = projector.capitalize()
                db_room.name = name
                db_room.save()
            return redirect('home:br_rooms')
        else:
            context = {'br_form': br_form, "error_message": "Ups something went wrong!", 'pk': pk}
            return render(request, 'home/modify.html', context)
    # has_changed()
    else:
        return form_render(request, '', pk)


def br_reserve(request, pk):
    if request.method == 'POST':
        br_reserve_form = BrReserveForm(request.POST)
        if br_reserve_form.is_valid():
            br_reserve_form.save()
            return redirect('home:br_rooms')
        else:
            context = {"br_reserve_form": br_reserve_form, "error_message": "Ups something went wrong!", 'pk': pk}
            return render(request, 'home/reserve.html', context)

    else:
        room_to_book = Boardrooms.objects.get(pk=pk)
        br_reserve_form = BrReserveForm(initial={"boardrooms": room_to_book})
        context = {'br_reserve_form': br_reserve_form, 'pk': pk}
        return render(request, 'home/reserve.html', context)


def br_detail(request, pk):
    if request.method == "POST":
        pass
    else:
        br_data = Boardrooms.objects.get(pk=pk)
        # br_reservation_data = Reservations.objects.get(boardrooms=pk)
        rooms_reservation_data = br_data.reservations.all()
        context = {"br_data": br_data,
                   "rooms_reservation_data": rooms_reservation_data,
                   "error_message": "Ups something went wrong!",
                   'pk': pk}
        return render(request, 'home/br_ind_view.html', context)


