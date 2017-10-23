# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=200)
    doctor_department = models.CharField(max_length=200)
    doctor_specialization = models.CharField(max_length=200)
    doctor_age = models.CharField(max_length=200)
    doctor_qualification = models.CharField(max_length=200)

    def __str__(self):
        return self.doctor_name


class Ward(models.Model):
    ward_number = models.CharField(max_length=200)
    ward_type = models.CharField(max_length=200)
    admitted_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.ward_number


class Receptionist(models.Model):
    receptionist_name = models.CharField(max_length=200)
    receptionist_age = models.CharField(max_length=200)
    receptionist_qualification = models.CharField(max_length=200)

    def __str__(self):
        return self.receptionist_name


class Patient(models.Model):
    patient_name = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor)
    receptionist = models.ForeignKey(Receptionist)
    Ward = models.ForeignKey(Ward)
    is_out_patient = models.BooleanField(default=True)
    diagnosed_disease = models.CharField(max_length=200)
    additional_text = models.TextField()
    appointment_date = models.DateTimeField(default=timezone.now)
    admitted_date = models.DateTimeField(blank=True, null=True)
    is_diagnosed = models.BooleanField(default=True)

    def publish(self):
        self.appointment_date = timezone.now()
        self.save()

    def __str__(self):
        return self.patient_name
