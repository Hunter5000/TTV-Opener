import easygui as eg
import os

def openChat(url):
	check1 = url.find("http")
	if check1 != -1:
		newurl = (url + "/chat")
		webbrowser.open_new(newurl)
		os.system("livestreamer " + newurl + " best")
		return "Opening..."
	check2 = url.find("twitch.tv")
	if check2 != -1:
		newurl = ("http://" + url + "/chat")
		webbrowser.open_new(newurl)
		os.system("livestreamer " + newurl + " best")
		return "Opening..."
	if check1 == -1 and check2 == -1:
		newurl = ("http://twitch.tv/" + url + "/chat")
		webbrowser.open_new(newurl)
		os.system("livestreamer " + newurl + " best")
		return "Opening..."		
	return "Error"

while 1:
    msg = "Open the given stream using Livestreamer and its chat in a new browser tab"
    title = "TTV Opener"
    fieldNames = ["Stream"]
    fieldValues = []
    fieldValues = eg.multenterbox(msg,title, fieldNames)

    message = openChat(fieldValues[0])

    eg.msgbox(message, "For points (" + fieldValues[0] + "," + fieldValues[1] + "), (" + fieldValues[2] + "," + fieldValues[3] + "), and (" + fieldValues[4] + "," + fieldValues[5] + ")")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if eg.ccbox(msg, title):
        pass  # user chose Continue
    else:
        sys.exit(0)
