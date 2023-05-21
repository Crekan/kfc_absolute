from rest_framework import serializers

from .models import Vakantie


class VakantieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vakantie
        fields = ['id', 'vakantie', 'start_vacation', 'end_vacation']


class VakantieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vakantie
        fields = ['id', 'vakantie', 'start_vacation', 'end_vacation']

    def validate_end_vacation(self, value):
        vakantie_choices = Vakantie.TYPE_VERLOF_CHOICES

        if self.initial_data.get('vakantie') in [choice[0] for choice in vakantie_choices if
                                                 choice[0] != 'Социальный(за свой счет)'] and value:
            raise serializers.ValidationError('Это поле должно заполнся при выборе "Социальный(за свой счет)".')
        if self.initial_data.get('vakantie') == 'Социальный(за свой счет)' and not value:
            raise serializers.ValidationError('Это поле должно заполнся при выборе "Социальный(за свой счет)".')
        return value

    def to_representation(self, instance):
        shift_choices = Vakantie.TYPE_VERLOF_CHOICES

        if instance.shift_choices in [choice[0] for choice in shift_choices if choice[0] != 'Социальный(за свой счет)']:
            self.fields['end_vacation'].read_only = True
        return super().to_representation(instance)
