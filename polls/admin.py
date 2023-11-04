from django.contrib import admin
from . models import Choice , Voter  , Question ,Wilaya , Destination


admin.site.register(Voter)
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Wilaya)
admin.site.register(Destination)