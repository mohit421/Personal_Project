from django.shortcuts import render


'''
- What below code gonna do?
    - It essentially allow us to just render this index template that we have right here
    and then react will take care of that and rendering things inside of this.
    - Notice folder is called 'frontend/index.html' .and we are referencing index.html 
    which is a name of our html file. What render will do is it will take the request and take the templates and simply return that HTML 
    to whatever sent the request. All right, so now we just need to make a URL for this 
    if we don't have urls.py file then create it

'''
# Create your views here.
from django.template.loader import get_template
def index(request, *args, **kwargs):
    print(get_template('frontend/index.html'))
    return render(request, 'frontend/index.html') 

