from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Project,Task
from .serializers import ProjectSerializer,TaskSerializer
from django.contrib.auth.models import User

from team.models import Team
from client.models import Client
from django_filters import rest_framework as filters

from .filters import ProjectDateRangeFilter


class LeadPagination(PageNumberPagination):
    page_size = 2


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    pagination_class = LeadPagination
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter,)
    search_fields = ('project_name',)
    filterset_fields = ('start_date',)
    filterset_class = ProjectDateRangeFilter


    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        status = self.request.query_params.get('project_status')
        if status:
            return self.queryset.filter(team=team, project_status=status)
        else:
             return self.queryset.filter(team=team).order_by('-id')
        
    def perform_update(self, serializer):
        obj = self.get_object()
        member_id = self.request.data.get('assigned_to')
        client_id = self.request.data.get('client')

        if member_id:
            user = User.objects.get(pk=member_id)
            serializer.save(assigned_to=user)
        else:
            serializer.save()

        if client_id:
            client = Client.objects.get(pk=client_id)
            serializer.save(client=client)

          

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.data['client']
        client = Client.objects.get(pk=client_id)

        assigned_to_id = self.request.data['assigned_to']
        assigned_to_id = User.objects.get(pk=assigned_to_id)

        serializer.save(team=team, member=self.request.user, client=client, assigned_to=assigned_to_id)


    
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        project_id = self.request.GET.get('project_id')

        return self.queryset.filter(project_id=project_id)

    def perform_update(self, serializer):
        obj = self.get_object()
        member_id = self.request.data['member']
        if member_id:
            user = User.objects.get(pk=member_id)
            serializer.save(member=user)

        else:
            serializer.save()

    def perform_create(self, serializer):
        # department = Department.objects.filter(member__in=[self.request.user]).first()
        project_id = self.request.data['project_id']
        member_id = self.request.data['member']
        member = User.objects.get(pk=member_id)
        serializer.save(project_id=project_id, member=member)


@api_view(['POST'])
def delete_project(request, project_id):
    team = Team.objects.filter(members__in=[request.user]).first()

    project = team.projects.filter(pk=project_id)
    project.delete()

    return Response({'message': 'The project was deleted'})


@api_view(['POST'])
def delete_task(request, project_id, task_id):
    team = Team.objects.filter(members__in=[request.user]).first()

    project = team.projects.filter(pk=project_id)
    task = Task.objects.filter(pk=task_id)
    task.delete()

    return Response({'message': 'The task was deleted'})


@api_view(['GET'])
def get_my_tasks(request):
    # Get the logged-in user
    logged_in_user = request.user

    # Filter tasks assigned to the logged-in user
    tasks = Task.objects.filter(member=logged_in_user).all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)



class PairByPriorityStatusListView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        pair_queryset = Project.objects.all()
        user = self.request.user

        if user.is_authenticated:
            priority = self.request.query_params.get('priority')
            status = self.request.query_params.get('project_status')

            pair_queryset = Project.objects.all()
            if priority and status:
                pair_queryset = pair_queryset.filter(priority=priority, project_status=status)

        return pair_queryset


class DateOrderedFilterView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (OrderingFilter,)
    filterset_fields = ('start_date',)


class ProjectSearchFilterView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('project_name',)


class ProjectDateRangeFilterView(ListAPIView):
    queryset =  Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectDateRangeFilter


