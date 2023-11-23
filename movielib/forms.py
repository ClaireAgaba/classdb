from django.forms import ModelForm

#accessing our models

from .models import *


class BranchForm(ModelForm):
    class Meta:
        Fields = [ 'branch_name', 'city', 'district', 'tel_no']


class StaffForm(ModelForm):
    class Meta:
        Fields = ['branch_number', 'name', 'position', 'salary']


class MemberForm(ModelForm):
    class Meta:
        Fields = ['first_name', 'last_name', 'address', 'registration_date', 'branch_number']


class VideoForm(ModelForm):
    class Meta:
        Fields = [ 'video_number', 'title', 'category', 'daily_rental', 'cost', 'status', 'actors', 'director', 'year']


class RentalForm(ModelForm):
    class Meta:
        Fields = ['member', 'video', 'branch', 'quantity', 'rental_date', 'return_date', 'due_date']