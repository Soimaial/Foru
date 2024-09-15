from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Forum, Topic, Message  # Assure-toi d'importer tes modèles

# Enregistrement simple des modèles
admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Message)
