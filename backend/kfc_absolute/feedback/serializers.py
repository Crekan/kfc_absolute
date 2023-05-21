from rest_framework import serializers

from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'address', 'team', 'situation', 'other']


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'address', 'team', 'situation', 'other']

    def validate_other(self, value):
        for_whom_choices = Feedback.TYPE_TREATMENT_CHOICES

        if self.initial_data.get('address') in [choice[0] for choice in for_whom_choices if
                                                choice[0] != 'Другое'] and value:
            raise serializers.ValidationError('Это поле должно заполнся при выборе "Другое".')
        if self.initial_data.get('address') == 'Другое' and not value:
            raise serializers.ValidationError('Это поле должно заполнся при выборе "Другое".')
        return value

    def to_representation(self, instance):
        for_whom_choices = Feedback.TYPE_TREATMENT_CHOICES

        if instance.shift_type in [choice[0] for choice in for_whom_choices if choice[0] != 'Другое']:
            self.fields['other'].read_only = True
        return super().to_representation(instance)
