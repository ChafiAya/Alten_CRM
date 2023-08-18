from rest_framework import serializers
from .models import Project,Task
from team.serializers import UserSerializer
from client.serializers import ClientSerializer
from django.db.models import Q

class ProjectSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    client = ClientSerializer(read_only=True)
    
    class Meta:
        model = Project
        read_only_fields = (
            'member',
        )

        fields = (
            'id',
            'project_name',
            'project_status',
            'priority',
            'start_date',
            'end_date',
            'assigned_to',
            'client',
            'project_description'
        )


    

class TaskSerializer(serializers.ModelSerializer):
    member = UserSerializer(read_only=True)

    class Meta:
        model = Task

        fields = (
            'id',
            'name',
            'member',
            'status',
            'start_date',
            'end_date',
            'description',
        )
