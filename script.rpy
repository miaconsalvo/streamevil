# Declare characters used by this game. The color argument colorizes the
# name of the character.

#narrator definitions
default reg_narrator = Character(None, window_style = "window")
default alt_narrator = Character(None, window_style = "ig_window", what_style = "ig_dialogue", what_color = "#000000", window_background="images/textbox/ig_textbox_blue.png")
define player = Character("[my_name]") #represents the protagonist's name which will be defined by the player via an input screen.

#Justin: this is how I define the micro game characters in their stream and non-stream versions
#As you can see the style is different to be more compatible with the asset I made 
define m = Character("Moze", window_style = "window", who_color="#a333ff", what_color="#000000", image = "captain", window_background = "images/textbox/textbox_purple.png")
define mS = Character ("Moze", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#a333ff", what_color = "#000000", image = "captain_stream", window_background="images/textbox/ig_textbox_purple.png")

define en = Character("Teresa", window_style = "window", who_color="#FF3333", what_color="#000000", image = "engineer", window_background = "images/textbox/textbox_red.png")
define enS = Character ("Teresa", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color="#FF3333", what_color="#000000", image = "engineer_stream", window_background="images/textbox/ig_textbox_red.png")

define p = Character("Jennica", window_style = "window", who_color="#ef8f3a", what_color="#000000", image = "pilot", window_background = "images/textbox/textbox_orange.png")
define pS = Character ("Jennica", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color="#ef8f3a", what_color="#000000", image = "pilot_stream.png", window_background = "images/textbox/ig_textbox_orange.png")

define mac = Character("MAC", window_style = "window", who_color="#33a3ff", what_color="#000000", image = "mac", window_background = "images/textbox/textbox_blue.png")
define macS = Character("MAC", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#a333ff", what_color = "#000000", image = "captain_stream", window_background="images/textbox/ig_textbox_blue.png")

#Additional variables
default viewCount = 4 #viewCount changes how many viewers are displayed in the streamdetails screen
default macroChoice = False  #this variable adjusts where the choice screen will appear. It should be False when decisions happen in microgame. It should be True when decisions happen in macro game.
default macroNarration = True #this variable helps determine if a macro game choice should return us to narration style that is micro game or macro game

#variables to track morality
default marshal = 2
default outlaw = 5

#variables to track interest of player
default reluctance = 0
default enthusiasm = 0

#variables to track attributes
default curiosity = False

#variables to track viewer engagement
default csEngagement = 5
default pdEngagement = 3
default kkEngagement = 4

#Approval of micro-game characters
default teresaApproval = 3
default jennicaApproval = 4

# Before the game starts, we define these are the positions for micro game characters to appear in the micro and macro game
init: 
    $ stream_left = Position (xpos=0.13, ypos=0.6) #stream view
    $ stream_right = Position (xpos = 0.67, ypos=0.6)
    $ screen_left = Position (xpos = 0.2, ypos = 0.7) #non-stream view
    $ screen_right = Position (xpos = 0.8, ypos = 0.7)

label start:
    $ narrator = reg_narrator #setting narrator so the text will appear in the middle of the screen

    "Hello! This is the start of the game!"
    "So you should make a new name!"
    $ my_name = renpy.input("Your name is: ", length = 16) #invokes an input screen that allows player to define their own name. Length determines how long the name can be.

    "Your name is now [player]" #the player's name can now be interpellated using this method

    "This is a prototype to test the integration of stream comments with the in-game script."
    "Comments in the chat that are highlighted in yellow can be clicked on to interact with."
    "We will start now."
    jump gameStart

label gameStart():
    #Since our full game screen will be composed of multiple discrete screens, we need to specify which screen layers
    #the backgrounds are appearing on. "onlayer master" ensures that they will still appear behind character portraits
    #and behind textboxes.
    #Justin here! 
    #For the micro game backgrounds use the usualy "scene" command 
    #For the stream overlay use "show streamview at center onlayer master", so it appears above the scene but below the character profiles
    #See line 96 
    show streamview at center onlayer master
    show screen streamDetails
    show screen streamChat
    $ comments_list.append(comment1)
    $ comments_list.append(comment2)
    $ comments_list.append(comment4)
    pause 1.0
    $ AddToChatter()
    pause 1.0
    $ chatter_list.append(comment3)

    "You begin the stream and see some of your viewers commenting in the chat."
    "You take a second to check in with the viewers."
    "And then boot up the game."
    scene bridge_stream with dissolve
    show streamview at center onlayer master
    "You load the save file you were previously playing, and are ready to go."
    
    $ macroNarration = False
    $ narrator = alt_narrator
    show pilot_stream at stream_left with dissolve
    show engineer_stream at stream_right with dissolve
    "Moze wakes up to find Jennica (the Pilot) and Teresa (the Engineer) arguing about contacting corrupt cop Savlian Matticus."
    pS "Jennica states that he can't be trusted but Teresa counters that they don't have any other options."

    "What do you do?"
    menu: #decision1
        "What do you do?"
        "Side with Jennica":
            $ jennicaApproval += 1
            $ chatter_list.append(commentPilotCS)
            "Although you have to acknowledge that you need Savlian's help, you do it in a way where Jennica still feels heard."
        "Side with Teresa":
            $ teresaApproval += 1
            $ chatter_list.append(commentEngineerPD)
            "Teresa appreciates your understanding that you need Savlian's help. Jennica looks somewhat hurt."
        "Do Nothing":
            $ chatter_list.append(commentNothingKK)
            "The Pilot and Engineer continue to fight. Somehow it seems like MAC is uncomfortable."
    $ chatter_list.append(kkAsksRomance)
    pause 1.0
    jump CustomsDepot

label CustomsDepot:
    scene port at topleft with dissolve
    show streamview at center onlayer master
    mS "The crew of the Oakley land on Gibian V and enter the Customs depot with MAC hidden in a secure crate."
    pause 0.7
    $ chatter_list.append(kkMac)
    show engineer_stream at stream_left with dissolve
    enS "Teresa notices a BigCorp inspector nearby and suggests preparing a distraction."
    pause 0.5
    $ chatter_list.append(pdLovesChaos)
    pause 1.0
    show pilot_stream at stream_right with dissolve
    pS "Jennica is concerned that will draw too much attention and suggests bribing an official instead."
    "What do you do?"
    menu: #decision2
        "What do you do?"
        "Have Teresa prep the distraction":
            "Teresa prepares a smoke bomb and tosses it in to the crowd."
            $ outlaw += 1
            $ pdEngagement += 1
            $ kkEngagement += 1
            $ chatter_list.append(pdOutlawD2)
            pause 1.0
            "Someone in the crowd starts to yell \"FIRE\" and everyone starts stampeding toward the gates."
            "The smoke bomb lights up, engulfing the Big Corp employee in smoke."
            "You use the crowd's momentum to dive past the gates."
            pause 0.5
            $ chatter_list.append(csOutlawD2)
        "Follow Jennica and bribe a guard":
            "You move to the edge of the crowd and find a BC employee you can successfully bribe."
            $ marshal += 1
            $ pdEngagement -= 1
            $ csEngagement += 1
            $ kkEngagement -= 1
            $ chatter_list.append(kkMarshalD2)
            pause 1.0
            $ chatter_list.append(csMarshalD2)
            pause 1.0
            "The crew slips through the barriers undetected."
    "Your viewers talk about the situation that just happened and you take a second to catch your breath."
    
    mS "Then you and the Oakley crew navigate to Savlian Matticus's hideout."

    scene streamview
    show hideout at topleft with dissolve

    show pilot_stream at stream_left with dissolve
    show engineer_stream at stream_right with dissolve
    $ narrator = reg_narrator
    $ macroNarration = True
    "Now the game will end"
    "But I put some buffer lines here in case we want to do some extra testing"
    "buffer"
    "bufferbufferbuffer"
    "BUFFER"
    "Click one more time to close the game"
    return




label justinTests():
    $ narrator = alt_narrator

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
