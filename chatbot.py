import os 
import pyttsx3 as pyt

print(".........................................................................")
print("............ Hello! Welcome to IIEC RISE, How May I Help You ............")
print(".........................................................................")
pyt.speak("Hello, Welcome to IIEC RISE, How May I Help You")
print()
resume="Yes"

while("Yes" in resume or "yes" in resume):
    print("Please Enter what you want to do. : ",end="")
    pyt.speak("Please Enter what you wnat to do")
    p=input()


    if ((("want" in p) or ("run" in p) or ("play" in p) or ("open" in p)) and ("music" in p or "songs" in p)) or ("music" in p or "song" in p or "songs" in p):
        pyt.speak("Opening a media player for you")
        os.system("wmplayer")

    elif ((("want" in p) or ("run" in p) or ("execute" in p) or ("open" in p)) and ("notepad" in p or "text editor" in p)) or ("notepad" in p or "text editor" in p):
        pyt.speak("Opening a text editor for you")
        os.system("notepad")

    elif ((("want" in p) or ("run" in p) or ("execute" in p) or ("open" in p)) and ("chrome" in p or "chrome browser" in p)) or ("chrome" in p or "chrome browser" in p):
        pyt.speak("Opening chrome browser for you")
        os.system("chrome")

    elif ((("want" in p) or ("run" in p) or ("execute" in p) or ("open" in p)) and ("paint" in p)) or ("paint" in p):
        pyt.speak("Opening paint for you")
        os.system("mspaint")

    elif ((("want" in p) or ("run" in p) or ("execute" in p) or ("open" in p)) and ("wordpad" in p)) or ("wordpad" in p):
        pyt.speak("Opening wordpad for you")
        os.system("WINWORD")

    elif ((("want" in p) or ("run" in p) or ("execute" in p) or ("open" in p)) and ("powerpoint" in p)) or ("powerpoint" in p):
        pyt.speak("Opening powerpoint for you")
        os.system("POWERPNT")

    elif ((("want" in p) or ("run" in p) or ("execute" in p) or ("open" in p)) and ("onenote" in p)) or ("onenote" in p):
        pyt.speak("Opening wordpad for you")
        os.system("ONENOTE")

    elif ((("want" in p) or ("run" in p) or ("execute" in p) or ("open" in p)) and ("outlook" in p)) or ("outlook" in p):
        pyt.speak("Opening powerpoint for you")
        os.system("OUTLOOK")
        
    elif ((("want" in p) or ("run" in p) or ("execute" in p) or ("open" in p)) and ("excel" in p)) or ("excel" in p):
        pyt.speak("Opening excel for you")
        os.system("EXCEL")    

    elif ((("want" in p) or ("run" in p) or ("execute" in p) or ("open" in p)) and ("control panel" in p)) or ("control panel" in p):
        pyt.speak("Opening control panel for you")
        os.system("control")

    elif ((("want" in p) or ("run" in p) or ("execute" in p) or ("open" in p)) and ("cmd" in p)) or ("cmd" in p):
        pyt.speak("Opening command prompt for you")
        os.system("conhost")

    elif ("exit" in p or "close" in p):
        break

    else:
        print("Sorry, Can't get You")
        pyt.speak("Sorry, Can't get You")
    
    
    print("\nDo You want more Help!! \nPress Yes for continue, No for Exit the Program : ")
    pyt.speak("Do You want more Help, Press Yes for continue, No for Exit the Program")
    resume=input()
    print()





