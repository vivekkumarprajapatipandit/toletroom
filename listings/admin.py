from django.contrib import admin
from .models import rentar,details
from .models import contact_team

class rentarAdmin(admin.ModelAdmin):
    list_display=('id','name','phone','add','state','dist','images') # type: ignore
admin.site.register(rentar,rentarAdmin)

class detailsAdmin(admin.ModelAdmin):
    list_display=('id','Name','Username','Email','Password','Mnumber') # type: ignore
admin.site.register(details,detailsAdmin)


class contact_teamAdmin(admin.ModelAdmin):
    list_display=('Name','Email', 'Subject', 'Message','M_No') 
admin.site.register(contact_team, contact_teamAdmin)

