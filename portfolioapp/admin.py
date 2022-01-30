from django.contrib import admin

from portfolioapp.models import Projects, Query, Skills, Testimonial

# Register your models here.
admin.site.register(Skills)
admin.site.register(Projects)
admin.site.register(Testimonial)
admin.site.register(Query)