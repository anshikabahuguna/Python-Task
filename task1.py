import os
import pyttsx3

while True:

	print("chat with me about your requirements : " , end='')
	pyttsx3.speak("write your choice")
	p = input()

	if ("run" in p) and ("chrome" in p):
  	  os.system("chrome")
	  

	elif(("run" in p) or ("execute" in p))and (("notepad" in p) or ("editor" in p)) :
  	  os.system("notepad")

	elif("run" in p) and ("vlc" in p) :
  	  os.system("vlc")
	  

	elif(("run" in p) or ("open" in p)) and ("firefox" in p) :
	  os.system("firefox")

	elif(("run" in p) or ("open" in p)) and ("brackets" in p) :
	  os.system("brackets")

	elif(("run" in p) or ("open" in p)) and  ("zoom" in p):
	  speak("opening vlc zoom")
	  os.system("zoom")
	
	elif("exit" in p) or ("quit" in p) :
	  print("Bye Bye!!")
	  pyttsx3.speak("Bye")
	  break;

	else :
  	  print("dont support")