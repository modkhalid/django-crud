from django.contrib import admin

# Register your models here.
from second_app.models import Topic,Webpage,AccessRecord


admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)