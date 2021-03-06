from rest_framework import serializers
from .models import Tasks


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = ('title', 'status', 'priority')
