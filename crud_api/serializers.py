from rest_framework import serializers
from crud_api.models import User, Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    task = serializers.HyperlinkedRelatedField(many= True, view_name = 'task-detail', read_only = True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'task']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Task
        fields = ['url', 'id', 'user', 'title', 'task_detail', 
                  'date_created', 'due_date', 'date_finished',
                  'completed']