label vig4_sc1_pdParanoia():
    $ macroChoice = True
    $ vig4_sc1_comment5.click = False
    $ narrator = reg_narrator
    menu:
        "Is Moze over her paranoia?"
        "For sure.":
            player "Oh yeah, I think she was able to work through a lot of that in the last episode."
            player "Especially if the crew isn't at each other's throats anymore."
        "No way.":
            player "No way. You don't just magically get over that stuff."
            player "I'd expect we're in for some hallucinations or maybe a trippy dream sequence."            
        "I don't know.":
            player "Hmm interesting idea. Honestly, idk."
            player "They're not in as stressful a position anymore, but that's not something you just like get over."
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc1_csRomance():
    $ macroChoice = True
    $ vig4_sc1_2_comment20.click = False
    $ narrator = reg_narrator
    menu:
        "The Chat is asking who I want to romance again."
        "I'm team Jennica.":
            $ csEngagement += 1
            $ kcEngagement -=1
            player "Oh, I'm team Jennica for sure."
            player "Friendly, sensitive, and a crack pilot. What's not to love?"
            $ AddChatter(vig4_sc1_interact_comment1)
        "I'm team Teresa.":
            $ csEngagement -=1
            $ kcEngagement += 1
            player "Oh, I'm team Teresa for sure."
            player "Smart, loyal, and a clever engineer in the clutch. What's not to love?"
            $ AddChatter(vig4_sc1_interact_comment2)
        "I'm still hoping for Ama." if deadeyeApproval >= 2:
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
            $ csEngagement -= 1
            $ kcEngagement -= 1
            $ pdEngagement += 1
            player "I'm actually not feeling much of a romance in this game."
            player "The characters are great, but I don't see the chemsitry."
            $ AddChatter(vig4_sc1_interact_comment6)
            pause 0.5
            $ AddChatter(vig4_sc1_interact_comment7)
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
    menu:
        "How do I think the story's going to play out?"
        "I have no idea.":
            $ pdEngagement -= 1
            $ kcEngagement -= 1
            player "I have no clue to be honest."
            player "I've learned that you can't predict where things are going to go with this story."
        "The Alliance is gonna be the real big bad.":
            $ csEngagement += 1
            player "I agree with pickledDragons, I think the Alliance is gonna be a factor at the end here."
            player "Feels like they could be the real big bad and then set up Oakley 3 nicely."
            $ AddChatter(vig4_sc2_interact_comment1)
        "Ama's going to come back for sure.":
            $ kcEngagement += 1
            $ pdEngagement += 1
            player "I think Ama's going to kidnap MAC and we're gonna have to fight her and BigCorp to get him back."
            player "We didn't get a proper resolution to her story in Episode 3 so I'd be shocked if she doesn't come back in some capacity."
            $ AddChatter(vig4_sc2_interact_comment2)
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc2_rube():
    $ macroChoice = True
    $ vig4_sc2_1_comment8.click = False
    $ narrator = reg_narrator
    menu:
        "Should I play into this?"
        "Say nothing.":
            pass
        "Rube!":
            player "Rube!"
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
    menu:
        "Do I believe Polaris is a peaceful town."
        "No way.":
            player "No way. There's something going on here that he's not telling us."
        "I buy it.":
            player "It seemed pretty chill while we were walking in. They're at least not actively hostile, that's for sure."
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
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
    menu:
        "kitcat's asking why I'm not romancing Jennica or Teresa."
        "We can't if we want to romance Ama.":
            player "I saw a thread on BlueIt that said we can't romance Jenn or Teresa if we want to romance Ama."
            player "And I'm still holding out hope for the Ama drama!"
            $ AddChatter(vig4_sc3_interact_comment1)
            pause 0.5
            $ AddChatter(vig4_sc3_interact_comment2)
        "I want to get to know Vega more.":
            player "I know, I know, but I want to get to know Vega better."
            player "Maybe we can learn more about Coil from her too."
            $ AddChatter(vig4_sc3_interact_comment3)
        "Say nothing.":
            pass
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
    menu:
        "How do I feel about Coil's actions?"
        "I don't like him.":
            player "I don't like him. I feel like he didn't even try to make a case for us."
            $ AddChatter(vig4_sc3_interact_comment4)
            pause 0.5
            $ AddChatter(vig4_sc3_interact_comment5)
        "I think he's right.":
            player "The thing is, what he's saying isn't necessarily wrong."
            player "Maybe we haven't been the best parental figure for MAC."
            $ AddChatter(vig4_sc3_interact_comment6)
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
    menu:
        "How do I feel about Coil's actions?"
        "I don't like him.":
            $ pdEngagement += 1
            $ csEngagement -= 1
            player "I don't like him. I feel like he didn't even try to make a case for us."
            $ AddChatter(vig4_sc3_interact_comment4)
            pause 0.5
            $ AddChatter(vig4_sc3_interact_comment5)
        "I think he's right.":
            $ pdEngagement -= 1
            $ csEngagement += 1
            player "The thing is, what he's saying isn't necessarily wrong."
            player "Maybe we haven't been the best parental figure for MAC."
            $ AddChatter(vig4_sc3_interact_comment7)
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
    menu:
        "Why didn't I choose to ally with Ama?"
        "Cause she's been trying to kill us.":
            player "Ama's been trying to kill us for months, and now she just decides to swap sides?"
            player "We can't just forgive her that fast. She has to earn it."
            $ AddChatter(vig4_sc4_interact_comment1)
            pause 0.5
            $ AddChatter(vig4_sc4_interact_comment2)
        "We don't need her.":
            player "We don't need her. Our crew is tough enough to handle what's coming up on our own."
            $ AddChatter(vig4_sc4_interact_comment3)
            pause 0.5
            $ AddChatter(vig4_sc4_interact_comment4)
        "We can't trust her.":
            player "I mean, we just can't trust her."
            player "Especially after Episode 3, I wouldn't want her watching my back."
            $ AddChatter(vig4_sc4_interact_comment4)
            pause 0.5
            $ AddChatter(vig4_sc4_interact_comment5)
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
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
    menu:
        "swayy0scar! They were in chat for the first stream but haven't been around since."
        "Welcome back!":
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
            pass
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
    menu:
        "Chat seems sad about the tank being destroyed."
        "RIP.":
            player "Another fallen soldier. Get those RIPs in chat."
            $ AddChatter(vig4_sc6_interact_comment1)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment2)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment3)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment4)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment5)
        "Say nothing.":
            pass
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
    menu:
        "Chat is talking about Moze's morality."
        "Moze's flexibility is what makes her a good character.":
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
            $ pdEngagement += 1
            $ csEngagement == 1
            player "Who cares about her character arc. This is just a good time!"
            $ AddChatter(vig4_sc6_interact_comment8)
        "Moze getting \"worse\" is also a good story.":
            $ pdEngagement += 1
            player "Moze failing at \"doing better\" and actually \"doing worse\" is an interesting story."
            player "I think it reflects the complexity of the galaxy and how hard it is for her to change. Especially considering her mentor."
            $ AddChatter(vig4_sc6_interact_comment9)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment10)
        "It does feel inconsistent with the game's themes.":
            $ pdEngagement -= 1
            player "Yeah, I'll admit, a lot of Outlaw Moze's decisions do feel kind of inconsistent with the game's themes."
            $ AddChatter(vig4_sc6_interact_comment11)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment12)
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
    menu:
        "Chat is reacting to Reginald's return."
        "REGGIE!":
            player "REGGIE!"
            player "HE'S BACK!"
            $ AddChatter(vig4_sc6_interact_comment14)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment15)
            $ AddChatter(vig4_sc6_interact_comment16)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment17)
            pause 0.5
            $ AddChatter(vig4_sc6_interact_comment18)
        "Is Matticus going to want something?":
            player "Oh god, is Matticus going to want something for this?"
            $ AddChatter(vig4_sc6_interact_comment13)
        "Say nothing.":
            pass
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
    menu:
        "kitcat wants to know why I backed out of romancing Ama."
        "They're not right for each other.":
            player "I don't think they're right for each other."
            player "Plus Ama's kind of a mother figure to Moze."
            player "It didn't end up feeling good in the end. Sorry chat."
            $ AddChatter(vig4_sc7_interact_comment2)
        "Too soon.":
            player "I think there's something between them, but saying \"I love you\" right now feels a bit rushed."
            $ AddChatter(vig4_sc7_interact_comment1)
        "Say nothing.":
            pass
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_pdEndFeeling():
    $ macroChoice = True
    $ vig4_sc7_epilogue_comment4.click = False
    $ narrator = reg_narrator
    menu:
        "How am I feeling now that I'm at the end of the game?"
        "Tired.":
            player "I'll be honest Chat, I'm beat haha"
            player "This has been a long time coming. It's been super fun, but I am tired."
            player "A bit relieved to be bringing this to a closed."
            $ AddChatter(vig4_epilogue_interact_comment1)
            pause 0.5
            $ AddChatter(vig4_epilogue_interact_comment2)
            pause 0.5
            $ AddChatter(vig4_epilogue_interact_comment3)
        "Ecstatic.":
            player "Oh I feel amazing, ecstatic even!"
            player "That climax was so cool and all the drama between the characters was amazing!"
            player "I think I'm gonna be riding this high for a while haha"
            $ AddChatter(vig4_epilogue_interact_comment4)
            pause 0.5
            $ AddChatter(vig4_epilogue_interact_comment5)
            pause 0.5
            $ AddChatter(vig4_epilogue_interact_comment3)
        "Kind of sad.":
            player "In all honesty, I'm a bit sad that it's over."
            player "This has been so much fun and it's ending really well."
            player "I just wish there was more!"
            $ AddChatter(vig4_epilogue_interact_comment6)
            pause 0.5
            $ AddChatter(vig4_epilogue_interact_comment7)
            pause 0.5
            $ AddChatter(vig4_epilogue_interact_comment3)
        "Not sure.":
            player "Honestly, I don't know what to feel."
            player "I'm like sad, but also happy."
            player "It just feels surreal for this gaming to actually be coming to an end."
            $ AddChatter(vig4_epilogue_interact_comment1)
            pause 0.5
            $ AddChatter(vig4_epilogue_interact_comment2)
            pause 0.5
            $ AddChatter(vig4_epilogue_interact_comment3)
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
            player "Chat did MAC just tell a joke!?"
            player "That's crazy!"
            $ AddChatter (vig4_sc1_react_comment1)
            $ AddChatter (vig4_sc1_react_comment2)
            pause 0.5
        "That's so cute!":
            $ reactImage = "stream ui/reactshocked.png"
            player "Holy crap, MAC's a lil joker!"
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
            $ AddChatter(vig4_sc2_react_comment2)
            pause 0.5
        "This is going to go poorly.":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactunsure.png"
            player "This is going to go so bad."
            player "This might've been the wrong call."
            $ AddChatter(vig4_sc2_react_comment3)
            pause 0.5
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
            $ csEngagement += 1
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Woah!"
            player "This old man's got some cool tech!"
            $ AddChatter(vig4_sc2_react_comment9)
            pause 0.5
        "Of course he's got tricks.":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "I knew it wouldn't go over well."
            player "There's obviously more to this old guy than meets the eye."
            $ AddChatter(vig4_sc2_react_comment10)
            pause 0.5
        "Shoot him again!":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Fire again Teresa!"
            player "That shield ain't limitless!"
            $ AddChatter(vig4_sc2_react_comment11)
            pause 0.5
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
            $ AddChatter(vig4_sc2_react_comment15)
            $ AddChatter(vig4_sc2_react_comment16)
            $ AddChatter(vig4_sc2_react_comment17)
            pause 0.5
            $ AddChatter(vig4_sc2_react_comment18)
            pause 0.5
        "MAC's got some upgrades!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Badass!"
            player "MAC's a bonafide outlaw!"
            $ AddChatter(vig4_sc2_react_comment19)
            pause 0.5
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
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Wow. You can tell he regrets this."
            player "Coil's got hangups about his old partner."
            $ AddChatter(vig4_sc2_react_comment23)
            pause 0.5
        "Can't side with BigCorp!":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "Damnit Coil!"
            player "You should've known better than to trust BigCorp!"
            $ AddChatter(vig4_sc2_react_comment24)
            pause 0.5
            $ AddChatter(vig4_sc2_react_comment25)
            #add chatter
            pause 0.5
        "Boring!":
            $ pdEngagement += 1
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
            pause 0.5
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
            pause 0.5
            $ AddChatter(vig4_sc2_react_comment30)
            pause 0.5
        "Not fair!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "This is bogus chat!"
            player "We took all this risk and got him this far!"
            $ AddChatter(vig4_sc2_react_comment31)
            pause 0.5
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

label vig4_sc3_jenndatelose():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Jennica winning the game."
        "We never had a chance!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Shoulda known."
            player "She's the best pilot in the galaxy after all!"
            $ AddChatter(vig4_sc3jenn_react_comment1)
            pause 0.5
        "Damn that was close!":
            $ reactImage = "stream ui/reactunsure.png"
            player "Ahh damn!"
            player "Thought we had her."
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

label vig4_sc3_jenndatewin():
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
        "React to kissing Jennica."
        "WOOOO!!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Finally!!"
            player "Best ship finally is canon chat!!"
            $ AddChatter(vig4_sc3jenn_react_comment10)
            pause 0.5
            $ AddChatter(vig4_sc3jenn_react_comment12)
            pause 0.5
        "Awwwww.":
            $ reactImage = "stream ui/reactconfident.png"
            player "Awwwwww."
            player "They're perfect for each other chat!!"
            $ AddChatter(vig4_sc3jenn_react_comment11)
            pause 0.5
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
            pause 0.5
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
        "Comment on Coil telling you to leave without MAC."
        "Wow brutal.":
            $ reactImage = "stream ui/reactconversational.png"
            player "Wow that really sucks chat."
            player "All this work to get MAC here and just like that."
            player "Pushed aside."
            $ AddChatter(vig4_sc3coil1_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc3coil1_react_comment2)
            pause 0.5
        "Bullshit!":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "This is bullshit chat!"
            player "All this work to get MAC here!"
            player "No way we're letting this happen!"
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
        "I should've known!":
            $ reactImage = "stream ui/reactconversational.png"
            player "Yeah no chance they were going to leave us alone."
            player "No trust with these guys chat."
            player "Brutal."
            $ AddChatter(vig4_sc3coil2_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc3coil2_react_comment2)
            pause 0.5
        "Dammit!":
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Crap! They got us."
            player "Should've known they wouldn't trust us."
            $ AddChatter(vig4_sc3coil2_react_comment3)
            pause 0.5
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
            pause 0.5
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
            player "Chat, this is tragic."
            player "I'm getting choked up."
            $ AddChatter(vig4_sc3macgoodbye_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc3macgoodbye_react_comment2)
            pause 0.5
        "You're on your own now MAC.":
            $ reactImage = "stream ui/reactconversational.png"
            player "I think this is the right decision."
            player "He needs to go with them, even if it's sad."
            $ AddChatter(vig4_sc3macgoodbye_react_comment3)
            pause 0.5
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
        "Hurts, but it's the right thing to do.":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactshocked.png"
            player "This sucks but it's what we have to do."
            player "We have to lie, or MAC isn't going to stay."
            player "After all we've been through!?"
            $ AddChatter(vig4_sc3macgoodbye_react_comment9)
            pause 0.5
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

label vig4_sc4_amaoffer():
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
            pause 0.5
            $ AddChatter(vig4_sc4_react_comment13)
            pause 0.5
        "Was this the right call?":
            $ reactImage = "stream ui/reactunsure.png"
            player "Are we rewarding the Dragonflies for betraying us?"
            player "I don't know about this chat."
            $ AddChatter(vig4_sc4_react_comment16)
            pause 0.5
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
            pause 0.5
            $ AddChatter(vig4_sc4_react_comment13)
            pause 0.5
        "Was this too far?":
            $ reactImage = "stream ui/reactunsure.png"
            player "I'm not sure about this chat..."
            player "We're making a {i}lot{/i} of enemies here."
            $ AddChatter(vig4_sc4_react_comment14)
            pause 0.5
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
            player "Noooo!"
            player "Chat our ship is destroyed!"
            $ AddChatter(vig4_sc5_react_comment1)
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
            $ pdEngagement += 1
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Wooooooo!"
            player "Ama's on the scene!"
            player "Snakehawks reunion!"
            $ AddChatter(vig4_sc5_react_comment5)
            pause 0.5
            $ AddChatter(vig4_sc5_react_comment6)
            pause 0.5
            $ AddChatter(vig4_sc5_react_comment7)
            pause 0.5
        "Not sure about this still.":
            $ csEngagement += 1
            $ reactImage = "stream ui/reactunsure.png"
            player "I'm still not so sure about this."
            player "I wonder if we can change our mind later."
            $ AddChatter(vig4_sc5_react_comment8)
            pause 0.5
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

label vig4_sc6_attack_killdflies():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to killing the Dragonfly hostages."
        "Serves them right.":
            $ pdEngagement += 1
            $ csEngagement -= 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Thats what you get for betraying us!"
            player "Score settled."
            $ AddChatter(vig4_sc6_attack_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_react_comment2)
            $ AddChatter(vig4_sc6_attack_react_comment3)
            pause 0.5
        "Was that too far?":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactunsure.png"
            player "Damn that might have been too much."
            player "They were just following orders a the end of the day."
            $ AddChatter(vig4_sc6_attack_react_comment4)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_react_comment5)
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

label vig4_sc6_attack_sparedflies():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to resucing the Dragonfly hostages."
        "Pay it forward.":
            $ csEngagement += 1
            $ pdEngagement -= 1
            $ reactImage = "stream ui/reactconversational.png"
            player "Definitely the right thing to do."
            player "They were just following orders after all."
            $ AddChatter(vig4_sc6_attack_react_comment6)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_react_comment7)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_react_comment8)
            pause 0.5
        "Maybe we shoulda gotten our revenge":
            $ kcEngagement += 1
            $ reactImage = "stream ui/reactthumbsdown.png"
            player "Definitely the good guy thing to do."
            player "I don't know though. They did betray us after all."
            $ AddChatter(vig4_sc6_attack_react_comment9)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_react_comment10)
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

label vig4_sc6_both_maccall():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on MAC's reappearance."
        "MAC's ok!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Thank god MAC's ok chat!"
            player "If he was hurt it might've broken me hahaha."
            $ AddChatter(vig4_sc6_maccall_react_comment1)
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
            $ AddChatter(vig4_sc6_maccall_react_comment4)
            pause 0.5
            $ AddChatter(vig4_sc6_maccall_react_comment5)
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

label vig4_sc6_attack_barricadesurprise():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Justify pretending to be BigCorp and attacking the Dragonflies."
        "Gotta look out for our own.":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "The crew is what's important to us."
            player "We can't risk ourselves for some Dragonflies!"
            $ AddChatter(vig4_sc6_attack_barricade_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_barricade_react_comment2)
            pause 0.5
        "No mercy for Dragonflies!":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Time to squash some bugs!"
            player "These Dragonflies had it coming when they betrayed us!"
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
            player "Damn that might have been too much."
            player "I feel kinda bad. Not sure they deserve this."
            $ AddChatter(vig4_sc6_attack_barricade_react_comment6)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc6_attack_barricadeassault():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Justify blowing your cover and attacking BigCorp."
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
            $ AddChatter(vig4_sc6_attack_barricade_react_comment9)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_barricade_react_comment10)
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

label vig4_sc6_attack_barricadechaos():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Justify blowing your cover and attacking both sides."
        "Blast em all!":
            $ csEngagement -= 1
            $ kcEngagement -= 1
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Kill em all!"
            player "Let the makers sort em out!"
            $ AddChatter(vig4_sc6_attack_barricade_react_comment11)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_barricade_react_comment12)
            pause 0.5
        "Chaos time!":
            $ pdEngagement += 1
            $ reactImage = "stream ui/reactconfident.png"
            player "Time for some good ol' fashioned chaos!"
            player "Let's blow em all up!"
            $ AddChatter(vig4_sc6_attack_barricade_react_comment13)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_barricade_react_comment14)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_barricade_react_comment15)
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

label vig4_sc6_attack_finding_coil():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on Coil's haggard appearance."
        "He looks terrible.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Wow Coil looks like he's been through it."
            player "Wonder if this'll be easy."
            $ AddChatter(vig4_sc6_attack_findingcoil_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_findingcoil_react_comment2)
            #$ AddChatter(vig4_sc3coil2_react_comment2)
            pause 0.5
        "Time to get even!":
            $ reactImage = "stream ui/reactconfident.png"
            player "Get ready to meet your end Coil!"
            player "Vengeance is a dish best served... Coiled."
            $ AddChatter(vig4_sc6_attack_findingcoil_react_comment3)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_findingcoil_react_comment4)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_findingcoil_react_comment5)
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

label vig4_sc6_defend_findingvega():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Vega."
        "Hero time.":
            $ reactImage = "stream ui/reactcelebrate.png"
            player "Look's like we got here just in the nick of time..."
            player "Guess that makes us big damn heroes!"
            $ AddChatter(vig4_sc6_defend_react_comment1)
            pause 0.5
            $ AddChatter(vig4_sc6_defend_react_comment2)
            pause 0.5
            $ AddChatter(vig4_sc6_defend_react_comment3)
            pause 0.5
        "Glad she's ok!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "I'm happy Vega made it!"
            player "Now let's get to saving Polaris!"
            $ AddChatter(vig4_sc6_defend_react_comment4)
            pause 0.5
            $ AddChatter(vig4_sc6_defend_react_comment5)
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

label vig4_sc6_defend_finding_coil():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "Comment on rescuing Coil."
        "He looks terrible.":
            $ reactImage = "stream ui/reactthinking.png"
            player "Wow Coil looks like he's been through it."
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
            player "I knew this was too easy."
            $ AddChatter(vig4_sc6_defend_react_comment9)
            pause 0.5
            $ AddChatter(vig4_sc6_defend_react_comment10)
            #$ AddChatter(vig4_sc3coil2_react_comment4)
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

label vig4_sc7_starshower():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to your climactic choice."
        "What a climax!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Wow what crazy visuals!"
            player "This climax is epic chat!"
            player "Great way to end the game."
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
            player "But Coil betrayed us!"
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
            pause 0.5
            $ AddChatter(vig4_sc7_react_comment9)
            if jennicaRomance == False and teresaRomance == False:
                pause 0.5
                $ AddChatter(vig4_sc7_react_comment10)
            pause 0.5
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    $ reactImage = "stream ui/reactneutral.png"
    return

label vig4_sc7_killama():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Ama's death."
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
            player "Wow this is kinda sad chat."
            player "This is the real end of the Snakehawks."
            player "Rip."
            $ AddChatter(vig4_sc7_killama_react_comment4)
            pause 0.5
            $ AddChatter(vig4_sc7_killama_react_comment5)
            pause 0.5
            $ AddChatter(vig4_sc7_killama_react_comment6)
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

label vig4_sc7_killcoil():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to Coil's death."
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
            player "Damn chat this is kinda sad."
            player "Did we doom Polaris with this decision?"
            player "Rip."
            $ AddChatter(vig4_sc7_killcoil_react_comment4)
            pause 0.5
            $ AddChatter(vig4_sc7_killcoil_react_comment5)
            pause 0.5
            $ AddChatter(vig4_sc7_killcoil_react_comment6)
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

#We should probably have reactions to how MAC deals with Vega

label vig4_epilogue_maclove():
    hide screen streamerCommentary
    $ macroChoice = True
    $ narrator = reg_narrator
    menu:
        "React to MAC's admission of love."
        "Cute!":
            $ reactImage = "stream ui/reactthumbsup.png"
            player "Awwwwww!"
            player "MAC is so cute chat."
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
            player "MAC's programmed for love?"
            player "The implications of this are like mind boggling!"
            player "Super curious where they'll go with this in the next game!"
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