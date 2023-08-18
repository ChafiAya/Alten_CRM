from django.db import models
from django.contrib.auth.models import User
from team.models import Team
from client.models import Client

class Project(models.Model):
    NEW = 'new'
    IN_PROGRESS = 'inprogress'
    CANCELLED = 'cancelled'
    FINISHED = 'finished'
    FROZEN = 'frozen'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (CANCELLED, 'Cancelled'),
        (FINISHED, 'Finished'),
        (FROZEN, 'Frozen'),
    )

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high')
    )

    team = models.ForeignKey(Team, related_name="projects", on_delete=models.CASCADE, blank=True, null=True)
    project_name = models.CharField(max_length=255)
    project_status = models.CharField(max_length=25, choices=CHOICES_STATUS, default=NEW)
    priority = models.CharField(max_length=25, choices=CHOICES_PRIORITY, default=MEDIUM)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    assigned_to = models.ForeignKey(User, related_name='assignedprojects', blank=True, null=True, on_delete=models.SET_NULL, default=None)

    project_description = models.TextField(max_length=400, blank=True, null=True)
    member= models.ForeignKey(User, related_name='project_app', blank=True, null=True,
                                 on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, related_name='project_app', on_delete=models.CASCADE, blank=True, null=True)




class Task(models.Model):
    # department = models.ForeignKey(Department, related_name="projects", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)

    NEW = 'new'
    IN_PROGRESS = 'inprogress'
    CANCELLED = 'cancelled'
    FINISHED = 'finished'
    FROZEN = 'frozen'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (CANCELLED, 'Cancelled'),
        (FINISHED, 'Finished'),
        (FROZEN, 'Frozen')
    )

    status = models.CharField(max_length=25, choices=CHOICES_STATUS, default=NEW)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    name = models.TextField(max_length=400, blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)
    member= models.ForeignKey(User, related_name='assignedtasks', blank=True, null=True,
                                 on_delete=models.SET_NULL)