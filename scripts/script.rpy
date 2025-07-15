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
define bro = Character("Elliot", who_font="Mukta-Regular.ttf", what_font="Mukta-Regular.ttf")
define player_nvl = Character("[my_name]", what_font="Mukta-Regular.ttf", kind = nvl, image = "images/socials/profilepics/profile2.png")
define streamer_nvl = Character("[username]", what_font="Mukta-Regular.ttf", kind = nvl, image = "images/socials/profilepics/profile2.png")
define mod_nvl = Character("Jessie", what_font="Mukta-Regular.ttf", kind = nvl, image = "images/socials/profilepics/profile1.png")
define bro_nvl = Character("El", what_font="Mukta-Regular.ttf", kind = nvl )
define cs_nvl = Character("Coriolis", what_font="Mukta-Regular.ttf", kind = nvl, )
define kc_nvl = Character("kitcat", what_font="Mukta-Regular.ttf", kind = nvl, )
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

define mac = Character("MAC", what_font="Play-Regular.ttf", window_style = "window", who_color="#a622c7e1", what_color="#000000", image = "mac", window_background = "images/textbox/stream textbox MAC.png")
define macS = Character("MAC", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#a622c7e1", what_color = "#000000", image = "mac stream", window_background="images/textbox/stream textbox MAC.png")

define a = Character("Allistar", what_font="Play-Regular.ttf", window_style = "window", who_color="#ce1fd4", what_color="#000000", image = "allistar neutral", window_background = "images/textbox/stream textbox npc.png")
define aS = Character("Allistar", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#ce1fd4", what_color = "#000000", image = "allistar stream neutral", window_background="images/textbox/stream textbox npc.png")

define ama = Character("Deadeye", what_font="Play-Regular.ttf", window_style = "window", who_color="#1113a1", what_color="#000000", image = "ama neutral", window_background = "images/textbox/stream textbox npc.png")
define amaS = Character("Deadeye", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#1113a1", what_color = "#000000", image = "ama stream neutral", window_background="images/textbox/stream textbox npc.png")

define enforcer = Character("Enforcer", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "enforcer neutral", window_background="images/textbox/stream textbox npc.png")

define unknown = Character("Unknown", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "enforcer neutral", window_background="images/textbox/stream textbox npc.png")

define jenter = Character ("Jennica & Teresa", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#a333ff", what_color = "#000000", image = "captain_stream", window_background="images/textbox/stream textbox Moze.png")


#vig2 characters
define shipcom = Character("Ship Intercom", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define agent1 = Character("Customs Agent", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define smatt = Character("Matticus", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "matticus stream", window_background="images/textbox/stream textbox npc.png")
define goon =  Character("Reginald", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "goon stream", window_background="images/textbox/stream textbox npc.png")
define worker = Character("Technician", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "worker stream", window_background="images/textbox/stream textbox npc.png")
define mattdoorbell = Character("Doorcom", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define hsguard1 = Character("Guard", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")

#vig3 characters
define houndleaderunknown = Character("Gangster", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "hound leader stream", window_background="images/textbox/stream textbox npc.png")
define houndleader = Character("Hound Leader", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "hound leader stream", window_background="images/textbox/stream textbox npc.png")
define houndgoon = Character("Hound Gangster", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "hound goon stream", window_background="images/textbox/stream textbox npc.png")
define recS = Character("Reccrin", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#ce1fd4", what_color = "#000000", image = "reccrin stream neutral", window_background="images/textbox/stream textbox npc.png")
define showgirl = Character("Daisy", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "showgirl stream", window_background="images/textbox/stream textbox npc.png")
define dflycontact = Character("Dragonfly", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "dragonfly contact stream", window_background="images/textbox/stream textbox npc.png")
define strngr1 = Character("Stranger", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "stranger 1 stream", window_background="images/textbox/stream textbox npc.png")
define zan = Character("Zan", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "zan stream", window_background="images/textbox/stream textbox npc.png")
define ovid = Character("Ovid", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "ovid stream", window_background="images/textbox/stream textbox npc.png") 
define wifenpc = Character("Young Woman", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define husbnpc = Character("Young Man", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define vyattend = Character("Ryo", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", image = "vyattend stream", window_background="images/textbox/stream textbox npc.png")
define invfairnpc1 = Character("Inventor's Fair Guest", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define invfairnpc2 = Character("Mills", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define invfairannounce = Character("Announcer", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define bcrep = Character("Big Corp Representative", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define reynar = Character("Reynar", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")

#vig4 Characters
define cS = Character ("Coil", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#b60873", what_color = "#000000", image = "images/characters/Vignette 4/coil.png", window_background="images/textbox/stream textbox npc.png")
define vS = Character ("Vega", what_font="Play-Regular.ttf", window_style = "ig_character", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#dd6819", what_color = "#000000", image = "images/characters/Vignette 4/vega.png", window_background="images/textbox/stream textbox npc.png")
define townguy = Character("Townsperson", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define diceP1 = Character("Dice Player 1", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define diceP2 = Character("Dice Player 2", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")
define dflyGuard = Character("Dragonfly Guard", what_font="Play-Regular.ttf", window_style = "ig_window", what_style = "ig_dial", namebox_xpos = 250, namebox_ypos = 50, who_color = "#000000", what_color = "#000000", window_background="images/textbox/stream textbox npc.png")

#General system variables
default viewCount = 4 #viewCount changes how many viewers are displayed in the streamdetails screen
default macroChoice = False  #this variable adjusts where the choice screen will appear. It should be False when decisions happen in microgame. It should be True when decisions happen in macro game.
default commentPing = True
default pingText = "Sound is Off"
default pingImage = "stream ui/soundon.png"
default playerNVLNarration = ""
default reactTarget = "vig1_sc1_startStream"
default profilePic = "images/socials/profilepics/profile2.png"
default reactImage = "stream ui/reactneutral.png"

#variables to track morality
default marshal = 4
default outlaw = 3

#variables to track MAC's morality
default macHope = 0
default macPessimism = 0
default macViolence = 0
default macPeace = 0
default macHonesty = 0

#Approval of micro-game characters
default engineerApproval = 3
default pilotApproval = 4
default deadeyeApproval = 0

#variables to track viewer engagement
default csEngagement = 5
default pdEngagement = 3
default kcEngagement = 4

#variable to check status of viewer
default viewershipHigh = False
default viewershipMed = False
default viewershipLow = False

#variables to track interest of player - tracked for macro game purposes
default reluctance = 0
default enthusiasm = 0
default energy = 5

#Flags to track what vignette we're on
default vignette1 = False
default vignette2 = False
default vignette3 = False
default vignette4 = False

#variables to track attributes
default curiosity = False
default vibes = False
default humour = False
default story = False

###Variables for Vignette 1###
default allistarSuspicious = False
default houseExplosion = False
default killAllistar = False #if you tried to kill allistar = true
default omegaDead = False
default misclick = False
default askBandit = False

####Variables for Vignette 2#####
default customsStampede = False
default shnzi = True
default romanceAma = False
default romanceJennica = False
default romanceTeresa = False
default baseGuardKilled = False #if you killed the guard at the commsbase  = true (outlaw route)
default gunsBlazing = False
default technicianChoice = False #if you spared the technician = false (outlaw route)
default reginaldChoice = False #if you stunned reginald = true (marshal route)
default customsSpeculation = False
default vig2_marshalEpilogue = False
default vig2_outlawEpilogue = False
default promisedPDOutlaw = False #if you told pickleddragons that you want to do outlaw = true

####Variables for Vignette 3####
default firstfightprediction = False
default shipbetprediction = False
default vig3_brika = 0

###Variables for Vignette 4###
default stunGuy = False
default polarisQuestion = False
default vegacoilQuestion = False
default vig4_checkSights = False
default vig4_checkTrigger = False
default vig4_vegaVictory = False
default jennicaRomance = False
default teresaRomance = False
default rudeMACGoodbye = False
default vig4_amaOffer = False
default vig4_defendPolaris = False
default vig4_attackPolaris = False
default vig4_killDflies = False
default amaRomance = False
default jennicaDate = False
default teresaDate = False
default vegaDate = False
default vig4_amaCrew = False

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

###Variables to make free navigation of pos-stream scenes possible:
default flinchView = False #When set to "True," this will turn off the button to open the Flinch page
default blueitView = False #When set to "True," this will turn off the button to open the Blueit page
default loopdView = False #You're never gonna gues what this does
default screenComplete = False #Another gate to regulate when the webNavigation screen will display

###Variables for tracking Flinch Analytics Vignette 1
default topfan = ""
default followerGoal = "8"
default flinchCheck = 0
default viewcountCheck = False
default topfanCheck = False
default alignmentCheck = False
default audienceCheck = False

###Variabels for tracking Flinch Analytics Vignette 2
default viewcountCheck_vig2 = False
default topfanCheck_vig2 = False
default audienceCheck_vig2 = False
default viewershipThoughtCheck = False
default flinchViewershipShnzi = False
default flinchViewershipOutlaw = False
default flinchViewershipMarshal = False
default flinchViewershipAssault = False

#blueit variables
default blueitCheck = 0
default blueitImage = ""
default yb = 0 #this sets how long the viewport of the blueit threads will scroll down to
default blueitChoiceCheck = False
default blueitLaunchCheck = False


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
    $ stream_grab_mac = Position (xpos =0.50, ypos=0.70)
    $ screen_left = Position (xpos = 0.2, ypos = 0.6) #non-stream view
    $ screen_right = Position (xpos = 0.7, ypos = 0.6)
    $ screen_center = Position(xpos = 0.4, ypos = 0.6)
    $ stream_left5 = Position (xpos=0.3, ypos=0.82) #for five models on screen
    $ stream_right5 = Position (xpos=0.5, ypos=0.82)
    $ stream_left5mac = Position (xpos=0.27, ypos=0.70)
    $ stream_right5mac = Position (xpos=0.54, ypos=0.70)
    $ renpy.music.register_channel("backAudio")
    $ renpy.add_layer("background", below = "master") #created a layer called "background" for displaying micro-game scenes
    #this layer is below the master so we can define the streamview as a "scene", which means that the streamview won't
    #fade out whenever we transition to another label

label start:
    $ quick_menu = False #- for when we don't want players to be able to go "back" in the game
    $ macroChoice = True
    $ chatter_list = [vig1_sc1_comment1, vig1_sc1_comment2, vig1_sc1_comment3, vig1_sc1_comment4, vig1_sc1_comment5, vig1_sc1_comment6, vig1_sc1_comment7, vig1_sc1_comment8]

    show bg black at topleft onlayer background

    "Hello, welcome to Stream Evil!"
    "Please note: we ask that you do not redistribute or replicate any portion of this game."
    "The copy you have downloaded is for testing purposes only."
    "By clicking \"Continue\" to play the game you acknowledge this fact. Thank you."
    menu:
        "By clicking \"Continue\" to play the game you acknowledge this fact. Thank you."
        "Continue":
            pass
    "This is the start of a new game."
    jump userName

label userName:
    "Please tell me your streamer username."
    $ username = renpy.input("Your username is: ", length = 16)
    "Your streamer username will be {b}\"[username]\"{/b}. Is this correct?"
    menu:
        "Your streamer username will be {b}\"[username]\"{/b}. Is this correct?"
        "Yes":
            jump playerName
        "No":
            jump userName

label playerName:
    "Now please tell me your character's first name in real life."
    $ my_name = renpy.input("Your character's real name is: ", length = 16)
    "Your name in real life will be {b}\"[my_name]\"{/b}. Is this correct?"
    menu:
        "Your name in real life will be {b}\"[my_name]\"{/b}. Is this correct?"
        "Yes":
            pass
        "No":
            jump playerName

    "Now select your streaming profile picture."
    call screen selectProfilePic
    #We add chatter here, otherwise you would see them come in like super fast when the game starts
    #$ AddChatter(vig1_sc1_comment1)
    #$ AddChatter(vig1_sc1_comment2)
    #$ AddChatter(vig1_sc1_comment3)
    #$ AddChatter(vig1_sc1_comment4)
    #$ AddChatter(vig1_sc1_comment5)
    #$ AddChatter(vig1_sc1_comment6)
    #$ AddChatter(vig1_sc1_comment7)
    #$ AddChatter(vig1_sc1_comment8)
    "And now we begin."
    
    "For testing purposes, you can jump ahead to other vignettes."
    menu:
        "Which Vignette would you like to begin with?"
        "Vignette 1":
            jump vignette1Start
        "Vignette 2":
            jump testing_jumpahead_vig2
        "Vignette 3":
            jump testing_jumpahead_vig3
        "Vignette 4":
            jump vignette4Start
    
label testing_jumpahead_vig2():
    "Choose the decisions you want to have made in Vignette 1"
    menu:
        "How did you describe your stream during the raid?"
        "Vibes focused":
            $ vibes = True
        "Humour focused":
            $ humour = True
        "Story focused":
            $ story = True
    "Next, what did you pick when given the choice to stun or kill Allistar?"
    menu:
        "Allistar choice?"
        "Stunned Allistar":
            $ killAllistar = False
        "Killed Allistar":
            $ killAllistar = True
    "Lastly, when you shot Allistar, did you say it was a misclick?"
    menu:
        "Did you say killing Allistar was a misclick?"
        "Yes":
            $ misclick = True
        "No":
            $ misclick = False
    "Excellent. You will now begin Vignette 2."
    jump vignette2Start

label testing_jumpahead_vig3():
    "First, you must choose the decisions you want to have made in Vignette 1"
    menu:
        "How did you describe your stream during the raid?"
        "All about Vibes":
            $ vibes = True
        "Humour focused":
            $ humour = True
        "Story focused":
            $ story = True
    "Next, what did you pick when given the choice to stun or kill Allistar?"
    menu:
        "Allistar choice?"
        "Stunned Allistar":
            $ killAllistar = False
        "Killed Allistar":
            $ killAllistar = True
    "Lastly, when you shot Allistar, did you say it was a misclick?"
    menu:
        "Did you say killing Allistar was a misclick?"
        "Yes":
            $ misclick = True
        "No":
            $ misclick = False
    "Now you will decide what choices you made in Vignette 2."
    menu:
        "How did you get through the customs depot?"
        "Bribed an agent.":
            $ customsStampede = False
        "Caused a stampede.":
            $ customsStampede = True
    "Next, how did you get into the communications base?"
    menu:
        "How did you get into the commsbase?"
        "Stealthily, sneaking in":
            $ gunsBlazing = False
        "Guns blazing":
            $ gunsBlazing = True
            "Did you kill the guard who wanted to surrender?"
            menu:
                "Did you kill the surrendering guard?"
                "Yes":
                    $ baseGuardKilled = True
                "No":
                    $ baseGuardKilled = False
    "Lastly, did you choose to follow through with Matticus's plan and blow up the aid ship?"
    menu:
        "Did you blow up the aid ship?"
        "No":
            $ vig2_marshalEpilogue = True
            "How did you deal with Reginald?"
            menu:
                "What did you do with Reginald?"
                "Stunned him":
                    $ reginaldChoice = True
                "Bribed him":
                    $ reginaldChoice = False
        "Yes":
            $ vig2_outlawEpilogue = True
            "How did you deal with the technician?"
            menu:
                "What did you do with the technician?"
                "Threatened him":
                    $ technicianChoice = False
                "Killed him":
                    $ technicianChoice = True
    "Excellent. You will now jump to the start of Vignette 3."
    jump vignette3Start








    #jump vignette1Start

