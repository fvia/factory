from django.contrib import admin

from factapp.models import Process, Machine, Article, Component

# Process
admin.site.register(Process)


# Machine
admin.site.register(Machine)


# Article
admin.site.register(Article)


# Component
admin.site.register(Component)

