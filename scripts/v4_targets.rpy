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

label vig4_sc2_AFKDream():
    $ macroChoice = True
    $ vig4_sc2_6_comment8.click = False
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

label vig4_sc2_elliotEntrance():
    $ macroChoice = True
    $ vig4_sc2_6_comment43.click = False
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

