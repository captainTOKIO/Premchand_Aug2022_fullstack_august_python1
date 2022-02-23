from rest_framework import serializers
from problems.models import Problems

class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields=('ProblemId','Title','Solution','Difficulty')
