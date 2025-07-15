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
    $ vig4_sc2_1_comment8.click = False
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