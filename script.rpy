# Declare characters used by this game. The color argument colorizes the
# name of the character.
#Defining character's name as None sets them as a potential narrator.
#set each characters window_style equal to the window style you want them to use.
#namebox_xpos adjusts the character's position within the textbox so that they don't look out of place.
#can use "namebox_[insert parameter here]" to adjust other qualities of the namebox for specific characters
define e = Character("Eileen", window_style = "ig_window", what_style = "ig_dialogue", namebox_xpos = 450)

#Justin this is how I define the micro game characters in their stream and non-stream versions
#As you can see the style is different to be more compatible with the asset I made 
define en = Character("Engineer", window_style = "window", who_color="#FF3333", what_color="#000000", image = "engineer", window_background = "images/textbox/textbox_red.png")
define enS = Character ("Engineer", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color="#FF3333", what_color="#000000", image = "engineer_stream", window_background="images/textbox/ig_textbox_red.png")

define p = Character("Pilot", window_style = "window", who_color="#ef8f3a", what_color="#000000", image = "pilot", window_background = "images/textbox/textbox_orange.png")
define pS = Character ("Pilot", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color="#ef8f3a", what_color="#000000", image = "pilot_stream.png", window_background = "images/textbox/ig_textbox_orange.png")
3
default alt_narrator = Character(None, window_style = "ig_window", what_style = "ig_dialogue")
default reg_narrator = Character(None, window_style = "window")
define pName = Character("[my_name]") #represents the protagonist's name which will be defined by the player via an input screen.
default newChat = default #an empty variable that can be set to any ChatEntry object so we can add story specific comments to the chat screen.
default viewCount = 4 #viewCount changes how many viewers are displayed in the streamdetails screen
default macroChoice = False #this variable adjusts where the choice screen will appear. It should be False when decisions happen in microgame. It should be True when decisions happen in macro game.
#Full disclosure, keeping track of the variable macroChoice is probably going to be a bit of a pain. 
#It's doable, but just a bit unintuitive. Open to alternatives.

# The game starts here. (not yet)
# Before that, these are the positions for micro game characters to appear in the micro and macro game
init: 
    $ stream_left = Position (xpos=0.13, ypos=0.6) #stream view
    $ stream_right = Position (xpos = 0.67, ypos=0.6)
    $ screen_left = Position (xpos = 0.2, ypos = 0.7) #non-stream view
    $ screen_right = Position (xpos = 0.8, ypos = 0.7)

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
    
    #Since our full game screen will be composed of multiple discrete screens, we need to specify which screen layers
    #the backgrounds are appearing on. "onlayer master" ensures that they will still appear behind character portraits
    #and behind textboxes.
    
    #Justin here! 
    #For the micro game backgrounds use the usualy "scene" command 
    #For the stream overlay use "show streamview at center onlayer master", so it appears above the scene but below the character profiles
    #See line 89
    
    "Hello! This is the start of the game!"

    "So you should make a new name!"
    $ my_name = renpy.input("Your name is: ") #invokes an input screen that allows player to define their own name

    "Your name is now [pName]" #the player's name can now be interpellated using this method
    "Now let's turn the lights on" 

    scene bridge

    #The next six lines test that character window styles are working appropriately
    #Eileen's should appear in the same location every time.
    #The narrator location should change each time the narrator is altered.
    "You've created a new Ren'Py game."
    "Now we'll show the characters in a non-stream view"

    show pilot at screen_left
    e "You've created a new Ren'Py game."

    show engineer at screen_right
    en "Well done Captain!"

    p "That's not the Captain..."

    en "Might as well be"

    hide pilot
    hide engineer

    $ narrator = reg_narrator
    "The narrator has changed the narrator and should appear in a different spot!"
    "Now let's get you set up"

    scene bridge_stream
    show streamview at center onlayer master

    e "This is checking that the character Eileen will continue appear in a consistent space even when Narrator changes"

    $ narrator = alt_narrator #sets narrator to where dialogue will appear during micro game situations
    "This is the last check"

    e "This is the last check"

    $ narrator = reg_narrator #sets narrator to where dialogue will appear during macro game situations
 
    "Now we'll test the stream set up"

     $ narrator = alt_narrator

    "Just to make sure we can play the game!"
    "Let's bring in the characters again!"

    show pilot_stream at stream_left 
    pS "We're back baby!"

    show engineer_stream at stream_right
    enS "Back and better than ever!"

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

    scene desert
    hide bridge
    show streamview at center onlayer master

    e "we can change the scene that appears specifically for the microgame"
    scene hallway at topleft onlayer master 
    show streamview at center onlayer master
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
    scene discordview
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
