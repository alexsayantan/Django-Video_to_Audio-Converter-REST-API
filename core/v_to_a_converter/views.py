import mimetypes
import os
from wsgiref.util import FileWrapper
from django.http import FileResponse, HttpResponse
from .serializers import UserSerializer, MediaSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from moviepy.editor import VideoFileClip 


# Create your views here.
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MediaView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        serializer = MediaSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            media = request.data.get('media', None)

            if media is not None:
                clip = VideoFileClip(media.temporary_file_path())
                output_path = 'media/audio/output.mp3'  # replace with your desired output path
                clip.audio.write_audiofile(output_path, codec='libmp3lame')

                wrapper = FileWrapper(open(output_path, 'rb'))
                content_type = mimetypes.guess_type(output_path)[0]
                response = HttpResponse(wrapper, content_type=content_type)
                response['Content-Length'] = os.path.getsize(output_path)
                response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(output_path)

                return response
            else:
                return Response("Please Provide Media File", status=status.HTTP_406_NOT_ACCEPTABLE)

            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)