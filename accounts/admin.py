"""
Accounts admin
"""
###
# Libraries
###
from django.contrib import admin

from . import models


###
# Inline Admin Models
###


###
# Main Admin Models
###
@admin.register(models.ChangeEmailRequest)
class ChangeEmailRequestAdmin(admin.ModelAdmin):
    list_display = ('email',)
    readonly_fields = ('uuid',)
