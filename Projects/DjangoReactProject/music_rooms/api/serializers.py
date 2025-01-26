

from rest_framework import serializers # type: ignore
from .models import Room # type: ignore

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room 
        '''
        We have wondering why we have id
        - Well each of our model have something called a primary key and primary key is some unique integer
        - typically that can identify the model  in relations to all the other model. So, it's always unique
        - Usually, an integer and it will be automatically created when we actually insert in this case a new room into our database
        - So even though we have not defined an ID in Room model models.py, It will automatically an  ID fields on every single model
        - So we we want to see id field we have to add id in fields and return that
        - that make more sense as we get through
        '''
        fields = ('id','code','host','guest_can_pause',
                  'votes_to_skip','created_at')

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room 
        fields = ('guest_can_pause','votes_to_skip')

class UpdateRoomSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])
    class Meta:
        model = Room 
        fields = ('guest_can_pause','votes_to_skip','code')