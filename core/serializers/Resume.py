from rest_framework import serializers
from ..models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    candidate_name = serializers.CharField(
        source='candidate.full_name',
        read_only=True,
    )

    class Meta:
        model = Resume
        fields = [
            'id',
            'candidate',
            'candidate_name',
            'file',
            'uploaded_at',
        ]
        read_only_fields = ['id', 'uploaded_at']

    def validate_file(self, value):
        max_size = 5 * 1024 * 1024

        if value.size > max_size:
            raise serializers.ValidationError(
                'File size must not exceed 5 MB.'
            )

        return value