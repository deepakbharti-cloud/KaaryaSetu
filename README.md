# KaaryaSetu

**Kaarya** = work, **Setu** = bridge — a hyperlocal labour marketplace that connects local skilled workers (plumbers, electricians, carpenters, painters, cleaners, drivers, masons, cooks) with customers who need their services.

## ✨ Features

- Role-based signup/login — Customer, Worker, Admin
- Category & subcategory browsing (OLX-style "All Categories" mega menu)
- Worker listing with search/filter by category and area
- Worker profile page with rate, bio, area and reviews
- Booking system — request, accept, complete, cancel
- Rating & review system with auto-updating worker average rating
- Role-based dashboards after login (customer bookings, worker requests, admin overview)
- Responsive UI built with Tailwind CSS

## 🛠 Tech Stack

- **Backend:** Python, Django (plain Django — no DRF)
- **Database:** SQLite (dev) — MySQL planned for production
- **Frontend:** Django Templates, HTML5, Tailwind CSS (CDN) javascript
- **Auth:** Django's built-in session authentication with a custom User model

## 📁 Project Structure

```
kaaryasetu/
├── accounts/      # Custom User model, register/login/logout, role-based redirect
├── categories/    # Category & SubCategory models, nav context processor
├── workers/       # WorkerProfile model, home page, listing, detail page
├── bookings/      # Booking model, booking flow, worker dashboard
├── reviews/       # Review model, rating logic
├── templates/     # Shared base template (navbar, mega menu, footer)
└── manage.py
```

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/deepakbharti-cloud/kaaryasetu.git
cd kaaryasetu

# 2. Install dependencies
pip install django

# 3. Run migrations
python manage.py migrate

# 4. Create an admin account
python manage.py createsuperuser

# 5. Start the server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the app and `http://127.0.0.1:8000/admin/` for the admin panel.

> After creating a worker account, verify it from the admin panel (`is_verified`) so it appears in the public listing.

## 📌 Roadmap

- [ ] Link workers to subcategories for exact filtering
- [ ] Worker profile photo upload
- [ ] Online payments (Razorpay) + cash-on-service
- [ ] In-app chat / contact reveal after booking
- [ ] Location-based nearby search
- [ ] Migrate to MySQL and deploy

## 👤 Author

**Deepak** — [GitHub](https://github.com/deepakbharti-cloud) · [Portfolio](https://deepakbharti.github.io)
