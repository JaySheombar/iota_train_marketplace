import datetime
import pytz

from django.utils import timezone
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Channel
from ..serializers import ChannelSerializer

class Channels(APIView):

	paris_tz = pytz.timezone("Europe/Paris")

	def get_object(self, pk):
		try:
			return Channel.objects.get(id=pk)
		except Channel.DoesNotExist:
			raise Http404

	def get(self, request, format=None):
		channels = Channel.objects.all()
		serializer = ChannelSerializer(channels, many=True)
		return Response(serializer.data)

	def put(self, request, format=None):
		channel = self.get_object(request.data['id'])
		channel.sensor_name = channel.sensor_name
		channel.channel_root = channel.channel_root
		channel.channel_next_root = request.data['channel_next_root']
		channel.pub_date = datetime.datetime.now(tz=self.paris_tz)
		channel.save()
		serializer = ChannelSerializer(channel)
		return Response(serializer.data)

	def post(self,request):
		channel = Channel()
		channel.sensor_name = request.data['sensor_name']
		channel.channel_root = request.data['channel_root']
		channel.channel_next_root = request.data['channel_next_root']
		channel.pub_date = datetime.datetime.now(tz=self.paris_tz)
		channel.save()
		serializer = ChannelSerializer(channel)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def delete(self, request, format=None):
		channel = get_object_or_404(Channel, sensor_name=request.data['sensor_name'])
		channel.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)