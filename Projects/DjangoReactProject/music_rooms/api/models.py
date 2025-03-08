from django.db import models
import string
import random


'''
Any standard database would have a table. You would have rows and columns in those tables
and that how's you would store information.
Now, that's no different in django, but when we actually go ahead and create a table, what 
we're going is creating a model instead. So what Django allows us to do is write Python code, 
that will interpret that python code and automatically perform all of the database 
operations for us.
So, essentially it's a layer of abstraction it makes it a lot easier for us as Python 
developers to write database related stuff.

'''

'''
 the model that we only have is room model
 Our app we would have to group similar users together, or group users together in a room
 that room will control over the host music.
 - One person hosting or playing a music and other people join in on this 
    room and they can control that music
'''


'''
- Basic rule in django is to have fat models and thin views.
- That means put most of the logic in our models that what django is trying to tell us to do
- My code for the room is random and to be unique.
- every time we create a room we come up with some random 8 digit code that represent us a room
-
'''
def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code

# Create your models here.
# Room model to represent a room for hosting music sessions

class Room(models.Model):
    code = models.CharField(
        max_length=8, default=generate_unique_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    current_song = models.CharField(max_length=50, null=True, blank=True)
    volume = models.IntegerField(default=50)  #store volume

    
    # Now, our migrations is done. apply makemigrations and migrate 
    # We have create our model. We want to setup an API view. This is different from standard HTML view.
    # They can return all of the Room that are currently in our database.
    # We trying to program a backend. What's mean by backend is that
    #  is just the server that essentially can handle information. So handle requests, and
    # give some type of valid response. if we think about it, It would make sense that our frontend want to be able to
    # access or check specific rooms, Users try to join a room needs to look in the rooms 
    # In the backend notice that roo exist? 
    # So need to create some kind of endpoint that can return to us information about the rooms in a format that make sense.
    # We probably not going to return HTML code we return JSON format , where key value pair and our frontend really easily handle 
    # look at it and do things with now. We create serializers file that takes Room models
    #  that will translate our room into json response.


