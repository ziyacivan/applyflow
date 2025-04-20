from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BaseModel(models.Model):
    """
    Abstract base model for shared fields across models.

    Includes:
        - created_at: Timestamp when the instance is created.
        - updated_at: Timestamp when the instance is updated.
        - is_active: Soft-delete flag (False means logically deleted).
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    active = ActiveManager()
    objects = models.Manager()

    class Meta:
        abstract = True

    def soft_delete(self):
        self.is_active = False
        self.save()
