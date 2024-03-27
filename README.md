# automated-whatsapp-birthday-reminders
Code to send automated birthday reminders on what's app using python

The assumptions made in the creation of this code is that people within a family or friend group or organization desire to be reminded of each others bithdays. To achieve this this code will have you insert the peoples names and phone numbers as seen on whatsapp ie +1234556677 and create a message that you would want to be sent to others to remind them of fellow members birthdays. Enusre to read the comments in the code and the rest of this readme. 

Another assumption since these are birthday reminders this code has been set up to run nonstop 365 days a year. It only runs once a day and then is set to sleep until the next day.
You dont have to keep this running however. If you already have a means remembering birthdays but its a hassle to text all the people to remind them you can always just turn on this code the day before someones birthday and use this code to send the automated messages for you and then terminate it when youre done that way you dont have to keep copying and pasting messages and all that.

Note the code is set to remind people only a day before. So if a persons birthday is March 2nd the reminders will be sent March 1st. BE AWARE OF TIMEZONES. The code will run each day at that same time that you initially ran the code until you terminate the code using ctrl-c on the command line and run it again at a different time. So if you start the code at 6pm and someone is someone else is in another timeszone 6hrs ahead where it is 12am, they will still get the message but if your message isnt clear on when the birhtday is people might think the birthday is March 3rd rather than March 2nd.

Another assumption is that you will be adding your own number and birthday. So that you dont send yourself birthday reminders since the code is using your whatsapp account to be reminding people you will have modify a line of code that will be explained to you later.


Prerequisites:

Ensure you have pyhton3 and pip installed as you will need it to install the needed library and run the code.

In order to run this code go to https://pypi.org/project/pywhatkit/ and install the pywhatkit repository in the directory that you will download the code to.

You will need to open your default browser and sign into whatsapp. You can run the code without doing this but while the code is running you will still have to do this and this can cause the code to miss out on sending messages to people cause it was still running while you were logging in. So make sure that you are signed in first or you might have to kill the code and run it again to make sure that no one doesnt get a reminder.

Code Modifications: 

You will need to modify some lines of code in the birthday-reminders.py.

Special thing to note: the numbers and birthday dictionaries are in the Key Value pair ```String:String``` and ```String:Date``` respectively. If you have a person Jane Jones whose number is +1234567890 and birthday March 4th make sure that to represent that person that the string that you use for the name match in both dictionaries. So it will look like

```"Jane Jones":"+1234567890"``` and ```"Jane Jones":date(2000, 3, 4)```.

- ```birthday = {} ```

  add all the birthdays here of the the people you want to have reminders of birthdays for in the format specified in the comments in the code. This is MANDATORY!
  
- ``` numbers  = {} ```

  add all the numbers as seen in their whatsapp of the the people you want to send reminders of birthdays to in the format specified in the comments in the code. This is MANDATORY!
  
- ```textedNumbers = []```

  this is and array that will be used to keep track of texted numbers. The only number that you need to add to it should be yours so that you dont text yourself. however if someone comes along and says they dont want to get reminders anymore but you still want to remind people of their birthday and how to reach them then add their number to this list in the format specified by the comments. This is OPTIONAL! So you can leave this line as is.

- ```message = ""```

  this string will contain the message you are sending to all the phone numbers so if you leave this blank you will not be sending out anything. This is MANDATORY! It was left blank for you to be creative with your message. read the comments for more info on how the code has been set up to help you add the names and numbers to your message so that you dont have to.
  
Running the Code:

To run the code run ```python3 birthday-reminders.py ``` in command line in the directory of the folder.

The code is meant to be run all year round so to stop it you would need to kill its using the ```ctrl-C```.
