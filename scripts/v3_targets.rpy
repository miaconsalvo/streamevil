###This script contains targets that the comments and reactions can direct to in Vignette 3

### streamer react moments###

label vig3_sc1_out():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Teresa's upset."
        "Wow it's weighing heavily on her.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Wow, crazy to see it weighing so heavily on Teresa!"
            player "She's usually so stoic!"
            $ AddChatter(vig3_sc1_out_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc1_out_react_comment2)
            pause 0.5
        "Brutal!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Hate to see the crew fighting." 
            $ AddChatter(vig3_sc1_out_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc1_out_react_comment3)
            pause 0.5
        "This is what she wanted.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Wasn't Teresa the one saying we needed to do this?"
            player "C'mon girl, this is what you wanted!"
            $ AddChatter(vig3_sc1_out_react_comment2)
            pause 0.5
            $ AddChatter(vig3_sc1_out_react_comment4)
            pause 0.5
            $ AddChatter(vig3_sc1_out_react_comment5)
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc1_mar():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Jennica's upset."
        "It was always risky.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Damn it's weighing heavily on her."
            player "Definitely was risky."
            $ AddChatter(vig3_sc1_mar_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc1_mar_react_comment2)
            pause 0.5
            $ AddChatter(vig3_sc1_mar_react_comment3)
            pause 0.5
        "They're fighting!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Hate to see the crew fighting." 
            $ AddChatter(vig3_sc1_mar_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc1_mar_react_comment4)
            pause 0.5
        "This is what she wanted.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Wasn't Jennica saying this was what we needed to do?"
            player "C'mon girl this is what you wanted!"
            $ AddChatter(vig3_sc1_mar_react_comment5)
            pause 0.5
            $ AddChatter(vig3_sc1_mar_react_comment6)
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc2_macdad(): #I commented this out of the main game script. MAC references Vanas as his father in episode 1, this wouldn't be a surprise.
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Comment on MAC's dad."
        "MAC has a dad!?":
            $ reactImage = "stream ui/reactshocked.png"
            player "Did he just say \"Dad\"?."
            player "Holy shit things getting crazy!"
            pause 0.5
        "Interesting!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Cool!"
            player "MAC's Dad must be that scientist or someone!"
            player "The plot thickens."
            #add chatter
            pause 0.5
        "Predictable!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Of course we're gonna meet the guy who made MAC."
            player "Hahaha how convenient!"
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc3_maccandy():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "MAC's like a kid who just wants candy."
        #"Talk about MAC's naivete."
        "MAC is so innocent!":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactshocked.png"
            player "Wow MAC is too innocent for this world!"
            $ AddChatter(vig3_sc2_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc2_react_comment2)
            pause 0.5
            $ AddChatter(vig3_sc2_react_comment3)
            pause 0.5
        "Watch out MAC!":
            $ reactImage = "stream ui/reactthinking.png"
            player "Oh god, MAC's gonna get in trouble!"
            player "He's so out of his element!"
            $ AddChatter(vig3_sc2_react_comment3)
            pause 0.5
            $ AddChatter(vig3_sc2_react_comment4)
            pause 0.5
        "This will end badly hahaha!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Oh god, MAC's gonna be a problem here."
            player "We're about to get scammed!"
            $ AddChatter(vig3_sc2_react_comment5)
            pause 0.5
            $ AddChatter(vig3_sc2_react_comment4)
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc3_firstfight():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"React to the fight."
        "The crew is stirring up a bit of trouble."
        "Wow badass!":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Holy smokes look at them go!"
            player "Jenn and Resa kicking butt!"
            $ AddChatter(vig3_sc3_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc3_react_comment3)
        "Bit of an overreaction.":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactunsure.png"
            player "Well that seemed uneccesary!"
            player "Not saying that he wasn't gross, but still!"
            $ AddChatter(vig3_sc3_react_comment5)
            pause 0.5
            $ AddChatter(vig3_sc3_react_comment4)
            pause 0.5
        "This will come back around.":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactconversational.png"
            player "We really shouldn't be antagonizing people."
            player "This is going to come back to bite us!"
            $ firstfightprediction == True
            $ AddChatter(vig3_sc3_react_comment5)
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc4_houndraid():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"React to the raid."
        "These troublemakers are shaking down Rec's shop."
        "Told you!" if firstfightprediction == True:
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "I knew it!"
            player "See chat! I knew they would be back!"
            $ AddChatter(vig3_sc4_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc4_react_comment2)
        "They better not take the antenna.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Oh no! They're going to take the part we need!"
            #player "Things bout to get complicated!" #Think this is better with just the one line
            $ AddChatter(vig3_sc4_react_comment3)
            pause 0.5
        "Let's fight 'em!":
            $ reactImage = "stream ui/reactthumbsup.png"
            #player "We can take 'em!" #similar as above, I think one line is stronger here.
            player "Let's rumble. They ain't so tough!"
            $ AddChatter(vig3_sc4_react_comment5)
            pause 0.5
            $ AddChatter(vig3_sc4_react_comment4)
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc5_amahallu():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Moze's paranoia is getting pretty intense."
        "Damn Moze is flipping out.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Moze is pulling guns on showgirls!"
            player "She's seeing ghosts!"
            $ AddChatter(vig3_sc5_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc5_react_comment2)
            pause 0.5
            $ AddChatter(vig3_sc5_react_comment3)
        "That's the second time now!":
            $ reactImage = "stream ui/reactunsure.png"
            player "This is the second time!"
            player "Chat, Moze is shook!"
            player "Talk about paranoia."
            $ AddChatter(vig3_sc5_react_comment2)
            pause 0.5
        "Spooky!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Damn, it's hard to know if we're actually being tailed!"
            player "Chat I'm spooked!"
            $ AddChatter(vig3_sc5_react_comment4)
            pause 0.5
            $ AddChatter(vig3_sc5_react_comment5)
            pause 0.5
            $ AddChatter(vig3_sc5_react_comment6)
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc6_crewspat():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "The crew's mad at each other."
        "They're at each other's throats.":
            $ reactImage = "stream ui/reactconfident.png"
            #player "Oh damn! The girls are angry!"
            player "Oh damn, this isn't like normal banter."
            player "They're throwing some serious shade!"
            $ AddChatter(vig3_sc6_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment2)
            pause 0.5
        "Jennica's so protective of MAC.":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactshocked.png"
            player "Awww, Jennica doesn't want MAC to hear the bad words!"
            player "Cute!"
            $ AddChatter(vig3_sc6_react_comment3)
            pause 0.5
        "Relax Jennica, he's a bot.":
            $ kcEngagement -= 1 
            $ reactImage = "stream ui/reactconversational.png"
            player "I mean he's just a robot."
            player "C'mon now, his database definitely has worse, no?"
            $ AddChatter(vig3_sc6_react_comment4)
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc6_stranger():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Moze is following a stranger."
        "Moze is super paranoid.":
            $ reactImage = "stream ui/reactunsure.png"
            player "Damn Moze is following strangers now!"
            player "I don't like the looks of this!"
            $ AddChatter(vig3_sc6_react_comment5)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment6)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment7)
        "This seems dangerous.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Oh god, this is going to go badly!"
            player "What you doing Moze!"
            $ AddChatter(vig3_sc6_react_comment8)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment5)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment9)
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc6_recbonding():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Rec is opening up."
        "Rec is cool!":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Rec is so cool!"
            player "Really love their character!"
            $ AddChatter(vig3_sc6_react_comment10)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment18)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment19)
        "Rec is cute!":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Rec is so cute!"
            player "Really love their design!"
            $ AddChatter(vig3_sc6_react_comment10)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment15)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment16)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment17)
        "Damn I'm guilty.":
            $ kcEngagement += 1
            $ csEngagement += 1
            $ pdEngagement -= 1
            $ reactImage = "stream ui/reactshocked.png"
            player "Rec is so cool! But every time I think that, I remember we killed their brother."
            player "So much guilt!"
            $ AddChatter(vig3_sc6_react_comment10)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment11)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment12)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment13)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment14)
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc6_shipbet1():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Did they actually bet the ship on this game?"
        "Classic Jenn and Resa.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Oh damn! Bit of an overbet!"
            player "Now we gotta win!"
            $ AddChatter(vig3_sc6_react_comment21)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment20)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment22)
        "What the hell!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Holy smokes!"
            player "Now we gotta win!"
            $ AddChatter(vig3_sc6_react_comment20)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment23)
            pause 0.5
        "I don't buy it.":
            $ reactImage = "stream ui/reactunsure.png"
            player "Naw chat. I'm calling cap on this."
            player "They're reckless but not like that."
            $ shipbetprediction == True
            $ AddChatter(vig3_sc6_react_comment24)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment25)
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc6_trustcrew():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"Comment on Moze trusting her crew and not cheating."
        "You chose to trust your crew and not cheat anymore."
        "Got to have integrity.":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactthumbsup.png"
            player "They got themselves into this mess."
            player "They'll have to get themselves out of it!"
            $ AddChatter(vig3_sc6_react_comment26)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment27)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment28)
            pause 0.5
        "I trust Jennica and Teresa.":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthinking.png"
            player "Trust the crew!"
            player "Jenn and Resa got this!"
            $ AddChatter(vig3_sc6_react_comment29)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment30)
            pause 0.5
        "Oh no I hope they win!":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactshocked.png"
            player "Crap this there's a lot riding on this!"
            player "Was this a mistake?"
            $ AddChatter(vig3_sc6_react_comment27)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment29)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment30)
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc6_shootingzan():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You chose to cheat by shooting Zan in the leg."
        "Blast em!":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Get blasted Zan!"
            $ AddChatter(vig3_sc6_react_comment31)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment32)
            pause 0.5
        "Wow crazy!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Woah that was awesome!"
            player "Crazy!"
            $ AddChatter(vig3_sc6_react_comment33)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment34)
            pause 0.5
        "That was cheating!":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Damn, feels weird that we had to cheat to win."
            $ AddChatter(vig3_sc6_react_comment35)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment36)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment37)
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc6_shipbet2():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Turns out, the crew didn't actually bet the ship."
        "What a relief.":
            $ reactImage = "stream ui/reactunsure.png"
            player "Phew. That's a relief"
            player "That could've been bad!"
            $ AddChatter(vig3_sc6_react_comment38)
            pause 0.5
        "I knew it!" if shipbetprediction == True:
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "I called it chat!"
            player "No way they'd bet the ship!"
            $ AddChatter(vig3_sc6_react_comment39)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment40)
            pause 0.5
        "Wow cop out.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Hahaha"
            player "Of course they didn't bet the ship."
            player "What a cop out."
            $ AddChatter(vig3_sc6_react_comment41)
            pause 0.5
            $ AddChatter(vig3_sc6_react_comment42)
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc7_lostmac():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"React to losing MAC."
        "MAC got taken by the Hounds!"
        "Oh no!":
            $ reactImage = "stream ui/reactshocked.png"
            player "MAC!"
            player "Nooooo!"
            $ AddChatter(vig3_sc7_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc7_react_comment2)
            pause 0.5
        "The plot thickens.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Oh damn, did not expect that to happen."
            player "Things are getting complicated on Solara!"
            $ AddChatter(vig3_sc7_react_comment3)
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc8_teresabluff():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"Comment on Teresa's bluff."
        "Teresa just bluffed our way into the Inventor's Fair."
        "Teresa's in her element.":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Wow, Teresa knows her way around high society."
            $ AddChatter(vig3_sc8_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc8_react_comment2)
            pause 0.5
        "How lucky.":
            $ reactImage = "stream ui/reactconversational.png"
            #player "Wow."
            player "We're lucky Teresa was here."
            $ AddChatter(vig3_sc8_react_comment3)
            pause 0.5
        "This is boring.": #maybe have this only if you stealthed into the commsbase in vig2 or maybe different based on vig2
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Jeez. More stealth?"
            player "Really seems like that's always an option."
            player "Wish we could go loud!"
            $ AddChatter(vig3_sc8_react_comment4)
            pause 0.5
            $ AddChatter(vig3_sc8_react_comment5)
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc9_daisyreturns():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"Say something about Daisy."
        "We met up with Daisy at the Inventor's Fair."
        "She's back!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Daisy returns!"
            player "Love it! She's the realest person in this room."
            $ AddChatter(vig3_sc9_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc9_react_comment2)
        "Maybe she's following us?":
            $ reactImage = "stream ui/reactthinking.png"
            player "Oh damn! Maybe she was following us?"
            player "Pretty sus chat."
            $ bacon8r_6
            $ AddChatter(vig3_sc9_react_comment3)
            pause 0.5
            $ AddChatter(vig3_sc9_react_comment4)
            pause 0.5
            $ AddChatter(vig3_sc9_react_comment5)
        "Cute!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "She's so cute!"
            player "I love her design!"
            $ AddChatter(vig3_sc9_react_comment6)
            pause 0.5
            $ AddChatter(vig3_sc9_react_comment7)
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc9_daisybar():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"Say something about Daisy."
        "We met up with Daisy at the Inventor's Fair."
        "Maybe there was a better way of handling this...":
            $ reactImage = "stream ui/reactthinking.png"
            player "Idk chat, maybe there was a better way of handling this..."
            $ AddChatter(vig3_sc9_react_comment18)
            pause 0.5
        "Get him!" if vig3_daisyChoice == 1:
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Yeah, Mills! What are you gonna do about it?"
            $ AddChatter(vig3_sc9_react_comment13)
            pause 0.5
            $ AddChatter(vig3_sc9_react_comment14)
            pause 0.5
        "Get him!" if vig3_daisyChoice == 2:
            $ reactImage = "stream ui/reactcelebrate.png"
            player "And what are you gonna do about it, Mills?"
            $ AddChatter(vig3_sc9_react_comment13)
            pause 0.5
            $ AddChatter(vig3_sc9_react_comment16)
            pause 0.5
            $ AddChatter(vig3_sc9_react_comment17)
            pause 0.5
        "Don't want to attract attention." if vig3_daisyChoice == 3:
            $ reactImage = "stream ui/reactthinking.png"
            player "I want to mess with him so bad."
            player "But we can't take the risk."
            $ AddChatter(vig3_sc9_react_comment15)
            pause 0.5
            $ AddChatter(vig3_sc9_react_comment16)
        "Say nothing.":
            pass
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc9_amasurprise():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"React to Ama."
        "Ama found Moze!"
        "Oh no!":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactshocked.png"
            player "This is bad!"
            player "This is really bad!"
            $ AddChatter(vig3_sc9_react_comment8)
            pause 0.5
            $ AddChatter(vig3_sc9_react_comment9)
            pause 0.5
        "Not so paranoid after all!":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthinking.png"
            player "Oh wow, guess Moze wasn't being paranoid after all!"
            $ AddChatter(vig3_sc9_react_comment10)
            pause 0.5
        "It's go time.":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Oh it's time to rumble."
            player "Let's get loud!"
            $ AddChatter(vig3_sc9_react_comment11)
            pause 0.5
            $ AddChatter(vig3_sc9_react_comment12)
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc11_amabacksass():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"Comment on Moze and Ama's insults."
        "The back and forth between Moze and Ama is tense."
        "Burn Ama!":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            #player "Damn Ama!"
            player "Get roasted, Ama!"
            $ AddChatter(vig3_sc11_react_comment1)
            pause 0.5
        "Love this sass.":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Feel like they haven't missed a step!"
            player "Just like old times hahaha!"
            $ AddChatter(vig3_sc11_react_comment2)
            pause 0.5
            $ AddChatter(vig3_sc11_react_comment3)
            pause 0.5
        "Let them fight!":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Boo. Let me fight."
            player "She's got a whole lot coming to her."
            $ AddChatter(vig3_sc11_react_comment4)
            pause 0.5
            $ AddChatter(vig3_sc11_react_comment5)
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc12_amachoke():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"Comment on Ama's workplace relations."
        "Ama's choking the BigCorp representative."
        "Don't mess with Ama.":
            $ reactImage = "stream ui/reactshocked.png"
            #player "Damn!"
            player "Good reminder: do not piss off Ama."
            $ AddChatter(vig3_sc12_react_comment1)
            pause 0.5
            $ AddChatter(vig3_sc12_react_comment3)
            pause 0.5
            $ AddChatter(vig3_sc12_react_comment4)
            pause 0.5
            $ AddChatter(vig3_sc12_react_comment5)
        "Better call HR!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Better file an HR report!"
            player "Terrible workplace conduct from Ama!"
            $ AddChatter(vig3_sc12_react_comment2)
            pause 0.5
        "Say nothing.":
            pass
            #$ reactImage = "stream ui/reactthinking.png"
            #player "Could have been worse."
            #player "This guy was asking for trouble!"
            #pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc12_amafindsout():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"Ama knows that it's the real MAC!"
        "Ama realized that's the real MAC!"
        "The jig is up!":
            $ reactImage = "stream ui/reactshocked.png"
            player "This is really bad!"
            player "Ama figured it out!"
            pause 0.5
        "Time to fight!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Finally time for some battle!"
            player "Don't get between Mozely and our MAC!"
            #add chatter
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc12_macalignment_violencepessimism():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "MAC shot Ama!"
        "MAC's a badass!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Wow he shot her!"
            player "Zero hesitation! Ice cold!"
            player "MAC for the win! Crack shot!"
            pause 0.5
        "MAC, no!":
            $ reactImage = "stream ui/reactshocked.png"
            player "Noooo!"
            player "MAC you're supposed to be better than us!"
            #add chatter
            pause 0.5
        "Is this because of our choices?":
            $ reactImage = "stream ui/reactthinking.png"
            player "What!?"
            player "Has MAC been learning this whole time?"
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc12_macalignment_violenceoptimism():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "MAC almost shot Ama!"
        "MAC's a badass!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Damn! MAC's a crack shot!"
            player "Zero hesitation! Warning shot right a hair away from her face!"
            player "So cool!"
            pause 0.5
        "So much for MAC's innocence.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Did MAC just fire a warning shot a hair away from her face?"
            player "Damn MAC, you're supposed to be better..."
            #add chatter
            pause 0.5
        "Is this because of our choices?":
            $ reactImage = "stream ui/reactthinking.png"
            player "What!?"
            player "Has MAC been learning this whole time?"
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc12_macalignment_peacepessimism():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "MAC just tried to intimidate Ama!"
        "Good thing Moze is here!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "MAC with the distraction!"
            player "Good thing Moze is here to take advantage though!"
            pause 0.5
        "MAC is so innocent!":
            $ reactImage = "stream ui/reactshocked.png"
            player "Oh MAC!"
            player "Too pure for this world!"
            #add chatter
            pause 0.5
        "Is this because of our choices?":
            $ reactImage = "stream ui/reactthinking.png"
            player "What!?"
            player "Has MAC been learning this whole time?"
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc12_macalignment_peaceoptimism():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "MAC just read Ama perfectly!"
        "Did MAC just do that?":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "What!?"
            player "Did MAC just hard read Ama!?"
            player "She's a softie underneath it all!"
            pause 0.5
        "Mac for the win!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Did MAC just grow up!?"
            player "Like he just saw right through Ama!"
            #player "What is going on!?"
            #add chatter
            pause 0.5
        "Is this because of our choices?":
            $ reactImage = "stream ui/reactthinking.png"
            player "What!?"
            player "Has MAC been learning this whole time?"
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc14_recfindsout_regret():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"React to Moze's confession."
        "Moze confessed to Rec that she killed Allistar."
        "Finally coming clean.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Wow. Brutal."
            player "But at least she's finally telling Rec."
            pause 0.5
        "Sorry, Rec.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Noooo!"
            player "This is so sad chat."
            #add chatter
            pause 0.5
        "Sorry, not sorry.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "I guess it was the right thing to do."
            player "Not sure we should be apologizing though."
        "Say nothing.":
            player "..."
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc14_recfindsout_ihadto():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"React to Moze's confession."
        "Moze confessed to Rec that she killed Allistar."
        "Damn right.":
            $ reactImage = "stream ui/reactunsure.png"
            player "I mean she's right. Allistar betrayed them."
            player "What do you expect?"
            #add chatter
            pause 0.5
        "Moze with the cop out!":
            $ reactImage = "stream ui/reactconfident.png"
            player "\"I had no choice!\""
            player "Classic Moze!"
            player "We never have any choice hahahaha!"
            pause 0.5
        "Sorry, not sorry.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Yeah, I guess that was the right thing to do."
            player "They shouldn't expect an apology though. Allistar crossed us!"
        "Say nothing.":
            player "..."
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig3_sc14_recfindsout_noremorse():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        #"React to Moze's admission."
        "Moze confessed to Rec that she killed Allistar."
        "No remorse!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Hell yeah!"
            player "Allistar deserved it! No regrets."
            pause 0.5
        "That was cold.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Wow maybe that was too far?"
            player "Even if Allistar deserved it..."
            player "Might've been too cruel."
            #add chatter
            pause 0.5
        "Hahaha get owned Rec!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Hahahaha!"
            player "f's in the chat for Rec!"
            player "Traitor brother got what he deserved."
            #add chatter #many f's 
        "Say nothing.":
            player "..."
            pause 0.5
    if commentVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

### Mid-Stream Break Chat Responses ###
label vig3break_crash10():
    $ macroChoice = True
    $ vig3break_crash_comment10.click = False
    $ narrator = reg_narrator
    menu:
        "So do you think this was intentional?"
        "I hope not, I hate those games!":
            player "Oh please no."
            player "The last thing I need is a survival horror in the last half."
        "No way.":
            player "I don't think they're going for that."
            player "Now if it was Matticus I would believe it a bit more."            
        "I don't know.":
            player "Hmm. Honestly, idk."
            player "But we'll find out soon I'm sure."
    $ macroChoice = True
    if macroChoice == False: 
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3break_brb12():
    $ macroChoice = True
    $ vig3break_brb_comment12.click = False
    $ narrator = reg_narrator
    menu:
        "How's your progress?"
        "It's gonna be a while...":
            player "It's gonna be a while."
            player "But that gives us more time to chat!"
            player "It's great to see all the new faces."
        "Rough for sure.":
            player "It's rough out here."
            player "But it's also been rough for the Oakley."
            player "Maybe they can also use the break."           
    $ macroChoice = True
    if macroChoice == False: 
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3break_take7():
    $ macroChoice = True
    $ vig3break_ama_take_comment7.click = False
    $ narrator = reg_narrator
    menu:
        "Do you think you can escape Ama again?"
        "There's always a way out!":
            player "We've been in binds before."
            player "I think we got this one!"
            player "We're not leaving without MAC."
        "Not without serious force.":
            player "Ama is not gonna let us go easily."
            player "We'll probably need to ifght our way out."
            player "Gotta do it for MAC."          
    $ macroChoice = True
    if macroChoice == False: 
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3break_take10():
    $ macroChoice = True
    $ vig3break_ama_take_comment10.click = False
    $ narrator = reg_narrator
    menu:
        "What do you think about the new locations?"
        "Hot take but I love Gibian V":
            player "Gibian V has that true western vibe."
            player "Even Matticus' fortress was amazing."
            player "It really kicked off the game in the best way."
        "Akar is the place to be!":
            player "It's gonna hard to top Akar."
            player "The rework is incredible!"
            player "Gotta love the Snakehawks unofficial HQ."  
            player "Also the best music so far."
        "The next ones will be even better.": 
            player "We've seen some great spots."
            player "But some teasers leaked for the next chapter and HOOOO"
            player "I can tell that's gonna be my fave."          
    $ macroChoice = True
    if macroChoice == False: 
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3break_kiss10():
    $ macroChoice = True
    $ vig3break_ama_kiss_comment10.click = False
    $ narrator = reg_narrator
    menu:
        "How do you feel about Outlaw MAC"
        "MAC's learning from the best":
            player "The Oakley are the best in the buisness."
            player "The world's first robot Outlaw!"
            player "He just needs a little hat."
        "MAC is for something bigger than Outlaw life":
            player "We're not supposed to make him an Outlaw."
            player "We're sending him to the Dragonflies."
            player "Plus he's just a little guy."          
    $ macroChoice = True
    if macroChoice == False: 
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

#label vig3break_dead4():

label vig3break_dead11():
    $ macroChoice = True
    $ vig3break_ama_dead_comment11.click = False
    $ narrator = reg_narrator
    menu:
        "How'do you feel about the other Snakehawks?"
        "It feels nostalgic":
            player "It's nice to see them all again."
            player "Even if it's under stressful circumstance."
            player "And you know..."
            player "We killed one."
        "I prefer the newer characters":
            player "Seeing everyone is nice"
            player "But it's better to meet the newer folks."
            player "I think they make the sotry more interesting."           
    $ macroChoice = True
    if macroChoice == False: 
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3break_tense4():
    $ macroChoice = True
    $ vig3break_rec_tense_comment4.click = False
    $ narrator = reg_narrator
    menu:
        "Are you Outlaws?"
        "We're a different kind of Outlaw":
            player "I think the Oakley is trying to be a different kind of Outlaw."
            player "The SnakeHawks had a different code."
            player "We have an important goal now."
        "We are!":
            player "Hundred percent."
            player "We do what we need to."
            player "At any cost."           
    $ macroChoice = True
    if macroChoice == False: 
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3break_tense10():
    $ macroChoice = True
    $ vig3break_rec_tense_comment10.click = False
    $ narrator = reg_narrator
    menu:
        "How do you even respond to that."
        "I hope you're joking.":
            player "I'm going to assume that's a joke."
            player "But I appreciate the energy!."
        "When it's narratively relevant.":
            player "Narrative relevant scarring is important."
            player "Cornerstone to a good story."
        "Scarring is a consequence.":
            player "We do what we do."
            player "Potential scarring may occur."
            player "That's how it goes."          
    $ macroChoice = True
    if macroChoice == False: 
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3break_reunion3():
    $ macroChoice = True
    $ vig3break_rec_reunion_comment3.click = False
    $ narrator = reg_narrator
    menu:
        "How do you feel about Rec and Allistar's lost reunion."
        "That's just what happens.":
            player "It's a part of life."
            player "That could've happened even without our intervention."
            player "It'd be the same thing."
        "I know the feeling.":
            player "I know..."
            player "It's hard being away from a sibling for that long."
            player "Especially when you can't even talk to them."      
    $ macroChoice = True
    if macroChoice == False: 
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3break_reunion9():
    $ macroChoice = True
    $ vig3break_rec_reunion_comment9.click = False
    $ narrator = reg_narrator
    menu:
        "What about an Ama romance?"
        "I'd do anything!":
            player "I really want that to happen."
            player "That would be so awesome if we could."
            player "Probably need to survive first."
        "I'd rather someone else.":
            player "I don't know..."
            player "Doesn't feel like the natural thing for their relationship."
            player "I'd rather someone else."      
    $ macroChoice = True
    if macroChoice == False: 
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3break_end5():

#####MACRO GAME TARGETS FOR FLINCH #######
label vig3_analytics_topfan():
    hide screen viewershipButton_vig3
    $ flinchCheck += 1
    $ flinch_topfanCheck = True
    if topfan == "Coriolis":
        "Coriolis's steady presence in the chat has been a consistent reassurance."
        "They're never going to say the most outrageous thing or get the chat rolling with laughter."
        "But they'll always be a welcoming voice. Every chat needs that."
    elif topfan == "kitcat":
        "kitcat has really gotten comfortable in the chat."
        "It's nice to have someone who's less didactic about \"Marshal\" this or \"Outlaw\" that."
        "For them, it's all about MAC. And maybe that's more reflective of Moze's view than anyone else's."
    elif topfan == "pickledDragons":
        "pickledDragons brings so much energy to the chat it's remarkable."
        "It feels like whenever chat pops off, they're there inciting more activity."
        "Every chat needs someone who's making sure that people are having fun."        
    else:
        "Coriolis's steady presence in the chat has been a consistent reassurance."
        "They're never going to say the most outrageous thing or get the chat rolling with laughter."
        "But they'll always be a welcoming voice. Every chat needs that."
    if flinchCheck >= 3:
        $ screenComplete = True
    else:
        pass
    show screen viewershipButton_vig3
    return

label vig3_analytics_audience():
    hide screen viewershipButton_vig3
    $ flinchCheck += 1
    $ flinch_audienceCheck = True
    if viewershipHigh == True:
        "We made it! 50 Followers!"
        "That means you won't have to collect any new follows for the last stream."
        "But you'll still have to keep the average viewership number above ten."
        "After all the people watching this week though, that shouldn't be an issue."
        "Cross your fingers."
    else:
        "49 followers? You're one away!"
        "You were hoping to cross that threshold already, but at least you're close."
        "It shouldn't be too much of an issue. You just need to grab one extra follow by the end of the next stream."
        "That should be doable."
        "You'll also have to keep the average viewership over 10."
        "This week was a little close for comfort. Hopefully next week will be stable."
        "Cross your fingers."
    if flinchCheck >= 3:
        $ screenComplete = True
    else:
        pass
    show screen viewershipButton_vig3
    return

label vig3_analytics_viewcount():
    $ flinchCheck += 1
    $ flinch_viewcountCheck = True
    hide screen viewershipButton_vig3
    if viewershipHigh == True:
        "The viewership numbers for this week are up compared to last week."
        "That's a good sign!"
    else:
        "The viewership numbers for this week are similar to last week."
        "That's not bad, but it's a bit disappointing that they didn't grow at all."
    "Hopefully next week will keep up the average viewership."
    jump vig3_analytics_viewcount2

label vig3_analytics_viewcount2():
    menu:
        "Hopefully next week will keep up the average viewership."
        "The crash didn't hurt viewership too much." if flinchViewershipCrash == False:
            $ flinchViewershipCrash = True
            "It's kind of crazy that the crash didn't have a bigger impact on viewership numbers."
            "Some people did leave, but the chat was still very active after you got back on track."
            "Maybe Jessie was right and you did handle it pretty well."
            jump vig3_analytics_viewcount2
        "It's barely enough to make Affiliate." if viewershipLow == True and flinchViewershipAffiliate == False:
            $ flinchViewershipAffiliate = True
            $ vig3_viewership = "Low"
            "The viewership is stable, but it's barely enough to make Affiliate."
            "There's basically no margin for losing anyone."
            "If the numbers drop for the last episode..."
            "You don't really want to think about it."
            jump vig3_analytics_viewcount2
        "It looks like Affiliate's in the bag!" if viewershipHigh == True and flinchViewershipAffiliate == False:
            $ flinchViewershipAffiliate = True
            $ vig3_viewership = "High"
            "The viewership is stable and looks comfortably above the Affiliate requirement."
            "You won't know for certain until after the last stream, but the calculations are looking good."
            "Average viewership is well above 10 per stream, so as long as something drastic doesn't happen at the end, it looks like you're good."
            "Cross your fingers."
            jump vig3_analytics_viewcount2
        "Playing with chat is interesting." if flinchViewershipChat == False:
            $ flinchViewershipChat = True
            "Playing this game along with the chat is interesting."
            "You're hearing about so many people's perspectives on the choices before you even make them."
            "How does it feel?"
            menu:
                "How does it feel?"
                "It's fun!":
                    "It's a lot of fun!"
                    "Chat is so interactive. It really feels like you're playing this game together."
                "It's a lot of pressure.":
                    "It's a lot of pressure."
                    "Not bad, necessarily. But you feel like you have to represent other people's interests as well as your own."
                "I don't really like it.":
                    "You don't really like it."
                    "It is interesting, but you don't see yourself streaming this kind of game again."
                "Interesting.":
                    "It's just interesting."
                    "It doesn't feel bad, but it's also not as fun as you might've expected."
                    "It feels like a different way to play games."
            jump vig3_analytics_viewcount2
        "Go back to the main Flinch page" if flinchViewershipAffiliate == True:
            if flinchCheck >= 3:
                $ screenComplete = True
            else:
                pass
            show screen viewershipButton_vig3
            return
    return

######MACRO GAME TARGETS FOR BLUEIT ########


label vig3_blueit_amaThread():
    $ screenComplete = False
    $ blueitImage = "socials/v3_amaRomance.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig3_blueit_fairThread():
    $ screenComplete = False
    $ blueitImage = "socials/v3_inventorsFair.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig3_blueit_recThread():
    $ screenComplete = False
    $ blueitImage = "socials/v3_reccrin.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig3_blueit_favStreamThread():
    $ screenComplete = False
    $ blueitImage = "socials/v3_favoriteStreamers.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig3_blueit_formalThread():
    $ screenComplete = False
    $ blueitImage = "socials/v3_formalWear.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig3_blueit_dflyThread():
    $ screenComplete = False
    $ blueitImage = "socials/v3_dragonflies.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return
        





