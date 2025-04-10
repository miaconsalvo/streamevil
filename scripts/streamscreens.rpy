################################################################################
## Stream Details Screens
################################################################################

#This script contains code for screens that interact with the streamer's UI
#Or that affect the stream in some way.

#This establishes a screen in which chats will appear
screen streamChat():
    #python:
    #    yadj.value = yadjValue

    frame:
        #Sets the borders and set up of the chat window
        background Solid("#00000000")
        xpos 1550
        ypos 120
        xsize 355
        ysize 740
        xpadding 10 #These padding variables will affect how close the position of the scrollbar relative to the frame as well
        ypadding 20
        viewport: #id "vp": #creates a viewport so chat can be scrolled through and there won't be overflow
            yadjustment yadj #Using the "yadj" values determined at start of main script, this should set the viewport to adjust to the bottom whenever it's updated. It's only working 70ish% of the time though
            draggable True #allows scrollbar to be dragged
            mousewheel True #allows mousewheel to scroll viewport
            scrollbars "vertical" #sets vertical scroll bar
            yinitial 1.0 #should place scrollbar at bottom of viewport by default - not working though
            vbox:             #Establishes a "vertical box" that displays the objects in chats_list
                #box_reverse True #current way to make us see the newest chat by having it appear at top instead of bottom.
                #yalign 1.0 #This will place these at the bottom
                spacing 9
                for c in (chatter_list): #checks through chatter_list and displays the objects within that list in the vertical boxes.
                    if c.click == True: #if one of the ChatEntry objects in chats_list has "self.click = True," it will create a textbutton.
                        textbutton c.prompt:
                            action Call(c.target, from_current = True)
                            text_color c.colour #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
                            text_hover_color "#ffffffa1" 
                            text_selected_color "#ffffff4f"
                            background "#eeff00cb" #this will highlight textbuttons in yellow. Because of this, I have the text still appearing as white
                            text_size 24
                        #"text_size" can adjust how large the text is. But it would probably be best to define this in the chat_entry class
                        #in Chat_entry, add a "size" property and set it for individual ones. Then here, do "text_size = c.size"
                        #-useful if you want the size to be variable. If constant, may as well just hard code it here instead of in Class.
                    else:
                        text c.prompt color c.colour size 25 #if the ChatEntry object has "self.click = False" it will be plain text
                        #You can change color with c.colour (an attribute that was added to ChatEntry class in Lists script). The Textbutton is a bit more complicated

screen streamerCommentary(): #This screen appears when the player can interact with the stream of their own volition
    textbutton "React":
        action Call(reactTarget, from_current = True)
        text_color "#ffffffff" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
        text_hover_color "#ffffffa1" 
        text_selected_color "#ffffff4f"
        background "#00aeffcb"
        align (0.95, 0.93)
        #vbox:
        #    spacing 10
        #    align (0.5, 0.5)
        #    for c in (streamer_comments):
        #        if c.click == True: #if one of the ChatEntry objects in chats_list has "self.click = True," it will create a textbutton.
        #                textbutton c.prompt:
        #                    action Call(c.target, from_current = True)
        #                    text_color c.colour #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
        #                    text_hover_color "#000000a1" 
        #                    text_selected_color "#0000004f"
        #                    background "#00aeffcb" #this will highlight textbuttons in yellow. Because of this, I have the text still appearing as white
        #                    text_size 30
                        #"text_size" can adjust how large the text is. But it would probably be best to define this in the chat_entry class
                        #in Chat_entry, add a "size" property and set it for individual ones. Then here, do "text_size = c.size"
                        #-useful if you want the size to be variable. If constant, may as well just hard code it here instead of in Class.
        #        else:
        #            text c.prompt color c.colour size 25

#A basic screen to display stream details. All the numbers will likely need to change
screen streamDetails():
    frame:
        background Solid("#00000000")
        xpos 0
        ypos 900
        xsize 1530
        ysize 150
        xpadding 5
        ypadding 5
        text "[streamer]" align (.1, .1) color "#d418acff" #displays the name that players chose for themselves at the beginning of the game.
        text "Viewers [viewCount]" align (.99, .7) color "#000000ff" #displays the current viewer count
        #text "PickledDragons\n{u}Interest:{/u}\n      [pdEngagement]" align (0.25, 0.5) color "#04cdffff"
        #text "KitCat\n{u}Interest:{/u}\n      [kcEngagement]" align (0.45, 0.5) color "#f03535ff"
        #text "Coriolis\n{u}Interest:{/u}\n      [csEngagement]" align (0.6, 0.5) color "#720ee6ff"
        #text "Outlaw Score: [outlaw]" align (0.8, 0.25) color "#e6a20eff"
        #text "Marshal Score: [marshal]" align (0.8, 0.7) color "#27e60eff"
        textbutton pingText:
            action Call("TurnSound", from_current = True)
            text_color "#ffffffb9" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
            text_hover_color "#ffffffd5" 
            text_selected_color "#ffffffff"
            background "#000000ff" #this will highlight textbuttons in yellow. Because of this, I have the text still appearing as white
            text_size 25
            align (1.21, -.3)
            #align (0.06, .95) # - this is an ok alignment to the left and bottom of streamDetails screen
        image "[profilePic]" align (.001, 0) size (100, 100) #displays a profile pic for the streamer

###Tutorial screens for vignette 1
screen chatTutorial():
    frame:
        ypos 40 
        xsize 1000
        ysize 230
        right_margin 200
        background Solid("#000000ff")
        text "Sometimes your chat will make comments you can respond to.\nThese are highlighted in yellow.\nClick on them to interact with your viewers."
        textbutton "Close Tutorial":
            action Hide("chatTutorial")
            text_color "#ffffffb9" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
            text_hover_color "#ffffffd5" 
            text_selected_color "#ffffffff"
            background "#000000ff"
            align (0.5, 1.0)

screen chatTutorial2():
    frame:
        ypos 40 
        xsize 1000
        ysize 230
        right_margin 200
        background Solid("#000000ff")
        text "When the textbox at the bottom of the chat is highlighted in blue and says \"React\",\nyou can click on it to initiate a conversation with your viewers."
        textbutton "Close Tutorial":
            action Hide("chatTutorial2")
            text_color "#ffffffb9" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
            text_hover_color "#ffffffd5" 
            text_selected_color "#ffffffff"
            background "#000000ff"
            align (0.5, 1.0)

screen discordNotification():
    frame:
        ypos 40 
        xsize 1000
        ysize 230
        right_margin 200
        background Solid("#000000ff")
        text "Dude, it's a raid!\n8bitBANDIT just finished their stream of the game and brought a bunch of people in!"
        textbutton "Close Notification":
            action Return() #Hide("discordNotification")
            text_color "#ffffffb9" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
            text_hover_color "#ffffffd5" 
            text_selected_color "#ffffffff"
            background "#000000ff"
            align (0.5, 1.0)

screen streamFreeze():
    frame:
        xsize 1920
        ysize 1080
        background Solid("#00000000")
        textbutton "React":
            action [Return(), Call(reactTarget)]
            align (0.95, 0.93)
            text_color "#ffffffff" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
            text_hover_color "#ffffffa1" 
            text_selected_color "#ffffff4f"
            background "#00aeffcb"

screen raidFreeze():
    frame:
        xsize 1920
        ysize 1080
        background Solid("#00000000")
        imagebutton:
            xsize 298
            ysize 135
            xalign 0.965
            yalign .753
            idle "#eeff0081"
            hover "#eeff0060"
            action [Return(), Call("vig1_sc3_banditConvo")] #could set the Call to like "[curent_analytics_viewcount]" - and then before making the jump, make sure to set $current_analytics_viewcount to the appropriate string


#screen for selecting profile picture
screen selectProfilePic():
    text "Now select your streaming profile picture.":
        align (0.33, 0.843)
    #imagebutton:
    #    action [SetVariable("profilePic", "socials/profilepics/profile1.png"), Return()]
    #    background Image("socials/profilepics/profile1.png")
    #    idle Image("socials/profilepics/profile1.png")
    #    hover Solid("#5e5e5e4b")
    #    xsize 100
    #    ysize 100
    #    align (0.2, 0.5)
    imagebutton:
        action [SetVariable("profilePic", "socials/profilepics/profile2.png"), Return()]
        background Image("socials/profilepics/profile2.png")
        idle Image("socials/profilepics/profile2.png")
        hover Solid("#5e5e5e4b")
        xsize 100
        ysize 100
        align (0.4, 0.5)
    imagebutton:
        action [SetVariable("profilePic", "socials/profilepics/profile5.png"), Return()]
        background Image("socials/profilepics/profile5.png")
        idle Image("socials/profilepics/profile5.png")
        hover Solid("#5e5e5e4b")
        xsize 100
        ysize 100
        align (0.6, 0.5)
    #imagebutton: #turned off for time being so the mod has their own profile pic
    #    action [SetVariable("profilePic", "socials/profilepics/profile4.png"), Return()]
    #    background Image("socials/profilepics/profile4.png")
    #    idle Image("socials/profilepics/profile4.png")
    #    hover Solid("#5e5e5e4b")
    #    xsize 100
    #    ysize 100
    #    align (0.8, 0.5)