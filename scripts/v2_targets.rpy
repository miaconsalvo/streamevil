###This script contains targets that the comments and reactions can direct to

label vig2_sc1_testquestion():
    $ macroChoice = True
    $ vig2_sc1_comment2.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "Coriolis remembered I had a test today."
        "It went well!":
            $ reactImage = "stream ui/reactthumbsup.png"
            $ csEngagement += 1
            player "It was really great actually! Can't believe you remembered!"
            $ AddChatter(vig2_sc1_coriolis_comment1)
            pause 0.5
        "Not so hot.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            $ csEngagement += 1
            player "It kicked my butt. Honestly I'm just hoping I pass."
            $ AddChatter(vig2_sc1_coriolis_comment2)
            pause 0.5
        "Say nothing.":
            pass
    if reactVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ commentVariable = False
    return

label vig2_sc1_matticusopinion():
    $ macroChoice = True
    $ vig2_sc1_comment13.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "What did I think of Matticus in game 1?"
        "He was the worst.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Ugh, no this guy has always been the worst"
            $ AddChatter(vig2_sc1_kitcat_comment1)
            pause 0.5
        "He was fine.":
            $ reactImage = "stream ui/reactconversational.png"
            $ kcEngagement += 1
            player "I didn't mind him as much as some fans, even though I didn't ally with him a ton."
            $ AddChatter(vig2_sc1_kitcat_comment2)
            pause 0.5
    if reactVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ commentVariable = False
    return

label vig2_sc2_mar_consistency():
    $ macroChoice = True
    $ vig2_sc2_mar_comment3.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "Someone's asking if this is consistent with the last episode"
        "We'll warm up to Outlaw.":
            $ reactImage = "stream ui/reactunsure.png"
            $ pdEngagement += 1
            player "Don't worry chat, we're just getting warmed up."
            player "After all, can't be Outlaw all the time or it isn't special."
            $ AddChatter(vig2_sc2_mar_J4MresponseOUT)
            pause 0.5
        "Let's avoid Outlaw for now.":
            $ reactImage = "stream ui/reactconversational.png"
            $ reluctance += 1
            player "I mean, we don't want MORE people getting hurt."
            player "This keeps us under the radar for the mission too."
            $ AddChatter(vig2_sc2_mar_J4MresponseMAR)
            pause 0.5
    if reactVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ commentVariable = False
    return

label vig2_sc2_out_romance():
    $ macroChoice = True
    $ vig2_sc2_out_comment5.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "Which character am I thinking of romancing?"
        "I'm thinking Jennica.":
            $ reactImage = "stream ui/reactconfident.png"
            $ csEngagement += 1
            player "Jennica's sweet, I'm leaning her at the moment!"
            $ romanceJennica = True
            $ romanceTeresa = False
            $ romanceAma = False
            pause 0.5
            $ AddChatter(vig2_sc2_romance_pilot1)
            pause 1.0
        "Probably Teresa.":
            $ reactImage = "stream ui/reactconfident.png"
            $ kcEngagement += 1
            player "Teresa for sure. She's got an edge I appreciate."
            $ romanceJennica = False
            $ romanceTeresa = True
            $ romanceAma = False
            pause 0.5
            $ AddChatter(vig2_sc2_romance_engineer1)
            pause 1.0
        "Ama all day.":
            $ reactImage = "stream ui/reactconfident.png"
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
    if reactVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ commentVariable = False
    return

label vig2_sc4_gameplan():
    $ macroChoice = True
    $ vig2_sc4_comment1.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "How should I approach Matticus?"
        "Let's lean into it.":
            $ reactImage = "stream ui/reactconfident.png"
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
        "Don't listen to him.":
            $ reactImage = "stream ui/reactconversational.png"
            $ reluctance += 1
            $ csEngagement += 1
            $ pdEngagement -= 1
            player "Yeah, do the exact opposite of whatever Matticus wants."
            $ AddChatter(vig2_sc4_against_comment1)
            pause 1.0
            $ AddChatter(vig2_sc4_against_comment2)
    if reactVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ commentVariable = False
    return

label vig2_sc7_toofar():
    $ macroChoice = True
    $ vig2_sc7_out_comment1.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "Is this too far?"
        "Let's roll with it!":
            $ reactImage = "stream ui/reactthumbsup.png"
            $ enthusiasm += 1
            $ pdEngagement += 1
            $ kcEngagement += 1
            player "YOU SAID IT!"
        "It's feeling off to me.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            $ csEngagement += 2
            $ pdEngagement -= 2
            $ reluctance -= 1
            player "Kinda wish I could go back tbh..."
    if reactVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ commentVariable = False
    return

label vig2_sc7_rips():
    $ macroChoice = True
    $ vig2_sc7_out_execute_comment4.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "Should I encourage this?"
        "Guys, this is serious.":
            $ reactImage = "stream ui/reactshocked.png"
            $ reluctance += 2
            $ pdEngagement -= 2
            $ kcEngagement -= 1
            $ csEngagement += 1
            $ encourageRIPS = False
            "This is pretty heavy stuff guys, let's not get too carried away."
        "Put those rips in chat.":
            $ reactImage = "stream ui/reactcelebrate.png"
            $ enthusiasm += 2
            $ pdEngagement += 1
            $ kcEngagement += 1
            $ encourageRIPS = True
            "RIP Otacon guy!"
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
    if reactVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ commentVariable = False
    return

label vig2_epilogue_outlaw():
    $ macroChoice = True
    $ vig2_epilogue_out_comment6.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "That was pretty different from how things usually go."
        "It was exciting!":
            $ reactImage = "stream ui/reactthumbsup.png"
            $ enthusiasm += 1
            player "Nope! But definitely fun hahaha"
        "It was exhausing!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            #Just because one choice affects a variable doesn't mean its opposite has to do something
            #We can have a "neutral" choice
            player "I feel like just ran an emotional marathon hahaha"
    if reactVariable == True:
        "Where was I?"
        $ narrator = reg_narrator
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ commentVariable = False
    return

#################
### streamer react moments ###
#################

label vig2_sc1_openingstream():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Introduce the stream."
        "Welcome back!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Hey guys! Welcome back to the stream!"
            player "Lets get into the next episode!"
            pause 0.5
        "How's it going everyone!":
            $ reactImage = "stream ui/reactconversational.png"
            player "Oh damn here we go again!" 
            player "How's it going everyone?"
            $ AddChatter(vig2_sc1_reactcomment1)
            pause 0.5
        "Trouble time!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Hey folks!"
            player "Are you guys ready to get into some trouble?"
            $ AddChatter(vig2_sc1_reactcomment2)
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

label vig2_sc1_mentionallistar():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Talk about Allistar?"
        "I still feel bad about that.":
            $ reactImage = "stream ui/reactunsure.png"
            player "Not gonna lie, I feel a bit bad for that one."
            $ AddChatter(vig2_sc1_reactcomment3)
            pause 0.5
            $ AddChatter(vig2_sc1_reactcomment4)
            pause 0.5
        "Don't mess with MAC!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Listen, you mess with MAC, you mess with me!"
            $ AddChatter(vig2_sc1_reactcomment5)
            pause 0.5
    if commentVariable == True:
        $ narrator = reg_narrator
        "Where was I?"
    else:
        $ macroChoice = False
        if macroChoice == False:
            $ narrator = alt_narrator
        else:
            $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    $ reactVariable = False
    return

label vig2_sc1_matticusjennicaopinion():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Think about the relationships with other characters."
        "What's the relationship system in this game like?":
            $ reactImage = "stream ui/reactthinking.png"
            player "I wonder what the relationship track is like in this one..."
            $ AddChatter(vig2_sc1_reactcomment6)
            pause 0.5
        "Jennica looks pissed.":
            $ reactImage = "stream ui/reactunsure.png"
            player "She is definitely not happy, that's not a good sign."
            $ AddChatter(vig2_sc1_reactcomment7)
            pause 0.5
            $ AddChatter(vig2_sc1_reactcomment8)
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

label vig2_sc2_landingongibian():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Speculate about what happens next."
        "How bad do you guys think this'll go?":
            $ reactImage = "stream ui/reactconfident.png"
            player "Alright on a scale of 1 to 10 how fast is this gonna go bad?"
            $ customsSpeculation = True
            $ AddChatter(vig2_sc2_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment2)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment3)
            pause 0.5
        "I wanna explore!":
            $ reactImage = "stream ui/reactconversational.png"
            player "I wonder how much exploring we'll get to do…"
            pause 0.5
        "Is Ama gonna show up?":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "If Ama shows up, I'm gonna FREAK!"
            $ AddChatter(vig2_sc2_reactcomment4)
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

label vig2_sc2_whywedidntfly():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Hype the chat about MAC."
        "MAC's so cool!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "MAC best cargo confirmed."
            $ AddChatter(vig2_sc2_reactcomment5)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment6)
            pause 0.5
        "MAC would get away with it.":
            $ reactImage = "stream ui/reactconfident.png"
            player "I think they would just let MAC go they're too cute."
            $ AddChatter(vig2_sc2_reactcomment7)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment8)
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

label vig2_sc2_firstproblem():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Call back to speculating what will happen."
        "I called it!" if customsSpeculation == True:
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Well, that didn't take very long…."
            $ AddChatter(vig2_sc2_reactcomment9)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment10)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment11)
            pause 0.5
        "Guess we can't explore.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Guess that's a no on the exploring."
            pause 0.5
        "We're definitely getting exposed.":
            $ reactImage = "stream ui/reactunsure.png"
            player "Well if Ama wasn't here already, she'll definitely be on her way after this."
            $ AddChatter(vig2_sc2_reactcomment12)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment13)
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

label vig2_sc2_customsdecision():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Think about if you made the right choice."
        "All good!":
            $ reactImage = "stream ui/reactconfident.png"
            player "This will be fine!"
            $ AddChatter(vig2_sc2_reactcomment14)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment15)
            pause 0.5
        "Maybe we should reload.":
            $ reactImage = "stream ui/reactthinking.png"
            player "We can always save scum right?"
            pause 0.5
        "It's so over.":
            $ reactImage = "stream ui/reactconversational.png"
            player "We're so boned, but we're boned together!"
            $ AddChatter(vig2_sc2_reactcomment16)
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

label vig2_sc3_aftercustoms():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Reflect about the choice you just made."
        "We were fine all along!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "See! Everything went perfect!"
            $ AddChatter(vig2_sc3_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc3_reactcomment2)
            pause 0.5
            $ AddChatter(vig2_sc3_reactcomment3)
            pause 0.5
        "Phew. That was close.":
            $ reactImage = "stream ui/reactunsure.png"
            player "I won't lie, I was scared about how that was going to go."
            pause 0.5
        "Weak.":
            player "Honestly that was a bit disappointing."
            $ reactImage = "stream ui/reactthumbsdown.png"
            $ AddChatter(vig2_sc3_reactcomment4)
            pause 0.5
            $ AddChatter(vig2_sc3_reactcomment5)
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

label vig2_sc4_meetingmatticus():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Tell the chat how you feel about Matticus."
        "This guy sucks.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "I wonder if he ever thought about not breathing... forever."
            $ AddChatter(vig2_sc4_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc4_reactcomment2)
            pause 0.5
        "Cool design!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Ooooo cool character redesign!"
            $ AddChatter(vig2_sc4_reactcomment3)
            pause 0.5
        "Oh boy, here comes chaos!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "This is gonna be so bad, I'm so excited."
            $ AddChatter(vig2_sc4_reactcomment4)
            pause 0.5
            $ AddChatter(vig2_sc4_reactcomment5)
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

label vig2_sc4_plancheckin():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Check-in with the chat."
        "Matticus is gonna make this tough.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Of course. Matticus needs to make this complicated."
            $ AddChatter(vig2_sc4_reactcomment6)
            pause 0.5
            $ AddChatter(vig2_sc4_reactcomment7)
            pause 0.5
            $ AddChatter(vig2_sc4_reactcomment8)
            pause 0.5
        "Things are never easy.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Why did I expect an easy mission this time around?"
            pause 0.5
        "Just like old times!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Back to the ol' Snakehawk playbook!"
            $ AddChatter(vig2_sc4_reactcomment9)
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

label vig2_sc5_macquestion():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Inquire about MAC's learning."
        "MAC's seems inquisitive.":
            $ reactImage = "stream ui/reactthinking.png"
            player "MAC is asking a lot of questions, maybe I should be more careful."
            $ AddChatter(vig2_sc5_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc5_reactcomment2)
            pause 0.5
        "Is MAC remembering everything?":
            $ reactImage = "stream ui/reactconversational.png"
            player "Do y'all think MAC will develop based on what we do?"
            $ AddChatter(vig2_sc5_reactcomment3)
            pause 0.5
        "MAC shield your eyes!":
            $ reactImage = "stream ui/reactconfident.png"
            player "MAC, not gonna lie to you buddy, we might kill so many people."
            $ AddChatter(vig2_sc5_reactcomment4)
            pause 0.5
            $ AddChatter(vig2_sc5_reactcomment5)
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

label vig2_sc6_out_reflect():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Reflect on the confrontation."
        "Lotta violence.":
            $ reactImage = "stream ui/reactunsure.png"
            player "Well that was messy..."
            $ AddChatter(vig2_sc6_out_reactcomment1)
            pause 0.5
        "I messed up.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Definitely could've done that a lot better."
            $ AddChatter(vig2_sc6_out_reactcomment2)
            pause 0.5
            $ AddChatter(vig2_sc6_out_reactcomment3)
            pause 0.5
        "Hell yeah!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Yeah that feels like the way that should've gone."
            $ AddChatter(vig2_sc6_out_reactcomment4)
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

label vig2_sc6_mar_reflect():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Reflect on the stealth mission."
        "We just had to sneak in?":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "So that was the big stealth mission?"
            $ AddChatter(vig2_sc6_mar_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc6_mar_reactcomment2)
            pause 0.5
        "Definitely the right way.":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Quick and quient, best strategy."
            $ AddChatter(vig2_sc6_mar_reactcomment3)
            pause 0.5
        "We're gonna get caught for sure!":
            $ reactImage = "stream ui/reactunsure.png"
            player "Those guards are definitely coming back after us afterwards."
            $ AddChatter(vig2_sc6_mar_reactcomment4)
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

label vig2_sc7_bigreveal():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Respond to Reginald."
        "True.":
            $ reactImage = "stream ui/reactthinking.png"
            player "I mean, he's not wrong..."
            $ AddChatter(vig2_sc7_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc7_reactcomment2)
            pause 0.5
        "This is another level though.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Listen I've done some terrible things, but destroying an aid ship is crazy."
            $ AddChatter(vig2_sc7_reactcomment3)
            pause 0.5
            $ AddChatter(vig2_sc7_reactcomment4)
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

label vig2_sc8_out_postchoice():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "After your choice."
        "We had no choice.":
            $ reactImage = "stream ui/reactthinking.png"
            player "I have to do what I have to do."
            $ AddChatter(vig2_sc8_out_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment2)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment3)
            pause 0.5
        "It's good to be bad!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "That felt better than I expected."
            $ AddChatter(vig2_sc8_out_reactcomment4)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment5)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment6)
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

label vig2_sc8_out_reflect():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Reflect on your choice."
        "Jennica's upset.":
            $ reactImage = "stream ui/reactshocked.png"
            player "I think we lost Jennica's trust a bit."
            $ AddChatter(vig2_sc8_out_reactcomment7)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment8)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment9)
            pause 0.5
        "Was that wrong?":
            $ reactImage = "stream ui/reactunsure.png"
            player "Maybe that was too much..."
            $ AddChatter(vig2_sc8_out_reactcomment10)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment11)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment12)
            pause 0.5
        "Get wrecked!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Bye bye, Sallent."
            $ AddChatter(vig2_sc8_out_reactcomment13)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment14)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment15)
            if baseGuardKilled == True:
                $ AddChatter(vig2_sc8_out_reactcomment16)
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

label vig2_sc9_out_end():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Reflect on the Outlaw choice."
        "Matticus will get his karma.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Don't worry, I'll make sure Matticus gets his."
            $ AddChatter(vig2_sc9_out_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc9_out_reactcomment2)
            pause 0.5
        "A new friend?":
            $ reactImage = "stream ui/reactconversational.png"
            player "A Matticus ally run maybe?"
            $ AddChatter(vig2_sc9_out_reactcomment3)
            pause 0.5
            $ AddChatter(vig2_sc9_out_reactcomment4)
            pause 0.5
        "So much more content!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "I can't believe I missed stuff like this on my first playthrough."
            $ AddChatter(vig2_sc9_out_reactcomment5)
            pause 0.5
            $ AddChatter(vig2_sc9_out_reactcomment6)
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

label vig2_sc8_mar_reacttoregi():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "React to Reginald."
        "Add him to the pile!" if gunsBlazing == True:
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Looks like we're going to get another body."
            $ AddChatter(vig2_sc8_mar_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment2)
            pause 0.5
        "Predictable.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Of course he does."
            $ AddChatter(vig2_sc8_mar_reactcomment3)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment4)
            pause 0.5
        "Can we persuade him?":
            $ reactImage = "stream ui/reactthinking.png"
            player "Maybe we can talk our way out of this?"
            $ AddChatter(vig2_sc8_mar_reactcomment5)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment6)
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

label vig2_sc8_mar_reacttoregistun():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "React to stunning Reginald."
        "Better than he deserved.":
            $ reactImage = "stream ui/reactconfident.png"
            player "I mean if we would've killed him that wouldn't be a problem."
            $ AddChatter(vig2_sc8_mar_reactcomment7)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment8)
            pause 0.5
        "Fair enough.":
            $ reactImage = "stream ui/reactconversational.png"
            player "I guess that makes sense."
            $ AddChatter(vig2_sc8_mar_reactcomment9)
            pause 0.5
        "Get stunned!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "That felt pretty good."
            $ AddChatter(vig2_sc8_mar_reactcomment10)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment11)
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

label vig2_sc8_mar_reacttoregibribe():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "React to the bribe."
        "Easy.":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Welp, that was easy."
            $ AddChatter(vig2_sc8_mar_reactcomment12)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment13)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment14)
            pause 0.5
        "Better than he deserved.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "It would've felt better to shoot him."
            $ AddChatter(vig2_sc8_mar_reactcomment15)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment16)
            pause 0.5
        "This is getting expensive.":
            $ reactImage = "stream ui/reactunsure.png"
            player "Do we even have that kind of money?"
            $ AddChatter(vig2_sc8_mar_reactcomment17)
            pause 0.5
    $ macroChoice = False
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

label vig2_sc9_mar_end():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Reflect on the Marshal choice."
        "Too easy tbh.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "That was a bit too convenient, to be honest."
            $ AddChatter(vig2_sc9_mar_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc9_mar_reactcomment2)
            pause 0.5
        "Sweet!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Honestly couldn't ask to be in a better spot."
            $ AddChatter(vig2_sc9_mar_reactcomment3)
            pause 0.5
            $ AddChatter(vig2_sc9_mar_reactcomment4)
            pause 0.5
        "Was this the best choice?":
            $ reactImage = "stream ui/reactthinking.png"
            player "Definitely should've blown up the ship."
            $ AddChatter(vig2_sc9_mar_reactcomment5)
            pause 0.5
            $ AddChatter(vig2_sc9_mar_reactcomment6)
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


######Below this is code for Blueit and Flinch in Vignette 2##############
label vig2_blueit_allistarthread():
    $ screenComplete = False
    $ blueitImage = "socials/v2_allistar thread.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig2_blueit_matticusthread():
    $ screenComplete = False
    $ blueitImage = "socials/v2_matticus thread.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show major choice thread at top:
    #    zoom 1.5
    call screen blueitButtonCheck
    return

label vig2_blueit_copoutthread():
    $ screenComplete = False
    $ blueitImage = "socials/v2_copout thread.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show romance thread at top:
    #    zoom 1.5
    call screen blueitButtonCheck
    return

label vig2_blueit_stealththread():
    $ screenComplete = False
    #show first game thread at top:
    #    zoom 1.5
    $ blueitImage = "socials/v2_stealth thread.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    call screen blueitButtonCheck
    return


###Targets for Flinch#####
label vig2_analytics_viewcount():
    $ flinchCheck += 1
    $ flinch_viewcountCheck = True
    hide screen viewershipButton_vig2
    "The view counts are much more stable than the last Oakley stream."
    "No crazy spikes like the raid, but much more consistent viewership overall."
    jump vig2_analytics_viewcount2

label vig2_analytics_viewcount2():
    menu:
        "No crazy spikes like the raid, but much more consistent viewership overall."
        "What's the average viewer count?" if viewershipThoughtCheck == False:
            "The average viewer count for the stream is about 10.4."
            "Over 10! That's great!"
            "It's a little close to dropping below 10, so you'll have to keep up the momentum for the next couple weeks."
            "Your other streams have been a bit lower than that, but if this count stays stable, you should be on track!" #Here's the issue, we can say this, what can people do to change this if they weren't on track
            $ viewershipThoughtCheck = True
            jump vig2_analytics_viewcount2
        "Losing viewers sucks!" if shnzi == False and flinchViewershipShnzi == False:
            "What was that viewer who left the stream?"
            "Shnzi?"
            "Like, you get it. If you've already seen the game on stream, it makes sense not to watch."
            "But they didn't have to {i}say{/i} they were leaving."
            $ flinchViewershipShnzi = True
            jump vig2_analytics_viewcount2
        "The assault on the base was crazy!" if gunsBlazing == True and flinchViewershipAssault == False:
            "The action scene at the datacentre was nuts."
            "So many people commenting it was hard to pay attention to the game."
            menu:
                "So many people commenting it was hard to pay attention to the game."
                "It was easier than the raid.":
                    "It was a lot less intense than the raid though."
                    "You think you're getting better at managing the chat."
                    "It feels good!"
                "I'm still getting used to it.":
                    "You're not used to hearing so many people's opinions about the game."
                    "Sometimes it's tough to figure out what you think about it."
                    "You think it'll get easier though."
            $ flinchViewershipAssault = True
            jump vig2_analytics_viewcount2
        "Will the Outlaw route pull people in?" if vig2_outlawEpilogue == True and flinchViewershipOutlaw == False:
            "There was one person in the chat who said they wanted to see the stream with the \"evil MC.\""
            "You wonder if going Outlaw at the end of this episode will bring more people to the stream next time."
            $ flinchViewershipOutlaw = True
            jump vig2_analytics_viewcount2
        "Will the Marshal route deter people from viewing?" if vig2_marshalEpilogue == True and flinchViewershipMarshal == False:
            "There was one person in the chat who said they wanted to see the stream with the \"evil MC.\""
            "You wonder if you maybe missed an opportunity to get more viewers by going Marshal at the end of this episode."
            $ flinchViewershipMarshal = True
            jump vig2_analytics_viewcount2
        "Go back to the main Flinch page." if viewershipThoughtCheck == True:
            if flinchCheck >= 3:
                $ screenComplete = True
            else:
                pass
            show screen viewershipButton_vig2
            return
    return

label vig2_analytics_topfan():
    hide screen viewershipButton_vig2
    $ flinchCheck += 1
    $ flinch_topfanCheck = True
    if topfan == "Coriolis":
        "Even though you've got so many new people in chat, Coriolis is still holding down the fort."
        if vig2_outlawEpilogue == True:
            "It's a bit surprising considering some of the turns your stream has taken."
        "They're support feels really genuine."
    elif topfan == "kitcat":
        "kitcat is a real hoot."
        "They're obsession with MAC is truly next level."
        "Crazy that they just lucked into your stream."
        "It's already kind of hard to imagine playing the game without them."
    elif topfan == "pickledDragons":
        "pickledDragons really likes to push the envelope."
        "You wonder if they play \"Outlaw\" when they play games."
        "It seems like they really draw a line between the game and their personal life."
        "Maybe that's an attitude worth exploring."
    else:
        "Even though you've got so many new people in chat, Coriolis is still holding down the fort."
        if vig2_outlawEpilogue == True:
            "It's a bit surprising considering some of the turns your stream has taken."
        "They're support feels really genuine."
    if flinchCheck >= 3:
        $ screenComplete = True
    else:
        pass
    show screen viewershipButton_vig2
    return

label vig2_analytics_audience():
    hide screen viewershipButton_vig2
    $ flinchCheck += 1
    $ flinch_audienceCheck = True
    "The past couple streams have been a little light, but it seems like people are turning up for the Oakley sessions."
    "Now you're just a few followers away from crossing one of the thresholds for Affiliate."
    "How do you feel?"
    menu:
        "How do you feel?"
        "You can taste it!":
            $ energy += 1
            $ enthusiasm += 1
            "You're so close!"
            "Just a couple more weeks and all the metrics are pointing in the right direction."
            "You can't wait to celebrate with Jessie and El."
        "Average viewership is harder to crack.":
            $ energy += 1
            "Getting the follower number is good, but the average viewership is what held you back last time."
            "Can't take your eyes off the prize."
            "Still gotta stick to the schedule and go with what's working."
        "Maybe Affiliate isn't so important.": #I think this would be better at the end of vignette 3
            "It's weird, now that you have more viewers in chat consistently, getting Affiliate suddenly feels less important."
            "Is it cliche to say that maybe the people you've met have been the real prize?"
            "Probably."
            "But does that make them less valuable?"
    if flinchCheck >= 3:
        $ screenComplete = True
    else:
        pass
    show screen viewershipButton_vig2
    return