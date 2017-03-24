from django.contrib import admin

# Register your models here.

from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__str__","full_name",'location','contact_no']
	form=SignUpForm
#	class Meta:
#		model = SignUp

admin.site.register(SignUp,SignUpAdmin)