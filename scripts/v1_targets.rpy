###This script contains the target labels that interactable stream comments can redirect to for vignette 1.
###This script also contains the target labels for interacting with Flinch Analytics and Blueit Threads

#Chatter labels
label vig1_sc1_startStream():
    $ macroChoice = True
    $ narrator = reg_narrator
    hide screen streamerCommentary
    hide screen chatTutorial2
    "Alright, gang, sorry for the extended break! Roommate needed help moving some furniture."
    "Let's catch up to speed."
    "We're on the run from BigCorp cause we stole our new robot friend MAC from their facilities and we are {i}not{/i} giving him back."
    "But he's been having some wiring issues that we gotta fix before we get to dropping him off with the humanitarian organization."
    "So we hit up our old pal Allistar the mechanic to fix up MAC and had to grab some thermal paste from the local shop." 
    "And I'ma be honest, that shopkeep was quite rude."
    "But we did a bit of bribing, got the paste, and now we're meeting back up with the boys."
    "Let's go!"
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig1_sc2_whoQuestion():
    $ macroChoice = True
    $ vig1_sc2_comment2.click = False
    $ narrator = reg_narrator
    hide screen chatTutorial
    menu:
        "A viewer wants to catch up on some back story."
        "Explain \"Deadeye\"":
            player "\"Deadeye\" is the nickname for Ama Reyes."
            player "She was Moze's mentor when she was running with the Snake Hawks."
            player "But then Ama ran a heist against BigCorp that went south and got almost the entire gang wiped out."
            player "This was all lore stuff from before the first game, actually."
            $ AddChatter(vig1_sc2_comment2_csSH)
            pause 0.5
            $ AddChatter(vig1_sc2_comment3)
            pause 0.5
        "Explain Snake Hawks":
            player "The Snake Hawks were the gang that Moze and Jennica ran with before they became mercenaries."
            player "Allistar was part of the gang too, that's why he has the same tattoo as Moze."
            player "They used to be a big deal in the Outposts until most of 'em got wiped out."
            player "This was all lore stuff from before the first game, actually."
            $ AddChatter(vig1_sc2_comment2_csAma)
            pause 0.5
            $ AddChatter(vig1_sc2_comment3)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig1_sc2_thankCS():
    $ macroChoice = True
    $ vig1_sc2_comment2_csSH.click = False
    $ vig1_sc2_comment2_csAma.click = False
    $ narrator = reg_narrator
    menu:
        "Thanks, Coriolis!":
            $ csEngagement += 1
            "Thanks for filling in, Coriolis!"
        "Say nothing":
            pass
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig1_sc2_allistarhunk():
    $ macroChoice = True
    $ vig1_sc2_comment6.click = False
    $ narrator = reg_narrator
    hide screen chatTutorial
    menu:
        "The stream seems to like Allistar."
        "He's great!":
            $ csEngagement += 1
            player "Hunky mechanic coming up clutch!"
            $ allistarSuspicious = False
        "I'm a bit suspicious":
            player "Honestly chat, I think we gotta be careful about him."
            $ allistarSuspicious = True
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig1_sc2_combatReact():
    hide screen chatTutorial2
    hide screen streamerCommentary
    $ vig1_sc2_streamer1.click = False
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "What do I want to say?"
        "Never didn't have it!":
            player "Not a problem."
            player "BC gotta do more than that to stop the Oakley!"
            $ AddChatter(vig1_sc2_comment12)
            pause 0.5
        "That was tough!":
            player "Whew, that was some tough combat." 
            player "Got me sweating a bit, chat."
            $ AddChatter(vig1_sc2_comment13)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig1_sc2_houseExplosion():
    $ macroChoice = True
    $ vig1_sc2_comment16.click = False
    $ narrator = reg_narrator
    menu:
        "I did consider it":
            player "I thought about it for a second."
            player "But I think it was a bit extreme."
        "No way":
            player "Just took a second to read the choices."
            player "No way I was going that violent."
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    return

label vig1_sc3_banditConvo():
    $ macroChoice = True
    $ vig1_sc3_comment3_bandit0.click = False
    $ narrator = reg_narrator
    menu:
        "Bandit asked if I'm a big Oakley fan"
        "Massive!":
            player "Oh yeah, big time!"
            player "My brother and I got hooked on the first game, played it a bunch of times."
            player "What about you?"
            $ AddChatter(vig1_sc3_comment3_bandit1)
            pause 3.0
            $ AddChatter(vig1_sc3_comment3_bandit2)
            pause 1.0
        "I'm a fan.":
            player "Yeah, I've been waiting on this game for a while."
            player "My brother and I played the first together so it's got a special place in my heart."
            player "What about you?"
            $ AddChatter(vig1_sc3_comment3_bandit1)
            pause 3.0
            $ AddChatter(vig1_sc3_comment3_bandit4)
            pause 2.0
            $ AddChatter(vig1_sc3_comment3_bandit2)
            pause 1.0
        "My brother's a bigger fan than me.":
            player "I like the game, but honestly my little brother is a bigger fan than me."
            player "We got hooked on the first game, played it a bunch of times."
            player "He read up on all the prequel comics and stuff after that."
            $ AddChatter(vig1_sc3_comment3_bandit1)
            pause 3.0
            $ AddChatter(vig1_sc3_comment3_bandit4)
            pause 2.0
            $ AddChatter(vig1_sc3_comment3_bandit2)
            pause 1.0
    menu:
        "Marshal.":
            player "I would always tell myself I was gonna replay Oakley 1 as Outlaw Moze."
            player "Then I'd get to that first choice with the detective and could never not go Marshal hahaha."
            $ AddChatter(vig1_sc3_comment3_bandit3)
            pause 1.0
    menu:
        "Ask Bandit's favorite Oakley character.":
            player "So, Bandit, time to read the tea leaves of your soul."
            player "Who's your favorite Oakley character?"
            $ AddChatter(vig1_sc3_comment3_bandit5)
            pause 2.0
            $ AddChatter(vig1_sc3_comment3_bandit6)
            pause 3.0
            $ AddChatter(vig1_sc3_comment3_bandit7)
            pause 1.0
        
        
    menu:
        "Bandit asked who my favorite Oakley character is."
        "MAC":
            $ kcEngagement += 1
            player "Honestly, same."
            player "I wasn't sure how they would characterize him for a full game, but he's so adorable!"
            $ AddChatter(vig1_sc3_comment3_bandit8)
            pause 1.0
            $ AddChatter(vig1_sc3_comment3_bandit9)
            pause 1.0
            player "Ooh that would be interesting. Hope it's true!" 
            player "Well, let's get back to the game!"
        "Teresa":
            $ pdEngagement += 1
            player "I'm a big fan of Teresa."
            player "She always comes up with clutch plans."
            $ AddChatter(vig1_sc3_comment3_bandit10)
            pause 1.0
            player "Maybe just a bit haha" 
            player "Well, let's get back to the game!"
        "Allistar":
            player "Also recency bias, but it's been really cool to connect with Allistar."
            player "This hunky mechanic has good vibes."
            $ AddChatter(vig1_sc3_comment3_banditAllistar)
            pause 2.0
            "That's...ominous. Let's get back to the game."
        "Jennica":
            $ csEngagement += 1
            player "Jennica all the way."
            player "She's the reason the Oakley gets anywhere!"
            $ AddChatter(vig1_sc3_comment3_bandit11)
            pause 1.0
            player "Definitely haha" 
            player "Well, let's get back to the game!"
    $ macroChoice = False
    $ narrator = reg_narrator
    return

######Below are targets for Flinch Analytics and Reddit#####

#Flynch Analytics
label vig1_analytics_topfan():
    $ flinchCheck += 1
    $ topfanCheck = True
    hide screen viewershipButton
    "Coriolis has been around since your second year of streaming."
    "You haven't even talked to them outside of the stream, but they always seem to be so happy to be in the chat."
    "It's almost like they're a second mod."
    show screen viewershipButton
    return

label vig1_analytics_alignment():
    $ flinchCheck += 1
    $ alignmentCheck = True
    hide screen viewershipButton
    "Moze's alignment is almost entirely Marshal."
    "But there's a little bit of red for Outlaw."
    menu:
        "It's exciting":
            $ enthusiasm += 1
            "It's actually kind of exciting!"
            "Kind of like the start of a new adventure."
        "It looks weird":
            $ reluctance += 1
            "Looking at it here, it feels odd."
            "Maybe you'll get used to it?"
    show screen viewershipButton
    return

label vig1_analytics_viewcount():
    $ flinchCheck += 1
    $ viewcountCheck = True
    hide screen viewershipButton
    "Wow, look at that spike at the end."
    "It makes the viewership numbers at the start of the stream look so small."
    menu:
        "It was fun!":
            $ energy += 1
            "Having so many people in chat at once was awesome."
            "Kind of felt like we were all playing together."
            "Past streams felt like that occasionally."
            "But this was a different scale."
        "Did I earn this?":
            $ energy -= 1
            "Getting all those viewers was nice, but did you really earn this?"
            "They came to the stream because of 8bitBANDIT."
            "You were just lucky."
            "But luck is opportunity plus preparation."
    "Hopefully you can keep up this momentum."
    show screen viewershipButton
    return

label vig1_analytics_audience():
    $ flinchCheck += 1
    $ audienceCheck = True
    hide screen viewershipButton
    "That spike from the raid boosted your average audience all the way to thirteen."
    "Not everyone from the raid will stick around next time though."
    "You'll still have to keep around ten viewers per stream to get Affiliate."
    menu:
        "Think about your last attempt":
            "Last time you tried this you missed by just one average viewer."
            "It was brutal."
        "Think about your conversation with Jessie":
            "Playing the Outlaw route might help with that."
            "But what if you don't like it?"
    "You said this would be your last try to get Affiliate."
    "If you don't, you'll probably stop streaming."
    "It's just hard to justify the time while your schoolwork is so busy."
    "It wouldn't be the end of the world...but it would suck."
    show screen viewershipButton
    return

#Blueit Threads
label vig1_blueit_launchthread():
    $ blueitImage = "Socials/launch thread.png"
    $ yb = 1080
    $ blueitLaunchCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig1_blueit_firstchoice():
    $ blueitImage = "Socials/major choice thread.png"
    $ yb = 1080
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show major choice thread at top:
    #    zoom 1.5
    call screen blueitButtonCheck
    return

label vig1_blueit_romance():
    $ blueitImage = "Socials/romance thread.png"
    $ yb = 1080
    show screen blueitThread
    #show romance thread at top:
    #    zoom 1.5
    call screen blueitButtonCheck
    return

label vig1_blueit_firstgame():
    #show first game thread at top:
    #    zoom 1.5
    $ blueitImage = "Socials/first game thread.png"
    $ yb = 1080
    show screen blueitThread
    call screen blueitButtonCheck
    return

label vig1_blueit_glitch():
    #show glitch thread at top:
    #    zoom 1.5
    $ blueitImage = "Socials/glitch thread.png"
    $ yb = 1080
    show screen blueitThread
    call screen blueitButtonCheck
    return
