label vig4_sc1_pdParanoia():
    $ macroChoice = True
    $ vig4_sc1_comment5.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "Is Moze over her paranoia?"
        "For sure.":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Oh yeah, I think she was able to work through a lot of that in the last episode."
            player "Especially if the crew isn't at each other's throats anymore."
        "No way.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "No way. You don't just magically get over that stuff."
            player "I'd expect we're in for some hallucinations or maybe a trippy dream sequence."            
        "I don't know.":
            $ reactImage = "stream ui/reactconversational.png"   
            player "Hmm interesting idea. Honestly, I don't know."
            player "They're not in as stressful a position anymore, but that's not something you just like get over."
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

label vig4_sc1_csRomance():
    $ macroChoice = True
    $ vig4_sc1_2_comment20.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "The Chat is asking who I want to romance again."
        "I'm team Jennica.":
            $ reactImage = "stream ui/reactthumbsup.png"
            $ csEngagement += 1
            $ kcEngagement -=1
            player "Oh, I'm team Jennica for sure."
            player "Friendly, sensitive, and a crack pilot. What's not to love?"
            $ AddChatter(vig4_sc1_interact_comment1)
        "I'm team Teresa.":
            $ reactImage = "stream ui/reactthumbsup.png"
            $ csEngagement -=1
            $ kcEngagement += 1
            player "Oh, I'm team Teresa for sure."
            player "Smart, loyal, and a clever engineer in the clutch. What's not to love?"
            $ AddChatter(vig4_sc1_interact_comment2)
        "I'm still hoping for Ama." if deadeyeApproval >= 2:
            $ reactImage = "stream ui/reactconfident.png"
            $ pdEngagement += 2
            $ csEngagement += 1
            $ kcEngagement += 1
            player "I'm still holding out hope for an Ama path."
            player "We can fix her, Chat!"
            $ AddChatter(vig4_sc1_interact_comment3)
            pause 0.5
            $ AddChatter(vig4_sc1_interact_comment4)
            pause 0.5
            $ AddChatter(vig4_sc1_interact_comment5)
        "I'm not feeling a romance.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            $ csEngagement -= 1
            $ kcEngagement -= 1
            $ pdEngagement += 1
            player "I'm actually not feeling much of a romance in this game."
            player "The characters are great, but I don't see the chemsitry."
            $ AddChatter(vig4_sc1_interact_comment6)
            pause 0.5
            $ AddChatter(vig4_sc1_interact_comment7)
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

label vig4_sc1_kcPrediction():
    $ macroChoice = True
    $ vig4_sc2_1_comment1.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "How do I think the story's going to play out?"
        "I have no idea.":
            $ reactImage = "stream ui/reactconversational.png"
            $ pdEngagement -= 1
            $ kcEngagement -= 1
            player "I have no clue to be honest."
            player "I've learned that you can't predict where things are going to go with this story."
        "Something's gonna go wrong.":
            $ reactImage = "stream ui/reactthinking.png"
            $ csEngagement += 1
            player "Whatever it is, I just know something's gonna go wrong."
            player "Can't have an epic finale without some drama."
            #$ AddChatter(vig4_sc2_interact_comment1)
        "Ama's going to come back for sure.":
            $ reactImage = "stream ui/reactconfident.png"
            $ kcEngagement += 1
            $ pdEngagement += 1
            player "I think Ama's going to kidnap MAC, and we're gonna have to fight her and BigCorp to get him back."
            player "We didn't get a proper resolution to her story in Episode 3, so I'd be shocked if she doesn't come back in some capacity."
            $ AddChatter(vig4_sc2_interact_comment2)
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

label vig4_sc2_rube():
    $ macroChoice = True
    $ vig4_sc2_1_comment8.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "Should I play into this?"
        "Say nothing.":
            player "..."
            pass
        "Rube!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Rube!"
            $ AddChatter(vig4_sc2_1_comment9)
            pause 0.5
            $ AddChatter(vig4_sc2_1_comment10)
            pause 0.5
            $ AddChatter(vig4_sc2_1_comment11)
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

label vig4_sc2_peacefulTown():
    $ macroChoice = True
    $ vig4_sc2_6_comment1.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "Do I believe Polaris is a peaceful town."
        "No way.":
            $ reactImage = "stream ui/reactthinking.png"
            player "No way. There's something going on here that he's not telling us."
        "I buy it.":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "It seemed pretty chill while we were walking in. They're at least not actively hostile, that's for sure."
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

#label vig4_sc2_AFKDream(): #I commented out the chat that would lead to this label
#    $ macroChoice = True
#    $ vig4_sc2_6_comment8.click = False
#    $ narrator = reg_narrator
    #menu:
    #    "Fill the menu with something."
#    $ macroChoice = False
#    if macroChoice == False:
#        $ narrator = alt_narrator
#    else:
#        $ narrator = reg_narrator
#    $ reactImage = "stream ui/reactneutral.png"
#    return

label vig4_sc2_elliotEntrance():
    #$ screenFreeze = False
    stop music fadeout 1.0
    $ macroChoice = True
    $ vig4_sc2_6_comment43.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    play music "soundtrack/elsGroove.wav" volume 1.0 fadein 1.0
    menu:
        "Elliot joined the chat!"
        "Aren't you supposed to be on a date?":
            $ reactImage = "stream ui/reactthinking.png"
            player "Hey El! Aren't you supposed to be on a date right now?"
            $ AddChatter(vig4_bro_comment1)
            pause 1.0
            player "Oh my god that's so sweet! It's great to have you here!"
            $ AddChatter(vig4_bro_comment3)
            menu:
                player "Oh my god that's so sweet! It's great to have you here!"
                "Everyone say \"hi\" to my brother!":
                    $ reactImage = "stream ui/reactthumbsup.png"
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
                    player "Alright, alright, let's get back to it."
                    $ AddChatter(vig4_bro_comment26)
                "Let's catch Elliot up to speed.":
                    $ reactImage = "stream ui/reactconversational.png"
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
                    player "Alright, alright, let's get back to it."
                    $ AddChatter(vig4_bro_comment26)
        "So good to see you!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "El! It's so good to have you in chat!"
            $ AddChatter(vig4_bro_comment2)
            player "Oh wow, that's so sweet! It's great to have you here!"
            $ AddChatter(vig4_bro_comment3)
            menu:
                player "Oh wow, that's so sweet! It's great to have you here!"
                "Everyone say \"hi\" to my brother!":
                    $ reactImage = "stream ui/reactthumbsup.png"
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
                    player "Alright, alright, let's get back to it."
                    $ AddChatter(vig4_bro_comment26)
                "Let's catch Elliot up to speed.":
                    $ reactImage = "stream ui/reactconversational.png"
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
                    player "Alright, alright, let's get back to it."
                    $ AddChatter(vig4_bro_comment26)
        "Everyone, say hi to my brother!":
            $ reactImage = "stream ui/reactconfident.png"
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
            player "Alright, alright, let's get back to it."
            $ AddChatter(vig4_bro_comment27)
    stop music fadeout 2.0
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

label vig4_sc3_festivalRomance():
    $ macroChoice = True
    $ vig4_sc3_2_vega_comment2.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "kitcat's asking why I'm not romancing Jennica or Teresa."
        "We can't if we want to romance Ama.":
            $ reactImage = "stream ui/reactconversational.png"
            player "I saw a thread on blueit that said we can't romance Jenn or Teresa if we want to romance Ama."
            player "And I'm still holding out hope for the Ama drama!"
            $ AddChatter(vig4_sc3_interact_comment1)
            pause 0.5
            $ AddChatter(vig4_sc3_interact_comment2)
        "I want to get to know Vega more.":
            $ reactImage = "stream ui/reactthinking.png"
            player "I know, I know, but I want to get to know Vega better."
            player "Maybe we can learn more about Coil from her too."
            $ AddChatter(vig4_sc3_interact_comment3)
        "Say nothing.":
            player "..."
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

label vig4_sc3_pdCoilCommentary():
    $ macroChoice = True
    $ vig4_sc3_3_comment36.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "How do I feel about Coil's actions?"
        "I don't like him.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "I don't like him. I feel like he didn't even try to make a case for us."
            $ AddChatter(vig4_sc3_interact_comment4)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter(vig4_sc3_interact_comment5)
        "I think he's right.":
            $ reactImage = "stream ui/reactthinking.png"
            player "The thing is, what he's saying isn't necessarily wrong."
            player "Maybe we haven't been the best parental figure for MAC."
            $ AddChatter(vig4_sc3_interact_comment6)
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

label vig4_sc3_csCoilCommentary():
    $ macroChoice = True
    $ vig4_sc3_3_comment39.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "How do I feel about Coil's actions?"
        "I don't like him.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            $ pdEngagement += 1
            $ csEngagement -= 1
            player "I don't like him. I feel like he didn't even try to make a case for us."
            $ AddChatter(vig4_sc3_interact_comment4)
            pause 0.5
            $ AddChatter(vig4_sc3_interact_comment5)
        "I think he's right.":
            $ reactImage = "stream ui/reactthinking.png"
            $ pdEngagement -= 1
            $ csEngagement += 1
            player "The thing is, what he's saying isn't necessarily wrong."
            player "Maybe we haven't been the best parental figure for MAC."
            $ AddChatter(vig4_sc3_interact_comment7)
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

label vig4_sc4_kcNoOffer():
    $ macroChoice = True
    $ vig4_sc4_1_comment31.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "Why didn't I choose to ally with Ama?"
        "Cause she's been trying to kill us.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Ama's been trying to kill us for months, and now she just decides to swap sides?"
            player "We can't just forgive her that fast. She has to earn it."
            $ AddChatter(vig4_sc4_interact_comment1)
            pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc4_interact_comment2)
        "We don't need her.":
            $ reactImage = "stream ui/reactconfident.png"
            player "We don't need her. Our crew is tough enough to handle what's coming up on our own."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc4_interact_comment3)
                pause 0.5
            $ AddChatter(vig4_sc4_interact_comment4)
        "We can't trust her.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "I mean, we just can't trust her."
            player "Especially after Episode 3, I wouldn't want her watching my back."
            $ AddChatter(vig4_sc4_interact_comment4)
            pause 0.5
            $ AddChatter(vig4_sc4_interact_comment5)
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

#label vig4_sc5_csClimax(): #Made this noninteractable to make managing the vignette a bit easier
#    $ macroChoice = True
#    $ vig4_sc5_1_comment27.click = False
#    $ narrator = reg_narrator
    #menu:
    #    "Fill the menu with something."
#    $ macroChoice = False
#    if macroChoice == False:
#        $ narrator = alt_narrator
#    else:
#        $ narrator = reg_narrator
#    $ reactImage = "stream ui/reactneutral.png"
#    return

label vig4_sc5_oscarReturn():
    $ macroChoice = True
    $ vig4_sc6_defend_1_comment1.click = False
    $ vig4_sc6_attack_1_ama_comment1.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "swayy0scar! They were in chat for the first stream, but haven't been around since."
        "Welcome back!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Hey, Oscar! Welcome back!"
            player "It's been a while, what's going on with you?"
            $ AddChatter(vig4_sc5_interact_comment1)
            pause 0.5
            $ AddChatter(vig4_sc5_interact_comment2)
            pause 0.5
            $ AddChatter(vig4_sc5_interact_comment3)
            pause 0.5
            $ AddChatter(vig4_sc5_interact_comment4)
        "Say nothing.":
            player "..."
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

label vig4_sc6_ripTank():
    $ macroChoice = True
    $ vig4_sc6_defend_4_comment5.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "Chat seems sad about the tank being destroyed."
        "RIP.":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Another fallen soldier. Get those RIPs in chat."
            $ AddChatter(vig4_sc6_interact_comment1)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment2)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc6_interact_comment3)
                pause 0.5
            $ AddChatter(vig4_sc6_interact_comment4)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment5)
        "Say nothing.":
            player "..."
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

label vig4_sc6_pdGoodPerson():
    $ macroChoice = True
    $ vig4_sc6_attack_3_ama_comment19.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "Chat is talking about Moze's morality."
        "Moze's flexibility is what makes her a good character.":
            $ reactImage = "stream ui/reactthinking.png"
            $ pdEngagement += 2
            $ kcEngagement += 1
            $ csEngagement += 1
            player "I always thought the great thing about Moze was how flexible she could be."
            player "Like, considering the galaxy that she lives in, it's believable for her to lean into the violence or try to more peaceful in opposition to it."
            player "And the beauty of that, is you don't have to play her as strictly one or the other. She can be both in equal measure."
            $ AddChatter(vig4_sc6_interact_comment6)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment7)
        "Who cares about Moze's morality, this is fun!":
            $ reactImage = "stream ui/reactcelebrate.png"
            $ pdEngagement += 1
            $ csEngagement == 1
            player "Who cares about her character arc. This is just a good time!"
            $ AddChatter(vig4_sc6_interact_comment8)
        "Moze getting \"worse\" is also a good story.":
            $ reactImage = "stream ui/reactconfident.png"
            $ pdEngagement += 1
            player "Moze failing at \"doing better\" and actually \"doing worse\" is an interesting story."
            player "I think it reflects the complexity of the galaxy and how hard it is for her to change. Especially considering her mentor."
            $ AddChatter(vig4_sc6_interact_comment9)
            pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc6_interact_comment10)
        "It does feel inconsistent with the game's themes.":
            $ reactImage = "stream ui/reactunsure.png"
            $ pdEngagement -= 1
            player "Yeah, I'll admit, a lot of Outlaw Moze's decisions do feel kind of inconsistent with the game's themes."
            $ AddChatter(vig4_sc6_interact_comment11)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment12)
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

label vig4_sc6_reggieReaction():
    $ macroChoice = True
    $ vig4_sc6_defend_5_comment19.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "Chat is reacting to Reginald's return."
        "REGGIE!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "REGGIE!"
            player "HE'S BACK!"
            $ AddChatter(vig4_sc6_interact_comment14)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment15)
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc6_interact_comment16)
                pause 0.5
                $ AddChatter(vig4_sc6_interact_comment17)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment18)
        "Is Matticus going to want something?":
            $ reactImage = "stream ui/reactunsure.png"
            player "Oh god, is Matticus going to want something for this?"
            $ AddChatter(vig4_sc6_interact_comment13)
        "Say nothing.":
            player "..."
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

label vig4_sc7_kcWhyNoRomance():
    $ macroChoice = True
    $ vig4_sc7_3_ama_comment56.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "kitcat wants to know why I backed out of romancing Ama."
        "They're not right for each other.":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "I don't think they're right for each other."
            player "Plus, Ama's kind of a mother figure to Moze."
            player "It didn't end up feeling good in the end. Sorry, chat."
            $ AddChatter(vig4_sc7_interact_comment2)
        "Too soon.":
            $ reactImage = "stream ui/reactunsure.png"
            player "I think there's something between them, but saying \"I love you\" right now feels a bit rushed."
            $ AddChatter(vig4_sc7_interact_comment1)
        "Say nothing.":
            player "..."
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

label vig4_pdEndFeeling():
    $ macroChoice = True
    $ vig4_sc7_epilogue_comment4.click = False
    $ narrator = reg_narrator
    $ commentVariable = True
    menu:
        "How am I feeling now that I'm at the end of the game?"
        "Tired.":
            $ reactImage = "stream ui/reactunsure.png"
            player "I'll be honest Chat, I'm beat haha."
            player "This has been a long time coming. It's been super fun, but I am tired."
            player "A bit relieved to be bringing this to a closed."
            $ AddChatter(vig4_epilogue_interact_comment1)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_epilogue_interact_comment2)
                pause 0.5
            $ AddChatter(vig4_epilogue_interact_comment3)
        "Ecstatic.":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Oh I feel amazing, ecstatic even!"
            player "That climax was so cool and all the drama between the characters was amazing!"
            player "I think I'm gonna be riding this high for a while haha."
            $ AddChatter(vig4_epilogue_interact_comment4)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_epilogue_interact_comment5)
                pause 0.5
            $ AddChatter(vig4_epilogue_interact_comment3)
        "Kind of sad.":
            $ reactImage = "stream ui/reactconversational.png"
            player "In all honesty, I'm a bit sad that it's over."
            player "This has been so much fun and it's ending really well."
            player "I just wish there was more!"
            $ AddChatter(vig4_epilogue_interact_comment6)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_epilogue_interact_comment7)
                pause 0.5
            $ AddChatter(vig4_epilogue_interact_comment3)
        "Not sure.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Honestly, I don't know what to feel."
            player "I'm like sad, but also happy."
            player "It just feels surreal for this gaming to actually be coming to an end."
            $ AddChatter(vig4_epilogue_interact_comment1)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_epilogue_interact_comment2)
                pause 0.5
            $ AddChatter(vig4_epilogue_interact_comment3)
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

### Streamer Reacts ##########################

label vig4_sc1_macjokes():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "MAC just made a joke."
        "MAC can joke!?":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Chat did MAC just tell a joke!?"
            player "That's crazy!"
            $ AddChatter (vig4_sc1_react_comment1)
            $ AddChatter (vig4_sc1_react_comment2)
            pause 0.5
        "That's so cute!":
            $ reactImage = "stream ui/reactshocked.png"
            player "Holy crap, MAC's a lil joker!"
            player "Adorable!"
            $ AddChatter (vig4_sc1_react_comment3)
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

label vig4_sc2_trustvillager():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Can you trust this person?"
        "Suspicious.":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthinking.png"
            player "Not sure we can trust him."
            player "Kinda sus that he's so friendly."
            $ AddChatter(vig4_sc2_react_comment1)
            pause 0.5
        "They seem to mean well enough.":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "He seems to be friendly!"
            player "I say we trust him!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_react_comment2)
                pause 0.5
        "This is going to go poorly.":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactunsure.png"
            player "This is going to go so bad."
            player "This might've been the wrong call."
            $ AddChatter(vig4_sc2_react_comment3)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc2_react_comment4)
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

label vig4_sc2_macischanging():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "MAC's personality has been changing."
        "Cool!":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Yeah he's been changing since the start right?"
            player "Really cool how that's been happening as we go!"
            $ AddChatter(vig4_sc2_react_comment5)
            pause 0.5
        "Obviously.":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "Yeah, duh."
            player "Isn't that what the game's been doing all along?"
            $ AddChatter(vig4_sc2_react_comment6)
            pause 0.5
        "What have we been teaching him?":
            $ kcEngagement += 1
            if marshal > outlaw:
                $ reactImage = "stream ui/reactunsure.png"
                player "Oh damn! MAC's been learning from us!"
                player "Super cool!"
                $ AddChatter(vig4_sc2_react_comment7)
            else: 
                $ reactImage = "stream ui/reactshocked.png"
                player "Oh no! MAC's been learning from us!"
                player "What if he's been picking up all the wrong things!?"
                $ AddChatter(vig4_sc2_react_comment8)
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

label vig4_sc2_coilshield():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Teresa's blaster just got absorbed by some kind of shield."
        "Cool!":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Woah!"
            player "This old man's got some cool tech!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_react_comment9)
                pause 0.5
        "Of course he's got tricks.":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "I knew it wouldn't go over well."
            player "There's obviously more to this old guy than meets the eye."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc2_react_comment10)
                pause 0.5
        "Shoot him again!":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Fire again, Teresa!"
            player "That shield ain't limitless!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_react_comment11)
                pause 0.5
            $ AddChatter(vig4_sc2_react_comment12)
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

label vig4_sc2_macchant():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "MAC just saved Moze and Teresa!"
        "MAC for the win!":
            $ kcEngagement += 1
            $ pdEngagement += 1
            $ csEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            #set variable for mac chant
            player "MAC coming in clutch!"
            player "MAC! MAC! MAC!"
            $ AddChatter(vig4_sc2_react_comment13)
            pause 0.5
            $ AddChatter(vig4_sc2_react_comment14)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc2_react_comment15)
            $ AddChatter(vig4_sc2_react_comment16)
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_react_comment17)
            pause 0.5
            $ AddChatter(vig4_sc2_react_comment18)
            pause 0.5
        "MAC's got some upgrades!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Badass!"
            player "MAC's a bonafide outlaw!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_react_comment19)
                pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_react_comment20)
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

label vig4_sc2_longjourney():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Talk about how hard the journey's been."
        "It's taken forever!":
            $ reactImage = "stream ui/reactconversational.png"
            player "Yeah, it took forever."
            player "And it was awful!"
            if viewershipHigh == True:
                $ AddChatter(vig4_sc2_react_comment21)
                pause 0.5
        "You call that hard?":
            $ reactImage = "stream ui/reactconfident.png"
            player "Nope! Didn't notice at all."
            player "Pretty easy actually hahaha!"
            $ AddChatter(vig4_sc2_react_comment22)
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

label vig4_sc2_coilbackstory():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Coil is revealing his backstory."
        "Interesting.":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Wow. You can tell he regrets this."
            player "Coil's got hangups about his old partner."
            $ AddChatter(vig4_sc2_react_comment23)
            pause 0.5
        "Can't side with BigCorp!":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "Damn it, Coil!"
            player "You should've known better than to trust BigCorp!"
            if viewershipHigh == True:
                $ AddChatter(vig4_sc2_react_comment24)
                pause 0.5
            $ AddChatter(vig4_sc2_react_comment25)
            #add chatter
            pause 0.5
        "Boring!":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Ugh, this is taking forever."
            player "Enough backstory already!"
            $ AddChatter(vig4_sc2_react_comment26)
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

label vig4_sc2_macstays():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "The Dragonflies are going to take MAC from the Oakley!?"
        "No way!":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactshocked.png"
            player "What!? No!"
            player "No chance we're letting that happen chat!"
            $ AddChatter(vig4_sc2_react_comment27)
            pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_react_comment28)
                pause 0.5
        "Makes sense.":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "I mean, I get it."
            if marshal > outlaw:
                player "Like even if we've been good, it's tough to trust ex-Snakehawks."
            else: 
                player "Like we've been pretty violent and chaotic hahaha!"
            $ AddChatter(vig4_sc2_react_comment29)
            pause 0.5
            $ AddChatter(vig4_sc2_react_comment30)
            pause 0.5
        "Not fair!":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "This is bogus chat!"
            player "We took all this risk and got him this far!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_react_comment31)
                pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc2_react_comment32)
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

label vig4_sc3_jenndatelose():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Jennica won this round of {i}Star Battler IV: Destructostar{i}."
        "We never had a chance!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Should've known."
            player "She's the best pilot in the galaxy after all!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3jenn_react_comment1)
                pause 0.5
        "Damn that was close!":
            $ reactImage = "stream ui/reactunsure.png"
            player "Ahh, damn!"
            player "Thought we had her."
            $ AddChatter(vig4_sc3jenn_react_comment2)
            pause 0.5
        "Cute!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Jennica's so cute!"
            player "I don't even care that we lost, chat!"
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3jenn_react_comment3)
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

label vig4_sc3_jenndatewin():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You beat Jennica in this round of {i}Star Battler IV: Destructostar{i}."
        "New pilot on the scene!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Move over Jenn!"
            player "We're taking over pilot duties now!"
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3jenn_react_comment4)
                pause 0.5
        "That was close!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Whew!"
            player "I'm surprised we beat her! That was super close!"
            $ AddChatter(vig4_sc3jenn_react_comment5)
            pause 0.5
        "Cute!":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Awww Jennica's so cute!"
            player "Best girl!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3jenn_react_comment6)
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

label vig4_sc3_jenndatetie():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Moze and Jennica tied in this round of {i}Star Battler IV: Destructostar{i}."
        "Not a bad result!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Getting her to a tie is pretty good in my book."
            player "Wonder if she took it easy on us!"
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3jenn_react_comment7)
                pause 0.5
        "Fair enough.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Makes sense."
            player "She's a way better pilot. It's a win that we tied at all!"
            $ AddChatter(vig4_sc3jenn_react_comment8)
            pause 0.5
        "Cute!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Jennica's so cute!"
            player "I love how competitive she is!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3jenn_react_comment9)
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

label vig4_sc3_jenndatekiss():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Moze and Jennica kissed!"
        "WOOOO!":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Finally!"
            player "Best ship is finally canon, chat!"
            $ AddChatter(vig4_sc3jenn_react_comment10)
            pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3jenn_react_comment12)
                pause 0.5
        "Awwwww.":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "Awwwwww."
            player "They're perfect for each other, chat"
            $ AddChatter(vig4_sc3jenn_react_comment11)
            pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3jenn_react_comment12)
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

label vig4_sc3_jenndaterejection():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Jennica rejected Moze's confession!?"
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
            pause 0.5
            $ AddChatter(vig4_sc3jenn_react_comment15)
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3jenn_react_comment16)
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

label vig4_sc3_teresadatewin():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You beat Teresa at Liar's Dice!"
        "Got her!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Hell yeah!"
            player "Prismari's got nothing on our girl!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3tere_react_comment1)
                pause 0.5
            $ AddChatter(vig4_sc3tere_react_comment2)
            pause 0.5
        "Game of chance after all.":
            $ reactImage = "stream ui/reactconversational.png"
            player "I mean it's a game of luck, right?"
            $ AddChatter(vig4_sc3tere_react_comment3)
            pause 0.5
            $ AddChatter(vig4_sc3tere_react_comment4)
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

label vig4_sc3_teresadatelose():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Teresa beat you at Liar's Dice."
        "She got us!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Damn!"
            player "Prismari's got a heck of a poker face!"
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3tere_react_comment5)
                pause 0.5
            $ AddChatter(vig4_sc3tere_react_comment6)
            pause 0.5
        "Game of chance after all.":
            $ reactImage = "stream ui/reactconversational.png"
            player "I mean it's a game of luck, right?"
            $ AddChatter(vig4_sc3tere_react_comment4)
            pause 0.5
            $ AddChatter(vig4_sc3tere_react_comment3)
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

label vig4_sc3_teresadatekiss():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Moze and Teresa kissed!"
        "WOOOO!":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Finally!"
            player "Best ship is finally canon!"
            $ AddChatter(vig4_sc3tere_react_comment8)
            $ AddChatter(vig4_sc3tere_react_comment10)
            pause 0.5
        "Awwwww.":
            $ kcEngagement += 1
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

label vig4_sc3_teresadaterejection():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Teresa rejected Moze's confession."
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
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3jenn_react_comment16)
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

label vig4_sc3_coil1():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Coil is telling you to leave without MAC."
        "Wow, brutal.":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactconversational.png"
            player "Wow, that really sucks chat."
            player "All this work to get MAC here and just like that..."
            player "Pushed aside."
            $ AddChatter(vig4_sc3coil1_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc3coil1_react_comment2)
            pause 0.5
        "Bullshit!":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "This is bullshit, chat!"
            player "All this work to get MAC here!"
            player "No way we're letting this happen!"
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3coil1_react_comment3)
                pause 0.5
            $ AddChatter(vig4_sc3coil1_react_comment4)
            pause 0.5
            $ AddChatter(vig4_sc3coil1_react_comment5)
            pause 0.5
        "Understandable.":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "Yeah, I mean it makes sense."
            player "Given our reputation..."
            if marshal > outlaw:
                player "We can't expect them to trust us."
            else: 
                player "Why the heck would they trust us?"
            $ AddChatter(vig4_sc3coil1_react_comment6)
            pause 0.5
            $ AddChatter(vig4_sc3coil1_react_comment7)
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

label vig4_sc3_coil2():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Coil took Jennica and Teresa into custody while you were talking with MAC."
        "I should've known!":
            $ reactImage = "stream ui/reactconversational.png"
            player "Yeah no chance they were going to leave us alone."
            player "No trust with these guys chat."
            player "Brutal."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3coil2_react_comment1)
                pause 0.5
            $ AddChatter(vig4_sc3coil2_react_comment2)
            pause 0.5
        "Dammit!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Crap! They got us."
            player "Should've known they wouldn't trust us."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3coil2_react_comment3)
                pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3coil2_react_comment4)
                pause 0.5
        "Understandable.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Yeah I didn't think they'd let us try anything."
            if marshal > outlaw:
                player "Even if we've been good."
            else: 
                player "Like why would they?"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3coil2_react_comment5)
                pause 0.5
            $ AddChatter(vig4_sc3coil2_react_comment6)
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

label vig4_sc3_macgoodbyekind():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You have to say goodbye to MAC."
        "So sad.":
            $ reactImage = "stream ui/reactshocked.png"
            player "Chat, this is tragic."
            player "I'm getting choked up."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3macgoodbye_react_comment1)
                pause 0.5
            $ AddChatter(vig4_sc3macgoodbye_react_comment2)
            pause 0.5
        "You're on your own now MAC.":
            $ reactImage = "stream ui/reactconversational.png"
            player "I think this is the right decision."
            player "It's better for the galaxy, even if it's sad."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3macgoodbye_react_comment3)
                pause 0.5
            $ AddChatter(vig4_sc3macgoodbye_react_comment4)
            #add chatter
            pause 0.5
        "Say nothing.":
            player "..."
            #add chatter
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

label vig4_sc3_macgoodbyerude():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You have to say goodbye to MAC."
        "Hurts, but it's the right thing to do.":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactshocked.png"
            player "This sucks but it's what we have to do."
            player "We have to lie, or MAC isn't going to stay."
            #player "After all we've been through!?"
            $ AddChatter(vig4_sc3macgoodbye_react_comment9)
            pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3macgoodbye_react_comment10)
                pause 0.5
        "She's not wrong.":
            $ kcEngagement -= 1
            $ reactImage = "stream ui/reactunsure.png"
            player "I mean she's not wrong."
            player "All this work was to get MAC this far."
            player "No point in getting attached."
            $ AddChatter(vig4_sc3macgoodbye_react_comment11)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3macgoodbye_react_comment12)
                #add chatter
                pause 0.5
        "Say nothing.":
            player "..."
            #add chatter
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

label vig4_sc3_machug(): # dont know if were using this one 
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "MAC is hugging Moze."
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

label vig4_sc4_amaoffer():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Ama is proposing an alliance with Moze."
        "Wow, quite the offer.":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthinking.png"
            player "Holy shit chat. This is interesting."
            player "The Dragonflies kinda suck, but should we side with Ama?"
            $ AddChatter(vig4_sc4_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc4_react_comment2)
            pause 0.5
        "No way!":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Side with the person who's been hunting us!?"
            player "Not a chance!"
            $ AddChatter(vig4_sc4_react_comment3)
            pause 0.5
            $ AddChatter(vig4_sc4_react_comment4)
            #add chatter
            pause 0.5
        "Hell yeah.":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Woah a chance to get even with the Dragonflies..."
            player "{i}Plus{/i} a redemption arc for Ama?"
            player "Sounds awesome!"
            $ AddChatter(vig4_sc4_react_comment5)
            pause 0.5
            $ AddChatter(vig4_sc4_react_comment6)
            pause 0.5
            $ AddChatter(vig4_sc4_react_comment7)
            #add chatter
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

label vig4_sc4_amaofferaccept():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You accepted Ama's offer."
        "We made the right choice.":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Hell yeah!"
            player "Let's reunite the Snakehawks."
            player "And squash some Dragonflies!"
            $ AddChatter(vig4_sc4_react_comment8)
            pause 0.5
            $ AddChatter(vig4_sc4_react_comment9)
            pause 0.5
        "Maybe this was too far.":
            $ reactImage = "stream ui/reactunsure.png"
            player "I don't know about this chat."
            player "Maybe trusting Ama was the wrong move?"
            $ AddChatter(vig4_sc4_react_comment10)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter(vig4_sc4_react_comment11)
            #add chatter
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

label vig4_sc4_amaofferrejectdefend():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You rejected Ama's offer and decided to help defend Polaris."
        "Time to save the galaxy!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Let's save the galaxy chat!"
            player "Polaris needs our help!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc4_react_comment12)
                pause 0.5
            $ AddChatter(vig4_sc4_react_comment13)
            pause 0.5
        "Was this the right call?":
            $ reactImage = "stream ui/reactunsure.png"
            player "Wait, are we technically rewarding the Dragonflies for betraying us?"
            player "Maybe this wasn't the right call."
            $ AddChatter(vig4_sc4_react_comment16)
            pause 0.5
            $ AddChatter(vig4_sc4_react_comment17)
            #add chatter
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

label vig4_sc4_amaofferrejectattack():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You rejected Ama's offer and decided to take MAC back yourself."
        "We gotta save MAC!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Time to rescue MAC!"
            player "We're only loyal to our own here!"
            player "Screw the Dragonflies and screw Ama!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc4_react_comment12)
                pause 0.5
            $ AddChatter(vig4_sc4_react_comment13)
            pause 0.5
        "Was this too far?":
            $ reactImage = "stream ui/reactunsure.png"
            player "I'm not sure about this chat..."
            player "We're making a {i}lot{/i} of enemies here."
            $ AddChatter(vig4_sc4_react_comment14)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter(vig4_sc4_react_comment15)
            #add chatter
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

#label vig4_sc5_oakleypicture(): might not need this one if we have one reacting to the explosion
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
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

label vig4_sc5_oakleydestroyed():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "The Oakley is destroyed."
        "Noooo!":
            $ reactImage = "stream ui/reactshocked.png"
            player "Noooo!"
            player "Chat our ship is destroyed!"
            $ AddChatter(vig4_sc5_react_comment1)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter(vig4_sc5_react_comment2)
            pause 0.5
        "Fitting.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Classic finale move."
            player "There's no going back now!"
            $ AddChatter(vig4_sc5_react_comment3)
            pause 0.5
            $ AddChatter(vig4_sc5_react_comment4)
            pause 0.5
        "Say nothing":
            player "..."
            #add chatter
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

label vig4_sc5_amashowsup():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Ama is back!"
        "Badass!":
            $ pdEngagement += 1
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Wooooooo!"
            player "Ama's on the scene!"
            player "Snakehawks reunion!"
            $ AddChatter(vig4_sc5_react_comment5)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc5_react_comment6)
                pause 0.5
            $ AddChatter(vig4_sc5_react_comment7)
            pause 0.5
        "Not sure about this still.":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactunsure.png"
            player "I'm still not sure about this."
            player "I wonder if we can change our mind later."
            $ AddChatter(vig4_sc5_react_comment8)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc5_react_comment9)
                pause 0.5
        "Say nothing.":
            player "..."
            #add chatter
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

label vig4_sc5_viewershipBump():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Wow, a bunch of people just joined the stream cause I chose to ally with Ama!"
        "Welcome everyone!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Welcome everyone!"
            player "Great to have y'all join for the end of this journey!"
            player "Stoked to see what this Ama alliance has in store!"
            if viewershipLow == True:
                $ AddChatter(vig4_sc5_react_comment11)
                pause 0.5
            $ AddChatter(vig4_sc5_react_comment12)
            pause 0.5
            $ AddChatter(vig4_sc5_react_comment13)
            pause 0.5
        "Let's take these Dragonflies down!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Hello new folks! And I see some familiar faces comibg back too!"
            player "Y'all ready to take on these Dragonflies!?"
            if viewershipLow == True:
                $ AddChatter(vig4_sc5_react_comment14)
                pause 0.5
                $ AddChatter(vig4_sc5_react_comment15)
                pause 0.5
            $ AddChatter(vig4_sc5_react_comment13)
            pause 0.5
        "Wow...(fumble for words)":
            $ reactImage = "stream ui/reactunsure.png"
            player "Oh my go--, I mean wow that's--"
            player "Holy crap y'all, that's a lot of viewers!"
            player "Uhh, thanks for joining the stream! We're doing this secret Ama route which, honestly I don't even think I got on purpose haha"
            if viewershipLow == True:
                $ AddChatter(vig4_sc5_react_comment16)
            $ AddChatter(vig4_sc5_react_comment13)
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

label vig4_sc6_attack_killdflies():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You decided to kill the Dragonfly hostages."
        "Serves them right.":
            $ pdEngagement += 1
            $ csEngagement -= 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Thats what you get for betraying us!"
            #player "Score settled."
            #$ vig4_scoresettled = True
            if viewershipHigh == True:
                $ AddChatter(vig4_sc6_attack_react_comment1)
                pause 0.5
            $ AddChatter(vig4_sc6_attack_react_comment2)
            if viewershipHigh == True or viewershipMed == True:
                pause 0.5
                $ AddChatter(vig4_sc6_attack_react_comment3)
            pause 0.5
        "Was that too far?":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactunsure.png"
            player "Damn that might have been too much."
            player "They were just following orders a the end of the day."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc6_attack_react_comment4)
                pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc6_attack_react_comment5)
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

label vig4_sc6_attack_sparedflies():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You decided to save the Dragonfly hostages."
        "Pay it forward.":
            $ csEngagement += 1
            $ pdEngagement -= 1
            $ reactImage = "stream ui/reactconversational.png"
            player "Definitely the right thing to do."
            player "They were just following orders after all."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc6_attack_react_comment6)
                pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc6_attack_react_comment7)
                pause 0.5
            $ AddChatter(vig4_sc6_attack_react_comment8)
            pause 0.5
        "Maybe we should've gotten our revenge":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Definitely the good guy thing to do."
            player "I don't know though. They did betray us..."
            $ AddChatter(vig4_sc6_attack_react_comment9)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc6_attack_react_comment10)
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

label vig4_sc6_both_maccall():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "MAC found a way to contact Moze and the crew."
        "MAC's ok!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Thank god MAC's ok chat!"
            player "If he was hurt it might've broken me hahaha."
            $ AddChatter(vig4_sc6_maccall_react_comment1)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter(vig4_sc6_maccall_react_comment2)
                pause 0.5
                $ AddChatter(vig4_sc6_maccall_react_comment3)
            pause 0.5
        "Coil has MAC still.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Ok. So we know where to find MAC."
            player "Good to know for sure."
            $ AddChatter(vig4_sc6_maccall_react_comment1)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc6_maccall_react_comment4)
                pause 0.5
            $ AddChatter(vig4_sc6_maccall_react_comment5)
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

label vig4_sc6_attack_barricadesurprise():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You chose to keep up the BigCorp disguise and attack the Dragonflies."
        "Gotta look out for our own.":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "The crew is what's important to us."
            player "We can't risk ourselves for some Dragonflies!"
            $ AddChatter(vig4_sc6_attack_barricade_react_comment1)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc6_attack_barricade_react_comment2)
                pause 0.5
        "No mercy for Dragonflies!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Time to squash some bugs!"
            player "These Dragonflies had it coming!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc6_attack_barricade_react_comment3)
                pause 0.5
            $ AddChatter(vig4_sc6_attack_barricade_react_comment4)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_barricade_react_comment5)
            #$ AddChatter(vig4_sc3coil2_react_comment4)
            pause 0.5
        "Was that too far?":
            $ kcEngagement += 1
            $ csEngagement += 1
            $ reactImage = "stream ui/reactunsure.png"
            player "Damn, that might've  been too much."
            player "I feel kinda bad. Not sure they deserve this."
            $ AddChatter(vig4_sc6_attack_barricade_react_comment6)
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

label vig4_sc6_attack_barricadeassault():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You chose to blow your cover and attack BigCorp."
        "BC scum!":
            $ csEngagement += 1
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "BigCorp's the real enemy!"
            player "Gotta keep our priorities straight!"
            $ AddChatter(vig4_sc6_attack_barricade_react_comment7)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_barricade_react_comment8)
            pause 0.5
        "Our first objective is MAC.":
            $ kcEngagement += 2
            $ reactImage = "stream ui/reactconversational.png"
            player "We're doing this to get MAC back."
            player "We don't need to make this a bloodbath if we don't have to."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc6_attack_barricade_react_comment9)
                pause 0.5
            $ AddChatter(vig4_sc6_attack_barricade_react_comment10)
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

label vig4_sc6_attack_barricadechaos():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You chose to attack both sides in the conflict."
        "Blast 'em all!":
            $ csEngagement -= 1
            $ kcEngagement -= 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Kill 'em all!"
            player "Let the makers sort 'em out!"
            $ AddChatter(vig4_sc6_attack_barricade_react_comment11)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc6_attack_barricade_react_comment12)
                pause 0.5
        "Chaos time!":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "Time for some good ol' fashioned chaos!"
            player "Let's blow 'em all up!"
            $ AddChatter(vig4_sc6_attack_barricade_react_comment13)
            pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc6_attack_barricade_react_comment14)
                pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc6_attack_barricade_react_comment15)
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

label vig4_sc6_attack_finding_coil():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Coil looks like he's in bad shape."
        "He looks terrible.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Wow, Coil looks like he's been through it."
            player "Wonder if this'll be easy."
            $ AddChatter(vig4_sc6_attack_findingcoil_react_comment1)
            if viewershipHigh == True or viewershipMed == True:
                pause 0.5
                $ AddChatter(vig4_sc6_attack_findingcoil_react_comment2)
            #$ AddChatter(vig4_sc3coil2_react_comment2)
            pause 0.5
        "Time to get even!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Get ready to meet your end, Coil!"
            player "Vengeance is a dish best served... Coiled."
            $ AddChatter(vig4_sc6_attack_findingcoil_react_comment3)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_findingcoil_react_comment4)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc6_attack_findingcoil_react_comment5)
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

label vig4_sc6_defend_findingvega():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Vega came back and rescued Moze."
        "Hero time.":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Look's like we got here just in the nick of time..."
            player "Guess that makes us big damn heroes!"
            $ AddChatter(vig4_sc6_defend_react_comment1)
            pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc6_defend_react_comment2)
                pause 0.5
            $ AddChatter(vig4_sc6_defend_react_comment3)
            pause 0.5
        "Glad she's ok!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "I'm happy Vega made it!"
            player "Now let's get to saving Polaris!"
            if viewershipHigh == True:
                $ AddChatter(vig4_sc6_defend_react_comment4)
                pause 0.5
            $ AddChatter(vig4_sc6_defend_react_comment5)
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

label vig4_sc6_defend_finding_coil():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "Coil looks like he's in bad shape."
        "He looks terrible.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Wow, Coil looks like he's been through it."
            player "Good thing we got here in time."
            $ AddChatter(vig4_sc6_defend_react_comment6)
            pause 0.5
            $ AddChatter(vig4_sc6_defend_react_comment7)
            pause 0.5
            $ AddChatter(vig4_sc6_defend_react_comment8)
            pause 0.5
        "Ama's here!":
            $ reactImage = "stream ui/reactshocked.png"
            player "Oh no!"
            player "Deadeye got here first!"
            #player "I knew this was too easy."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc6_defend_react_comment9)
                pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc6_defend_react_comment10)
                #$ AddChatter(vig4_sc3coil2_react_comment4)
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

label vig4_sc7_starshower():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "This is for sure the climax of the game!"
        "What a climax!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Wow, what crazy visuals!"
            player "This climax is epic, chat!"
            #player "Great way to end the game."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_react_comment1)
                pause 0.5
            $ AddChatter(vig4_sc7_react_comment2)
            pause 0.5
            $ AddChatter(vig4_sc7_react_comment3)
            pause 0.5
        "Tough choice.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Damn this is a real hard decision!"
            player "Ama's kinda evil..."
            player "But Coil tried to take MAC from us!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_react_comment4)
                pause 0.5
            $ AddChatter(vig4_sc7_react_comment5)
            pause 0.5
            $ AddChatter(vig4_sc7_react_comment6)
            pause 0.5
        "Ask the chat.":
            player "This is a tough one..."
            player "I don't know chat."
            player "What do y'all think?"
            $ AddChatter(vig4_sc7_react_comment7)
            pause 0.5
            $ AddChatter(vig4_sc7_react_comment4)
            pause 0.5
            $ AddChatter(vig4_sc7_react_comment8)
            pause 0.5
            $ AddChatter(vig4_sc7_react_comment5)
            pause 0.5
            $ AddChatter(vig4_sc7_react_comment6)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter(vig4_sc7_react_comment9)
            if jennicaRomance == False and teresaRomance == False:
                pause 0.5
                $ AddChatter(vig4_sc7_react_comment10)
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

label vig4_sc7_killama():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You killed Ama."
        "That's payback.":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Score settled."
            $ AddChatter(vig4_sc7_killama_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc7_killama_react_comment2)
            pause 0.5
            $ AddChatter(vig4_sc7_killama_react_comment3)
            pause 0.5
        "End of the Snakehawks.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Wow this is kinda sad, chat."
            player "This is the real end of the Snakehawks."
            player "Rip."
            $ AddChatter(vig4_sc7_killama_react_comment4)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_killama_react_comment5)
                pause 0.5
            $ AddChatter(vig4_sc7_killama_react_comment6)
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

label vig4_sc7_killcoil():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "You killed Coil."
        "That's payback!":
            $ reactImage = "stream ui/reactcelebrate.png"
            #player "That'll teach him to betray us!" #I think better with just the one line here
            player "Score settled."
            $ AddChatter(vig4_sc7_killcoil_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc7_killcoil_react_comment2)
            pause 0.5
            $ AddChatter(vig4_sc7_killcoil_react_comment3)
            pause 0.5
        "Is this the end of Polaris?":
            $ reactImage = "stream ui/reactthinking.png"
            player "Damn, chat, this is kinda sad."
            player "Did we doom Polaris with this decision?"
            player "RIP."
            $ AddChatter(vig4_sc7_killcoil_react_comment4)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_killcoil_react_comment5)
                pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_killcoil_react_comment6)
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

label vig4_sc7_mackillsvega():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "MAC just killed Vega!"
        "Ah!":
            $ reactImage = "stream ui/reactshocked.png"
            #player "That'll teach him to betray us!" #I think better with just the one line here
            player "Ah!"
            player "What the--"
            player "MAC what'd you do!?"
            $ AddChatter(vig4_sc7_killvega_react_comment1)
            pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_killvega_react_comment2)
                pause 0.5
            $ AddChatter(vig4_sc7_killvega_react_comment3)
            pause 0.5
            $ AddChatter(vig4_sc7_killvega_react_comment4)
            pause 0.5
        "Tough, but had to be done.":
            $ reactImage = "stream ui/reactconversational.png"
            player "I hate that she had to die, but she was literally threatening to come after us."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_killvega_react_comment5)
                pause 0.5
            $ AddChatter(vig4_sc7_killvega_react_comment6)
        "Right on.":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Unfortunate, but that's what you gotta do as an Outlaw."
            player "Can't leave someone alive who's just gonna stab you in the back later."
            $ AddChatter(vig4_sc7_killvega_react_comment7)
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
    return

label vig4_sc7_macsparesvega():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "MAC just decided not to kill Vega."
        "MAC is mature.":
            $ reactImage = "stream ui/reactthinking.png"
            player "MAC has really matured."
            player "So proud of the boy we all raised together!"
            $ AddChatter(vig4_sc7_sparevega_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc7_sparevega_react_comment2)
            pause 0.5
        "I thought he was going to shoot her.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Phew! I thought for sure he was gonna shoot her."
            player "And I do not know how I would've felt about that."
            $ AddChatter(vig4_sc7_sparevega_react_comment3)
            pause 0.5
            $ AddChatter(vig4_sc7_sparevega_react_comment4)
            pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_sparevega_react_comment5)
                pause 0.5
        "This is dangerous.":
            $ reactImage = "stream ui/reactunsure.png"
            player "I don't know, leaving someone alive who's vowed vengeance against you?"
            player "Feels dangerous."
            $ AddChatter(vig4_sc7_sparevega_react_comment6)
            pause 0.5
            $ AddChatter(vig4_sc7_sparevega_react_comment7)
            pause 0.5
            $ AddChatter(vig4_sc7_sparevega_react_comment8)
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
    return

label vig4_sc7_macamasburial():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "MAC is suggesting we bury Ama's body."
        "That's really thoughtful.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Wow, that's incredibly empathetic."
            player "MAC really matured, gang."
            $ AddChatter(vig4_sc7_amaburial_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc7_amaburial_react_comment2)
            pause 0.5
        "MAC's the captain now.":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Alright, I'm gonna say it, MAC for new captain."
            player "So thoughtful and attentive!"
            $ AddChatter(vig4_sc7_amaburial_react_comment3)
            pause 0.5
            $ AddChatter(vig4_sc7_amaburial_react_comment4)
            pause 0.5
        "I dunno, she wasn't the best mentor.":
            $ reactImage = "stream ui/reactunsure.png"
            player "I don't know MAC, she wasn't really the best mother-figure."
            $ AddChatter(vig4_sc7_amaburial_react_comment5)
            pause 0.5
            $ AddChatter(vig4_sc7_amaburial_react_comment6)
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
    return

label vig4_epilogue_maclove():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    $ reactVariable = True
    menu:
        "MAC said he loves you."
        "Cute!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Awwwwww!"
            player "MAC is so cute, chat."
            player "I love you too!"
            $ AddChatter(vig4_epilogue_react_comment1)
            pause 0.5
            $ AddChatter(vig4_epilogue_react_comment2)
            pause 0.5
            $ AddChatter(vig4_epilogue_react_comment3)
            pause 0.5
            $ AddChatter(vig4_epilogue_react_comment4)
            pause 0.5
        "Interesting.":
            $ reactImage = "stream ui/reactthinking.png"
            player "MAC's programmed for love!?"
            player "The implications of this are like mind boggling!"
            player "Super curious where they'll go with this in the next game!"
            if viewershipHigh == True:
                $ AddChatter(vig4_epilogue_react_comment5)
                pause 0.5
            $ AddChatter(vig4_epilogue_react_comment6)
            pause 0.5
            $ AddChatter(vig4_epilogue_react_comment7)
            pause 0.5
            $ AddChatter(vig4_epilogue_react_comment8)
            pause 0.5
        "Say nothing.":
            player "..."
            $ AddChatter(vig4_epilogue_react_comment9)
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

####TARGETS FOR BLUEIT ######

label vig4_blueit_endHypeThread():
    $ screenComplete = False
    $ blueitImage = "socials/v4_endingHype.png"
    $ yb = 1080
    $ blueitCheck += 1
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig4_blueit_devThread():
    $ screenComplete = False
    $ blueitImage = "socials/v4_devThanks.png"
    $ yb = 1080
    $ blueitCheck += 1
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig4_blueit_amaRomanceThread():
    $ screenComplete = False
    $ blueitImage = "socials/v4_amaRomance.png"
    $ yb = 1080
    $ blueitCheck += 1
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig4_blueit_endChoicethread():
    $ screenComplete = False
    $ blueitImage = "socials/v4_endingChoice.png"
    $ yb = 1080
    $ blueitCheck += 1
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig4_blueit_romanceRouteThread():
    $ screenComplete = False
    $ blueitImage = "socials/v4_romanceRoute.png"
    $ yb = 1080
    $ blueitCheck += 1
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig4_blueit_polarisThread():
    $ screenComplete = False
    $ blueitImage = "socials/v4_polaris.png"
    $ yb = 1080
    $ blueitCheck += 1
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

label vig4_blueit_oakley3Thread():
    $ screenComplete = False
    $ blueitImage = "socials/v4_oakley3.png"
    $ yb = 1080
    $ blueitCheck += 1
    $ blueitChoiceCheck = True
    show screen blueitThread
    #show launch thread at top:
    #    zoom 1.0
    call screen blueitButtonCheck
    return

####TARGETS FOR FLINCH ######

label vig4_analytics_audience():
    hide screen viewershipButton_vig4
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
    elif topfan == "kitcat":
        "kitCat."
    elif topfan == "pickledDragons":
        "pickledDragons."
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