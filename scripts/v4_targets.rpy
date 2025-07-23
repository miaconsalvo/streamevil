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


label vig4_sc3_pdCoilCommentary():
    $ macroChoice = True
    $ vig4_sc3_3_comment36.click = False
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

label vig4_sc3_csCoilCommentary():
    $ macroChoice = True
    $ vig4_sc3_3_comment39.click = False
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

label vig4_sc4_kcNoOffer():
    $ macroChoice = True
    $ vig4_sc4_1_comment31.click = False
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

label vig4_sc5_csClimax():
    $ macroChoice = True
    $ vig4_sc5_1_comment27.click = False
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

label vig4_sc5_oscarReturn():
    $ macroChoice = True
    $ vig4_sc6_defend_1_comment1.click = False
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

label vig4_sc6_ripTank():
    $ macroChoice = True
    $ vig4_sc6_defend_4_comment5.click = False
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

label vig4_sc6_pdGoodPerson():
    $ macroChoice = True
    $ vig4_sc6_attack_3_ama_comment19.click = False
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

label vig4_sc6_reggieReaction():
    $ macroChoice = True
    $ vig4_sc6_defend_5_comment19.click = False
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

label vig4_sc7_kcWhyNoRomance():
    $ macroChoice = True
    $ vig4_sc7_3_ama_comment56.click = False
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

### Streamer Reacts

label vig4_sc1_macjokes():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "MAC just made a joke."
        "MAC can joke!?":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Chat did make just tell a joke!?"
            player "That's crazy! He's really learning."
            $ AddChatter (vig4_sc1_react_comment1)
            $ AddChatter (vig4_sc1_react_comment2)
            pause 0.5
        "That's so cute!":
            $ reactImage = "stream ui/reactshocked.png"
            player "Holy crap MAC's a lil joker!"
            player "ADORABLE!!!"
            $ AddChatter (vig4_sc1_react_comment3)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc2_trustvillager():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Can you trust this person?"
        "Suspicious.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Not sure we can trust him."
            player "Kinda sus that he's so friendly."
            $ AddChatter(vig4_sc2_react_comment1)
            pause 0.5
        "They seem to mean well enough.":
            $ reactImage = "stream ui/reactconfident.png"
            player "He seems to be friendly!"
            player "I say we trust him!"
            $ AddChatter(vig4_sc2_react_comment2)
            pause 0.5
        "This is going to go poorly.":
            $ reactImage = "stream ui/reactunsure.png"
            player "This is going to go so bad."
            player "This might've been the wrong call."
            $ AddChatter(vig4_sc2_react_comment3)
            $ AddChatter(vig4_sc2_react_comment4)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc2_macischanging():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on MAC changing."
        "Cool!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Yeah he's been changing since the start right?"
            player "Really cool how the game's been changing as we go!"
            $ AddChatter(vig4_sc2_react_comment5)
            pause 0.5
        "Obviously.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Yeah duh."
            player "Isn't that what the game's been doing all along?"
            $ AddChatter(vig4_sc2_react_comment6)
            pause 0.5
        "What have we been teaching him?":
            if marshal > outlaw:
                $ reactImage = "stream ui/reactunsure.png"
                player "Oh damn! MAC's been learning from us!"
                player "Super cool!"
                $ AddChatter(vig4_sc2_react_comment7)
            else: 
                $ reactImage = "stream ui/reactshocked.png"
                player "Oh no! MAC's been learning from us!"
                player "He's been picking up all the wrong things!"
                $ AddChatter(vig4_sc2_react_comment8)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc2_coilshield():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to the shield deflecting Teresa's blaster."
        "Cool!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Woah!"
            player "This old man's got some moves!"
            $ AddChatter(vig4_sc2_react_comment9)
            pause 0.5
        "Of course he's got tricks.":
            $ reactImage = "stream ui/reactconfident.png"
            player "I knew it wouldn't go over well."
            player "There's obviously more to this old guy than meets the eye."
            $ AddChatter(vig4_sc2_react_comment10)
            pause 0.5
        "Shoot him again!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Fire again Teresa!"
            player "That shield ain't limitless!"
            $ AddChatter(vig4_sc2_react_comment11)
            $ AddChatter(vig4_sc2_react_comment12)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc2_macchant():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on MAC showing up."
        "MAC for the win!":
            $ reactImage = "stream ui/reactcelebrate.png"
            #set variable for mac chant
            player "MAC coming in clutch!"
            player "MAC! MAC! MAC!"
            $ AddChatter(vig4_sc2_react_comment13)
            $ AddChatter(vig4_sc2_react_comment14)
            $ AddChatter(vig4_sc2_react_comment15)
            $ AddChatter(vig4_sc2_react_comment16)
            $ AddChatter(vig4_sc2_react_comment17)
            $ AddChatter(vig4_sc2_react_comment18)
            pause 0.5
        "MAC's got some upgrades!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Badass!"
            player "MAC's a bonafide outlaw!"
            $ AddChatter(vig4_sc2_react_comment19)
            $ AddChatter(vig4_sc2_react_comment20)
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc2_longjourney():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Talk about how hard the journey's been."
        "It's taken forever!":
            $ reactImage = "stream ui/reactconversational.png"
            player "Yeah it has been awful."
            player "Its been ages!"
            $ AddChatter(vig4_sc2_react_comment21)
            pause 0.5
        "You call that hard?":
            $ reactImage = "stream ui/reactconfident.png"
            player "Nope! Didn't notice at all."
            player "Pretty easy actually hahaha!"
            $ AddChatter(vig4_sc2_react_comment22)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc2_coilbackstory():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on Coil's backstory."
        "Interesting.":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Wow. You can tell he regrets this."
            player "Coil's got hangups about his old partner."
            $ AddChatter(vig4_sc2_react_comment23)
            pause 0.5
        "Can't side with BigCorp!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Damnit Coil!"
            player "You should've known better than to trust BigCorp!"
            $ AddChatter(vig4_sc2_react_comment24)
            $ AddChatter(vig4_sc2_react_comment25)
            #add chatter
            pause 0.5
        "Boring!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Ugh this is taking forever."
            player "Enough backstory already!"
            $ AddChatter(vig4_sc2_react_comment26)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc2_macstays():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to the Dragonflies taking MAC."
        "No way!":
            $ reactImage = "stream ui/reactshocked.png"
            player "What!? No!!"
            player "No chance we're letting that happen chat!"
            $ AddChatter(vig4_sc2_react_comment27)
            $ AddChatter(vig4_sc2_react_comment28)
            pause 0.5
        "Makes sense.":
            $ reactImage = "stream ui/reactconfident.png"
            player "I mean, I get it."
            if marshal > outlaw:
                player "Like even if we've been good, it's tough to trust ex Snakehawks."
            else: 
                player "Like we've been pretty violent and chaotic hahaha!"
            $ AddChatter(vig4_sc2_react_comment29)
            $ AddChatter(vig4_sc2_react_comment30)
            pause 0.5
        "Not fair!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "This is bogus chat!"
            player "We took all this risk and got him this far!"
            $ AddChatter(vig4_sc2_react_comment31)
            $ AddChatter(vig4_sc2_react_comment32)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

#will come back to this one later#
#label vig4_sc3_veganickname():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "What would Moze's nickname be?"
        "No way!":
            $ reactImage = "stream ui/reactshocked.png"
            player "What!? No!!"
            player "No chance we're letting that happen chat!"
            pause 0.5
        "Makes sense.":
            $ reactImage = "stream ui/reactconfident.png"
            player "I mean, I get it."
            if marshal > outlaw:
                player "Like even if we've been good, it's tough to trust ex Snakehawks."
            else: 
                player "Like we've been pretty violent and chaotic hahaha!"
            #add chatter
            pause 0.5
        "Not fair!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "This is bogus chat!"
            player "We took all this risk and got him this far!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_jenndatewin():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Jennica winning the game."
        "We never had a chance!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Shoulda known."
            player "She's the best pilot in the verse after all!"
            $ AddChatter(vig4_sc3jenn_react_comment1)
            pause 0.5
        "Damn that was close!":
            $ reactImage = "stream ui/reactunsure.png"
            player "Ahh damn!"
            player "Thought we woulda had her."
            $ AddChatter(vig4_sc3jenn_react_comment2)
            pause 0.5
        "Cute!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Jennica's so cute!"
            player "I don't even care that we lost chat!"
            $ AddChatter(vig4_sc3jenn_react_comment3)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_jenndatelose():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to beating Jennica in the game."
        "New pilot on the scene!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Move over Jenn!"
            player "Moze is taking over pilot duties!"
            $ AddChatter(vig4_sc3jenn_react_comment4)
            pause 0.5
        "That was close!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Whew!"
            player "I'm surprised we beat her! That was super close!"
            $ AddChatter(vig4_sc3jenn_react_comment5)
            pause 0.5
        "Cute!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Awww Jennica's so cute!"
            player "Best girl!"
            $ AddChatter(vig4_sc3jenn_react_comment6)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_jenndatetie():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to the game ending in a tie."
        "Not a bad result!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Getting her to a tie is pretty good in my books."
            player "Wonder if she took it easy on us!"
            $ AddChatter(vig4_sc3jenn_react_comment7)
            pause 0.5
        "Fair enough.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Makes sense."
            player "She's a way better pilot, it's a win that we tied at all!"
            $ AddChatter(vig4_sc3jenn_react_comment8)
            pause 0.5
        "Cute!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Jennica's so cute!"
            player "I love how competitive she is!"
            $ AddChatter(vig4_sc3jenn_react_comment9)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_jenndatekiss():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Kissing Jennica."
        "WOOOO!!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Finally!!"
            player "Best ship finally is canon chat!!"
            $ AddChatter(vig4_sc3jenn_react_comment10)
            $ AddChatter(vig4_sc3jenn_react_comment12)
            pause 0.5
        "Awwwww.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Awwwwww."
            player "They're perfect for each other chat!!"
            $ AddChatter(vig4_sc3jenn_react_comment11)
            $ AddChatter(vig4_sc3jenn_react_comment12)
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_jenndaterejection():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Jennica rejecting you."
        "Noooo!":
            $ reactImage = "stream ui/reactshocked.png"
            player "No!"
            player "That's brutal chat. Ooof."
            $ AddChatter(vig4_sc3jenn_react_comment13)
            pause 0.5
        "Poor Moze.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Ooooof."
            player "F's in the chat for Moze."
            $ AddChatter(vig4_sc3jenn_react_comment14)
            $ AddChatter(vig4_sc3jenn_react_comment15)
            $ AddChatter(vig4_sc3jenn_react_comment16)
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_teresadatewin():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to beating Teresa at dice."
        "Got her!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Hell yeah!"
            player "Prismari's got nothing on our girl!"
            $ AddChatter(vig4_sc3tere_react_comment1)
            $ AddChatter(vig4_sc3tere_react_comment2)
            pause 0.5
        "Game of chance after all":
            $ reactImage = "stream ui/reactconversational.png"
            player "I mean it's a game of luck right?"
            $ AddChatter(vig4_sc3tere_react_comment3)
            $ AddChatter(vig4_sc3tere_react_comment4)
            #add chatter
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_teresadatelose():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to losing to Teresa."
        "She got us!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Damn!"
            player "Prismari's got a heck of a poker face!"
            $ AddChatter(vig4_sc3tere_react_comment5)
            $ AddChatter(vig4_sc3tere_react_comment6)
            pause 0.5
        "Game of chance after all":
            $ reactImage = "stream ui/reactconversational.png"
            player "I mean it's a game of luck right?"
            $ AddChatter(vig4_sc3tere_react_comment4)
            $ AddChatter(vig4_sc3tere_react_comment3)
            #add chatter
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_teresadatekiss():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to kissing Teresa."
        "WOOOO!!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Finally!!"
            player "Best ship is finally canon!"
            $ AddChatter(vig4_sc3tere_react_comment8)
            $ AddChatter(vig4_sc3tere_react_comment10)
            pause 0.5
        "Awwwww.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Awwwww."
            player "I love them for each other!"
            $ AddChatter(vig4_sc3tere_react_comment9)
            $ AddChatter(vig4_sc3tere_react_comment10)
            #add chatter
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_teresadaterejection():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Teresa rejecting you."
        "Noooo!":
            $ reactImage = "stream ui/reactshocked.png"
            player "No!"
            player "That's brutal chat. Ooof."
            $ AddChatter(vig4_sc3jenn_react_comment13)
            pause 0.5
        "Poor Moze.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Ooooof."
            player "F's in the chat for Moze."
            $ AddChatter(vig4_sc3jenn_react_comment14)
            $ AddChatter(vig4_sc3jenn_react_comment15)
            $ AddChatter(vig4_sc3jenn_react_comment16)
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_coil1():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on Coil telling you to leave."
        "Wow brutal.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Wow that really sucks chat."
            player "All this work to get MAC here and just like that."
            player "Pushed aside."
            $ AddChatter(vig4_sc3coil1_react_comment1)
            $ AddChatter(vig4_sc3coil1_react_comment2)
            pause 0.5
        "Bullshit!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "This is bullshit chat!"
            player "All this work to get MAC here!"
            player "No way we're letting this happen!"
            $ AddChatter(vig4_sc3coil1_react_comment3)
            $ AddChatter(vig4_sc3coil1_react_comment4)
            $ AddChatter(vig4_sc3coil1_react_comment5)
            pause 0.5
        "Understandable.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Yeah I mean it makes sense."
            player "Given our reputation..."
            if marshal > outlaw:
                player "We can't expect them to trust us."
            else: 
                player "Why the heck would they trust us?"
            $ AddChatter(vig4_sc3coil1_react_comment6)
            $ AddChatter(vig4_sc3coil1_react_comment7)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_coil2():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Coil ambushing you."
        "I shoulda known!":
            $ reactImage = "stream ui/reactconversational.png"
            player "Yeah no chance they were going to leave us alone."
            player "No trust with these guys chat."
            player "Brutal."
            $ AddChatter(vig4_sc3coil2_react_comment1)
            $ AddChatter(vig4_sc3coil2_react_comment2)
            pause 0.5
        "Dammit!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Crap! They got us."
            player "Shoulda known they wouldn't trust us."
            $ AddChatter(vig4_sc3coil2_react_comment3)
            $ AddChatter(vig4_sc3coil2_react_comment4)
            pause 0.5
        "Understandable.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Yeah I didn't think they'd let us try anything."
            if marshal > outlaw:
                player "Even if we've been good."
            else: 
                player "Like why would they?"
            $ AddChatter(vig4_sc3coil2_react_comment5)
            $ AddChatter(vig4_sc3coil2_react_comment6)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_macgoodbyekind():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Talk about saying goodbye to MAC."
        "So sad.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Chat this is tragic."
            player "I'm getting choked up."
            $ AddChatter(vig4_sc3macgoodbye_react_comment1)
            $ AddChatter(vig4_sc3macgoodbye_react_comment2)
            pause 0.5
        "You're on your own now MAC.":
            $ reactImage = "stream ui/reactconversational.png"
            player "I think this is the right decision."
            player "He needs to go with them, even if its sad."
            $ AddChatter(vig4_sc3macgoodbye_react_comment3)
            $ AddChatter(vig4_sc3macgoodbye_react_comment4)
            #add chatter
            pause 0.5
        "Say nothing.":
            player "..."
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_macgoodbyerude():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Talk about saying goodbye to MAC."
        "Moze no!.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Nooo!!"
            player "How could you say that Moze!?"
            player "After all we've been through!?"
            $ AddChatter(vig4_sc3macgoodbye_react_comment9)
            $ AddChatter(vig4_sc3macgoodbye_react_comment10)
            pause 0.5
        "She's not wrong.":
            $ reactImage = "stream ui/reactunsure.png"
            player "I mean she's not wrong."
            player "All this work was to get MAC this far."
            player "No point in getting attached."
            $ AddChatter(vig4_sc3macgoodbye_react_comment11)
            $ AddChatter(vig4_sc3macgoodbye_react_comment12)
            #add chatter
            pause 0.5
        "Say nothing.":
            player "..."
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc3_machug(): # dont know if were using this one 
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to MAC's hug."
        "MAC's too pure!":
            $ reactImage = "stream ui/reactshocked.png"
            player "I'm going to cry chat."
            player "This is going to make me weep."
            pause 0.5
        "He's grown so much!":
            $ reactImage = "stream ui/reactconversational.png"
            player "Wow MAC really has learned so much!"
            player "Adorbs. Hope we get to see him again."
            #add chatter
            pause 0.5
        "Say nothing.":
            player "..."
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc4_amadealoffer():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Ama's proposition."
        "Wow quite the offer.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Holy shit chat."
            player "This is interesting."
            player "The Dragonflies suck but should we side with Ama?"
            $ AddChatter(vig4_sc4_react_comment1)
            $ AddChatter(vig4_sc4_react_comment2)
            pause 0.5
        "No way!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Side with the person who's been hunting us!?"
            player "Not a chance!"
            $ AddChatter(vig4_sc4_react_comment3)
            $ AddChatter(vig4_sc4_react_comment4)
            #add chatter
            pause 0.5
        "Hell yeah.":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Woah a chance to get even with the Dragonflies..."
            player "{i}Plus{/i} a redemption arc for Ama?"
            player "Sounds awesome!"
            $ AddChatter(vig4_sc4_react_comment5)
            $ AddChatter(vig4_sc4_react_comment6)
            $ AddChatter(vig4_sc4_react_comment7)
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc4_amaofferaccept():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on taking Ama's deal."
        "We made the right choice.":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Hell yeah!"
            player "Let's reunite the Snakehawks."
            player "And squash some Dragonflies!"
            $ AddChatter(vig4_sc4_react_comment8)
            $ AddChatter(vig4_sc4_react_comment9)
            pause 0.5
        "Maybe this was too far.":
            $ reactImage = "stream ui/reactunsure.png"
            player "I don't know about this chat."
            player "Maybe trusting Ama was the wrong move?"
            $ AddChatter(vig4_sc4_react_comment10)
            $ AddChatter(vig4_sc4_react_comment11)
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc4_amaofferrejectdefend():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on rejecting Ama's deal."
        "Time to save the galaxy!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Let's save the galaxy chat!"
            player "Polaris needs our help!"
            $ AddChatter(vig4_sc4_react_comment12)
            $ AddChatter(vig4_sc4_react_comment13)
            pause 0.5
        "Was this the right call?":
            $ reactImage = "stream ui/reactunsure.png"
            player "Are we rewarding the Dragonflies for betraying us?"
            player "I don't know about this chat."
            $ AddChatter(vig4_sc4_react_comment16)
            $ AddChatter(vig4_sc4_react_comment17)
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc4_amaofferrejectattack():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on rejecting Ama's deal."
        "We gotta save MAC!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Time to rescue MAC!"
            player "We're only loyal to our own here!"
            player "Screw the Dragonflies and screw Ama!"
            $ AddChatter(vig4_sc4_react_comment12)
            $ AddChatter(vig4_sc4_react_comment13)
            pause 0.5
        "Was this too far?":
            $ reactImage = "stream ui/reactunsure.png"
            player "I'm not sure about this chat..."
            player "We're making a {i}lot{/i} of enemies here."
            $ AddChatter(vig4_sc4_react_comment14)
            $ AddChatter(vig4_sc4_react_comment15)
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

#label vig4_sc5_oakleypicture(): might not need this one if we have one reacting to the explosion
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Talk about this flashback."
        "Wow quite the offer.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Holy shit chat."
            player "This is interesting."
            player "The Dragonflies suck but should we side with Ama?"
            pause 0.5
        "No way!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Side with the person who's been hunting us!?"
            player "Not a chance!"
            #add chatter
            pause 0.5
        "Hell yeah.":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Woah a chance to get even with the Dragonflies..."
            player "{i}Plus{/i} a redemption arc for Ama?"
            player "Sounds awesome!"
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc5_oakleydestroyed():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to the Oakley's end."
        "Noooo!":
            $ reactImage = "stream ui/reactshocked.png"
            player "Noooo!."
            player "Chat our ship is destroyed!"
            $ AddChatter(vig4_sc5_react_comment1)
            $ AddChatter(vig4_sc5_react_comment2)
            pause 0.5
        "Fitting.":
            $ reactImage = "stream ui/reactconversational.png"
            player "There's no going back now."
            player "Time to press on!"
            $ AddChatter(vig4_sc5_react_comment3)
            $ AddChatter(vig4_sc5_react_comment4)
            pause 0.5
        "Say nothing":
            player "..."
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc5_amashowsup():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Talk about Ama's entrance."
        "Badass!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Wooooooo!"
            player "Ama's on the scene!"
            player "Snakehawks reunion!"
            $ AddChatter(vig4_sc5_react_comment5)
            $ AddChatter(vig4_sc5_react_comment6)
            $ AddChatter(vig4_sc5_react_comment7)
            pause 0.5
        "Not sure about this still.":
            $ reactImage = "stream ui/reactunsure.png"
            player "I'm still not so sure about this."
            player "I wonder if we can change our mind later."
            $ AddChatter(vig4_sc5_react_comment8)
            $ AddChatter(vig4_sc5_react_comment9)
            pause 0.5
        "Say nothing.":
            player "..."
            #add chatter
            pause 0.5
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