###This script contains code to make the Flinch sections of the game function.

###The screen below this ensures that these details won't disappear whenever the player selects an option on the flinch screen.
screen streamAnalytics_Details():
    image "[profilePic]" align (.0455, .135) size (220, 220)
    text "{b}[username]{/b}" align (0.078, 0.37) size 30
    text "{b}[topfan]{/b}" align (0.28, 0.51) size 30
    text "{b}[followerGoal] fans{/b}" align (0.527, 0.908) size 40 


#The frame below this is for the viewership analytics
screen viewership:
    frame:
        background Solid("#00000000")
        xsize 1020
        ysize 400
        xalign 0.92
        yalign 0.48
        text "Viewers" xalign 0.015 yalign 0.06 vertical True
        #text "Time" xalign 0.5 yalign 1.0

        vbar value AnimatedValue(vbar1, max_viewers, delay=1.0):
            xalign 0.07 yalign 0.008
            xmaximum 47
            ymaximum 327
            left_bar Frame("images/bar/love_empty.png", 100, 10)
            right_bar Frame("images/bar/love_full.png", 100, 10)
            #thumb "images/bar/love_thumb.png" ##Not currently using "thumbs" - could do if we want
            #thumb_offset 30
        #imagebutton idle "images/bar/love_text.png" xalign 1.00 yalign 0.06 xmaximum 47 ymaximum 327 action NullAction()
        vbar value AnimatedValue(vbar2, max_viewers, delay=1.0):
            xalign 0.17 yalign 0.008
            xmaximum 47
            ymaximum 327
            left_bar Frame("images/bar/love_empty.png", 100, 10)
            right_bar Frame("images/bar/love_full.png", 100, 10)
        vbar value AnimatedValue(vbar3, max_viewers, delay=1.0):
            xalign 0.27 yalign 0.008
            xmaximum 47
            ymaximum 327
            left_bar Frame("images/bar/love_empty.png", 100, 10)
            right_bar Frame("images/bar/love_full.png", 100, 10)
        vbar value AnimatedValue(vbar4, max_viewers, delay=1.0):
            xalign 0.37 yalign 0.008
            xmaximum 47
            ymaximum 327
            left_bar Frame("images/bar/love_empty.png", 100, 10)
            right_bar Frame("images/bar/love_full.png", 100, 10)
        vbar value AnimatedValue(vbar5, max_viewers, delay=1.0):
            xalign 0.47 yalign 0.008
            xmaximum 47
            ymaximum 327
            left_bar Frame("images/bar/love_empty.png", 100, 10)
            right_bar Frame("images/bar/love_full.png", 100, 10)
        vbar value AnimatedValue(vbar6, max_viewers, delay=1.0):
            xalign 0.57 yalign 0.008
            xmaximum 47
            ymaximum 327
            left_bar Frame("images/bar/love_empty.png", 100, 10)
            right_bar Frame("images/bar/love_full.png", 100, 10)
        vbar value AnimatedValue(vbar7, max_viewers, delay=1.0):
            xalign 0.67 yalign 0.008
            xmaximum 47
            ymaximum 327
            left_bar Frame("images/bar/love_empty.png", 100, 10)
            right_bar Frame("images/bar/love_full.png", 100, 10)
        vbar value AnimatedValue(vbar8, max_viewers, delay=1.0):
            xalign 0.77 yalign 0.008
            xmaximum 47
            ymaximum 327
            left_bar Frame("images/bar/love_empty.png", 100, 10)
            right_bar Frame("images/bar/love_full.png", 100, 10)
        vbar value AnimatedValue(vbar9, max_viewers, delay=1.0):
            xalign 0.87 yalign 0.008
            xmaximum 47
            ymaximum 327
            left_bar Frame("images/bar/love_empty.png", 100, 10)
            right_bar Frame("images/bar/love_full.png", 100, 10)
        vbar value AnimatedValue(vbar10, max_viewers, delay=1.0):
            xalign 0.97 yalign 0.008
            xmaximum 47
            ymaximum 327
            left_bar Frame("images/bar/love_empty.png", 100, 10)
            right_bar Frame("images/bar/love_full.png", 100, 10)


#probably easier to just make a separate screen for vignette 2. Or at least a separate screen that can hold all the buttons. 
#Yeah, separate screen would be easiest by far
screen streamAnalytics():
    #zorder 100 #determines how much overlayed it is

    ####Below is commented out to set up webNavigation screen as the guide through the poststream events
    #if flinchCheck >= 3 and vignette1 == True:
    #    textbutton "Open Blueit":
    #        background Solid("#a03f2eff")
    #        action [Hide("viewership"), Hide("streamAnalytics_Details"), Jump("blueitVignette1")] #can change this to a [variable] so we can adjust on the fly
    #        text_color "#ffffffff" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
    #        text_hover_color "#ffffffce" 
    #        text_selected_color "#ffffffff"
    #        text_size 22
    #        align (0.4, 0.008)

    #elif flinchCheck >= 3 and vignette2 == True:
    #    textbutton "Open Blueit":
    #        background Solid("#a03f2eff")
    #        action [Hide("viewership"), Hide("streamAnalytics_Details"), Jump("vig2_macro_viewerChat_1")] #can change this to a [variable] so we can adjust on the fly
    #        text_color "#ffffffff" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
    #        text_hover_color "#ffffffce" 
    #        text_selected_color "#ffffffff"
    #        text_size 22
    #        align (0.4, 0.008)

    #The frame below this is for identifying the average audience number
    imagebutton:
        idle Solid("#00000036")
        hover Solid("#0000006b")
        xsize 360
        ysize 260
        xalign 0.53
        yalign 0.935
        if audienceCheck == False:
            action Call("vig1_analytics_audience", from_current = True)
        else:
            action NullAction()
    
    #textbutton "Average Audience: 13":
    #    if audienceCheck == False:
    #        action Call("vig1_analytics_audience", from_current = True)
    #    else:
    #        action NullAction()
    #    background Solid("#2b2929ff")
    #    text_color "#ffee02cb" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
    #    text_hover_color "#ffee02ff" 
    #    text_selected_color "#ffffffff"
    #    text_size 50
    #    align (0.03, 0.2)
    #The frame below this is for the Top Fan
    imagebutton:
        xsize 353
        ysize 200
        #background Solid("#0000001c")
        xalign 0.278
        yalign 0.47
        idle Solid("#00000036")
        hover Solid("#0000006b")
        if topfanCheck == False:
            action Call("vig1_analytics_topfan", from_current = True)
        else:
            action NullAction()
        #style "flinch_button"
        #textbutton "[topfan]":
        #    if topfanCheck == False:
        #        action Call("vig1_analytics_topfan", from_current = True)
        #    else:
        #        action NullAction()
        #    text_color "#ffee02cb" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
        #    text_hover_color "#ffee02ff" 
        #    text_selected_color "#ffffffff"
        #    text_size 50
        #    align (0.5, 0.5)


screen viewershipButton:
        imagebutton:
            xsize 1020
            ysize 400
            xalign 0.92
            yalign .475
            idle Solid("#00000036")
            hover Solid("#0000006b")
            if viewcountCheck == False:
                action Call("vig1_analytics_viewcount", from_current = True) #could set the Call to like "[curent_analytics_viewcount]" - and then before making the jump, make sure to set $current_analytics_viewcount to the appropriate string
            else:
                action NullAction()

    #The frame below this is for vieweing Moze's alignment
    #textbutton "Check Alignment":
    #    background Solid("#000000ff")
    #    if alignmentCheck == False:    
    #        action Call("vig1_analytics_alignment", from_current = True)
    #    else:
    #        action NullAction()
    #    text_color "#ffee02cb" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
    #    text_hover_color "#ffee02ff" 
    #    text_selected_color "#ffffffff"
    #    text_size 50
    #    align (0.78, 0.15)

######Screens for Vignette 2########
screen streamAnalytics_vig2():
    #zorder 100 #determines how much overlayed it is
    #if flinchCheck >= 3:
    #    textbutton "Close Flinch":
    #        background Solid("#66439eff")
    #        action [Hide("viewership"), Hide("streamAnalytics_Details"), Jump("vig2_macro_viewerChat_1")] #can change this to a [variable] so we can adjust on the fly
    #        text_color "#ffffffff" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
    #        text_hover_color "#ffffffce" 
    #        text_selected_color "#ffffffff"
    #        text_size 22
    #        align (0.4, 0.008)

    #The frame below this is for identifying the average audience number
    imagebutton:
        idle Solid("#00000036")
        hover Solid("#0000006b")
        xsize 360
        ysize 260
        xalign 0.53
        yalign 0.935
        if flinch_audienceCheck == False:
            action Call("vig2_analytics_audience", from_current = True) #Change these to new target labels for vignette 2
        else:
            action NullAction()
    
    imagebutton:
        xsize 353
        ysize 200
        #background Solid("#0000001c")
        xalign 0.278
        yalign 0.47
        idle Solid("#00000036")
        hover Solid("#0000006b")
        if flinch_topfanCheck == False:
            action Call("vig2_analytics_topfan", from_current = True)
        else:
            action NullAction()

screen viewershipButton_vig2:
        imagebutton:
            xsize 1020
            ysize 400
            xalign 0.92
            yalign .475
            idle Solid("#00000036")
            hover Solid("#0000006b")
            if flinch_viewcountCheck == False:
                action Call("vig2_analytics_viewcount", from_current = True) #could set the Call to like "[curent_analytics_viewcount]" - and then before making the jump, make sure to set $current_analytics_viewcount to the appropriate string
            else:
                action NullAction()


### VIGNETTE 3 SCREENS #####

screen streamAnalytics_vig3():
    #The frame below this is for identifying the average audience number
    imagebutton:
        idle Solid("#00000036")
        hover Solid("#0000006b")
        xsize 360
        ysize 260
        xalign 0.53
        yalign 0.935
        if flinch_audienceCheck == False:
            action Call("vig3_analytics_audience", from_current = True)
        else:
            action NullAction()
    
    imagebutton:
        xsize 353
        ysize 200
        #background Solid("#0000001c")
        xalign 0.278
        yalign 0.47
        idle Solid("#00000036")
        hover Solid("#0000006b")
        if flinch_topfanCheck == False:
            action Call("vig3_analytics_topfan", from_current = True)
        else:
            action NullAction()

screen viewershipButton_vig3:
        imagebutton:
            xsize 1020
            ysize 400
            xalign 0.92
            yalign .475
            idle Solid("#00000036")
            hover Solid("#0000006b")
            if flinch_viewcountCheck == False:
                action Call("vig3_analytics_viewcount", from_current = True) 
            else:
                action NullAction()

### VIGNETTE 4 SCREENS ####

screen streamAnalytics_vig4():
    #The frame below this is for identifying the average audience number
    imagebutton:
        idle Solid("#00000036")
        hover Solid("#0000006b")
        xsize 360
        ysize 260
        xalign 0.53
        yalign 0.935
        if flinch_audienceCheck == False:
            action Call("vig4_analytics_audience", from_current = True)
        else:
            action NullAction()
    
    imagebutton:
        xsize 353
        ysize 200
        #background Solid("#0000001c")
        xalign 0.278
        yalign 0.47
        idle Solid("#00000036")
        hover Solid("#0000006b")
        if flinch_topfanCheck == False:
            action Call("vig4_analytics_topfan", from_current = True)
        else:
            action NullAction()

screen viewershipButton_vig4:
        imagebutton:
            xsize 1020
            ysize 400
            xalign 0.92
            yalign .475
            idle Solid("#00000036")
            hover Solid("#0000006b")
            if flinch_viewcountCheck == False:
                action Call("vig4_analytics_viewcount", from_current = True) 
            else:
                action NullAction()