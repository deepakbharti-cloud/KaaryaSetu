from django.shortcuts import render, get_object_or_404
from .models import WorkerProfile
from django.contrib import messages
from categories.models import Category



def worker_list(request):
    # Can you filter the list of all verified workers by category or area?

    workers = WorkerProfile.objects.filter(is_verified=True)

    category_id = request.GET.get('category')
    area = request.GET.get('area')

    if category_id:
        workers = workers.filter(category_id=category_id)

    if area:
        workers = workers.filter(area__icontains=area)

    categories = Category.objects.all()

    context = {
        'workers': workers,
        'categories': categories,
    }
    return render(request, 'workers/worker_list.html', context)


def worker_detail(request, worker_id):
    # Ek worker ki full detail + uske reviews

    worker = get_object_or_404(WorkerProfile, id=worker_id)
    reviews = worker.bookings_received.filter(review__isnull=False)

    context = {
        'worker': worker,
        'bookings_with_reviews': reviews,
    }
    return render(request, 'workers/worker_detail.html', context)


def home(request):
    # Landing page - hero banner + featured categories + kuch top workers

    categories = Category.objects.all()
    featured_workers = WorkerProfile.objects.filter(is_verified=True)[:6]

    context = {
        'categories': categories,
        'featured_workers': featured_workers,
    }
    return render(request, 'workers/home.html', context)
def about(request):
    return render(request, "about.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Abhi testing ke liye
        print(name, email, subject, message)

        messages.success(request, "Aapka message successfully send ho gaya!")

    return render(request, "contact.html")