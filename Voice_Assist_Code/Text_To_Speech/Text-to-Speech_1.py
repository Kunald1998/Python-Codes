# Below both module is need to be install using pip. it is not comes with python.
import gtts # google-text-to-speech.
from playsound import playsound

# This code creates 'audio.mp3' file every time when we create object and
# that audio.mp3 file contains voice of that text we provided.

def Add(no1,no2):
    return (no1 + no2)

def main():
    obj3 = gtts.gTTS("Hay there.") # Object creation.
    obj3.save("greetings1.mp3") # Create a file with the provided name in current directory, and convert text into speach.
    playsound("greetings1.mp3") # Playing that created file.

    obj4 = gtts.gTTS("Welcome to marvellous infosystems.")
    obj4.save("greetings2.mp3")
    playsound("greetings2.mp3")

    obj1 = gtts.gTTS("Please enter first number.")
    obj1.save("no_one.mp3")
    playsound("no_one.mp3")

    No1 = int(input("Please enter first number: "))

    obj2 = gtts.gTTS("Please enter second number.")
    obj2.save("no_two.mp3")
    playsound("no_two.mp3")

    No2 = int(input("please enter second number: "))

    Ret = Add(No1,No2)
    print("The addition of given two number is: {}".format(Ret))
    strx = str(Ret)

    speach = "The addition of given two number is"+ strx

    obj3 = gtts.gTTS(speach)
    obj3.save("Ret.mp3")
    playsound("Ret.mp3")

if __name__ == "__main__":
    main()

# Below thing are my predictions.
# save() method internally act like open(file="name that we provided",mode="wb")w=write b=binary.
# playsound() method internally open that created file in mode='b' mode.