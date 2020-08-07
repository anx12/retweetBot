

## Twitter Bot for liking and retweeting a tweet that contains a search-term, from your account automatically every 100 seconds

Every 100 seconds because twitter has a cap of 2400 tweets every 24 hours. You can make a maximum number of requests through API calls.
I wouldn't recommend anything less than 40 seconds.

### PREREQUISITES
> Before running the script you need to make sure you have all these prerequisites. Heroku Account is optional.
* [Developer account](https://developer.twitter.com/apps) You need to have a developer account for this and then you need to create an app in your Twitter developer account. 
   Make sure to set the app permissions to 'read and write' and then generate the 'access_token' and 
   'access_token_secret' keys. 
   Make sure to save the api_key, api_secret_key, access_token and access_token_secret key to your notepad before proceeding and then put them in your script.py
   Also put your search-term in script.py in line(11).
     https://developer.twitter.com/apps

* [Git](https://git-scm.com/downloads)

* [Python](https://www.python.org/downloads/)

* [Heroku Account](https://www.heroku.com/) (Only if you are planning to run the script on a server)




# Running the script
## I would recommend running the script locally on your machine if you find it difficult running it on Heroku server


1. If you want to run the script locally on your machine just run the ```script.py``` file.
   NOTE-If you are using Windows you need to install Python https://www.python.org/downloads/ and Git https://git-scm.com/downloads first.
        If you are using Linux they are already preinstalled.
   Once Python and Git are installed, open terminal or command-prompt and then copy and paste the higlighted commands in terminal or command-prompt:
   NOTE: You have to keep your terminal or command-prompt open the whole time.
   ```bash
   cd Desktop
   ```
   ```bash
   git clone https://github.com/anx12/retweetBot.git
   ```
   * This will create a folder named 'retweetBot' in your Desktop folder. The 'retweetBot' folder will contain all the files including 'script.py' file. Open script.py in            your editor(notepad or any other) and place your api_key, api_secret_key, access_token and access_token_secret keys in script.py and save. Then go back to terminal or            command-prompt and enter the below commands.
   ```bash
   cd retweetBot
   ```
   ```bash
   pip install tweepy
   ```
   ```bash
   python script.py
   ```

2. If you want to run the script on Heroku server upload all the files to Heroku server.
   Follow these steps:
   1. Create heroku account https://www.heroku.com/
      Create an app in Heroku
      Install heroku cli https://devcenter.heroku.com/articles/heroku-cli

   2. ```git clone``` this repository. 
      If you are using Windows you need to install Git https://git-scm.com/downloads
      Open your terminal or command-prompt and enter this command:
      ```bash
      git clone https://github.com/anx12/retweetBot
      ```
   
   3. Move into the cloned folder
      ```bash
      cd retweetBot
      ```
      
   4. Open script.py in your editor and place your api_key, api_secret_key, 
      access_token and access_token_secret keys in script.py
   
   5. Then commit the changes 
      ```bash
      git add .
      ```
      ```bash
      git commit -m "change keys"
      ```
      
   6. Upload files to Heroku
      ```bash
      heroku login
      ```
      ```bash
      $ heroku git:remote -a your_Heroku_app_name
      ```
      ```bash
      git push heroku master
      ```
      
   7. To run your application
      ```bash
      heroku ps:scale worker=1
      ```
      
   8. From now on you can use usual git commands (push, add, commit, etc.) to update your app. 
      Every time you push heroku master your app gets redeployed with updated source code
      
   9. To see your logs
      ```bash
      heroku logs --tail
      ```
      
   10. To stop your application
       ```bash
       heroku ps:scale worker=0
       ```
     
      
   

