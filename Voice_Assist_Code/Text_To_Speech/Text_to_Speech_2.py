# Below module is need to be install using pip. it is not comes with python.
import pyttsx3

# This code will not generate any 'audio file.mp3' in current directory.
def AddNumber(A,B):
	return (A + B)

def main():
	obj = pyttsx3.init() # Object creation.
	VoiceList = obj.getProperty('voices') # This method return lest of voice only male and female voice. list = [<pyttsx3.voice.Voice object at 0x000001B9D202AE60>, <pyttsx3.voice.Voice object at 0x000001B9D202B220>]
	obj.setProperty('voice', VoiceList[0].id) # Here we select/set male voice as VoiceList[0] or female voice as VoiceList[1]

	print("Hay there...")
	pyttsx3.speak("Hay there.")
	print("Welcome to Marvellous Infosystems.")
	pyttsx3.speak("Welcome to Marvellous Infosystems.")

	pyttsx3.speak("Please enter first number.")
	No1 = int(input("Please enter first number: "))

	pyttsx3.speak("Please enter second number.")
	No2 = int(input("Please enter second number: "))

	Ret = AddNumber(No1,No2)
	print("The addition of given two number is: ",Ret)

	strx = str(Ret)
	speach = "The addition of given two number is"+strx
	pyttsx3.speak(speach)

if __name__ == "__main__":
	main()