# LightScout 2020
### Built for the Infinite Recharge FRC Game

This Python based app is made for scouting at competitions, home, and at meetings. The code is developed so that it can be easily redeveloped if we decide to use Kivy the next year!

## Set-Up

You can host the app either on an android tablet or a computer

#### Android Tablet

1. Download "Kivy Launcher" from the Google Play Store (you may have to root your tablet if it does not have the Play Store).
2. Connect a USB cable from the tablet to your computer, and download the required drivers and software (if needed) to transfer files!
3. Clone this repo and put the folder "IRScout" into the "kivy" folder on the tablet. The other files are for automation purposes in your database work!
4. You are done! Launch the Kivy Launcher app and click your app title. The default name is `IRScoutV#.#`

#### Computer

1. Download Python on your computer and make it a path so all folders can access it from the command line
2. Type `pip install kivy` in your command line to install the kivy package. Make sure that python is a full path, or else you won't be able to access the kivy packages outside the folder
3. Run the command inside the "IRScout" folder `python main.py` and you will see a bunch of lines pop up. Your app is starting up and it will soon launch in another window
4. You are done! The app on the computer should function exactly as the app on the tablet!

##Administration

There are several administration tools available to the user!

####Database Creation

You can create a database using your data! If you use the default file names, great! Uploading them into your "After" folder will allow you to run the script "createtodatabase.py". After doing this, you will get a CSV file that will have all your data formatted in a way that can be used by most database interpreters.

####ScoutAdmin

LightScout also offers an administration tool to track progress of the students and disable tablets if needed. Per the game manual, WiFi connections are not allowed, so the process stores a file which will be used when opening "createtodatabase.py". All of the FLAGGED data entries will not be counted. To use the console interface, run `python scoutadmin.py` in the python folder to get started!
