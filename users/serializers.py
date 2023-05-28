from rest_framework import serializers

from . import models


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('email', 'username', 'password')


class CreateTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class GetUserSerializer(serializers.Serializer):
    token = serializers.CharField()


class FeedbackSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    text = serializers.CharField()

    class Meta:
        model = models.Feedback
        fields = ('id', 'user_id', 'title', 'text')

    def create(self, validated_data):
        user_id = self.context.get('user_id')
        user = models.User.objects.get(id=user_id)

        feedback = models.Feedback.objects.create(
            user_id=user,
            **validated_data
        )

        return feedback




