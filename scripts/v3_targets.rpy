###This script contains targets that the comments and reactions can direct to in Vignette 3



### streamer react moments###

label vig3_sc1_out():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Teresa's upset."
        "Wow it's weighing heavily on her.":
            player "Wow it's crazy to see it weighing so heavily on Teresa!"
            player "She's usually so stoic!"
            pause 0.5
        "Brutal!":
            player "The girls are fighting!!" 
            #$ AddChatter(vig2_sc1_reactcomment1)
            pause 0.5
        "This is what she wanted.":
            player "Wasn't Teresa the one saying we needed to do this?"
            player "C'mon girl this is what you wanted!"
            #$ AddChatter(vig2_sc1_reactcomment2)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc1_mar():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Jennica's upset."
        "It was always risky":
            player "Damn it's weighing heavily on her."
            player "Definitely was risky."
            pause 0.5
        "They're fighting!":
            player "Oh damn the girls are fighting!"
            #add chatter
            pause 0.5
        "This is what she wanted.":
            player "Wasn't Jennica saying this was what we needed to do?"
            player "C'mon girl this is what you wanted!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc2_macdad():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on MAC's dad."
        "MAC has a dad!?":
            player "Did he just say \"Dad\"?."
            player "Holy shit things getting crazy!"
            pause 0.5
        "Interesting!":
            player "Cool!"
            player "MAC's Dad must be that scientist or someone!"
            player "The plot thickens."
            #add chatter
            pause 0.5
        "Predictable!":
            player "Of course we're gonna meet the guy who made MAC."
            player "Hahaha how convenient!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc3_maccandy():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Talk about MAC's naivete."
        "MAC is so innocent!":
            player "Wow MAC is too innocent."
            player "Too pure for this world!"
            pause 0.5
        "Watch out MAC!":
            player "Oh god MAC's gonna get in trouble!"
            player "He's so out of his element!"
            #add chatter
            pause 0.5
        "This will end badly hahaha!":
            player "Oh God"
            player "MAC's gonna be a problem here."
            player "We're about to get scammed!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc3_firstfight():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to the fight."
        "Wow badass!":
            player "Holy smokes look at them go!"
            player "Jenn and Resa kicking butt!"
            pause 0.5
        "Bit of an overreaction.":
            player "Well that seemed uneccesary!"
            player "Not saying that he wasn't gross but still!"
            #add chatter
            pause 0.5
        "This will come back around.":
            player "We really shouldn't be antagonizing people."
            player "This is going to come back to bite us!"
            $ firstfightprediction == True
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc4_houndraid():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to the raid."
        "Told you!" if firstfightprediction == True:
            player "I knew it!"
            player "See chat! I knew they would be back!"
            pause 0.5
        "They better not take the antenna.":
            player "Oh no! They're going to take the part we need!"
            player "Things bout to get complicated!"
            #add chatter
            pause 0.5
        "Let's fight em!":
            player "We can take em!"
            player "Let's rumble. They ain't so tough!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc5_amahallu():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Talk about Moze's paranoia."
        "Damn Moze is flipping out.":
            player "Moze is pulling guns on showgirls!"
            player "She's seeing ghosts!"
            pause 0.5
        "Damn that's the second time now!":
            player "This is the second time!"
            player "Chat Moze is shook!"
            player "Talk about paranoia!"
            #add chatter
            pause 0.5
        "Spooky!":
            player "Damn it's hard to know if we're actually being tailed!"
            player "Chat I'm spooked!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return








        





