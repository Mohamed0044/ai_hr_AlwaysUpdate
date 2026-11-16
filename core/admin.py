from django.contrib import admin

# Register your models here.


from .models import (
    Department,
    JobPosition,
    Candidate,
    Resume,
    ScreeningResult,
    InterviewQuestionSet,
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at',)


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'created_at')
    search_fields = ('title', 'department__name')
    list_filter = ('department',)
    readonly_fields = ('created_at',)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    readonly_fields = ('created_at',)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'file', 'uploaded_at')
    search_fields = ('candidate__full_name', 'candidate__email')
    readonly_fields = ('uploaded_at',)


@admin.register(ScreeningResult)
class ScreeningResultAdmin(admin.ModelAdmin):
    list_display = (
        'candidate', 'job_position', 'score',
        'recommendation', 'generated_at',
    )
    search_fields = ('candidate__full_name', 'job_position__title')
    list_filter = ('recommendation', 'job_position')
    readonly_fields = ('generated_at',)


@admin.register(InterviewQuestionSet)
class InterviewQuestionSetAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job_position', 'generated_at')
    search_fields = ('candidate__full_name', 'job_position__title')
    list_filter = ('job_position',)
    readonly_fields = ('generated_at',)