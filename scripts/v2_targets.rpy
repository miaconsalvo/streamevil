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
            pause 0.5
        "Not so hot":
            $ csEngagement += 1
            player "It kicked my butt. Honestly I'm just hoping I pass."
            $ AddChatter(vig2_sc1_coriolis_comment2)
            pause 0.5
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
            pause 0.5
        "He was fine":
            $ kcEngagement += 1
            player "I didn't mind him as much as some fans, even though I didn't ally with him a ton."
            $ AddChatter(vig2_sc1_kitcat_comment2)
            pause 0.5
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
            pause 0.5
        "Let's avoid Outlaw for now":
            $ reluctance += 1
            player "I mean, we don't want MORE people getting hurt."
            player "This keeps us under the radar for the mission too."
            $ AddChatter(vig2_sc2_mar_J4MresponseMAR)
            pause 0.5
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

#################
### streamer react moments ###
#################

label vig2_sc1_openingstream():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Introduce the stream."
        "Welcome back!":
            player "Hey guys! Welcome back to the stream!"
            player "Lets get into the next episode!"
            pause 0.5
        "How's it going everyone!":
            player "Oh damn here we go again!" 
            player "How's it going everyone?"
            $ AddChatter(vig2_sc1_reactcomment1)
            pause 0.5
        "Trouble time!":
            player "Hey folks!"
            player "Are you guys ready to get into some trouble?"
            $ AddChatter(vig2_sc1_reactcomment2)
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc1_mentionallistar():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Talk about Allistar?"
        "I still feel bad about that.":
            player "Not gonna lie, I feel a bit bad for that one."
            $ AddChatter(vig2_sc1_reactcomment3)
            pause 0.5
            $ AddChatter(vig2_sc1_reactcomment4)
            pause 0.5
        "Don't mess with MAC!":
            player "Listen, you mess with MAC, you mess with me!"
            $ AddChatter(vig2_sc1_reactcomment5)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc1_matticusjennicaopinion():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Think about the relationships with other characters."
        "What's the relationship system in this game like?":
            player "I wonder what the relationship track is like in this one..."
            $ AddChatter(vig2_sc1_reactcomment6)
            pause 0.5
        "Jennica looks pissed.":
            player "She is definitely not happy, that's not a good sign."
            $ AddChatter(vig2_sc1_reactcomment7)
            pause 0.5
            $ AddChatter(vig2_sc1_reactcomment8)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc2_landingongibian():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Speculate about what happens next."
        "How bad do you guys think this'll go?":
            player "Alright on a scale of 1 to 10 how fast is this gonna go bad?"
            $ customsSpeculation = True
            $ AddChatter(vig2_sc2_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment2)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment3)
            pause 0.5
        "I wanna explore!":
            player "I wonder how much exploring we'll get to do…"
            pause 0.5
        "Is Ama gonna show up?":
            player "If Ama shows up, I'm gonna FREAK!"
            $ AddChatter(vig2_sc2_reactcomment4)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc2_whywedidntfly():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Hype the chat about MAC."
        "MAC's so cool!":
            player "MAC best cargo confirmed."
            $ AddChatter(vig2_sc2_reactcomment5)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment6)
            pause 0.5
        "MAC would get away with it.":
            player "I think they would just let MAC go they're too cute."
            $ AddChatter(vig2_sc2_reactcomment7)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment8)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc2_firstproblem():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Call back to speculating what will happen."
        "I called it!" if customsSpeculation == True:
            player "Well, that didn't take very long…."
            $ AddChatter(vig2_sc2_reactcomment9)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment10)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment11)
            pause 0.5
        "Guess we can't explore.":
            player "Guess that's a no on the exploring."
            pause 0.5
        "We're definitely getting exposed.":
            player "Well if Ama wasn't here already, she'll definitely be on her way after this."
            $ AddChatter(vig2_sc2_reactcomment12)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment13)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc2_customsdecision():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Think about if you made the right choice."
        "All good!":
            player "This will be fine!"
            $ AddChatter(vig2_sc2_reactcomment14)
            pause 0.5
            $ AddChatter(vig2_sc2_reactcomment15)
            pause 0.5
        "Maybe we should reload.":
            player "We can always save scum right?"
            pause 0.5
        "It's so over.":
            player "We're so boned, but we're boned together!"
            $ AddChatter(vig2_sc2_reactcomment16)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc3_aftercustoms():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Reflect about the choice you just made."
        "We were fine all along!":
            player "See! Everything went perfect!"
            $ AddChatter(vig2_sc3_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc3_reactcomment2)
            pause 0.5
            $ AddChatter(vig2_sc3_reactcomment3)
            pause 0.5
        "Phew. That was close.":
            player "I won't lie, I was scared about how that was going to go."
            pause 0.5
        "Weak.":
            player "Honestly that was a bit disappointing."
            $ AddChatter(vig2_sc3_reactcomment4)
            pause 0.5
            $ AddChatter(vig2_sc3_reactcomment5)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc4_meetingmatticus():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Tell the chat how you feel about Matticus."
        "This guy sucks.":
            player "I wonder if he ever thought about not breathing... forever."
            $ AddChatter(vig2_sc4_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc4_reactcomment2)
            pause 0.5
        "Cool design!":
            player "Ooooo cool character redesign!"
            $ AddChatter(vig2_sc4_reactcomment3)
            pause 0.5
        "Oh boy here comes chaos!":
            player "This is gonna be so bad, I'm so excited."
            $ AddChatter(vig2_sc4_reactcomment4)
            pause 0.5
            $ AddChatter(vig2_sc4_reactcomment5)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc4_plancheckin():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Check-in with the chat."
        "Matticus is gonna make this tough.":
            player "Of course. Matticus needs to make this complicated."
            $ AddChatter(vig2_sc4_reactcomment6)
            pause 0.5
            $ AddChatter(vig2_sc4_reactcomment7)
            pause 0.5
            $ AddChatter(vig2_sc4_reactcomment8)
            pause 0.5
        "Things are never easy.":
            player "Why did I expect an easy mission this time around?"
            pause 0.5
        "Just like old times!":
            player "Back to the ol' Snakehawk playbook!"
            $ AddChatter(vig2_sc4_reactcomment9)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc5_macquestion():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Inquire about MAC's learning."
        "MAC's seems inquisitive.":
            player "MAC is asking a lot of questions, maybe I should be more careful."
            $ AddChatter(vig2_sc5_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc5_reactcomment2)
            pause 0.5
        "Is MAC remembering everything?":
            player "Do y'all think MAC will develop based on what we do?"
            $ AddChatter(vig2_sc5_reactcomment3)
            pause 0.5
        "MAC shield your eyes!":
            player "MAC, not gonna lie to you buddy, we might kill so many people."
            $ AddChatter(vig2_sc5_reactcomment4)
            pause 0.5
            $ AddChatter(vig2_sc5_reactcomment5)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc6_out_reflect():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Reflect on the confrontation."
        "Lotta violence.":
            player "Well that was messy..."
            $ AddChatter(vig2_sc6_out_reactcomment1)
            pause 0.5
        "I messed up.":
            player "Definitely could've done that a lot better."
            $ AddChatter(vig2_sc6_out_reactcomment2)
            pause 0.5
            $ AddChatter(vig2_sc6_out_reactcomment3)
            pause 0.5
        "Hell yeah!":
            player "Yeah that feels like the way that should've gone."
            $ AddChatter(vig2_sc6_out_reactcomment4)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc6_mar_reflect():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Reflect on the stealth mission."
        "We just had to sneak in?":
            player "So that was the big stealth mission?"
            $ AddChatter(vig2_sc6_mar_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc6_mar_reactcomment2)
            pause 0.5
        "Definitely the right way.":
            player "Quick and quient, best strategy."
            $ AddChatter(vig2_sc6_mar_reactcomment3)
            pause 0.5
        "We're gonna get caught for sure!":
            player "Those guards are definitely coming back after us afterwards."
            $ AddChatter(vig2_sc6_mar_reactcomment4)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc7_bigreveal():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Respond to Reginald."
        "True.":
            player "I mean he's not wrong..."
            $ AddChatter(vig2_sc7_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc7_reactcomment2)
            pause 0.5
        "This is another level though.":
            player "Listen I've done some terrible things, but destroying an aid ship is crazy."
            $ AddChatter(vig2_sc7_reactcomment3)
            pause 0.5
            $ AddChatter(vig2_sc7_reactcomment4)
            pause 0.5
        "Say nothing.":
            player "..."
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc8_out_postchoice():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "After your choice."
        "We had no choice.":
            player "I have to do what I have to do."
            $ AddChatter(vig2_sc8_out_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment2)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment3)
            pause 0.5
        "It's good to be bad!":
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
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc8_out_reflect():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Reflect on your choice."
        "Jennica's upset.":
            player "I think we lost Jennica's trust a bit."
            $ AddChatter(vig2_sc8_out_reactcomment7)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment8)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment9)
            pause 0.5
        "Was that wrong?":
            player "Maybe that was too much..."
            $ AddChatter(vig2_sc8_out_reactcomment10)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment11)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment12)
            pause 0.5
        "Get wrecked!":
            player "Bye bye, Sallent."
            $ AddChatter(vig2_sc8_out_reactcomment13)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment14)
            pause 0.5
            $ AddChatter(vig2_sc8_out_reactcomment15)
            if baseGuardKilled == True:
                $ AddChatter(vig2_sc8_out_reactcomment16)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc9_out_end():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Reflect on the Outlaw choice."
        "Matticus will get his karma.":
            player "Don't worry, I'll make sure Matticus gets his."
            $ AddChatter(vig2_sc9_out_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc9_out_reactcomment2)
            pause 0.5
        "A new friend?":
            player "A Matticus ally run maybe?"
            $ AddChatter(vig2_sc9_out_reactcomment3)
            pause 0.5
            $ AddChatter(vig2_sc9_out_reactcomment4)
            pause 0.5
        "So much more content!":
            player "I can't believe I missed stuff like this on my first playthrough."
            $ AddChatter(vig2_sc9_out_reactcomment5)
            pause 0.5
            $ AddChatter(vig2_sc9_out_reactcomment6)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc8_mar_reacttoregi():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Reginald."
        "Add him to the pile!" if gunsBlazing == True:
            player "Looks like we're going to get another body."
            $ AddChatter(vig2_sc8_mar_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment2)
            pause 0.5
        "Predictable.":
            player "Of course he does."
            $ AddChatter(vig2_sc8_mar_reactcomment3)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment4)
            pause 0.5
        "Can we persuade him?":
            player "Maybe we can talk our way out of this?"
            $ AddChatter(vig2_sc8_mar_reactcomment5)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment6)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc8_mar_reacttoregistun():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to stunning Reginald."
        "Better than he deserved.":
            player "I mean if we would've killed him that wouldn't be a problem."
            $ AddChatter(vig2_sc8_mar_reactcomment7)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment8)
            pause 0.5
        "Fair enough.":
            player "I guess that makes sense."
            $ AddChatter(vig2_sc8_mar_reactcomment9)
            pause 0.5
        "Get stunned!":
            player "That felt pretty good."
            $ AddChatter(vig2_sc8_mar_reactcomment10)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment11)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc8_mar_reacttoregibribe():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to the bribe."
        "Easy.":
            player "Welp, that was easy."
            $ AddChatter(vig2_sc8_mar_reactcomment12)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment13)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment14)
            pause 0.5
        "Better than he deserved.":
            player "It would've felt better to shoot him."
            $ AddChatter(vig2_sc8_mar_reactcomment15)
            pause 0.5
            $ AddChatter(vig2_sc8_mar_reactcomment16)
            pause 0.5
        "This is getting expensive.":
            player "Do we even have that kind of money?"
            $ AddChatter(vig2_sc8_mar_reactcomment17)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig2_sc9_mar_end():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Reflect on the Marshal choice."
        "Too easy tbh.":
            player "That was a bit too convenient, to be honest."
            $ AddChatter(vig2_sc9_mar_reactcomment1)
            pause 0.5
            $ AddChatter(vig2_sc9_mar_reactcomment2)
            pause 0.5
        "Sweet!":
            player "Honestly couldn't ask to be in a better spot."
            $ AddChatter(vig2_sc9_mar_reactcomment3)
            pause 0.5
            $ AddChatter(vig2_sc9_mar_reactcomment4)
            pause 0.5
        "Was this the best choice?":
            player "Definitely should've blown up the ship."
            $ AddChatter(vig2_sc9_mar_reactcomment5)
            pause 0.5
            $ AddChatter(vig2_sc9_mar_reactcomment6)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return


######Below this is code for Blueit and Flinch in Vignette 2##############
label vig2_blueit_allistarthread():
    $ blueitImage = "socials/allistar thread.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig2_blueit_matticusthread():
    $ blueitImage = "socials/matticus thread.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show major choice thread at top:
    #    zoom 1.5
    call screen blueitButtonCheck
    return

label vig2_blueit_copoutthread():
    $ blueitImage = "socials/copout thread.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show romance thread at top:
    #    zoom 1.5
    call screen blueitButtonCheck
    return

label vig2_blueit_stealththread():
    #show first game thread at top:
    #    zoom 1.5
    $ blueitImage = "socials/stealth thread.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    call screen blueitButtonCheck
    return


###Targets for Flinch#####
label vig2_analytics_viewcount():
    $ flinchCheck += 3
    $ viewcountCheck_vig2 = True
    hide screen viewershipButton_vig2
    "this is a test"
    show screen viewershipButton_vig2

