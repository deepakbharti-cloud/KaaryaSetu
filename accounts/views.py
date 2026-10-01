from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import User
from workers.models import WorkerProfile
from bookings.models import Booking
from categories.models import Category


def redirect_by_role(user):
    # User ka role dekh ke sahi jagah bhej do

    if user.role == 'worker':
        return redirect('worker_dashboard')
    elif user.role == 'admin':
        return redirect('admin_dashboard')
    else:
        return redirect('home')


def register_view(request):
    # Naya customer ya worker signup karega yaha se

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Agar worker banke aaya hai, toh uske liye ek WorkerProfile bhi bana do
            if user.role == 'worker':
                WorkerProfile.objects.create(user=user, area='')

            messages.success(request, "Account ban gaya! Welcome " + user.username)
            return redirect_by_role(user)
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect_by_role(user)
        else:
            messages.error(request, "Username ya password galat hai")

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def admin_dashboard(request):
    # Sirf admin role wale hi ye dashboard dekh sakte hain

    if request.user.role != 'admin':
        messages.error(request, "Ye page sirf admin ke liye hai")
        return redirect('home')

    context = {
        'total_workers': WorkerProfile.objects.count(),
        'total_customers': User.objects.filter(role='customer').count(),
        'total_bookings': Booking.objects.count(),
        'total_categories': Category.objects.count(),
        'recent_bookings': Booking.objects.order_by('-created_at')[:5],
    }
    return render(request, 'accounts/admin_dashboard.html', context)
