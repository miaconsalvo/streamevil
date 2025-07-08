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

label vig3_sc6_crewspat():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "The crew's mad at each other."
        "They're at each other's throats.":
            player "Oh damn! The girls are angry!"
            player "Some serious shade getting thrown!"
            pause 0.5
        "Jennica's so protective of MAC.":
            player "Awww. Jennica doesn't want MAC to hear the bad words!"
            player "Cute!"
            #add chatter
            pause 0.5
        "Relax Jennica, he's a bot.":
            player "I mean he's just a robot."
            player "C'mon now, his database def has worse no?"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc6_stranger():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Moze is following someone."
        "Moze is super paranoid.":
            player "Damn Moze is following strangers now!"
            player "I don't like the looks of this!"
            pause 0.5
        "This seems dangerous.":
            player "Oh god, this is going to go badly!"
            player "What you doing Moze!"
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc6_recbonding():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Rec is opening up."
        "Rec is cool!":
            player "Rec is so cool!"
            player "Really love their character!"
            pause 0.5
        "Rec is cute!":
            player "Rec is so cute!"
            player "Really love their design!"
            #add chatter
            pause 0.5
        "Damn I'm guilty.":
            player "Oh god we kill their brother."
            player "This is going to come back to bite us!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc6_shipbet1():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "They bet the ship on this game?"
        "Classic Jenn and Resa.":
            player "Oh damn! Bit of an overbet!"
            player "Now we gotta win!"
            pause 0.5
        "What the hell!":
            player "Holy smokes!"
            player "That's crazy! Now we gotta win!"
            #add chatter
            pause 0.5
        "I don't buy it.":
            player "Naw chat. I'm calling cap."
            player "They're reckless but not like that."
            #variable to track you predicting this
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc6_trustcrew():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Moze isn't going to help them cheat."
        "Got to have integrity.":
            player "They got themselves into this mess."
            player "They'll have to get themselves out of it!"
            pause 0.5
        "I trust Jennica and Teresa.":
            player "Trust the crew!"
            player "Jenn and Resa got this!"
            #add chatter
            pause 0.5
        "Oh no I hope they win!":
            player "Crap this there's a lot riding on this!"
            player "Was this a mistake?"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc6_shootingzan():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Moze shot Zan to help them."
        "Blast em!":
            player "Get blasted Zan!"
            pause 0.5
        "Wow crazy!":
            player "Woah that was awesome!"
            player "Crazy!"
            #add chatter
            pause 0.5
        "That was cheating!":
            player "Damn, feels weird that we had to cheat to win."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc6_shipbet2():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "The crew didn't actually bet the ship."
        "What a relief.":
            player "Phew. That's a relief"
            player "That coulda been bad!"
            pause 0.5
        "I knew it!":
            #if the player predicted it
            player "I called it chat!"
            player "No way they'd bet the ship!"
            #add chatter
            pause 0.5
        "Wow cop out.":
            player "Hahaha"
            player "Of course they didn't bet the ship."
            player "What a cop out."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc7_lostmac():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to losing MAC."
        "Oh no!":
            player "MAC!"
            player "Nooooo!"
            pause 0.5
        "The plot thickens.":
            player "Oh damn! Things are getting interesting!"
            player "Cool!"
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc8_teresabluff():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on Teresa's bluff."
        "Teresa's in her element.":
            player "Wow! Teresa knows her high society."
            player "That's so cool!"
            pause 0.5
        "How lucky.":
            player "Lucky Teresa was here!"
            #add chatter
            pause 0.5
        "This is boring.": #maybe have this only if you stealthed into the commsbase in vig2 or maybe different based on vig2
            player "Wow more stealth?"
            player "Really seems like that's always an option."
            player "Wish we could go loud!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc9_daisyreturns():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Say something about Daisy."
        "She's back!":
            player "Daisy returns!"
            player "Love it! She's the realest person in this room."
            pause 0.5
        "Maybe she is following us?":
            player "Oh damn! Maybe she was following us?"
            player "Pretty sus chat."
            #add chatter
            pause 0.5
        "Cute!":
            player "She's so cute!"
            player "I love her design!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc9_amasurprise():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Ama."
        "Oh no!":
            player "This is bad!"
            player "This is really bad!"
            pause 0.5
        "Not so paranoid after all!":
            player "Oh wow!"
            player "Guess Moze wasn't being paranoid after all!"
            #add chatter
            pause 0.5
        "It's go time.":
            player "Oh it's time to rumble."
            player "Let's get loud!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc11_amabacksass():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on Moze and Ama's insults."
        "Burn Ama!":
            player "Damn Ama!"
            player "Get roasted!"
            pause 0.5
        "Love this sass.":
            player "Feel like they haven't missed a step!"
            player "Just like old times hahaha!"
            #add chatter
            pause 0.5
        "Let them fight!":
            player "Boo. Let me fight."
            player "She's got a whole lot coming to her."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig3_sc12_amachoke():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on Ama's workplace relations."
        "Don't mess with Ama.":
            player "Damn!"
            player "Watch out, don't piss off Ama!"
            pause 0.5
        "Better call HR!":
            player "Better file an HR report!"
            player "Terrible workplace conduct from Ama!"
            #add chatter
            pause 0.5
        "Buddy got off easy.":
            player "Yeah I'd have done worse."
            player "This guy was asking for trouble!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return






        





