


# React integration Using Webpack & Babel

- Type NPM and make sure that this cmd works
- If it does good to go and if it doesn't make sure you download and install NPM and nodejs.
- Next thing that we do is create a new app inside of our Projects we don't called this an app but in fact, what we called is a frontend cuz this app is going to  store the frontend of our project
- Run django-admin startapp frontend - Now e have a frontend app inside our directory
- cd .\frontend\
- Create a few folder
- static and template folder and also a source and component folder.
- Now this app here is now going to be storing all of the stuff related to our frontend related to react aspect of this project.
- Static folder is gonna store all of the static files that the pretty much that the browser would cash 
- And infact, so we can separate all of the different things inside of here, and we going to make three folders 
    1. frontend :- store our main JS bundle
    2. css:-  
    3. images
- We have package.json file inside frontend. Our node modules come after doing few more thing.
- So now that we have that to do is a bunch of stuff from NPM.
- NPM store all of the modules like react. It can store a Babel and can store a webpack. 
- It's gonna do all the things that we need to actually transpile our code and get ready to run in the browser
- npm i webpack webpack-cli --save-dev 
- We need webpack what web pack going to do is take all of our source Javascript stuff. It's gonna trans pile it. That bundle it into a single Javascript file.
- Next thing that we going to install is Babel 
- It will take our code and transpile it into code that is friendly with all different types of browsers. So we're going in writing with, I believe it's ES6 or ES7 in JS code it's like newer JS code 
- This will take our code and compile it just kind of convert it that will run in older browsers that what Babel does for us.
- npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
- Next thing we need to install is react
- npm i react react-dom --save-dev
- We need to install material UI - similar to bootstrap and tailwindcss
- npm install @material-ui/core
- npm install @babel/plugin-proposal-class-properties - we need to include async and await in our JS code 
- npm install react-router-dom
- npm install @material-ui/icon
- Add scripts from github in babel.config.json and webpack.config.json inside frontend
- IN package.json inside scripts we need to add two scripts there
    1. Dev scripts:- "dev":"webpack --mode development --watch" :- what this will do is we wanna webpack to run. we want to run in the development mode and we want it to be in watch mode. Just like the server we are running before 
    - Just like the server that we were running before. so that python script. 
    - This wil just watch the changes to our JS file then automatically recompile or re-bundle whatever we wanna call it. the output JS file so that bundled file so that we can just refresh our browser and everything be all good

    2. Build Scripts:- 
    "build":"webpack --mode production"

- What we need to do now is actually make it so that our Django  app will render a page that react will take control of So this is seems kind of strange and if we haven't used Django and react before 
- The idea here is going to have our Django application render a template, which gonna be some vanilla, plain HTML and then 
- REACT code is going to take over that template and actually fill it in. So we will technically have the Django backend actually rendering the template, but react will manage it after that.

- Let's go to views file into our frontend a little strange, but we need to just render this index template and then let react, take care of it.
- go and write som code in views.py and create a urls.p file inside frontend.
    - and add url inside our music_rooms app with an i=empty string and targeting to frontend.urls.
    - That way we can handle the urls from the frontend.
    The reason we need that we see it

- Let make a component called app.js and now let writing some react code. So don't worry it doesn't make any sense to us 
- We render the App component inside the appDiv
-We have app component we just need to now put this into essentially our index.js file the way that we actually get this to work.
- We simply import App from './components/App' inside index.js
- Now index.js file will importing the file it will run the code it will render App int the index.html template


<!-- Tutorial 5 -->
<!-- Handling Post requests -->

- We will working on Backend:-
- We're gonna be writing view that will allow us to actually create a new room by simply sending a post request to the end point that we setup
- Go to APi->views.py 
 Import from rest_framework.views import APIView
from rest_framework.response import Response
- From this we will send a custom response from our view
- Status will give us HTTP status code, which we are going to use when we use our custom response.

- Create another serializer CreateRoomSerializer:-
- The idea behind this is we are going to send a post request, to the end point we are going to set up here. So we'll make a view inside up here. They will handle a post request and the  post request we're not aware is typically when we are creating something new, we send something new that we type of request and we send a payload that has information in it.
So I will send a post request to say like /create-room what hidden in this request is what we were typing this in is the payload that have the information in the post-request. SO, we'll have a payload that has something like  {votes_to_skip:3, guest_can_pause:True}
- We want serializer here to pretty much sure make sure that the data that's being sent in our post request is valid and that it fits or correspond to the correct fields that we need to create a room.
- So whenever we are handling different requests, it's usually a good idea to get a serializer, either an incoming serializer to handle the request or an outgoing one to handle the response depending on what we are sending.
- how to get host?
Well the frontend, or whoever's sending us request, isn't really going to know how to how to identify who the host is and hence, it doesn't really make sense for them to send us the host the way in which is going to puck how we store the host or figure out who the host is , by using something called a session key. So this leads me to sessions, Which I need to discuss and that's kind of why I went back to room here. But whenever we connect to a website, what happens is we establish as a session.
- Session is just a temporary connection between two computers or between two devices. that's the best way to think about it. and a way that session works, the best example  session is something like you heading to facebook or Instagram or a page that you frequently visit, and that you have to signin to but you're on the same device that we always, we don't have to 
- So when we got to Facebook., we have been there yesterday and day before yesterday we signed in some point recently It doesn't ask us to sign in again The reason it doesn't ask us to do that again is bcuz we are on the same session that we were previously,
- SO that know the person who is in this session is aleady authenticated and already signed in and hence, we don't need to sing them in again.
-mIf that was not the case then we need to go different url every time on FB, we would have to sign in  again , again and again and obviously that's not good. The way that sessions are itentified is by a unique key. SO it does have to do with your IP address and location in the world. But session have unique identity and while our web browsers establishes a session with your website it remembers us quotes unquote for a temporary period of time.
- Now, this session is stored in memory typically. At least our Django app to be stored in memory so in system RAM,essentially.
- Which means if we stop running this app or the server goes down our computer crashes or lose that session data.
- Now, that fine we don't care for permanently identify users. We just need to know relatively which users is which and if they're currently  hosting a room or if they aren't figure that out.



<!-- Material UI Components - Part 6 -->

- In this we are creating a CreateRoomPage . So actually be filling out all of the annoying html that we need all of the components to make this look half decent, we'll then be hooking this up to the backend and so making them as user can actually, press a button and deal with some nice frontend UI and forms based on the information.

- After making createRoomPage functional
- We need to hook this up to the backend
- Go to handleRoomButtonPressed():-
    instead of console.log() - let's actually send a request to the endpoint we have created previously that will allow us to actually create the new room with the information from this form \\\



<!-- Django & React Tutorial #7 - Calling API Endpoints From React-->

- Right now, we are able to create a room 
for eg:- {id: 3, code: 'YGCBSV', host: 'da849fscdpsv8yn6pyi8iq47b98bsgr4', guest_can_pause: true, votes_to_skip: 5, …}

- How to view room:-  using code to access the room 

- We need to get the others details like, we need the votes to skip and guest can pause and we need isHost or not 
How we do this?
    - We have to send a request to a backend for this information.
    So, what we're gonna give our backend the room code, and then the backend we'll look at that room code , find the room and give us the information that  we want like votes to skip and guest can pause is host and maybe anything else. 
    - So let's go to views.py inside tof API, and let's make a new views that can do that for us.
    - ```
    Get Room
GET /api/get-room?code=YGCBSV
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 3,
    "code": "YGCBSV",
    "host": "da849fscdpsv8yn6pyi8iq47b98bsgr4",
    "guest_can_pause": true,
    "votes_to_skip": 7,
    "created_at": "2025-01-23T19:31:57.485192Z",
    "is_host": true
}```
- We need to send this request from to Javascript  we'll be update our state on our room
- For that we need to add method inside there called getRoomDetails
- Everything working now,
- When we click on create room button then it will redirect to correct page - 

<!-- Django & React Tutorial #8 - Creating The Room Join Page -->

- Create Join Room Page just like createROom page once frontend working with all functionality
- Hook this up with the backend

- self.request.session['room_code'] = code
    what above line tell us:
        - before return Response, what we do actually is to make a note on the backend that this user is iin this room. 
        - we make a new variable called room_code 
        - this tell us that, hey, this user in its current session is in this room. So later on, we will check that 
        user is currently in a room and if they are say they, return to the website, like they close their safari, or close their mobile phone app, whatever and when they come back to it later we'll know that they were originally in this room and we can return them to that room without having them to type the code in again. 
    - Essentially what we want to do with sessions is store information relevant to each individual user or to each individual session. So by me saying self.request.session and typing in that code 'room_code' 
    - What i really doing is creating a kind of temporary storage object. That's called room_code and is being equal to whatever the value of code is variable code 
    - This will just be stored in this Just like this user session, just like this user has a session key  
    - This is kind of way to store your own info in the user's session 