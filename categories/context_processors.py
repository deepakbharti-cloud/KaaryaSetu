from .models import Category


def categories_processor(request):
    # Ye function har page ko categories (+ unki subcategories) bhej dega, taaki navbar mein dikha sakein
    # prefetch_related se ek hi query mein subcategories bhi le aate hain (fast rahega)

    return {'nav_categories': Category.objects.prefetch_related('subcategories').all()}
