# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#narrator definitions
default reg_narrator = Character(None, what_font="Mukta-Regular.ttf", window_style = "window")
default alt_narrator = Character(None, what_font="Lato-Regular.ttf", window_style = "ig_window", what_style = "ig_dialogue", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")

define player = Character("[my_name]", who_font="Mukta-Regular.ttf", what_font="Mukta-Regular.ttf") #represents the protagonist's name which will be defined by the player via an input screen.
define streamer = Character("[username]") #represents protagonist's username on Flinch
define mod = Character("Jessie", what_font="Mukta-Regular.ttf")
define bro = Character("El", what_font="Mukta-Regular.ttf")
define player_nvl = Character("[my_name]", what_font="Mukta-Regular.ttf", kind = nvl, image = "captain_stream")
define streamer_nvl = Character("[username]", what_font="Mukta-Regular.ttf", kind = nvl, image = "captain_stream")
define mod_nvl = Character("Jessie", what_font="Mukta-Regular.ttf", kind = nvl, image = "profile1small")
define bro_nvl = Character("El", what_font="Mukta-Regular.ttf", kind = nvl )
define cs_nvl = Character("Coriolis", what_font="Mukta-Regular.ttf", kind = nvl, )
define kc_nvl = Character("KitCat", what_font="Mukta-Regular.ttf", kind = nvl, )
define pd_nvl = Character("PickledDragons", what_font="Mukta-Regular.ttf", kind = nvl, )
define elliotflashback = Character("Elliot", who_font="Mukta-Regular.ttf", what_font="Mukta-Regular.ttf") 

define adv_menu = menu

#Justin: this is how I define the micro game characters in their stream and non-stream versions
#As you can see the style is different to be more compatible with the asset I made 
define m = Character("Moze", what_font="Play-Regular.ttf", window_style = "window", who_color="#a333ff", what_color="#000000", image = "captain", window_background = "images/textbox/stream textbox Moze.png")
define mS = Character ("Moze", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#a333ff", what_color = "#000000", image = "captain_stream", window_background="images/textbox/stream textbox Moze.png")

define en = Character("Teresa", what_font="Play-Regular.ttf", window_style = "window", who_color="#FF3333", what_color="#000000", image = "engineer", window_background = "images/textbox/stream textbox Teresa.png")
define enS = Character ("Teresa", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color="#FF3333", what_color="#000000", image = "teresa stream neutral", window_background="images/textbox/stream textbox Teresa.png")

define p = Character("Jennica", what_font="Play-Regular.ttf", window_style = "window", who_color="#ef8f3a", what_color="#000000", image = "pilot", window_background = "images/textbox/stream textbox Jennica.png")
define pS = Character ("Jennica", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color="#ef8f3a", what_color="#000000", image = "jennica stream neutral.png", window_background = "images/textbox/stream textbox Jennica.png")

define mac = Character("MAC", what_font="Play-Regular.ttf", window_style = "window", who_color="#33a3ff", what_color="#000000", image = "mac", window_background = "images/textbox/stream textbox MAC.png")
define macS = Character("MAC", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#33a3ff", what_color = "#000000", image = "mac stream", window_background="images/textbox/stream textbox MAC.png")

define a = Character("Allistar", what_font="Play-Regular.ttf", window_style = "window", who_color="#ce1fd4", what_color="#000000", image = "allistar neutral", window_background = "images/textbox/stream textbox npc.png")
define aS = Character("Allistar", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#ce1fd4", what_color = "#000000", image = "allistar stream neutral", window_background="images/textbox/stream textbox npc.png")

define ama = Character("Deadeye", what_font="Play-Regular.ttf", window_style = "window", who_color="#1113a1", what_color="#000000", image = "ama neutral", window_background = "images/textbox/stream textbox npc.png")
define amaS = Character("Deadeye", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#1113a1", what_color = "#000000", image = "ama stream neutral", window_background="images/textbox/stream textbox npc.png")

define enforcer = Character("Enforcer", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "enforcer neutral", window_background="images/textbox/stream textbox npc.png")

define shipcom = Character("Ship Intercom", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define agent1 = Character("Customs Agent", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define smatt = Character("Matticus", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "matticus stream", window_background="images/textbox/stream textbox npc.png")
define goon =  Character("Reginald", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "goon stream", window_background="images/textbox/stream textbox npc.png")
define worker = Character("Technician", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "worker stream", window_background="images/textbox/stream textbox npc.png")
define mattdoorbell = Character("Doorcom", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define hsguard1 = Character("Guard", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")

#General system variables
default viewCount = 4 #viewCount changes how many viewers are displayed in the streamdetails screen
default macroChoice = False  #this variable adjusts where the choice screen will appear. It should be False when decisions happen in microgame. It should be True when decisions happen in macro game.
default commentPing = False
default pingText = "Sound is Off"
default playerNVLNarration = ""
default reactTarget = "vig1_sc1_startStream"
default profilePic = "images/Socials/profilepics/profile2.png"

#variables to track morality
default marshal = 2
default outlaw = 3

#variables to track interest of player - tracked for macro game purposes
default reluctance = 0
default enthusiasm = 0
default energy = 5

#variables to track attributes
default curiosity = False

#variables to track viewer engagement
default csEngagement = 5
default pdEngagement = 3
default kcEngagement = 4

#variables to track MAC's morality
default macCynicism = 0
default macTrust = 0
default macViolence = 0

#Approval of micro-game characters
default engineerApproval = 3
default pilotApproval = 4

#Variables specific to vignette 1
default allistarSuspicious = False
default houseExplosion = False
default omegaDead = False
default misclick = False
default askBandit = False

#Variables to track viewers for Analytics screen in MacroGame
default viewCheck1 = 0
default viewCheck2 = 0
default viewCheck3 = 0
default viewCheck4 = 0
default viewCheck5 = 0
default viewCheck6 = 0
default viewCheck7 = 0
default viewCheck8 = 0
default viewCheck9 = 0
default viewCheck10 = 0
default vbar1 = 0 #make sure to set these vbar values back to zero at the start of every vignette (or just when you leave the analytics screen)
default vbar2 = 0
default vbar3 = 0
default vbar4 = 0
default vbar5 = 0
default vbar6 = 0
default vbar7 = 0
default vbar8 = 0
default vbar9 = 0
default vbar10 = 0
default max_viewers = 40

###Variables for tracking Flinch Analytics
default topfan = ""
default flinchCheck = 0
default viewcountCheck = False
default topfanCheck = False
default alignmentCheck = False
default audienceCheck = False

#blueit variables
default blueitCheck = 0
default blueitImage = ""
default yb = 0 #this sets how long the viewport of the blueit threads will scroll down to
default blueitChoiceCheck = False
default blueitLaunchCheck = False


####Variables for Vignette 2#####
default shnzi = True
default romanceAma = False
default romanceJennica = False
default romanceTeresa = False
default baseGuardKilled = False



#default yadj = ui.adjustment()

#init python: - code to change for adjusting stream chat box lowering
    #yadjValue = float("inf")
    #yadj = ui.adjustment()
    #yadj.value = yadjValue

init: 
    $ stream_left = Position (xpos=0.13, ypos=0.82) #stream view
    $ stream_right = Position (xpos = 0.67, ypos=0.82)
    $ stream_center = Position (xpos=0.40, ypos=0.82)
    $ stream_center_mac = Position (xpos=0.40, ypos=0.70)
    $ stream_left_mac = Position (xpos=0.13, ypos=0.70)
    $ stream_right_mac =  Position (xpos = 0.67, ypos=0.70)
    $ screen_left = Position (xpos = 0.2, ypos = 0.6) #non-stream view
    $ screen_right = Position (xpos = 0.7, ypos = 0.6)
    $ screen_center = Position(xpos = 0.4, ypos = 0.6)
    $ renpy.add_layer("background", below = "master") #created a layer called "background" for displaying micro-game scenes
    #this layer is below the master so we can define the streamview as a "scene", which means that the streamview won't
    #fade out whenever we transition to another label

label start:
    show bg black at topleft onlayer background

    "Hello, this is the start of a new game"

    "Please tell me your streamer username"
    $ username = renpy.input("Your username is: ", length = 16)
    "Now please tell me your first name in real life"
    $ my_name = renpy.input("Your character's real name is: ", length = 16)

    "Here you would select a streaming profile picture"
    #We add chatter here, otherwise you would see them come in like super fast when the game starts
    $ AddChatter(vig1_sc1_comment1)
    $ AddChatter(vig1_sc1_comment2)
    $ AddChatter(vig1_sc1_comment3)
    $ AddChatter(vig1_sc1_comment4)
    $ AddChatter(vig1_sc1_comment5)
    $ AddChatter(vig1_sc1_comment6)
    $ AddChatter(vig1_sc1_comment7)
    $ AddChatter(vig1_sc1_comment8)
    "And now we begin"
    jump vignette1Start

