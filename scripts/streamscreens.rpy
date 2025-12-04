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
            if screenFreeze == False:
                draggable True #allows scrollbar to be dragged
                mousewheel True #allows mousewheel to scroll viewport
            else: #My idea to fix the issue with the highlight not moving with BANDI or Elliot's comments is to disable to ability to scroll the chat in those moments. This doesn't work unfortunately.
                draggable False
                mousewheel False
            scrollbars "vertical" #sets vertical scroll bar
            yinitial 1.0 #should place scrollbar at bottom of viewport by default - not working though
            vbox:             #Establishes a "vertical box" that displays the objects in chats_list
                #box_reverse True #current way to make us see the newest chat by having it appear at top instead of bottom.
                #yalign 1.0 #This will place these at the bottom
                spacing 9
                for c in (chatter_list): #checks through chatter_list and displays the objects within that list in the vertical boxes.
                    if c.click == True and c.tag == 5: #if one of the ChatEntry objects in chats_list has "self.click = True," it will create a textbutton.
                        textbutton c.prompt:
                            action [Return(), Call(c.target)]
                            text_color c.colour #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
                            text_hover_color "#ffffffa1" 
                            text_selected_color "#ffffff4f"
                            background "#eeff00cb" #this will highlight textbuttons in yellow. Because of this, I have the text still appearing as white
                            text_size 24
                    elif c.click == True: #if one of the ChatEntry objects in chats_list has "self.click = True," it will create a textbutton.
                        textbutton c.prompt:
                            action [Return(), Call(c.target, from_current = True)]
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
    frame:
        xsize 1920
        ysize 1080
        background Solid("#00000000")
        imagebutton: #just the overlay that you click on
            action [Return(), Call(reactTarget, from_current = True)]
            idle Solid("#00000000")
            hover Solid("#bd050556")
            #hover Image("stream ui/reactHighlight.png") 
            #hover Solid("#dad60563") "#bd0505",
            #hover Solid("#44444463")
            xsize 192
            ysize 120
            align (0.001, 0.113)
        image ["stream ui/reactHighlight.png"] align (0.001, 0.113) xsize 192 ysize 120
        image ["stream ui/reactalert.png"] align (0.095, 0.1) size (30, 30) #the red exclaim image itself

###I commented out the imagebutton below this because I created an outline for the react image instead of a filled in shape
#    imagebutton: #just the overlay that you click on
#        action Call(reactTarget, from_current = True)
#        idle Solid("#00000000")
#        hover Solid("#dad60563")
#        xsize 192
#        ysize 120
#        align (0.005, 0.12)
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
        xsize 1920
        ysize 1080
        text "[streamer]" align (.07, 0.89) color "#d418acff"
        text "Viewers: [viewCount]" align (0.94, 0.05) color "#ffffffff"
        imagebutton:
            action Call("TurnSound", from_current = True)
            background Image(pingImage)
            idle Solid("#00000000")
            hover Solid("#00000044")
            xsize 80
            ysize 72
            align (0.85, 0.85)
        image "[profilePic]" align (1, 0.91) size (100, 100) #displays a profile pic for the streamer
        if newGame == False:
            image "[reactImage]" align (-0.02, 0.105) size (263.1, 131.7)
        #image ["stream ui/reactalert.png"] align (0.13, 0.125) size (40, 40)

        #DEBUG MODE
        textbutton "Debug Mode: [debugText]": 
            align(0.05, 1.0)
            action Call("turnDebug", from_current = True)
            text_color "#11a7d4"
            text_hover_color "#11a6d4d8"
        if debugMode == True:
            text "Marshal: [marshal]" align(0.25, 0.85) size 30 color"#d31c1c"
            text "Outlaw: [outlaw]" align(0.25, 0.90) size 30 color"#17c9e0"
            text "Coriolis: [csEngagement]" align(0.35, 0.85) size 30 color"#ee24ee"
            text "KitCat: [kcEngagement]" align(0.35, 0.9) size 30 color"#11fdaf"
            text "pickledDragons: [pdEngagement]" align(0.35, 0.95) size 30 color"#ebe717"
            text "MAC Peace: [macPeace]" align(0.53, 0.85) size 30 color"#ffffff"
            text "MAC Violence: [macViolence]" align(0.53, 0.89) size 30 color"#ffffff"
            text "MAC Hope: [macHope]" align(0.53, 0.93) size 30 color"#ffffff"
            text "MAC Pessimism: [macPessimism]" align(0.53, 0.97) size 30 color"#ffffff"
            text "Jennica: [pilotApproval]" align(0.66, 0.85) size 30 color"#eea112"
            text "Teresa: [engineerApproval]" align(0.66, 0.9) size 30 color"#e41a1a"
            text "Ama: [deadeyeApproval]" align(0.66, 0.95) size 30 color"#14eb75"
            if viewershipHigh == True:
                text "Viewership: High" xpos 1250 ypos 50 size 30 color"#ffe926"
            elif viewershipMed == True:
                text "Viewership: Med" xpos 1250 ypos 50 size 30 color"#ffe926"
            else:
                text "Viewership: Low" xpos 1250 ypos 50 size 30 color"#ffe926"
            text "Reluctance: [reluctance]" xpos 1000 ypos 5 size 30 color"#00ff0d"
            text "Enthusiasm: [enthusiasm]" xpos 1250 ypos 5 size 30 color"#00ff0d"
            text "Energy: [energy]" xpos 1500 ypos 5 size 30 color"#00ff0d"
            text "vig2 ints: [vig2_interactions]" xpos 300 ypos 50 size 30 color"#54d6fd"
            text "vig3 ints: [vig3_interactions]" xpos 500 ypos 50 size 30 color"#54d6fd"
            text "vig4 ints: [vig4_interactions]" xpos 700 ypos 50 size 30 color"#54d6fd"

###Tutorial screens for vignette 1
screen chatTutorial():
    frame:
        ypos 100
        xpos 530 
        xsize 1000
        ysize 230
        xpadding 15 
        ypadding 15 
        right_margin 200
        background Image("images/stream ui/tutorialUI.png")
        text "Sometimes your chat will make comments you can respond to.\nThese are highlighted in yellow.\nClick on them to interact with your viewers."
        textbutton "Close Tutorial":
            action Hide("chatTutorial")
            text_color "#ffffffb9" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
            text_hover_color "#ffffffd5" 
            text_selected_color "#ffffffff"
            align (1.35, 1.0)

screen chatTutorial2():
    frame:
        ypos 100
        xpos 530 
        xsize 1000
        ysize 230
        xpadding 15 
        ypadding 15 
        right_margin 200
        background Image("images/stream ui/tutorialUI.png")
        text "When the face-cam image in the top left has a red exclamation point, you can click on it to initiate a conversation with your viewers."
        textbutton "Close Tutorial":
            action Hide("chatTutorial2")
            text_color "#ffffffb9" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
            text_hover_color "#ffffffd5" 
            text_selected_color "#ffffffff"
            align (1.35, 1.0)  

screen discordNotification():
    frame:
        ypos 653
        xpos 731 
        xsize 1000
        ysize 230
        right_margin 200
        background Solid("#000000ff")
        text "[my_name], it's a raid!\n8bitBANDIT just finished their stream of the game and brought a bunch of people in!"
        textbutton "Close Notification":
            action Return() #Hide("discordNotification")
            text_color "#ffffffb9" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
            text_hover_color "#ffffffd5" 
            text_selected_color "#ffffffff"
            background "#000000ff"
            align (0.5, 1.0)

screen streamFreeze():
    #frame:
        #xsize 1920
        #ysize 1080
        #background Solid("#00000000")
        #textbutton "React":
            #action [Return(), Call(reactTarget)]
            #align (0.95, 0.93)
            #text_color "#ffffffff" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
            #text_hover_color "#ffffffa1" 
            #text_selected_color "#ffffff4f"
            #background "#00aeffcb"
    frame:
        xsize 1920
        ysize 1080
        background Solid("#00000000")
        imagebutton: #just the overlay that you click on
            action [Return(), Call(reactTarget)]
            idle Solid("#00000000")
            hover Solid("#bd050556")
            #hover Image("stream ui/reactHighlight.png") 
            #hover Solid("#dad60563") "#bd0505",
            #hover Solid("#44444463")
            xsize 192
            ysize 120
            align (0.001, 0.113)
        image ["stream ui/reactHighlight.png"] align (0.001, 0.113) xsize 192 ysize 120
        image ["stream ui/reactalert.png"] align (0.095, 0.1) size (30, 30) #the red exclaim image itself

screen raidFreeze():
    frame:
        xsize 1920
        ysize 1080
        background Solid("#00000000")
        #imagebutton:
        #    xsize 298
        #    ysize 135
        #    xalign 0.965
        #    yalign .753
        #    idle "#eeff0081"
        #    hover "#eeff0060"
        #    action [Return(), Call("vig1_sc3_banditConvo")] #could set the Call to like "[curent_analytics_viewcount]" - and then before making the jump, make sure to set $current_analytics_viewcount to the appropriate string

screen vig4_streamFreeze():
    frame:
        xsize 1920
        ysize 1080
        background Solid("#00000000")
        #imagebutton:
        #    xsize 298
        #    ysize 135
        #    xalign 0.965
        #    yalign .753
        #    idle "#eeff0065"
        #    hover "#eeff0044"
        #    action [Return(), Call("vig4_sc2_elliotEntrance")]

#screen for selecting profile picture
screen selectProfilePic():
    text "Now select your streaming profile picture.":
        align (0.33, 0.843)
    imagebutton:
        action [SetVariable("profilePic", "socials/profilepics/profile1.png"), Return()]
        background Image("socials/profilepics/profile1.png")
        idle Image("socials/profilepics/profile1.png")
        hover Solid("#5e5e5e4b")
        xsize 100
        ysize 100
        align (0.3, 0.5)
    imagebutton:
        action [SetVariable("profilePic", "socials/profilepics/profile2.png"), Return()]
        background Image("socials/profilepics/profile2.png")
        idle Image("socials/profilepics/profile2.png")
        hover Solid("#5e5e5e4b")
        xsize 100
        ysize 100
        align (0.5, 0.5)
    imagebutton:
        action [SetVariable("profilePic", "socials/profilepics/profile5.png"), Return()]
        background Image("socials/profilepics/profile5.png")
        idle Image("socials/profilepics/profile5.png")
        hover Solid("#5e5e5e4b")
        xsize 100
        ysize 100
        align (0.7, 0.5)
    #imagebutton: #turned off for time being so the mod has their own profile pic
    #    action [SetVariable("profilePic", "socials/profilepics/profile4.png"), Return()]
    #    background Image("socials/profilepics/profile4.png")
    #    idle Image("socials/profilepics/profile4.png")
    #    hover Solid("#5e5e5e4b")
    #    xsize 100
    #    ysize 100
    #    align (0.8, 0.5)

screen webNavTutorial():
    frame:
        ypos 100
        xpos 530 
        #xpos 530
        #ypos 653
        xsize 1000
        ysize 230
        right_margin 200
        background Image("images/stream ui/tutorialUI.png")
        text "Now that you're done streaming, you can open different tabs on your computer to get updates on your progress and the {i}Oakley 2{/i} community. Click on the highlighted tabs to explore!"
        textbutton "Close Tutorial":
            action Hide("webNavTutorial")
            text_color "#ffffffb9" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
            text_hover_color "#ffffffd5" 
            text_selected_color "#ffffffff"
            align (1.35, 1.0)  

###These screens set up the "Gates" for players to navigate the post-stream session based on their desires.
screen webNavigation_vig1():
    if flinchView == False and screenComplete == True:
        imagebutton:
            action [Hide("webNavigation_vig1"), Hide("viewership"), Hide("viewershipButton"), Hide("streamAnalytics_Details"), Hide("webNavTutorial"), Jump("FlinchAnalytics_vig1")]
            idle Solid("#eff3176b")
            hover Solid("#eff317b9")
            xsize 128
            ysize 40
            align (0.4095, 0.007)          

    if blueitView == False and screenComplete == True:
        imagebutton:
            action [Hide("webNavigation_vig1"), Hide("viewership"), Hide("viewershipButton"), Hide("streamAnalytics_Details"), Hide("webNavTutorial"), Jump("blueitVignette1")]
            idle Solid("#eff3176b")
            hover Solid("#eff317b9")
            xsize 128
            ysize 40
            align (0.4845, 0.007)

    if flinchView == True and blueitView == True and screenComplete == True:
        textbutton "Close Computer":
            action [Hide("webNavigation_vig1"), Hide("viewership"), Hide("viewershipButton"), Hide("streamAnalytics_Details"), Hide("webNavTutorial"), Jump("vig1_brother_1")]
            background Solid("#a03f2eff")
            text_color "#ffffffff"
            text_hover_color "#ffffffce" 
            text_selected_color "#ffffffff"
            text_size 20
            align (0.98, 0.007)


#### WEBNAV SCREEN FOR VIG2####
screen webNavigation_vig2():
    if loopdView == False and screenComplete == True:
        imagebutton:
            action [Hide("webNavigation_vig2"), Hide("viewership"), Hide("viewershipButton_vig2"), Hide("streamAnalytics_Details"), Jump("vig2_macro_modStart")]
            idle Solid("#eff3176b")
            hover Solid("#eff317b9")
            xsize 128
            ysize 40
            align (0.334, 0.007)          

    if flinchView == False and screenComplete == True:
        imagebutton:
            action [Hide("webNavigation_vig2"), Hide("viewership"), Hide("viewershipButton_vig2"), Hide("streamAnalytics_Details"), Jump("FlinchAnalytics_vig2")]
            idle Solid("#eff3176b")
            hover Solid("#eff317b9")
            xsize 128
            ysize 40
            align (0.4095, 0.007)          

    if blueitView == False and screenComplete == True:
        imagebutton:
            action [Hide("webNavigation_vig2"), Hide("viewership"), Hide("viewershipButton_vig2"), Hide("streamAnalytics_Details"), Jump("blueitVignette2_1")]
            idle Solid("#eff3176b")
            hover Solid("#eff317b9")
            xsize 128
            ysize 40
            align (0.4845, 0.007)

    if flinchView == True and blueitView == True and loopdView == True and screenComplete == True:
        #imagebutton:
        #    action [Hide("webNavigation_vig2"), Hide("viewership"), Hide("viewershipButton_vig2"), Hide("streamAnalytics_Details"), Jump("vig2_macro_viewerChat_1")]
        #    idle Solid("#a03f2e85")
        #    hover Solid("#a03f2eff")
        #    xsize 128
        #    ysize 40
        #    align (0.4845, 0.007)
        textbutton "Close Computer":
            action [Hide("webNavigation_vig2"), Hide("viewership"), Hide("viewershipButton_vig2"), Hide("streamAnalytics_Details"), Jump("vig2_macro_viewerChat_1")]
            background Solid("#a03f2eff")
            text_color "#ffffffff"
            text_hover_color "#ffffffce" 
            text_selected_color "#ffffffff"
            text_size 20
            align (0.98, 0.007)      

#### WEBNAV SCREEN FOR VIG3#####
screen webNavigation_vig3():
    if loopdView == False and screenComplete == True:
        imagebutton:
            action [Hide("webNavigation_vig3"), Hide("viewership"), Hide("viewershipButton_vig3"), Hide("streamAnalytics_Details"), Jump("vig3_macro_viewerChat_1")]
            idle Solid("#eff3176b")
            hover Solid("#eff317b9")
            xsize 128
            ysize 40
            align (0.334, 0.007)           

    if flinchView == False and screenComplete == True:
        imagebutton:
            action [Hide("webNavigation_vig3"), Hide("viewership"), Hide("viewershipButton_vig3"), Hide("streamAnalytics_Details"), Jump("FlinchAnalytics_vig3")]
            idle Solid("#eff3176b")
            hover Solid("#eff317b9")
            xsize 128
            ysize 40
            align (0.4095, 0.007)  

    if blueitView == False and screenComplete == True:
        imagebutton:
            action [Hide("webNavigation_vig3"), Hide("viewership"), Hide("viewershipButton_vig3"), Hide("streamAnalytics_Details"), Jump("blueitVignette3_1")]
            idle Solid("#eff3176b")
            hover Solid("#eff317b9")
            xsize 128
            ysize 40
            align (0.4845, 0.007)

    if flinchView == True and blueitView == True and loopdView == True and screenComplete == True:
        textbutton "Close Computer":
            action [Hide("webNavigation_vig3"), Hide("viewership"), Hide("viewershipButton_vig3"), Hide("streamAnalytics_Details"), Jump("vig3_macro_brother_1")]
            background Solid("#a03f2eff")
            text_color "#ffffffff"
            text_hover_color "#ffffffce" 
            text_selected_color "#ffffffff"
            text_size 20
            align (0.98, 0.007)

#### WEBNAV SCREEN FOR VIG4 ###### 
screen webNavigation_vig4():
    if loopdView == False and flinchView == True and blueitView == False and screenComplete == True:
        imagebutton:
            action [Hide("webNavigation_vig4"), Hide("viewership"), Hide("viewershipButton_vig4"), Hide("streamAnalytics_Details"), Jump("vig4_macro_viewerChat_1")]
            idle Solid("#eff3176b")
            hover Solid("#eff317b9")
            xsize 128
            ysize 40
            align (0.334, 0.007)           

    #if flinchView == False and screenComplete == True:
    #    imagebutton:
    #        action [Hide("webNavigation_vig4"), Hide("viewership"), Hide("viewershipButton_vig4"), Hide("streamAnalytics_Details"), Jump("FlinchAnalytics_vig4")]
    #        idle Solid("#eff3176b")
    #        hover Solid("#eff317b9")
    #        xsize 128
    #        ysize 40
    #        align (0.4095, 0.007)  

    if blueitView == False and flinchView == True and loopdView == True and screenComplete == True:
        imagebutton:
            action [Hide("webNavigation_vig4"), Hide("viewership"), Hide("viewershipButton_vig4"), Hide("streamAnalytics_Details"), Jump("blueitVignette4_1")]
            idle Solid("#eff3176b")
            hover Solid("#eff317b9")
            xsize 128
            ysize 40
            align (0.4845, 0.007)

    if flinchView == True and blueitView == True and loopdView == True and screenComplete == True:
        imagebutton:
            action [Hide("webNavigation_vig4"), Hide("viewership"), Hide("viewershipButton_vig4"), Hide("streamAnalytics_Details"), Jump("vig4_macro_writeUp")]
            #background Solid("#a03f2eff")
            #text_color "#ffffffff"
            #text_hover_color "#ffffffce" 
            #text_selected_color "#ffffffff"
            #text_size 20
            idle Solid("#eff3176b")
            hover Solid("#eff317b9")
            xsize 330
            ysize 60
            align (0.96, 0.32)        

##The button below this is a replication of the close computer button in case we want to use it
    #if flinchView == True and blueitView == True and loopdView == True and screenComplete == True:
    #    textbutton "Close Computer":
    #        action [Hide("webNavigation_vig4"), Hide("viewership"), Hide("viewershipButton_vig4"), Hide("streamAnalytics_Details"), Jump("endgame")]
    #        background Solid("#a03f2eff")
    #        text_color "#ffffffff"
    #        text_hover_color "#ffffffce" 
    #        text_selected_color "#ffffffff"
    #        text_size 20
    #        align (0.98, 0.007)

screen closeComputer():
    imagebutton:
        action [Hide("webNavigation_vig4"), Hide("viewership"), Hide("viewershipButton_vig4"), Hide("streamAnalytics_Details"), Jump("endgame")]
        #background Solid("#a03f2eff")
        idle Solid("#eff3176b")
        hover Solid("#eff317b9")
        xsize 145
        ysize 44
        xpos 1695
        ypos 188
        #text_color "#ffffffff"
        #text_hover_color "#ffffffce" 
        #text_selected_color "#ffffffff"
        #text_size 20
        #align (0.95, 0.18)

###PLAYTESTING RECORD SCREEN###
screen playtestRecord():
    text "These are the choices that were made during this playtest":
        align(0.5, 0.1)
    textbutton "End Game":
        action Return()
        align (0.9, 1.0)
        text_color "#ffffffb9" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
        text_hover_color "#ffffffd5" 
        text_selected_color "#ffffffff"
    vbox:
        spacing 25
        align (0.5, 0.4)
        text "Stream vibes: {b}[streamVibes]{/b}"
        text "Kill Allistar: {b}[killAllistar]{/b}"
        text "Customs Depot: {b}[customsDepot]{/b}"
        text "Data Base: {b}[dataBase]{/b}"
        text "Spare Guard with Family: {b}[spareGuard]{/b}"
        text "Aid Ship: {b}[aidShip]{/b}"
        text "Technician: {b}[technicianChoice]{/b}"
        text "Reginald: {b}[reginaldChoice]{/b}"
        text "Top Fan: {b}[topfan]{/b}"