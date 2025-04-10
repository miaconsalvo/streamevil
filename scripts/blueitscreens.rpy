#This script contains code to make the blueit sections of the game function.

screen blueit():
    if blueitChoiceCheck == True:
        textbutton "Close Blueit":
            action Jump("vig1_brother_1")
            background Solid("#66439eff")
            text_color "#ffffffff"
            text_hover_color "#ffffffce" 
            text_selected_color "#ffffffff"
            text_size 20
            align (0.395, 0.007)

    viewport:
        area (430, 460, 1050, 580)
        draggable True #allows scrollbar to be dragged
        mousewheel True #allows mousewheel to scroll viewport
        scrollbars "vertical" #sets vertical scroll bar
        #The frame below this was set up to display Blueit Threads similar to how chats are shown in stream.
        #Each thread is an individual object that gets organized within a vbox.
        #The advantage of this is organization and the ability to quickly change what threads appear by adusting
        #what variables appear in the "blueitpages" list (in the "lists" script)
        #The downside is these will always only be imagebuttons, so adding things like "upvotes" or having players
        #actually click the "read more" elements wouldn't be possible
        vbox:
            spacing 10
            for t in (blueitPages):
                if t.tag == 1:
                    imagebutton:
                        action Call(t.target, from_current = True)
                        background Image(t.image)
                        idle Image(t.image)
                        hover Solid("#2a6c9742")
                        xsize 1010
                        ysize 340
                else:
                    imagebutton:
                        action Call(t.target, from_current = True)
                        background Image(t.image)
                        idle Image(t.image)
                        hover Solid("#2a6c9742")
                        xsize 1010
                        ysize 620
        #This frame displays the main page of Blueit Threads as a single image, like how we'll show specific threads
        #Downside to this is lack of flexibility if we want to change anything about the threads. We'll be displaying the whole image
        #in its entirety so there's less modularity. This is relevant for one of the upsides which is flexibility in what parts
        #of the image are buttons. By displaying this as a single image, we can cut out the "titles" from the top of the threads
        #and then render them as textbuttons in Ren'Py. Then, we can also put buttons to activate the "upvote" buttons.
        #There's another downside that results from this though which is just that we need to be fairly particular and specific about
        #what parts we're leaving out of the image, it also means we'll need to make sure to get Ren'Py to display the textbuttons
        #with the right font. So we also sacrifice a bit in terms of the look. The second upside though is just that it's easy to implement at first
        #The downside is that we would probably need to create specific placements for each successive screen after each vignette - cause where the
        #textbuttons and image buttons line up might change each time. So in order to get the benefit of the visual flexibility, it comes at the cost
        #of time.
        #frame:
        #    background Image("blueitposts.png")
        #    xsize 1050
        #    ysize 1080
        #    text "This is text": 
        #        xpos 500
        #        ypos 1000

screen blueitButtonCheck():
    textbutton "Back to Main Page":
        action [Hide("blueitThread"), Jump("blueitVignette2")]
        background Solid("#000000ff")
        text_color "#ffffffd3" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
        text_hover_color "#ffffffff" 
        text_selected_color "#ffffffff"
        text_size 25
        align (0.74, 0.39)

screen blueitThread():
    viewport:
        area (430, 460, 1050, 580)
        draggable True #allows scrollbar to be dragged
        mousewheel True #allows mousewheel to scroll viewport
        scrollbars "vertical" #sets vertical scroll bar
        image(blueitImage)

#screen blueitThread():
#    frame:
#        #background Image("launch thread.png") xalign 0.5
#        viewport id "blueitView":
#            area (0, 0, 1920, 1080)
#            draggable True #allows scrollbar to be dragged
#            mousewheel True #allows mousewheel to scroll viewport
#            scrollbars "vertical"
#            frame:
#                background Image(blueitImage)
#                xsize 1920
#                ysize yb














#The code below this was used back when I was defining all the buttons of BlueIt manually and without the right background.
        #text "This is Blueit" xalign 0.5 yalign 0.0
        #textbutton "Official Oakley 2 Launch Thread":
        #    action Call("vig1_blueit_launchthread") #, from_current = True)
        #    background Solid("#000000ff")
        #    text_color "#ffffffd3" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
        #    text_hover_color "#ffffffff" 
        #    text_selected_color "#ffffffff"
        #    text_size 30
        #    align (0.36, 0.49)
        #textbutton "Thoughts on first major choice":
        #    action Call("vig1_blueit_firstchoice")
        #    background Solid("#000000ff")
        #    text_color "#ffffffd3" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
        #    text_hover_color "#ffffffff" 
        #    text_selected_color "#ffffffff"
        #    text_size 30
        #    align (0.36, 0.76)
        #textbutton "Who are you\nromancing <3":
        #    action Call("vig1_blueit_romance")
        #    background Solid("#000000ff")
        #    text_color "#ffffffd3" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
        #    text_hover_color "#ffffffff" 
        #    text_selected_color "#ffffffff"
        #    text_size 30
        #    align (0.3, 0.25)
        #textbutton "Do I need to play\nthe first game?":
        #    action Call("vig1_blueit_firstgame")
        #    background Solid("#000000ff")
        #    text_color "#ffffffd3" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
        #    text_hover_color "#ffffffff" 
        #    text_selected_color "#ffffffff"
        #    text_size 30
        #    align (0.872, 0.25)
        #textbutton "Funny glitch":
        #    action Call("vig1_blueit_glitch")
        #    background Solid("#000000ff")
        #    text_color "#ffffffd3" #this applies colors to the text. It will appear as plain white text after selection because it will default back to its c.colour property. 
        #    text_hover_color "#ffffffff" 
        #    text_selected_color "#ffffffff"
        #    text_size 30
        #    align (0.66, 0.25)
        