from django.db import models
from django.core.validators import FileExtensionValidator


class Resume(models.Model):
    candidate = models.ForeignKey(
        'Candidate',
        on_delete=models.CASCADE,
        related_name='resumes',
    )
    file = models.FileField(
        upload_to='resumes/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'docx', 'txt'],
            ),
        ],
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f'Resume for {self.candidate.full_name}'