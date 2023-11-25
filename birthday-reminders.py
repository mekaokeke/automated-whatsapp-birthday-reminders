from datetime import date, datetime, timedelta
import pywhatkit
import time

# put all the peoples birtdays in this dictionary. The year doesnt matter. So all the years can be 2000. But if you want to caluclate ages make sure you have the right year.
birthdays = {
    #"John" : date(2000, 1, 13),
}
# put the phone numbers as is they are in whatsapp for the people you want to send reminders to
numbers = {
    #"Alice" : "+123456789012",
}

def findBirthdays():
   # get todays date
   today = datetime.now()
   print("The code ran today on {}".format(today))
   # then use that to figure out tomorrows date
   tomrrow = today + timedelta(1)
   # select only the month and day this is why year is not important cause we dont use it
   day = tomrrow.day
   month = tomrrow.month
   # go through the birthday list and if you find someones whose birthday is tomorrow add their name
   celebrants = []
   for person in birthdays.keys():
       if month == birthdays[person].month and day == birthdays[person].day:
           print("{} is a Celebrant".format(person))
           celebrants.append(person)
   return celebrants

    
def sendMessage(celebrants):
    if len(celebrants) != 0:
        #putting all the celebrants names into one string to be used in message
        names = ""
        for person in celebrants:
            names += person + " "

        #puttinge the celebrants phone numbers into one string to be used in message
        pnumbers = ""
        for person in celebrants:
            pnumbers += numbers[person] + " "

        # array to keep track of texted numbers so that we dont text the same number more than once, put your number so that you dont text myself.
        #only add your number or numbers that are in the numbers dictionary that you dont want to text. If there arent any numbers you dont want to text leave line below as is.
        #textedNumbers = ["+123485435343"]
        textedNumbers = []
        #this will be used to track how many messages were actually sent.
        timeWasted  = 0
        # A variable message that has the string we want to insert. INSERT THE MESSAGE YOU WOULD LIKE WITHIN THE QUOTES. ie "Hi all this is a birthday reminder ..."
        # You can use the names variable and pnumbers variable to insert the names and numbers of the celebrants respectively 
        # that would look like "hi all tomorrow is {} birthday(s) you can call/text them at {} number(s)".format(names,pnumbers)
        message = ""
        # This loop goes through all the phone numbers and makes sure that you are not sending a reminder to any of the celebrants so ensure that names in the birthdays dictionary
        # match names in the numbers dictionary
        # This also means that celebrants will not be reminded of other celebrants birthdays. Hopefully they would already know since they share the same birthday.
        for name in numbers.keys():
            if name not in celebrants and numbers[name] not in textedNumbers:
                textedNumbers.append(numbers[name])
                pywhatkit.sendwhatmsg_instantly(numbers[name], message)
                timeWasted  = timeWasted + 1
                #this sleep is to give it time to send the message before it tries to text the next person
                time.sleep(60)
        print("this is the number of numbers texted {}".format(len(textedNumbers)))
        print(textedNumbers)
        #returns the time wasted assuming it takes a minute to send a message cause of the sleep
        return timeWasted

def main():
    while True:
        celebrants = findBirthdays()
        timeWasted = sendMessage(celebrants)
        #gets the timewasted to use to offset the sleep time so that the code runs the same time everyday
        sleepTime = 86400 - (60 * timeWasted)
        #this sleep is to wait till the next day to run the message
        time.sleep(sleepTime)
       

if __name__ == "__main__":
    main()
