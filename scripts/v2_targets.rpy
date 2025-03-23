###This script contains targets that the comments and reactions can direct to

label vig2_sc1_testquestion():
    $ macroChoice = True
    $ vig2_sc1_comment2.click = False
    $ narrator = reg_narrator
    menu:
        "Coriolis remembered I had a test today, that's so sweet!"
        "It went well!":
            $ csEngagement += 1
            player "It was really great actually! Can't believe you remembered!"
            $ AddChatter(vig2_sc1_coriolis_comment1)
        "Not so hot":
            $ csEngagement += 1
            player "It kicked my butt. Honestly I'm just hoping I pass."
            $ AddChatter(vig2_sc1_coriolis_comment2)
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc1_matticusopinion():
    $ macroChoice = True
    $ vig2_sc1_comment13.click = False
    $ narrator = reg_narrator
    menu:
        "What did I think of Matticus in game 1?"
        "He was the worst":
            player "Ugh, no this guy has always been the worst"
            $ AddChatter(vig2_sc1_kitcat_comment1)
        "He was fine":
            $ kcEngagement += 1
            player "I didn't mind him as much as some fans, even though I didn't ally with him a ton."
            $ AddChatter(vig2_sc1_kitcat_comment2)
    $ macroChoice = False
    #if macroNarration == False:
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc2_mar_consistency():
    $ macroChoice = True
    $ vig2_sc2_mar_comment3.click = False
    $ narrator = reg_narrator
    menu:
        "Someone's asking if this is consistent with the last episode"
        "We'll warm up to Outlaw":
            $ pdEngagement += 1
            player "Don't worry chat, we're just getting warmed up."
            player "After all, can't be Outlaw all the time or it isn't special."
            $ AddChatter(vig2_sc2_mar_J4MresponseOUT)
        "Let's avoid Outlaw for now":
            $ reluctance += 1
            player "I mean, we don't want MORE people getting hurt."
            player "This keeps us under the radar for the mission too."
            $ AddChatter(vig2_sc2_mar_J4MresponseMAR)
    $ macroChoice = False
    #if macroNarration == False:
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc2_out_romance():
    $ macroChoice = True
    $ vig2_sc2_out_comment5.click = False
    $ narrator = reg_narrator
    menu:
        "I'm thinking Jennica":
            $ csEngagement += 1
            player "Jennica's sweet, I'm leaning her at the moment!"
            $ romanceJennica = True
            $ romanceTeresa = False
            $ romanceAma = False
            pause 0.5
            $ AddChatter(vig2_sc2_romance_pilot1)
            pause 1.0
        "Probably Teresa":
            $ kcEngagement += 1
            player "Teresa for sure. She's got an edge I appreciate."
            $ romanceJennica = False
            $ romanceTeresa = True
            $ romanceAma = False
            pause 0.5
            $ AddChatter(vig2_sc2_romance_engineer1)
            pause 1.0
        "Ama all day, for sure":
            $ kcEngagement += 2
            $ csEngagement += 1
            $ pdEngagement += 1
            player "Actually, I'm holding out that there will be an Ama romance path."
            $ romanceTeresa = False
            $ romanceJennica = False
            $ romanceAma = True
            pause 1.0
            $ AddChatter(vig2_sc2_romance_ama1)
            pause 1.0
            $ AddChatter(vig2_sc2_romance_ama2)
            pause 1.0
    $ macroChoice = False
    #if macroNarration == False:
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc4_gameplan():
    $ macroChoice = True
    $ vig2_sc4_comment1.click = False
    $ narrator = reg_narrator
    menu:
        "How should I approach Matticus?"
        "Let's lean into it":
            $ enthusiasm += 1
            $ pdEngagement += 1
            $ kcEngagement += 1
            $ csEngagement -= 1
            player "Of course, we're taking a walk on the dark side."
            $ AddChatter(vig2_sc4_ally_comment1)
            pause 1.0
            $ AddChatter(vig2_sc4_ally_comment2)
            pause 1.0
            $ AddChatter(vig2_sc4_ally_comment3)
            pause 1.0
            $ AddChatter(vig2_sc4_ally_comment4)
        "Don't listen to him":
            $ reluctance += 1
            $ csEngagement += 1
            $ pdEngagement -= 1
            player "Yeah, do the exact opposite of whatever Matticus wants."
            $ AddChatter(vig2_sc4_against_comment1)
            pause 1.0
            $ AddChatter(vig2_sc4_against_comment2)
    $ macroChoice = False
    #if macroNarration == False:
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc7_toofar():
    $ macroChoice = True
    $ vig2_sc7_out_comment1.click = False
    $ narrator = reg_narrator
    menu:
        "Is this too far?"
        "Let's roll with it":
            $ enthusiasm += 1
            $ pdEngagement += 1
            $ kcEngagement += 1
            player "YOU SAID IT!"
        "It's feeling off to me":
            $ csEngagement += 2
            $ pdEngagement -= 2
            $ reluctance -= 1
            player "Kinda wish I could go back tbh..."
    $ macroChoice = False
    #if macroNarration == False:
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc7_rips():
    $ macroChoice = True
    $ vig2_sc7_out_execute_comment4.click = False
    $ narrator = reg_narrator
    menu:
        "Should I encourage this?"
        "Guys, this is serious":
            $ reluctance += 2
            $ pdEngagement -= 2
            $ kcEngagement -= 1
            $ csEngagement += 1
            $ encourageRIPS = False
            "This is pretty heavy stuff guys, let's not get too carried away."
        "Put those rips in chat":
            $ enthusiasm += 2
            $ pdEngagement += 1
            $ kcEngagement += 1
            $ encourageRIPS = True
            "RIP Otacon guy"
            pause 1.0
            $ AddChatter(vig2_epilogue_out_rips1)
            pause 0.5
            $ AddChatter(vig2_epilogue_out_rips2)
            pause 0.5
            $ AddChatter(vig2_epilogue_out_rips3)
            pause 1.5
            $ AddChatter(vig2_epilogue_out_rips4)
            pause 1.0
            $ AddChatter(vig2_epilogue_out_rips5)
            pause 1.0
            $ AddChatter(vig2_epilogue_out_rips6)
            pause 0.5
            $ AddChatter(vig2_epilogue_out_rips7)
    $ macroChoice = False
    #if macroNarration == False:
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_epilogue_outlaw():
    $ macroChoice = True
    $ vig2_epilogue_out_comment6.click = False
    $ narrator = reg_narrator
    menu:
        "That was pretty different from how things usually go."
        "It was exciting!":
            $ enthusiasm += 1
            player "Nope! But definitely fun haha"
        "It was exhausing!":
            #Just because one choice affects a variable doesn't mean its opposite has to do something
            #We can have a "neutral" choice
            player "I feel like just ran an emotional marathon haha"
    $ macroChoice = False
    #if macroNarration == False:
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return