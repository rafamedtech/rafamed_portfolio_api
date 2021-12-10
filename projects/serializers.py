
from rest_framework import serializers
from projects.models import Project, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)


    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'featured_image', 'demo_link', 'source_link', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        project = Project.objects.create(**validated_data)
        for tag in tags_data:
            Tag.objects.create(project=project, **tag)
        return project
        