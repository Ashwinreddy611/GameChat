#  **GameChat**

## **User Stories**

### **User Experience (UX)**

#### **First Time Visitor Goals:**

a) As a first time visitor I would like to get to grips with and comprehend instantly the purpose and intent of the website. This should be communicated clearly

b) I should be able to search for specific games using a search bar feature as well as have the option to view all games by genre

c) I should be able to see the posts of other users with a feature to identify these users. 

d) I should be able to register an account where I can interact with the sites community via the comment sections of games as well as be able to create a wishlist for all the games I am interested in purchasing in the future. 

#### **Returning Visitor Goals:**
a) As a returning user I would like to be able to manage my account that I have set up when first interacting with the site. There should be no way for an individual to brute force their way into my account.

b) I should also be able to uplad games to the site for the communities benefit where other members can leave their own opiions on and add to their own wishlist if they desire so. Any games, and subsequent comments for the game, that have been uploaded to the GameChat website should only be deletable by an admin of the site and the user who has uploaded said game. 

c) I should be able to manage the games on my wishlist with ease and be able to sort the wishlist by genre as well as alphabetically. 


#### **Site Owner Goals:** 
a) As the site owner I should have full admin capabitlites being able to monitor and update anything I would like to on the webiste. This includes users, games posted and genres of games on the website. 

### Design

#### Colour Scheme
* The colour scheme for my website is a primary colour of red, secondary colour of black in the form of the background and a tertiary colour of white in the form of all scripture on the site. I feel the scheme chosen reflects what I would like the user to feel when on the site and that is relaxed and comfortable. This comfort comes from the dark tones of the site which is less straining to the eyes than more conventional light tones but still retains an aesthetically pleasing design.

#### Typography
* In terms of typography the fonts Monoton and Roboto. The Monoton font was chosen due to the fact that it has a very retro connotation and is a reminder to the user of the games and tech of the past. This is coupled with the Roboto font that is very sleek and modern to connote the ever changing and devloping games coming out now and in the coming future. These two fonts complement each other even though there symbolism run parallel and that's why I was very much happy to choose this pairing.  

### Wireframes
A seperate md file has been created for all wireframes found [Here](/wireframes.md)


### Features
#### Features availible to all members 
* The ability to view all the posts on the site of all the different games. There is also the ability to register for these unregistered memebers which is very easy. 

#### Features available to registered members 
* The ability to post games to the site, edit the details of the post as well as delte the post if they so please. The only other user with the same access to another individuals post is the admin who goes by the name of admin.

#### Review of the website components 
* All users when registering to the website, the proghramming measures take full effect in that users can't register with a taken username or anything less than five characters. This prevents users from registering with a tap of the spacebar. 

* All registered users can only edit and delete their own posts and this is done using a conditional check to have the buttons that allow for editing and/or deletion to only be availiable to said user. 

* The form for the addition of games must have all fields completed properly otherwise the user cannot submit the form. This prevents users from making incomplete posts to the site. 

* The navbar is conditional to the user. If the user is not registered or logged out then all that is available and displayed to the user is the: Home, Log In and Register pages. For all Registered user then what is availiable and displayed is the: Home, Profile, Add Game and Log Out pages. 

#### Features to be implemented in the future
* The first feature to be implemented in the future is a comment section for each post so that registered users can interact with each other and discuss their thoughts about each game. Non registered users would be able to read these comments only. 

* The second feature to be implemented is a button to add a post to a watchlist page. This would essentially be a bookmark feature so that users can save posts for games they are interested in and keep track of games they would like to purchase in the future. 

* The third feature to implement is an affiliate link system where users can sell the game that has been posted and the site would take a percentage of any purchases. The attraction to selling on the website would be that there is a large community of users making a sale very convenient. 

### Database
* The Database design can be found [Here](database.png) 
### Technologies Used
#### Languages
* HTML5
* CSS3
* Javascript
* Python

#### Libraries and Frameworks
* Jinja
* Materialize
* The Py-Mongo Python package
* Werkzeug
* Google Fonts 

#### Other
* Github - were the repository was located.
* GitPod - the develpment evironment where the site was created.
* Heroku - The site were the application has been deployed. 
* MongoDB - The site where GameChat's database information was created.
* RandomKeyGen - The site used to create a secure secret key for the site.

### Testing 
#### Validation
* HTML - All pages passed the validation using the validator found [Here](https://validator.w3.org/nu/). The checks were done by viewing the page sources of each page as the validator had problems with jinja templating. 
* CSS - The css passed validation using the validator found [Here](https://jigsaw.w3.org/css-validator/#validate_by_input).
* JS - The js didn't need validating as all that was used ws jquery used from materialize to intiate it's components.
* Python 

### Deployment 
#### Heroku Deployment 
* Before connecting to Heroku the app needed a procfile, requirements.txt and an env.py file that had the following variables: 
1. os.environ.setdefault("IP", "0.0.0.0")
2. os.environ.setdefault("PORT", "5000")
3. os.environ.setdefault("SECRET_KEY", *undisclosed key*)
4. os.environ.setdefault("MONGO_URI", *undisclosed uri*)
5. os.environ.setdefault("MONGO_DBNAME", *undisclosed db name*)
These were all added to the .gitignore file due to sensitivity. 

* Next a heroku app was created by first loggin in and then clicking "new app", choosing a new and clicking the appropriate region.

* Next the app had to be connected to the github repository. The github deployment method is chosen from the deploy tab, the repo is located and you click connect. Then go the settings page and click config vars, then reveal vars and enter the variables from the env.py file. Now you can enable automatyic deployment from the deployment section, then manual deploy and deploy branch (choosing the master branch). 
#### Forking the Repository
* Log in to your GitHub account and then locate the GameChat Repository
* Above the settings button there is a fork button 
* You'll now have a copy of the repo in your account that you can make changes to whilst keeping the original untouched


#### Making a clone of the Repository
* Log into your Github accopunt and locate the GameChat repository
* Click the code dropdown and copy the repo url 
* Open your terminal application (Git Bash for example) and change the working directory to the location where you want this clone.
* enter the Git clone command and past the orignal url and click enter.

### Credits 
* All images were taken from google images and can be found by searching the game name into the google search bar

* The stripey background on the forms was found on css tricks and can be found [Here](https://css-tricks.com/stripes-css/)
