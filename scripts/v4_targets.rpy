label vig4_sc1_pdParanoia():
    $ macroChoice = True
    $ vig4_sc1_comment5.click = False
    $ narrator = reg_narrator
    #menu:
    #    "Fill the menu with something."
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc1_csRomance():
    $ macroChoice = True
    $ vig4_sc2_2_comment20.click = False
    $ narrator = reg_narrator
    #menu:
    #    "Fill the menu with something."
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc1_kcPrediction():
    $ macroChoice = True
    $ vig4_sc2_1_comment1.click = False
    $ narrator = reg_narrator
    #menu:
    #    "Fill the menu with something."
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc2_rube():
    $ macroChoice = True
    $ vig4_sc2_8_comment8.click = False
    $ narrator = reg_narrator
    #menu:
    #    "Fill the menu with something."
    $ AddChatter(vig4_sc2_1_comment9)
    pause 0.5
    $ AddChatter(vig4_sc2_1_comment10)
    pause 0.5
    $ AddChatter(vig4_sc2_1_comment11)
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc2_peacefulTown():
    $ macroChoice = True
    $ vig4_sc2_6_comment1.click = False
    $ narrator = reg_narrator
    #menu:
    #    "Fill the menu with something."
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc2_AFKDream():
    $ macroChoice = True
    $ vig4_sc2_6_comment8.click = False
    $ narrator = reg_narrator
    #menu:
    #    "Fill the menu with something."
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc2_elliotEntrance():
    $ macroChoice = True
    $ vig4_sc2_6_comment43.click = False
    $ narrator = reg_narrator
    menu:
        "Elliot joined the chat!"
        "Aren't you supposed to be on a date?":
            player "Hey El! Aren't you supposed to be on a date right now?"
            $ AddChatter(vig4_bro_comment1)
            pause 1.0
            player "Oh my god that's so sweet! It's great to have you here!"
            $ AddChatter(vig4_bro_comment3)
            menu:
                player "Oh my god that's so sweet! It's great to have you here!"
                "Everyone say \"hi\" to my brother!":
                    player "El, meet Chat. Chat, say \"hi\" to my lil bro!"
                    $ AddChatter(vig4_bro_comment4)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment5)
                    $ AddChatter(vig4_bro_comment6)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment7)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment8)
                    $ AddChatter(vig4_bro_comment9)
                    $ AddChatter(vig4_bro_comment10)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment11)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment12)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment13)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment14)
                    player "Alright El, so basically, we landed on this moon called Polaris and found the Dragonflies."
                    player "Their leader is this old engineer guy named Coil who helped create MAC with Dr. Vanas back in the day."
                    $ AddChatter(vig4_bro_comment15)
                    pause 0.5
                    player "Yeah, her name's Vega, she's cool."
                    $ AddChatter(vig4_bro_comment16)
                    player "Right, so turns out they want us to leave MAC behind."
                    $ AddChatter(vig4_bro_comment17)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment18)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment19)
                    player "Yeah, and while we're waiting to hear back, we're gonna hit up a festival that's happening in the town."
                    $ AddChatter(vig4_bro_comment20)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment21)
                    pause 0.5
                    player "Pretty much. Let's keep it rolling!"
                    $ AddChatter(vig4_bro_comment22)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment23)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment24)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment25)
                    "Alright, alright, let's get back to it."
                    $ AddChatter(vig4_bro_comment26)
                "Let's catch Elliot up to speed.":
                    player "Alright El, so basically, we landed on this moon called Polaris and found the Dragonflies."
                    player "Their leader is this old engineer guy named Coil who helped create MAC with Dr. Vanas back in the day."
                    $ AddChatter(vig4_bro_comment15)
                    pause 0.5
                    player "Yeah, her name's Vega, she's cool."
                    $ AddChatter(vig4_bro_comment16)
                    player "Right, so turns out they want us to leave MAC behind."
                    $ AddChatter(vig4_bro_comment17)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment18)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment19)
                    player "Yeah, and while we're waiting to hear back, we're gonna hit up a festival that's happening in the town."
                    $ AddChatter(vig4_bro_comment20)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment21)
                    pause 0.5
                    player "Pretty much. Let's keep it rolling!"
                    $ AddChatter(vig4_bro_comment22)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment23)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment24)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment25)
                    "Alright, alright, let's get back to it."
                    $ AddChatter(vig4_bro_comment26)
        "So good to see you!":
            player "Oh my god, El! It's so good to have you in chat!"
            $ AddChatter(vig4_bro_comment1)
            player "Oh my god that's so sweet! It's great to have you here!"
            $ AddChatter(vig4_bro_comment3)
            menu:
                player "Oh my god that's so sweet! It's great to have you here!"
                "Everyone say \"hi\" to my brother!":
                    player "El, meet Chat. Chat, say \"hi\" to my lil bro!"
                    $ AddChatter(vig4_bro_comment4)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment5)
                    $ AddChatter(vig4_bro_comment6)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment7)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment8)
                    $ AddChatter(vig4_bro_comment9)
                    $ AddChatter(vig4_bro_comment10)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment11)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment12)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment13)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment14)
                    player "Alright El, so basically, we landed on this moon called Polaris and found the Dragonflies."
                    player "Their leader is this old engineer guy named Coil who helped create MAC with Dr. Vanas back in the day."
                    $ AddChatter(vig4_bro_comment15)
                    pause 0.5
                    player "Yeah, her name's Vega, she's cool."
                    $ AddChatter(vig4_bro_comment16)
                    player "Right, so turns out they want us to leave MAC behind."
                    $ AddChatter(vig4_bro_comment17)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment18)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment19)
                    player "Yeah, and while we're waiting to hear back, we're gonna hit up a festival that's happening in the town."
                    $ AddChatter(vig4_bro_comment20)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment21)
                    pause 0.5
                    player "Pretty much. Let's keep it rolling!"
                    $ AddChatter(vig4_bro_comment22)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment23)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment24)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment25)
                    "Alright, alright, let's get back to it."
                    $ AddChatter(vig4_bro_comment26)
                "Let's catch Elliot up to speed.":
                    player "Alright El, so basically, we landed on this moon called Polaris and found the Dragonflies."
                    player "Their leader is this old engineer guy named Coil who helped create MAC with Dr. Vanas back in the day."
                    $ AddChatter(vig4_bro_comment15)
                    pause 0.5
                    player "Yeah, her name's Vega, she's cool."
                    $ AddChatter(vig4_bro_comment16)
                    player "Right, so turns out they want us to leave MAC behind."
                    $ AddChatter(vig4_bro_comment17)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment18)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment19)
                    player "Yeah, and while we're waiting to hear back, we're gonna hit up a festival that's happening in the town."
                    $ AddChatter(vig4_bro_comment20)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment21)
                    pause 0.5
                    player "Pretty much. Let's keep it rolling!"
                    $ AddChatter(vig4_bro_comment22)
                    pause 1.0
                    $ AddChatter(vig4_bro_comment23)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment24)
                    pause 0.5
                    $ AddChatter(vig4_bro_comment25)
                    "Alright, alright, let's get back to it."
                    $ AddChatter(vig4_bro_comment26)
        "Everyone say hi to my brother!":
            player "El, meet Chat. Chat, say \"hi\" to my lil bro!"
            $ AddChatter(vig4_bro_comment4)
            pause 0.5
            $ AddChatter(vig4_bro_comment5)
            $ AddChatter(vig4_bro_comment6)
            pause 1.0
            $ AddChatter(vig4_bro_comment7)
            pause 0.5
            $ AddChatter(vig4_bro_comment8)
            $ AddChatter(vig4_bro_comment9)
            $ AddChatter(vig4_bro_comment10)
            pause 1.0
            $ AddChatter(vig4_bro_comment11)
            pause 1.0
            $ AddChatter(vig4_bro_comment12)
            pause 1.0
            $ AddChatter(vig4_bro_comment13)
            pause 0.5
            $ AddChatter(vig4_bro_comment14)
            player "Alright El, so basically, we landed on this moon called Polaris and found the Dragonflies."
            player "Their leader is this old engineer guy named Coil who helped create MAC with Dr. Vanas back in the day."
            $ AddChatter(vig4_bro_comment15)
            pause 0.5
            player "Yeah, her name's Vega, she's cool."
            $ AddChatter(vig4_bro_comment16)
            player "Right, so turns out they want us to leave MAC behind."
            $ AddChatter(vig4_bro_comment17)
            pause 0.5
            $ AddChatter(vig4_bro_comment18)
            pause 1.0
            $ AddChatter(vig4_bro_comment19)
            player "Yeah, and while we're waiting to hear back, we're gonna hit up a festival that's happening in the town."
            $ AddChatter(vig4_bro_comment20)
            pause 1.0
            $ AddChatter(vig4_bro_comment21)
            pause 0.5
            player "Pretty much. Let's keep it rolling!"
            $ AddChatter(vig4_bro_comment22)
            pause 1.0
            $ AddChatter(vig4_bro_comment23)
            pause 0.5
            $ AddChatter(vig4_bro_comment24)
            pause 0.5
            $ AddChatter(vig4_bro_comment25)
            pause 0.5
            $ AddChatter(vig4_bro_comment26)
            "Alright, alright, let's get back to it."
            $ AddChatter(vig4_bro_comment27)
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_festivalRomance():
    $ macroChoice = True
    $ vig4_sc3_2_vega_comment2.click = False
    $ narrator = reg_narrator
    #menu:
    #    "Fill the menu with something."
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_elMemory():
    $ macroChoice = True
    $ vig4_sc3_2_jenn_comment12.click = False
    $ narrator = reg_narrator
    #menu:
    #    "Fill the menu with something."
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return





####TARGETS FOR BLUEIT ######

label vig4_blueit_endgamethread():
    $ screenComplete = False
    $ blueitImage = "socials/bThread_v4_endgame.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

####TARGETS FOR FLINCH ######

label vig4_analytics_audience():
    hide screen viewershipButton_vig4
    "This is a test for the Flinch screen of Vignette 4."
    $ flinchCheck += 1
    $ flinch_audienceCheck = True
    if flinchCheck >= 3:
        $ screenComplete = True
    else:
        pass
    show screen viewershipButton_vig4
    return

label vig4_analytics_topfan():
    hide screen viewershipButton_vig4
    $ flinchCheck += 1
    $ flinch_topfanCheck = True
    if topfan == "Coriolis":
        "Coriolis."
    elif topfan == "KitCat":
        "KitCat."
    elif topfan == "PickledDragons":
        "PickledDragons."
    else:
        "Coriolis by default."
    if flinchCheck >= 3:
        $ screenComplete = True
    else:
        pass
    show screen viewershipButton_vig4
    return

label vig4_analytics_viewcount():
    $ flinchCheck += 1
    $ flinch_viewcountCheck = True
    hide screen viewershipButton_vig4
    "This is a test for the Flinch screen of Vignette 4."
    if flinchCheck >= 3:
        $ screenComplete = True
    else:
        pass
    show screen viewershipButton_vig4
    return

