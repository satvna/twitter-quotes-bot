# What does this do?
After uploading images, text, and video to Firestore, this bot will post an entry randomly every 12 hours. It keeps track of which tweets have already been uploaded, and will stop posting if all entries have been tweeted.

![image](https://github.com/user-attachments/assets/a47fedba-5e62-49b6-8a4f-3c390a3c4982 | width=100)
*An example of the bot*


# Setup - Firestore
- Create a [Firebase](https://firebase.google.com/) account. Once in the console, create a project.
- Go to Project settings -> Service accounts and generate a new key. Store the JSON file in the same directory as twitter-bot.py and set firebase_credentials (in keys-template.py) to the filename.
- Once your project is created, add a Firestore Database. 
- Start a new collection named "quotes".
- To start adding your favorite quotes, add a new document (any name is fine). Under the document, add three fields:
  
Field: "alreadyquoted"  Type: boolean   Value: false

Field: "quote"  Type:string  Value: "if quote, insert the text for your favorite quote here. if an image, paste the image link here"

Field: "type"  Type:string  Value: "if quote, set value to 'string'. if image, set to 'image'."

# Setup - Twitter Developer Portal
- Apply for a Twitter for Developers account. Follow [this tutorial](https://blog.hubspot.com/website/how-to-make-a-twitter-bot) to create a project and generate your keys.
- In the "other" directory, rename "keys-template.py" to "keys.py". 
- Store your generated keys in the keys.py file.

# Setup (Optional) - PythonAnywhere
You can host your bot for free on [PythonAnywhere](https://www.pythonanywhere.com/) and schedule your tweets with Tasks.

However, on the free tier, your bot will only run once a day (you only get one task).

- Create an account. On the dashboard, under files, upload this project. 
- Next, under consoles, create a bash console. In this console, create a virtual environment named "myvirtualenv" and install the required packages. Run twitter-bot.py to make sure it's working, then CTRL+C to cancel.
- Finally, under the tasks tab, create a task. Set the time to when you want your bot to tweet.
Task command:
source virtualenvwrapper.sh && workon myvirtualenv && python /home/username/twitter-bot.py

