from django.db import models
from django.core.exceptions import ValidationError


class JobPosition(models.Model):
    department = models.ForeignKey(
        'Department',
        on_delete=models.PROTECT,
        related_name='job_positions',
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


    def clean(self):
        super().clean()

        if not isinstance(self.required_skills, list):
            raise ValidationError({
                'required_skills': 'Skills must be a list.'
            })

        if any(
            not isinstance(skill, str) or not skill.strip()
            for skill in self.required_skills
        ):
            raise ValidationError({
                'required_skills': 'Each skill must be non-empty text.'
            })