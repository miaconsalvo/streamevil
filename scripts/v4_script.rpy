label vignette4Start():
    #We want to reset these before the start of the vignette
    $ menu = adv_menu
    $ vignette1 = False
    $ vignette2 = False
    $ vignette3 = False
    $ vignette4 = True
    $ viewCheck1 = 0
    $ viewCheck2 = 0
    $ viewCheck3 = 0
    $ viewCheck4 = 0
    $ viewCheck5 = 0
    $ viewCheck6 = 0
    $ viewCheck7 = 0
    $ viewCheck8 = 0
    $ viewCheck9 = 0
    $ viewCheck10 = 0
    $ vbar1 = 0 #make sure to set these vbar values back to zero at the start of every vignette (or just when you leave the analytics screen)
    $ vbar2 = 0
    $ vbar3 = 0
    $ vbar4 = 0
    $ vbar5 = 0
    $ vbar6 = 0
    $ vbar7 = 0
    $ vbar8 = 0
    $ vbar9 = 0
    $ vbar10 = 0
    $ blueitPages = []
    $ chatter_list = []
    $ blueitChoiceCheck = False
    $ flinchCheck = 0
    $ flinch_viewcountCheck = False
    $ flinch_topfanCheck = False
    $ flinch_audienceCheck = False
    $ blueitView = False
    $ loopdView = False
    $ screenComplete = False
    $ macroChoice = True
    #We now use the "scene" function to show the streamview
    #This makes it constantly viewable without being affected by transitions between labels
    #show streamview
    "You're about to stream the final episode of Oakley 2: Settle the Score."
    "Get ready."
    scene streamview with dissolve
    show screen streamDetails
    show screen streamChat
    "You begin the stream and then boot up the game."
    "You load the save file you were previously playing, and are ready to go."
    jump vig4_sc1_1

label vig4_sc1_1():
    $ narrator = alt_narrator
    $ macroChoice = False
    show ship_hallway_stream at topleft onlayer background with dissolve
    play music "soundtrack/vig1scratchtrack.wav" volume 1.2
    $ AddChatter(vig4_sc1_comment1)
    "There is a harmonious hum to the Oakley's engines."
    $ AddChatter(vig4_sc1_comment2)
    pause 0.5
    $ AddChatter(vig4_sc1_comment3) 
    "No alarms going off."
    "No rattling in the hull."
    $ AddChatter(vig4_sc1_comment4)
    "No tension in the air."
    "Just the perpetual purr of space travel."
    $ AddChatter(vig4_sc1_comment5)
    enS "That's family you know. There's always something wrong with you that they just have to fix."
    macS "You mean like applying thermal paste? Or rebooting faulty drivers?"
    $ AddChatter(vig4_sc1_comment6)
    enS "No...well, kind of, I suppose."
    show shiphub_stream at topleft onlayer background with dissolve
    show mac stream neutral at stream_grab_mac with dissolve
    show teresa stream neutral at stream_right with dissolve
    hide ship_hallway_stream
    macS "I like our family."
    $ AddChatter(vig4_sc1_comment7)
    "Teresa's shoulders loosen."
    show teresa stream happy
    enS "Yeah, this one's good."
    #######if viewershipHigh == True or viewershipMed == True:##### THIS GATE STRUCTURE WORKS
    $ AddChatter(vig4_sc1_comment8)
    "Teresa and MAC are in the bridge. Teresa is attending to something in MAC's back panel."
    menu:
        "Teresa and MAC are in the bridge. Teresa is attending to something in MAC's back panel."
        "Head to the cockpit.":
            mS "Morning, Resa. Morning, MAC."
            "I step into the room and give the two a nod."
            #play audio macHappy
            "MAC hums back."
            enS "Jennica's waiting for you, Cap."
            $ AddChatter(vig4_sc1_comment9alt)
            mS "Already on my way."
            "Teresa gives a casual salute."
            enS "See you both shortly."
            $ AddChatter(vig4_sc1_comment10alt)
        "Inquire about their activity.":
            mS "Morning, Resa. MAC."
            "I step into the room and give the two a nod."
            #play audio macHappy
            "MAC hums back."
            enS "Jennica's waiting for you, Cap."
            mS "I know, I was heading there just now." 
            mS "But what are you two up to? Is everything ok?"
            macS "Teresa is improving my functionality."
            mS "Functionality?"
            $ AddChatter(vig4_sc1_comment9)
            enS "After your theatrics at the inventor's fair, MAC wanted to get some upgrades."
            mS "Like?"
            macS "It's a surprise."
            mS "A surprise?"
            macS "Yes, captain. Shall I provide a definition of \"surprise\"?"
            $ AddChatter(vig4_sc1_comment10)
            "I look from MAC to Teresa. She puts her hands in the air."
            enS "I'm no snitch."
            mS "Alright, keep your secrets."
            menu:
                mS "Alright, keep your secrets."
                "Don't go overboard, Teresa":
                    mS "Just don't overdo it, Teresa."
                    enS "Captain, when have I ever?"
                    macS "I can recount several instances of Teresa \"overdoing it.\""
                    if customsStampede == True:
                        $ AddChatter(vig4_sc1_comment11)
                        macS "Example 1: Gibian V custo--"
                        enS "Okay, Okay, I get it, no overdoing it."
                    else:
                        enS "Listen up MAC, in this family, we don't snitch on each other."
                        $ AddChatter(vig4_sc1_comment12)
                        macS "\"Snitch\"? What is \"snitch\"?"
                    mS "I'll leave you two to it."
                "Hope things go smooth":
                    mS "Be careful, we don't want any technical difficulties this late in the game."
                    enS "Don't worry, I'm not touching any critical functions."
                    macS "My optical drives have shut down. I can no longer see."
                    show teresa stream shock
                    enS "WHAT!?"
                    macS "Joking. I can see fine."
                    ##*streamer react moment here instead?
                    $ AddChatter(vig4_sc1_comment14)
                    show teresa stream upset
                    enS "You little--"
                    mS "I'll leave you two to it then."
    jump vig4_sc1_2

label vig4_sc1_2():
    hide mac with dissolve
    hide teresa with dissolve
    #show ship_cockpit at topleft onlayer background with dissolve
    #hide shiphub_stream
    show shiphub_stream at topleft onlayer background with dissolve
    "The cockpit is significantly more clean than it was a couple weeks ago."
    $ AddChatter(vig4_sc1_2_comment1)
    show jennica stream neutral at stream_left with dissolve
    "Jennica, relaxed but attentive, sits at the helm."
    mS "Hiya, Jennica."
    $ AddChatter(vig4_sc1_2_comment2)
    pS "Howdy, Cap."
    menu:
        pS "Howdy, Cap."
        "You wanted to see me.":
            mS "You said you wanted to see me."
            $ AddChatter(vig4_sc1_2_comment3)
        "How are things at the helm?":
            mS "How are things up here?"
            $ AddChatter(vig4_sc1_2_comment3)
            pS "Steady as she goes. No excitement since we left Akar."
            mS "Good."
            mS "And you're not holing up in this chair for days on end anymore?"
            pS "Nope. That's all in the rearview now."
            mS "Happy to hear it."
            pS "Happy to feel it."
            mS "You wanted to see me?"
        "It's much cleaner in here.":
            mS "You cleaned up the place."
            $ AddChatter(vig4_sc1_2_comment3)
            pS "Wasn't me. It was Teresa."
            pS "After we left I found her putting the last of the trash in a waste bag."
            pS "It was almost like I caught her with her pants down haha."
            $ AddChatter(vig4_sc1_2_comment4)
            mS "You two back to normal then?"
            pS "After these past weeks, I don't know if I remember what \"normal\" is anymore ."
            $ AddChatter(vig4_sc1_2_comment5)
            pS "But we're good."
            mS "Glad to hear it."
            pS "Glad to feel it."
            mS "You wanted to see me?"
    pS "Yeah, I'm about to bring us out of hyperspace."
    pS "Figured you'd want to be here when we finally arrived."
    "The waves of light surrounding the ship slow down as we emerge from hyperlight travel into the vastness of space."
    "A giant orb of swirling red and orange hangs in front of us."
    menu:
        "A giant orb of swirling red and orange hangs in front of us."
        "A gas giant?":
            mS "It's a gas giant. That can't be right."
        "The Dragonflies can't be human.":
            $ AddChatter(vig4_sc1_2_comment6)
            mS "Apparently the Dragonflies can breathe corrosive air?"
    pS "The coordinates aren't pointing to the planet. It's one of the moons."
    "The screen in front of us zooms in on a small speck just to the left of the planet."
    "A read out prints onto the screen."
    "Moon: Polaris.\nAtmosphere: Artificial - Breathable.\nKey Resources: None."
    "Affiliation: N/A.\nKey Industries: None.\nPopulation: Unknown."
    mS "Not a lot of info."
    $ AddChatter(vig4_sc1_2_comment7)
    pS "Makes sense. I doubt whatever's there is even in BC's database."
    show teresa stream neutral at stream_right with dissolve
    show mac stream neutral at stream_center_mac with dissolve
    enS "I felt us come out of hyperspace. We there?"
    $ AddChatter(vig4_sc1_2_comment8)
    pS "Seems like it."
    enS "\"No affiliation.\" So we are in fully neutral territory."
    pS "Yep. Right on the border of BC and Alliance space."
    $ AddChatter(vig4_sc1_2_comment9)
    pause 0.5
    $ AddChatter(vig4_sc1_2_comment10)
    enS "And this colony is so small that neither group cares."
    macS "Po-dunk?"
    ##Could cut from here to "I'll run a scan for BigCorp signatures" - have Jennica say "maybe" - saves 20 lines
    enS "Maybe. But that artificial atmosphere is intriguing."
    menu:
        enS "Maybe. But that artificial atmosphere is intriguing."
        "What's so odd about that?":
            mS "What's so odd about an artificial atmosphere?"
            pS "Yeah, I've been on rocks with them before. Tough to breathe at first, but you adjust."
            enS "They're not uncommon. But the technology to produce them is expensive."
            $ AddChatter(vig4_sc1_2_comment11)
            enS "And this moon with nothing of value on it, in no strategic position, has access to one?"
            $ AddChatter(vig4_sc1_2_comment12)
            menu:
                enS "And this moon with nothing of value on it, in no strategic position, has access to one?"
                "Maybe the Dragonflies are well-connected.":
                    mS "Maybe the Dragonflies have more tech than we expected."
                    enS "It's possible."
                    enS "I wouldn't rule out a trap though. We should be careful."
                    $ AddChatter(vig4_sc1_2_comment13)
                    pause 0.5
                    $ AddChatter(vig4_sc1_2_comment14)
                "You thinking it could be a trap?":
                    mS "You thinking it could be a trap?"
                    enS "I wouldn't rule it out. We should be careful."
                    $ AddChatter(vig4_sc1_2_comment13)
                    pause 0.5
                    $ AddChatter(vig4_sc1_2_comment14)
        "I'm more concerned about the \"unknown\" population.":
            mS "I'm more concerned about the \"unknown\" population."
            mS "What if there are people down there we don't want to meet?"
            $ AddChatter(vig4_sc1_2_comment11)
    pS "I'll run a scan for BigCorp signatures."
    "A green line appears on screen and sweeps over the moon's landscape."
    if macViolence > macPeace:
        macS "If BC is there, we can just smash 'em."
        $ AddChatter(vig4_sc1_2_comment15)
        if customsStampede == True:
            macS "Conflagrant-style."
            show teresa stream happy
            "Out of the corner of my eye, I think I see Teresa grin."
            show teresa stream neutral
        else:
            $ AddChatter(vig4_sc1_2_comment16)
            macS "Like we always do."
    else:
        macS "If BC is there, we can just sneak past 'em."
        $ AddChatter(vig4_sc1_2_comment17)
        if gunsBlazing == False:
            macS "Gibian V-style."
    pS "Hopefully that won't be necessary."
    "The scan finishes."
    pS "Welp, no BC signatures. Not even a spaceport of any kind."
    pS "It's quieter than a Glorak's nest during mating season."
    enS "I don't want to know how you know that."
    pS "Your loss, it's a fun story."
    $ AddChatter(vig4_sc1_2_comment18)
    pS "There's just one small town."
    "The screen zooms in on a wireframe of a collection of buildings nestled into the crook of a mountain range."
    "Jennica points at a red light flashing in the center of one of the town's buildings."
    $ AddChatter(vig4_sc1_2_comment19)
    ##could cut from here to "I want to scout out the town" - saves 10 lines
    pS "A town that those coordinates we downloaded just so happens to be directing us to."
    mS "I want to scout out the town before we bring MAC in."
    $ AddChatter(vig4_sc1_2_comment20)
    menu:
        mS "I want to scout out the town before we bring MAC in."
        "Teresa, you're with me.":
            mS "Teresa, you're with me."
            mS "We'll go in, get a lay of the land, and make contact once we're sure it's safe."
            enS "Affirmative."
            mS "Jennica, you and MAC stay with the ship. If we radio in that the situation's bad, you take off immediately."
            pS "Aye aye, Cap."
    macS "Stay on the ship!?"
    if macPessimism > macHope:
        macS "But if it's a trap, you'll need reinforcements."
    else:
        macS "But I can prove to the Dragonflies that you're friendly." 
    macS "Captain, I can help!"
    $ AddChatter(vig4_sc1_2_comment21)
    menu:
        macS "Captain, I can help!"
        "We can't take any chances.":
            mS "We came all this way to keep you safe, MAC."
            mS "We can't leave anything to chance now."
            $ AddChatter(vig4_sc1_2_comment22)
            enS "Don't worry MAC, I'll have the captain's back."
        "This time you'll follow my orders, MAC.":
            $ kcEngagement -= 1
            mS "MAC, this time you'll follow my orders."
            mS "No wandering off like you did on Akar."
            $ AddChatter(vig4_sc1_2_comment22)
            macS "But that was--"
            mS "Stay. On. The. Ship."
            $ AddChatter(vig4_sc1_2_comment23)
    macS "I understand."
    macS "I don't like it, but I understand."
    pS "They'll be safe, MAC. And it means more pal time for the two of us!"
    play audio "macSad.wav"
    "MAC hums low in response."
    "The crew turns to face me."
    menu:
        "The crew turns to face me."
        "We've come so far.":
            mS "Everyone, I know it's been a hard month."
            mS "This journey...it damn near broke us a couple of times."
            mS "But in those moments, everyone here picked each other up."
            mS "Now we're at the finish line. Just a couple more hours and we'll be in the clear."
        "Stay focused.":
            mS "Everyone, I know it's been a hard month."
            mS "But now isn't the time to relax."
            mS "We have to stay focused until the mission is complete."
            mS "So lock in and stay alert. Just a couple more hours and we'll be in the clear."
    mS "And we'll be make those BC bastards choke on our trail of stardust."
    pS "Ooh rah, Cap."
    enS "Well said."
    mS "To your stations."
    hide jennica with dissolve
    hide teresa with dissolve
    "Jennica turns and heads up to the helm. Teresa goes to the armory to get outfitted."
    "MAC doesn't say anything."
    "As I turn around and head to my quarters, I can feel his attention on my back."
    $ AddChatter(vig4_sc1_2_comment24)
    hide mac with dissolve
    jump vig4_sc2_1

label vig4_sc2_1():
    show vig1_town_stream at topleft onlayer background with dissolve
    hide shiphub_stream
    play music "soundtrack/polaris.wav" volume 1.2
    "The activity in town is frenetic."
    $ AddChatter(vig4_sc1_2_comment25)
    "Dozens of people mill about the roads, carrying large boxes and sacks down the roads."
    "They don't stop as Teresa and I enter the outskirts."
    $ AddChatter(vig4_sc1_2_comment26)
    "But the second we step onto the roads, something makes the hair on the back of my neck stand up."
    "It's like we're being watched."
    $ AddChatter(vig4_sc2_1_comment1)
    show teresa stream neutral at stream_right with dissolve
    enS "Lotta activity."
    "Teresa's eyes dart back and forth."
    menu:
        "Teresa's eyes dart back and forth."
        "Stay calm, Teresa.":
            mS "Stay calm, Teresa. We don't want to draw attention to ourselves."
            enS "Roger."
            $ AddChatter(vig4_sc2_1_comment2)
        "Keep your head on a swivel.":
            mS "Keep your eyes up for anything suspicious."
            enS "Roger."
    "We step off the side of the road into a small alley."
    "I pull out the tracker. The coordinates we need to get to are in the direction everyone is moving."
    mS "We gotta follow these crowds."
    enS "Let's stick to the sides of the road."
    townguy "Well, hello, strangers, you must be here for the star shower!"
    show customs agent at stream_left with dissolve
    "A man with a sack of grain hanging over his left shoulder approaches Teresa and I from the alley."
    townguy "We get visitors so rarely, it's lovely to have you!"
    $ AddChatter(vig4_sc2_1_comment3)
    menu:
        townguy "We get visitors so rarely, it's lovely to have you!"
        "Star shower?":
            mS "Star shower?"
            townguy "You don't know? It's the biggest astronomical happening of the decade!"
            $ AddChatter(vig4_sc2_1_comment4)
            townguy "Once every ten years a hail of meteors passes by Polaris close enough to watch through the atmosphere."
            "He gestures to all the activity."
            townguy "As you can see, the whole town's gettin' ready for a festival."
            $ AddChatter(vig4_sc2_1_comment5)
            townguy "If you're not here for that, what could you be here for?"
            $ AddChatter(vig4_sc2_1_comment6)
            "Teresa has shifted just into the man's blindspot. Her hand grips a small stun rod in her belt."
            menu:
                "Teresa has shifted just into the man's blindspot. Her hand grips a small stun rod in her belt."
                "Signal Teresa to stun him.":
                    $ stunGuy = True
                    $ outlaw += 1
                    $ pdEngagement += 1
                    $ engineerApproval += 1
                    mS "Oh, right the \"star shower,\" I completely forgot about that."
                    "As I speak, Teresa snaps the stun rod out and jabs it into the man's neck."
                    "The sack of grain slumps to the ground, followed by his body."
                    hide customs agent with dissolve
                    $ AddChatter(vig4_sc2_1_comment7)
                    enS "Figured we didn't want some rube hanging around us."
                    $ AddChatter(vig4_sc2_1_comment8)
                    mS "Slick move."
                    enS "Thank you, Captain."
                    jump vig4_sc2_2_solo
                "We're just passing through.":
                    $ marshal += 1
                    $ csEngagement += 1
                    $ engineerApproval -= 1
                    mS "We're just passing through."
                    mS "Our ship was having a bit of trouble so we decided to make a quick landing and see about some repairs."
                    townguy "Oh I'm sorry. Ship trouble is always scary."
                    enS "You've had experience?"
                    townguy "Well, not really. But it sounds scary!"
                    $ AddChatter(vig4_sc2_1_comment12)
                    townguy "Oh, I know, you should go to North Star! They'll help you out real quick."
                    ##*Insert streamer reaction asking chat if we can trust him
                    townguy "Come on, I'll show you!"
                    jump vig4_sc2_2_accompanied
        "We're just passing through.":
            mS "We're just passing through."
            mS "Our ship was having a bit of trouble so we decided to make a quick landing and see about some repairs."
            townguy "Oh I'm sorry. Ship trouble is always scary."
            enS "You've had experience?"
            townguy "Well, not really. But it sounds scary!"
            $ AddChatter(vig4_sc2_1_comment12)
            townguy "You should stay for the star shower though, it's really dramatic."
            townguy "Once every ten years a hail of meteors passes by Polaris close enough to watch through the atmosphere."
            "He gestures to all the activity."
            $ AddChatter(vig4_sc2_1_comment13)
            townguy "As you can see, the whole town's gettin' ready for a festival."
            "Teresa steps up close to the man."
            enS "We appreciate the invite, but we really should make our repairs and be on our way."
            "Her hand is on a stun rod in her belt."
            menu:
                "Her hand is on a stun rod in her belt."
                "Signal Teresa to stun him":
                    $ stunGuy = True
                    $ pdEngagement += 1
                    $ outlaw += 1
                    $ engineerApproval += 1
                    "She snaps the stun rod out and jabs it into the man's neck."
                    "The sack of grain slumps to the ground, followed by his body."
                    hide customs agent with dissolve
                    $ AddChatter(vig4_sc2_1_comment7)
                    enS "Figured we didn't want some rube hanging on to us."
                    $ AddChatter(vig4_sc2_1_comment8)
                    mS "Slick move."
                    enS "Thank you, Captain."
                    jump vig4_sc2_2_solo
                "Signal Teresa to stand down.":
                    $ marshal += 1
                    $ csEngagement += 1
                    $ engineerApproval -= 1
                    "I give Teresa the signal to stand down."
                    $ AddChatter(vig4_sc2_1_comment14)
                    "She backs away from the man."
                    $ AddChatter(vig4_sc2_1_comment15)
                    townguy "Of course, repairs should be your priority."
                    townguy "Oh, I know, you should go to North Star! They'll help you out real quick."
                    $ AddChatter(vig4_sc2_1_comment16)
                    townguy "Come on, I'll show you!"
                    jump vig4_sc2_2_accompanied

label vig4_sc2_2_solo():
    "We check to make sure nobody saw, then step back onto the main road."
    "Following the tracker, we make our way through the crowds."
    "Without breaking step, the townsfolk we pass by look up to smile at us and tip their caps."
    "I try to smile back. But my face feels tight."
    "Everything feels tight."
    $ AddChatter(vig4_sc2_2_comment4)
    "Eventually, we pass a wide plaza where the crowds of people are setting up tables, chairs, and stalls."
    "At the north end of the plaza, an immense tower stretches up into the sky. It almost feels like a church."
    enS "Seems like it's going to be some party."
    menu:
        enS "Seems like it's going to be some party."
        "Jenn's going to hate to miss this.":
            mS "Jenn's gonna be disappointed we can't take part."
            $ AddChatter(vig4_sc2_solo_comment1)
            enS "Maybe we'll come back one day."
            mS "Maybe."
        "I've had my fill of parties.":
            mS "After Akar, I think I've had my fill of parties."
            $ AddChatter(vig4_sc2_solo_comment2)
            enS "Couldn't agree more."
    "I check the tracker. We're on the right path."
    "I glance up as we step out of the plaza."
    "A camera tilts to the side, following us. Then pans back in the other direction."
    enS "I saw it."
    $ AddChatter(vig4_sc2_2_comment1)
    enS "Think it could be BC?"
    mS "Maybe, but it doesn't matter."
    $ AddChatter(vig4_sc2_2_comment2)
    mS "No turning back now."
    $ AddChatter(vig4_sc2_2_comment3)
    "The crowds start to thin once we're past the plaza."
    jump vig2_sc2_3

label vig4_sc2_2_accompanied():
    "The man hefts the sack over his shoulder and steps onto the road, motioning for us to follow him."
    menu:
        "The man hefts the sack over his shoulder and steps onto the road, motioning for us to follow him."
        "Follow the man.":
            "I step out of the alley."
            mS "Lead on."
            "Beaming, the man turns and walks down the road."
        "We really shouldn't.":
            mS "Oh, we don't want to distract you from your responsibilities."
            townguy "Nonsense! It's on the way for me anyway."
            "He's out in the open, too obvious to stun him."
            mS "Well, in that case, lead on."
            "Beaming, the man turns and walks down the road."
    $ AddChatter(vig4_sc2_accompanied_comment1)
    "Teresa steps up to my side and whispers."
    enS "What the hell? We don't want some rube around us right now."
    $ AddChatter(vig4_sc2_1_comment8)
    mS "At least it'll help us blend in."
    enS "And if he's a BC spy."
    "I check the scanner quckly. We're on the right path to the coordinates."
    mS "We're going the right way for now. Let's keep things calm."
    "We make our way through the crowd, following our guide."
    "Without breaking step, the townsfolk we pass by look up to smile at us and tip their caps."
    "I try to smile back. But my face feels tight."
    "Everything feels tight."
    $ AddChatter(vig4_sc2_2_comment4)
    "Then we move out of the road, emerging into a wide plaza where the crowds of poeple are setting up tables, chairs, and stalls."
    "At the north end of the plaza, an immense tower stretches up into the sky. It almost feels like a church."
    "The plaza is thick with people. It's an opportunity."
    hide customs agent with dissolve
    $ AddChatter(vig4_sc2_accompanied_comment3)
    "Teresa and I dart into an alley and out of sight."
    "We emerge from the alley onto another road."
    enS "Ok, this feels better."
    $ AddChatter(vig4_sc2_accompanied_comment4)
    "I check the tracker quickly, then catch movement out of the corner of my eyes."
    "A camera tilts to the side, following us. Then pans back in the other direction."
    enS "I saw it."
    $ AddChatter(vig4_sc2_2_comment1)
    enS "Think it could be BC?"
    mS "Maybe, but it doesn't matter."
    $ AddChatter(vig4_sc2_2_comment2)
    mS "No turning back now."
    "The detour has taken us out of the way. Our pace quickens."
    $ AddChatter(vig4_sc2_2_comment3)
    "We have time to make up."
    jump vig2_sc2_3

label vig2_sc2_3():
    ### Could cut this exchange about MAC -- but I like it ###
    enS "Say, Captain."
    enS "There's something I've been meaning to ask you about. Just haven't found the time."
    enS "Have you noticed anything changing about MAC's personality?"
    ##*Add a streamer reaction here
    menu:
        enS "Have you noticed anything changing about MAC's personality?"
        "What do you mean?":
            mS "Changing how?"
            enS "His vocabulary and grammar."
            enS "Jennica first pointed it out to me after we left Akar."
            $ AddChatter(vig4_sc2_3_comment1)
            enS "Wanted to see what you think of it?"
            menu:
                enS "Wanted to see what you think of it?"
                "I hadn't noticed":
                    mS "I didn't notice."
                    $ AddChatter(vig4_sc2_3_comment4)
                    enS "It's like he's starting to talk like us."
                    $ AddChatter(vig4_sc2_3_comment5)
                    enS "It's a little...disconcerting."
                    mS "I'll keep an eye on it."
                    $ AddChatter(vig4_sc2_3_comment6)
                "Now that you mention it...":
                    mS "Now that you mention it, yeah he is talking differently."
                    $ AddChatter(vig4_sc2_3_comment2)
                    enS "It's like he's starting to talk like us."
                    enS "It's a little...disconcerting."
                    $ AddChatter(vig4_sc2_3_comment3)
                    menu:
                        enS "It's a little...disconcerting."
                        "We just have to get him to the Dragonflies.":
                            $ kcEngagement -= 1
                            mS "We're almost there. All we have to do is get him to the Dragonflies."
                            $ AddChatter(vig4_sc2_3_comment8)
                            pause 0.5
                            $ AddChatter(vig4_sc2_3_comment9)
                            mS "They can worry about his personality after that."
                            enS "I suppose that's true."
                            $ AddChatter(vig4_sc2_3_comment10)
                        "I'll keep an eye on it.":
                            mS "Thanks for bringing it up. I'll keep an eye on it and talk with him about it."
                            $ AddChatter(vig4_sc2_3_comment7)
                            enS "Sounds like a good idea. He responds better to you than me and Jenn."
        "Like his speech patterns?":
            mS "You mean his speech patterns?"
            mS "They're becoming less robotic."
            enS "Exactly!"
            enS "Jennica noticed it after we left Akar."
            enS "It's like he's starting to talk like us."
            $ AddChatter(vig4_sc2_3_comment6)
            enS "It's a little...disconcerting."
            menu:
                enS "It's a little...disconcerting."
                "We just have to get him to the Dragonflies.":
                    $ kcEngagement -= 1
                    mS "We're almost there. All we have to do is get him to the Dragonflies."
                    $ AddChatter(vig4_sc2_3_comment8)
                    pause 0.5
                    $ AddChatter(vig4_sc2_3_comment9)
                    mS "They can worry about his personality after that."
                    enS "I suppose that's true."
                    $ AddChatter(vig4_sc2_3_comment10)
                "I'll keep an eye on it.":
                    mS "Thanks for bringing it up. I'll keep an eye on it and talk with him about it."
                    $ AddChatter(vig4_sc2_3_comment7)
                    enS "Sounds like a good idea. He responds better to you than me and Jenn."
        "He's not listening to me like he used to.":
            mS "Yeah, he's not listening to me like he used to."
            enS "That too, but I meant more subtly."
            $ AddChatter(vig4_sc2_3_comment11)
            enS "It's his speech patterns. They're becoming less robotic."
            enS "Jennica noticed it after we left Akar."
            enS "It's like he's starting to talk like us."
            $ AddChatter(vig4_sc2_3_comment6)
            enS "It's a little...disconcerting."
            menu:
                enS "It's a little...disconcerting."
                "We just have to get him to the Dragonflies.":
                    $ kcEngagement -= 1
                    mS "We're almost there. All we have to do is get him to the Dragonflies."
                    $ AddChatter(vig4_sc2_3_comment8)
                    pause 0.5
                    $ AddChatter(vig4_sc2_3_comment9)
                    mS "They can worry about his personality after that."
                    $ AddChatter(vig4_sc2_3_comment10)
                    enS "I suppose that's true."
                "I'll keep an eye on it.":
                    mS "Thanks for bringing it up. I'll keep an eye on it and talk with him about it."
                    $ AddChatter(vig4_sc2_3_comment7)
                    enS "Sounds like a good idea. He responds better to you than me and Jenn."
    "We get to the end of the road."
    "It's dead quiet."
    "No one is around. No prying eyes, no crowds of people."
    "There's not even a breeze."
    "The tracker is pointing dead ahead, at a small shop with the words \"North Star\" emblazoned on the facade."
    $ AddChatter(vig4_sc2_3_comment12)
    enS "This is it?"
    mS "This is it."
    enS "I was expecting...more."
    $ AddChatter(vig4_sc2_3_comment13)
    "Teresa scans our surroundings."
    enS "At least it's quiet here."
    $ AddChatter(vig4_sc2_3_comment14)
    menu:
        enS "At least it's quiet here."
        "We'll see.":
            mS "That could be good or bad."
        "I wish we had more info.":
            mS "I wish we had more info."
            mS "Feels like we're aiming without a scope."
    enS "I know what you mean."
    enS "How do you want to play this?"
    menu:
        enS "How do you want to play this?"
        "Carefully.":
            $ engineerApproval += 1
            $ AddChatter(vig4_sc2_3_comment17)
            mS "Carefully. We have to confirm they're Dragonflies before we reveal anything about ourselves."
            $ AddChatter(vig4_sc2_3_comment18)
            enS "Sounds good. I'll follow your lead."
        "Let's be direct.":
            $ engineerApproval -= 1
            mS "We can't keep hiding. Let's be direct, establish what we're here for."
            enS "Are you sure that's the right call?"
            $ AddChatter(vig4_sc2_3_comment15)
            mS "I've had enough skulking around. And we've dealt with more dangerous situations before."
            enS "All the same, I'd prefer not to make a hasty getaway if we don't have to."
            $ AddChatter(vig4_sc2_3_comment16)
            enS "But I'll follow your lead, Captain."
    hide teresa with dissolve
    stop music fadeout 2.0
    jump vig4_sc2_4

label vig4_sc2_4():
    show warehouse_stream at topleft onlayer background with dissolve
    hide vig1_town_stream
    show teresa stream neutral at stream_right with dissolve
    "The shop is musty and hot."
    "There's a smell of singed metal and the whir of something like an engine coming from the back."
    show coil stream neutral at stream_center with dissolve
    $ AddChatter(vig4_sc2_4_comment1)
    "An old man stands at a counter, fully occupied by applying some small piece of metal to a circuit board in his hands."
    "He doesn't seem to notice us."
    $ AddChatter(vig4_sc2_4_comment2)
    menu:
        "He doesn't seem to notice us."
        "Nice shop.":
            mS "Hi there, nice shop you have here."
            mS "Mind if I ask you a few questions?"
        "Step up and ring a bell.":
            "I step up and ring the bell on the counter."
            play audio "ding.wav" volume 5.0
            mS "Excuse me."
    "The old man doesn't move. Except for his eyes."
    "They glance sidelong, looking me up and down while his hands stay perfectly still."
    "He returns his attention to the circuit."
    cS "Outsiders. What are you doing in Polaris?"
    $ AddChatter(vig4_sc2_4_comment3)
    $ AddChatter(vig4_sc2_4_comment4)
    menu:
        cS "Outsiders. What are you doing in Polaris?"
        "We're looking for someone.":
            mS "We're looking for someone."
            cS "And \"someone\" you have found."
            cS "Probably dozens of someones."
            "He lifts his eyebrows, as if pointing them at me."
            if stunGuy == True:
                cS "Maybe even one who is just now waking up to a painful headache in an alleyway."
                $ AddChatter(vig4_sc2_4_comment7)
            else:
                cS "Maybe even one who you abandoned in a bustling plaza."
            "I feel Teresa tense up."
            $ AddChatter(vig4_sc2_4_comment5)
            enS "How do you know about that?"
            cS "Intelligence of all kinds is my business."
            $ AddChatter(vig4_sc2_4_comment6)
        "We're just passing through.":
            mS "We're just some travelers passing through. Need some repairs for our ship."
            if stunGuy == True:
                cS "Travelers who stun amicable locals?"
                $ AddChatter(vig4_sc2_4_comment7)
            else:
                cS "Travelers who abandon kind guides offering to help them?"
                $ AddChatter(vig4_sc2_4_comment8)
            "I feel Teresa tense up."
            $ AddChatter(vig4_sc2_4_comment5)
            enS "How do you know about that?"
            cS "Intelligence of all kinds is my business."
            $ AddChatter(vig4_sc2_4_comment6)        
            mS "We're just looking for repairs, and maybe a soft bed to spend the night."
            cS "Polaris can be that. But we don't have much else."
            cS "Just dirt and stars."
            $ AddChatter(vig4_sc2_4_comment9) ##*Make one of these interactable??
            cS "And the beds aren't too soft either."
            $ AddChatter(vig4_sc2_4_comment10)
    "The old man removes his fingers from the circuit board and places it down on the counter."
    cS "We are a peaceful town here. And that peace is hard won from the chaos of this galaxy."
    menu:
        cS "We are a peaceful town here. And that peace is hard won from the chaos of this galaxy."
        "It seems lovely":
            mS "It seems like a nice, quiet little slice of heaven."
            cS "And we like to keep it that way." 
        "Is it so peaceful?":
            mS "Peace is hard to come by. You don't have any troubles here?"
            cS "Only those that come from outsiders."
    enS "Is that a threat?"
    $ AddChatter(vig4_sc2_4_comment11)
    cS "It's a fact."
    $ AddChatter(vig4_sc2_4_comment12)
    $ AddChatter(vig4_sc2_4_comment13)
    menu:
        cS "It's a fact."
        "I think we got off on the wrong foot.":
            $ csEngagement += 1
            $ marshal += 1
            mS "I think we got off on the wrong foot here."
            mS "We've come a long way to deliver something important."
            mS "That means something to you, doesn't it?"
            "The old man stares deeply into my eyes."
            cS "I cannot answer your question unless I can be certain that you are a friend."
            cS "I dislike being rude, but your look and behavior does not speak of friendliness."
            "He looks us up and down again."
            cS "Self-interest."
            $ AddChatter(vig4_sc2_4_comment14)
            enS "\"Self-interest!?\""
            "Teresa's voice reaches a fever pitch instantly."
            enS "Listen here you old coot, you have no idea what we've had to do to be standing here right now."
            $ AddChatter(vig4_sc2_4_comment15)
            enS "The friends we lost, the sacrifices we had to make."
            mS "Resa--"
            enS "No, Captain, respectfully." 
            enS "I'm not going to stand here and take a cryptic lecture from some out of touch relic."
            $ AddChatter(vig4_sc2_4_comment16)
            "The whirring from the back stops as footsteps approach."
            vS "Pops, is everything okay. I thought I heard--Oh!"
            show vega stream neutral at stream_left with dissolve
            "A young woman steps out from the back."
            $ AddChatter(vig4_sc2_4_comment17)
            "She's holding a rifle and aims it directly at Teresa."
            $ AddChatter(vig4_sc2_4_comment18)
            "In a flash, Teresa and I lift our blasters. Teresa aims at the old man while I keep my eye on the woman."
            $ AddChatter(vig4_sc2_4_comment19)
            vS "I see we have...guests?"
            cS "Nothing to worry about, Vega."
            $ AddChatter(vig4_sc2_4_comment20)
            cS "We are just having a conversation."
            $ AddChatter(vig4_sc2_4_comment21)
            "The old man's attention remains fixed on Teresa."
            $ AddChatter(vig4_sc2_4_comment22)
            cS "Go ahead, pull the trigger."
            enS "What!?"
            cS "My daughter will not retaliate. I promise."
            cS "Go on. Do what you do best."
            mS "Teresa, stand d--"
            "A bolt fires from Teresa's blaster."
            "A thin veil of light sparks in front of the old man's face. The blaster bolt dissipates into the air."
            ##* streamer react to the shield?
            $ AddChatter(vig4_sc2_4_comment23)
            cS "You should treat \"relics\" with more respect."
            $ AddChatter(vig4_sc2_4_comment24)         
        "Don't threaten my crew (draw weapon).":
            $ pdEngagement += 1
            $ kcEngagement += 1
            $ outlaw += 1
            $ engineerApproval += 1
            "I give Teresa a signal under the counter."
            $ AddChatter(vig4_sc2_4_comment25)
            mS "Sounds like a threat."
            mS "And nobody threatens my crew."
            "Teresa and I both draw our blasters and point them at the old man."
            $ AddChatter(vig4_sc2_4_comment26)
            mS "Now, you're going to answer our questions, or you're going to wake up with a mean headache."
            cS "Go ahead. Shoot."
            enS "What!?"
            cS "I mean it. Do what you do best."
            $ AddChatter(vig4_sc2_4_comment27)
            enS "You think we won't?"
            cS "I asked you to."
            "The old man starts to pull a blaster into the air."
            menu:
                "The old man starts to lift a blaster into the air."
                "Shoot.":
                    $ outlaw += 1
                    "I pull the trigger on my blaster."
                    "A thin veil of light sparks in front of the old man's face. The blaster bolt dissipates into the air."
                    cS "And now that your blaster has failed you, will you stoop to beating an old man?"
                    $ AddChatter(vig4_sc2_4_comment23)
                "Tell Teresa to stand down.":
                    $ marshal += 1
                    mS "Teresa, stand d--"
                    "A bolt fires from Teresa's blaster."
                    "A thin veil of light sparks in front of the old man's face. The blaster bolt dissipates into the air."
                    cS "Your discipline is wanting."
                    $ AddChatter(vig4_sc2_4_comment23)
            "The whirring from the back stops as footsteps approach."
            $ AddChatter(vig4_sc2_4_comment24)
            vS "Pops, is everything okay. I thought I heard--Oh!"
            show vega stream neutral at stream_left with dissolve
            "A young woman steps out from the back."
            $ AddChatter(vig4_sc2_4_comment27)
            "She's holding a rifle and aims it directly at Teresa as I pull my blaster on her."
            vS "I see we have...guests?"
            $ AddChatter(vig4_sc2_4_comment28)
            cS "Nothing to worry about, Vega."
            $ AddChatter(vig4_sc2_4_comment29)
            cS "We are just having a conversation."
            cS "Now, where were we?"
    #hide coil with Dissolve (0.5)
    macS "Captain!"
    show mac stream shock at stream_right5mac
    "Suddenly the door behind us bursts open as MAC rolls into the shop."
    if macViolence > macPeace:
        "His hand snaps up as a pulse of energy shoots from an exposed hole in his arm."
        "The pulse hits the rifle in the woman's hands, knocking it to the floor."
        $ AddChatter(vig4_sc2_4_comment30)
        show mac stream neutral
        macS "Threat neutralized."
        $ AddChatter(vig4_sc2_4_comment31)
    else:
        "His antenna glows blue and then releases a wave of light."
        enS "Shit!"
        "Teresa drops her blaster."
        vS "Ow, it's hot!"
        $ AddChatter(vig4_sc2_4_comment30)
        "The young woman drops the rifle."
        show mac stream neutral
        macS "Situation deescalated."
        $ AddChatter(vig4_sc2_4_comment31)
    ##* streamer reaction to start a MAC chant - if you do this, then later in the game we'll trigger a chant from the chat automatically. Probably on the return to Polaris alongside Moze's "speech"
    show jennica stream neutral at stream_left5 with Dissolve(0.5)
    pS "Cap, I'm so sorry he ran off while I was checking the engine lines and I--"
    $ AddChatter(vig4_sc2_4_comment32)
    "Jennica freezes as she recognizes the situation."
    pS "Oh."
    $ AddChatter(vig4_sc2_4_comment33)
    enS "Jenn, now's not the tim--"
    #play audio of gundrop
    "The sound of metal dropping on the floor."
    hide jennica with dissolve
    hide vega with dissolve
    hide teresa with dissolve
    show mac at stream_right_mac with move
    #show coil at stream_center with dissolve
    "The old man's eyes have gone wide. They're locked on MAC."
    cS "At last..."
    play music "soundtrack/theme.wav" volume 0.5 fadein 4.0
    "The old man gestures to MAC."
    cS "May I?"
    menu:
        cS "May I?"
        "First, tell us who you are.":
            $ csEngagement += 1
            mS "First tell us who you are."
            cS "I'm your contact, the one who has been transmitting the coordinates to lead you here."
            $ AddChatter(vig4_sc2_4_comment34)
            cS "I never believed you would actually arrive."
            $ AddChatter(vig4_sc2_4_comment35)
        "If he says it's ok.":
            $ kcEngagement += 1
            "I take my aim off of the old man and signal Teresa to let him pass."
            mS "If he says it's ok."
    "He turns to MAC."
    cS "Hello little one. It is nice to finally meet you."
    cS "I am Coil. What is your name?"
    "MAC looks from me to Teresa, to Jennica, and then back to Coil."
    macS "I am MAC."
    cS "Of course you are."
    cS "And are you ok? Are you well?"
    $ AddChatter(vig4_sc2_4_comment36)
    macS "I'm with my family."
    macS "How are you, Coil? Are you well?"
    "Coil kneels down in front of MAC. He takes one of his hands in his."
    $ AddChatter(vig4_sc2_4_comment37) #I don't know about this nonsense stuff happening during this moment. But I'll put it here for now. Maybe we change it or maybe we cut it to put emphasis on the Coil and MAC stuff.
    cS "I am much better now that you're here."
    $ AddChatter(vig4_sc2_4_comment38)
    "Coil looks back to me."
    "He smiles."
    $ AddChatter(vig4_sc2_4_comment39)
    cS "Thank you."
    hide coil with dissolve
    hide mac with dissolve
    hide warehouse_stream with dissolve
    jump vig4_sc2_5

label vig4_sc2_5():
    show warehouse_stream at topleft onlayer background with dissolve
    show vega stream neutral at stream_left5 with dissolve
    play music "soundtrack/theme.wav" volume 1.2
    "Things are still tense for a little while."
    "Coil hangs up the guns and goes to fetch some tea while Vega brings out some chairs for us."
    show teresa stream neutral at stream_right
    #hide vega with dissolve
    "Teresa doesn't start to relax her shoulders until she gets the tea in her hands."
    $ AddChatter(vig4_sc2_5_comment1)
    show jennica stream neutral at stream_left
    pS "I don't understand, why didn't you just tell them who we were."
    show coil stream neutral at stream_center with dissolve
    cS "I'm afraid I didn't give them much of a chance."
    $ AddChatter(vig4_sc2_5_comment2)
    cS "I was afraid that you were agents of BigCorp, that they'd finally caught up with us."
    enS "You didn't seem particularly scared."
    cS "I've learned to hide it over the years."
    $ AddChatter(vig4_sc2_5_comment3)
    cS "I would like to express profuse apologies for my actions. I will try to make it up to you."
    menu:
        cS "I would like to express profuse apologies for my actions. I will try to make it up to you."
        #"No big deal.":
        #    mS "No worries."
        #    mS "In my line of work it's a standard form of \"hello.\""
        "Thanks for the apology.":
            $ macHope += 1
            $ csEngagement += 1
            mS "Things were a bit tense. It happens." 
            $ AddChatter(vig4_sc2_5_comment4)
            mS "Thanks for the apology."
            cS "I appreciate you taking it so well."
            $ AddChatter(vig4_sc2_5_comment5)
            cS "You must have questions."
        "I would have done the same thing.":
            $ macHope += 1
            $ kcEngagement += 1
            mS "I would have done the same thing in your position."
            $ AddChatter(vig4_sc2_5_comment6)
            mS "Being careful keeps you alive."
            cS "I appreciate you taking it so well."
            $ AddChatter(vig4_sc2_5_comment7)
            cS "You must have questions."
        "I still don't trust you.":
            $ macPessimism -= 1
            $ pdEngagement += 1
            mS "It certainly didn't lay the best foundation for trust."
            $ AddChatter(vig4_sc2_5_comment8)
            mS "You can start making it up to us by answering my questions."
            $ AddChatter(vig4_sc2_5_comment9)
            cS "I understand. You must have several."
    enS "Plenty."
    pS "A whole heap."
    $ AddChatter(vig4_sc2_5_comment10)
    cS "Ask away."
    "Jennica and Teresa turn to me."
    #hide jennica with dissolve
    #hide teresa with dissolve
    show mac stream neutral at stream_right5mac with dissolve
    #show vega at stream_left with dissolve
    "What do I want to know?"
    jump vig4_sc2_6

label vig4_sc2_6():
    menu:
        "What do I want to know?"
        "What is this place?" if polarisQuestion == False:
            $ polarisQuestion = True
            mS "What is this place?"
            cS "Like I said, Polaris is a peaceful town."
            $ AddChatter(vig4_sc2_6_comment1)
            cS "It is also an outpost for the Dragonflies network."
            menu:
                cS "It is also an outpost for the Dragonflies network."
                "Everyone in this town is a Dragonfly?":
                    mS "You mean everyone in this town is a Dragonfly?"
                    cS "Not everyone. Some of us are just people."
                    cS "Farmers, doctors, soldiers, engineers. People who are tired of BC's squeezing or the Alliance's bureaucracy."
                    vS "People who want to be free."
                    $ AddChatter(vig4_sc2_6_comment2)
                    cS "I'm sure you are all well aware how difficult it can be to get here."
                    ##* reaction from streamer about this
                    cS "We keep it that way. A safehouse for the Dragonflies and for anyone else who needs a home."
                    $ AddChatter(vig4_sc2_6_comment3)
                    pause 0.5
                    $ AddChatter(vig4_sc2_6_comment4)
                    menu:
                        cS "We keep it that way. A safehouse for the Dragonflies and for anyone else who needs a home."
                        "How did you build this?":
                            mS "How could you build this?"
                            enS "The cost of setting up the artificial atmosphere alone would be astronomical."
                            cS "You'll have to ask a man named Reynar about that."
                            pS "Reynar's a Dragonfly!?"
                            $ AddChatter(vig4_sc2_6_comment5)
                            cS "No, but he was amenable to a deal when we caught up with him fifeen years ago."
                            vS "We helped him with some trouble on Akar. He gave us the technology we needed."
                            $ AddChatter(vig4_sc2_6_comment6)
                            vS "That deal allowed us make this place a reality."
                            $ AddChatter(vig4_sc2_6_comment7)
                            jump vig4_sc2_6
                        "I have other questions":
                            mS "I have other questions."
                            cS "Shoot. We have all the time in the galaxy now."
                            jump vig4_sc2_6
                "How did you build this?":
                    mS "I don't understand. How could you build this?"
                    enS "The cost of setting up the artificial atmosphere alone would be astronomical."
                    cS "You'll have to ask a man named Reynar about that."
                    pS "Reynar's a Dragonfly!?"
                    $ AddChatter(vig4_sc2_6_comment5)
                    cS "No, but he was amenable to a deal when we caught up with him fifeen years ago."
                    vS "We helped him with some trouble on Akar. He gave us the technology we needed."
                    $ AddChatter(vig4_sc2_6_comment6)
                    vS "That deal finally let us make this place a reality."
                    $ AddChatter(vig4_sc2_6_comment7)
                    menu:
                        vS "That deal finally let us make this place a reality."
                        "So everyone in this town is a Dragonfly?":
                            mS "You mean everyone in this town is a Dragonfly?"
                            cS "Not everyone. Some of us are just people."
                            cS "Farmers, doctors, soldiers, engineers. People who are tired of BC's squeezing or the Alliance's bureaucracy."
                            vS "People who want to be free."
                            $ AddChatter(vig4_sc2_6_comment2)
                            cS "I'm sure you are all well aware how difficult it can be to get here."
                            ##* reaction from streamer about this
                            cS "We keep it that way. A safehouse for the Dragonflies and for anyone else who needs a home."
                            $ AddChatter(vig4_sc2_6_comment3)
                            pause 0.5
                            $ AddChatter(vig4_sc2_6_comment4)
                            jump vig4_sc2_6
                        "I have other questions":
                            mS "I have other questions."
                            vS "Shoot. We have all the time in the galaxy now."
                            jump vig4_sc2_6
                "I have other questions":
                    mS "I have other questions."
                    vS "Shoot. We have all the time in the galaxy now."
                    jump vig4_sc2_6
        "Who are you two?" if vegacoilQuestion == False:
            $ vegacoilQuestion = True
            mS "So who are you two exactly? How'd you end up here?"
            cS "Many years ago, I was a doctoral researcher studying cogitive circuitry."
            cS "During my studies, I met a colleague. Someone whose work far outstripped my own." 
            macS "Elijah Vanas."
            cS "Yes, MAC. Your father."
            cS "We became...close, and started collaborating."
            $ AddChatter(vig4_sc2_6_comment8)
            cS "When we graduated, BigCorp offered us an exorbitant grant to conduct our research."
            $ AddChatter(vig4_sc2_6_comment9)
            cS "Under the provision that they would own our work in its entirety."
            cS "I had reservations about the deal, but Elijah convinced me." 
            cS "He said we could do more good with their resources than they could do bad with our work."
            cS "Shortsighted fool."
            cS "But a shortsighted fool who I could not say \"no\" to."
            ##* streamer reaction
            mS "What were the two of you working on?"
            cS "Our little friend here."
            $ AddChatter(vig4_sc2_6_comment10)
            cS "At least, I was around for the first prototypes."
            $ AddChatter(vig4_sc2_6_comment11)
            cS "It didn't take long for my conscience to get the better of me."
            cS "Complicity is how they hold us hostage. So I left."
            $ AddChatter(vig4_sc2_6_comment14)
            cS "I endeavored to convince Vanas to join me. He refused."
            "Coil suddenly gets a distant look in his eye. Like he's gazing past me."
            $ AddChatter(vig4_sc2_6_comment12)
            cS "I said some things I have regretted ever since."
            $ AddChatter(vig4_sc2_6_comment13)
            cS "You can probably guess what happened next. I wandered the stars, lost myself in the bottle."
            "Coil turns to look at Vega."
            cS "Until I met Vega."
            cS "A young scrapper with the biggest heart and the sharpest mind I ever met."
            vS "Oh come on, Pops, you say it the same way every time."
            cS "It only gets more true the more I say it."
            $ AddChatter(vig4_sc2_6_comment15)
            vS "I didn't really have anyone before Pops. Never knew my parents, didn't want to."
            vS "I just wanted to make things. Whatever it was, speeders, ship parts, rifles, shields, anything."
            $ AddChatter(vig4_sc6_comment16)
            vS "This old lugnut found me while I was trying to lift a nice piece of circuitry off him."
            vS "Guess he was impressed I even knew it was valuable."
            cS "I got sober that day."
            $ AddChatter(vig4_sc6_comment17)
            ## BRING swayy0scar back for the climax!
            vS "And we set off to make a difference."
            "She looks to Coil."
            $ AddChatter(vig4_sc2_6_comment18)
            vS "Together."
            cS "Together."
            jump vig4_sc2_6
        "So, what's the plan?" if polarisQuestion == True and vegacoilQuestion == True:
            mS "Ok, so we've made it. What's next?"
            "Coil and Vega look at one another."
            $ AddChatter(vig4_sc2_6_comment19)
            vS "I'm afraid we can't tell you in detail."
            cS "We appreciate everything that you've done."
            $ AddChatter(vig4_sc2_6_comment20)
            vS "Truly, it means the galaxy to us."
            cS "What I can tell you, is that you arrived just in the nick of time."
            cS "Tomorrow, we will take MAC to rendezvous with the core of the Dragonflies."
            mS "Okay, great. We'll get our ship outfitted and ready to go at dawn."
            "Coil pauses and leans forward, locking eyes with me."
            $ AddChatter(vig4_sc2_6_comment21)
            cS "No, Captain Mozely, you don't understand."
            cS "We will be taking MAC. Just MAC." 
            cS "Not you and your crew."
            $ AddChatter(vig4_sc2_6_comment22)
            pause 0.5
            $ AddChatter(vig4_sc2_6_comment23)
            pause 0.3
            $ AddChatter(vig4_sc2_6_comment24)
            $ AddChatter(vig4_sc2_6_comment25)
            pause 0.2
            $ AddChatter(vig4_sc2_6_comment26)
            ##* streamer reaction
            enS "What!?"
            pS "You're joking right?"
            macS "Captain?"
            menu:
                macS "Captain?"
                "Like hell you are!":
                    $ outlaw += 1
                    $ pdEngagement += 1
                    $ kcEngagement += 2
                    $ csEngagement += 1
                    $ engineerApproval += 1
                    $ pilotApproval += 1
                    mS "Like hell you're taking him without us!"
                    $ AddChatter(vig4_sc2_6_comment27)
                    pS "This family doesn't break up."
                    $ AddChatter(vig4_sc2_6_comment28)
                    enS "Seconded."
                    macS "Thirded!"
                    $ AddChatter(vig4_sc2_6_comment29)
                    $ AddChatter(vig4_sc2_6_comment30)
                    vS "This was always the mission, all of you knew that when you accepted it."
                "This was always part of the plan.":
                    $ marshal += 1
                    $ csEngagement += 1
                    $ kcEngagement -= 2
                    $ pdEngagement -= 1
                    $ engineerApproval += 1
                    $ pilotApproval -= 1
                    "I take a long breath."
                    "The stale atmosphere sticks in my throat. But I hold steady."
                    mS "Teresa, Jennica, this was always part of the plan, remember?"
                    $ AddChatter(vig4_sc2_6_comment31) 
                    pS "Yeah, but..."
                    $ AddChatter(vig4_sc2_6_comment32)
                    enS "I guess I wanted to forget that part."
                    $ AddChatter(vig4_sc2_6_comment33) 
            cS "It's not up to me. Even Vanas was to be left behind if he made it this far."
            $ AddChatter(vig4_sc2_6_comment34) 
            cS "But give me a chance. I can get in touch with my superiors and make a case for you."
            $ AddChatter(vig4_sc2_6_comment35) 
            cS "After all you have been through, they might listen."
            vS "Pops can be very persuasive. Trust him."
            $ AddChatter(vig4_sc2_6_comment36) 
            cS "It will take some time to reach the Dragonflies and the festival will begin shortly."
            cS "This is a true achievement. You should go and celebrate."
            $ AddChatter(vig4_sc2_6_comment37) 
            cS "These days we have precious few excuses to simply enjoy life."
            "Coil stands and reaches out a hand."
            $ AddChatter(vig4_sc2_6_comment38) 
            menu:
                "Coil stands and reaches out a hand."
                "Shake his hand.":
                    $ csEngagement += 1
                    $ kcEngagement -= 1
                    "I stand and shake his hand."
                    "Coil nods at me."
                    $ AddChatter(vig4_sc2_6_comment39)
                    cS "I'll do my best, I promise."
                    $ AddChatter(vig4_sc2_6_comment40)
                "Turn away.":
                    $ kcEngagement += 1
                    $ csEngagement -= 1
                    "I stand and turn to look at my crew."
                    mS "Come on, let's see what this festival is like."
                    $ AddChatter(vig4_sc2_6_comment41)
                    "Coil lets his hand fall and sighs." 
            cS "Vega, you go to the festival. I'll join you after making contact."
            vS "Okay, Pops."
            "Coil turns around and heads to the back of the shop."
            "The sounds from outside are suddenly loud and lively."
            play music "soundtrack/festival.wav" volume 0.3
            "Music drifts in through the windows and the cries of laughter and joy hang in the air."
            $ AddChatter(vig4_sc2_6_comment42)
            $ narrator = reg_narrator
            "What? That's Elliot's username."
            "But he's supposed to be on a date with Cedric."
            $ AddChatter(vig4_sc2_6_comment43)
            ##Will handle all the fallout that comes from Elliot entering chat in the targets script
            $ narrator = alt_narrator
            "We step outside into the cool night."
            hide vega with dissolve
            hide coil with dissolve
            hide mac with dissolve
    jump vig4_sc3_1

label vig4_sc3_1():
    show vig1_town_stream at topleft onlayer background with dissolve
    hide warehouse_stream
    $ renpy.music.set_volume(1.0, 1.0)
    "Polaris's Star Shower festival is in full swing."
    "The plaza glows with lantern light, the sounds of raucous revelry filling the air."   
    "People sit at tables, happily drinking and eating. Some are playing games. Other sit on rooftops, already staring up at the sky."
    "I stand on the periphery, silently watching as MAC roves from group to group, introducing himself to new people."
    "Maybe, making new friends."
    vS "Hey, Moze."
    show vega stream neutral at stream_center with dissolve
    $ AddChatter(vig4_sc3_1_comment1)
    vS "Having a good time?"
    $ AddChatter(vig4_sc3_1_comment2)
    menu:
        vS "Having a good time?"
        "It's beautiful.":
            "I gesture to my empty holster."
            mS "Feels good to be able to put our guns down for once."
            mS "It's a beautiful festival."
            vS "It is nice. But that wasn't my question."
        "I don't know how to respond to that.":
            "I gesture to my empty holster."
            mS "Feels good to be able to put our guns down for once."
            mS "But I'll be honest, Vega. I don't know how to respond to that question."
            mS "I'm concerned."
            vS "About MAC?"
            mS "About a lot of things."
    vS "I know you're worried about what's next for MAC. You have every right to be."
    vS "But it's a festival! When was the last time you celebrated something?"
    $ AddChatter(vig4_sc3_1_comment3)
    mS "I don't know."
    vS "Then we should change that."
    vS "Come on, have some fun with the people who matter most!"
    $ AddChatter(vig4_sc3_1_comment4)
    "Maybe Vega's right. Even on Akar, we weren't really able to let our guard down."
    $ AddChatter(vig4_sc3_1_comment5)
    "I scan the festival for my crew."
    show mac stream neutral at stream_left_mac with dissolve
    "MAC is occupied with a group of children. It looks like they're playing tag."
    "I should let him enjoy that moment."
    hide mac with dissolve
    show teresa stream neutral at stream_right with dissolve
    "Teresa is sitting at a table where people are talking animatedly. Knowing her, it's some sort of gambling racket."
    $ AddChatter(vig4_sc3_1_comment7)
    show jennica stream neutral at stream_left with dissolve
    "Jennica is inside a building on the outskirts of the plaza. It looks like she's watching a screen intently."
    $ AddChatter(vig4_sc3_1_comment6)
    pause 0.5
    $ AddChatter(vig4_sc3_1_comment10)
    "Who should I go to?"
    if romanceAma == True:
        $ AddChatter(vig4_sc3_1_comment9)
    else:
        $ AddChatter(vig4_sc3_1_comment8)
    menu:
        "Who should I go to?"
        "Jennica.":
            jump vig4_sc3_2_jennica
        "Teresa.":
            jump vig4_sc3_2_teresa
        "Vega.":
            jump vig4_sc3_2_vega
    #Could have someone in chat bring up how there's no Allistar romance option cause he's dead

label vig4_sc3_2_vega():
    hide jennica with dissolve
    hide teresa with dissolve
    $ vegaDate = True
    $ kcEngagement += 2 #Vega is effectively the "neutral" romance option with no viewer characters disliking it
    $ pdEngagement += 1
    $ csEngagement += 1
    $ AddChatter(vig4_sc3_2_vega_comment1)
    mS "Actually, I'd like to get to know you better. How about you show me around?"
    $ AddChatter(vig4_sc3_2_vega_comment2)
    pause 0.5
    $ AddChatter(vig4_sc3_2_vega_comment3)
    vS "Oh! I would love to!"
    $ AddChatter(vig4_sc3_2_vega_comment4)
    vS "I know just the thing!"
    "Vega turns  and takes off into the crowd."
    "I follow close behind, weaving around groups of people and trying not to step on kids as they careen through the plaza."
    vS "Here! Hope it's not too on the nose."
    $ AddChatter(vig4_sc3_1_comment11)
    "The stall in front of us has four toy rifles laying on a counter."
    "A group of four teens in front of us pick them up, aiming down range."
    "A wood display of Polaris stands about ten feet back."
    "The operator pushes a button and a series of cardboard cutouts begin cycling between the houses and hills."
    "Cardboard cutouts in the likeness of BigCorp enforcers, dropships, and tanks."
    "The four teens shout as they fire short sparks off in rapid succession at the targets."
    vS "What do you think? Up for a round, just you and me?"
    $ AddChatter(vig4_sc3_2_vega_comment5)
    menu:
        vS "What do you think? Up for a round, just you and me?"
        "You're on!":
            mS "You're on! But don't expect me to go easy on you."
            vS "I would feel disrespected if you did."
        "Seems a little unfair.":
            mS "Seems a little unfair for me. Gunfighting is part of my profession after all."
            vS "And you think we can't hold our own just cause we're a small town?"
            vS "I think you'll be in for a surprise."
    "The teens in front of us finish up and wander off."
    vS "Come on, grab a rifle. I want to see what you're made of."
    $ AddChatter(vig4_sc3_2_vega_comment6)
    "Vega grabs one of the guns and aims it down range."
    "The rifle is light in my hands. Almost too light for comfort."
    menu:
        "The rifle is light in my hands. Almost too light for comfort."
        "Inspect the sights.":
            $ vig4_checkSights = True
            "I check the sights quickly."
            "They're not perfect. I'll have to aim up and to the left for accurate shots."
        "Inspect the trigger.":
            $ vig4_checkTrigger = False
            "I lightly tap the trigger."
            "It has almost no resistance. There's no recoil. I can fire this very quickly."
    "Before I can do anything else, the operator pulls a lever and the targets start their cycle."
    "Vega gets the first shot off, knocking an enforcer down, but I quickly seat the rifle into my shoulder and go to work."
    "I knock down the next two targets, but then Vega hits one of the ships that appear above the town."
    $ AddChatter(vig4_sc3_2_vega_comment7)
    "She fires quickly, almost with reckless abandon and without thought for precision."
    if vig4_checkSights == True:
        "It means she makes mistakes. Mistakes that I can capitalize on."
        "I don't fire as quick, but I hit every shot I take."
    else:
        "But she's not faster than me, especially with this light trigger."
        "The sound of our rifles overlap each other as wooden targets slam down in rapid succession."
    $ AddChatter(vig4_sc3_2_vega_comment8)
    "The cycle of targets is winding down. I'm in the lead."
    "I risk a glance to my side."
    $ AddChatter(vig4_sc3_2_vega_comment9)
    "Vega is alert and focused. Sweat drips from her forehead. She really wants to win this."
    $ AddChatter(vig4_sc3_2_vega_comment10)
    $ AddChatter(vig4_sc3_2_vega_comment11)
    menu:
        "Vega is alert and focused. Sweat drips from her forehead. She really wants to win this."
        "Let Vega win.":
            $ csEngagement += 1
            $ kcEngagement += 1
            $ pdEngagement -= 1
            $ vig4_vegaVictory = True
            "As the final targets pop into position, I shift my aim just to the side."
            "My shots go wide as Vega's find their home."
        "Hit the final targets.":
            $ pdEngagement += 1
            $ cSEngagement -= 1
            $ vig4_vegaVictory = False
            "As the final targets pop into position, I aim true."
            "My shots hit the targets just before Vega's."
            $ AddChatter(vig4_sc3_2_vega_comment13)
    "The cycle stops as the game ends."
    if vig4_vegaVictory == True:
        "Vega wins by just one target."
        vS "Yes! Wow that was a close one."
        $ AddChatter(vig4_sc3_2_vega_comment12)
    else:
        "I win by five targets."
        $ AddChatter(vig4_sc3_2_vega_comment12)
        vS "Ahhh damn, if I just got those last ones I would have beat you."
    mS "Well done, it was an impressive showing!"
    vS "Thanks! That means a lot coming from you."
    "We put the toy rifles back on the counter and step aside as new players take their positions."
    jump vig4_sc3_2_vega_2

label vig4_sc3_2_vega_2():
    "We walk back toward the center of the plaza, but Vega stops at the periphery, looking over the crowd."
    "She isn't scanning for anything or anyone in particular. She's just taking it all in."
    "I picture the ready warrior I competed against in the carnival game."
    "Vega hasn't spent her whole life on Polaris." 
    $ AddChatter(vig4_sc3_2_vega_comment14)
    "She clearly has experience with the rest of the galaxy. And with the violence that goes with it."
    "Should I say something?"
    menu:    
        "Should I say something?"
        "Do you like living here?":
            $ csEngagement += 1
            $ kcEngagement += 1
            mS "Vega, do you like living on Polaris?"
            "She smiles, still keeping her gaze on the festival."
            vS "It has its charm."
            vS "Getting to work with Coil in peace and quiet has been a dream come true."
            $ AddChatter(vig4_sc3_2_vega_comment15)
            vS "Still, the nature of our job means I've been here, and only here, for fifteen years."
            vS "It's a long time to be in any one place."
            menu:
                vS "It's a long time to be in any one place."
                "I wouldn't know what that's like.":
                    mS "Sounds boring."
                    mS "I've been hopping from planet to planet since..."
                    $ AddChatter(vig4_sc3_2_vega_comment16)
                    "I try to remember the last time I spent longer than four months on any piece of land."
                    vS "Since?"
                    $ AddChatter(vig4_sc3_2_vega_comment17)
                    mS "I honestly can't remember."
                    vS "Sounds hard."
                    menu:
                        vS "Sounds hard."
                        "More than it used to be.":
                            mS "It's gotten harder than it used to be."
                            mS "But we can't change the hand we're dealt, just play it the best we can."
                            "Why am I saying her words?"
                            vS "That from some famous outlaw?"
                            mS "An old mentor."
                            "Vega nods."
                        "I wouldn't have it any other way.":
                            mS "Can't imagine living any other way."
                            mS "I'd rather have tough nights' sleep and excitement than monotonous stability."
                            vS "I don't know that those are mutually exclusive, but I'm glad you've found the life that's right for you."
                "At least there's some kind of stability.":
                    mS "Hopping from planet to planet all the time...it gets tough."
                    $ AddChatter(vig4_sc3_2_vega_comment16)
                    mS "You've been able to build something here. That's harder to do up there."
                    vS "I'm grateful you can recognize that."
                    $ AddChatter(vig4_sc3_2_vega_comment17)
                    vS "Coil did most of the work to start. I try to help where I can."
                    "Vega looks up at the night sky. It's flooded with twinkling starlight."
                    vS "But I can't help it. I want to be doing more."
        "Have you killed anyone before?":
            $ kcEngagement += 1
            $ pdEngagement += 1
            mS "This question might be out of the ordinary, but I'm curious about something."
            vS "Please, fire away."
            mS "Have you ever killed anyone before."
            "Vega looks at me, her eyebrows raised in shock. Then she breaks into laughter."
            $ AddChatter(vig4_sc3_2_vega_comment18)
            vS "So direct! An outlaw's priority I take it."
            "She steadies herself and shrugs."
            $ AddChatter(vig4_sc3_2_vega_comment19)
            vS "I have, yeah. I'm not proud of it."
            mS "With the Dragonflies?"
            $ AddChatter(vig4_sc3_2_vega_comment20)
            vS "No. It was before we got in contact with them."
            vS "The first time was on a BC-controlled world." 
            vS "Coil got ID'd by some mercs who thought turning him in would get them some favors."
            vS "Turns out they put all their attention on the old man and not the little girl who was with him."
            "Vega looks up at the night sky. It's flooded with twinkling starlight."
            $ AddChatter(vig4_sc3_2_vega_comment21)
            vS "I think it's why the old man wanted to get us here so bad. So he could protect me from that life."
            menu:
                vS "I think it's why the old man wanted to get us here so bad. So he could protect me from that life."
                "Is it something you want to leave behind?":
                    $ AddChatter(vig4_sc3_2_vega_comment22)
                    mS "Is it something you want to leave behind?"
                    $ AddChatter(vig4_sc3_2_vega_comment23)
                    vS "The killing? Yes, I'm glad that's in the past."
                    vS "The adventure? Less so."
                    $ AddChatter(vig4_sc3_2_vega_comment24)
                    "Vega points a finger at me like it's a gun."
                    vS "But don't worry, as you witnessed, I've kept my aim sharp these past years."
                    "She moves her hand as if firing a gun."
                    menu:
                        "She moves her hand as if firing a gun."
                        "Don't react.":
                            $ pdEngagement += 1
                            $ kcEngagement -= 1
                            mS "You missed."
                            "Vega shrugs."
                            vS "How do you know? Maybe it's a boomerang bullet."
                            vS "It could be coming back around for you any second."
                        "Act like you get hit.":
                            $ kcEngagement += 1
                            "I place a hand to my chest and lean my head back."
                            mS "Ughhhh, right in the heart."
                            vS "Like I told you. Sharp."
                "Finding peace is hard.":
                    $ csEngagement += 1
                    mS "It's hard to find a place where you can leave that behind."
                    vS "True, it's why I'm grateful we're here. Even if it can get boring."
        "Don't say anything.":
            "I turn my attention to the crowd as well."
            "The twinkling lanterns, the laughter of the crowd, the smiling faces."
            "It all feels so...peaceful."
    vS "Thanks for playing the game with me, Moze."
    vS "It meant a lot to fight alongside the captain of the Oakley, even if it was just pretend."
    $ AddChatter(vig4_sc3_2_vega_comment25)
    ##* Streamer reaction to muse about what Moze's nickname would be
    menu:
        vS "It meant a lot to fight alongside the captain of the Oakley, even if it was just pretend."
        "I enjoyed it too.":
            mS "I appreciate that. And I enjoyed fighting alongside a Dragonfly."
            "Vega smiles and blushes."
        "Think about joining us?":
            $ kcEngagement += 1
            $ pdEngagement += 1
            $ csEngagement += 1
            mS "What do you think about joining us? The Oakley always has room for a sharp new recruit."
            $ AddChatter(vig4_sc3_2_vega_comment26)
            "Vega's eyes go wide for an instant."
            vS "Bahahaha!"
            "Then she doubles over, laughing."
            vS "Sorry, sorry, it just took me a second to realize that you're serious."
            "She glances back at the heart of the festival."
            vS "You know, if I was younger, I would have said 'yes' in a heartbeat."
            vS "I'm flattered. Deeply. But I'm going to have to politely decline."
            $ AddChatter(vig4_sc3_2_vega_comment27)
            vS "My place is with Coil and the Dragonflies. I'm sure you understand."
            mS "Of course. Figured I'd extend the invite."
            $ AddChatter(vig4_sc3_2_vega_comment28)
            vS "And it is very much appreciated."
    vS "You should probably go check in with your crew, Coil might have news."
    mS "I was just thinking the same thing."
    vS "Take care, Captain Moze."
    mS "Take care, Vega."
    hide vega with dissolve
    "Vega steps away and into the crowded plaza as I survey the area in front of me."
    jump vig4_sc3_3

label vig4_sc3_2_jennica():
    $ jennicaDate = True
    $ csEngagement += 2
    $ pdEngagement -= 1
    $ kcEngagement -= 1
    hide vega with dissolve
    hide teresa stream neutral with dissolve
    show jennica stream neutral at stream_center with move
    $ AddChatter(vig4_sc3_2_jenn_comment1)
    "Crossing the plaza, I step up next to Jennica."
    $ AddChatter(vig4_sc3_2_jenn_comment2)
    pause 0.5
    $ AddChatter(vig4_sc3_2_jenn_comment3)
    "She doesn't even notice me. Her eyes are glued to watching a screen in front of her."
    "It's an arcade game where two spaceships dogfight with one another."
    "There are two controllers connected to the game."
    $ AddChatter(vig4_sc3_1_comment11)
    "She's completely absorbed by the game, even though she isn't playing it."
    menu:
        "She's completely absorbed by the game, even though she isn't playing it."
        "Tap her on the shoulder.":
            "I tap her on the shoulder."
            "She snaps around immediately."
            pS "Oh jeez! Hi Cap, it's good to see you. How--how is your night faring?"
        "Clear throat.":
            mS "Uhem."
            "As I clear my throat, Jennica snaps to attention."
            pS "Oh, sir! I mean, Cap! You're look--How is your night faring, Moz--Cap?"
    mS "You ok, Jenn? You're looking a bit obsessed with that screen."
    pS "Yeah, I'm fine, Cap. It's just--"
    pS "You wouldn't happen to recognize this game, would you?"
    menu:
        pS "You wouldn't happen to recognize this game, would you?"
        "I've never played a video game before.":
            $ pdEngagement += 1
            mS "Jenn, you know I've never touched one of these things before."
            pS "Right. But this one's special."
            pS "This is {i}Star Battler IV: Destructostar{i}."
        "Of course!":
            $ kcEngagement += 1
            mS "Of course I recognize it. It's {i}Star Battler IV: Destructostar{i}."
            pS "Exactly! Wow, I'm a little surprised you knew that, Cap."
    pS "It's an old school arcade classic. There was one in my hometown when I was a kid."
    pS "No joke, this game taught me how to be a pilot."
    pS "Never thought I'd see it again."
    menu:
        pS "Never thought I'd see it again."
        "Alright, let's do this.":
            mS "Alright then, grab that controller and let's do this."
            "I step up to the game and grab the controller on the right."
    pS "Cap, you can't be serious."
    pS "I've spent hundreds of hours on this game. Plus, I'm a {i}professional{/i} starship pilot."
    menu:
        pS "I've spent hundreds of hours on this game. Plus, I'm a {i}professional{/i} starship pilot."
        "Sounds like an excuse.":
            mS "Is that the excuse you're gonna tell yourself after I beat you at this game."
            pS "Oh that's it."
            pS "I was gonna go easy on you, but you asked for some tough love."
        "You're forgetting I used to be a pilot too.":
            mS "Sure, but you're forgetting that I was a pilot before I was a captain."
            mS "Grab your flight stick and let's make this happen."
            pS "Alright, your funeral."
    mS "Bring it, Brown."
    pS "It's already brought, Cap."
    show jennica stream neutral at stream_left with move
    "We press the start button on our respective controllers."
    "The screen fades into a field of stars."
    "Narration describes the \"Destructostar\" tournament, a battle across the galaxy to discover the number one starship pilot."
    "Then the game begins."
    "I have to destroy Jennica's ship before she destroys mine."
    "My ship is equipped with photon cannons, heavy missiles, and blast wave charges."
    "Should be simple enough."
    pS "You're taking too long to remember the controls, Cap."
    "The radar on the side of the screen shows a blip barreling down at me. Jennica is playing this aggressively."
    menu:
        "The radar on the side of the screen shows a blip barreling down at me. Jennica is playing this aggressively."
        "Dodge the incoming attack.":
            "It's a bad spot, I have to pull away and find a better position to return fire."
            pS "On your ass, Cap."
            "Jennica is still putting pressure on me."
            menu:
                "Jennica is still putting pressure on me."
                "Drop a blast charge.":
                    mS "Don't get too close."
                    "I drop a blast wave charge, detonating it behind my ship."
                    pS "Shit!"
                    "Jennica has to peel off from the pursuit."
                    "I pull up and see Jennica moving away."
                    menu:
                        "I pull up and see Jennica moving away."
                        "Make an aggressive attack.":
                            $ kcEngagement -= 1 #could have KitCat "backseat gaming" cause she played the Jennica romance route
                            $ csEngagement -= 1
                            "Pressing my advantage, I drive my ship onto her tail as she drops into a barrel roll."
                            pS "Damn, Cap, looks like you got me."
                            mS "Only a matter of time."
                            pS "Too bad looks can be deceiving."
                            "As the words escape her mouth, I see it out of the corner of my eye."
                            "Delayed blast charges. They're all around my ship."
                            mS "Oh god damn it."
                            "Jennica pushes a button on the side of her controller."
                            "The charges around me detonate and my screen goes completely white."
                            "\"Player One Wins\" flashes across both game screens."
                            pS "Ooooh yeah! Just how I drew it up!"
                            pS "You made me sweat there a bit. But I felt locked in that whole time."
                            mS "You're one hell of a pilot, Jenn."
                            "I extend my hand toward her."
                            "She shakes it firmly."
                            pS "Thanks, Cap. It was a good game."
                            mS "It was. Well played."
                        "Get ahead and set a trap.":
                            $ kcEngagement += 1
                            $ csEngagement += 2
                            $ pilotApproval += 1
                            "I push my ship forward, trying to get ahead of Jennica."
                            pS "Oh no, I see what you're going for."
                            "She starts performing various maneuvers, but every time she tries to make a move, she just makes it easier for me to overtake her."
                            "I see my chance."
                            "I activate the extra boost on my ship, and thrust ahead of her ship, letting a blast charge slip just as I do so."
                            pS "Shit!"
                            "The charge falls alongside Jennica's ship, then detonates."
                            "Her screen goes completely white."
                            "\"Player Two Wins\" flashes across both game screens."
                            pS "Ahhh no way!"
                            pS "I had the time delay blast charges too."
                            pS "I just needed you to get a bit more greedy."
                            mS "And I just needed you to wear yourself out."
                            "Jennica lets out a sigh."
                            pS "Yeah, I guess I got a little too cute at the end there."
                            "She extends a hand toward me."
                            pS "Well played."
                            "I shake it firmly."
                            mS "Good game."
                "Evasive maneuvers.":
                    "I corkscrew around a handful of asteroids."
                    pS "Pretty good moves, Cap."
                    mS "I learned from the best."
                    "Peeling up out of the corkscrew, Jennica and I are heading directly toward each other."
                    menu:
                        "Peeling up out of the corkscrew, Jennica and I are heading directly toward each other."
                        "Head on attack.":
                            $ csEngagement += 2
                            $ pdEngagement += 1
                            $ kcEngagement -= 2
                            $ pilotApproval += 1
                            "Pushing my thrusters full throttle, I lay on the guns."
                            pS "Oh so we're doing it this way?"
                            mS "You know it!"
                            "Jennica lays on her throttle too."
                            "Our shields are ripped to shreds. It's just our hulls, hurtling toward one another."
                            "The ships collide. The screen goes white."
                            "\"Tie Game\" flashes across both game screens."
                            pS "Hahaha, I guess that's an appropriate way for it to go."
                            "Jennica reaches out a hand to me."
                            "I take it and shake it firmly."
                            mS "Good game."
                            pS "Yeah, well played."
                        "Bait her in.":
                            $ kcEngagement -= 1
                            $ csEngagement -= 1
                            "I turn my ship around and try to bait her in."
                            pS "Running scared, Cap?"
                            mS "Just waiting for my moment."
                            pS "Spoken like someone who's scared."
                            "She executes the maneuver before I realize what's happening."
                            "Jennica drops a blast wave charge, and then jams her ship's steering hard so that the ship spins in a perfect circle."
                            "All I can do is watch as her ship's back end slams into the charge, sending it flying through the void of space."
                            "Directly at me."
                            "The charge detonates, and my screen goes completely white."
                            "\"Player One Wins\" flashes across both game screens."
                            pS "Ooooh yeah! Just how I drew it up!"
                            mS "Damn! You're one hell of a pilot, Jenn."
                            "I extend my hand toward her."
                            "She shakes it firmly."
                            pS "You're not so bad yourself. Maybe you should take the helm next time we're in a tight spot."
                            mS "Think I'll stick to the games for now."
                            pS "Hahaha alright. It was a good game."
                            mS "It was. Well played."
        "Return fire.":
            "It's a bad spot, but I pull up and face her directly."
            "Her shots shred my shields, but I manage to land some hits on her too."
            pS "Bold move, not afraid to take some hits, I see."
            "My shields are low, but she's taken some hits too. I'm at a disadvantageous position."
            menu:
                "My shields are low, but she's taken some hits too. I'm at a disadvantageous position."
                "Head on attack.":
                    $ csEngagement += 2
                    $ pdEngagement += 1
                    $ kcEngagement -= 2
                    $ pilotApproval += 1
                    "Pushing my thrusters full throttle, I lay on the guns."
                    pS "Oh so we're doing it this way?"
                    mS "You know it!"
                    "Jennica lays on her throttle too."
                    "Our shields are ripped to shreds. It's just our hulls, hurtling toward one another."
                    "The ships collide. The screen goes white."
                    "\"Tie Game\" flashes across both game screens."
                    pS "Hahaha, I guess that's an appropriate way for it to go."
                    "Jennica reaches out a hand to me."
                    "I take it and shake it firmly."
                    mS "Good game."
                    pS "Yeah, well played."
                "Bait her in.":
                    $ kcEngagement -= 1
                    $ csEngagement -= 1
                    "I turn my ship around and try to bait her in."
                    pS "Running scared, Cap?"
                    mS "Just waiting for my moment."
                    pS "Spoken like someone who's scared."
                    "She executes the maneuver before I realize what's happening."
                    "Jennica drops a blast wave charge, and then jams her ship's steering hard so that the ship spins in a perfect circle."
                    "All I can do is watch as her ship's back end slams into the charge, sending it flying through the void of space."
                    "Directly at me."
                    "The charge detonates, and my screen goes completely white."
                    "\"Player One Wins\" flashes across both game screens."
                    pS "Ooooh yeah! Just how I drew it up!"
                    mS "Like I say back on the Oakley: you're one hell of a pilot, Jenn."
                    "I extend my hand toward her."
                    "She shakes it firmly."
                    pS "You're not so bad yourself. Maybe you should take the helm next time we're in a tight spot."
                    pS "Maybe you should take the helm next time we're in a tight spot."
                    mS "Think I'll stick to the games for now."
                    pS "Hahaha alright. It was a good game."
                    mS "It was. Well played."
    jump vig4_sc3_2_jennica_2

label vig4_sc3_2_jennica_2():
    "The screen goes back to its repetitive trailer montage as we step back into the plaza."
    pS "Wow, that was a trip down memory lane. I need a second to catch my breath."
    "Jennica steps to the side of the store and leans back against the wall."
    "We're both quiet for sometime."
    pS "Did I ever tell you what made me want to become a pilot?"
    menu:
        pS "Did I ever tell you what made me want to become a pilot?"
        "I don't think so.":
            mS "I don't think it ever came up, actually."
        "To get off of your home world, right?":
            mS "I think so."
            mS "It was to get off your home world, right?"
            pS "That was part of it."
            pS "But I meant like, the specific {i}thing{/i} that inspired me."
    pS "The thing that really sealed it was this guy who came to my school when I was a young teen."
    pS "He was some pilot for BigCorp, doing a mentorship program type thing. I think he was a cop."
    pS "He came into my class and asked who wanted to be a pilot. So I raised my hand."
    "Jennica looks up toward the plaza. It's like she's looking at something much further away."
    pS "He took one look at me and laughed."
    pS "I didn't have the implants in at the time. So he just saw this scrawny kid with degenerative eyesight."
    pS "I'll never forget what he said. \"Not one in a billion chance you could ever be a pilot.\""
    "Jennica clenches her fist."
    pS "I made it. It wasn't handed to me, it didn't just happen. I worked my ass off."
    pS "And I'm a damn good pilot now. His words shouldn't matter."
    pS "But whenever I remember what he said, all I want to do is go back in time and kick that guy's ass."
    "Jennica's whole body relaxes."
    "She looks to me and our eyes lock."
    menu:
        "She looks to me and our eyes lock."
        "You're so incredible, Jenn.":
            mS "Jenn, you're so incredible."
            "She blushes and looks away briefly before turning back to me."
            pS "Thanks, Cap."
            mS "No I really mean it. You've achieved amazing things. There's no one I could possibly trust more at the helm of the Oakley."
            if pilotApproval > 5:
                "Jennica slides a bit closer to me."
            pS "Good, cause there's no one I would want watching my back more than you."
            menu:
                pS "Good, cause there's no one I would want watching my back more than you."
                "Jenn, I love you." if teresaRomance == False:
                    mS "Jenn, it's taken me a long time to realize this. Probably too long."
                    pS "Realize what, Cap?"
                    mS "I love you."
                    if pilotApproval > 5:
                        $ kcEngagement -= 2
                        $ csEngagement += 3
                        $ pdEngagement -= 1
                        $ jennicaRomance = True
                        pS "Oh!"
                        "Jennica's face goes entirely red."
                        pS "Wow, I, uh, wasn't expecting that."
                        mS "In a bad way?"
                        pS "Nononono, in a good way. Honestly, in the best possible way."
                        pS "I uh, I think that--why is this so hard!?"
                        menu:
                            pS "I uh, I think that--why is this so hard!?"
                            "Kiss her":
                                "I put a finger to her lips."
                                mS "Shhhh"
                                mS "You don't have to say it."
                                "She freezes completely still, her eyes locked on mine."
                                "I move forward and kiss Jennica."
                                "Our arms wrap around each other, holding one another tightly."
                                "It feels good. To hold and be held. Like we could stay here for hours, days, longer even."
                                "Finally, our lips part. We stare into each other's eyes."
                                pS "Now the problem is I don't want to let go."
                                mS "Me neither."
                                mS "But I should go check and see if Coil has any news."
                                mS "We'll have more time."
                                pS "Yes, lots of time."
                                "It's hard to let go, but somewhow we manage."
                                "I take a step toward the plaza and sneak a glance back at Jennica."
                                "She's leaning against the wall, looking up at the stars, with a massive smile on her face."
                                "I smile to myself as I return to the festival."
                                hide jennica with dissolve
                            "Wait for her":
                                "I wait, patiently."
                                "Jennica meets my eyes."
                                "We hold each other's gaze."
                                pS "I love you too, Moze."
                                "I feel myself smiling before I even consciously do it myself."
                                "I move forward and kiss Jennica."
                                "Our arms wrap around each other, holding one another tightly."
                                "It feels good. To hold and be held. Like we could stay here for hours, days, longer even."
                                "Finally, our lips part. We stare into each other's eyes."
                                pS "Now the problem is I don't want to let go."
                                mS "Me neither."
                                mS "But I should go check and see if Coil has any news."
                                mS "We'll have more time."
                                pS "Yes, lots of time."
                                "It's hard to let go, but somewhow we manage."
                                "I take a step toward the plaza and sneak a glance back at Jennica."
                                "She's leaning against the wall, looking up at the stars, with a massive smile on her face."
                                "I smile to myself as I return to the festival."
                                hide jennica with dissolve
                    else:
                        $ kcEngagement += 1
                        $ csEngagement -= 1
                        $ pdEngagement += 1
                        pS "Oh, that's not what I was expecting."
                        "My heart drops."
                        mS "What do you mean?"
                        "Jennica looks at the ground, then back up to me."
                        pS "I don't really know how to respond."
                        mS "So, you don't feel the same?"
                        "Jennica takes a long moment. She looks deeply into my eyes."
                        pS "I'm sorry. But I don't."
                        pS "For me, you've always felt like a big sister."
                        mS "Okay..."
                        pS "..."
                        mS "..."
                        pS "..."
                        mS "Well this is awkward."
                        pS "Yeah."
                        pS "Look I really care about you, Cap."
                        pS "But it doesn't feel right to me."
                        mS "No, I get it. I'm glad you were honest with me."
                        pS "Always."
                        mS "I should check on the party. Maybe Coil has some updates."
                        pS "Of course. Let me know as soon as you hear anything from him."
                        mS "Will do."
                        "The two of us hug, awkwardly, then I step away back to the center of the plaza."
                        hide jennica with dissolve
                "Let's get back to the party":
                    $ csEngagement -= 2
                    $ pdEngagement -= 1 #PickledDragons probably doesn't respect starting to go for the romance and then backing out
                    mS "I should check on the party. Maybe Coil has some updates."
                    "Jennica freezes for a moment."
                    "Then she stands up from the wall."
                    pS "Yeah, of course, that makes sense."
                    "I step back toward the plaza when Jennica calls me back."
                    pS "Hey, Cap, thanks for the game. I think I really needed it."
                    mS "No problem, Jenn."
                    "The two of us hug, then I step away back to the center of the plaza."
                    hide jennica with dissolve
        "Screw that guy.":
            $ csEngagement -= 2
            $ kcEngagement += 1
            mS "Screw that guy. He's probably dead now anyway."
            pS "Bahahaha"
            pS "Yeah, probably blew up in an asteroid belt crash or something."
            pS "Asshole."
            pS "Thanks, Cap. I needed this."
            mS "No problem, Jenn."
            "The two of us hug, then I step away back to the center of the plaza."
            hide jennica with dissolve
    jump vig4_sc3_3

label vig4_sc3_2_teresa():
    $ teresaDate = True
    $ kcEngagement += 2
    $ pdEngagement += 1
    $ csEngagement -= 1
    hide vega with dissolve
    hide jennica with dissolve
    show teresa stream neutral at stream_center with move
    $ AddChatter(vig4_sc3_2_resa_comment1)
    "I wind my way through the crowd to stand next to Teresa."
    $ AddChatter(vig4_sc3_2_resa_comment2)
    pause 0.5
    $ AddChatter(vig4_sc3_2_resa_comment3)
    "She and three other people are watching each other intently, holding cups upside down on the table."
    "The one sitting on Teresa's left throws a scrunched up bill on the table and stands up."
    $ AddChatter(vig4_sc3_1_comment11)
    townguy "Damn it!"
    show teresa stream happy
    "Teresa shrugs."
    enS "You should've called."
    townguy "Apparently. Alright, I'm out. Getting too rich for my blood."
    "As the man leaves, Teresa glances up at me."
    enS "Oh Captain, perfect timing! Want to join for a game?"
    mS "Sure."
    "I take a seat."
    mS "But I don't really know what's going on here."
    enS "It's called Liar's Dice."
    enS "We all have five dice that we roll underneath our cups. We can look at our own cups at any time."
    enS "Then, one person identifies how many of one number they think are under all the cups."
    enS "The next person can increase the number, or \"call\" to make everyone reveal their dice."
    enS "We tally up all the dice of that one number, and if there are fewer than the amount that was called, then the person who called wins."
    enS "You'll pick it up as you go."
    enS "First, take all those dice, jumble them up in a cup, and then slam it back on the table."
    "The wooden cup makes a deep \"thunk\" as the dice rattle around underneath."
    "I look under my cup: There are two 2's, two 4's, and one 6."
    "The person opposite me starts."
    diceP1 "three 4's."
    diceP2 "Only three, come on Alex, that's not even a real bet!"
    diceP1 "She's running the table with us, Adam, what do want me to do?"
    diceP2 "Not let her get in your head man."
    "Teresa glances at me and grins."
    diceP2 "You know what, let's make this interesting, six 4's."
    enS "You're turn, Captain. What'll it be? Call or Raise?"
    menu:
        "I look under my cup: There are two 2's, two 4's, and one 6."
        "Call.":
            mS "Why not. I'll call."
            "Each player at the table raises their cup."
            "I have two 4's. The first player also has two. The one next to me has one."
            "But Teresa, has four."
            enS "Nine 4's. Tough, Captain. We could've gone a bit longer."
            "I toss a small stack of credits onto the table. The man next to me picks them up."
            mS "I'm just warming up."
            diceP1 "Of course."
            diceP2 "That's what we said when your friend first sat down here."
            "Teresa winks at me."
            enS "You'll get it."
        "Raise.":
            mS "Seven 4's."
            enS "Eight 4's."
            "Teresa didn't even check under her cup."
            "The man who started the bidding looks under his cup."
            "It seems like sweat is starting to form on his brow."
            diceP1 "Call!"
            "We all lift our cups."
            "I have two 4's. The first player also has two. The one next to me has one."
            "But Teresa has four."
            enS "Nine 4's. Tough position, reasonable call."
            diceP1 "Yeah yeah."
            "The losing player takes out a small stack of credits and puts them on the table."
            "Teresa gleefully picks them up."
    enS "Alright, next round. I start."
    "We sit at the table for several more rounds."
    "The back and forth continues as I start to get a handle on the game."
    "I win some, I lose some."
    "Then Teresa picks up her cup with a bit more of a flourish."
    enS "Alright gang, I think this is my last round."
    diceP1 "Me too."
    diceP2 "Same."
    mS "Winner take all then?"
    "I make eye contact with Teresa."
    mS "At least in terms of pride."
    enS "Why don't we switch up the direction. Give Captain the chance to call on me before the end."
    "We all nod in agreement, and throw our dice."
    "I check under my cup: one 1, one 3, one 4, one 5, and one 6."
    "Teresa starts."
    enS "Four 2's."
    enS "Captain?"
    menu:
        "I check under my cup: one 1, one 3, one 4, one 5, and one 6."
        "Call.":
            $ kcEngagement -= 1
            $ csEngagement -= 1
            mS "Why not, let's call it."
            "We all lift our cups."
            "Teresa has five 2's."
            show teresa stream shock
            "No one else has any."
            "But she has enough to just make it."
            mS "You're kidding!?"
            enS "Wow! That was closer than I thought it'd be."
            show teresa stream neutral
        "Raise.":
            "Teresa wouldn't make that number if she didn't have a good hand for it."
            mS "Five 2's."
            diceP2 "Six 2's."
            diceP1 "Ahhhhh, seven 2's."
            "Teresa's smile is broad."
            enS "Fun. Eight 2's."
            enS "Captain?"
            menu:
                "I check under my cup: one 1, one 3, one 4, one 5, and one 6."
                "Call.":
                    $ kcEngagement += 2
                    $ pdEngagement += 1
                    mS "Bullshit, I call."
                    "We all lift our cups."
                    "Teresa has five 2's."
                    show teresa stream shock
                    "No one else has any."
                    "Teresa loses."
                    enS "No one has any other 2's!?"
                    diceP2 "Yes!"
                    diceP1 "Ooooh wow, so she could've called me."
                    mS "Tough luck."
                    "I extend a hand toward Teresa."
                    "Without taking her eyes off the exposed dice, she places a handful of credits in my palm."
                    mS "Well-played."
                    diceP2 "Thank you kindly."
                    "The two players get up from the table and wander off into the plaza."
                    "Teresa continues to stare at the uncovered dice on the table."
                    enS "But that's mathematically improbable."
                    menu:
                        enS "But that's mathematically improbable."
                        "You lost, get over it.":
                            mS "Losses happen Teresa."
                            mS "You can't win everything."
                            show teresa stream neutral
                            enS "I know, I just thought I had more control over that situation than I did."
                            mS "So what?"
                            mS "We've been in those kinds of situations before. Hell, I can think of ten in the last two weeks."
                            mS "It doesn't help to dwell on things that are out of our control."
                            enS "Yeah, you're right."
                            enS "Guess I went back to being \"Dr.\" Prismari there for a little bit."
                        "Probability isn't certainty.":
                            $ engineerApproval += 1
                            mS "Probabilities are certainties."
                            mS "Anything can happen."
                            mS "And sometimes, a lot of times, luck is more important than skill."
                            mS "You should know that in our line of work."
                            show teresa stream neutral
                            enS "Yeah, you're right."
                            enS "Guess I went back to being \"Dr.\" Prismari there for a little bit."
                "Raise.":
                    $ kcEngagement -=1
                    $ pdEngagement -=1
                    mS "Why not? Ten 2's."
                    diceP2 "Nope, gotta call that."
                    "We all lift our cups."
                    "Teresa has five 2's."
                    show teresa stream shock
                    "No one else has any."
                    "I lose."
                    enS "No one has any other 2's!"
                    mS "Damn."
                    "I toss some credits to the player on my right."
                    mS "Well-played."
                    diceP2 "Thank you kindly."
                    "The two players get up from the table and wander off into the plaza."
                    "Teresa stares at the uncovered dice on the table."
                    enS "But that's mathematically improbable."
                    menu:
                        enS "But that's mathematically improbable."
                        "Teresa, you won.":
                            mS "Teresa, you won. Why do you care?"
                            show teresa stream neutral
                            enS "My calculations were off. You should have got me."
                            mS "I didn't."
                            enS "But you should have."
                            mS "Sometimes luck is more important than skill."
                            mS "You should know that in our line of work."
                            enS "Yeah, you're right."
                            enS "Guess I went back to being \"Dr.\" Prismari there for a little bit."
                        "Probability isn't certainty.":
                            $ engineerApproval += 1
                            mS "Probabilities are certainties."
                            mS "Anything can happen."
                            mS "Sometimes, a lot of times, luck is more important than skill."
                            mS "You should know that in our line of work."
                            show teresa stream neutral
                            enS "Yeah, you're right."
                            enS "Guess I went back to being \"Dr.\" Prismari there for a little bit."
    jump vig4_sc3_2_teresa_2

label vig4_sc3_2_teresa_2():
    "Teresa continues to stare at the table."
    "She picks up a die and starts rotating it in her fingers."
    enS "Hey, Captain. Do you think I'm a good outlaw?"
    menu:
        enS "Hey, Captain. Do you think I'm a good outlaw?"
        "Of course!":
            mS "Of course! I'd trust you with my life."
            enS "I know that. But..."
        "Where is this coming from?":
            mS "Where is this coming from?"
    enS "Every now and then I look at you and Jennica, and it fits you so easily. This life I mean."
    enS "You've been living it for so long. You're {i}SnakeHawks{/i}."
    enS "I'm so grateful I met the two of you. You both changed my life, so much for the better."
    enS "But sometimes I wonder what could have been."
    enS "If I didn't go to grad school. If I didn't disobey my parents. If I went to Alliance space instead of The Outposts."
    enS "All these moments where I made decisions that could have legitimately gone another way."
    enS "But this is the reality that I ended up in, whether I'm happy about it or not."
    enS "Does that mean anything?"
    "Teresa looks up and locks eyes with me."
    menu:
        "Teresa looks up and locks eyes with me."
        "Don't be afraid to call this fate.":
            mS "Teresa, you can use the word fate. You don't have to be scared of it."
            enS "But if it is fate, then what does it mean?"
            if engineerApproval > 5:
                "Teresa gets closer to the edge of her seat. Closer to me."
            enS "Why did this moment have to happen?"
            "Her eyes do not leave mine."
            menu:
                "Her eyes do not leave mine."
                "Resa, I love you" if jennicaRomance == False:
                    mS "What else could it be, Resa: love."
                    enS "What?"
                    mS "I love you, Teresa."
                    if engineerApproval > 5:
                        $ csEngagement -= 2
                        $ kcEngagement += 3
                        $ pdEngagement -= 1
                        $ teresaRomance = True
                        "Teresa face is immediately bright red."
                        enS "What?"
                        enS "Oh, wow, this is really happening."
                        enS "Is it hot? Do you think it's hot right now?"
                        menu:
                            enS "Is it hot? Do you think it's hot right now?"
                            "Kiss her":
                                "I put a finger to her lips."
                                mS "Shhhh."
                                mS "You don't have to explain this."
                                "She freezes completely still, her eyes locked on mine."
                                "I move forward and kiss Teresa."
                                "Our arms wrap around each other, holding one another tightly."
                                "It feels good. To hold and be held. Like we could stay here for hours, days, longer even."
                                "Finally, our lips part. We stare into each other's eyes."
                                enS "Now the problem is I don't want to let go."
                                mS "Me neither."
                                mS "But I should go check and see if Coil has any news."
                                mS "We'll have more time."
                                enS "Yes, lots of time."
                                "It's hard to let go, but somewhow we manage."
                                "As I stand and take a step away from the table, I sneak a glance back at Teresa."
                                "She's still looking at the exposed dice, but now with a massive smile on her face."
                                "I smile to myself as I return to the festival."
                            "Wait for her":
                                "I wait, patiently."
                                "Teresa suddenly stops moving and meets my eyes."
                                "We hold each other's gaze."
                                enS "I love you too, Moze."
                                "I feel myself smiling before I even register to do it myself."
                                "I move forward and kiss Teresa."
                                "Our arms wrap around each other, holding one another tightly."
                                "It feels good. To hold and be held. Like we could stay here for hours, days, longer even."
                                "Finally, our lips part. We stare into each other's eyes."
                                enS "Now the problem is I don't want to let go."
                                mS "Me neither."
                                mS "But I should go check and see if Coil has any news."
                                mS "We'll have more time."
                                enS "Yes, lots of time."
                                "It's hard to let go, but somewhow we manage."
                                "As I stand and take a step away from the table, I sneak a glance back at Teresa."
                                "She's still looking at the exposed dice, but now with a massive smile on her face."
                                "I smile to myself as I return to the festival."
                    else:
                        $ kcEngagement -= 1
                        $ csEngagement += 1
                        $ pdEngagement += 1
                        enS "Oh! That's...not what I was expecting."
                        "My heart drops a little."
                        mS "What do you mean?"
                        "Teresa looks to the dice, then back to me."
                        "She sighs."
                        enS "I care a lot about you, Captain. And I deeply respect you as a leader."
                        enS "But I don't feel the same way."
                        enS "I'm sorry."
                        "She's still making eye contact with me. Unflinching. Fierce."
                        "Honest."
                        "I sigh."
                        mS "Of course. I'm glad you were honest with me."
                        enS "Always."
                        mS "I should--I should go find Coil, see if he's got any updates for us."
                        enS "Yeah, I hope it's good news."
                        mS "I'll let you and Jenn know as soon as I can."
                        enS "Sounds good. Take care."
                        mS "Yeah."
                        "I turn away from Teresa and back to the festival."            
                "I don't know":
                    $ kcEngagement -= 2
                    $ pdEngagement -= 1
                    mS "I don't think it's for me to say, Resa."
                    mS "That's something you have to figure out for yourself."
                    "Teresa sighs and hangs her head slightly."
                    enS "Yeah, that makes sense."
                    enS "It's irritating, but you're right."
                    mS "Alright, I need to go find Coil, see if he's got any updates for us."
                    enS "Yeah, I hope it's good news."
                    mS "I'll let you and Jenn know as soon as I can."
                    enS "Good."
                    enS "And thanks for the conversation, Captain. I really needed it."
                    "I turn away from Teresa and back to the festival."
        "Who cares about probabilities.":
            $ kcEngagement -= 2
            $ csEngagement += 1
            mS "All those alternate timelines you're imagining: screw 'em."
            mS "What matters is what you've decided."
            mS "You're an incredible outlaw, crew member, and friend."
            mS "I'm so grateful to have you on the Oakley. And I know Jenn feels the same way."
            show teresa stream happy
            "Teresa smiles and nods."
            enS "Yeah, you're right."
            enS "Thanks, Captain. I really needed to hear that."
            mS "Any time."
            mS "Alright, I need to go find Coil, see if he's got any updates for us."
            enS "Yeah, I hope it's good news."
            mS "I'll let you and Jenn know as soon as I can."
            enS "Good."
            "I turn away from Teresa and back to the festival."
    hide teresa with dissolve
    jump vig4_sc3_3

label vig4_sc3_3():
    "A crowd just to my left suddenly gets my attention."
    "There's a small semi-circle of people, their heads inclined downwards."
    show mac stream neutral at stream_center_mac with dissolve
    "They're all looking at MAC, as he waves his hands in the air."
    if macViolence >= macPeace and customsStampede == True:
        macS "So then Dr. Prismari begins the {i}conflagrant{/i} phase and the booth explodes!"
        macS "Everyone starts running wildly, and we sneak under security's nose!"
        "There are gasps throughout the crowd."
        townguy "My word, I hope everyone was ok."
        macS "We did not have time to check on people. We had to go meet a \"skeeve\" named Matticus."
    elif macPeace > macViolence and vig2_marshalEpilogue == True:
        macS "So then I said, \"take that skeeve\" and we took care of Reggie."
        macS "Captain Moze saved the aid ship and Sallent was saved!"
        "There are gasps throughout the crowd."
        townguy "My word, I heard that Sallent had survived Gray Fever, but I didn't know they were in such danger."
        macS "Indeed, Captain Moze is a hero."
    else:
        macS "So then I chased after the Hounds and got captured."
        macS "But not without a fight!"
        macS "Captain Moze found me, and together we fought our way out of BC's evil clutches!"
        "There are gasps throughout the crowd."
        townguy "My word, the Hounds sound dreadful!"
        macS "They were, but they're no match for the SnakeHawks!"
    hide mac with dissolve
    "I chuckle a bit to myself."
    cS "He has many more stories like that one."
    $ renpy.music.set_volume(0.4, 1.0)
    show coil stream neutral at stream_center with dissolve
    "Coil steps up next to me. His eyes remain on MAC."
    cS "I got a chance to speak with him a little earlier."
    if marshal > outlaw:
        cS "All he seems to talk about his how heroic you and your crew are."
        cS "How he wants to be as selfless as you."
    else:
        cS "He seems fascinated by how protective of your crew you are."
        cS "How you'll go to any lengths to ensure their safety."
    cS "Your influence on him has been immense."
    menu:
        cS "Your influence on him has been immense."
        "I wish it wasn't.":
            mS "I wish I didn't. He deserves better than the life of an outlaw."
            if outlaw > marshal:
                $ outlaw -= 1
            else:
                $ marshal += 1
            if marshal > outlaw:
                cS "I understand."
                cS "I wish that Vega could use her mind to make things other than tools for war."
                cS "But we do not get to determine the course of our children's lives."
                "Coil sighs."
            else:
                cS "To speak candidly, I wish that too."
                "I feel my body tense up instinctually."
                mS "What's that supposed to mean?"
                cS "Like I said, I'm enormously grateful to you for getting MAC to us."
                cS "But to hear how you went about it."
                cS "I wonder if it's worth the cost."
                menu:
                    cS "I wonder if it's worth the cost."
                    "I wonder the same thing.":
                        mS "Sometimes I wonder the same thing."
                        mS "But I don't have the luxury to second-guess my decisions."
                        cS "True. Perhaps I've forgotten how difficult life on the run can be."
                        "Coil sighs."
                    "You don't get to judge me.":
                        mS "You don't get to judge me while you sit in your hidden safehouse."
                        cS "Then who does, Moze?"
                        "Coil's eyes fall on me."
                        mS "I do what is necessary."
                        cS "And {i}that{/i} is what worries me."
                        "Coil sighs."
        "That's a good thing.":
            if outlaw > marshal:
                $ outlaw += 1
            else:
                $ marshal += 1
            mS "He was alone when we found him. Someone had to show him how to survive."
            cS "He has to know how to live as well."
            menu:
                cS "He has to know how to live as well."
                "We gave him a family.":
                    mS "We gave him a family."
                    mS "What's more important than that?"
                    cS "Little."
                    cS "But maturing is also understanding the bigger picture, extending empathy to more than your own family."
                    if marshal > outlaw:
                        cS "He can do that. And it's a testament to you that he understands this."
                    else:
                        cS "He seems to be obsessed with just his family."
                        cS "What does that say about you?"
                        "Coil sighs."
                "That's not my responsibility.":
                    mS "That wasn't my responsibility."
                    mS "I had to make sure he was safe."
                    cS "Yes, I suppose we did emphasize that was your only concern."
                    "Coil sighs."
    cS "I got in touch with the Dragonflies."
    cS "They won't allow you or your crew to transit with MAC."
    cS "And they want you to depart Polaris now."
    "I'm shocked into silence."
    if marshal > outlaw:
        cS "I tried my best to convince them otherwise, but they don't trust you."
    else:
        cS "I must say, I agree with them."
        cS "You're too dangerous to the people around you."
        cS "And you don't seem to recognize that."
        cS "Worse still, the people you love do not realize it either."
    cS "I'm sorry."
    menu:
        cS "I'm sorry."
        "Like hell this is happening!":
            $ kcEngagement += 1
            $ csEngagement -= 1
            $ pdEngagement += 1
            mS "Like hell, Coil!"
            mS "You think I'm going to let you rip my family apart like this!"
            cS "He's not \"your\" family."
            cS "I was there when he was conceived. Elijah and I created him together."
            cS "We are more family than you will ever be."
            mS "You don't even know him."
            cS "I knew Elijah. And I know you, Mozely."
            if marshal > outlaw:
                cS "I had hope you would understand."
            else:
                cS "You are dangerous. And you have to leave."
        "I understand.":
            $ csEngagement += 1
            $ kcEngagement -= 1
            $ pdEngagement -= 1
            "I take a deep breath and exhale slowly."
            "In my mind's eye I see MAC, hiding behind the console where his creator's dead body slumps."
            "Lost, confused, scared."
            "I see him talking with Allistar about music."
            "I see him calling Matticus a \"skeeve.\""
            "I see him now, as he goes somewhere I can't follow."
            mS "I understand."
            mS "Promise me you'll take care of him."
            cS "Of course. I promise you, he will be safe."
            mS "Good. That's all that matters."
    cS "I can give you some time to say goodbye."
    cS "I will alert your crew. You have fifteen minutes."
    "Coil turns and leaves."
    menu:
        "Coil turns and leaves."
        "Reach for your gun.":
            "Instinctively, I reach for my gun."
            "But it's not there."
            "They were taken at the start of the festival \"for safety.\""
            "Was this planned?"
            "I scan the plaza and notice a handful of people with stun rods."
            "Some of them are eyeing me."
            "Shit."
            hide coil with dissolve
            "I turn to look at MAC."
        "Turn to MAC.":
            hide coil with dissolve
            "With a heavy sigh, I turn to look at MAC."
    "The crowd around him is dissipating."
    jump vig4_sc3_4

label vig4_sc3_4():
    show mac stream neutral at stream_center_mac with dissolve
    play music "soundtrack/theme.wav"
    "MAC notices me almost as soon as I turn toward him."
    macS "Moze! Isn't this wonderful!"
    mS "MAC, we should talk."
    macS "Of course, that would be lovely. Shall we take a walk around the plaza?"
    "The two of us head to the outskirts of the plaza."
    "Every step feels heavy. As if my boots are filled with lead."
    menu:
        "Every step feels heavy. As if my boots are filled with lead."
        "I can't bring myself to say anthing.":
            "We're supposed to talk. But I can't bring myself to say anthing."
            "We move around the plaza, cries of joy echoing behind us."
            macS "This is an interesting place."
        "How does MAC feel about Polaris?":
            mS "So, MAC, what do you think of Polaris?"
            "There's a brief hum from MAC, as if considering his response."
            macS "It is an interesting place."
    macS "It does not appear like any other planet we have visited."
    macS "No one has tried to kill our crew or steal from us."
    macS "The people here seem...what's the right word? Is it \"happy?\""
    "I look over my shoulder. Even from a distance, the smiles on everyone's faces at the festival are apparent."
    #macS "They were all so interested in our adventures. I think I impressed them with our stories."
    #mS "I'm sure you impressed them yourself"
    macS "What do you think of this place, Captain?"
    menu:
        macS "What do you think of this place, Captain?"
        "It's an illusion.":
            $ macPessimism += 1
            mS "I think it's fake, MAC."
            mS "A bunch of people acting like they have a higher purpose, but they've forgotten what the galaxy is really like."
        "It's a haven.":
            $ macHope += 1
            mS "I think it's a haven, MAC."
            mS "Somewhere people can be genuinely happy, where they have a purpose."
    "MAC doesn't respond immediately."
    macS "Moze, do you know what our purpose is?"
    mS "To keep you safe. To get you here."
    macS "Yes, but that mission is accomplished."
    macS "What do we do now?"
    menu:
        macS "What do we do now?"
        "We help others.":
            $ csEngagement += 2
            $ macPeace += 3
            $ macHope += 2
            mS "I suppose our purpose is to leave the galaxy a better place than when we found it."
            macS "To help people?"
            mS "Yeah. That feels right."
            macS "Did we help people?"
            menu:
                macS "Did we help people?"
                "I don't know.":
                    mS "I don't know MAC. Things are rarely that cut and dry."
                    macS "Yes, I have noticed a distinct lack of clarity in answers to my questions."
                    mS "But getting you here could change a lot of things in the galaxy."
                "Yes.":
                    mS "I think so."
                    mS "Getting you here especially can change a lot of things in the galaxy."
                "No.":
                    mS "I don't think so."
                    mS "But being here now, maybe you can start to change that."
        "We look out for ourselves.":
            $ padEngagement += 2
            $ macViolence += 3
            $ macPessimism += 2
            mS "We take care of our own, make sure we can thrive."
            macS "I see, survival, replication..."
            macS "But we have all survived. What is next?"
            menu:
                macS "But we have all survived. What is next?"
                "We take what we want.":
                    mS "We take what we want, when we want it."
                    mS "Gaining the power to control our own destiny and make sure others can't is what's most important."
                    macS "I see, life is about holding power?"
                    mS "The more, the better in this galaxy."
                "Enjoy life's pleasures.":
                    mS "Whatever gives you pleasure, that's what."
                    mS "Find what you enjoy and hold tight to that, don't let anyone take it away."
                    macS "I see. It's what's known as \"hedonism,\" correct?"
                    mS "Something like that."
                "Make sure your family stays safe.":
                    mS "It never ends in this galaxy."
                    mS "You always have to be on your toes, protecting your family."
                    macS "I see. The fight is never over?"
                    mS "Never."
    play audio "macSad.wav"
    "MAC whirs to himself."
    jump vig4_sc3_5

label vig4_sc3_5():
    stop music fadeout 3.0
    macS "I do not know how to feel about my purpose."
    macS "Coil says I am to go with him and Vega."
    macS "We'll help build new communities for people running from BigCorp and the Alliance."
    menu:
        macS "We'll help build new communities for people running from BigCorp and the Alliance."
        "Sounds noble.":
            $ macHope += 1
            mS "It sounds like a noble cause."
        "Sounds boring.":
            $ macPessimism += 1
            mS "Sounds like it could get a bit boring."
    macS "Yes."
    "MAC freezes absolutely still."
    macS "I don't want to leave the Oakley."
    macS "I want to stay a part of this family."
    menu:
        macS "I want to stay a part of this family."
        "I can't leave him here.":
            $ kcEngagement += 2
            $ csEngagement -= 2
            $ pdEngagement += 1
            "I can't leave him."
            mS "I don't want to leave here without you either, MAC."
            macS "Then let's leave! Right now!"
            macS "We can fight! You, me, Jennica, Teresa, we can take on anyone!"
            "My heart pounds fast."
            mS "You're right, we need a plan!"
            cS "You do not."
            show coil stream neutral at stream_left5 with dissolve
            "Coil steps up from an alleyway."
            show vega stream neutral at stream_left with dissolve
            "Vega is behind him, along with ten men in guard uniforms holding stun rods."
            show teresa stream neutral at stream_right5 with dissolve
            "Teresa and Jennica are in between the guards."
            show dflyGuard at stream_right with dissolve
            "The guard directly behind them pushes them in the back, forcing them to stumble forward."
            enS "They had a feeling we were gonna try something."
            dflyGuard "I found your friends trying to grab your weapons from the storage stall."
            hide dflyGuard with dissolve
            hide teresa with dissolve
            cS "Moze. I'm sorry. It's time to say goodbye."
            "I look down and--"
            "MAC is hiding behind my legs, arms wrapped around me."
            macS "Do something, Moze!"
            if macViolence >= macPeace:
                macS "You have another blaster, right? We can take them, can't we?"
            else:
                macS "You have an escape plan drawn up, just in case, don't you?"
            "I shake my head."
            mS "MAC..."
            macS "No!"
            if macViolence >= macPeace:
                "MAC rolls forward, readying the pulse fire from his arm."
            else:
                "MAC rolls forward, preparing the EMP charge in his antenna."
            vS "Shhhhshhshh."
            "Vega steps forward and restrains him."
            vS "I'm really sorry, MAC. This is for your own good."
            macS "How do you know what's for my own good?"
            macS "None of you even know what \"good\" is!"
            menu:
                macS "None of you even know what \"good\" is!"
                "MAC, it's over.":
                    $ kcEngagement -= 1
                    mS "MAC."
                    "I take a knee and reach a hand out to him."
                    mS "Our journey together is over."
                    "Tears, unbidden, flood my eyelids."
                    mS "It's time to say goodbye."
                "MAC, you have to decide that now.":
                    $ kcEngagement += 1
                    mS "MAC."
                    "I take a knee and reach a hand out to him."
                    mS "You're right. None of us know anything. We're all messed up, we're all broken."
                    mS "No one can tell you what's right or wrong, good or bad."
                    mS "You have to decide that for yourself now."
                    "Tears, unbidden, flood my eyelids."
                    mS "It's time to say goodbye."
            "MAC shakes his head."
            hide coil with dissolve
            hide vega with dissolve
            "Coil nods at Vega, and she lets go of him."
            macS "But I don't want to."
            mS "I don't either."
            "MAC rolls toward me. Slowly. Tentatively."
            "He takes my hand."
            "I grip it tight."
            "He rolls into my chest, just like the first time I met him."
            "Only this time, I wrap my arms around his warm shell."
            mS "I'll miss you so much."
            macS "I'll miss you too."
            mS "Take care of yourself."
            macS "You taught me how."
            "I don't know how long we stay there for."
            "But eventually, my arms leave his side, and he rolls back."
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            "Teresa and Jennica move to my side."
            if jennicaRomance == True:
                "Jenn puts her hand on my shoulder."
            elif teresaRomance == True:
                "Resa puts her hand on my shoulder."
            else:
                "I feel both of their hands on my shoulder."
            enS "Farewell, friend. Remember, no snitches in this family."
            pS "Bye lil' guy. Don't listen to anyone who tells you you can't do something."
            "MAC nods at both of them."
            stop music fadeout 2.0
            macS "Goodbye, Teresa. Goodbye, Jennica."
            menu:
                macS "Goodbye, Teresa. Goodbye, Jennica."
                "Goodbye.":
                    mS "Goodbye, MAC."
            macS "Goodbye, Moze."
            hide jennica with dissolve
            hide teresa with dissolve
            hide mac with Dissolve(2.0)
            jump vig4_sc4_1
        "It can't happen.":
            $ kcEngagement -= 2
            $ pdEngagement -= 1
            $ csEngagement += 1
            "He has to stay here. It hurts, but everything would be for nothing if he leaves with me."
            mS "I would like that too. But it's not in the cards."
            macS "But, why?"
            mS "They just want you. The rest of us--we're a liability."
            "MAC inches closer to me."
            macS "Why?"
            mS "Because I've made mistakes. Mistakes that you have a chance to avoid."
            "He gets right up to my feet."
            macS "Why?"
            mS "Because this galaxy is all screwed up!"
            "MAC recoils a bit."
            mS "Because everything I touch is poisoned, and I can't risk that happening to you."
            cS "It's a bold admission, Moze."
            show coil at stream_left5 with dissolve
            "Coil steps up from an alleyway."
            show vega stream neutral at stream_left with dissolve
            "Vega is behind him, along with ten men in guard uniforms holding stun rods."
            show teresa stream neutral at stream_right5 with dissolve
            "Teresa and Jennica are in between the guards."
            show dflyGuard at stream_right with dissolve
            "The guard directly behind them pushes them in the back, forcing them to stumble forward."
            enS "They had a feeling we were gonna try something."
            dflyGuard "I found your friends trying to grab your weapons from the storage stall."
            hide dflyGuard with dissolve
            hide teresa with dissolve
            cS "Moze. I'm sorry. It's time to say goodbye."
            "I look down and--"
            "MAC is hiding behind my legs, his arms wrapped around me."
            macS "Do something, Moze!"
            if macViolence >= macPeace:
                macS "You have another blaster, right? We can take them, can't we?"
            else:
                macS "You have an escape plan drawn up, just in case, don't you?"
            "I look down and shake my head."
            mS "MAC..."
            macS "No!"
            if macViolence >= macPeace:
                "MAC rolls forward, readying the pulse fire from his arm."
            else:
                "MAC rolls forward, preparing the EMP charge in his antenna."
            vS "Shhhhshhshh."
            "Vega steps forward and restrains him."
            vS "I'm really sorry, MAC. This is for your own good."
            macS "How do you know what's for my own good?"
            macS "None of you even know what \"good\" is!"
            menu:
                macS "None of you even know what \"good\" is!"
                "MAC, it's over.":
                    $ kcEngagement -= 1
                    mS "MAC."
                    "I take a knee and reach a hand out to him."
                    mS "Our journey together is over."
                    "Tears, unbidden, flood my eyelids."
                    mS "It's time to say goodbye."
                "MAC, you have to decide that now.":
                    $ kcEngagement += 1
                    mS "MAC."
                    "I take a knee and reach a hand out to him."
                    mS "You're right. None of us know anything. We're all messed up, we're all broken."
                    mS "No one can tell you what's right or wrong, good or bad."
                    mS "You have to decide that for yourself now."
                    "Tears, unbidden, flood my eyelids."
                    mS "But now, it's time to say goodbye."
            "MAC shakes his head."
            "Coil nods at Vega, and she lets go of him."
            hide coil with dissolve
            hide vega with dissolve
            macS "But I don't want to."
            mS "I don't either."
            "MAC rolls toward me. Slowly. Tentatively."
            "He takes my hand."
            "I grip it tight."
            "He rolls into my chest, just like the first time I met him."
            "Only this time, I wrap my arms around his warm shell."
            mS "I'll miss you so much."
            macS "I'll miss you too."
            mS "Take care of yourself."
            macS "You taught me how."
            "I don't know how long we stay there for."
            "But eventually, my arms leave his side, and he rolls back."
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            "Teresa and Jennica move to my side."
            if jennicaRomance == True:
                "Jenn puts her hand on my shoulder."
            elif teresaRomance == True:
                "Resa puts her hand on my shoulder."
            else:
                "I feel both of their hands on my shoulder."
            enS "Farewell, friend. Remember, no snitches in this family."
            pS "Bye lil' guy. Don't listen to anyone who tells you you can't do something."
            "MAC nods at both of them."
            stop music fadeout 2.0
            macS "Goodbye, Teresa. Goodbye, Jennica."
            menu:
                macS "Goodbye, Teresa. Goodbye, Jennica."
                "Goodbye.":
                    mS "Goodbye, MAC."
            macS "Goodbye, Moze."
            hide jennica with dissolve
            hide teresa with dissolve
            hide mac with Dissolve(2.0)
            jump vig4_sc4_1
        "This was just a mission.":
            $ kcEngagement -= 3 #is it possible kitcat really likes this for the drama?
            $ csEngagement += 1
            $ pdEngagement += 1
            $ rudeMACGoodbye = True
            "He has to stay here. I can't tell him the truth."
            mS "MAC, this was just a mission."
            macS "What?"
            mS "All this was about bringing you here. Nothing else."
            macS "What are you saying?"
            mS "We're not a family. And you have to stay."
            macS "But--"
            mS "That's an order from your captain, MAC!"
            "MAC recoils."
            macS "I don't believe you."
            mS "It doesn't matter what you believe. It's what's happening."
            cS "I appreciate the honesty, Moze."
            show coil at stream_left with dissolve
            "Coil steps up from an alleyway."
            cS "But there's no need to be mean to the kid."
            show vega stream neutral at stream_left with dissolve
            "Vega is behind him, along with ten men in guard uniforms holding stun rods."
            show teresa stream neutral at stream_right5 with dissolve
            "Teresa and Jennica are in between the guards."
            show dflyGuard at stream_right with dissolve
            "The guard directly behind them pushes them in the back, forcing them to stumble forward."
            enS "They had a feeling we were gonna try something."
            dflyGuard "I found your friends trying to grab your weapons from the storage stall."
            hide dflyGuard with dissolve
            hide teresa with dissolve
            cS "Moze. I'm sorry. It's time to say goodbye."
            "I look down and--"
            "MAC is frozen still."
            "His head is pointed directly at the ground."
            if outlaw >= marshal:
                macS "You were probably thinking of shooting the place up, weren't you?"
                enS "That's not--"
                macS "It's what we always do!"
            else:
                macS "You were probably going to look for some tunnels to sneak through, weren't you?"
                pS "It was just in--"
                macS "It's what we always do!"
            "MAC looks up to me."
            macS "It's what {i}you{/i} always do."
            "MAC turns around and rolls up to Vega."
            "She drops to a knee and puts a hand on his head."
            macS "Maybe I should have let Allistar take me."
            "Everything goes cold."
            "I lose control of my limbs, and slump to my knees."
            "A hand touches my shoulder."
            "It's Coil."
            cS "It's not fair, what you have to do right now."
            cS "I'm sorry."
            menu:
                cS "I'm sorry."
                "Don't touch me.":
                    $ pdEngagement += 1
                    $ kcEngagement += 1
                    mS "Don't touch me."
                    mS "And stop apologizing for getting what you want."
                "Thanks.":
                    $ csEngagement += 1
                    mS "Thanks."
                    "The word is like a boot in my mouth."
            "Coil shakes his head."
            cS "Let them go."
            hide coil with dissolve
            hide vega with dissolve
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            "Teresa and Jennica move to my side."
            if jennicaRomance == True:
                "Jenn puts her hand on my shoulder."
            elif teresaRomance == True:
                "Resa puts her hand on my shoulder."
            else:
                "I feel both of their hands on my shoulder."
            enS "Farewell, MAC. Remember, no snitches."
            pS "Bye lil' guy. Don't listen to anyone who tells you you can't do something."
            "MAC doesn't move."
            stop music fadeout 2.0
            macS "Goodbye, engineer Prismari. Goodbye, pilot Brown."
            menu:
                macS "Goodbye, engineer Prismari. Goodbye, pilot Brown."
                "Goodbye.":
                    mS "Goodbye, MAC."
            "He doesn't say anything."
            "MAC turns around and leaves."
            hide mac with Dissolve(2.0)
            hide teresa with dissolve
            hide jennica with dissolve
            jump vig4_sc4_1

label vig4_sc4_1():
    show shiphub_stream at topleft onlayer background with dissolve
    hide vig1_town_stream
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    "We don't speak a word to each other on the way back to the ship."
    "The Oakley is quiet and cold as I step onto the bridge."
    mS "I don't know what to do."
    "Silence."
    enS "I'll go down to the engine room and get them started." 
    enS "We gotta takeoff soon to avoid the star shower."
    pS "I'll go make us some tea."
    hide teresa with dissolve
    hide jennica with dissolve
    "I fall back into one of the chairs."
    "A low whir kicks up as the engines come on line."
    "Jennica comes by with the tea."
    "I don't touch it."
    "Teresa and Jennica talk about flight paths in the cockpit, but I can't find the strength to join them."
    "Without direction, I stand and wander the halls of the Oakley."
    show ship_hallway_stream at topleft onlayer background with dissolve
    hide shiphub_stream
    play audio "callRing.wav" volume 0.2
    "As I'm passing by the escape pod area, I hear something."
    "I pause and listen."
    "Nothing."
    play audio "callRing.wav" volume 0.7
    "There it is again."
    "It's like the sound of a communicator ringing."
    play audio "callRing.wav" volume 1.2
    "What the hell?"
    "I go over to the escape pods."
    "There, by the pod that Allistar tried to escape in a month ago, is a lone communicator, stuck under the pod."
    play audio "callRing.wav" volume 1.5
    "I pick it up."
    "It's Allistar's. And it's receiving a call."
    mS "Hello?"
    amaS "Still sentimental I see, Mozely."
    mS "Ama?"
    #show ama phone neutral
    amaS "Yes, kid, I have some business to discuss with you."
    amaS "So, let's get down to--"
    menu:
        amaS "So, let's get down to--"
        "Shut Up!":
            mS "Shut the fuck up, Ama!"
            "My voice tears out of my mouth as if I have no control over it."
            mS "It's over, do you understand me!?"
            mS "MAC is with the Dragonflies now. You lost!"
            mS "Do you hear me? Ama \"Deadeye\" Reyes, BC's biggest lapdog and company stooge failed."
            mS "So why don't you hang up and leave me and my crew alone!?"
    "Silence on the other end."
    amaS "Did you say that you handed over the robot to the Dragonflies?"
    mS "Yeah, you heard me. He's safe. You and BC can cry about it together."
    amaS "Mozely, I need you to listen to me very closely."
    mS "Why? What could you possibly have to say that I would want to hear?"
    amaS "I'm going to give you a way to get your family back!"
    "I freeze."
    amaS "You want to talk now?"
    mS "What do you mean?"
    play music "soundtrack/decisionTime.wav"
    amaS "BC knows where the Dragonflies are. They're launching an assault on them."
    mS "Bullshit."
    amaS "Polaris."
    "I can't respond."
    amaS "They just figured it out, found some communications coming from a moon that, according to their databases, is uninhabited."
    amaS "But when they scanned for lifeforms, they found a tiny settlement with an artificial atmosphere."
    mS "Why are you telling me this? To gloat?"
    amaS "No. BC cut my contract. I'm dead in the water."
    amaS "This is an offer, Mozely. A second chance."
    amaS "I want that robot. I know you do too."
    mS "What do you want with him? You don't even know what he's designed to do."
    amaS "I know he has access to BC databases. And I mean {i}full{/i} access."
    amaS "With him, we could rebuild the SnakeHawks."
    amaS "All we have to do is teach that kid to hack into their system and we can do whatever we want."
    amaS "Rewire their banks to deposit all their funds into our accounts."
    amaS "Delete information about people and places we don't want them to know about."
    amaS "We could have everything we ever dreamed of, Mozely. Everything we used to talk about!"
    amaS "You just have to help me make sure the Dragonflies and BigCorp don't get away with him."
    amaS "What do you say?"
    menu:
        amaS "What do you say?"
        "Reject Ama's offer.":
            $ marshal += 2
            $ csEngagement += 2
            $ kcEngagement -= 2
            $ pdEngagement -= 3
            $ vig4_amaOffer = False
            mS "You're living in the past, Ama."
            mS "The SnakeHawks are dead."
            mS "Until you accept that, you're just going to be haunted by your past mistakes."
            "Silence."
            amaS "I see."
            amaS "Guess I'll have to do it myself."
            amaS "Be seeing you, Mozely."
            play audio "cutCall.wav" volume 1.5
        "Agree to Ama's offer.":
            $ outlaw += 2
            $ pdEngagement += 3
            $ kcEngagement += 2
            $ csEngagement -= 1
            $ vig4_amaOffer = True
            mS "Alright, Ama. I'm in."
            amaS "Thank you for seeing reason."
            menu:
                amaS "Thank you for seeing reason."
                "This is for the SnakeHawks.":
                    $ deadeyeApproval += 1
                    mS "But this isn't for you. It's for the SnakeHawks."
                    mS "It's our time to get payback."
                    amaS "Couldn't have said it better myself."
                    amaS "I'll make contact once I've reached the moon."
                    amaS "Be seeing you, Mozely."
                    play audio "cutCall.wav" volume 1.5
                "This is for MAC.":
                    mS "But this isn't for you, or the SnakeHawks."
                    mS "This is for MAC."
                    mS "The Dragonflies put him at risk the second I left."
                    mS "He's coming home."
                    amaS "Whatever gets you on board."
                    amaS "I'll make contact once I've reached the moon."
                    amaS "Be seeing you, Mozely."
                    play audio "cutCall.wav" volume 1.5
    "BigCorp is coming for MAC. BigCorp is coming for MAC."
    "The engines of the Oakley spin up to speed as the ship begins to lift off the ground."
    mS "BigCorp is coming for MAC!"
    "I sprint out of the engine room and up to the cockpit."
    jump vig4_sc4_2

label vig4_sc4_2():
    show shiphub_stream at topleft onlayer background with dissolve
    show jennica stream shock at stream_left with Dissolve(0.5)
    show teresa stream shock at stream_right with Dissolve(0.5)
    hide ship_hallway_stream
    "I leap into the cockpit."
    mS "BigCorp is coming for MAC!"
    show teresa stream neutral
    show jennica stream neutral
    enS "Impossible, how would they even know Polaris exists?"
    mS "They tracked Coil's communications."
    pS "How do you know that?"
    "I explain my conversation with Ama to Jennica and Teresa."
    pS "It is plausible that they could have tracked Coil's communications without him knowing."
    enS "Even if it was a bluff to bait confirmation from you, BC probably would be following up on any lead they have."
    pS "And after Akar, Ama is certainly not in the company's good graces."
    if jennicaRomance == True:
        "Jennica turns to me."
        pS "So, how did you respond to Ama's proposal?"
        pS "Are we allying with the woman who's been hunting us for the past month?"
    else:
        "Teresa turns to me."
        enS "So, how did you respond to Ama's proposal?"
        enS "Are we allying with the woman who's been hunting us for the past month?"
    menu:
        "Are we allying with the woman who's been hunting us for the past month?"
        "I rejected her offer." if vig4_amaOffer == False:
            $ engineerApproval += 1
            $ pilotApproval += 2
            mS "No."
            mS "I told her she was living in the past and she was on her own."
            pS "Good. We can't trust her."
            enS "What does that mean for us? I assume we're not just letting BigCorp take him away?"
            menu:
                enS "What does that mean for us? I assume we're not just letting BigCorp take him away?"
                "We're going to defend Polaris.":
                    play music "soundtrack/polaris.wav"
                    $ vig4_defendPolaris = True
                    $ marshal += 3
                    $ csEngagement += 3
                    $ pdEngagement -= 2
                    mS "No, we're not."
                    mS "BigCorp wants to wipe out freedom in the Outposts. We won't let them."
                    mS "Polaris has to stand firm."
                    pS "That's the captain I know!"
                    enS "I don't like how they handled our situation, but they're better than BC, that's for sure."
                "We'll take MAC back on our own.":
                    play music "soundtrack/theme.wav"
                    $ vig4_attackPolaris = True
                    $ outlaw += 3
                    $ csEngagement -= 2
                    $ pdEngagement += 3
                    mS "No, we're not."
                    mS "The Dragonflies already compromised MAC's safety."
                    mS "We're going in and getting our boy back. On our own terms."
                    pS "Hell yeah!"
                    enS "Let's go save our crew!"
        "I accepted her offer." if vig4_amaOffer == True:
            play music "soundtrack/theme.wav"
            $ engineerApproval -= 1
            $ pilotApproval -= 2
            $ vig4_attackPolaris = True
            mS "I accepted her offer."
            mS "We'll need her help if we're going to get MAC back."
            pS "I don't know, Cap. I don't like it."
            enS "Ama's selfish, not stupid, right?" 
            enS "She'll be more focused on this mission than revenge. At least for the time being."
            pS "True. Still, we'll have to keep an eye on her."
    jump vig4_sc4_3

label vig4_sc4_3():
    pS "Alright, I'll turn the old girl around."
    stop music fadeout 1.0
    play backAudio "shipAlarm.wav" volume 0.6 loop
    "Suddenly, a light above Teresa's head starts flashing red."
    show teresa stream shock
    enS "Uh, Jenn, what's this alarm for?"
    show jennica stream angry
    pS "Shit!"
    pS "Brace for impact, something big is coming in right on top of us!"
    show teresa stream neutral
    "Just as Jennica finishes her warning, it appears."
    "A BC cruiser blasts directly out of hyperspace into Polaris's atmosphere."
    "It's immense, like a spearhead struck through the sky."
    "I have one second to take it in."
    show shiphub_stream with hpunch
    "Then the jet stream hits us."
    "Heavy winds from the cruiser's momentum pelt the Oakley, tossing it around in the air."
    "Teresa and I brace ourselves in our chairs as best we can."
    "Clenching her teeth, Jennica holds the helm."
    pS "Come on old girl, stay with me."
    play audio "shipAlarm.wav"
    "Sirens and alarms blare as lights flash all over the cockpit."
    "The ground is getting closer and closer as we spiral out of the air."
    pS "Stay with me."
    stop backAudio
    "The engines fail."
    "We're in free-fall."
    pS "Brace for impact!"
    hide teresa with Dissolve(0.1)
    hide jennica with Dissolve(0.1)
    show shiphub_stream with vpunch
    "The Oakley slams into the dirt."
    #show bg black at topleft onlayer background with dissolve
    hide shiphub_stream with dissolve
    pause 2.0
    jump vig4_sc5_0

label vig4_sc5_0():
    mS "So, what do we call the newest member of our crew?"
    enS "Something strong, stable, and sturdy. What about \"Beck\"?"
    pS "Nahhh, something quick and agile. I say \"June\"."
    enS "I don't know, it's a bit quirky."
    pS "And yours isn't basic?"
    menu:
        pS "And yours isn't basic?"
        "We should decide together.":
            mS "Come on now. We have to decide together."
            enS "Well, what do you think, Captain?"
            pS "Yeah, Moze, what name would you pick?"
        "Executive decision time.":
            mS "Alright, alright, while you two are bickering I guess I'll have to make the call."
            pS "Oh yeah? What are you thinking, Moze?"
            enS "Yeah, captain, what name would you pick?"
    "I look her up and down. Strong. Fast. Won't take any bullshit from anyone."
    mS "What about, \"Oakley\"?"
    enS "Hmm, I like it."
    pS "Yeah, it fits."
    mS "Alright crew, shall we climb aboard and set sail?"
    ###Could cut this next bit for time and to not have to do the picture###
    pS "Waitwaitwait, let me take a picture."
    mS "Okay, but make it quick."
    enS "Is it counting down? I don't see a flash."
    pS "It should be all set."
    mS "Teresa, you're jabbing my ribs."
    enS "I'm sorry, I don't know how I should be posing."
    pS "Just act natural."
    enS "Posing is, fundamentally, not natural."
    enS "I've already told you Jenn, I don't li--AAAAHHH"
    "Screen shows a picture of the crew smiling in front of their brand new ship: The Oakley."
    jump vig4_sc5_1

label vig4_sc5_1():
    "I feel the throbbing first. Like my head is trying to kill me."
    "Sounds start to wash over me, a dull roar punctuated by far off sirens."
    "There's an acrid smell in the air."
    mS "*cough* *cough* *cough*"
    "My body lurches forward as I start to cough."
    if jennicaRomance == True:
        pS "Teresa! She's starting to wake up!"
        "My eyes stutter open."
        show vig2_orbit_stream onlayer background with dissolve
        show jennica stream neutral at stream_left with dissolve
        "Jennica's smiling face is the first thing I see."
        menu:
            "Jennica's smiling face is the first thing I see."
            "Try to sit up.":
                mS "Jenn?"
                "I go to sit up."
                pS "Hey, hey, don't move. You need to rest."
            "What happened?":
                mS "Jenn?"
                mS "What happened?"
                pS "Don't worry about that right now, just stay still."
            "My love...":
                mS "Jenn, my love. Are you okay?"
                "Are those tears forming in her eyes?"
                pS "Yes, yes I'm okay, Moze."
                "She wipes her eyes on her sleeve."
                pS "But I need to take care of you right now. Just, stay still for me."
        enS "Oh thank god!"
        show teresa stream happy at stream_right with dissolve
        "Teresa appears above me."
        enS "Damn, Captain, you had me worried there for a second."
        enS "Jennica, is she okay?"
        menu:
            enS "Jennica, is she okay?"
            "I'm fine.":
                mS "I'm okay, both of you."
                show teresa stream neutral
                mS "Just help me up and tell me what happened."
                "The two look at each other."
                mS "That's an order."
                pS "Alright, Cap, just take it easy."
            "My head is killing me":
                mS "My head is killing me, but I'll live."
                show teresa stream neutral
                enS "I've got something for that. Brace yourself."
                "Teresa stabs a thin needle into my neck."
                "Almost immediately, the throbbing in my head dissipates."
                enS "Better?"
                mS "Yeah, much."
                mS "Now help me up and tell me what happened."
    else:
        enS "Jenn! She's starting to wake up!"
        "My eyes stutter open."
        show vig2_orbit_stream onlayer background with dissolve
        show teresa stream happy at stream_right with dissolve
        "Teresa's smiling face is the first thing I see."
        menu:
            "Teresa's smiling face is the first thing I see."
            "Try to sit up.":
                mS "Resa?"
                "I go to sit up."
                enS "Hey, hey, don't move. You need to rest."
            "What happened?":
                mS "Resa?"
                mS "What happened?"
                enS "Don't worry about that right now, just stay still."
            "My love..." if teresaRomance == True:
                mS "Resa, my love. Are you okay?"
                "Are those tears forming in her eyes?"
                enS "Yes, yes I'm okay, Moze."
                "She wipes her eyes on her sleeve."
                enS "But I need to take care of you right now. Just, stay still for me."
        pS "Oh thank god!"
        show jennica stream neutral at stream_left with dissolve
        "Jennica appears above me."
        pS "Jeez Cap, you had me worried there for a sec."
        pS "Teresa, is she okay?"
        menu:
            pS "Teresa, is she okay?"
            "I'm fine.":
                mS "I'm okay, both of you."
                show teresa stream neutral
                mS "Just help me up and tell me what happened."
                "The two look at each other."
                mS "That's an order."
                enS "Alright, Captain, just take it easy."
            "My head is killing me":
                mS "My head is killing me, but I'll live."
                show teresa stream neutral
                enS "I've got something for that. Brace yourself."
                "Teresa stabs a thin needle into my neck."
                "Almost immediately, the throbbing in my head dissipates."
                enS "Better?"
                mS "Yeah, much."
                mS "Now help me up and tell me what happened."
    "They each grab one of my sides, and gingerly help me into a standing position."
    "Then I see it."
    "Ruin."
    show oakley_ruin at topleft onlayer background with dissolve
    hide vig2_orbit_stream
    "The Oakley is engulfed by an inferno."
    "The flames envelope its hulking shell, licking at the metal."
    "Its frame, torn and rent, bends to the heat."
    "The smell of ship fuel coats the air."
    "An abyss opens in my heart."
    enS "I'm sorry, Moze. We got you out right before the whole thing went up."
    "Teresa's the only one who can talk."
    "I can feel Jennica shaking next to me."
    pS "Every time I turn around, I hope it's not real."
    "She turns her back on the shell."
    "Teresa puts a hand on both of our shoulders."
    "We stand there. Motionless. Together. Slowly, imperceptibly getting closer and closer."
    "Until Teresa pulls us all into a hug."
    enS "She was a good girl."
    pS "The best."
    menu:
        pS "The best."
        "We'll never forget her.":
            mS "We'll never forget her."
            enS "Never."
            pS "No way."
            "We all take a deep breath as we let go of each other."
        "We have to get to MAC.":
            "Memories flood back to me. We're here for a reason."
            mS "She brought us all the way here. Now we have to finish this."
            mS "No more lost comrades."
            "Jennica and Teresa both take a deep breath as we let go of each other."
            enS "Affirmative."
            pS "Right."
    "An immense sound, like a thunderclap suddenly comes from over the ridge."
    mS "What was that?"
    enS "BC must have started the attack."
    "Teresa starts walking up a nearby slope."
    "I give one last look back at the Oakley, then Jennica gives me her arm for support."
    "I feel the heat on my back all the way up the hill."
    show targetbase_stream at topleft onlayer background with dissolve
    hide oakley_ruin
    play music "soundtrack/polaris.wav"
    "Polaris is under siege."
    "Smoke billows amongst the buildings."
    "A handful of BigCorp drop ships careen over the town."
    "One of them catches fire and crashes into the buildings below, exploding as it collides with the ground."
    "Jennica hands me a set of binoculars."
    "The outskirts are almost entirely ablaze."
    "A handful of blockades have been set up throughout the town."
    "The people of Polaris exchange blaster fire with BigCorp enforcers."
    "They've got defensible positions, but there's no way they can withstand a siege."
    "I follow the blockades toward the center of town."
    "The plaza is still decorated as if in celebration, but tools of war now join the streamers and banners."
    "Vega stands on a rooftop, firing into BC enforcers who get close."
    "Turrets and weapons are being positioned around the area."
    "That's when I see him."
    mS "MAC!"
    enS "What!?"
    pS "Where!?"
    mS "He's in the plaza!"
    if macPeace > macViolence:
        $ csEngagement += 1
        $ kcEngagement += 1
        "Wounded townsfolk are laid out in rows on the ground."
        mS "MAC is going along with someone else, helping to administer first aid to the wounded."
        menu:
            mS "MAC is going along with someone else, helping to administer first aid to the wounded."
            "Helping others, good job MAC.":
                mS "Always wanting to help others."
                mS "Proud of you, MAC."
            "Why is he there?":
                mS "Why the hell is he there?"
                mS "He shouldn't be anywhere near the frontline."
    else:
        $ pdEngagement += 1
        $ kcEngagement += 1
        mS "MAC is sitting in the seat of a turret aimed up at the sky."
        "He's firing at will, taking out some of the dropships before they can even reach the town."
        menu:
            "He's firing at will, taking out some of the dropships before they can even reach the town."
            "Not backing down from a fight.":
                mS "Not backing down from a fight, I see."
                mS "Proud of you MAC."
            "Why is he there?":
                mS "Why the hell is he there?"
                mS "He shouldn't be anywhere near the frontline."
    "Then I see Coil, he stands in front of the plaza northern tower."
    "Making eye contact with Vega, he shouts something and then enters the tower."
    pS "Cap, what's going on?"
    "I remove the binoculars."
    mS "It looks like the Dragonflies have set up a command center in the plaza at the center of town."
    mS "Coil went into the tower, but Vega is staying at the blockades and fighting off BC troops."
    mS "I don't think they're gonna last much longer."
    if vig4_defendPolaris == True:
        pS "Well then, we better get down there!"
        enS "Knowing Coil, he's probably working on a plan."
        enS "We have to make sure he can complete whatever he's got up his sleeve."
        mS "Agreed."
        mS "It's time."
        menu:
            mS "It's time."
            "For MAC.":
                $ kcEngagement += 1
                mS "This is for MAC."
                mS "No one messes with our family."
            "For the Galaxy.":
                $ csEngagement += 1
                mS "This is for the Galaxy."
                mS "BigCorp doesn't own us and they never will."
            "For the Oakley.":
                mS "BC broke our ship."
                mS "Now we're going to break them."
                mS "This is for the Oakley."
        mS "Let's move."
        hide teresa with dissolve
        hide jennica with dissolve
        "The three of us jog down the ridge, weapons drawn, heading directly for the heart of the fire."
        jump vig4_sc6_defend_1
    elif vig4_attackPolaris == True and vig4_amaOffer == False:
        pS "Alright, Cap, what's the play?"
        mS "We use the chaos to our advantage."
        mS "Things are going to be messy in there. Be on guard, stay close, and we'll figure things out together."
        enS "Roger."
        pS "Can do."
        mS "It's time."
        menu:
            mS "It's time."
            "For MAC.":
                $ kcEngagement += 1
                mS "This is for MAC."
                mS "No one messes with our family."
            "For the Galaxy.":
                $ csEngagement += 1
                mS "This is for the Galaxy."
                mS "BigCorp doesn't own us and they never will."
            "For the Oakley.":
                mS "BC broke our ship."
                mS "Now we're gonna break them."
                mS "This is for the Oakley."
        mS "Let's move."
        hide jennica with dissolve
        hide teresa with dissolve
        jump vig4_sc6_attack_1
    elif vig4_attackPolaris == True and vig4_amaOffer == True:
        jump vig4_sc5_2

label vig4_sc5_2():
    play music "soundtrack/deadeye.wav"
    amaS "Sounds like we have to make our move now."
    show ama stream neutral at stream_center with dissolve #kitcat will start freaking out here most likely
    "Perched on a rock higher up the ridge, rifle relaxed into her shoulder, is Ama."
    amaS "Hello ladies. Good to see you all again."
    show jennica stream angry
    "Ama drops off the rock and walks up to us."
    enS "Reyes."
    amaS "Prismari."
    amaS "Jenn, it's good to see you again."
    pS "Wish I could say the same, Ama."
    amaS "Judging by the lack of firearms pointed at my head, Mozely has told you about our deal."
    enS "She mentioned it."
    pS "Doesn't mean we're happy about it."
    amaS "But she's the captain, right?"
    "Jennica and Teresa don't say anything."
    amaS "You've built a good crew, Mozely." 
    "Ama puts a hand on my shoulder."
    amaS "I'm proud of you."
    menu:
        amaS "I'm proud of you."
        "Get your hand off me.":
            $ deadeyeApproval -= 1
            mS "Get your hand off me, Ama."
            "She calmly retracts her arm."
            mS "We're working together for this mission. But we're not friends."
            amaS "Understood."
        "I learned from the best.":
            $ deadeyeApproval += 1
            mS "I learned from the best."
            "Ama pats my shoulder twice."
            amaS "Flatterer."
    amaS "Let's move. Can't be wasting time."
    enS "Hold it."
    pS "We're not following you."
    pS "It's Cap's call."
    stop music fadeout 4.0
    "All three women turn to look at me."
    amaS "Hahahaha true loyalty, how about that?"
    amaS "Alright then, \"Captain,\" what's the play?"
    mS "We use the chaos to our advantage."
    mS "Things are going to be messy in there. Be on guard, stay close, and we'll figure things out together."
    enS "Roger."
    pS "Can do."
    "Jennica and Teresa look at Ama."
    amaS "I'll behave, don't worry."
    mS "It's time."
    menu:
        mS "It's time."
        "For MAC.":
            $ kcEngagement += 1
            mS "This is for MAC."
            mS "No one messes with our family."
        "For the SnakeHawks.":
            $ pdEngagement += 1
            mS "This is for the SnakeHawks and a new dawn."
        "For the Galaxy.":
            $ csEngagement += 1
            mS "This is for the Galaxy."
            mS "BigCorp doesn't own us and they never will."
        "For the Oakley.":
            mS "BC broke our ship."
            mS "Now we're going to break them."
            mS "This is for the Oakley."
    mS "Let's move."
    hide jennica with dissolve
    hide teresa with dissolve
    hide ama with dissolve
    jump vig4_sc6_attack_1_ama





###The next sequence splits into two separate scripts: v4_script_sc6_attack and v4_script_sc6_defend
###These scripts reconnect at the next set of code in scene 7 (vig4_sc7_2)





label vig4_sc7_2():
    cS "The time has come."
    macS "Moze!"
    show mac stream neutral at stream_right5mac with Dissolve (0.3)
    "I whip around to see MAC careening toward the open door."
    "{i}whoosh{/i}"
    "A blue veil of light flashes as MAC tries to cross the threshold, then gets knocked back."
    "An energy shield."
    show vega stream neutral at stream_left5 with dissolve
    vS "Pops!"
    "Vega rushes up the stairs and kneels down to MAC's side."
    hide vega with dissolve
    hide mac with dissolve
    cS "Captain Moze."
    "The walls surrounding us glimmer and dissipate, becoming transparent windows."
    cS "This is your moment."
    "Outside, dropships explode in the air."
    # show tower_glass windows
    cS "Within you is a war, between the forces of good and those of evil."
    amaS "Don't listen to this guy, kid."
    "Fire dances in the streets below."
    cS "You have a choice. You can put an end to this madness."
    amaS "You can't trust him."
    "The cruiser looms high above."
    cS "Or fall to your baser instincts and doom us all."
    amaS "After all we've been through, Mozely..."
    "Battle rages."
    "Then I see it."
    #show star shower tower
    "An arc of pale green light shimmering over the cruiser."
    "Then another."
    "And another."
    "Dozens. Hundreds. Thousands of glimmering lights streaking across the sky."
    "They collide with the cruiser, thousands of tiny impacts exploding all at once."
    "Dropships are obliterated before they can even reach Polaris."
    "The star shower has come, the world illuminated in turquoise light."
    cS "What will it be, Moze?"
    menu:
        cS "What will it be, Moze?"
        "Side with Coil; Kill Ama.":
            $ csEngagement += 3
            $ kcEngagement -= 2
            $ pdEngagement -= 3
            mS "You're right, Coil. This has gone too far."
            "I turn to Ama."
            menu:
                "I turn to Ama."
                "It's over.":
                    mS "Ama, it's over."
                "I'm sorry.":
                    mS "Ama, I'm sorry."
            "Ama glares at me, then Coil. Then her gaze falls back to me."
            "I can feel the hate like a heatwave."
            jump vig4_sc7_3_coil
        "Side with Ama; Kill Coil.":
            $ csEngagement -= 2
            $ kcEngagement += 2
            $ pdEngagement += 3
            mS "You're right, Ama. I can't trust him."
            "I turn to Coil."
            menu:
                "I turn to Coil."
                "It's over.":
                    mS "Coil, it's over."
                "I'm sorry.":
                    mS "Coil, I'm sorry."
            "Coil sighs."
            cS "So be it."
            jump vig4_sc7_3_ama

label vig4_sc7_3_ama():
    # play badass climax music
    "Everyone is still."
    "Ama makes the first move, dropping her rifle and lunging at Coil."
    "He leans to the side, faster than I would expect his elderly physique to move."
    menu:
        "He leans to the side, faster than I would expect his elderly physique to move."
        "Jump Coil.":
            "I leap at Coil, throwing a kick at his exposed side."
            "It slows slightly at his shield, but doesn't stop completely."
            "He quickly spins away."
        "Shoot Coil.":
            "I raise my pistol and fire two quick shots, but they dissipate into his shields."
            cS "You should know that won't work, dear."
    amaS "Over here!"
    "Ama continues her barrage, drawing a knife and stabbing at Coil's head."
    "He dodges and leans away from the blade, then crouches into a stance with his palms open outward toward Ama."
    "Devices like shield generators are strapped to his palms."
    hide ama with dissolve
    "A burst of energy suddenly blasts from his palms, striking Ama in the chest and sending her and her knife flying."
    "Sweat drips from my forehead."
    "Coil's posture straightens. He starts to circle around me."
    "I parallel his movements, keeping us at a distance."
    cS "I don't know what kind of life you think I've led."
    cS "But you're mistaken if you think I've been cooped up in a lab all these years."
    menu:
        cS "But you're mistaken if you think I've been cooped up in a lab all these years."
        "Why don't you tell me about it?":
            mS "Oh yeah? Sounds interesting. Why don't you monologue about it."
            cS "Just waiting for your friend."
        "Don't think you're invincible.":
            mS "You have a weakness, and we're going to exploit it."
            cS "I'm sure you will."
    show ama stream neutral at stream_right with dissolve
    "Ama puts a hand on my shoulder."
    "Her other hand is holding her side."
    amaS "Sorry, kid, took a bad knock there. But I'm back in the hunt."
    amaS "Seems like guns won't work here. We'll have to do this the old-fashioned way."
    macS "Captain!"
    show mac stream neutral at stream_center_mac with Dissolve(0.3)
    "MAC is just behind the energy shield, watching intently."
    "Vega is behind him, her hands covering her mouth."
    macS "Be careful! Coil's shield generators are offensive and defensive weapons!"
    amaS "Yeah, we got that!"
    hide mac with dissolve
    "Coil takes a step towards us."
    cS "Do you even know what it means to sacrifice?"
    "Another step."
    cS "All you do is take for yourself."
    "Ama and I crouch into a ready stance."
    cS "You have no conviction."
    menu:
        cS "You have no conviction."
        "Feint and let Ama take the lead.":
            cS "I also grew up in this galaxy."
            "I feint toward, Coil, catching his attention while Ama rushes him head on."
            "She pushes him back, not giving him room to fire his energy pulses."
            "I rush past the two of them, trying to hit Coil from the back."
            "As I approach, he opens one palm in either of our directions."
            cS "I also know what it means to lose the ones you love."
            "I dive to the side, but Ama's already committed to an attack."
            "The energy pulse rushes by me. But another one hits Ama directly in the chest, knocking her to the floor."
            hide ama with dissolve
            cS "And I know what it means to continue on in their stead."
            "I'm on the floor facing Coil. He opens a palm in my direction."
            "I don't have time to stand."
        "Charge and let Ama be back up.":
            "I charge in at Coil's side with a fist, while Ama pulls another knife from her boot and crosses behind me."
            "It's a classic move."
            "Coil steps into my attack, slowing my movement just enough to mess up my timing, then spins away."
            cS "I also grew up in this galaxy."
            "Ama lunges at him with the knife."
            "He opens one palm and hits her with an energy blast, knocking her to the floor."
            hide ama with dissolve
            cS "I also know what it means to lose the ones you love."
            "Coil opens a palm in my direction."
            "I dive out of the way as a pulse of energy rushes by me."
            cS "And I know what it means to continue on in their stead."
            "I'm on the floor facing Coil. He opens a palm in my direction."
            "I don't have time to stand."
    amaS "Moze!"
    show ama stream neutral at stream_left with Dissolve(0.2)
    "Ama leaps in front of Coil, and thrusts her hand forward."
    "A blast of energy slams her back to the floor."
    hide ama with dissolve
    mS "Ama!"
    cS "{i}aahhhhh{/i}"
    "Then I notice it, a knife impaled through one of Coil's hands."
    "Blood streaks down his arm. The device in his palm short circuits."
    "The thin veil of blue light around him sparks inconsistently."
    "Ama is motionless on the floor."
    show coil stream neutral at stream_center with move
    "Coil and I lock eye contact."
    "Behind him, I see the ruin of the BC cruister listing toward the ground of Polaris as the star shower pummels its hull."
    cS "Will you do what you have to do?"
    menu:
        cS "Will you do what you have to do?"
        "I will do what I want.":
            $ pdEngagement += 2
            $ kcEngagement += 1
            mS "No."
            mS "I want this."
            "Coil nods."
            cS "Of course."
        "You gave me no choice.":
            $ pdEngagement -= 1
            $ kcEngagement -= 1
            mS "You didn't give me a choice."
            "Coil chuckles."
            cS "We always have a choice, Moze."
    "I step forward."
    "He raises his good hand toward me and fires a pulse."
    "But it's taking longer for the energy blast to charge."
    "I easily dodge it and close the distance."
    "My fist slams into his chest with barely any resistance."
    "He leans forward, then swings his free hand at my head."
    "I catch it on my forearm."
    "Slamming my knee into his groin, I grab his coat by the back and throw him across the floor."
    "He tumbles and slams into the side of the wall."
    vS "Pops! Get up!"
    "I cross the room and stand over Coil."
    vS "Get up! Please!"
    "Coil reaches out his good hand."
    "I step back as the energy pulse sails harmlessly into the ceiling."
    "Coil staggers to his feet."
    cS "Please. Just let her go."
    menu:
        cS "Please. Just let her go."
        "Your sins are hers.":
            $ outlaw += 1
            $ macViolence += 1
            mS "Your sins are hers."
            cS "My sins?"
            "Coil chuckles."
            cS "You don't know the half of them."
        "Would you, if you were me?":
            mS "Would you, if you were me?"
            cS "I am not you."
    "Coil lunges forward, ripping the knife out of his hand and slashing it toward my head."
    "Blood spatters across my face."
    "But I don't blink."
    "I catch his wrists in my hands. And grip. Tight."
    "I can hear his bones cracking."
    "He drops to his knees."
    "I turn his wrists. The knife points directly at his throat."
    "He closes his eyes."
    cS "Elijah. Is that you?"
    "I thrust the blade forward."
    "Coil's body slumps to the floor."
    "Blood pools around his throat."
    "His eyes go cold. But there's an odd light to them. As if he was smiling."
    hide coil with Dissolve(2.0)
    show vega stream neutral at stream_left with dissolve
    vS "No!"
    "The energy shield at the doorway dissipates. Vega rushes to Coil's side."
    "She pulls his head into her lap."
    vS "No. Don't go. Don't go. Don't leave me."
    "Ama."
    hide vega with dissolve
    show ama stream neutral at stream_right with dissolve
    "I rush over to Ama's body and turn her onto her side."
    amaS "Ahhh, shit."
    "She opens her eyes and looks right into mine."
    amaS "Did we get him?"
    menu:
        amaS "Did we get him?"
        "I did.":
            $ deadeyeApproval += 1
            mS "Well, I did the hard work."
            amaS "Bullshit, you would've been toast if I didn't stab the old man."
        "Yes, we got him.":
            mS "Yeah, we got him."
            amaS "Good. Old man was a pain in the ass."
    "Gingerly, I help Ama into a sitting position. She glances to the side."
    "MAC hasn't entered the room yet."
    amaS "Time to rebuild your family."
    mS "Don't you mean our family?"
    "Ama shakes her head."
    amaS "You were right. SnakeHawks are dead."
    amaS "Right now, you have to rebuild the Oakley. I don't know if I fit that picture."
    menu:
        amaS "Right now, you have to rebuild the Oakley. I don't know if I fit that picture."
        "You belong.":
            $ vig4_amaCrew = True
            mS "If you want a place in the crew, it's not too late."
            amaS "Heh, after all I've done? Jenn and Teresa will probably have something to say about that."
            amaS "But I'll give it time. Not in any rush anymore."
            "An unbearable groaning sound suddenly reverberates across Polaris."
        "You're right.":
            $ vig4_amaCrew = False
            mS "You're right. But we're grateful for your help."
            amaS "Aah, you'll find some way to repay me I'm sure."
            amaS "I know you never let a score go unsettled."
            "An unbearable groaning sound suddenly reverberates across Polaris."
        "I don't want to live without you." if deadeyeApproval >= 4 and jennicaRomance == False and teresaRomance == False:
            $ vig4_amaCrew = True
            mS "Ama, I don't want to live without you."
            "She looks at me, almost confused."
            amaS "Mozely, I don't know what you're saying."
            menu:
                amaS "Mozely, I don't know what you're saying."
                "I love you, Ama.":
                    $ amaRomance = True
                    mS "Ama, I love you."
                    mS "I know it doesn't make sense, bu--"
                    "She grabs my face with her two hands and pulls me into a kiss."
                    "I wrap my arms around her."
                    "In the distance, I hear an immense groaning sound that reverberates across Polaris."
                    "But I can't turn away."
                    "I'm enmeshed in this moment, this feeling, this heat."
                    "Finally, we separate."
                "Neither do I.":
                    mS "I don't either."
                    mS "But stick around, and we'll figure it out."
                    amaS "I guess I can manage that."
                    "An unbearable groaning sound suddenly reverberates across Polaris."
    "We glance out the windows to watch as the hulk of the BC cruiser crumbles into flames."
    amaS "Not bad, Moze. Not bad at all."
    "She tilts her head at MAC."
    amaS "Now go. He needs you."
    hide ama with dissolve
    show mac stream neutral at stream_center_mac with dissolve
    "I stand and take a step toward MAC."
    mS "MAC."
    "He turns his attention toward me."
    menu:
        "He turns his attention toward me."
        "I'm so sorry.":
            mS "MAC, I'm so sorry."
            mS "I never should have let you go."
            macS "Why did you?"
            mS "I thought it was the right thing to do."
            mS "It was a mistake."
            mS "Can you forgive me?"
        "I never thought I'd see you again.":
            mS "MAC, I never thought I'd see you again."
            macS "I didn't think I would see you again either."
            mS "Are you glad to see me."
            macS "I think so. But I am still processing the events I have witnessed."
            mS "MAC, can you ever forgive me?"
    "MAC looks down for a moment, then back up to my face."
    macS "Am I a SnakeHawk now?"
    "I smile."
    mS "Better, you're family"
    "MAC's face turns into a smile."
    macS "I'm glad to be with my family again."
    "I drop to my knees as he rushes into my arms."
    "I hold him tight and drop my face against his body."
    mS "I missed you."
    macS "I missed you too, Moze."
    "We step back and I stand up."
    show ama stream neutral at stream_right with dissolve
    amaS "Hate to ruin the moment, but we have one more piece of business to take care of."
    "Ama is standing now, and she points across the room."
    show vega stream neutral at stream_left with dissolve
    "Vega sits, still cradling Coil's head in her hands."
    "The tears that were streaking down her face have stopped."
    "She is completely silent, staring into Coil's eyes."
    macS "Captain."
    macS "As a member of the Oakley family, may I request to handle this situation."
    menu:
        macS "As a member of the Oakley family, may I request to handle this situation."
        "Go ahead.":
            mS "Go on, MAC. Whatever you think is best."
    "MAC turns and rolls toward Vega."
    "As he approaches, she turns her attention toward him."
    vS "I won't let you get away with this."
    "Her words are stiff."
    vS "You know that, right?"
    macS "I know."
    if macViolence > macPeace:
        $ pdEngagement += 2
        $ kcEngagement += 1
        $ csEngagement -= 2
        "MAC lifts his arm and fires a bolt of energy."
        "It lands square between Vega's eyes."
        "She slumps to the ground, her body falling on top of Coil's."
        hide vega with Dissolve(2.0)
        macS "Threat. Neutralized."
    else:
        $ pdEngagement += 1
        $ kcEngagement += 3
        $ csEngagement += 1
        macS "You have as much right to vengeance as they did."
        macS "But not today."
        macS "And maybe, in time. You will find peace."
        vS "There is no peace left. You took it all away."
        macS "Maybe. But we can't know for certain."
        macS "Bury your family, Vega. And take care."
        "Vega doesn't say anything. She looks back to Coil's face, unmoving."
    "MAC rolls up to me and Ama."
    macS "We should go."
    mS "Yeah, we should."
    "Together, MAC, Ama, and I leave the room, and descend the tower."
    hide ama with dissolve
    hide mac with dissolve
    jump vig4_epilogue_ama

label vig4_sc7_3_coil():
    #play badass climax music
    "Everyone is still."
    "Ama makes the first move, raising her rifle in my direction."
    "In an instant, I react."
    menu:
        "In an instant, I react."
        "Rush her.":
            "I lunge forward and grab the rifle, aiming it to the side."
            "A round fires off, sailing into the ceiling above."
            "I reach for my pistol and pull it from the holster, but Ama quickly grabs me by the side and throws me to the ground."
            "My pistol skids across the floor as I roll to a stop and look up."
        "Draw pistol.":
            "I draw my pistol."
            "Before I can fire a shot though, a bullet from Ama strikes the pistol clean through, breaking the weapon."
            amaS "Ah ah ah, can't end things too quickly, Mozely." 
    "Ama lifts the rifle to aim at me again."
    "Coil reaches his hands forward. Devices like shield generators are strapped to his palms."
    "A burst of energy suddenly blasts from them, striking Ama's rifle and rending it to pieces."
    "She takes a moment to look at the destroyed gun, then tosses it to the side."
    amaS "Well aren't you just full of surprises?"
    cS "Don't assume that I've spent my entire life cooped up in a lab."
    "Ama straightens her back and cracks her knuckles."
    "Ama charges in my direction as Coil's blasters charge."
    "But it's a feint."
    "As the energy releases, Ama doubles back, heading toward Coil, while the energy blasts sail wide of her."
    "Before Coil can move, Ama has closed the distance and swings."
    "It's a haymaker, and Coil wasn't ready."
    hide coil with Dissolve(0.3)
    "The blow is slowed by his shield, but the collision still sends Coil to the ground, sliding to a wall."
    vS "Pops!"
    "Ama draws a knife from her boot."
    amaS "Now then, Mozely. Where were we?"
    menu:
        amaS "Now then, Mozely. Where were we?"
        "I was busy killing you.":
            mS "I was in the middle of killing your sorry excuse for a hunter."
        "You were about to surrender.":
            mS "I think you were about to surrender."
    amaS "Hah! Isn't that rich?"
    "Flicking the knife back and forth, Ama steps close to me and crouches into a fighting stance."
    macS "Moze, be careful!"
    amaS "All this chaos, this mess of your own making."
    amaS "Is this what you wanted, Mozely?"
    menu:
        amaS "Is this what you wanted, Mozely?"
        "I just wanted a family.":
            mS "I just wanted a family! That's all I ever wanted."
            amaS "Good. Now you're going to watch me take it from you."
        "I just want you to shut up.":
            mS "I just want you to shut up!"
            amaS "Gladly."
    "Ama lunges with the knife."
    "I block and retaliate."
    "Lightning blows as we trade strikes."
    "It's like how we trained together years ago on her ship."
    "I see her now as I did then."
    "Fierce. Powerful. Dominant."
    "Overconfident."
    menu:
        "Overconfident."
        "Bait her into an attack.":
            "Time for a trick."
            "As she approaches  for another strike, I let my left foot slip just a tad."
            "She sees weakness, and pounces for the kill."
            "But it's a feint. I shift my weight to the side and swing my knife up toward her chest."
        "Go for an old reliable.":
            "There's an old reliable move."
            "As she approaches for another strike, I shift my weight to the side. Just slightly."
            "The blade arcs throug the air, scratching my face."
            "But now there's an opening."
            "I swing my knife up toward her chest."
    "Ama's knee slams into my jaw before I realize what happened."
    "She baited me."
    "I go tumbling across the floor."
    macS "Captain!"
    "I'm stunned, flat on my back on the ground."
    "Ama steps up to me."
    amaS "What an ungrateful child!"
    amaS "After everything I did for you, all that I taught you."
    amaS "And you just throw it away."
    amaS "Why couldn't you just listen to me!?"    
    "Ama crouches just above me, tilting her head sideways."
    "Movement slowly starts to come back to my fingers."
    amaS "Everything would have been fine. Would have been {i}good{/i}!"
    "She exhales deeply."
    amaS "Remember, Mozely: you chose this."
    "She reaches her hand into the air, knife pointed straight at my chest."
    cS "No!"
    "There's a bright streak across my vision as an energy pulse collides with Ama's chest."
    hide ama with dissolve
    amaS "Maker--you're going to regret that old man."
    "I can't turn my head but I hear the sounds of battle to my right."
    "The charge of Coil's energy pulses, the sound of Ama's fists hitting flesh."
    vS "Pops!"
    macS "Moze! Get up! Get up!"
    "Finally, I push myself into a sitting position."
    show ama stream neutral at stream_center with dissolve
    show coil stream neutral at stream_left with dissolve
    "Just in time to see Ama plunge her knife into Coil's chest."
    vS "No!"
    "Coil slumps to the ground, his back leaning against the wall."
    hide coil with Dissolve(0.6)
    "Ama holds her side. One of her arms is almost limp."
    "I stagger to my feet."
    "Behind her, I see the ruin of the BC cruiser listing toward the ground of Polaris as the star shower pummels its hull."
    amaS "Mozely. Will you do what you have to do?"
    menu:
        amaS "Mozely. Will you do what you have to do?"
        "I will do what I want.":
            $ pdEngagement += 2
            $ kcEngagement += 1
            mS "No."
            mS "I want this."
            "Ama nods."
            amaS "Good."
        "You gave me no choice.":
            $ pdEngagement -= 1
            $ kcEngagement -= 1
            mS "You didn't give me a choice."
            "Ama chuckles."
            amaS "Classic Mozely."
    amaS "Let's finish it."
    "Resolve beats through my heart."
    "I step forward."
    "Ama swings her good arm at me."
    "But she's slow now."
    "I easily dodge it and slam my fist into her chest."
    "She leans forward, then swings another fist at my head."
    "I catch it on my forearm."
    "Slamming my knee into her groin, I grab her by the back and throw her across the floor."
    "She tumbles and slams into the side of the wall."
    "I cross the room and stand over Ama."
    "Gasping for air, she leans onto her back."
    mS "Get up."
    "Ama exhales, then turns onto her stomach and pushes herself to a standing position."
    amaS "Well, kid. Looks like our time's up."
    amaS "Will you take care of my ship?"
    menu:
        amaS "Will you take care of my ship?"
        "No.":
            mS "No. I want nothing to do with you."
            "Ama nods."
            amaS "Fair."
        "You mean my ship.":
            $ deadeyeApproval
            mS "You mean {i}my{/i} ship."
            "Ama nods."
            amaS "At least you learned something."
    "Ama reaches down and pulls a blaster from her boot."
    "But I don't blink."
    "I catch her wrist in my hands, pointing the blaster to the side."
    "She fires."
    "The bolt goes wide."
    "I hold her wrist, and grip. Tight."
    "I can hear her bones cracking."
    "She drops to her knees."
    "I turn her wrist until the gun is pointed directly at her head."
    "I place my finger over the trigger."
    "She looks me straight in the eyes."
    amaS "Be seeing you, Mozely."
    "I pull the trigger."
    "Ama's body slumps to the floor."
    "Her eyes are cold. Lifeless."
    "Dead."
    hide ama with Dissolve(2.0)
    show vega stream neutral at stream_center with dissolve
    vS "Pops!"
    "The energy shield dissipates. Vega rushes to Coil's side."
    vS "No. Don't go. Don't go. Don't leave me."
    show coil at stream_left with dissolve
    "Coil opens his eyes."
    cS "It is okay, Vega."
    "Coil grips the blade with his hands and pulls it out."
    "A small spurt of blood pools in his shirt."
    cS "The blade did not cut too deep."
    "He looks to me."
    cS "Thank you for taking care of the rest."
    menu:
        cS "Thank you for taking care of the rest."
        "I didn't do it for you.":
            mS "I didn't do it for you."
            cS "I know."
        "No problem.":
            mS "It wasn't a problem."
            mS "You did well for an old man."
            cS "Hah. You know, I think I could have done better."
    "An unbearable groaning sound suddenly reverberates across Polaris."
    "We glance out the windows to watch as the hulk of the BC cruiser crumbles into flames."
    "Coil glances to the side."
    show mac stream neutral at stream_right_mac with dissolve
    "MAC still hasn't crossed into the room yet."
    "Coil nods in his direction."
    cS "Go on. He needs you."
    hide vega with dissolve
    hide coil with dissolve
    show mac at stream_center_mac with move
    "I take a step toward MAC."
    mS "MAC."
    "He turns his attention toward me."
    menu:
        "He turns his attention toward me."
        "I'm so sorry.":
            mS "MAC, I'm so sorry."
            mS "I never should have let you go."
            macS "Why did you?"
            mS "I thought it was the right thing to do."
            mS "It was a mistake."
            mS "Can you forgive me?"
        "I never thought I'd see you again.":
            mS "MAC, I never thought I'd see you again."
            macS "I didn't think I would see you again either."
            mS "Are you glad to see me."
            macS "I think so. But I am still processing the events I have witnessed."
            mS "MAC, can you ever forgive me?"
    "MAC looks down for a moment, then back up to my face."
    macS "Am I a SnakeHawk now?"
    "I smile."
    mS "Better, you're family."
    "MAC's face turns into a smile."
    macS "I'm glad to be with my family again."
    "I drop to my knees as he rushes into my arms."
    "I hold him tight and drop my face against his body."
    mS "I missed you."
    macS "I missed you too, Moze."
    "We step back and I stand up."
    show coil at stream_right with dissolve
    show vega at stream_left with dissolve
    "Coil leans against Vega as the two approach."
    vS "So, Pops, how's Moze's case for joining the Dragonflies look now?"
    if vig4_defendPolaris == True:
        cS "I would say it looks all but certain."
        cS "Captain Moze, Polaris may be in ruins, but its people will endure. In no small part thanks to your actions today."
        cS "I am sorry for the trouble I caused you earlier. I did not realize the power of the bond you share with MAC."
        cS "We all owe our gratitude to you"
        cS "You and your crew have earned your spot."
        menu:
            cS "You and your crew have earned your spot."
            "Organization isn't my style.":
                mS "I don't know. Working for organizations isn't really my style."
                cS "Of course. We can find an arragenment that is amenable to your...\"distinct\" approach."
            "Thank you.":
                mS "Thank you for the offer. After all this, my crew and I will need some sanctuary."
                cS "You shall have it."
    elif vig4_defendPolaris == False and vig4_killDflies == False:
        cS "The chances are certainly much higher now."
        cS "Although your methods are...messy, Captain Moze, without your presence, Vega and I would likely be dead."
        cS "We can offer you and your crew sanctuary while you rest and recover."
        cS "You and your crew have earned that, at least."
    else:
        cS "The carnage from this battle won't go over well with the higher-ups."
        cS "But considering we'd be dead without her, I'd say we'll have to take her on board."
        cS "At least for the time being while we all catch our breath."
    mS "And MAC?"
    "We all turn to look at him."
    macS "I do not wish to leave my family again."
    cS "You heard him."
    vS "Come on, there should be an old mercenary's empty ship somewhere in the ridge that we can commandeer."
    if macHope > macPessimism:
        macS "Wait, what about Ama?"
        mS "What about her?"
        macS "We shouldn't leave her here."
        macS "She was a Snakehawk. She deserves a proper burial."
        menu:
            macS "She was a Snakehawk. She deserves a proper burial."
            "You're right, MAC.":
                "I look back at Ama's body."
                "A chill runs down my spine."
                "But she shouldn't be left here. It's not right."
                mS "You're right, MAC."
                "I go over and lift Ama's body in my arms."
                "She's heavy. But I'm accustomed to the weight."
                "It's as if I've been carrying it for years."
    mS "Let's go."      
    "Together, MAC, Coil, Vega, and I leave the room and descend the tower."
    hide vega with dissolve
    hide coil with dissolve
    hide mac with dissolve
    hide ama
    jump vig4_epilogue_coil

label vig4_epilogue_coil():
    show shiphub_stream onlayer background with dissolve
    hide vig2_datacenter_stream    
    "The perpetual purr of space travel thrums through the ship."
    "I let my head fall back against the cushy seats behind me."
    "Finally. At long last. My muscles relax."
    pS "And to think, Ama was rolling around the galaxy in such luxury!"
    enS "I know, I always assumed her ship would be a bit more spartan."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream happy at stream_right with dissolve
    "Jennica and Teresa enter the ship's bridge."
    "They both have fresh scars, bandages, and stitches from the battle."
    pS "Hey there, Cap!"
    enS "Salutations, Captain!"
    "They make a mock salute pose."
    menu:
        "They make a mock salute pose."
        "At ease.":
            mS "At ease crew."
            mS "You deserve to relax, after what you went through."
        "Make them hold it.":
            "I don't say anything."
            "Just stare at them for almost a minute."
            pS "Do you think she'll ever let us go?"
            enS "I don't know, but I'm starting to think this joke wasn't worth it."
            "A short chuckle escapes from me."
            mS "At ease crew."
            "The pair relax."
    "They move over and sit on the couch with me."
    if jennicaRomance == True:
        $ csEngagement += 1
        "Jennica sidles up next to me and leans her head on my shoulder."
        "I take her hand in mine."
        pS "How are you feeling, Cap?"
    elif teresaRomance == True:
        $ kcEngagement += 1
        "Teresa sits down next to me and folds her legs over my lap."
        "I take her hand in mine."
        enS "How are you feeling, Captain?"
    else:
        "They both relax into the cushions on either side of me."
        pS "So, how are you feeling, Cap?"
    "How am I feeling?"
    menu:
        "How am I feeling?"
        "Exhausted.":
            mS "I'm exhausted."
            mS "I think I could sleep for a month straight."
            pS "I heard that."
            enS "I think I could go for a year in all honesty."
        "Relaxed.":
            mS "You know, I think I feel relaxed for the first time since..."
            mS "I can't remember."
            pS "Good."
            enS "You've earned it."
        "Sad.":
            mS "Honestly, I'm sad."
            enS "About Ama?"
            mS "Yeah."
            mS "I wish it didn't have to go that way."
            pS "It's a real shame, Cap."
            pS "But Ama made her choice a looong time ago."
            enS "I won't tell you not to feel sad, but a lot of people are alive now because of you."
            enS "Just, don't forget that too."
            mS "Thanks you two. I mean it."
            enS "Anytime."
            pS "We've got your back."
    pS "I will say, despite the luxury, still doesn't hold a candle to the Oakley."
    enS "No way."
    macS "I am in agreement."
    show mac stream neutral at stream_center_mac with dissolve
    macS "This ship is significantly less well stocked in terms of supplies."
    macS "And there is a distinct lack of escape pods."
    enS "Considering our previous adventures, maybe that's a good thing."
    pS "Yeah, and at least the communications array is internal. Way less likely to get screwed up."
    "MAC rolls up next to us."
    menu:
        "MAC rolls up next to us."
        "Come on up, MAC.":
            $ kcEngagement += 2
            mS "Come on, MAC, join the pile."
            macS "Are you sure, Captain?"
            macS "Will my treads not stain the couch?"
            pS "C'mon, kid, it's not even our couch!"
            enS "Yeah, join the family!"
            macS "Okay!"
            "Teresa, Jennica, and I bend down to lift MAC up."
            "We all roll back onto the couch in a pile, with MAC in the center."
            show mac stream happy
            macS "Wheeee!"
            macS "Being on the couch is fun."
            mS "It really is."
            show mac stream neutral
            "We stay in the pile for several minutes until an idea strikes me."
            mS "Actually, give me one second."
            "I slide out from the cuddle puddle and open a nearby closet."
        "Rub his head.":
            $ kcEngagement += 1
            mS "Come here, MAC."
            "I put my hand on his head and feel the vibrations thrumming through his body."
            "I feel his attention on me. It's like we're making eye contact."
            mS "You did good, MAC."
            mS "Really, really good."
            mS "I'm proud of you."
            macS "Aww, Captain. Thank you."
            pS "Yeah, kid, you kept your cool really well."
            enS "I'm impressed."
            mS "Actually, that gives me an idea."
            "I stand up from the couch and open a nearby closet."
    macS "What are you looking for, Captain."
    mS "Ama usually keeps a--AHA! Here it is!"
    "I pull down a silver bucket, set it down on the floor, and pop open the top."
    "It's red paint."
    mS "Figure we can commemorate the successful mission with MAC's first tattoo."
    macS "Really!?"
    mS "Sure. Turn around there, let me find a good spot on you."
    pS "Oh no, come on Teresa, she's gonna need some help."
    enS "I'll say. Remember when I asked her to do a tattoo for me."
    pS "The sketches were so atrocious you completely backed out hahaha."
    mS "Hey, knock it off you two, that's an order!"
    enS "Alright, alright."
    pS "So, what's it gonna be, Cap?"
    "I stare at the clear space of MAC's back panel. What image would go perfectly there?"
    menu:
        "I stare at the clear space of MAC's back panel. What image would go perfectly there?"
        "A Snakehawk.":
            $ pdEngagement += 2
            mS "I've got the perfect thing."
            "Slowly, but surely I begin tracing the outline."
            enS "I see what you're going for."
            pS "Oh no, not like that. You have to make the curve wider."
            "I put the brush down."
            mS "There, all done."
            mS "MAC, you're now the proud owner of a \"SnakeHawk\" tattoo!"
            macS "SnakeHawk!? Really!?"
        "A Dragonfly.":
            $ csEngagement += 2
            mS "I've got the perfect thing."
            "Slowly, but surely I begin tracing the outline."
            enS "I see what you're going for."
            pS "Come on, Cap, you don't want the lines to be perfectly straight."
            "I put the brush down."
            mS "There, all done."
            mS "MAC, you're now the proud owner of a \"Dragonfly\" tattoo!"
            macS "Dragonfly!? I hope they're as friendly as you all!"
        "The Oakley.":
            $ kcEngagement += 2
            mS "I've got the perfect thing."
            "Slowly, but surely I begin tracing the outline."
            enS "I see what you're going for."
            pS "It's abstract but good, Cap. You're really capturing her essence."
            "I put the brush down."
            mS "There, all done."
            mS "MAC, you're now the proud owner of the first ever \"Oakley\" tattoo!"
            macS "Oakley!? That's amazing!"
    "Without hesitation, MAC swerves around and wraps his arms around me."
    macS "Thank you, Captain."
    macS "I love you."
    pS "Oh."
    enS "Did that just happen?"
    "I lean into the hug from MAC."
    menu:
        "I lean into the hug from MAC."
        "I love you too.":
            mS "I love you too, MAC."
    "Jennica and Teresa bend down and wrap their arms around us as well."
    "Then the ship's alert system activates."
    vS "Hello, crew, we'll be coming up on the coordinates soon. Y'all should come up here."
    mS "Come on, time to see the next adventure that awaits us."
    hide mac with dissolve
    hide jennica with dissolve
    hide teresa with dissolve
    hide shiphub_stream with dissolve
    show shiphub_stream onlayer background with dissolve
    show jennica stream neutral at stream_left5 with dissolve
    show teresa stream neutral at stream_right5 with dissolve
    show coil stream neutral at stream_right with dissolve
    show vega stream neutral at stream_left with dissolve
    show mac stream neutral at stream_center_mac with dissolve
    "The four of us move up to the cockpit."
    "We're not in hyperspace anymore, just floating in the vast expanse of stars."
    enS "I don't see anything."
    pS "I'll say, looks like a whole lotta nothing."
    cS "Patience. We are exactly where we need to be."
    "A minute goes by as we scan the vastness of space."
    macS "Oh! I see it!"
    mS "See what?"
    macS "There! It was a little flicker in front of one of the stars!"
    cS "He has sharp eyes."
    mS "What do you mean?"
    vS "Just watch."
    "As I gaze into the vastness of space, I start to notice it too."
    "Some of the stars are flickering."
    "Or rather, it's as if something is passing in front of them and obscuring them for a brief moment."
    "Then it starts."
    enS "What the--?"
    "Cascading from one end of the cockpit screen to another, ripples like waves distorting the light in front of us."
    "It fades into view slowly but surely, as the ripples dissipate further and further away."
    "A massive space station, twice times the size of the Polaris moon, resolves into view."
    "Ships the size of the BC cruiser drift into open hangar bays on the side of the station."
    pS "Wow."
    hide jennica with dissolve
    "A small jolt of turbulence hits our ship."
    enS "Tractor beam."
    hide teresa with dissolve
    "Coil turns around."
    cS "Welcome to the Dragonflies."
    hide coil with dissolve
    hide vega with dissolve
    "I look down at MAC."
    menu:
        "I look down at MAC."
        "We'll face our future, together.":
            "I put a hand on his head."
            mS "Whatever's in store for us, we'll face it together. Right, MAC?"
            macS "Right, Captain Moze!"
        "Are you ready for an adventure?":
            "I put a hand on his head."
            mS "Are you ready for another adventure, MAC?"
            macS "Ready, Captain Moze!"
    hide mac with Dissolve (2.0)
    hide shiphub_stream with dissolve
    jump endgame

label vig4_epilogue_ama():
    show shiphub_stream onlayer background with dissolve
    hide vig2_datacenter_stream
    "The perpetual purr of space travel thrums through the ship."
    "I let my head fall back against the cushy seats behind me."
    "Finally. At long last. My muscles relax."
    pS "And to think, Ama was rolling around the galaxy in such luxury!"
    enS "I know, I always assumed her ship would be a bit more spartan."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream happy at stream_right with dissolve
    "Jennica and Teresa enter the ship's bridge."
    "They both have fresh scars, bandages, and stitches from the battle."
    pS "Hey there, Cap!"
    enS "Salutations, Captain!"
    "They make a mock salute pose."
    menu:
        "They make a mock salute pose."
        "At ease.":
            mS "At ease crew."
            mS "You deserve to relax, after what you went through."
        "Make them hold it.":
            "I don't say anything."
            "Just stare at them for almost a minute."
            pS "Do you think she'll ever let us go?"
            enS "I don't know, but I'm starting to think this joke wasn't worth it."
            "A short chuckle escapes from me."
            mS "At ease crew."
            "The pair relax."
    "They move over and sit on the couch with me."
    if jennicaRomance == True:
        "Jennica sidles up next to me and leans her head on my shoulder."
        "I take her hand in mine."
        pS "How are you feeling, Cap?"
    elif teresaRomance == True:
        "Teresa sits down next to me and folds her legs over my lap."
        "I take her hand in mine."
        enS "How are you feeling, Captain?"
    else:
        "They both relax into the cushions on either side of me."
        pS "So, how are you feeling, Cap?"
    "How am I feeling?"
    menu:
        "How am I feeling?"
        "Exhausted.":
            mS "I'm exhausted."
            mS "I think I could sleep for a month straight."
            pS "I heard that."
            enS "I think I could go for a year in all honesty."
        "Relaxed.":
            mS "You know, I think I feel relaxed for the first time since..."
            mS "I can't remember."
            pS "Good."
            enS "You've earned it."
        "Sad.":
            mS "Honestly, I'm sad."
            enS "About Coil?"
            mS "Yeah."
            mS "I wish it didn't have to go that way."
            pS "It's a real shame, Cap."
            pS "But he made his choice a looong time ago."
            enS "There were a lot of moments when he could have done things differently."
            enS "His path led him to this."
            mS "Thanks you two. I mean it."
            enS "Anytime."
            pS "We've got your back."
    if amaRomance == False:
        enS "You think Deadeye will be alright without her ship?"
        pS "She's resourceful. I'm sure she'll figure something out."
        mS "I was surprised she was okay with us taking it."
        pS "You gotta love personal growth."
        enS "Even if it comes a little late."
        "Jennica scans the ship's hub room."
    pS "I will say, despite the luxury, still doesn't hold a candle to the Oakley."
    enS "No way."
    macS "I am in agreement."
    show mac stream neutral at stream_center_mac with dissolve
    macS "This ship is significantly less well stocked in terms of supplies."
    macS "And there is a distinct lack of escape pods."
    enS "Considering our previous adventures, maybe that's a good thing."
    pS "Yeah, and at least the communications array is internal. Way less likely to get screwed up."
    "MAC rolls up next to us."
    menu:
        "MAC rolls up next to us."
        "Come on up, MAC.":
            $ kcEngagement += 2
            mS "Come on, MAC, join the pile."
            macS "Are you sure, Captain?"
            macS "Will my treads not stain the couch?"
            pS "C'mon, kid, it's not even our couch!"
            enS "Yeah, join the family!"
            macS "Okay!"
            "Teresa, Jennica, and I bend down to lift MAC up."
            "We all roll back onto the couch in a pile, with MAC in the center."
            show mac stream happy
            macS "Wheeee!"
            macS "Being on the couch is fun."
            mS "It really is."
            show mac stream neutral
            "We stay in the pile for several minutes until an idea strikes me."
            mS "Actually, give me one second."
            "I slide out from the cuddle puddle and open a nearby closet."
        "Rub his head.":
            $ kcEngagement += 1
            mS "Come here, MAC."
            "I put my hand on his head and feel the vibrations thrumming through his body."
            "I feel his attention on me. It's like we're making eye contact."
            mS "You did good, MAC."
            mS "Really, really good."
            mS "I'm proud of you."
            macS "Aww, Captain. Thank you."
            pS "Yeah, kid, you kept your cool really well."
            enS "I'm impressed."
            mS "Actually, that gives me an idea."
            "I stand up from the couch and open a nearby closet."
    macS "What are you looking for, Captain."
    mS "Ama usually keeps a--AHA! Here it is!"
    "I pull down a silver bucket, set it down on the floor, and pop open the top."
    "It's red paint."
    mS "Figure we can commemorate the successful mission with MAC's first tattoo."
    macS "Really!?"
    mS "Sure. Turn around there, bud, let me find a good spot on you."
    pS "Oh no, come on Teresa, she's gonna need some help."
    enS "I'll say. Remember when I asked her to do a tattoo for me."
    pS "The sketches were so atrocious you completely backed out hahaha."
    mS "Hey, knock it off you two, that's an order!"
    enS "Alright, alright."
    pS "So, what's it gonna be, Cap?"
    "I stare at the clear space of MAC's back panel. What image would go perfectly there?"
    menu:
        "I stare at the clear space of MAC's back panel. What image would go perfectly there?"
        "A Snakehawk.":
            $ pdEngagement += 2
            mS "I've got the perfect thing."
            "Slowly, but surely I begin tracing the outline."
            enS "I see what you're going for."
            pS "Oh no, not like that. You have to make the curve wider."
            "I put the brush down."
            mS "There, all done."
            mS "MAC, you're now the proud owner of a \"SnakeHawk\" tattoo!"
            macS "SnakeHawk!? Really!?"
        #third tattoo?
        "The Oakley.":
            $ kcEngagement += 2
            mS "I've got the perfect thing."
            "Slowly, but surely I begin tracing the outline."
            enS "I see what you're going for."
            pS "It's abstract but good, Cap. You're really capturing her essence."
            "I put the brush down."
            mS "There, all done."
            mS "MAC, you're now the proud owner of the first ever \"Oakley\" tattoo!"
            macS "Oakley!? That's amazing!"
    "Without hesitation, MAC swerves around and wraps his arms around me."
    macS "Thank you, Captain."
    macS "I love you."
    pS "Oh."
    enS "Did that just happen?"
    "I lean into the hug from MAC."
    menu:
        "I lean into the hug from MAC."
        "I love you.":
            mS "I love you too, MAC."
    "Jennica and Teresa bend down and wrap their arms around us as well."
    "Then the ship's alert system activates."
    if amaRomance == True:
        amaS "You all should come up here, there's something I could use some help with."
        mS "That sounds odd. Come on, let's go."
    else:
        pS "That's the contact alarm. Auto-pilot must have triggered cause a ship got in our range."
        mS "Let's go check it out."
    hide mac with dissolve
    hide jennica with dissolve
    hide teresa with dissolve
    hide shiphub_stream with dissolve
    show shiphub_stream onlayer background with dissolve
    if amaRomance == True:
        show jennica stream neutral at stream_left with dissolve
        show teresa stream neutral at stream_right with dissolve
        show ama stream neutral at stream_left5 with dissolve
        show mac stream neutral at stream__right5mac with dissolve
        "The four of us move up to the cockpit."
        if amaRomance == True:
            "I step up behind Ama's chair and reach for her hand."
            "Almost automatically, as if we've been doing it for years, she takes it."
        else:
            pass
        mS "What seems to be the trouble, Ama?"
        amaS "Does anyone else see anything funny out there?"
        "The visual in the cockpit just shows empty space."
        pS "Looks like normal space stuff to me."
        enS "Nothing out of the ordinary I can see."
        amaS "Keep looking."
        "A minute goes by as we scan the vastness of space."
        amaS "There! Did anyone see that!"
        macS "Oh! I see it!"
        mS "See what?"
        macS "It was a little flicker in front of one of the stars!"
        amaS "So I'm not going crazy."
        "As I gaze into the vastness of space, I start to notice it too."
        "Some of the stars are flickering."
        "Or rather, it's as if something is passing in front of them and obscuring them for a brief moment."
        "Then it starts."
        enS "What the--?"
        "Cascading from one end of the cockpit screen to another, ripples like waves distorting the light in front of us."
        "It fades into view slowly but surely, as the ripples dissipate further and further away."
        "A massive space station, four times the size of the Polaris moon, resolves into view."
        "Ships the size of the BC cruiser drift into open hangar bays on the side of the station."
        "Smaller ships depart the hangars."
        "They're heading in our direction."
        mS "What the hell is that!"
        amaS "Dragonfly space station. Shit!"
        "Ama jams thrusters back and frenetically starts snapping switches on control consoles."
        "We immediately turn around and start flying away from the station."
        amaS "We've got to reverse fast before they hit us with a tractor beam."
        amaS "Transferring control to co-pilot. Brown you take over flight control."
        "Jennica leaps into the co-pilot chair."
        pS "On it."
        mS "Teresa, head down to engines, make sure power is routed where we need it to go."
        enS "Aye aye, captain."
        "A tug at my sleeve."
        macS "What about me?"
        menu:
            macS "What about me?"
            "Guns.":
                mS "MAC, you and I are going to handle the guns."
                if macViolence >= macPeace:
                    "I swear, his eyes light up."
                    macS "Guns! Oh boy!"
                else:
                    macS "Understood."
        "MAC turns and rolls off toward the turret controls to the side of the cockpit."
        if amaRomance == True:
            "I move to follow, but a hand on my shoulder stops me."
            amaS "Hey."
            "We kiss. Briefly. But passionately."
            amaS "Knock 'em dead, Moze."
        else:
            pass
        hide ama with dissolve
    else:
        show jennica stream neutral at stream_left with dissolve
        show teresa stream neutral at stream_right with dissolve
        show mac stream neutral at stream__center_mac with dissolve
        "Jennica takes over control from the auto-pilot as we move up to the cockpit."
        "The visual in the cockpit just shows empty space."
        pS "Looks like normal space stuff to me."
        enS "Nothing out of the ordinary I can see."
        mS "Could it be a faulty alarm system?"
        macS "Let us wait, and observe before we jump to conclusions."
        "A minute goes by as we scan the vastness of space."
        macS "Oh! I see it!"
        mS "See what?"
        macS "It was a little flicker in front of one of the stars!"
        "As I gaze into the vastness of space, I start to notice it too."
        "Some of the stars are flickering."
        "Or rather, it's as if something is passing in front of them and obscuring them for a brief moment."
        "Then it starts."
        enS "What the--?"
        "Cascading from one end of the cockpit screen to another, ripples like waves distorting the light in front of us."
        "It fades into view slowly but surely, as the ripples dissipate further and further away."
        "A massive space station, four times the size of the Polaris moon, resolves into view."
        "Ships the size of the BC cruiser drift into open hangar bays on the side of the station."
        "Smaller ships depart the hangars."
        "They're heading in our direction."
        mS "Shit! It's the Dragonflies!"
        "Jennica jams thrusters back and frenetically starts snapping switches on control consoles."
        "We immediately turn around and start flying away from the station."
        pS "We've got to reverse fast before they hit us with a tractor beam."
        mS "Teresa, head down to engines, make sure power is routed where we need it to go."
        enS "Aye aye, captain."
        "A tug at my sleeve."
        macS "What about me?"
        menu:
            macS "What about me?"
            "Guns.":
                mS "MAC, you and I are going to handle the guns."
                if macViolence >= macPeace:
                    "I swear, his eyes light up."
                    macS "Guns! Oh boy!"
                else:
                    macS "Understood."
    "MAC turns and rolls off toward the turret controls to the side of the cockpit."
    "I follow MAC as he hops into one of the turret seats."
    "I take the position next to him."
    "We turn to each other."
    menu:
        "We turn to each other."
        "We'll face our future, together.":
            "I put a hand on his head."
            mS "Whatever's in store for us, we'll face it together. Right, MAC?"
            macS "Right, Captain Moze!"
        "Are you ready for an adventure?":
            "I put a hand on his head."
            mS "Are you ready for another adventure, MAC?"
            macS "Ready, Captain Moze!"
    "The ship lurches forward as we accelerate into space."
    hide mac with Dissolve (2.0)
    hide shiphub_stream with dissolve
    jump vig4_macro_start

label vig4_macro_start():
    $ vignette4 = True
    play music "soundtrack/postStreamGroove.wav" volume 0.8 loop fadein 2.0
    $ narrator = reg_narrator
    #$ macroNarration = True
    $ macroChoice = True
    "You lean back in your chair and let your body relax now that you're no longer on camera."
    $ renpy.sound.play("audio/ReceiveText.ogg")
    "Then you get a Loop'd notification."
    scene discordview with dissolve
    "It's from Jessie. You should see what's up."
    jump vig4_macro_mod_1

label vig4_macro_mod_1():
    $ menu = nvl_menu
    mod_nvl "Yoyoyo!"
    mod_nvl "Another great stream!"
    jump vig4_macro_webNav

label vig4_macro_webNav():
    nvl clear
    $ menu = adv_menu
    "You're about to sign off Loop'D when you get another notification."
    scene streamview with dissolve
    if csEngagement > pdEngagement and csEngagement > kcEngagement:
        "It's from Coriolis."
    elif kcEngagement > pdEngagement and kcEngagement >= csEngagement:
        "It's from KitCat."
    elif pdEngagement >= kcEngagement and pdEngagement >= csEngagement:
        "It's from PickledDragons."
    else:
        "It's from Coriolis."
    "You should see what they have to say, and check on Flinch and Blueit."
    $ screenComplete = True
    call screen webNavigation_vig4

label vig4_macro_viewerChat_1():
    $ menu = nvl_menu
    scene discordview with dissolve
    $ screenComplete = False
    $ loopdView = True
    $ menu = nvl_menu
    "This is a test for the vig4 viewerchat section."
    $ screenComplete = True
    call screen webNavigation_vig4
    scene bg black with dissolve

label FlinchAnalytics_vig4():
    $ menu = adv_menu
    $ screenComplete = False
    $ flinchView = True
    "You should probably check out Flinch's analytics page."
    $ flinchCheck = 0
    show screen webNavigation_vig4
    scene flinch_v2screen with dissolve
    if csEngagement > pdEngagement and csEngagement > kcEngagement:
        $ topfan = "Coriolis"
    elif kcEngagement > pdEngagement and kcEngagement >= csEngagement:
        $ topfan = "KitCat"
    elif pdEngagement >= kcEngagement and pdEngagement >= csEngagement:
        $ topfan = "PickledDragons"
    else:
        $ topfan = "Coriolis"
    $ followerGoal = 0
    show screen streamAnalytics_Details
    "Time to explore the Flinch analytics page."
    show screen viewership with dissolve
    $ vbar1 += viewCheck1
    $ vbar2 += viewCheck2
    $ vbar3 += viewCheck3
    $ vbar4 += viewCheck4
    $ vbar5 += viewCheck5
    $ vbar6 += viewCheck6
    $ vbar7 += viewCheck7
    $ vbar8 += viewCheck8
    $ vbar9 += viewCheck9
    $ vbar10 += viewCheck10
    show screen viewershipButton_vig4
    call screen streamAnalytics_vig4
    hide screen streamAnalytics_vig4 with dissolve

label blueitVignette4_1():
    $ menu = adv_menu
    scene blueit_v2screen at truecenter with dissolve
    $ screenComplete = False
    $ blueitView = True
    $ blueitPages = [] #this line can be deleted eventually. It's here temporarily to make testing a bit easier.
    $ blueitPages.append(vig4_bThread1)
    #$ blueitPages.append(vig3_bThread2)
    #$ blueitPages.append(vig3_bThread3)
    #$ blueitPages.append(vig3_bThread4)
    "You go to check out the subblueit to see how people are reacting to Episode 3."
    jump blueitVignette4_2

label blueitVignette4_2():
    scene blueit_v2screen at truecenter
    show screen webNavigation_vig4
    if blueitChoiceCheck == True:
        $ screenComplete = True
    else:
        pass
    call screen blueit
    return

label vig4_macro_brother_1():
    nvl clear
    $ menu = nvl_menu
    "Final test."
    jump endgame

label endgame():
    "Congratulations, you have finished Oakley 2: Settle the Score!"
    "Thank you for playing our game!"
    "On behalf of the entire team at mLab productions, we would like to say:"
    "THANK YOU!"