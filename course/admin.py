from django.contrib import admin
from .models import Course, Section, ContentType, Content


class CourseAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    pass


class ContentTypeAdmin(admin.ModelAdmin):
    pass


class ContentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(ContentType, ContentTypeAdmin)
admin.site.register(Content, ContentAdmin)
