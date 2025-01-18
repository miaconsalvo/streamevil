#Discord NVL Mode Script
#This script will contain the code to make the NVL script for discord work

define nvl_mode = "discord"

screen DiscordDialogue(dialogue, items=None):

    style_prefix "discordFrame"
    frame:
        xfill True
        yfill True
        background Solid("#00000000") #"gui/nvl.png"
        xsize 1368
        ysize 800
        xpos 310
        ypos 100
        padding gui.nvl_borders.padding
    #    background Solid("#000000ff")
    #    xpos 830
    #    ypos 100
    #    xsize 1000
    #    ysize 800
        #if len(dialogue) == 1:
        #    at phone_appear(phone_position_x, phone_position_y)
        viewport:
            #draggable True
            mousewheel True
            scrollbars "vertical"
            # cols 1
            yinitial 1.0
            # scrollbars "vertical"
            vbox:
                null height 20
                #use nvl_dialogue(dialogue)
                use nvl_phonetext(dialogue)
                null height 0 #space between bottom of nvl dialogue screen and most recent dialogue line
            ## Displays the menu, if given. The menu may be displayed incorrectly if
            ## config.narrator_menu is set to True.
    ###Below this is for the menu
    #It's currently displaying at all times - how to get it to display only during a menu??
    if len(items) == 0:
        frame:
            background Solid("#00000000")
            xsize 1200
            ysize 150
            xpos 400
            ypos 900
            xpadding 10
            ypadding 20

    else:   
        frame:
            background Solid("#00000000")
            xsize 1200
            ysize 150
            xpos 400
            ypos 900
            xpadding 10
            ypadding 20
            viewport:
                mousewheel True
                scrollbars "vertical"
                vbox: #You could switch this to a grid. Leaving it as vbox for now.
                    #xalign 0.0
                    #yalign 1.0
                    #xpos 200
                    #ypos 850
                    #spacing 5
                    #yspacing 5
                    for i in items:
                            textbutton i.caption:
                                #xpos 400
                                #ypos 850
                                xalign 0.0
                                #ypos 10
                                ypadding 5
                                text_size 22
                                text_color "#ffffff"
                                text_hover_color "#bbbbbba1" 
                                text_selected_color "#ffffff4f"
                                background "#00000059"
                                action i.action
                                style "nvl_button"

screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        #This is for narration taking place in NVL so we are not using it
        if d.who == None: # Narrator
            text d.what:
                    xpos -335
                    ypos 0.0
                    xsize 350
                    text_align 0.5
                    italic True
                    size 28
                    slow_cps False
                    id d.what_id
                    if d.current:
                        at message_narrator
        else:
            #These lines establish frames that look different for senders/receivers
            #It's from the phone script, trying to replicate how received messages have different color frames
            #Not necessary for discord, but currently kept just in case we want to use
            if d.who == my_name:
                $ message_frame = "#1b56adab"
            else:
                $ message_frame = "#8b1e1e9a"

            hbox:
                xalign 0.5 #Shifts the hbox to the right for the display of discord
                spacing 20 #Establishes spacing between the two elements - an image and the namebox of the "speaker"
                #For some reason, taking out these bottom two lines equalizes the spacing.
                #When they were in place, the player's chats would appear more to the right of the other person.
                #if d.who == my_name:
                #    null width 50
                    #box_reverse True
                
                #If this is the first message of the character, show an icon
                if previous_d_who != d.who:
                    #We'll want to specify if "d.who == Jessie" so we can assign specific images for each profile
                    if d.who == my_name:
                        $ message_icon = "playerprofile"
                    elif d.who == "Jessie":
                        $ message_icon = "modprofile"
                    elif d.who == "El":
                        $ message_icon = "defaultprofile"
                    else:
                        $ message_icon = "defaultprofile"
                    #The line below this will add the message icon to the hbox. The lines below it add a transition animation that we aren't going to use
                    add message_icon#:
                        #if d.current:
                        #    at message_appear_icon()
                        
                else:
                    null width 100

                vbox:
                    yalign 1.0
                    #ypos 500
                    #This line produces the namebox above the NVL dialogue for people not the protagonist
                    if d.who != my_name and previous_d_who != d.who:
                        #spacing 30 -- Spacing does have an effect, but it puts space below the namebox, not above it
                        text d.who:
                            bold True
                            underline True #This and the previous line modify the namebox
                            size 40 #changes size of namebox
                    #This line produces the namebox above the NVL dialogue for the protagonist
                    if d.who == my_name and previous_d_who != d.who:
                        text d.who:
                            bold True
                            underline True #This and the previous line modify the namebox
                            size 40 #changes size of namebox

                    frame:
                        padding (5,5)#(20,20) #This sets up the spacing between each dialogue line
                        

                        background Frame(message_frame, 23,23,23,23) #Unsure what this frame does
                        xsize 1200 #350 #Establishes the size (width) of the dialogue lines
                        #Lines below this establish a transition animation that will likely be be taken out.
                        #if d.current:
                        #    if d.who == my_name:
                        #        at message_appear(-1)
                        #    else:
                        #        at message_appear(-1)

                        text d.what:
                            size 30 #changes size of text in NVL dialogue
                            pos (0,0)
                            xsize 1200 #This establishes the length of the actual dialogue. 
                            #If this is shorter than the "xsize" above, you'll see the text use margins that aren't the same size as the frame displays
                            slow_cps False
                            

                            if d.who == my_name :
                                color "#FFF"
                                #The two removed lines below this would put the protagonist's dialogue on the far right of the screen, like in a phone UI
                                #text_align 1.0
                                #xpos -580
                            else:
                                color "#FFF"

                                
                            id d.what_id
        $ previous_d_who = d.who #This line of code sets the current speaker to be the previous speaker for reference at the top of the script

style discordFrame is default

style discordFrame_frame:
    background Transform(xcenter=0.5,yalign=0.5)
    foreground Transform(xcenter=0.5,yalign=0.5)
    
    ysize 815
    xsize 495

style discordFrame_viewport:
    yfill True
    xfill True

    yoffset -20

style discordFrame_vbox:
    spacing 10
    xfill True

transform message_appear_icon():
    #zoom 0.5
    #easein_back 0.5 zoom 0.5
    #xalign 0.0
    #yalign 1.0
    xpos 50
    ypos 50

transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0
