from django.db import models
from utils.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=124)
    country = models.CharField(max_length=64)
