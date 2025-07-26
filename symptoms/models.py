from django.db import models


class Condition(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    severity_level = models.PositiveSmallIntegerField(
        choices=[(1, "Low"), (2, "Medium"), (3, "High"), (4, "Critical")], default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Symptom(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    conditions = models.ManyToManyField(Condition, related_name="symptoms")
    severity_level = models.PositiveSmallIntegerField(
        choices=[(1, "Mild"), (2, "Moderate"), (3, "Severe"), (4, "Critical")],
        default=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
