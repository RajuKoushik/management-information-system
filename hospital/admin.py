# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Patient, Doctor, Ward, Receptionist
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Ward)
admin.site.register(Receptionist)