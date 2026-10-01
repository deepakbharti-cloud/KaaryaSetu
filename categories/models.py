from django.db import models


class Category(models.Model):
    # Jaise: Plumber, Electrician, Carpenter, Painter, Cleaner

    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, help_text="Emoji ya icon name")

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    # Har category ke andar chhote specific kaam
    # Jaise Plumber ke andar: "Tap Repair", "Pipe Fitting", "Bathroom Fitting"

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category.name} - {self.name}"
