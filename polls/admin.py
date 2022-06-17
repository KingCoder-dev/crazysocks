from django.contrib import admin
from .models import Polls, Like, IpModel
# Register your models here.


admin.site.register(Polls)
admin.site.register(Like)
admin.site.register(IpModel)
