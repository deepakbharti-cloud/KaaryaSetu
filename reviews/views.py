from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
from bookings.models import Booking


@login_required
def add_review(request, booking_id):
    # Sirf completed booking pe hi review de sakte hain, aur sirf wahi customer jisne booking ki thi

    booking = get_object_or_404(Booking, id=booking_id)

    if booking.customer != request.user:
        messages.error(request, "Ye booking teri nahi hai")
        return redirect('my_bookings')

    if booking.status != 'completed':
        messages.error(request, "Booking abhi complete nahi hui, review nahi de sakte")
        return redirect('my_bookings')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.booking = booking
            review.save()

            # Worker ki average rating update kar do
            worker = booking.worker
            all_reviews = [b.review.rating for b in worker.bookings_received.filter(review__isnull=False)]
            worker.avg_rating = sum(all_reviews) / len(all_reviews)
            worker.save()

            messages.success(request, "Review de diya, dhanyawad!")
            return redirect('my_bookings')
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'booking': booking})
