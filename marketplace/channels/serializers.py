from rest_framework import serializers

from .models import Channel

class ChannelSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=False, allow_blank=True, max_length=200)

	class Meta:
		model = Channel
		fields = '__all__'