from django.contrib import admin
from .models import Assignment, StudentWork, QuestionBank, AssignmentQuestion, StudentQuestionWork

class AssignmentAdmin(admin.ModelAdmin):
    pass


class StudentWorkAdmin(admin.ModelAdmin):
    pass


class QuestionBankAdmin(admin.ModelAdmin):
    pass


class AssignmentQuestionAdmin(admin.ModelAdmin):
    pass


class StudentQuestionWorkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(StudentWork, StudentWorkAdmin)
admin.site.register(QuestionBank, QuestionBankAdmin)
admin.site.register(AssignmentQuestion, AssignmentQuestionAdmin)
admin.site.register(StudentQuestionWork, StudentQuestionWorkAdmin)
