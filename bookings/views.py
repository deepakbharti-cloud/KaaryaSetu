from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from workers.models import WorkerProfile


@login_required
def create_booking(request, worker_id):
    # Sirf customer hi booking bana sakta hai

    worker = get_object_or_404(WorkerProfile, id=worker_id)

    if request.user.role != 'customer':
        messages.error(request, "Sirf customer booking bana sakta hai")
        return redirect('worker_detail', worker_id=worker_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.worker = worker
            booking.save()
            messages.success(request, "Booking bhej di gayi! Worker ke accept karne ka wait karo")
            return redirect('my_bookings')
    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form, 'worker': worker})


@login_required
def my_bookings(request):
    # Customer apni sab bookings yaha dekhega

    bookings = Booking.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})


@login_required
def worker_dashboard(request):
    # Worker ke incoming booking requests yaha dikhenge

    try:
        worker_profile = request.user.workerprofile
    except WorkerProfile.DoesNotExist:
        messages.error(request, "Tera worker profile nahi mila")
        return redirect('worker_list')

    bookings = Booking.objects.filter(worker=worker_profile).order_by('-created_at')
    return render(request, 'bookings/worker_dashboard.html', {'bookings': bookings})


@login_required
def update_booking_status(request, booking_id, new_status):
    # Worker booking ko accept/complete/cancel kar sakta hai

    booking = get_object_or_404(Booking, id=booking_id)

    if booking.worker.user != request.user:
        messages.error(request, "Ye booking teri nahi hai")
        return redirect('worker_dashboard')

    if new_status in ['accepted', 'completed', 'cancelled']:
        booking.status = new_status
        booking.save()
        messages.success(request, f"Booking status update ho gaya: {new_status}")

    return redirect('worker_dashboard')
