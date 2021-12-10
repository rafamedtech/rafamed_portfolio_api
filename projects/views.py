from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
# from rest_framework.permissions import IsAuthenticated, IsAdminUser


from .serializers import ProjectSerializer, TagSerializer
from projects.models import Project, Tag
# Create your views here.



class ProjectsView(APIView):
    parser_classes = [MultiPartParser, JSONParser, FormParser]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)

# create an api_view for creating a project
class ProjectCreateView(APIView):
    parser_classes = [MultiPartParser, JSONParser, FormParser]
    
    def post(self, request, *args, **kwargs):
        data = request.data
        tags = data['tags'].split(',')
        tags = [tag.strip() for tag in tags]

        # create a project
        project = Project.objects.create(
            title=data['title'],
            description=data['description'],
            featured_image=data['featured_image'],
            demo_link=data['demo_link'],
            source_link=data['source_link'],
        )

        # create a tag
        for tag in tags:
            
            newTag = Tag.objects.create(name=tag.capitalize())
            project.tags.add(newTag)

        # serialize the project
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeleteProject(APIView):
    def delete(self, request, pk):
        project = Project.objects.get(id=pk)
        project.delete()
        return Response('Project deleted')




class RemoveTag(APIView):
    def delete(request):
        tagId = request.data['tag']
        projectId = request.data['project']

        project = Project.objects.get(id=projectId)
        tag = Tag.objects.get(id=tagId)

        project.tags.remove(tag)
        return Response('Tag was deleted!')