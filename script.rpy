# Declare characters used by this game. The color argument colorizes the
# name of the character.
#Defining character's name as None sets them as a potential narrator.
#set each characters window_style equal to the window style you want them to use.
#namebox_xpos adjusts the character's position within the textbox so that they don't look out of place.
#can use "namebox_[insert parameter here]" to adjust other qualities of the namebox for specific characters
define e = Character("Eileen", window_style = "ig_window", what_style = "ig_dialogue", namebox_xpos = 450)
default alt_narrator = Character(None, window_style = "ig_window", what_style = "ig_dialogue")
default reg_narrator = Character(None, window_style = "window")
define pName = Character("[my_name]") #represents the protagonist's name which will be defined by the player via an input screen.
default newChat = default #an empty variable that can be set to any ChatEntry object so we can add story specific comments to the chat screen.
default viewCount = 4 #viewCount changes how many viewers are displayed in the streamdetails screen
default macroChoice = False #this variable adjusts where the choice screen will appear. It should be False when decisions happen in microgame. It should be True when decisions happen in macro game.
#Full disclosure, keeping track of the variable macroChoice is probably going to be a bit of a pain. 
#It's doable, but just a bit unintuitive. Open to alternatives.

# The game starts here.

label start:
    #these six lines define transforms that can be used to align microgame characters where we want them on the screen
    #They're based on two images (profile1small and profile2small) and will need to be changed once we know the dimensions of character portraits
    #We'll want all our character portraits to be the same size so this method of defining transforms works consistently
    transform gameleft:
        xpos 0
        ypos 615
    transform gameright:
        xpos 1249
        ypos 615

    $ narrator = alt_narrator #setting narrator so the text will appear in the middle of the screen
    scene streamsetup
    #Since our full game screen will be composed of multiple discrete screens, we need to specify which screen layers
    #the backgrounds are appearing on. "onlayer master" ensures that they will still appear behind character portraits
    #and behind textboxes.
    show desert at topleft onlayer master

    "Hello! This is the start of the game!"

    "So you should make a new name!"
    $ my_name = renpy.input("Your name is: ") #invokes an input screen that allows player to define their own name

    "Your name is now [pName]" #the player's name can now be interpellated using this method

    #The next six lines test that character window styles are working appropriately
    #Eileen's should appear in the same location every time.
    #The narrator location should change each time the narraator is altered.
    "You've created a new Ren'Py game."

    e "You've created a new Ren'Py game."


    $ narrator = reg_narrator
    "The narrator has changed the narrator and should appear in a different spot!"

    e "This is checking that the character Eileen will continue appear in a consistent space even when Narrator changes"

    $ narrator = alt_narrator #sets narrator to where dialogue will appear during micro game situations
    "This is the last check"

    e "This is the last check"

    $ narrator = reg_narrator #sets narrator to where dialogue will appear during macro game situations
 
    "Now we'll test the stream set up"


    "This displays a screen for the chat"
    show screen streamDetails
    show screen streamChat

    e "Text will now be added to the chat"
    $ AddToChats() #This will execute the referenced function in the Lists script, adding a new Chat from the comments_list

    e "The screen should have changed"

    e "Let's try again"
    $ AddToChats()

    e "This time we'll make it a specific chat"
    $ newChat = comment4 #this illustrates how to add a specific chat to the screen.
    #comment4 is not in the comments_list, but it can still be added if we use
    #the addStoryBeat function and set the newChat variable to comment4.
    $ addStoryBeat()

    e "Two more times"
    $ AddToChats()

    $ newChat = comment3 #ensuring that comment3, the only one that is clickable, will appear at least once.
    e "One More Time" 
    $ addStoryBeat() #This fifth test ensures that the earliest item in chats_list will be deleted when the
    #lenght of chats list reaches 5.
    e "Was the top text deleted"

    e "Now we'll test menus."

    #using "onlayer master" and previously defined transforms to position assets in proper locations
    show port at topleft onlayer master with dissolve
    hide desert
    show profile1small at gameleft with dissolve
    show profile2small at gameright with dissolve

    #This menu will appear in position for the micro game set up
    $ narrator = alt_narrator #since the following menu is supposed to be modeled as part of the micro-game, we'll set the narrator to the alternate narrator
    menu:
        "Where does this appear?"
        "Choice 1":
            "This adds one viewer"
            $ viewCount += 1
            "This adds one viewer"
        "Choice 2":
            $ viewCount -= 1            
            "This loses a viewer"

    e "See how the menu appeared in the center of the micro game?"

    e "Now click on the third chat."

    e "Where did the menu appear?"

    "Now we'll test some transitions"

    show desert at topleft onlayer master with dissolve
    hide port

    e "we can change the scene that appears specifically for the microgame"
    show bridge at topleft onlayer master with dissolve
    hide desert #make sure you hide the screen after switching to a different microgame scene so we're not layering one asset over the other.

    "This will switch to the Discord scene"

    #make sure to "hide" specific screens when fully transitioning to new scenes.
    #Unless they have a specified endtime (like clicking a button that triggers the hide function), 
    #screens need to be manually "turned off" in code using the hide function.
    hide screen streamChat
    hide screen streamDetails
    #This discord stuff allows players to move between different chats for the brother and the mod.
    #We might not even need this functionality, but it works so figured I'd leave it in for now.
    $ narrator = reg_narrator
    scene discord1
    show screen discordChat

    "Click on either or both of the top two profile pictures in the top left of the screen."

    "They're both buttons that can shift between different chat windows for the Discord screen."

    "Leaving a bit of room for error here"

    "And a bit more"

    "Really just vamping for some tests"

    return



#Conversations between the borther and the mod that are called through the discord screens.
label brotherChat:
    show screen brotherDiscord
    show screen discordChat
    hide screen modDiscord
    "Hey bro, how's it going?"
    return

label modChat:
    show screen modDiscord
    show screen discordChat
    hide screen brotherDiscord
    "Hey man, how are you doing?"
    return