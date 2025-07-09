###This script contains targets that the comments and reactions can direct to in Vignette 3



### streamer react moments###

label vig3_sc1_out():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Teresa's upset."
        "Wow it's weighing heavily on her.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Wow it's crazy to see it weighing so heavily on Teresa!"
            player "She's usually so stoic!"
            pause 0.5
        "Brutal!":
            $ reactImage = "stream ui/reactconfident.png"
            player "The girls are fighting!!" 
            #$ AddChatter(vig2_sc1_reactcomment1)
            pause 0.5
        "This is what she wanted.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Wasn't Teresa the one saying we needed to do this?"
            player "C'mon girl this is what you wanted!"
            #$ AddChatter(vig2_sc1_reactcomment2)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc1_mar():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Jennica's upset."
        "It was always risky":
            $ reactImage = "stream ui/reactshocked.png"
            player "Damn it's weighing heavily on her."
            player "Definitely was risky."
            pause 0.5
        "They're fighting!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Oh damn the girls are fighting!"
            #add chatter
            pause 0.5
        "This is what she wanted.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Wasn't Jennica saying this was what we needed to do?"
            player "C'mon girl this is what you wanted!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc2_macdad():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
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
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc3_maccandy():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Talk about MAC's naivete."
        "MAC is so innocent!":
            $ reactImage = "stream ui/reactshocked.png"
            player "Wow MAC is too innocent."
            player "Too pure for this world!"
            pause 0.5
        "Watch out MAC!":
            $ reactImage = "stream ui/reactthinking.png"
            player "Oh god MAC's gonna get in trouble!"
            player "He's so out of his element!"
            #add chatter
            pause 0.5
        "This will end badly hahaha!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Oh God"
            player "MAC's gonna be a problem here."
            player "We're about to get scammed!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc3_firstfight():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to the fight."
        "Wow badass!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Holy smokes look at them go!"
            player "Jenn and Resa kicking butt!"
            pause 0.5
        "Bit of an overreaction.":
            $ reactImage = "stream ui/reactunsure.png"
            player "Well that seemed uneccesary!"
            player "Not saying that he wasn't gross but still!"
            #add chatter
            pause 0.5
        "This will come back around.":
            $ reactImage = "stream ui/reactconversational.png"
            player "We really shouldn't be antagonizing people."
            player "This is going to come back to bite us!"
            $ firstfightprediction == True
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc4_houndraid():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to the raid."
        "Told you!" if firstfightprediction == True:
            $ reactImage = "stream ui/reactconfident.png"
            player "I knew it!"
            player "See chat! I knew they would be back!"
            pause 0.5
        "They better not take the antenna.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Oh no! They're going to take the part we need!"
            player "Things bout to get complicated!"
            #add chatter
            pause 0.5
        "Let's fight em!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "We can take em!"
            player "Let's rumble. They ain't so tough!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc5_amahallu():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Talk about Moze's paranoia."
        "Damn Moze is flipping out.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Moze is pulling guns on showgirls!"
            player "She's seeing ghosts!"
            pause 0.5
        "Damn that's the second time now!":
            $ reactImage = "stream ui/reactunsure.png"
            player "This is the second time!"
            player "Chat Moze is shook!"
            player "Talk about paranoia."
            #add chatter
            pause 0.5
        "Spooky!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Damn it's hard to know if we're actually being tailed!"
            player "Chat I'm spooked!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc6_crewspat():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "The crew's mad at each other."
        "They're at each other's throats.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Oh damn! The girls are angry!"
            player "Some serious shade getting thrown!"
            pause 0.5
        "Jennica's so protective of MAC.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Awww. Jennica doesn't want MAC to hear the bad words!"
            player "Cute!"
            #add chatter
            pause 0.5
        "Relax Jennica, he's a bot.":
            $ reactImage = "stream ui/reactconversational.png"
            player "I mean he's just a robot."
            player "C'mon now, his database def has worse no?"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc6_stranger():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Moze is following someone."
        "Moze is super paranoid.":
            $ reactImage = "stream ui/reactunsure.png"
            player "Damn Moze is following strangers now!"
            player "I don't like the looks of this!"
            pause 0.5
        "This seems dangerous.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Oh god, this is going to go badly!"
            player "What you doing Moze!"
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc6_recbonding():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Rec is opening up."
        "Rec is cool!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Rec is so cool!"
            player "Really love their character!"
            pause 0.5
        "Rec is cute!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Rec is so cute!"
            player "Really love their design!"
            #add chatter
            pause 0.5
        "Damn I'm guilty.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Oh god we kill their brother."
            player "This is going to come back to bite us!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc6_shipbet1():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "They bet the ship on this game?"
        "Classic Jenn and Resa.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Oh damn! Bit of an overbet!"
            player "Now we gotta win!"
            pause 0.5
        "What the hell!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Holy smokes!"
            player "That's crazy! Now we gotta win!"
            #add chatter
            pause 0.5
        "I don't buy it.":
            $ reactImage = "stream ui/reactunsure.png"
            player "Naw chat. I'm calling cap."
            player "They're reckless but not like that."
            $ shipbetprediction == True
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc6_trustcrew():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on Moze trusting her crew and not cheating."
        "Got to have integrity.":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "They got themselves into this mess."
            player "They'll have to get themselves out of it!"
            pause 0.5
        "I trust Jennica and Teresa.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Trust the crew!"
            player "Jenn and Resa got this!"
            #add chatter
            pause 0.5
        "Oh no I hope they win!":
            $ reactImage = "stream ui/reactshocked.png"
            player "Crap this there's a lot riding on this!"
            player "Was this a mistake?"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc6_shootingzan():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on Moze shooting Zan."
        "Blast em!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Get blasted Zan!"
            pause 0.5
        "Wow crazy!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Woah that was awesome!"
            player "Crazy!"
            #add chatter
            pause 0.5
        "That was cheating!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Damn, feels weird that we had to cheat to win."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc6_shipbet2():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "The crew didn't actually bet the ship."
        "What a relief.":
            $ reactImage = "stream ui/reactunsure.png"
            player "Phew. That's a relief"
            player "That coulda been bad!"
            pause 0.5
        "I knew it!" if shipbetprediction == True:
            $ reactImage = "stream ui/reactcelebrate.png"
            player "I called it chat!"
            player "No way they'd bet the ship!"
            #add chatter
            pause 0.5
        "Wow cop out.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Hahaha"
            player "Of course they didn't bet the ship."
            player "What a cop out."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc7_lostmac():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to losing MAC."
        "Oh no!":
            $ reactImage = "stream ui/reactshocked.png"
            player "MAC!"
            player "Nooooo!"
            pause 0.5
        "The plot thickens.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Oh damn! Things are getting interesting!"
            player "Cool!"
            #add chatter
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc8_teresabluff():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on Teresa's bluff."
        "Teresa's in her element.":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Wow! Teresa knows her high society."
            player "That's so cool!"
            pause 0.5
        "How lucky.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Wow."
            player "Lucky Teresa was here."
            #add chatter
            pause 0.5
        "This is boring.": #maybe have this only if you stealthed into the commsbase in vig2 or maybe different based on vig2
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Jeez. More stealth?"
            player "Really seems like that's always an option."
            player "Wish we could go loud!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc9_daisyreturns():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Say something about Daisy."
        "She's back!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Daisy returns!"
            player "Love it! She's the realest person in this room."
            pause 0.5
        "Maybe she is following us?":
            $ reactImage = "stream ui/reactthinking.png"
            player "Oh damn! Maybe she was following us?"
            player "Pretty sus chat."
            #add chatter
            pause 0.5
        "Cute!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "She's so cute!"
            player "I love her design!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc9_amasurprise():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Ama."
        "Oh no!":
            $ reactImage = "stream ui/reactshocked.png"
            player "This is bad!"
            player "This is really bad!"
            pause 0.5
        "Not so paranoid after all!":
            $ reactImage = "stream ui/reactthinking.png"
            player "Oh wow!"
            player "Guess Moze wasn't being paranoid after all!"
            #add chatter
            pause 0.5
        "It's go time.":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Oh it's time to rumble."
            player "Let's get loud!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc11_amabacksass():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on Moze and Ama's insults."
        "Burn Ama!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Damn Ama!"
            player "Get roasted!"
            pause 0.5
        "Love this sass.":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Feel like they haven't missed a step!"
            player "Just like old times hahaha!"
            #add chatter
            pause 0.5
        "Let them fight!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Boo. Let me fight."
            player "She's got a whole lot coming to her."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc12_amachoke():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on Ama's workplace relations."
        "Don't mess with Ama.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Damn!"
            player "Watch out, don't piss off Ama!"
            pause 0.5
        "Better call HR!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Better file an HR report!"
            player "Terrible workplace conduct from Ama!"
            #add chatter
            pause 0.5
        "Buddy got off easy.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Yeah I'd have done worse."
            player "This guy was asking for trouble!"
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc12_amafindsout():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Ama knows that it's the real MAC!"
        "The jig is up!":
            $ reactImage = "stream ui/reactshocked.png"
            player "This is really bad!"
            player "Ama figured it out!"
            pause 0.5
        "Time to fight!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Finally time for some battle!"
            player "Don't get between Mozely and her MAC!"
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

label vig3_sc12_macalignment_violencepessimism():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "MAC shot Ama!"
        "MAC's a badass!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Wow he shot her!"
            player "Zero hesitation! Ice cold!"
            player "MAC for the win! Crack shot!"
            pause 0.5
        "MAC no!":
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
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc12_macalignment_violenceoptimism():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
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
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc12_macalignment_peacepessimism():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
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
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc12_macalignment_peaceoptimism():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
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
            player "What is going on!?"
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
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc14_recfindsout_regret():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Moze's confession."
        "Finally coming clean.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Wow. Brutal."
            player "But at least she's taking accountability for once."
            pause 0.5
        "Sorry Rec.":
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
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig3_sc14_recfindsout_ihadto():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Moze's confession."
        "Damn right.":
            $ reactImage = "stream ui/reactunsure.png"
            player "I mean she's right. Allistar betrayed them."
            player "What did he expect?"
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
            player "Yeah I guess that was the right thing to do."
            player "They shouldn't expect an apology though. Allistar crossed us!"
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

label vig3_sc14_recfindsout_noremorse():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Moze's admission."
        "No remorse!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Hell yeah!"
            player "Allistar deserved it! No regrets."
            pause 0.5
        "Damn that was cold.":
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
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return



        





