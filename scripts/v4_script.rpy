label vignette4Start():
    #We want to reset these before the start of the vignette
    $ menu = adv_menu
    $ viewCount = 0
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
    $ flinchView = False
    $ screenComplete = False
    $ macroChoice = True
    if vig3_outlaw >= 3 and vig2_outlawEpilogue == True:
        $ viewershipHigh = True
        $ viewershipMed = False
        $ viewershipLow = False
    elif vig3_outlaw >= 3 and vig2_outlawEpilogue == False:
        $ viewershipHigh = False
        $ viewershipMed = True
        $ viewershipLow = False
    elif vig3_outlaw >= 3 and vig2_outlawEpilogue == True:
        $ viewershipHigh = False
        $ viewershipMed = True
        $ viewershipLow = False
    elif vig3_outlaw < 3 and vig2_outlawEpilogue == True:
        $ viewershipHigh = False
        $ viewershipMed = True
        $ viewershipLow = False
    else:
        $ viewershipHigh = False
        $ viewershipMed = False
        $ viewershipLow = True
    #$ csEngagement = 0
    #$ kcEngagement = 0
    #$ pdEngagement = 0
    "It's been one week since your last stream."
    "You sit in front of your computer, about to stream the final episode of {i}Oakley 2: Settle the Score{/i}."
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
    #play music "soundtrack/vig1scratchtrack.wav" volume 1.2
    play backAudio "shipHum.wav" volume 0.6 loop fadein 1.0
    $ viewCount += 2
    $ AddChatter(vig4_sc1_comment1)
    "There is a harmonious hum to the Oakley's engines."
    $ viewCount += 4
    $ AddChatter(vig4_sc1_comment2)
    pause 0.5
    $ AddChatter(vig4_sc1_comment3) 
    "No alarms going off."
    "No rattling in the hull."
    $ AddChatter(vig4_sc1_comment4)
    "No tension in the air."
    "Just the perpetual purr of space travel."
    $ AddChatter(vig4_sc1_comment5)
    enS "That's family. There's always something wrong with you that they just have to fix."
    macS "You mean like applying thermal paste? Or rebooting faulty drivers?"
    $ AddChatter(vig4_sc1_comment6)
    $ viewCount += 2
    enS "No... well, kind of, I suppose."
    show shiphub_stream at topleft onlayer background with dissolve
    show mac stream neutral at stream_grab_mac with dissolve
    show teresa stream neutral at stream_right with dissolve
    hide ship_hallway_stream
    play audio "macAffirmative.wav" volume 1.5
    macS "I like our family."
    $ AddChatter(vig4_sc1_comment7)
    "Teresa's shoulders loosen."
    show teresa stream happy
    $ vig4_sc1_comment5.click = False
    if viewershipHigh == True:
        $ viewCount += 5
    elif viewershipMed == True:
        $ viewCount += 3
    elif viewershipLow == True:
        $ viewCount += 0
    enS "Yeah, this one's good."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc1_comment8)
    "Teresa and MAC are in the bridge. Teresa is attending to something in MAC's back panel."
    menu:
        "Teresa and MAC are in the bridge. Teresa is attending to something in MAC's back panel."
        "Head to the cockpit.":
            mS "Morning, Resa. Morning, MAC."
            "I step into the room and give the two a nod."
            play audio "macHum.wav" volume 1.5
            "MAC hums back."
            enS "Jennica's waiting for you."
            $ AddChatter(vig4_sc1_comment9alt)
            mS "Already on my way."
            "Teresa gives a casual salute."
            enS "See you both shortly."
            $ AddChatter(vig4_sc1_comment10alt)
        "Inquire about their activity.":
            mS "Morning, Resa. MAC."
            "I step into the room and give the two a nod."
            play audio "macHum.wav" volume 1.5
            "MAC hums back."
            enS "Jennica's waiting for you."
            mS "I know, I was heading there just now." 
            mS "But what are you two up to? Is everything ok?"
            macS "Teresa is improving my functionality."
            mS "Functionality?"
            $ AddChatter(vig4_sc1_comment9)
            enS "After our theatrics at the Inventor's Fair, MAC wanted to get some upgrades."
            mS "Like?"
            macS "It's a surprise."
            mS "A surprise?"
            play audio "macNeutral.wav" volume 1.5
            macS "Yes, Captain. Shall I provide a definition of \"surprise\"?"
            $ AddChatter(vig4_sc1_comment10)
            "I look from MAC to Teresa. She puts her hands in the air."
            enS "I'm no snitch."
            mS "Alright, keep your secrets."
            menu:
                mS "Alright, keep your secrets."
                "Don't go overboard, Teresa.":
                    mS "Just don't overdo it, Teresa."
                    enS "Captain, when have I ever?"
                    play audio "macPing.wav" volume 1.5
                    macS "I can recount several instances of Teresa \"overdoing it.\""
                    if customsStampede == True:
                        $ AddChatter(vig4_sc1_comment11)
                        macS "Example 1: Gibian V custo—"
                        enS "Okay, Okay, no overdoing it."
                    else:
                        enS "Listen up MAC, in this family, we don't snitch on each other."
                        if viewershipHigh == True:
                            $ AddChatter(vig4_sc1_comment12)
                        macS "\"Snitch\"? What is \"snitch\"?"
                    mS "I'll leave you two to it."
                "Hope things go smooth.":
                    mS "Be careful, we don't want any technical difficulties this late in the game."
                    enS "Don't worry, I'm not touching any critical functions."
                    macS "My optical drives have shut down. I can no longer see."
                    show teresa stream shock
                    enS "{i}What!?{/i}"
                    play audio "macPing.wav" volume 1.5
                    macS "Joking. I can see fine."
                    $ reactTarget = "vig4_sc1_macjokes"
                    show screen streamerCommentary
                    ##*streamer react moment here instead?
                    $ AddChatter(vig4_sc1_comment14)
                    show teresa stream upset
                    enS "You little—"
                    mS "I'll leave you two to it."
    jump vig4_sc1_2

label vig4_sc1_2():
    $ viewCheck1 = viewCount
    hide mac with dissolve
    hide teresa with dissolve
    show cockpit_stream at topleft onlayer background with dissolve
    hide shiphub_stream
    stop backAudio fadeout 1.0
    play music "soundtrack/vig1scratchtrack.wav" volume 1.2 fadein 1.0
    "The cockpit is significantly more clean than it was a couple weeks ago."
    if viewershipHigh == True:
        $ viewCount += 6
    elif viewershipMed == True:
        $ viewCount += 2
    hide screen streamerCommentary
    show jennica stream neutral at stream_left with dissolve
    "Jennica, relaxed but attentive, sits at the helm."
    $ AddChatter(vig4_sc1_2_comment1)
    mS "Hiya, Jennica."
    if viewershipHigh == True or viewershipMed == True:
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
            pS "Steady as she goes. No excitement since we left Solara."
            mS "Good."
            mS "And you're not holing up in this chair for days on end anymore?"
            pS "Nope. That's in the rearview now."
            mS "Happy to hear it."
            pS "Happy to feel it."
            mS "You wanted to see me?"
        "It's much cleaner in here.":
            mS "You cleaned up the place."
            $ AddChatter(vig4_sc1_2_comment3)
            pS "Wasn't me. It was Teresa."
            pS "After we left Solara I found her with a waste bag collectin' all the trash."
            pS "Felt like I caught her with her pants down haha."
            $ AddChatter(vig4_sc1_2_comment4)
            mS "You two back to normal then?"
            pS "Don't reckon I can recall what \"normal\" is after all we've been through."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc1_2_comment5)
            pS "But we're good."
            mS "Glad to hear it."
            pS "Glad to feel it."
            mS "You wanted to see me?"
    pS "Yeah, I'm about to bring us out of hyperspace."
    pS "Figured ya'd want to be here when we arrived."
    play audio "exitHyperspace.wav" volume 1.0
    "The waves of light surrounding the ship slow down as we emerge from hyperlight travel into the vastness of space."
    "A giant orb of swirling red and orange hangs in front of us."
    menu:
        "A giant orb of swirling red and orange hangs in front of us."
        "A gas giant?":
            mS "It's a gas giant? That can't be right."
        "The Dragonflies can't be human.":
            $ AddChatter(vig4_sc1_2_comment6)
            mS "Apparently the Dragonflies can breathe corrosive air?"
    pS "The coordinates ain't pointin' to the planet. It's one of the moons."
    "The screen in front of us zooms in on a small speck just to the left of the planet."
    "A read out prints onto the screen."
    "Moon: Polaris.\nAtmosphere: Artificial - Breathable.\nKey Resources: None."
    "Affiliation: N/A.\nKey Industries: None.\nPopulation: Unknown."
    mS "Not a lot of info."
    $ AddChatter(vig4_sc1_2_comment7)
    pS "Mighty convenient. Doubt whatever's there is even in BC's database."
    show teresa stream neutral at stream_right with dissolve
    show mac stream neutral at stream_center_mac with dissolve
    enS "I felt us come out of hyperspace. Have we arrived?"
    $ AddChatter(vig4_sc1_2_comment8)
    pS "Seems like it."
    enS "\"No affiliation.\" So we are in neutral territory."
    pS "Yep. Right on the border of BC and Alliance space."
    $ AddChatter(vig4_sc1_2_comment9)
    pause 0.5
    $ AddChatter(vig4_sc1_2_comment10)
    enS "And this colony is so small that neither group cares."
    show teresa stream think
    play audio "macPester.wav" volume 1.5
    macS "Po-dunk?"
    ##Could cut from here to "I'll run a scan for BigCorp signatures" - have Jennica say "maybe" - saves 20 lines
    enS "Maybe. That artificial atmosphere is intriguing though."
    menu:
        enS "Maybe. That artificial atmosphere is intriguing though."
        "What's so odd about that?":
            mS "What's so odd about an artificial atmosphere?"
            pS "I've been on rocks with 'em before. Tough to breathe at first, but ya adjust."
            enS "They're not uncommon. But the technology to produce them is expensive."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc1_2_comment11)
            else:
                $ AddChatter(vig4_sc1_2_comment11alt)
            enS "And this moon with nothing of value on it, in no strategic position whatsoever, has access to one?"
            if viewershipHigh == True:
                $ AddChatter(vig4_sc1_2_comment12)
            menu:
                enS "And this moon with nothing of value on it, in no strategic position whatsoever, has access to one?"
                "Maybe the Dragonflies are well-connected.":
                    mS "Maybe the Dragonflies have more tech than we expected."
                    enS "It is possible."
                    enS "I wouldn't rule out a trap though. We should be careful."
                    $ AddChatter(vig4_sc1_2_comment13)
                    pause 0.5
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc1_2_comment14)
                "You thinking it could be a trap?":
                    mS "You thinking it could be a trap?"
                    enS "I wouldn't rule it out. We should be careful."
                    $ AddChatter(vig4_sc1_2_comment13)
                    pause 0.5
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc1_2_comment14)
        "I'm more concerned about the \"unknown\" population.":
            mS "I'm more concerned about the \"unknown\" population."
            mS "What if there are people down there we don't want to meet?"
            $ AddChatter(vig4_sc1_2_comment11)
    pS "I'll run a scan for BigCorp signatures."
    show teresa stream neutral
    "A green line appears on screen and sweeps over the moon's landscape."
    play audio "macPing.wav" volume 1.5
    if macViolence > macPeace:
        macS "If BC is there, we can just smash 'em."
        $ AddChatter(vig4_sc1_2_comment15)
        if customsStampede == True:
            macS "Conflagrant-style."
            show teresa stream happy
            "I think I see Teresa grin out of the corner of my eye."
            show teresa stream neutral
        else:
            $ AddChatter(vig4_sc1_2_comment16)
            macS "Like we always do."
    else:
        macS "If BC is there, we can just sneak past 'em."
        $ AddChatter(vig4_sc1_2_comment17)
        if gunsBlazing == False:
            macS "Gibian V-style."
    pS "With any luck we won't have to."
    "The scan finishes."
    pS "Welp, no BC signatures. Not even a spaceport."
    show teresa stream shock
    pS "It's quieter than a Glorak's nest in matin' season."
    enS "I don't want to know how you know that."
    pS "Your loss, it's a fun story."
    show teresa stream neutral
    $ AddChatter(vig4_sc1_2_comment18)
    pS "There's just one small town."
    "The screen zooms in on a wireframe of a collection of buildings nestled into the crook of a mountain range."
    "Jennica points at a red light flashing in the center of one of the structures."
    $ AddChatter(vig4_sc1_2_comment19)
    ##could cut from here to "I want to scout out the town" - saves 10 lines
    pS "A town that those coordinates just so happen to be directin' us to."
    mS "I want to scout out the area before we bring MAC in."
    $ AddChatter(vig4_sc1_2_comment20)
    menu:
        mS "I want to scout out the town before we bring MAC in."
        "Teresa, you're with me.":
            mS "Teresa, you're with me."
            mS "We'll go in, get a lay of the land, and make contact once we're sure it's safe."
            enS "Affirmative."
            mS "Jennica, you and MAC stay with the ship. If we radio in that the situation's bad, you take off immediately."
            pS "Aye aye, Cap."
    play audio "macAlarmed.wav" volume 1.5
    show mac stream shock
    macS "Stay on the ship!?"
    if macPessimism > macHope:
        macS "But if it's a trap, you'll need reinforcements."
    else:
        macS "But I can prove to the Dragonflies that you're friendly." 
    $ vig4_sc1_2_comment20.click = False
    macS "Captain, I can help!"
    if viewershipHigh == True or viewershipMed == True:
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
            mS "No wandering off like you did in Akar."
            $ AddChatter(vig4_sc1_2_comment22)
            macS "But that was—"
            mS "Stay. On. The. Ship."
            $ AddChatter(vig4_sc1_2_comment23)
    play audio "macGrumble.wav" volume 1.5
    show mac stream neutral
    macS "I understand."
    #macS "I don't like it, but I understand."
    pS "They'll be safe, MAC. And it means more pal time for the two of us!"
    play audio "macSad.wav" volume 1.5
    "MAC hums low in response."
    "The crew turns to face me."
    menu:
        "The crew turns to face me."
        "We've come so far.":
            mS "Everyone, I know it's been a hard month."
            mS "This journey... it damn near broke us a couple of times."
            mS "But in those moments, everyone here picked each other up."
            mS "Now we're at the finish line. Just a couple more hours and we'll be in the clear."
        "Stay focused.":
            mS "Everyone, I know it's been a hard month."
            mS "But now isn't the time to relax."
            mS "We have to stay focused until the mission is complete."
            mS "So lock in and stay alert. Just a couple more hours and we'll be in the clear."
    mS "And we'll make those BC bastards choke on our trail of stardust."
    show teresa stream happy
    pS "Aye aye!"
    enS "Well said."
    mS "To your stations."
    hide jennica with dissolve
    hide teresa with dissolve
    "Jennica turns and heads up to the helm. Teresa goes to the armory to get outfitted."
    "MAC doesn't say anything."
    "As I turn around and head to my quarters, I can feel his attention on my back."
    if viewershipHigh == True:
        $ viewCount += 1 #potato is probably a high viewcount thing
        $ AddChatter(vig4_sc1_2_comment24)
    hide mac with Dissolve(1.5)
    jump vig4_sc2_1

label vig4_sc2_1():
    show polarisday_stream at topleft onlayer background with dissolve
    hide cockpit_stream
    play music "soundtrack/polaris.wav" volume 1.2
    play backAudio "bgCrowd.wav" volume 0.4 fadein 1.0
    "The activity in town is frenetic."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc1_2_comment25)
    "Dozens of people mill about the roads, carrying large boxes and sacks down the roads."
    "They don't stop as Teresa and I enter the outskirts."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc1_2_comment26)
    "But the second we step onto the roads, something makes the hair on the back of my neck stand up."
    "It's like we're being watched."
    $ AddChatter(vig4_sc2_1_comment1)
    show teresa stream neutral at stream_right with dissolve
    enS "Lots of activity."
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
    $ vig4_sc2_1_comment1.click = False
    mS "We gotta follow these crowds."
    enS "We should stay hidden and stick to the alleys if we can."
    townguy "Hello, strangers, you must be here for the star shower!"
    show townsperson stream neutral at stream_left with dissolve
    "A man with a sack of grain hanging over his left shoulder approaches Teresa and I from the alley."
    townguy "We get visitors so rarely. It's lovely to have you!"
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc2_1_comment3)
    menu:
        townguy "We get visitors so rarely. It's lovely to have you!"
        "Star shower?":
            mS "Star shower?"
            townguy "You don't know? It's the biggest astronomical happening of the decade!"
            if viewershipHigh == True:
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
                    mS "Oh, right, the \"star shower.\" I completely forgot about that."
                    with vpunch
                    "As I speak, Teresa snaps the stun rod out and jabs it into the man's neck."
                    "The sack of grain slumps to the ground, followed by his body."
                    hide townsperson stream neutral with dissolve
                    if viewershipHigh == True or viewershipMed == True:
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
                    $ reactTarget = "vig4_sc2_trustvillager"
                    show screen streamerCommentary
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
            show teresa stream upset
            enS "We appreciate the invite, but we really should make our repairs and be on our way."
            "Her hand is on a stun rod in her belt."
            menu:
                "Her hand is on a stun rod in her belt."
                "Signal Teresa to stun him":
                    $ stunGuy = True
                    $ pdEngagement += 1
                    $ outlaw += 1
                    $ engineerApproval += 1
                    show teresa stream neutral
                    "She snaps the stun rod out and jabs it into the man's neck."
                    with vpunch
                    "The sack of grain slumps to the ground, followed by his body."
                    hide townsperson stream neutral with dissolve
                    if viewershipHigh == True:
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
                    show teresa stream neutral
                    "I give Teresa the signal to stand down."
                    if viewershipHigh == True:
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
    $ vig4_sc2_1_comment8.click = False
    if viewershipHigh == True:
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
            mS "After the Vineyard, I think I've had my fill of parties."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc2_solo_comment2)
            show teresa stream happy
            enS "Couldn't agree more."
            show teresa stream neutral
    "I check the tracker. We're on the right path."
    "I glance up as we step out of the plaza."
    "A camera tilts to the side, following us. Then pans back in the other direction."
    enS "I saw it too."
    show teresa stream think
    $ AddChatter(vig4_sc2_2_comment1)
    enS "Think it could be BC?"
    mS "Maybe, but it doesn't matter."
    $ AddChatter(vig4_sc2_2_comment2)
    mS "No turning back now."
    show teresa stream neutral
    if viewershipHigh == True:
        $ AddChatter(vig4_sc2_2_comment3)
    stop backAudio fadeout 2.0
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
            hide screen streamerCommentary
        "We really shouldn't.":
            mS "Oh, we don't want to distract you from your responsibilities."
            townguy "Nonsense! It's on the way for me anyway."
            "He's out in the open, too obvious to stun him."
            mS "Well, in that case, lead on."
            "Beaming, the man turns and walks down the road."
            hide screen streamerCommentary
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc2_accompanied_comment1)
    "Teresa steps up to my side and whispers."
    show teresa stream upset
    enS "What the hell? We don't want some rube around us right now."
    $ AddChatter(vig4_sc2_1_comment8)
    mS "At least it'll help us blend in."
    enS "And if he's a BC spy?"
    "I check the scanner quckly. We're on the right path to the coordinates."
    mS "We're going the right way for now. Let's keep things calm."
    show teresa stream neutral
    "We make our way through the crowd, following our guide."
    "Without breaking step, the townsfolk we pass by look up to smile at us and tip their caps."
    "I try to smile back. But my face feels tight."
    "Everything feels tight."
    $ vig4_sc2_1_comment8.click = False
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc2_2_comment4)
    "Then we move out of the road, emerging into a wide plaza where the crowds of poeple are setting up tables, chairs, and stalls."
    "At the north end of the plaza, an immense tower stretches up into the sky. It almost feels like a church."
    "The plaza is thick with people. It's an opportunity."
    hide townsperson stream neutral with dissolve
    $ AddChatter(vig4_sc2_accompanied_comment3)
    "Teresa and I dart into an alley and out of sight."
    "We emerge from the alley onto another road."
    stop backAudio fadeout 2.0
    $ AddChatter(vig4_sc2_accompanied_comment4)
    "I check the tracker quickly, then catch movement out of the corner of my eyes."
    "A camera tilts to the side, following us. Then pans back in the other direction."
    enS "I saw it too."
    $ AddChatter(vig4_sc2_2_comment1)
    enS "Think it could be BC?"
    mS "Maybe, but it doesn't matter."
    $ AddChatter(vig4_sc2_2_comment2)
    mS "No turning back now."
    "The detour has taken us out of the way. Our pace quickens."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc2_2_comment3)
    "We have time to make up."
    jump vig2_sc2_3

label vig2_sc2_3():
    ### Could cut this exchange about MAC -- but I like it ###
    enS "Say, Captain. There's something I've been meaning to ask you about. Just haven't found the time."
    enS "Have you noticed anything changing about MAC's personality?"
    $ reactTarget = "vig4_sc2_macischanging"
    show screen streamerCommentary
    menu:
        enS "Have you noticed anything changing about MAC's personality?"
        "What do you mean?":
            mS "Changing how?"
            enS "His vocabulary and grammar."
            enS "Jennica first pointed it out to me after we left Solara."
            $ AddChatter(vig4_sc2_3_comment1)
            enS "Wanted to see what you think of it?"
            menu:
                enS "Wanted to see what you think of it?"
                "I hadn't noticed.":
                    mS "I didn't notice."
                    show teresa stream think
                    hide screen streamerCommentary
                    $ AddChatter(vig4_sc2_3_comment4)
                    enS "It's as if he's starting to talk like us."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc2_3_comment5)
                    enS "It's a little... disconcerting."
                    mS "I'll keep an eye on it."
                    $ AddChatter(vig4_sc2_3_comment6)
                "Now that you mention it...":
                    mS "Now that you mention it, yeah he is talking differently."
                    hide screen streamerCommentary
                    $ AddChatter(vig4_sc2_3_comment2)
                    show teresa stream think
                    enS "It's as if he's starting to talk like us."
                    enS "It's a little... disconcerting."
                    $ AddChatter(vig4_sc2_3_comment3)
                    menu:
                        enS "It's a little... disconcerting."
                        "We just have to get him to the Dragonflies.":
                            $ kcEngagement -= 1
                            mS "We're almost there. All we have to do is get him to the Dragonflies."
                            if viewershipHigh == True or viewershipMed == True:
                                $ AddChatter(vig4_sc2_3_comment8)
                                pause 0.5
                                $ AddChatter(vig4_sc2_3_comment9)
                            mS "They can worry about his personality after that."
                            enS "I suppose that's true."
                            if viewershipHigh == True:
                                $ AddChatter(vig4_sc2_3_comment10)
                            show teresa stream neutral
                        "I'll keep an eye on it.":
                            mS "Thanks for bringing it up. I'll keep an eye on it and talk with him about it."
                            if viewershipHigh == True or viewershipMed == True:
                                $ AddChatter(vig4_sc2_3_comment7)
                            enS "Sounds like a good idea. He responds better to you than me and Jenn."
                            show teresa stream neutral
        "Like his speech patterns?":
            mS "You mean his speech patterns?"
            mS "They're becoming less robotic."
            enS "Exactly!"
            enS "Jennica noticed it after we left Solara."
            enS "It's as if he's starting to talk like us."
            show teresa stream think
            hide screen streamerCommentary
            $ AddChatter(vig4_sc2_3_comment6)
            enS "It's a little... disconcerting."
            menu:
                enS "It's a little... disconcerting."
                "We just have to get him to the Dragonflies.":
                    $ kcEngagement -= 1
                    mS "We're almost there. All we have to do is get him to the Dragonflies."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc2_3_comment8)
                        pause 0.5
                        $ AddChatter(vig4_sc2_3_comment9)
                    mS "They can worry about his personality after that."
                    enS "I suppose that's true."
                    if viewershipHigh == True:
                        $ AddChatter(vig4_sc2_3_comment10)
                    show teresa stream neutral
                "I'll keep an eye on it.":
                    mS "Thanks for bringing it up. I'll keep an eye on it and talk with him about it."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc2_3_comment7)
                    enS "Sounds like a good idea. He responds better to you than me and Jenn."
                    show teresa stream neutral
        "He's not listening to me like he used to.":
            mS "Yeah, he's not listening to me like he used to."
            enS "That too, but I meant more subtly."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc2_3_comment11)
            enS "It's his speech patterns. They're becoming less robotic."
            enS "Jennica noticed it after we left Solara."
            enS "It's as if he's starting to talk like us."
            show teresa stream think
            $ AddChatter(vig4_sc2_3_comment6)
            enS "It's a little... disconcerting."
            menu:
                enS "It's a little... disconcerting."
                "We just have to get him to the Dragonflies.":
                    $ kcEngagement -= 1
                    mS "We're almost there. All we have to do is get him to the Dragonflies."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc2_3_comment8)
                        pause 0.5
                        $ AddChatter(vig4_sc2_3_comment9)
                    mS "They can worry about his personality after that."
                    if viewershipHigh == True:
                        $ AddChatter(vig4_sc2_3_comment10)
                    enS "I suppose that's true."
                    show teresa stream neutral
                "I'll keep an eye on it.":
                    mS "Thanks for bringing it up. I'll keep an eye on it and talk with him about it."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc2_3_comment7)
                    enS "Sounds like a good idea. He responds better to you than me and Jenn."
                    show teresa stream neutral
    "We get to the end of the road."
    "It's dead quiet."
    "No one is around. No prying eyes, no crowds of people."
    "There's not even a breeze."
    "The tracker is pointing dead ahead, at a small shop with the words \"North Star\" emblazoned on the facade."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc2_3_comment12)
    enS "This is it?"
    mS "This is it."
    enS "I was expecting... more."
    show teresa stream think
    if viewershipHigh == True or viewershipMed == True:
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
    show teresa stream neutral
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
            enS "All the same, I'd prefer not to make a hasty escape if we don't have to."
            $ AddChatter(vig4_sc2_3_comment16)
            enS "But I'll follow your lead, Captain."
    hide teresa with dissolve
    stop music fadeout 2.0
    jump vig4_sc2_4

label vig4_sc2_4():
    $ viewCheck2 = viewCount
    play audio "door.wav" volume 1.5
    show coilworkshop_stream at topleft onlayer background with dissolve
    hide polarisday_stream
    show teresa stream neutral at stream_right with dissolve
    play backAudio "jetEngines.wav" volume 0.05 fadein 2.0
    "The shop is musty and hot."
    "There's a smell of singed metal and the whir of something like an engine coming from the back."
    show coil stream neutral at stream_center with dissolve
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc2_4_comment1)
    "An old man stands at a counter, fully occupied by applying some small piece of metal to a circuit board in his hands."
    "He doesn't seem to notice us."
    if viewershipHigh == True:
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
    pause 0.5
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
            show teresa stream shock
            "I feel Teresa tense up."
            $ AddChatter(vig4_sc2_4_comment5)
            enS "How do you know about that?"
            cS "Intelligence of all kinds is my business."
            show teresa stream neutral
            $ AddChatter(vig4_sc2_4_comment6)
        "We're just passing through.":
            mS "We're just some travelers passing through. Need some repairs for our ship."
            if stunGuy == True:
                cS "Travelers who stun amicable locals?"
                $ AddChatter(vig4_sc2_4_comment7)
            else:
                cS "Travelers who abandon kind guides offering to help them?"
                $ AddChatter(vig4_sc2_4_comment8)
            show teresa stream shock
            "I feel Teresa tense up."
            $ AddChatter(vig4_sc2_4_comment5)
            enS "How do you know about that?"
            cS "Intelligence of all kinds is my business."
            show teresa stream neutral
            $ AddChatter(vig4_sc2_4_comment6)        
            mS "We're just looking for repairs, and maybe a soft bed to spend the night."
            cS "Polaris can be that. But we don't have much else."
            cS "Just dirt and stars."
            $ AddChatter(vig4_sc2_4_comment9) #Make one of these interactable??
            cS "And the beds aren't too soft either."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_4_comment10)
    "The old man removes his fingers from the circuit board and places it down on the counter."
    cS "We are a peaceful town here. And that peace is hard won from the chaos of this galaxy."
    menu:
        cS "We are a peaceful town here. And that peace is hard won from the chaos of this galaxy."
        "It seems lovely.":
            mS "It seems like a nice, quiet little slice of heaven."
            cS "And we like to keep it that way." 
        "Is it so peaceful?":
            mS "Peace is hard to come by. You don't have any troubles here?"
            cS "Only those that come from outsiders."
    enS "Is that a threat?"
    $ AddChatter(vig4_sc2_4_comment11)
    cS "It's a fact."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc2_4_comment12)
        pause 0.5
        $ AddChatter(vig4_sc2_4_comment13)
    menu:
        cS "It's a fact."
        "I think we got off on the wrong foot.":
            $ csEngagement += 1
            $ kcEngagement += 1
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
            show teresa stream upset
            enS "\"Self-interest!?\""
            "Teresa's voice reaches a fever pitch instantly."
            enS "Listen here you old coot, you have no idea what we've had to do to be standing here right now."
            $ AddChatter(vig4_sc2_4_comment15)
            enS "The friends we lost, the sacrifices we had to make."
            mS "Resa—"
            enS "No, Captain, respectfully." 
            enS "I'm not going to stand here and take a cryptic lecture from some out of touch relic."
            $ AddChatter(vig4_sc2_4_comment16)
            stop backAudio fadeout 1.0
            "The whirring from the back stops as footsteps approach."
            vS "Pops, is everything okay? I thought I heard—Oh!"
            play audio "gunCock.wav" volume 2.0
            show vega stream neutral at stream_left with dissolve
            "A young woman steps out from the back."
            $ AddChatter(vig4_sc2_4_comment17)
            show vega stream gun
            "She's aiming a blaster directly at Teresa."
            $ AddChatter(vig4_sc2_4_comment18)
            show teresa stream fight
            "In a flash, Teresa and I lift our blasters. Teresa aims at the old man while I keep my eye on the woman."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_4_comment19)
            vS "I see we have... guests?"
            cS "Nothing to worry about, Vega."
            $ AddChatter(vig4_sc2_4_comment20)
            cS "We are just having a conversation."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc2_4_comment21)
            "The old man's attention remains fixed on Teresa."
            $ AddChatter(vig4_sc2_4_comment22)
            cS "Go ahead, pull the trigger."
            enS "What!?"
            cS "My daughter will not retaliate. I promise."
            cS "Go on. Do what you do best."
            mS "Teresa, stand d—"
            play audio "lazer.wav" volume 5.0
            "A bolt fires from Teresa's blaster."
            play audio "shield.wav" volume 1.5
            "A thin veil of light sparks in front of the old man's face. The blaster bolt dissipates into the air."
            show teresa stream shock
            $ reactTarget = "vig4_sc2_coilshield"
            show screen streamerCommentary
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_4_comment23)
            cS "You should treat \"relics\" with more respect."       
        "Signal Teresa and draw your weapon.":
            $ pdEngagement += 1
            $ kcEngagement += 1
            $ outlaw += 1
            $ engineerApproval += 1
            "I give Teresa a signal under the counter."
            $ AddChatter(vig4_sc2_4_comment25)
            mS "Sounds like a threat."
            mS "And nobody threatens my crew."
            play audio "gunCock.wav" volume 2.0
            "Teresa and I both draw our blasters, and point them at the old man."
            show teresa stream fight
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_4_comment26)
            mS "Now, you're going to answer our questions, or you're going to wake up with a mean headache."
            cS "Go ahead. Shoot."
            enS "What?"
            cS "I mean it. Do what you do best."
            $ AddChatter(vig4_sc2_4_comment40)
            enS "You think we won't?"
            cS "I asked you to."
            menu:
                cS "I asked you to."
                "Shoot.":
                    $ outlaw += 1
                    play audio "lazer.wav" volume 5.0
                    "I pull the trigger on my blaster."
                    play audio "shield" volume 1.5
                    "A thin veil of light sparks in front of the old man's face. The blaster bolt dissipates into the air."
                    $ reactTarget = "vig4_sc2_coilshield"
                    show screen streamerCommentary
                    cS "And now that your blaster has failed you, will you stoop to beating an old man?"
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc2_4_comment23)
                "Tell Teresa to stand down.":
                    $ marshal += 1
                    mS "Teresa, stand d—"
                    play audio "lazer.wav" volume 5.0
                    "A bolt fires from Teresa's blaster."
                    play audio "shield" volume 1.5
                    "A thin veil of light sparks in front of the old man's face. The blaster bolt dissipates into the air."
                    show teresa stream shock
                    $ reactTarget = "vig4_sc2_coilshield"
                    show screen streamerCommentary
                    cS "Your discipline is wanting."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc2_4_comment23)
            "The whirring from the back stops as footsteps approach."
            #$ AddChatter(vig4_sc2_4_comment24)
            vS "Pops, is everything okay. I thought I heard—Oh!"
            play audio "gunCock.wav" volume 2.0
            show vega stream neutral at stream_left with dissolve
            "A young woman steps out from the back."
            $ AddChatter(vig4_sc2_4_comment27)
            show vega stream gun
            "She's aiming a shotgun directly at Teresa. I shift my blaster in her direction."
            show teresa stream fight
            vS "I see we have... guests?"
            $ AddChatter(vig4_sc2_4_comment28)
            cS "Nothing to worry about, Vega."
            $ AddChatter(vig4_sc2_4_comment29)
            cS "We are just having a conversation."
            cS "Now, where were we?"
    #hide coil with Dissolve (0.5)
    play audio "macAlarmed.wav" volume 1.5
    macS "Captain!"
    show mac stream shock at stream_right5mac
    "Suddenly the door behind us bursts open as MAC rolls into the shop."
    if macViolence > macPeace:
        play audio "lazer.wav" volume 4.0
        "His hand snaps up, and a pulse of energy shoots from an exposed hole in his arm."
        "The pulse hits the gun in the woman's hands, knocking it to the floor."
        hide screen streamerCommentary
        if viewershipHigh == True:
            $ AddChatter(vig4_sc2_4_comment30)
        show mac stream neutral
        play audio "macHum.wav" volume 1.5
        macS "Threat neutralized."
        show vega stream neutral
        show teresa stream neutral
        $ AddChatter(vig4_sc2_4_comment31)
    else:
        play audio "macEMP.wav" volume 1.5
        "His antenna glows blue and then releases a wave of light."
        show teresa stream shock
        enS "Shit!"
        "Teresa drops her blaster."
        vS "Ow, it's hot!"
        hide screen streamerCommentary
        if viewershipHigh == True:
            $ AddChatter(vig4_sc2_4_comment30)
        "The young woman drops the rifle."
        show mac stream neutral
        play audio "macHum.wav" volume 1.5
        macS "Situation deescalated."
        show vega stream neutral
        show teresa stream neutral
        $ AddChatter(vig4_sc2_4_comment31)
    ##* streamer reaction to start a MAC chant - if you do this, then later in the game we'll trigger a chant from the chat automatically. Probably on the return to Polaris alongside Moze's "speech"
    $ reactTarget = "vig4_sc2_macchant"
    show screen streamerCommentary
    show jennica stream neutral at stream_left5 with Dissolve(0.5)
    pS "Cap, I'm so sorry! I was checkin' the engine lines an' he just ran off—"
    "Jennica freezes as she recognizes the situation."
    pS "Butter my biscuit..."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc2_4_comment32)
        pause 0.5
    $ AddChatter(vig4_sc2_4_comment33)
    enS "Jenn, now's not the tim—"
    play audio "dropGun.wav" volume 1.0
    "The sound of metal dropping on the floor."
    hide jennica with dissolve
    hide vega with dissolve
    hide teresa with dissolve
    show coil at stream_left with move
    show mac at stream_right_mac with move
    #show coil at stream_center with dissolve
    "The old man's eyes have gone wide. They're locked on MAC."
    cS "At last..."
    play music "soundtrack/theme.wav" volume 0.5 fadein 2.0
    "The old man gestures to MAC."
    hide screen streamerCommentary
    cS "May I?"
    menu:
        cS "May I?"
        "First, tell us who you are.":
            $ csEngagement += 1
            mS "First, tell us who you are."
            cS "I'm your contact. The one who has been transmitting the coordinates to lead you here."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_4_comment34)
            cS "I never believed you would actually arrive."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_4_comment35)
        "If he says it's ok.":
            $ kcEngagement += 1
            "I take my aim off of the old man and signal Teresa to let him pass."
            mS "If he says it's ok."
    "He turns to MAC."
    show coil at stream_center with move
    cS "Hello, little one. It is nice to finally meet you."
    cS "I am Coil. What is your name?"
    "MAC looks from me to Teresa, to Jennica, and then back to Coil."
    play audio "macPing.wav" volume 1.5
    macS "I am MAC."
    cS "Of course you are."
    cS "And are you ok? Are you well?"
    $ AddChatter(vig4_sc2_4_comment36)
    macS "I'm with my family."
    macS "How are you, Coil? Are you well?"
    "Coil kneels down in front of MAC. He takes one of his hands in his."
    $ AddChatter(vig4_sc2_4_comment37) #I don't know about this nonsense stuff happening during this moment. But I'll put it here for now. Maybe we change it or maybe we cut it to put emphasis on the Coil and MAC stuff.
    cS "I am much better now that you're here."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc2_4_comment38)
    "Coil looks back to me."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc2_4_comment41)
    "He smiles."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc2_4_comment24)
    cS "Thank you."
    hide coil with dissolve
    hide mac with dissolve
    jump vig4_sc2_5

label vig4_sc2_5():
    $ renpy.music.set_volume(0.8, 2.0)
    show teresa stream neutral at stream_right with dissolve
    show jennica stream neutral at stream_left with dissolve
    show mac stream neutral at stream_right5mac with dissolve
    "Things are still tense for a little while."
    show vega stream neutral at stream_left5 with dissolve
    "Coil hangs up the guns, and goes to fetch some tea while Vega brings out some chairs for us."
    #hide vega with dissolve
    "Teresa doesn't start to relax her shoulders until she gets the tea in her hands."
    $ AddChatter(vig4_sc2_5_comment1)
    pS "I don't get it, why didn't ya just tell 'em who we were."
    show coil stream neutral at stream_center with dissolve
    cS "I'm afraid I did not give them much of a chance."
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
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_5_comment9)
            cS "I understand. You must have several."
    enS "Plenty."
    pS "A whole heap."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc2_5_comment10)
    cS "Ask away."
    "Jennica and Teresa turn to me."
    #hide jennica with dissolve
    #hide teresa with dissolve
    #show vega at stream_left with dissolve
    "What do I want to ask?"
    jump vig4_sc2_6

label vig4_sc2_6():
    menu:
        "What do I want to ask?"
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
                    show vega stream happy
                    vS "People who want to be free."
                    $ AddChatter(vig4_sc2_6_comment2)
                    cS "I'm sure you are all well aware how difficult it can be to get here."
                    $ reactTarget = "vig4_sc2_longjourney"
                    show screen streamerCommentary
                    cS "We keep it that way. A safehouse for the Dragonflies and for anyone else who needs a home."
                    show vega stream neutral
                    $ vig4_sc2_6_comment1.click = False
                    $ AddChatter(vig4_sc2_6_comment3)
                    pause 0.5
                    $ AddChatter(vig4_sc2_6_comment4)
                    menu:
                        cS "We keep it that way. A safehouse for the Dragonflies and for anyone else who needs a home."
                        "How did you build this?":
                            mS "How could you build this?"
                            enS "The cost of setting up the artificial atmosphere alone would be astronomical."
                            cS "You'll have to ask a man named Reynar about that."
                            show jennica stream shock
                            show teresa stream shock
                            pS "Reynar's a Dragonfly!?"
                            hide screen streamerCommentary
                            $ AddChatter(vig4_sc2_6_comment5)
                            cS "No, but he was amenable to a deal when we caught up with him fifteen years ago."
                            show vega stream happy
                            vS "We helped him with some trouble on Solara. He gave us the technology we needed."
                            $ AddChatter(vig4_sc2_6_comment6)
                            vS "That deal allowed us make this place a reality."
                            show jennica stream neutral
                            show teresa stream neutral
                            show vega stream neutral
                            if viewershipHigh == True:
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
                    show jennica stream shock
                    show teresa stream shock
                    pS "Reynar's a Dragonfly!?"
                    hide screen streamerCommentary
                    $ AddChatter(vig4_sc2_6_comment5)
                    cS "No, but he was amenable to a deal when we caught up with him fifteen years ago."
                    show vega stream happy
                    vS "We helped him with some trouble on Solara. He gave us the technology we needed."
                    $ AddChatter(vig4_sc2_6_comment6)
                    vS "That deal finally let us make this place a reality."
                    show jennica stream neutral
                    show teresa stream neutral
                    show vega stream neutral
                    $ vig4_sc2_6_comment1.click = False
                    if viewershipHigh == True:
                        $ AddChatter(vig4_sc2_6_comment7)
                    menu:
                        vS "That deal finally let us make this place a reality."
                        "So everyone in this town is a Dragonfly?":
                            mS "You mean everyone in this town is a Dragonfly?"
                            cS "Not everyone. Some of us are just people."
                            cS "Farmers, doctors, soldiers, engineers. People who are tired of BC's squeezing or the Alliance's bureaucracy."
                            show vega stream happy
                            vS "People who want to be free."
                            $ AddChatter(vig4_sc2_6_comment2)
                            cS "I'm sure you are all well aware how difficult it can be to get here."
                            $ reactTarget = "vig4_sc2_longjourney"
                            show screen streamerCommentary
                            cS "We keep it that way. A safehouse for the Dragonflies and for anyone else who needs a home."
                            show vega stream neutral
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
            hide screen streamerCommentary
            mS "So who are you two, exactly? How'd you end up here?"
            cS "Many years ago, I was a doctoral researcher studying cogitive circuitry."
            cS "During my studies, I met a colleague. Someone whose work far outstripped my own." 
            play audio "macSad.wav" volume 1.0
            macS "Elijah Vanas."
            cS "Yes, MAC. Your father."
            cS "We became... close, and started collaborating."
            $ AddChatter(vig4_sc2_6_comment8)
            cS "When we graduated, BigCorp offered us an exorbitant grant to conduct our research."
            #$ AddChatter(vig4_sc2_6_comment9)
            cS "Under the provision that they would own our work in its entirety."
            cS "I had reservations about the deal, but Elijah convinced me." 
            cS "He said we could do more good with their resources than they could do bad with our work."
            cS "Shortsighted fool."
            cS "But a shortsighted fool who I could not say \"no\" to."
            $ reactTarget = "vig4_sc2_coilbackstory"
            show screen streamerCommentary
            mS "What were the two of you working on?"
            cS "Our little friend here."
            $ AddChatter(vig4_sc2_6_comment10)
            cS "At least, I was around for the first prototypes."
            $ AddChatter(vig4_sc2_6_comment11)
            cS "It didn't take long for my conscience to get the better of me."
            cS "Complicity is how they hold us hostage. So I left."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_6_comment14)
            cS "I endeavored to convince Vanas to join me. He refused."
            "Coil suddenly gets a distant look in his eye. Like he's gazing past me."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_6_comment12)
            cS "I said some things I have regretted ever since."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_6_comment13)
            hide screen streamerCommentary
            cS "You can probably guess what happened next. I wandered the stars, lost myself in the bottle."
            "Coil turns to look at Vega."
            cS "Until I met Vega."
            cS "A young scrapper with the biggest heart and the sharpest mind I ever met."
            show vega stream happy
            vS "Oh come on, Pops, you say it the same way every time."
            cS "It only gets more true the more I say it."
            $ AddChatter(vig4_sc2_6_comment15)
            vS "I didn't really have anyone before Pops. Never knew my parents, didn't want to."
            vS "I just wanted to make things. Speeders, ship parts, rifles, shields, anything."
            $ AddChatter(vig4_sc2_6_comment16)
            vS "This old lugnut found me while I was trying to lift a nice piece of circuitry off him."
            vS "Guess he was impressed I even knew it was valuable."
            cS "I got sober that day."
            $ AddChatter(vig4_sc2_6_comment17)
            vS "And we set off to make a difference."
            "She looks to Coil."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc2_6_comment18)
            vS "Together."
            cS "Together."
            show vega stream neutral
            jump vig4_sc2_6
        "So, what's the plan?" if polarisQuestion == True and vegacoilQuestion == True:
            mS "Ok, so we've made it. What's next?"
            "Coil and Vega look at one another."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc2_6_comment19)
            cS "I'm afraid I cannot tell you in detail."
            cS "We appreciate everything that you've done."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_6_comment20)
            show vega stream happy
            vS "It means the galaxy to us."
            cS "What I can tell you, is that you arrived just in the nick of time."
            cS "Tomorrow, we will take MAC to rendezvous with the Dragonflies' headquarters."
            mS "Okay, great. We'll get our ship outfitted and ready to go at dawn."
            "Coil pauses and leans forward, locking eyes with me."
            $ AddChatter(vig4_sc2_6_comment21)
            cS "No, Captain Mozely, you do not understand."
            show vega stream neutral
            cS "We will be taking MAC. Just MAC." 
            cS "Not you and your crew."
            $ AddChatter(vig4_sc2_6_comment22)
            pause 0.5
            $ AddChatter(vig4_sc2_6_comment23)
            pause 0.3
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_6_comment24)
            $ AddChatter(vig4_sc2_6_comment25)
            pause 0.2
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_6_comment26)
            $ reactTarget = "vig4_sc2_macstays"
            show screen streamerCommentary
            show jennica stream shock
            show teresa stream shock
            enS "What!?"
            pS "You're jokin', right?"
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
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc2_6_comment27)
                    show jennica stream angry
                    show teresa stream neutral
                    pS "This family don't break up."
                    $ AddChatter(vig4_sc2_6_comment28)
                    enS "Seconded."
                    play audio "macAffirmative.wav" volume 1.5
                    macS "Thirded!"
                    $ AddChatter(vig4_sc2_6_comment29)
                    $ AddChatter(vig4_sc2_6_comment30)
                    vS "But this was the mission. You knew that when you accepted it, didn't you?"
                    hide screen streamerCommentary
                "This was always part of the plan.":
                    $ marshal += 1
                    $ csEngagement += 1
                    $ kcEngagement -= 2
                    $ pdEngagement -= 1
                    "I take a long breath."
                    "The stale atmosphere sticks in my throat. But I hold steady."
                    mS "Teresa, Jennica, this was always part of the plan, remember?"
                    mS "This was the deal when we accepted the mission."
                    if viewershipHigh == True:
                        $ AddChatter(vig4_sc2_6_comment31) 
                    show jennica stream angry
                    show teresa stream think
                    pS "Yeah, but..."
                    $ AddChatter(vig4_sc2_6_comment32)
                    enS "I guess I wanted to forget that part."
                    $ AddChatter(vig4_sc2_6_comment33)
                    hide screen streamerCommentary 
            cS "It's not up to me. Even Vanas was to be left behind if he made it this far."
            $ AddChatter(vig4_sc2_6_comment34) 
            cS "But give me a chance. I can get in touch with my superiors and make a case for you."
            $ AddChatter(vig4_sc2_6_comment35) 
            cS "After all you have been through, they might listen."
            vS "Pops can be very persuasive. Trust him."
            $ AddChatter(vig4_sc2_6_comment36) 
            cS "It will take some time to reach the Dragonflies and the festival will begin shortly."
            cS "This is a true achievement. You should go and celebrate."
            show teresa stream neutral
            show jennica stream neutral
            $ AddChatter(vig4_sc2_6_comment37) 
            cS "These days we have precious few excuses to simply enjoy life."
            "Coil stands, and reaches out a hand."
            $ AddChatter(vig4_sc2_6_comment38) 
            menu:
                "Coil stands, and reaches out a hand."
                "Shake his hand.":
                    $ csEngagement += 1
                    $ kcEngagement -= 1
                    "I stand and shake his hand."
                    "Coil nods at me."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc2_6_comment39)
                    cS "I'll do my best, I promise."
                    $ AddChatter(vig4_sc2_6_comment40)
                "Turn away.":
                    $ kcEngagement += 1
                    $ csEngagement -= 1
                    "I stand and turn to look at my crew."
                    mS "Come on, let's see what this festival is all about."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc2_6_comment41)
                    "Coil lets his hand fall and sighs." 
            cS "Vega, you go to the festival. I'll join you after making contact."
            vS "Okay, Pops."
            "Coil turns around and heads to the back of the shop."
            stop music fadeout (2.0)
            hide coil with dissolve
            hide vega with dissolve
            play music "soundtrack/festival.wav" volume 0.3 fadein 4.0
            "The sounds from outside are suddenly loud and lively."
            "Music drifts in through the windows and the cries of laughter and joy hang in the air."
            pause 0.5
            $ viewCount += 1
            $ AddChatter(vig4_sc2_6_comment42)
            pause 1.0
            $ narrator = reg_narrator
            stop music fadeout 2.0
            "What? That's Elliot's username in chat."
            "But he's supposed to be on a date with Cedric."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc2_6_comment43)
            else:
                $ AddChatter(vig4_sc2_6_comment44)
            call screen vig4_streamFreeze
            ##Will handle all the fallout that comes from Elliot entering chat in the targets script
            $ narrator = alt_narrator
            "We step outside into the cool night."
            hide teresa with dissolve
            hide jennica with dissolve
            hide mac with dissolve
    jump vig4_sc3_1

label vig4_sc3_1():
    #$ renpy.music.set_volume(0.8, 2.0)
    play music "soundtrack/festival.wav" volume 0.7
    show polarisplazanight_stream at topleft onlayer background with dissolve
    hide coilworkshop_stream
    play backAudio "crowdParty.wav" volume 0.4
    "Polaris's Star Shower festival is in full swing."
    "The plaza glows with lantern light, the sounds of raucous revelry filling the air."   
    "People sit at tables, happily drinking and eating. Some play games. Others sit on rooftops, already staring up at the sky."
    "I stand on the periphery, silently watching as MAC roves from group to group, introducing himself to new people."
    "Maybe making new friends."
    vS "Hey, Moze."
    show vega stream neutral at stream_center with dissolve
    $ AddChatter(vig4_sc3_1_comment1)
    vS "Having a good time?"
    if viewershipHigh == True or viewershipMed == True:
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
    vS "I know you're worried about what's going to happen with MAC. You have every right to be."
    show vega stream happy
    vS "But it's a festival! When was the last time you celebrated something?"
    $ AddChatter(vig4_sc3_1_comment3)
    mS "I don't know."
    vS "Then we should change that."
    vS "Come on, have some fun with the people who matter most!"
    $ AddChatter(vig4_sc3_1_comment4)
    "Maybe Vega's right. Even on Solara, we weren't really able to let our guard down."
    $ AddChatter(vig4_sc3_1_comment5)
    "I scan the festival for my crew."
    show mac stream neutral at stream_right_mac with dissolve
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
    $ viewCheck3 = viewCount
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
    show vega stream neutral
    $ vig4_sc3_2_vega_comment2.click = False
    $ AddChatter(vig4_sc3_1_comment11)
    "The stall in front of us has four toy rifles laying on a counter."
    "A group of four teens in front of us pick them up, aiming down range."
    "A wood display of Polaris stands about ten feet back."
    "The operator pushes a button and a series of cardboard cutouts begin cycling between the houses and hills."
    "Cardboard cutouts in the likeness of BigCorp enforcers, dropships, and tanks."
    "The four teens shout as they fire short sparks off in rapid succession at the targets."
    show vega stream happy
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
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc3_2_vega_comment6)
    show vega stream gun
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
    if viewershipHigh == True:
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
            $ csEngagement -= 1
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
    show vega stream happy
    vS "Thanks! That means a lot coming from you."
    "We put the toy rifles back on the counter and step aside as new players take their positions."
    jump vig4_sc3_2_vega_2

label vig4_sc3_2_vega_2():
    show vega stream neutral
    "We walk back toward the center of the plaza, but Vega stops at the periphery, looking over the crowd."
    "She isn't scanning for anything or anyone in particular. She's just taking it all in."
    "I picture the ready warrior I competed against in the carnival game."
    "Vega hasn't spent her whole life on Polaris." 
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc3_2_vega_comment14)
    "She clearly has experience with the rest of the galaxy. And with the violence that goes with it."
    "Should I say something?"
    menu:    
        "Should I say something?"
        "Do you like living here?":
            $ csEngagement += 1
            $ kcEngagement += 1
            mS "Vega, do you like living on Polaris?"
            show vega stream happy
            "She smiles, still keeping her gaze on the festival."
            vS "It has its charm."
            vS "Getting to work with Coil in peace and quiet has been a dream come true."
            $ AddChatter(vig4_sc3_2_vega_comment15)
            vS "Still, the nature of our job means I've been here, and only here, for fifteen years."
            show vega stream neutral
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
                    mS "Hopping from planet to planet all the time... it gets tough."
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
            show vega stream happy
            $ AddChatter(vig4_sc3_2_vega_comment18)
            vS "So direct! An outlaw's priority I take it."
            "She steadies herself and shrugs."
            $ AddChatter(vig4_sc3_2_vega_comment19)
            show vega stream neutral
            vS "I have, yeah. I'm not proud of it."
            mS "With the Dragonflies?"
            if viewershipHigh == True:
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
                            show vega stream happy
                            vS "How do you know? Maybe it's a boomerang bullet."
                            vS "It could be coming back around for you any second."
                            show vega stream neutral
                        "Act like you get hit.":
                            $ kcEngagement += 1
                            "I place a hand to my chest and lean my head back."
                            show vega stream happy
                            mS "Ughhhh, right in the heart."
                            vS "Like I told you. Sharp."
                            show vega stream neutral
                "Finding peace is hard.":
                    $ csEngagement += 1
                    mS "It's hard to find a place where you can leave that behind."
                    vS "True, it's why I'm grateful we're here. Even if it can get boring."
        "Don't say anything.":
            "I turn my attention to the crowd as well."
            "The twinkling lanterns, the laughter of the crowd, the smiling faces."
            "It all feels so... peaceful."
    vS "Thanks for playing the game with me, Moze."
    vS "It meant a lot to fight alongside the captain of the Oakley, even if it was just pretend."
    $ AddChatter(vig4_sc3_2_vega_comment25)
    ##* Streamer reaction to muse about what Moze's nickname would be
    menu:
        vS "It meant a lot to fight alongside the captain of the Oakley, even if it was just pretend."
        "I enjoyed it too.":
            mS "I appreciate that. And I enjoyed fighting alongside a Dragonfly."
            show vega stream happy
            "Vega smiles and blushes."
        "Think about joining us?":
            $ kcEngagement += 1
            $ pdEngagement += 1
            $ csEngagement += 1
            mS "What do you think about joining us? The Oakley always has room for a sharp new recruit."
            $ AddChatter(vig4_sc3_2_vega_comment26)
            "Vega's eyes go wide for an instant."
            show vega stream happy
            vS "Bahahaha!"
            "Then she doubles over, laughing."
            vS "Sorry, sorry, it just took me a second to realize that you're serious."
            "She glances back at the heart of the festival."
            vS "You know, if I was younger, I would have said 'yes' in a heartbeat."
            vS "I'm flattered. Deeply. But I'm going to have to politely decline."
            $ AddChatter(vig4_sc3_2_vega_comment27)
            show vega stream neutral
            vS "My place is with Coil and the Dragonflies. I'm sure you understand."
            mS "Of course. Figured I'd extend the invite."
            $ AddChatter(vig4_sc3_2_vega_comment28)
            vS "And it is very much appreciated."
    vS "You should probably go check in with your crew, Coil might have news."
    show vega stream neutral
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
    if viewershipHigh == True or viewershipMed == True:
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
            pS "Oh jeez! Howdy, Cap, how—how's your evenin'?"
        "Clear throat.":
            mS "Uhem."
            "As I clear my throat, Jennica snaps to attention."
            pS "Oh, sir! I mean, Cap! You're look—How's your evenin', Moz—Cap?"
    mS "You ok, Jenn? You're looking a bit obsessed with that screen."
    pS "Yeah, I'm fine, Cap. It's just—"
    pS "Ya wouldn't happen to recognize this game, would you?"
    $ AddChatter(vig4_sc3_2_jenn_comment4)
    menu:
        pS "Ya wouldn't happen to recognize this game, would you?"
        "I've never played a video game before.":
            $ pdEngagement += 1
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_2_jenn_comment5)
            mS "Jenn, you know I've never touched one of these things before."
            pS "Yeah, but this one's special."
            pS "This is {i}Star Battler IV: Destructostar{i}."
        "Of course!":
            $ kcEngagement += 1
            mS "Of course I recognize it. It's {i}Star Battler IV: Destructostar{i}."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_2_jenn_comment5)
            pS "Yep! I'm kinda surprised you knew that, Cap."
    pS "It's a classic. Used to play on a machine back in my hometown when I was just a kid."
    pS "No jokes, this game taught me to be a pilot."
    $ AddChatter(vig4_sc3_2_jenn_comment6)
    pS "Never thought I'd see one again."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc3_2_jenn_comment7)
    menu:
        pS "Never thought I'd see one again."
        "Alright, let's do this.":
            mS "Alright then, grab that controller and let's do this."
            "I step up to the game and grab the controller on the right."
    pS "Cap, ya can't be serious."
    pS "I've spent hundreds of hours on this game. Plus, I'm a {i}professional{/i} pilot."
    menu:
        pS "I've spent hundreds of hours on this game. Plus, I'm a {i}professional{/i} pilot."
        "Sounds like an excuse.":
            mS "Is that the excuse you're gonna tell yourself after I beat you at this game."
            pS "Oh, that does it."
            $ AddChatter(vig4_sc3_2_jenn_comment8)
            pS "I was gonna take it easy, but ya had to ask for some tough love."
        "You're forgetting I used to be a pilot too.":
            mS "Sure, but you're forgetting that I was a pilot before I was a captain."
            mS "Grab your flight stick and let's make this happen."
            pS "Alright, you're on."
            $ AddChatter(vig4_sc3_2_jenn_comment8)
    mS "Bring it, Brown."
    pS "Already brought, Cap."
    show jennica stream neutral at stream_left with move
    "We press the start button on our respective controllers."
    "The screen fades into a field of stars."
    "Narration describes the \"Destructostar\" tournament, a battle across the galaxy to discover the number one starship pilot."
    "Then the game begins."
    "I have to destroy Jennica's ship before she destroys mine."
    "My ship is equipped with photon cannons, heavy missiles, and blast wave charges."
    "Should be simple enough."
    pS "Takin' too long to figure out the controls."
    "The radar on the side of the screen shows a blip barreling down at me. Jennica is playing this aggressively."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc3_2_jenn_comment9)
    menu:
        "The radar on the side of the screen shows a blip barreling down at me. Jennica is playing this aggressively."
        "Dodge the incoming attack.":
            $ AddChatter(vig4_sc3_2_jenn_comment10)
            "It's a bad spot, I have to pull away and find a better position to return fire."
            pS "On your ass, Cap."
            $ AddChatter(vig4_sc3_2_jenn_comment11)
            "Jennica is still putting pressure on me."
            menu:
                "Jennica is still putting pressure on me."
                "Drop a blast charge.":
                    mS "Don't get too close."
                    "I drop a blast wave charge, detonating it behind my ship."
                    pS "Shit!"
                    $ AddChatter(vig4_sc3_2_jenn_comment12)
                    "Jennica has to peel off from the pursuit."
                    "I pull up and see Jennica moving away."
                    $ AddChatter(vig4_sc3_2_jenn_comment13)
                    $ AddChatter(vig4_sc3_2_jenn_comment14)
                    menu:
                        "I pull up and see Jennica moving away."
                        "Make an aggressive attack.":
                            $ kcEngagement -= 1
                            $ csEngagement -= 1
                            "Pressing my advantage, I drive my ship onto her tail as she drops into a barrel roll."
                            pS "Damn, Cap, looks like ya got me."
                            mS "Only a matter of time."
                            pS "Too bad looks can be deceivin'."
                            "As the words escape her mouth, I see it out of the corner of my eye."
                            "Delayed blast charges. They're all around my ship."
                            $ AddChatter(vig4_sc3_2_jenn_comment15)
                            mS "Oh damn it."
                            "Jennica pushes a button on the side of her controller."
                            "The charges around me detonate and my screen goes completely white."
                            $ AddChatter(vig4_sc3_2_jenn_comment16)
                            "\"Player One Wins\" flashes across both game screens."
                            $ reactTarget = "vig4_sc3_jenndatelose"
                            show screen streamerCommentary
                            pS "Ooooh yeah! Just how I drew it up!"
                            pS "Ya made me sweat a bit. But I was locked in the whole time."
                            $ AddChatter(vig4_sc3_2_jenn_comment17)
                            mS "You're one hell of a pilot, Jenn."
                            "I extend my hand toward her."
                            if viewershipHigh == True or viewershipMed == True:
                                $ AddChatter(vig4_sc3_2_jenn_comment18)
                            "She shakes it firmly."
                            pS "Thanks, Cap. It was a good game."
                            hide screen streamerCommentary
                            $ AddChatter(vig4_sc3_2_jenn_comment19)
                            mS "It was. Well played."
                        "Get ahead and set a trap.":
                            $ kcEngagement += 1
                            $ csEngagement += 2
                            $ pilotApproval += 1
                            "I push my ship forward, trying to get ahead of Jennica."
                            pS "Oh, I see what you're going for."
                            "She starts performing various maneuvers, but every time she makes a move, she just makes it easier for me to overtake her."
                            $ AddChatter(vig4_sc3_2_jenn_comment20)
                            "I see my chance."
                            "I activate the extra boost on my ship, and thrust ahead of her ship, letting a blast charge slip just as I do so."
                            $ AddChatter(vig4_sc3_2_jenn_comment21)
                            pS "Shit!"
                            "The charge falls alongside Jennica's ship, then detonates."
                            "Her screen goes completely white."
                            "\"Player Two Wins\" flashes across both game screens."
                            $ AddChatter(vig4_sc3_2_jenn_comment22)
                            $ reactTarget = "vig4_sc3_jenndatewin"
                            show screen streamerCommentary
                            pS "Ahhh no way!"
                            pS "I had the time delay blast charges too."
                            pS "I just needed ya to get a bit more greedy."
                            mS "And I just needed you to wear yourself out."
                            "Jennica lets out a sigh."
                            pS "Yeah, guess I got a little cute at the end there."
                            $ AddChatter(vig4_sc3_2_jenn_comment18)
                            "She extends a hand toward me."
                            pS "Well played."
                            hide screen streamerCommentary
                            $ AddChatter(vig4_sc3_2_jenn_comment19)
                            "I shake it firmly."
                            mS "Good game."
                "Evasive maneuvers.":
                    "I corkscrew around a handful of asteroids."
                    pS "Pretty good moves, Cap."
                    mS "I learned from the best."
                    $ AddChatter(vig4_sc3_2_jenn_comment12)
                    "Peeling up out of the corkscrew, Jennica and I are heading directly toward each other."
                    $ AddChatter(vig4_sc3_2_jenn_comment13)
                    $ AddChatter(vig4_sc3_2_jenn_comment14)
                    menu:
                        "Peeling up out of the corkscrew, Jennica and I are heading directly toward each other."
                        "Head on attack.":
                            $ csEngagement += 2
                            $ pdEngagement += 1
                            $ kcEngagement -= 2
                            $ pilotApproval += 1
                            "Pushing my thrusters full throttle, I lay on the guns."
                            pS "Oh, so we're doin' it this way?"
                            if viewershipHigh == True or viewershipMed == True:
                                $ AddChatter(vig4_sc3_2_jenn_comment23)
                            mS "You know it!"
                            "Jennica lays on her throttle too."
                            "Our shields are ripped to shreds. It's just our hulls, hurtling toward one another."
                            "The ships collide. The screen goes white."
                            "\"Tie Game\" flashes across both game screens."
                            $ AddChatter(vig4_sc3_2_jenn_comment24)
                            $ reactTarget = "vig4_sc3_jenndatetie"
                            show screen streamerCommentary
                            pS "Hahaha, that's an appropriate way for it to go."
                            $ AddChatter(vig4_sc3_2_jenn_comment25)
                            "Jennica reaches out a hand to me."
                            "I take it and shake it firmly."
                            $ AddChatter(vig4_sc3_2_jenn_comment26)
                            mS "Good game."
                            hide screen streamerCommentary
                            $ AddChatter(vig4_sc3_2_jenn_comment19)
                            pS "Yeah, well played."
                        "Bait her in.":
                            $ kcEngagement -= 1
                            $ csEngagement -= 1
                            "I turn my ship around and try to bait her in."
                            pS "Runnin' scared, Cap?"
                            if viewershipHigh == True or viewershipMed == True:
                                $ AddChatter(vig4_sc3_2_jenn_comment27)
                            mS "Just waiting for my moment."
                            pS "Spoken like a scaredy cat."
                            "She executes the maneuver before I realize what's happening."
                            "Jennica drops a blast wave charge, and then jams her ship's steering hard so that the ship spins in a perfect circle."
                            "All I can do is watch as her ship's back end slams into the charge, sending it flying through the void of space."
                            $ AddChatter(vig4_sc3_2_jenn_comment28)
                            "Directly at me."
                            "The charge detonates, and my screen goes completely white."
                            "\"Player One Wins\" flashes across both game screens."
                            $ AddChatter(vig4_sc3_2_jenn_comment29)
                            $ reactTarget = "vig4_sc3_jenndatelose"
                            show screen streamerCommentary
                            pS "Ooooh yeah! Just how I drew it up!"
                            mS "Damn! You're one hell of a pilot, Jenn."
                            $ AddChatter(vig4_sc3_2_jenn_comment30)
                            "I extend my hand toward her."
                            "She shakes it firmly."
                            if viewershipHigh == True or viewershipMed == True:
                                $ AddChatter(vig4_sc3_2_jenn_comment18)
                            pS "Ya ain't so bad yourself. Maybe ya should take the helm next time we're in a tight spot."
                            mS "Think I'll stick to the games for now."
                            hide screen streamerCommentary
                            $ AddChatter(vig4_sc3_2_jenn_comment19)
                            pS "Hahaha alright. It was a good game."
                            mS "It was. Well played."
        "Return fire.":
            "It's a bad spot, but I pull up and face her directly."
            $ AddChatter(vig4_sc3_2_jenn_comment10)
            "Her shots shred my shields, but I manage to land some hits on her too."
            $ AddChatter(vig4_sc3_2_jenn_comment11)
            pS "Bold move, not afraid to take some hits, I see."
            "My shields are low, but she's taken some hits too. I'm at a disadvantageous position."
            $ AddChatter(vig4_sc3_2_jenn_comment13)
            $ AddChatter(vig4_sc3_2_jenn_comment14)
            menu:
                "My shields are low, but she's taken some hits too. I'm at a disadvantageous position."
                "Head on attack.":
                    $ csEngagement += 2
                    $ pdEngagement += 1
                    $ kcEngagement -= 2
                    $ pilotApproval += 1
                    "Pushing my thrusters full throttle, I lay on the guns."
                    show jennica stream shock
                    pS "Oh, so we're doin' it this way?"
                    mS "You know it!"
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc3_2_jenn_comment23)
                    "Jennica lays on her throttle too."
                    show jennica stream neutral
                    "Our shields are ripped to shreds. It's just our hulls, hurtling toward one another."
                    "The ships collide. The screen goes white."
                    "\"Tie Game\" flashes across both game screens."
                    $ AddChatter(vig4_sc3_2_jenn_comment24)
                    $ reactTarget = "vig4_sc3_jenndatetie"
                    show screen streamerCommentary
                    pS "Hahaha, that's an appropriate way for it to go."
                    $ AddChatter(vig4_sc3_2_jenn_comment25)
                    "Jennica reaches out a hand to me."
                    "I take it and shake it firmly."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc3_2_jenn_comment18)
                    mS "Good game."
                    hide screen streamerCommentary
                    $ AddChatter(vig4_sc3_2_jenn_comment19)
                    pS "Yeah, well played."
                "Bait her in.":
                    $ kcEngagement -= 1
                    $ csEngagement -= 1
                    "I turn my ship around and try to bait her in."
                    pS "Runnin' scared, Cap?"
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc3_2_jenn_comment27)
                    mS "Just waiting for my moment."
                    pS "Spoken like a scaredy cat."
                    "She executes the maneuver before I realize what's happening."
                    "Jennica drops a blast wave charge, and then jams her ship's steering hard so that the ship spins in a perfect circle."
                    "All I can do is watch as her ship's back end slams into the charge, sending it flying through the void of space."
                    $ AddChatter(vig4_sc3_2_jenn_comment28)
                    "Directly at me."
                    "The charge detonates, and my screen goes completely white."
                    "\"Player One Wins\" flashes across both game screens."
                    $ AddChatter(vig4_sc3_2_jenn_comment29)
                    $ reactTarget = "vig4_sc3_jenndatelose"
                    show screen streamerCommentary
                    pS "Ooooh yeah! Just how I drew it up!"
                    mS "Like I say back on the Oakley: you're one hell of a pilot, Jenn."
                    $ AddChatter(vig4_sc3_2_jenn_comment30)
                    "I extend my hand toward her."
                    "She shakes it firmly."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc3_2_jenn_comment18)
                    pS "Ya ain't so bad yourself. Maybe ya should take the helm next time we're in a tight spot."
                    hide screen streamerCommentary
                    $ AddChatter(vig4_sc3_2_jenn_comment19)
                    mS "Think I'll stick to the games for now."
                    pS "Hahaha alright. It was a good game."
                    mS "It was. Well played."
    jump vig4_sc3_2_jennica_2

label vig4_sc3_2_jennica_2():
    "The screen goes back to its repetitive trailer montage as we step back into the plaza."
    pS "Well that was a trip down memory lane. I need a sec to catch my breath."
    "Jennica steps to the side of the store and leans back against the wall."
    "We're both quiet for sometime."
    pS "Did I ever tell ya what made me want to become a pilot?"
    menu:
        pS "Did I ever tell ya what made me want to become a pilot?"
        "I don't think so.":
            mS "I don't think it ever came up, actually."
        "To get off of your home world, right?":
            $ pilotApproval += 1
            mS "I think so."
            mS "It was to get off your home world, right?"
            pS "That was part of it."
            pS "But I meant like, the {i}thing{/i} that inspired me."
    pS "What really sealed it was this guy who came to my school when I was a young 'un."
    pS "He was some pilot for BigCorp, doin' a mentorship program kinda thing. I think he was a cop."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc3_2_jenn_comment31)
    pS "He came into my class and asked who wanted to be a pilot. So I raised my hand."
    "Jennica looks up toward the plaza. It's like she's looking at something much further away."
    show jennica stream angry
    pS "Bastard took one look at me and laughed."
    pS "Didn't have the implants yet, so he just saw this scrawny kid with degenerative eyesight."
    pS "I'll never forget what he said: \"Not one in a billion chance you could ever be a pilot.\""
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc3_2_jenn_comment32)
    "Jennica clenches her fist."
    $ AddChatter(vig4_sc3_2_jenn_comment33)
    show jennica stream crossed
    pS "I made it. It wasn't handed to me, it didn't just happen. I worked my ass off."
    pS "And I'm a damn good pilot now. His words shouldn't matter."
    pS "But whenever I remember what he said, all I want to do is go back in time and kick that guy's ass."
    show jennica stream neutral
    "Jennica's whole body relaxes."
    "She looks to me and our eyes lock."
    $ AddChatter(vig4_sc3_2_jenn_comment34)
    menu:
        "She looks to me and our eyes lock."
        "You're so incredible, Jenn.":
            mS "Jenn, you're so incredible."
            show jennica stream shock
            "She blushes and looks away briefly before turning back to me."
            $ AddChatter(vig4_sc3_2_jenn_comment39)
            show jennica stream neutral
            pS "Thanks, Cap."
            mS "No I really mean it. You've achieved amazing things." 
            mS "There's no one I could possibly trust more at the helm of the Oakley."
            if pilotApproval > 4:
                "Jennica slides a bit closer to me."
            pS "Good, cause there's no one I would want watchin' my back more than you."
            $ AddChatter(vig4_sc3_2_jenn_comment40)
            menu:
                pS "Good, cause there's no one I would want watchin' my back more than you."
                "Jenn, I love you." if teresaRomance == False:
                    mS "Jenn, it's taken me a long time to realize this. Probably too long."
                    pS "Realize what, Cap?"
                    mS "I love you."
                    $ AddChatter(vig4_sc3_2_jenn_comment41)
                    if pilotApproval > 4:
                        $ kcEngagement -= 2
                        $ csEngagement += 3
                        $ pdEngagement -= 1
                        $ jennicaRomance = True
                        show jennica stream shock
                        pS "Oh!"
                        "Jennica's face goes entirely red."
                        pS "Wow, I, uh, wasn't expectin' that."
                        mS "In a bad way?"
                        pS "Nononono, in a good way. In the best possible way."
                        pS "I uh, I think that—why is this so hard!?"
                        menu:
                            pS "I uh, I think that—why is this so hard!?"
                            "Kiss her.":
                                "I put a finger to her lips."
                                mS "Shhhh"
                                mS "You don't have to say it."
                                "She freezes completely still, her eyes locked on mine."
                                "I move forward and kiss Jennica."
                                show jennica stream neutral
                                $ AddChatter(vig4_sc3_2_jenn_comment42)
                            "Wait for her.":
                                "I wait, patiently."
                                "Jennica meets my eyes."
                                "We hold each other's gaze."
                                pS "I love you too, Moze."
                                "I feel myself smiling before I even consciously do it myself."
                                "I move forward and kiss Jennica."
                                show jennica stream neutral
                        $ AddChatter(vig4_sc3_2_jenn_comment42)
                        $ reactTarget = "vig4_sc3_jenndatekiss"
                        show screen streamerCommentary
                        "Our arms wrap around each other, holding one another tightly."
                        "It feels good. To hold and be held. Like we could stay here for hours, days, longer even."
                        $ AddChatter(vig4_sc3_2_jenn_comment43)
                        "Finally, our lips part. We stare into each other's eyes."
                        if viewershipHigh == True or viewershipMed == True:
                            $ AddChatter(vig4_sc3_2_jenn_comment44)
                        pS "Now the problem is I don't wanna let go."
                        mS "Me neither."
                        $ AddChatter(vig4_sc3_2_jenn_comment45)
                        mS "But I should go check and see if Coil has any news."
                        mS "We'll have more time."
                        pS "Yes, lots of time."
                        "It's hard to let go, but somewhow we manage."
                        "I take a step toward the plaza and sneak a glance back at Jennica."
                        "She's leaning against the wall, looking up at the stars, with a massive smile on her face."
                        $ AddChatter(vig4_sc3_2_jenn_comment46)
                        "I smile to myself as I return to the festival."
                        hide screen streamerCommentary
                        hide jennica with dissolve
                    else:
                        $ kcEngagement += 1
                        $ csEngagement -= 1
                        $ pdEngagement += 1
                        show jennica stream shock
                        pS "Oh, that's not what I was expectin'."
                        "My heart drops."
                        mS "What do you mean?"
                        "Jennica looks at the ground, then back up to me."
                        $ AddChatter(vig4_sc3_2_jenn_comment47)
                        pS "I don't really know how to respond."
                        $ AddChatter(vig4_sc3_2_jenn_comment48)
                        mS "So, you don't feel the same?"
                        $ AddChatter(vig4_sc3_2_jenn_comment49)
                        "Jennica takes a long moment. She looks deeply into my eyes."
                        show jennica stream neutral
                        pS "Sorry, Cap, but I don't."
                        if viewershipHigh == True or viewershipMed == True:
                            $ AddChatter(vig4_sc3_2_jenn_comment50)
                        pS "You've always felt like a big sister to me."
                        $ AddChatter(vig4_sc3_2_jenn_comment51)
                        $ reactTarget = "vig4_sc3_jenndaterejection"
                        show screen streamerCommentary
                        mS "Okay..."
                        pS "..."
                        mS "..."
                        pS "..."
                        mS "Well this is awkward."
                        $ AddChatter(vig4_sc3_2_jenn_comment52)
                        pS "Yeah."
                        $ AddChatter(vig4_sc3_2_jenn_comment53)
                        pS "Look I really care about ya, Cap."
                        pS "But it doesn't feel right to me."
                        $ AddChatter(vig4_sc3_2_jenn_comment54)
                        mS "No, I get it. I'm glad you were honest with me."
                        pS "Always."
                        mS "I should check on the party. Maybe Coil has some updates."
                        $ AddChatter(vig4_sc3_2_jenn_comment55)
                        pS "Of course. Let me know as soon as ya got any news."
                        mS "Will do."
                        $ AddChatter(vig4_sc3_2_jenn_comment56)
                        pause 0.5
                        $ AddChatter(vig4_sc3_2_jenn_comment57)
                        "The two of us hug, awkwardly, then I step away back to the center of the plaza."
                        hide screen streamerCommentary
                        hide jennica with dissolve
                "Let's get back to the party.":
                    $ csEngagement -= 2
                    $ pdEngagement -= 1 #PickledDragons probably doesn't respect starting to go for the romance and then backing out
                    mS "I should check on the party. Maybe Coil has some updates."
                    $ AddChatter(vig4_sc3_2_jenn_comment35)
                    show jennica stream shock
                    "Jennica freezes for a moment."
                    $ AddChatter(vig4_sc3_2_jenn_comment36)
                    "Then she stands up from the wall."
                    show jennica stream neutral
                    pS "Yeah, of course, that makes sense."
                    $ AddChatter(vig4_sc3_2_jenn_comment37)
                    "I step back toward the plaza when Jennica calls out."
                    pS "Hey, Cap, thanks for the game. I really needed it."
                    mS "No problem, Jenn."
                    $ AddChatter(vig4_sc3_2_jenn_comment38)
                    "The two of us hug, then I step away back to the center of the plaza."
                    hide jennica with dissolve
        "Screw that guy.":
            $ csEngagement -= 2
            $ kcEngagement += 1
            mS "Screw that guy. He's probably dead now anyway."
            $ AddChatter(vig4_sc3_2_jenn_comment35)
            pS "Bahahaha"
            $ AddChatter(vig4_sc3_2_jenn_comment36)
            pS "Yeah, probably blew up in an asteroid belt crash or something."
            pS "Asshole."
            $ AddChatter(vig4_sc3_2_jenn_comment37)
            pS "Thanks, Cap. I needed this."
            mS "No problem, Jenn."
            $ AddChatter(vig4_sc3_2_jenn_comment38)
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
    "She and three other people are watching each other intently, holding upside down cups."
    "The one sitting on Teresa's left throws a small bunch of credits on the table and stands up."
    $ AddChatter(vig4_sc3_1_comment11)
    townguy "Damn it!"
    show teresa stream happy
    "Teresa shrugs."
    enS "You should've called."
    townguy "Apparently. I'm out. Getting too rich for my blood."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc3_2_resa_comment4)
    "As the man leaves, Teresa glances up at me."
    enS "Oh Captain, perfect timing! Want to join for a game?"
    mS "Sure."
    "I take a seat."
    mS "But I don't really know what's going on here."
    enS "It's called Liar's Dice."
    $ AddChatter(vig4_sc3_2_resa_comment5)
    enS "We all have five dice that we roll underneath our cups. We can look at our own cups at any time."
    enS "Then, one person identifies how many of one number they think are under all the cups."
    enS "The next person can increase the number, or \"call\" to make everyone reveal their dice."
    enS "We tally up all the dice of that one number, and if there are fewer than the amount that was called, then the person who called wins."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc3_2_resa_comment6)
    enS "You'll pick it up as you go."
    enS "First, take all those dice, mix them up in the cup, and then slam it back on the table."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc3_2_resa_comment7)
    "The wooden cup makes a deep \"{b}THUNK{/b}\" as the dice rattle around underneath."
    "I look under my cup: There are two 2's, two 4's, and one 6."
    "The person opposite me starts."
    diceP1 "Three 4's."
    diceP2 "Only three, come on Alex, that's not even a real bet!"
    diceP1 "She's running the table with us, Adam, what do want me to do?"
    $ AddChatter(vig4_sc3_2_resa_comment8)
    diceP2 "Not let her get in your head!"
    "Teresa glances at me and grins."
    $ AddChatter(vig4_sc3_2_resa_comment9)
    diceP2 "You know what, let's make this interesting, six 4's."
    $ AddChatter(vig4_sc3_2_resa_comment10)
    enS "You're turn, Captain. What'll it be? Call or Raise?"
    $ AddChatter(vig4_sc3_2_resa_comment11)
    menu:
        "I look under my cup: There are two 2's, two 4's, and one 6."
        "Call.":
            mS "Why not. I'll call."
            "Each player at the table raises their cup."
            "I have two 4's. The first player also has two. The one next to me has one."
            "But Teresa has four."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_2_resa_comment12)
            enS "Nine 4's. Tough, Captain. We could've gone a bit longer."
            "I toss a small stack of credits onto the table. The man next to me picks them up."
            mS "I'm just warming up."
            $ AddChatter(vig4_sc3_2_resa_comment13)
            diceP1 "Of course."
            diceP2 "That's what we said when your friend first sat down here."
            "Teresa winks at me."
            enS "You'll get it."
        "Raise.":
            mS "Seven 4's."
            enS "Eight 4's."
            $ AddChatter(vig4_sc3_2_resa_comment14)
            "Teresa didn't even check under her cup."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_2_resa_comment16)
                pause 0.5
            $ AddChatter(vig4_sc3_2_resa_comment15)
            "The man who started the bidding looks under his cup."
            "It seems like sweat is starting to form on his brow."
            diceP1 "Call!"
            "We all lift our cups."
            "I have two 4's. The first player also has two. The one next to me has one."
            "But Teresa has four."
            $ AddChatter(vig4_sc3_2_resa_comment17)
            enS "Nine 4's. Tough position, reasonable call."
            diceP1 "Yeah, yeah."
            "The losing player takes out a small stack of credits and puts them on the table."
            "Teresa gleefully picks them up."
    enS "Alright, next round. I start."
    "We sit at the table for several more rounds."
    "The back and forth continues as I start to get a handle on the game."
    "I win some, I lose some."
    "Then Teresa picks up her cup with a bit more of a flourish."
    enS "Alright, gang, I think this is my last round."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc3_2_resa_comment18)
    diceP1 "Me too."
    diceP2 "Same."
    mS "Winner take all then?"
    if viewershipHigh == True:
        $ AddChatter(vig4_sc3_2_resa_comment19)
    "I make eye contact with Teresa."
    mS "At least in terms of pride."
    enS "Why don't we switch up the direction. Give Captain the chance to call on me before the end."
    "We all nod in agreement, and throw our dice."
    $ AddChatter(vig4_sc3_2_resa_comment20)
    "I check under my cup: one 1, one 3, one 4, one 5, and one 6."
    "Teresa starts."
    enS "Four 2's."
    enS "Captain?"
    $ AddChatter(vig4_sc3_2_resa_comment21)
    pause 0.5
    $ AddChatter(vig4_sc3_2_resa_comment22)
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
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3_2_resa_comment23)
            mS "You're kidding!?"
            $ reactTarget = "vig4_sc3_teresadatelose"
            show screen streamerCommentary
            diceP1 "Damn it!"
            diceP2 "So close!"
            enS "No one has any other 2's!?"
            "I take a small stack of credits out of my pocket and place them in front of Teresa."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3_2_resa_comment24)
            mS "Well played."
            diceP2 "Thank you kindly."
            "The two players get up from the table and wander off into the plaza."
            "Teresa doesn't move to take the credits. She continues to stare at the uncovered dice on the table."
            $ AddChatter(vig4_sc3_2_resa_comment25)
            enS "But that's mathematically improbable."
            menu:
                enS "But that's mathematically improbable."
                "Teresa, you won.":
                    mS "Teresa, you won. Why do you care?"
                    $ AddChatter(vig4_sc3_2_resa_comment27)
                    show teresa stream neutral
                    enS "My calculations were off. You should have called me."
                    mS "I didn't."
                    enS "But you could have."
                    $ AddChatter(vig4_sc3_2_resa_comment28)
                    mS "Sometimes luck is more important than skill."
                    mS "You should know that in our line of work."
                    enS "You're right."
                    enS "Guess I went back to being \"Dr.\" Prismari there for a little bit."
                "Probability isn't certainty.":
                    $ engineerApproval += 1
                    mS "Probabilities aren't certainties."
                    $ AddChatter(vig4_sc3_2_resa_comment27)
                    mS "Anything can happen."
                    mS "And sometimes, a lot of times, luck is more important than skill."
                    mS "You should know that in our line of work."
                    $ AddChatter(vig4_sc3_2_resa_comment28)
                    show teresa stream neutral
                    enS "You're right."
                    enS "Guess I went back to being \"Dr.\" Prismari there for a little bit."
                    hide screen streamerCommentary
        "Raise.":
            "Teresa wouldn't make that bet if she didn't have a good hand for it."
            mS "Five 2's."
            diceP2 "Six 2's."
            diceP1 "Ahhhhh, seven 2's."
            "Teresa's smile is broad."
            enS "Fun. Eight 2's."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_2_resa_comment29)
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
                    $ AddChatter(vig4_sc3_2_resa_comment30)
                    "Teresa loses."
                    $ reactTarget = "vig4_sc3_teresadatewin"
                    show screen streamerCommentary
                    enS "No one has any other 2's!?"
                    diceP2 "Yes!"
                    diceP1 "Ooooh wow, so she could've called me."
                    mS "Tough luck."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc3_2_resa_comment31)
                    "I extend a hand toward Teresa."
                    "Without taking her eyes off the exposed dice, she places a handful of credits in my palm."
                    mS "Well played."
                    diceP2 "Thank you kindly."
                    "The two players get up from the table and wander off into the plaza."
                    "Teresa continues to stare at the uncovered dice on the table."
                    $ AddChatter(vig4_sc3_2_resa_comment25)
                    enS "But that's mathematically improbable."
                    menu:
                        enS "But that's mathematically improbable."
                        "You lost, get over it.":
                            mS "Losses happen Teresa."
                            mS "You can't win everything."
                            show teresa stream neutral
                            $ AddChatter(vig4_sc3_2_resa_comment26)
                            enS "I know. I just thought I had more control over that situation than I did."
                            mS "So what?"
                            mS "We've been in those kinds of situations before. Hell, I can think of ten in the last two weeks."
                            mS "It doesn't help to dwell on things that are out of our control."
                            $ AddChatter(vig4_sc3_2_resa_comment28)
                            enS "You're right."
                            enS "Guess I went back to being \"Dr.\" Prismari there for a little bit."
                        "Probability isn't certainty.":
                            $ engineerApproval += 1
                            mS "Probabilities are certainties."
                            mS "Anything can happen."
                            $ AddChatter(vig4_sc3_2_resa_comment26)
                            mS "And sometimes, a lot of times, luck is more important than skill."
                            mS "You should know that in our line of work."
                            $ AddChatter(vig4_sc3_2_resa_comment28)
                            show teresa stream neutral
                            enS "You're right."
                            enS "Guess I went back to being \"Dr.\" Prismari there for a little bit."
                            hide screen streamerCommentary
                "Raise.":
                    $ kcEngagement -=1
                    $ pdEngagement -=1
                    mS "Why not? Nine 2's."
                    $ AddChatter(vig4_sc3_2_resa_comment33)
                    diceP2 "Nope, gotta call that."
                    "We all lift our cups."
                    "Teresa has five 2's."
                    show teresa stream shock
                    "No one else has any."
                    "I lose."
                    $ reactTarget = "vig4_sc3_teresadatelose"
                    show screen streamerCommentary
                    enS "No one has any other 2's!"
                    $ AddChatter(vig4_sc3_2_resa_comment34)
                    mS "Damn."
                    "I toss some credits to the player on my right."
                    mS "Well played."
                    diceP2 "Thank you kindly."
                    "The two players get up from the table and wander off into the plaza."
                    "Teresa stares at the uncovered dice on the table."
                    $ AddChatter(vig4_sc3_2_resa_comment25)
                    enS "But that's mathematically improbable."
                    menu:
                        enS "But that's mathematically improbable."
                        "Teresa, you won.":
                            mS "Teresa, you won. Why do you care?"
                            show teresa stream neutral
                            $ AddChatter(vig4_sc3_2_resa_comment27)
                            enS "My calculations were off. You should have called me."
                            mS "I didn't."
                            enS "But you could have."
                            $ AddChatter(vig4_sc3_2_resa_comment28)
                            mS "Sometimes luck is more important than skill."
                            mS "You should know that in our line of work."
                            enS "You're right."
                            enS "Guess I went back to being \"Dr.\" Prismari there for a little bit."
                        "Probability isn't certainty.":
                            $ engineerApproval += 1
                            mS "Probabilities are certainties."
                            $ AddChatter(vig4_sc3_2_resa_comment27)
                            mS "Anything can happen."
                            mS "Sometimes, a lot of times, luck is more important than skill."
                            mS "You should know that in our line of work."
                            $ AddChatter(vig4_sc3_2_resa_comment28)
                            show teresa stream neutral
                            enS "You're right."
                            enS "Guess I went back to being \"Dr.\" Prismari there for a little bit."
                            hide screen streamerCommentary
    hide screen streamerCommentary
    jump vig4_sc3_2_teresa_2

label vig4_sc3_2_teresa_2():
    "Teresa continues to stare at the table."
    "She picks up a die and starts rotating it in her fingers."
    enS "Hey, Captain. Do you think I'm a good outlaw?"
    $ AddChatter(vig4_sc3_2_resa_comment35)
    menu:
        enS "Hey, Captain. Do you think I'm a good outlaw?"
        "Of course!":
            $ engineerApproval += 1
            mS "Of course! I'd trust you with my life."
            enS "I know that. But..."
        "Where is this coming from?":
            mS "Where is this coming from?"
    enS "Sometimes I look at you and Jennica, and it fits you so easily. This life, I mean."
    enS "You've been living it for so long. You're {i}Snakehawks{/i}."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc3_2_resa_comment36)
    enS "I'm so grateful I met the two of you. You both changed my life, tremendously for the better."
    enS "But sometimes I wonder what could have been."
    enS "If I didn't get my doctorate? If I didn't disobey my parents? If I went to Alliance space instead of the Outposts?"
    $ AddChatter(vig4_sc3_2_resa_comment37)
    enS "All these moments where I made decisions that could have legitimately gone another way."
    enS "But this is the reality that I ended up in, whether I'm happy about it or not."
    enS "Does that mean something?"
    "Teresa looks up and locks eyes with me."
    $ AddChatter(vig4_sc3_2_resa_comment38)
    menu:
        "Teresa looks up and locks eyes with me."
        "Don't be afraid to call this fate.":
            mS "Teresa, you can use the word fate. You don't have to be scared of it."
            enS "But if it is fate, then what does it mean?"
            $ AddChatter(vig4_sc3_2_resa_comment43)
            if engineerApproval > 4:
                "Teresa gets closer to the edge of her seat. Closer to me."
            enS "Why did this moment have to happen?"
            $ AddChatter(vig4_sc3_2_resa_comment44)
            "Her eyes do not leave mine."
            menu:
                "Her eyes do not leave mine."
                "Resa, I love you." if jennicaRomance == False:
                    mS "What else could it be, Resa: love."
                    show teresa stream shock
                    enS "What!?"
                    mS "I love you, Teresa."
                    $ AddChatter(vig4_sc3_2_resa_comment45)
                    if engineerApproval > 4:
                        $ csEngagement -= 2
                        $ kcEngagement += 3
                        $ pdEngagement -= 1
                        $ teresaRomance = True
                        "Teresa face is immediately bright red."
                        enS "Oh, wow, this is really happening?"
                        enS "Is it hot? Do you think it's hot right now?"
                        menu:
                            enS "Is it hot? Do you think it's hot right now?"
                            "Kiss her.":
                                "I put a finger to her lips."
                                mS "Shhhh."
                                mS "You don't have to explain this."
                                "She freezes completely still, her eyes locked on mine."
                                "I move forward and kiss Teresa."
                                $ AddChatter(vig4_sc3_2_resa_comment46)
                            "Wait for her.":
                                "I wait, patiently."
                                "Teresa suddenly stops moving and meets my eyes."
                                "We hold each other's gaze."
                                enS "I love you too, Moze."
                                "I feel myself smiling before I even register to do it myself."
                                "I move forward and kiss Teresa."
                                $ AddChatter(vig4_sc3_2_resa_comment46)
                        $ reactTarget = "vig4_sc3_teresadatekiss"
                        show screen streamerCommentary
                        show teresa stream happy
                        "Our arms wrap around each other, holding one another tightly."
                        "It feels good. To hold and be held. Like we could stay here for hours, days, longer even."
                        $ AddChatter(vig4_sc3_2_resa_comment47)
                        "Finally, our lips part. We stare into each other's eyes."
                        if viewershipHigh == True or viewershipMed == True:
                            $ AddChatter(vig4_sc3_2_resa_comment48)
                        enS "Now the problem is I don't want to let go."
                        mS "Me neither."
                        if viewershipHigh == True or viewershipMed == True:
                            $ AddChatter(vig4_sc3_2_resa_comment49)
                        mS "But I should go check and see if Coil has any news."
                        mS "We'll have more time."
                        enS "Yes, lots of time."
                        "It's hard to let go, but somewhow we manage."
                        "As I stand and take a step away from the table, I sneak a glance back at Teresa."
                        "She's still looking at the exposed dice, but now with a massive smile on her face."
                        $ AddChatter(vig4_sc3_2_resa_comment50)
                        "I smile to myself as I return to the festival."
                        hide screen streamerCommentary
                    else:
                        $ kcEngagement -= 1
                        $ csEngagement += 1
                        $ pdEngagement += 1
                        enS "Oh! That's... not what I was expecting."
                        "My heart drops a little."
                        mS "What do you mean?"
                        "Teresa looks to the dice, then back to me."
                        $ AddChatter(vig4_sc3_2_resa_comment51)
                        "She sighs."
                        show teresa stream neutral
                        if viewershipHigh == True or viewershipMed == True:
                            $ AddChatter(vig4_sc3_2_resa_comment52)
                        $ AddChatter(vig4_sc3_2_resa_comment53)
                        enS "I care a lot about you, Captain. And I deeply respect you as a leader."
                        $ AddChatter(vig4_sc3_2_resa_comment55)
                        enS "But I don't feel the same way."
                        $ AddChatter(vig4_sc3_2_resa_comment56)
                        $ reactTarget = "vig4_sc3_teresadaterejection"
                        show screen streamerCommentary
                        enS "I'm sorry."
                        "She's still making eye contact with me. Unflinching. Fierce."
                        "Honest."
                        $ AddChatter(vig4_sc3_2_resa_comment57)
                        "I sigh."
                        mS "Of course. I'm glad you were honest with me."
                        enS "Always."
                        $ AddChatter(vig4_sc3_2_resa_comment58)
                        pause 0.5
                        $ AddChatter(vig4_sc3_2_resa_comment59)
                        mS "I should—I should go find Coil, see if he's got any updates for us."
                        enS "Yeah, I hope it's good news."
                        mS "I'll let you and Jenn know as soon as I can."
                        $ AddChatter(vig4_sc3_2_resa_comment60)
                        enS "Sounds good. Take care."
                        $ AddChatter(vig4_sc3_2_resa_comment61)
                        mS "Yeah."
                        "I turn away from Teresa and back to the festival." 
                        hide screen streamerCommentary           
                "I don't know.":
                    $ kcEngagement -= 2
                    $ pdEngagement -= 1
                    mS "I don't think it's for me to say, Resa."
                    $ AddChatter(vig4_sc3_2_resa_comment39)
                    mS "That's something you have to figure out for yourself."
                    "Teresa sighs and hangs her head slightly."
                    $ AddChatter(vig4_sc3_2_resa_comment40)
                    enS "Yeah, that makes sense."
                    enS "It's irritating, but you're right."
                    mS "Alright, I need to go find Coil, see if he's got any updates for us."
                    $ AddChatter(vig4_sc3_2_resa_comment41)
                    enS "Yeah, I hope it's good news."
                    mS "I'll let you and Jenn know as soon as I can."
                    $ AddChatter(vig4_sc3_2_resa_comment42)
                    enS "Good."
                    enS "And thanks for the conversation, Captain. I really needed it."
                    "I turn away from Teresa and back to the festival."
        "Who cares about probabilities.":
            $ kcEngagement -= 2
            $ csEngagement += 1
            mS "All those alternate timelines you're imagining: screw 'em."
            $ AddChatter(vig4_sc3_2_resa_comment39)
            mS "What matters is what you've decided."
            mS "You're an incredible outlaw, crew member, and friend."
            $ AddChatter(vig4_sc3_2_resa_comment40)
            mS "I'm so grateful to have you on the Oakley. And I know Jenn feels the same way."
            show teresa stream happy
            "Teresa smiles and nods."
            $ AddChatter(vig4_sc3_2_resa_comment41)
            enS "Yeah, you're right."
            enS "Thanks, Captain. I really needed to hear that."
            mS "Any time."
            $ AddChatter(vig4_sc3_2_resa_comment42)
            mS "Alright, I need to go find Coil, see if he's got any updates for us."
            enS "Yeah, I hope it's good news."
            mS "I'll let you and Jenn know as soon as I can."
            enS "Good."
            "I turn away from Teresa and back to the festival."
    hide teresa with dissolve
    jump vig4_sc3_3

label vig4_sc3_3():
    $ viewCheck4 = viewCount
    "A crowd just to my left suddenly gets my attention."
    "There's a small semi-circle of people, their heads inclined downwards."
    show mac stream neutral at stream_center_mac with dissolve
    "They're all looking at MAC, as he waves his hands in the air."
    play audio "macNeutral.wav" volume 1.5
    if macViolence >= macPeace and customsStampede == True:
        show mac stream happy
        macS "So then Dr. Prismari begins the {i}conflagrant{/i} phase and the booth explodes!"
        $ AddChatter(vig4_sc3_3_comment1)
        macS "Everyone starts running wildly, and we sneak under security's nose!"
        "There are gasps throughout the crowd."
        if gunsBlazing == True and viewershipHigh == True:
            $ AddChatter(vig4_sc3_3_comment2)
        else:
            $ AddChatter(vig4_sc3_3_comment3)
        townguy "My word, I hope everyone was ok."
        if viewershipHigh == True:
            $ AddChatter(vig4_sc3_3_comment4)
        macS "We did not have time to check on people. We had to go meet a \"skeeve\" named Matticus."
    elif macPeace > macViolence and vig2_marshalEpilogue == True and reginaldChoice == False:
        show mac stream happy
        macS "So then I said, \"take that skeeve\" and we took care of Reggie."
        $ AddChatter(vig4_sc3_3_comment1)
        macS "Captain Moze saved the aid ship and Sallent was saved!"
        "There are gasps throughout the crowd."
        if gunsBlazing == True and viewershipHigh == True:
            $ AddChatter(vig4_sc3_3_comment2)
        else:
            $ AddChatter(vig4_sc3_3_comment3)
        townguy "My word, I heard that Sallent had survived Gray Fever, but I didn't know they were in such danger."
        if viewershipHigh == True:
            $ AddChatter(vig4_sc3_3_comment4)
        macS "Indeed, Captain Moze is a hero."
    elif vig3_macShootAma == True:
        macS "So then I picked up the gun and aimed it right at Ama."
        $ AddChatter(vig4_sc3_3_comment1)
        macS "I shot her in the side, giving Captain Moze the chance to disarm her!"
        show mac stream happy
        macS "That's how we escaped the Deadeye's clutches!"
        townguy "My word, The Deadeye sounds dreadful!"
        macS "Indeed, but she cannot hope to stand up to the Oakley!"
    elif vig3_macReadAma == True:
        macS "So then I threatened Ama with the gun."
        macS "But I knew I didn't need it."
        show mac stream happy
        macS "I accurately read her emotions and calculated a response to throw her off guard."
        macS "That gave Captain Moze the chance to disarm her, and together we escaped The Deadeye's clutches!"
        townguy "My word, the Deadeye sounds dreadful!"
        macS "Indeed, but she cannot hope to stand against the Oakley!"
    else:
        macS "So then I chased after the Hounds and got captured."
        macS "But I escaped in the laundry and got rid of the bad BC prototype."
        $ AddChatter(vig4_sc3_3_comment1)
        show mac stream happy
        macS "Captain Moze found me, and together we fought our way out of BC's evil clutches!"
        "There are gasps throughout the crowd."
        townguy "My word, the Hounds sound dreadful!"
        if viewershipHigh == True:
            $ AddChatter(vig4_sc3_3_comment5)
        macS "They were, but they're no match for the Snakehawks!"
    hide mac with dissolve
    "I chuckle a bit to myself."
    cS "He has many more stories like that one."
    $ renpy.music.set_volume(0.4, 1.0)
    show coil stream neutral at stream_center with dissolve
    "Coil steps up next to me. His eyes remain on MAC."
    $ AddChatter(vig4_sc3_3_comment6)
    cS "I spoke with him earlier."
    $ AddChatter(vig4_sc3_3_comment7)
    if marshal > outlaw:
        cS "All he seems to talk about his how heroic you and your crew are."
        cS "How he wants to be as selfless as you."
        $ AddChatter(vig4_sc3_3_comment8)
    else:
        cS "He seems fascinated by how protective of your crew you are."
        cS "How you'll go to any lengths to ensure their safety."
        $ AddChatter(vig4_sc3_3_comment9)
    cS "Your influence on him has been immense."
    menu:
        cS "Your influence on him has been immense."
        "I wish it wasn't.":
            mS "I wish I didn't. He deserves better than the life of an outlaw."
            if outlaw > marshal:
                $ outlaw -= 2
            else:
                $ marshal += 2
            if marshal > outlaw:
                cS "I understand."
                cS "I wish that Vega could use her mind to make things other than tools for war."
                cS "But we do not get to determine the course of our children's lives."
                $ AddChatter(vig4_sc3_3_comment10)
                "Coil sighs."
            else:
                cS "To speak candidly, I wish that too."
                "I feel my body tense up instinctually."
                $ AddChatter(vig4_sc3_3_comment11)
                mS "What's that supposed to mean?"
                $ AddChatter(vig4_sc3_3_comment12)
                cS "Like I said, I'm enormously grateful to you for getting MAC to us."
                cS "But to hear how you went about it."
                $ AddChatter(vig4_sc3_3_comment13)
                cS "I wonder if it was worth the cost."
                $ AddChatter(vig4_sc3_3_comment14)
                menu:
                    cS "I wonder if it was worth the cost."
                    "I wonder the same thing.":
                        mS "Sometimes I wonder the same thing."
                        if viewershipHigh == True or viewershipMed == True:
                            $ AddChatter(vig4_sc3_3_comment15)
                        mS "But I don't have the luxury to second-guess my decisions."
                        cS "True. Perhaps I've forgotten how difficult life on the run can be."
                        $ AddChatter(vig4_sc3_3_comment16)
                        "Coil sighs."
                    "You don't get to judge me.":
                        mS "You don't get to judge me while you sit in your hidden safehouse."
                        if viewershipHigh == True:
                            $ AddChatter(vig4_sc3_3_comment17)
                        cS "Then who does, Moze?"
                        "Coil's eyes fall on me."
                        $ AddChatter(vig4_sc3_3_comment18)
                        mS "I do what is necessary."
                        cS "And {i}that{/i} is what worries me."
                        $ AddChatter(vig4_sc3_3_comment19)
                        "Coil sighs."
        "That's a good thing.":
            if outlaw > marshal:
                $ outlaw += 1
            else:
                $ marshal += 1
            mS "He was alone when we found him. Someone had to show him how to survive."
            cS "He has to know how to live as well."
            $ AddChatter(vig4_sc3_3_comment20)
            menu:
                cS "He has to know how to live as well."
                "We gave him a family.":
                    mS "We gave him a family."
                    mS "What's more important than that?"
                    cS "Little."
                    cS "But maturing is also understanding the bigger picture, extending empathy to more than your own family."
                    if marshal > outlaw:
                        $ AddChatter(vig4_sc3_3_comment10)
                        cS "He can do that. And it's a testament to you that he understands this."
                    else:
                        cS "He seems to be obsessed with just his family."
                        cS "What does that say about you?"
                        $ AddChatter(vig4_sc3_3_comment11)
                        "Coil sighs."
                        $ AddChatter(vig4_sc3_3_comment12)
                "That's not my responsibility.":
                    $ kcEngagement -= 1
                    mS "That wasn't my responsibility."
                    mS "I had to make sure he was safe."
                    $ AddChatter(vig4_sc3_3_comment21)
                    cS "Yes, I suppose we did emphasize that was your only concern."
                    "Coil sighs."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc3_3_comment22)
    cS "I got in touch with the Dragonflies."
    cS "They won't allow you or your crew to transit with MAC."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc3_3_comment23)
    cS "And they want you to depart Polaris now."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc3_3_comment24)
        pause 0.5
    $ AddChatter(vig4_sc3_3_comment25)
    "I'm shocked into silence."
    $ AddChatter(vig4_sc3_3_comment26)
    pause 0.5
    $ AddChatter(vig4_sc3_3_comment27)
    if marshal > outlaw:
        cS "I tried my best to convince them otherwise, but they don't trust you."
        $ AddChatter(vig4_sc3_3_comment28)
    else:
        cS "I must say, I agree with them."
        cS "You're too dangerous to the people around you."
        $ AddChatter(vig4_sc3_3_comment29)
        cS "And you don't seem to recognize that."
        if viewershipHigh == True:
            $ AddChatter(vig4_sc3_3_comment30)
        cS "Worse still, the people you love do not realize it either."
    cS "I'm sorry."
    $ reactTarget = "vig4_sc3_coil1"
    show screen streamerCommentary
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc3_3_comment31)
    menu:
        cS "I'm sorry."
        "Like hell this is happening!":
            $ kcEngagement += 1
            $ csEngagement -= 1
            $ pdEngagement += 1
            mS "Like hell, Coil!"
            mS "You think I'm going to let you rip my family apart like this!"
            if customsStampede == True:
                $ AddChatter(vig4_sc3_3_comment33)
            cS "He's not \"your\" family."
            cS "I was there when he was conceived. Elijah and I created him together."
            cS "We are more family than you will ever be."
            $ AddChatter(vig4_sc3_3_comment34)
            mS "You don't even know him."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_3_comment35)
            cS "I knew Elijah. And I know you, Mozely."
            if marshal > outlaw:
                cS "I had hope you would understand."
            else:
                cS "You are dangerous. And you have to leave."
            $ AddChatter(vig4_sc3_3_comment36)
        "I understand.":
            $ csEngagement += 1
            $ kcEngagement -= 1
            $ pdEngagement -= 1
            "I take a deep breath and exhale slowly."
            "In my mind's eye I see MAC, hiding behind the console where his creator's dead body slumps."
            "Lost, confused, scared."
            $ AddChatter(vig4_sc3_3_comment37)
            "I see him talking with Allistar about music."
            "I see him calling Matticus a \"skeeve.\""
            "I see him now, as he goes somewhere I can't follow."
            mS "I understand."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3_3_comment38)
            mS "Promise me you'll take care of him."
            cS "Of course. I promise you, he will be safe."
            $ AddChatter(vig4_sc3_3_comment39)
            mS "Good. That's all that matters."
    cS "I can give you some time to say goodbye."
    cS "I will alert your crew. You have fifteen minutes."
    "Coil turns and leaves."
    $ vig4_sc3_3_comment36.click = False
    $ vig4_sc3_3_comment39.click = False
    hide screen streamerCommentary
    menu:
        "Coil turns and leaves."
        "Reach for your gun.":
            "Instinctively, I reach for my gun."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_3_comment40)
            "But it's not there."
            "They were taken at the start of the festival \"for safety.\""
            "Was this planned?"
            #"I scan the plaza and notice a handful of people with stun rods."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3_3_comment41)
            #"Some of them are eyeing me."
            #"Shit."
            hide coil with dissolve
            "I turn to look at MAC."
        "Turn to MAC.":
            hide coil with dissolve
            "With a heavy sigh, I turn to look at MAC."
    "The crowd around him is dissipating."
    stop music fadeout 1.0
    jump vig4_sc3_4

label vig4_sc3_4():
    show mac stream neutral at stream_center_mac with dissolve
    play music "soundtrack/theme.wav" volume 0.7
    "MAC notices me almost as soon as I turn toward him."
    play audio "macHum.wav" volume 1.5
    macS "Moze! Isn't this wonderful!"
    mS "MAC, we should talk."
    macS "Of course, that would be nice. Shall we take a walk around the plaza?"
    stop backAudio fadeout 4.0
    $ AddChatter(vig4_sc3_4_comment1)
    "The two of us head to the outskirts of the plaza."
    "Every step feels heavy. As if my boots are filled with lead."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc3_4_comment2)
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
    $ AddChatter(vig4_sc3_4_comment3)
    macS "The people here seem... what's the right word? Is it \"happy\"?"
    "I look over my shoulder. Even from a distance, the smiles on everyone's faces at the festival are apparent."
    #macS "They were all so interested in our adventures. I think I impressed them with our stories."
    #mS "I'm sure you impressed them yourself"
    play audio "macPester.wav" volume 1.5
    macS "What do you think of this place, Captain?"
    $ AddChatter(vig4_sc3_4_comment4)
    menu:
        macS "What do you think of this place, Captain?"
        "It's an illusion.":
            $ macPessimism += 1
            mS "I think it's fake, MAC."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_4_comment5)
            mS "A bunch of people acting like they have a higher purpose, but they've forgotten what the galaxy is really like."
        "It's a haven.":
            $ macHope += 1
            mS "I think it's a haven, MAC."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_4_comment5)
            mS "Somewhere people can be genuinely happy, where they have a purpose."
    "MAC doesn't respond immediately."
    $ AddChatter(vig4_sc3_4_comment6)
    macS "Moze, do you know what our purpose is?"
    mS "To keep you safe. To get you here."
    play audio "macAffirmative.wav" volume 1.5
    macS "Yes, but that mission is accomplished."
    macS "What do we do now?"
    $ AddChatter(vig4_sc3_4_comment7)
    menu:
        macS "What do we do now?"
        "We help others.":
            $ csEngagement += 2
            $ macPeace += 3
            $ macHope += 2
            $ marshal += 1
            mS "I suppose our purpose is to leave the galaxy a better place than when we found it."
            macS "To help people?"
            mS "Yeah. That feels right."
            $ AddChatter(vig4_sc3_4_comment8)
            macS "Did we help people?"
            menu:
                macS "Did we help people?"
                "I don't know.":
                    mS "I don't know MAC. Things are rarely that cut and dry."
                    macS "Yes, I have noticed a distinct lack of clarity in answers to my questions."
                    $ AddChatter(vig4_sc3_4_comment9)
                    mS "But getting you here could change a lot of things in the galaxy."
                "Yes.":
                    mS "I think so."
                    if outlaw > marshal + 2:
                        $ AddChatter(vig4_sc3_4_comment10)
                    else:
                        $ AddChatter(vig4_sc3_4_comment11)
                    mS "Getting you here especially can change a lot of things in the galaxy."
                "No.":
                    mS "I don't think so."
                    if marshal > outlaw + 4:
                        $ AddChatter(vig4_sc3_4_comment12)
                    else:
                        $ AddChatter(vig4_sc3_4_comment13)
                    mS "But being here now, maybe you can start to change that."
        "We look out for ourselves.":
            $ pdEngagement += 2
            $ macViolence += 3
            $ macPessimism += 2
            $ outlaw += 1
            mS "We take care of our own, make sure we can live free."
            $ AddChatter(vig4_sc3_4_comment14)
            macS "I see, survival, replication..."
            macS "But we have all survived. What is next?"
            menu:
                macS "But we have all survived. What is next?"
                "We take what we want.":
                    mS "We take what we want, when we want it."
                    mS "Gaining the power to control our own destiny and make sure others can't is what's most important."
                    if viewershipHigh == True:
                        $ AddChatter(vig4_sc3_4_comment16)
                    macS "I see, life is about holding power?"
                    mS "The more, the better in this galaxy."
                "Enjoy life's pleasures.":
                    mS "Whatever gives you pleasure, that's what."
                    mS "Find what you enjoy and hold tight to that, don't let anyone take it away."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc3_4_comment15)
                    macS "I see. It's what's known as \"hedonism,\" correct?"
                    mS "Something like that."
                "Make sure your family stays safe.":
                    mS "It never ends in this galaxy."
                    mS "You always have to be on your toes, protecting your family."
                    macS "I see. The fight is never over?"
                    if viewershipHigh == True:
                        $ AddChatter(vig4_sc3_4_comment17)
                    mS "Never."
    play audio "macOK.wav" volume 1.5
    "MAC whirs to himself."
    jump vig4_sc3_5

label vig4_sc3_5():
    stop music fadeout 3.0
    macS "I do not know how to feel about my purpose."
    macS "Coil says I am to go with him and Vega."
    macS "We'll help build new communities for people running from BigCorp and the Alliance."
    $ AddChatter(vig4_sc3_5_comment1)
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
    $ AddChatter(vig4_sc3_5_comment2)
    pause 0.5
    $ AddChatter(vig4_sc3_5_comment3)
    play audio "macHum.wav" volume 1.5
    macS "I want to stay a part of this family."
    $ AddChatter(vig4_sc3_5_comment4)
    menu:
        macS "I want to stay a part of this family."
        "I can't leave him here.":
            $ kcEngagement += 2
            $ csEngagement -= 2
            $ pdEngagement += 1
            "I can't leave him."
            $ AddChatter(vig4_sc3_5_comment5)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment6)
            mS "I don't want to leave here without you either, MAC."
            play audio "macPing.wav" volume 1.5
            macS "Then let's leave! Right now!"
            macS "We can fight! You, me, Jennica, Teresa, we can take on anyone!"
            $ AddChatter(vig4_sc3_5_comment7)
            "My heart pounds fast."
            mS "You're right, we need a plan!"
            cS "You do not."
            hide mac with dissolve
            $ reactTarget = "vig4_sc3_coil2"
            show screen streamerCommentary
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_5_comment8)
            show coil stream neutral at stream_left5 with dissolve
            "Coil steps up from an alleyway."
            show vega stream gun at stream_left with dissolve
            "Vega is behind him, along with ten men in guard uniforms holding stun rods."
            $ AddChatter(vig4_sc3_5_comment9)
            show teresa stream neutral at stream_right5 with dissolve
            "Teresa and Jennica are in between the guards."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_5_comment10)
            show dflyguard at stream_right with dissolve
            "The guard directly behind them pushes them in the back, forcing them to stumble forward."
            enS "They had a feeling we were gonna try something."
            dflyGuard "I found your friends trying to grab your weapons from the storage stall."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3_5_comment11)
            hide dflyguard with dissolve
            hide teresa with dissolve
            cS "Moze. I'm sorry. It's time to say goodbye."
            $ AddChatter(vig4_sc3_5_comment12)
            "I look down and—"
            show mac stream neutral at stream_center_mac with dissolve
            "MAC is hiding behind my legs, arms wrapped around me."
            play audio "macNeutral.wav" volume 1.5
            macS "Do something, Moze!"
            $ AddChatter(vig4_sc3_5_comment13)
            if macViolence >= macPeace:
                macS "You have another blaster, right? We can take them, can't we?"
            else:
                macS "You have an escape plan drawn up, just in case, don't you?"
            "I shake my head."
            hide screen streamerCommentary
            $ AddChatter(vig4_sc3_5_comment14)
            mS "MAC..."
            macS "No!"
            if macViolence >= macPeace:
                "MAC rolls forward, readying the pulse fire from his arm."
            else:
                "MAC rolls forward, preparing the EMP charge in his antenna."
            vS "{i}Shhhhshhshh.{/i}"
            "Vega steps forward and restrains him."
            vS "I'm really sorry, MAC. This is for your own good."
            show vega stream neutral
            play audio "macAlarmed.wav" volume 1.5
            macS "How do you know what's for my own good?"
            $ AddChatter(vig4_sc3_5_comment15)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment16)
            macS "None of you even know what \"good\" is!"
            $ AddChatter(vig4_sc3_5_comment17)
            pause 1.0
            $ AddChatter(vig4_sc3_5_comment18)
            menu:
                macS "None of you even know what \"good\" is!"
                "MAC, it's over.":
                    $ kcEngagement -= 1
                    mS "MAC."
                    "I take a knee, and reach a hand out to him."
                    mS "Our journey together is over."
                    "Tears, unbidden, flood my eyelids."
                    mS "It's time to say goodbye."
                "MAC, you have to decide that now.":
                    $ kcEngagement += 1
                    mS "MAC."
                    "I take a knee, and reach a hand out to him."
                    mS "You're right. None of us know anything. We're all messed up, we're all broken."
                    mS "No one can tell you what's right or wrong, good or bad."
                    mS "You have to decide that for yourself now."
                    "Tears, unbidden, flood my eyelids."
                    mS "It's time to say goodbye."
            "MAC shakes his head."
            hide coil with dissolve
            hide vega with dissolve
            "Coil nods at Vega, and she lets go of him."
            play audio "macGrumble.wav" volume 1.5
            macS "But I don't want to."
            $ AddChatter(vig4_sc3_5_comment19)
            mS "I don't either."
            "MAC rolls toward me. Slowly. Tentatively."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_5_comment20)
            "He takes my hand."
            "I grip it tight."
            play audio "macSad.wav" volume 2.0
            "He rolls into my chest, just like the first time I met him."
            "Only this time, I wrap my arms around his warm shell."
            $ reactTarget = "vig4_sc3_macgoodbyekind"
            show screen streamerCommentary
            mS "I'll miss you so much."
            macS "I'll miss you too."
            mS "Take care of yourself."
            macS "You taught me how."
            $ AddChatter(vig4_sc3_5_comment21)
            "I don't know how long we stay there for."
            "But eventually, my arms leave his side, and he rolls back."
            hide screen streamerCommentary
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3_5_comment22)
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
            pS "Bye lil' guy. Don't listen to anyone who says ya can't do somethin'."
            $ AddChatter(vig4_sc3_5_comment23)
            "MAC nods at both of them."
            stop music fadeout 2.0
            macS "Goodbye, Teresa. Goodbye, Jennica."
            menu:
                macS "Goodbye, Teresa. Goodbye, Jennica."
                "Goodbye.":
                    mS "Goodbye, MAC."
            macS "Goodbye, Moze."
            $ AddChatter(vig4_sc3_5_comment24)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment25)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment26)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment27)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment28)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment29)
            pause 0.5
            hide jennica with dissolve
            hide teresa with dissolve
            hide mac with Dissolve(2.0)
            jump vig4_sc4_1
        "You have to stay.":
            $ kcEngagement -= 2
            $ pdEngagement -= 1
            $ csEngagement += 1
            "He has to stay here. It hurts, but everything would be for nothing if he leaves with me."
            mS "I would like that too. But it's not in the cards."
            $ AddChatter(vig4_sc3_5_comment30)
            play audio "macPester.wav" volume 1.5
            macS "But, why?"
            mS "They just want you. The rest of us—we're a liability."
            $ AddChatter(vig4_sc3_5_comment31)
            "MAC inches closer to me."
            play audio "macPester.wav" volume 1.5
            macS "Why?"
            mS "Because I've made mistakes. Mistakes that you have a chance to avoid."
            $ AddChatter(vig4_sc3_5_comment32)
            "He gets right up to my feet."
            play audio "macPester.wav" volume 1.5
            macS "Why?"
            mS "Because this galaxy is all screwed up!"
            play audio "macOK.wav" volume 1.5
            "MAC recoils a bit."
            $ AddChatter(vig4_sc3_5_comment33)
            mS "Because everything I touch is poisoned, and I can't risk that happening to you."
            cS "It's a bold admission, Moze."
            hide mac with dissolve
            show coil stream neutral at stream_left5 with dissolve
            "Coil steps up from an alleyway."
            show vega stream gun at stream_left with dissolve
            "Vega is behind him, along with ten men in guard uniforms holding stun rods."
            $ reactTarget = "vig4_sc3_coil2"
            show screen streamerCommentary
            $ AddChatter(vig4_sc3_5_comment9)
            show teresa stream neutral at stream_right5 with dissolve
            "Teresa and Jennica are in between the guards."
            show dflyguard at stream_right with dissolve
            "The guard directly behind them pushes them in the back, forcing them to stumble forward."
            enS "They had a feeling we were gonna try something."
            dflyGuard "I found your friends trying to grab your weapons from the storage stall."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3_5_comment34)
            hide dflyguard with dissolve
            hide teresa with dissolve
            cS "Moze. I'm sorry. It's time to say goodbye."
            "I look down and—"
            show mac stream neutral at stream_center_mac with dissolve
            "MAC is hiding behind my legs, his arms wrapped around me."
            play audio "macNeutral.wav" volume 1.5
            macS "Do something, Moze!"
            hide screen streamercommentary
            $ AddChatter(vig4_sc3_5_comment13)
            if macViolence >= macPeace:
                macS "You have another blaster, right? We can take them, can't we?"
            else:
                macS "You have an escape plan drawn up, just in case, don't you?"
            "I look down and shake my head."
            $ AddChatter(vig4_sc3_5_comment14)
            mS "MAC..."
            macS "No!"
            if macViolence >= macPeace:
                "MAC rolls forward, readying the pulse fire from his arm."
            else:
                "MAC rolls forward, preparing the EMP charge in his antenna."
            vS "Shhhhshhshh."
            "Vega steps forward and restrains him."
            show vega stream neutral
            vS "I'm really sorry, MAC. This is for your own good."
            play audio "macAlarmed.wav" volume 1.5
            macS "How do you know what's for my own good?"
            $ AddChatter(vig4_sc3_5_comment15)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment16)
            macS "None of you even know what \"good\" is!"
            $ AddChatter(vig4_sc3_5_comment17)
            pause 1.0
            $ AddChatter(vig4_sc3_5_comment18)
            menu:
                macS "None of you even know what \"good\" is!"
                "MAC, it's over.":
                    $ kcEngagement -= 1
                    mS "MAC."
                    "I take a knee, and reach a hand out to him."
                    mS "Our journey together is over."
                    "Tears, unbidden, flood my eyelids."
                    mS "It's time to say goodbye."
                "MAC, you have to decide that now.":
                    $ kcEngagement += 1
                    mS "MAC."
                    "I take a knee, and reach a hand out to him."
                    mS "You're right. None of us know anything. We're all messed up, we're all broken."
                    mS "No one can tell you what's right or wrong, good or bad."
                    mS "You have to decide that for yourself now."
                    "Tears, unbidden, flood my eyelids."
                    mS "But now, it's time to say goodbye."
            "MAC shakes his head."
            "Coil nods at Vega, and she lets go of him."
            hide coil with dissolve
            hide vega with dissolve
            play audio "macGrumble.wav" volume 1.5
            macS "But I don't want to."
            $ AddChatter(vig4_sc3_5_comment19)
            mS "I don't either."
            "MAC rolls toward me. Slowly. Tentatively."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc3_5_comment20)
            "He takes my hand."
            "I grip it tight."
            play audio "macSad.wav" volume 2.0
            "He rolls into my chest, just like the first time I met him."
            "Only this time, I wrap my arms around his warm shell."
            $ reactTarget = "vig4_sc3_macgoodbyekind"
            show screen streamerCommentary
            mS "I'll miss you so much."
            macS "I'll miss you too."
            mS "Take care of yourself."
            macS "You taught me how."
            $ AddChatter(vig4_sc3_5_comment21)
            "I don't know how long we stay there for."
            "But eventually, my arms leave his side, and he rolls back."
            hide screen streamerCommentary
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3_5_comment22)
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
            pS "Bye lil' guy. Don't listen to anyone who says ya can't do somethin'."
            $ AddChatter(vig4_sc3_5_comment23)
            "MAC nods at both of them."
            stop music fadeout 2.0
            macS "Goodbye, Teresa. Goodbye, Jennica."
            menu:
                macS "Goodbye, Teresa. Goodbye, Jennica."
                "Goodbye.":
                    mS "Goodbye, MAC."
            macS "Goodbye, Moze."
            hide screen streamerCommentary
            $ AddChatter(vig4_sc3_5_comment24)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment25)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment26)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment27)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment28)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment29)
            pause 0.5
            hide jennica with dissolve
            hide teresa with dissolve
            hide mac with Dissolve(2.0)
            jump vig4_sc4_1
        "You're not family.": #"This was just a mission."
            $ kcEngagement -= 3 #is it possible kitcat really likes this for the drama?
            #$ csEngagement += 1
            $ pdEngagement += 1
            $ rudeMACGoodbye = True
            "He has to stay here. I can't tell him the truth."
            mS "MAC, this was just a mission."
            $ AddChatter(vig4_sc3_5_comment35)
            play audio "macSad.wav" volume 1.5
            macS "What?"
            mS "All this was about bringing you here. Nothing else."
            $ AddChatter(vig4_sc3_5_comment36)
            macS "What are you saying?"
            mS "We're not a family. And you have to stay."
            $ reactTarget = "vig4_sc3_macgoodbyerude"
            show screen streamerCommentary
            $ AddChatter(vig4_sc3_5_comment37)
            macS "But—"
            $ AddChatter(vig4_sc3_5_comment38)
            mS "That's an order from your captain, MAC!"
            play audio "macAlarmed.wav" volume 1.5
            "MAC recoils."
            $ AddChatter(vig4_sc3_5_comment39)
            macS "I don't believe you."
            mS "It doesn't matter what you believe. It's what's happening."
            $ AddChatter(vig4_sc3_5_comment40)
            cS "I appreciate the honesty, Moze."
            hide mac with dissolve
            show coil stream neutral at stream_left with dissolve
            "Coil steps up from an alleyway."
            hide screen streamerCommentary
            cS "But there's no need to be mean to the child."
            show vega stream gun at stream_left5 with dissolve
            "Vega is behind him, along with ten men in guard uniforms holding stun rods."
            $ reactTarget = "vig4_sc3_coil2"
            show screen streamerCommentary
            $ AddChatter(vig4_sc3_5_comment9)
            show teresa stream neutral at stream_right5 with dissolve
            "Teresa and Jennica are in between the guards."
            show dflyguard at stream_right with dissolve
            "The guard directly behind them pushes them in the back, forcing them to stumble forward."
            enS "They had a feeling we were gonna try something."
            dflyGuard "I found your friends trying to grab your weapons from the storage stall."
            $ AddChatter(vig4_sc3_5_comment34)
            hide dflyguard with dissolve
            hide teresa with dissolve
            hide vega with dissolve
            cS "Moze. I'm sorry. It's time to say goodbye."
            hide screen streamerCommentary
            $ AddChatter(vig4_sc3_5_comment13)
            hide coil with dissolve
            "I look down and—"
            show mac stream neutral at stream_center_mac with dissolve
            "MAC is frozen still."
            $ AddChatter(vig4_sc3_5_comment14)
            "His head is pointed directly at the ground."
            if outlaw >= marshal:
                play audio "macPing.wav" volume 1.5
                macS "You were probably thinking of shooting the place up, weren't you?"
                enS "That's not—"
                macS "It's what we always do!"
            else:
                play audio "macPing.wav" volume 1.5
                macS "You were probably going to look for some tunnels to sneak through, weren't you?"
                pS "It was just in—"
                macS "It's what we always do!"
            "MAC looks up to me."
            macS "It's what {i}you{/i} always do."
            "MAC turns around and rolls up to Vega."
            "She drops to a knee and puts a hand on his head."
            play audio "macSad.wav" volume 2.0
            macS "Maybe I should have let Allistar take me."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc3_5_comment41)
                pause 0.5
            $ AddChatter(vig4_sc3_5_comment42)
            if viewershipHigh == True or viewershipMed == True:
                pause 0.5
                $ AddChatter(vig4_sc3_5_comment43)
            "Everything goes cold."
            "I lose control of my limbs, and slump to my knees."
            "A hand touches my shoulder."
            show coil stream neutral at stream_left with dissolve
            "It's Coil."
            cS "It's not fair, what you have to do right now."
            cS "I'm sorry."
            $ AddChatter(vig4_sc3_5_comment44)
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
            $ AddChatter(vig4_sc3_5_comment16)
            cS "Let them go."
            $ AddChatter(vig4_sc3_5_comment17)
            hide coil with dissolve
            hide vega with dissolve #do we need this? she gets hidden earlier i think
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            "Teresa and Jennica move to my side."
            if jennicaRomance == True:
                "Jenn puts her hand on my shoulder."
            elif teresaRomance == True:
                "Resa puts her hand on my shoulder."
            else:
                "I feel both of their hands on my shoulder."
            $ AddChatter(vig4_sc3_5_comment18)
            enS "Farewell, MAC. Remember, no snitches."
            pS "Bye lil' guy. Don't listen to anyone who says ya can't do somethin'."
            "MAC doesn't move."
            stop music fadeout 2.0
            macS "Goodbye, engineer Prismari. Goodbye, pilot Brown."
            menu:
                macS "Goodbye, engineer Prismari. Goodbye, pilot Brown."
                "Goodbye.":
                    mS "Goodbye, MAC."
            "He doesn't say anything."
            "MAC turns around and leaves."
            $ AddChatter(vig4_sc3_5_comment45)
            hide mac with Dissolve(2.0)
            $ AddChatter(vig4_sc3_5_comment46)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment47)
            pause 0.5
            $ AddChatter(vig4_sc3_5_comment48)
            hide teresa with dissolve
            hide jennica with dissolve
            jump vig4_sc4_1

label vig4_sc4_1():
    $ viewCheck5 = viewCount
    show shiphub_stream at topleft onlayer background with dissolve
    hide polarisplazanight_stream
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    "We don't speak a word to each other on the way back to the ship."
    "The Oakley is quiet and cold as I step onto the bridge."
    mS "I don't know what to do."
    $ AddChatter(vig4_sc4_1_comment1)
    "Silence."
    enS "I'll go down to the engine room and get them started." 
    enS "We gotta takeoff soon to avoid the star shower."
    $ AddChatter(vig4_sc4_1_comment2)
    pS "I'll go make us some tea."
    hide teresa with dissolve
    hide jennica with dissolve
    "I fall back into one of the chairs."
    play audio "shipWarmUp.wav" volume 1.0
    "A low whir kicks up as the engines come on line."
    play audio "shipHum.wav" volume 0.4 fadein 2.0
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc4_1_comment3)
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
    play audio "callRing.wav" volume 0.8
    "There it is again."
    $ AddChatter(vig4_sc4_1_comment4)
    "It's like the sound of a communicator ringing."
    play audio "callRing.wav" volume 1.4
    "What the hell?"
    "I go over to the escape pods."
    "There, by the pod that Allistar tried to escape in a month ago, is a lone communicator, stuck under the pod."
    play audio "callRing.wav" volume 2.0
    if viewershipHigh == True:
        $ AddChatter(vig4_sc4_1_comment5)
    "I pick it up."
    "It's Allistar's. And it's receiving a call."
    mS "Hello?"
    amaS "Still sentimental I see, Mozely."
    $ AddChatter(vig4_sc4_1_comment6)
    mS "Ama?"
    #show ama phone neutral
    amaS "Yes, kid, I have some business to discuss with you."
    $ AddChatter(vig4_sc4_1_comment7)
    pause 0.5
    $ AddChatter(vig4_sc4_1_comment8)
    amaS "So, let's get down to—"
    menu:
        amaS "So, let's get down to—"
        "Shut up!":
            mS "Shut the fuck up, Ama!"
            "My voice tears out of my mouth as if I have no control over it."
            mS "It's over, do you understand me!?"
            mS "MAC is with the Dragonflies now. You lost!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc4_1_comment9)
            mS "Do you hear me? Ama \"Deadeye\" Reyes, BC's biggest lapdog and company stooge failed."
            $ AddChatter(vig4_sc4_1_comment10)
            mS "So why don't you hang up and leave me and my crew alone!?"
    "Silence on the other end."
    amaS "Did you say that you handed over the robot to the Dragonflies?"
    mS "Yeah, you heard me. He's safe. You and BC can cry about it together."
    amaS "Mozely, I need you to listen to me very closely."
    mS "Why? What could you possibly have to say that I would want to hear?"
    amaS "I'm going to give you a way to get your family back!"
    $ AddChatter(vig4_sc4_1_comment11)
    "I freeze."
    amaS "You want to talk now?"
    mS "What do you mean?"
    amaS "BC knows where the Dragonflies are. They're launching an assault on them."
    mS "Bullshit."
    amaS "Polaris."
    "I can't respond."
    amaS "They just figured it out, found some communications coming from a moon that, according to their databases, is uninhabited."
    #$ AddChatter(vig4_sc4_1_comment12)
    amaS "But when they scanned for lifeforms, they found a tiny settlement with an artificial atmosphere."
    mS "Why are you telling me this? To gloat?"
    play music "soundtrack/decisionTime.wav" volume 1.2
    $ AddChatter(vig4_sc4_1_comment13)
    amaS "No. BC cut my contract. I'm dead in the water."
    $ AddChatter(vig4_sc4_1_comment14)
    amaS "This is an offer, Mozely. A second chance."
    $ AddChatter(vig4_sc4_1_comment15)
    amaS "I want that robot. I know you do too."
    $ AddChatter(vig4_sc4_1_comment16)
    mS "What do you want with him? You don't even know what he's designed to do."
    amaS "I know he has access to BC databases. And I mean {i}full{/i} access."
    amaS "With him, we could rebuild the Snakehawks."
    amaS "All we have to do is teach that kid to hack into their system and we can do whatever we want."
    $ reactTarget = "vig4_sc4_amaoffer"
    show screen streamerCommentary
    amaS "Rewire their banks to deposit all their funds into our accounts."
    amaS "Delete information about people and places we don't want them to know about."
    $ AddChatter(vig4_sc4_1_comment17)
    amaS "We could have everything we ever dreamed of, Mozely. Everything we used to talk about!"
    $ AddChatter(vig4_sc4_1_comment18)
    amaS "You just have to help me make sure the Dragonflies and BigCorp don't get away with him."
    $ AddChatter(vig4_sc4_1_comment19)
    amaS "What do you say?"
    $ AddChatter(vig4_sc4_1_comment20)
    pause 0.5
    $ AddChatter(vig4_sc4_1_comment21)
    if jennicaRomance == False and teresaRomance == False and viewershipHigh == True:
        pause 0.5
        $ AddChatter(vig4_sc4_1_comment22)
    pause 0.5
    $ AddChatter(vig4_sc4_1_comment23)
    menu:
        amaS "What do you say?"
        "Reject Ama's offer.":
            hide screen streamerCommentary
            $ marshal += 2
            $ csEngagement += 2
            $ kcEngagement -= 2
            $ pdEngagement -= 3
            $ vig4_amaOffer = False
            mS "You're living in the past, Ama."
            $ AddChatter(vig4_sc4_1_comment31)
            mS "The Snakehawks are dead."
            mS "Until you accept that, you're just going to be haunted by your past mistakes."
            $ AddChatter(vig4_sc4_1_comment32)
            "Silence."
            amaS "I see."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc4_1_comment33)
            amaS "Guess I'll have to do it myself."
            amaS "Be seeing you, Mozely."
            $ vig4_sc4_1_comment31.click = False
            $ AddChatter(vig4_sc4_1_comment34)
            play audio "cutCall.wav" volume 1.5
        "Agree to Ama's offer.":
            hide screen streamerCommentary
            $ outlaw += 2
            $ pdEngagement += 3
            $ kcEngagement += 2
            $ csEngagement -= 1
            $ vig4_amaOffer = True
            mS "Alright, Ama. I'm in."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc4_1_comment24)
                pause 0.5
            $ AddChatter(vig4_sc4_1_comment25)
            amaS "Thank you for seeing reason."
            if jennicaRomance == False and teresaRomance == False:
                $ AddChatter(vig4_sc4_1_comment26)
            menu:
                amaS "Thank you for seeing reason."
                "This is for the Snakehawks.":
                    $ deadeyeApproval += 1
                    mS "But this isn't for you. It's for the Snakehawks."
                    mS "It's our time to get payback."
                    if viewershipHigh == True or viewershipMed == True:
                        $ AddChatter(vig4_sc4_1_comment27)
                    amaS "Couldn't have said it better myself."
                    $ AddChatter(vig4_sc4_1_comment28)
                    amaS "I'll make contact once I've reached the moon."
                    $ AddChatter(vig4_sc4_1_comment29)
                    amaS "Be seeing you, Mozely."
                    play audio "cutCall.wav" volume 1.5
                "This is for MAC.":
                    mS "But this isn't for you, or the Snakehawks."
                    mS "This is for MAC."
                    $ AddChatter(vig4_sc4_1_comment27)
                    mS "The Dragonflies put him at risk the second I left."
                    $ AddChatter(vig4_sc4_1_comment28)
                    mS "He's coming home."
                    amaS "Whatever gets you on board."
                    $ AddChatter(vig4_sc4_1_comment29)
                    amaS "I'll make contact once I've reached the moon."
                    amaS "Be seeing you, Mozely."
                    play audio "cutCall.wav" volume 1.5
    "BigCorp is coming for MAC. BigCorp is coming for MAC."
    "The engines of the Oakley spin up to speed as the ship begins to lift off the ground."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc4_1_comment30)
    mS "BigCorp is coming for MAC!"
    "I sprint out of the engine room and up to the cockpit."
    jump vig4_sc4_2

label vig4_sc4_2():
    show cockpit_stream at topleft onlayer background with dissolve
    show jennica stream neutral at stream_left with Dissolve(0.5)
    show teresa stream neutral at stream_right with Dissolve(0.5)
    hide ship_hallway_stream
    "I leap into the cockpit."
    mS "BigCorp is coming for MAC!"
    show teresa stream shock
    show jennica stream shock
    $ AddChatter(vig4_sc4_2_comment1)
    enS "Impossible, how would they even know Polaris exists?"
    mS "They tracked Coil's communications."
    $ AddChatter(vig4_sc4_2_comment2)
    pS "How do ya know that?"
    "I quickly explain my conversation with Ama to Jennica and Teresa."
    pS "It's possible BC tracked Coil's communications without him knowin'."
    enS "Even if it was a bluff to bait confirmation from you, BC would probably follow up on any lead they have."
    pS "And after Solara, Ama definitely ain't in the company's good graces anymore."
    show jennica stream neutral
    show teresa stream neutral
    $ AddChatter(vig4_sc4_2_comment3)
    if jennicaRomance == True:
        "Jennica turns to me."
        pS "So, how'd ya respond to Ama's proposal?"
        pS "Are we sidin' with the woman who's been huntin' us for the past month?"
    else:
        "Teresa turns to me."
        enS "So, how did you respond to Ama's proposal?"
        enS "Are we allying with the woman who's been hunting us for the past month?"
    stop music fadeout 2.0
    menu:
        "Are we allying with the woman who's been hunting us for the past month?"
        "I rejected her offer." if vig4_amaOffer == False:
            $ engineerApproval += 1
            $ pilotApproval += 2
            mS "No."
            mS "I told her she was living in the past and she was on her own."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc4_2_comment6)
            pS "Good. We can't trust her."
            enS "What does that mean for us? I assume we're not just letting BigCorp take MAC away?"
            $ AddChatter(vig4_sc4_2_comment8)
            pause 0.5
            $ AddChatter(vig4_sc4_2_comment9)
            pause 0.5
            $ AddChatter(vig4_sc4_2_comment10)
            menu:
                enS "What does that mean for us? I assume we're not just letting BigCorp take MAC away?"
                "We're going to defend Polaris.":
                    $ reactTarget = "vig4_sc4_amaofferrejectdefend"
                    show screen streamerCommentary
                    play music "soundtrack/polaris.wav"
                    $ vig4_defendPolaris = True
                    $ marshal += 3
                    $ csEngagement += 3
                    $ pdEngagement -= 2
                    mS "No, we're not."
                    $ AddChatter(vig4_sc4_2_comment11)
                    mS "BigCorp wants to wipe out freedom in the Outposts. We won't let them."
                    mS "Polaris has to stand firm."
                    $ AddChatter(vig4_sc4_2_comment12)
                    pS "That's the captain I know!"
                    enS "I don't like how they handled our situation, but they're better than BC, that's for sure."
                    hide screen streamerCommentary
                "We'll take MAC back on our own.":
                    $ reactTarget = "vig4_sc4_amaofferrejectattack"
                    show screen streamerCommentary
                    play music "soundtrack/theme.wav"
                    $ vig4_attackPolaris = True
                    $ outlaw += 3
                    $ csEngagement -= 2
                    $ pdEngagement += 3
                    mS "No, we're not."
                    $ AddChatter(vig4_sc4_2_comment13)
                    mS "The Dragonflies already compromised MAC's safety."
                    mS "We're going in and getting our boy back. On our own terms."
                    $ AddChatter(vig4_sc4_2_comment14)
                    pS "Hell yeah!"
                    enS "Let's go save our crew!"
                    hide screen streamerCommentary
        "I accepted her offer." if vig4_amaOffer == True:
            $ reactTarget = "vig4_sc4_amaofferaccept"
            show screen streamerCommentary
            play music "soundtrack/theme.wav" fadein 1.0
            $ engineerApproval -= 1
            $ pilotApproval -= 2
            $ vig4_attackPolaris = True
            mS "I accepted her offer."
            mS "We'll need her help if we're going to get MAC back."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc4_2_comment4)
            pS "I don't know, Cap. I don't like it."
            enS "Ama's selfish, not stupid, right?" 
            $ AddChatter(vig4_sc4_2_comment5)
            enS "She'll be more focused on this mission than revenge. At least for the time being."
            pS "True. Still, we oughta keep an eye on her."
            hide screen streamerCommentary
    jump vig4_sc4_3

label vig4_sc4_3():
    pS "Alright, I'll turn the ol' girl around."
    stop music fadeout 1.0
    play backAudio2 "shipAlarm.wav" volume 0.4 loop
    "Suddenly, a light above Teresa's head starts flashing red."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc4_3_comment1)
    show teresa stream shock
    enS "Uh, Jenn, what's this alarm for?"
    show jennica stream angry
    pS "Shit!"
    pS "Brace for impact, somethin' big is comin' in right on top of us!"
    show teresa stream neutral
    "Just as Jennica finishes her warning, it appears."
    play audio "exitHyperspace.wav" volume 2.5
    "A BC cruiser blasts directly out of hyperspace into Polaris's atmosphere."
    $ AddChatter(vig4_sc4_3_comment2)
    "It's immense, like a spearhead struck through the sky."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc4_3_comment3)
    "I have one second to take it in."
    show cockpit_stream with hpunch
    stop backAudio
    "Then the jet stream hits us."
    "Heavy winds from the cruiser's momentum pelt the Oakley, tossing it around in the air."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc4_3_comment4)
    "Teresa and I brace ourselves in our chairs as best we can."
    "Clenching her teeth, Jennica holds the helm."
    $ AddChatter(vig4_sc4_3_comment5)
    pS "C'mon girl, stay with me."
    "Sirens and alarms blare as lights flash all over the cockpit."
    "The ground is getting closer and closer as we spiral out of the air."
    pS "Stay with me."
    stop backAudio2
    "The engines fail."
    "We're in free-fall."
    pS "Brace for impact!"
    hide teresa with Dissolve(0.1)
    hide jennica with Dissolve(0.1)
    show cockpit_stream with vpunch
    play audio "shipCrash.wav" volume 2.0
    "The Oakley slams into the dirt and everything goes black."
    ##*streamer reaction here?
    #show bg black at topleft onlayer background with dissolve
    hide cockpit_stream with dissolve
    $ AddChatter(vig4_sc4_3_comment6)
    pause 0.5
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc4_3_comment7)
        pause 2.0
    jump vig4_sc5_0

label vig4_sc5_0():
    mS "So, what do we call the newest member of our crew?"
    enS "Something strong, stable, and sturdy. What about \"Beck\"?"
    $ AddChatter(vig4_sc5_0_comment1)
    pS "Nahhh, somethin' quick and agile. I say \"June\"."
    enS "I don't know, it's a bit quirky."
    $ AddChatter(vig4_sc5_0_comment2)
    pS "And yours ain't basic?"
    $ AddChatter(vig4_sc5_0_comment3)
    menu:
        pS "And yours ain't basic?"
        "We should decide together.":
            mS "Come on now. We have to decide together."
            enS "Well, what do you think, Captain?"
            pS "Yeah, Cap, what's your pick?"
        "Executive decision time.":
            mS "Alright, alright, while you two are bickering I guess I'll have to make the call."
            pS "Oh yeah? What are ya thinking, Cap?"
            enS "Yeah, what name would you pick?"
    "I look her up and down. Strong. Fast. Won't take any bullshit from anyone."
    mS "What about, \"Oakley\"?"
    $ AddChatter(vig4_sc5_0_comment4)
    enS "Hmm, I like it."
    pS "Yeah, it fits."
    mS "Alright crew, shall we climb aboard and set sail?"
    ###Could cut this next bit for time and to not have to do the picture###
    pS "Waitwaitwait, lemme take a picture."
    mS "Okay, but make it quick."
    enS "Is it counting down? I don't see a flash."
    pS "Should be all set."
    mS "Teresa, you're jabbing my ribs."
    enS "I'm sorry, I don't know how I should be posing."
    $ AddChatter(vig4_sc5_0_comment5)
    pS "Just act natural."
    enS "Posing is, fundamentally, not natural."
    enS "I've already told you Jenn, I don't li—{i}aaaaaahhh{/i}"
    pause 2.0
    ##*streamer reaction 
    jump vig4_sc5_1

label vig4_sc5_1():
    $ viewCheck6 = viewCount
    "I feel the throbbing first. Like my head is trying to kill me."
    play backAudio "fireBackground.wav" volume 0.6
    play backAudio2 "siren.wav" volume 0.2
    "Sounds start to wash over me, a dull roar punctuated by far off sirens."
    "There's an acrid smell in the air."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc5_1_comment1)
    mS "{b}*cough* *cough* *cough*{/b}"
    "My body lurches forward as I start to cough."
    stop backAudio2 fadeout 20.0
    $ AddChatter(vig4_sc5_1_comment2)
    if jennicaRomance == True:
        pS "Teresa! She's startin' to wake up!"
        "My eyes stutter open."
        show vig2_orbit_stream at topleft onlayer background with dissolve
        show jennica stream neutral at stream_left with dissolve
        "Jennica's smiling face is the first thing I see."
        $ AddChatter(vig4_sc5_1_comment3)
        menu:
            "Jennica's smiling face is the first thing I see."
            "Try to sit up.":
                mS "Jenn?"
                "I go to sit up."
                pS "Hey, hey, don't move. Ya need to rest."
            "What happened?":
                mS "Jenn?"
                mS "What happened?"
                pS "Don't worry about that, just stay still."
            "My love...":
                mS "Jenn, my love. Are you okay?"
                "Are those tears forming in her eyes?"
                $ AddChatter(vig4_sc5_1_comment4)
                pS "Yes, yes I'm okay, Moze."
                "She wipes her eyes on her sleeve."
                $ AddChatter(vig4_sc5_1_comment6)
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
                if viewershipHigh == True:
                    $ AddChatter(vig4_sc5_1_comment7)
                mS "That's an order."
                pS "Alright, Cap, just take it easy."
            "My head is killing me.":
                mS "My head is killing me, but I'll live."
                show teresa stream neutral
                enS "I've got something for that. Brace yourself."
                "Teresa stabs a thin needle into my neck."
                "Almost immediately, the throbbing in my head dissipates."
                if viewershipHigh == True:
                    $ AddChatter(vig4_sc5_1_comment8)
                enS "Better?"
                mS "Yeah, much."
                mS "Now help me up and tell me what happened."
    else:
        enS "Jenn! She's starting to wake up!"
        "My eyes stutter open."
        show vig2_orbit_stream at topleft onlayer background with dissolve
        show teresa stream happy at stream_right with dissolve
        "Teresa's smiling face is the first thing I see."
        $ AddChatter(vig4_sc5_1_comment3)
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
                $ AddChatter(vig4_sc5_1_comment5)
                enS "Yes, yes I'm okay, Moze."
                "She wipes her eyes on her sleeve."
                $ AddChatter(vig4_sc5_1_comment6)
                enS "But I need to take care of you right now. Just, stay still for me."
        pS "Oh thank god!"
        show jennica stream neutral at stream_left with dissolve
        "Jennica appears above me."
        pS "Jeez, Cap, ya had me worried there for a sec."
        pS "Teresa, she okay?"
        menu:
            pS "Teresa, she okay?"
            "I'm fine.":
                mS "I'm okay, both of you."
                show teresa stream neutral
                mS "Just help me up and tell me what happened."
                "The two look at each other."
                if viewershipHigh == True:
                    $ AddChatter(vig4_sc5_1_comment7)
                mS "That's an order."
                enS "Alright, Captain, just take it easy."
            "My head is killing me.":
                mS "My head is killing me, but I'll live."
                show teresa stream neutral
                enS "I've got something for that. Brace yourself."
                "Teresa stabs a thin needle into my neck."
                "Almost immediately, the throbbing in my head dissipates."
                if viewershipHigh == True:
                    $ AddChatter(vig4_sc5_1_comment8)
                enS "Better?"
                mS "Yeah, much."
                mS "Now help me up and tell me what happened."
    "They each grab one of my sides, and gingerly help me into a standing position."
    "Then I see it."
    "Ruin."
    show oakley_ruin at topleft onlayer background with dissolve
    hide vig2_orbit_stream
    "The Oakley is engulfed by an inferno."
    $ AddChatter(vig4_sc5_1_comment9)
    pause 0.5
    $ AddChatter(vig4_sc5_1_comment10)
    pause 0.5
    $ AddChatter(vig4_sc5_1_comment11)
    $ reactTarget = "vig4_sc5_oakleydestroyed"
    show screen streamerCommentary 
    "The flames envelop its hulking shell, licking at the metal."
    "Its frame, torn and rent, bends to the heat."
    "The smell of ship fuel coats the air."
    "An abyss opens in my heart."
    enS "I'm sorry, Moze. We got you out right before the whole thing went up."
    "Teresa's the only one who can talk."
    "I can feel Jennica shaking next to me."
    pS "Every time I turn around, I wish it weren't real."
    "She turns her back on the shell."
    "Teresa puts a hand on both of our shoulders."
    "We stand there. Motionless. Together. Slowly, imperceptibly getting closer and closer."
    "Until Teresa pulls us all into a hug."
    show teresa stream happy
    enS "She was a good girl."
    pS "The best."
    menu:
        pS "The best."
        "We'll never forget her.":
            mS "We'll never forget her."
            enS "Never."
            pS "Ain't no way."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc5_1_comment12)
            "We all take a deep breath as we let go of each other."
        "We have to get to MAC.":
            "Memories flood back to me. We're here for a reason."
            mS "She brought us all the way here. Now we have to finish this."
            mS "No more lost comrades."
            "Jennica and Teresa both take a deep breath as we let go of each other."
            enS "Affirmative."
            pS "Right."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc5_1_comment12)
    play audio "explosion.wav" volume 0.8
    "The immense sound of an explosion suddenly comes from over the ridge."
    show teresa stream shock
    show jennica stream shock
    hide screen streamerCommentary
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc5_1_comment13)
    mS "What was that?"
    show teresa stream neutral
    show jennica stream neutral
    enS "BC must have started the attack."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc5_1_comment14)
    "Teresa starts walking up a nearby slope."
    $ AddChatter(vig4_sc5_1_comment15)
    "I give one last look back at the Oakley, then Jennica gives me her arm for support."
    "I feel the heat on my back all the way up the hill."
    show targetbase_stream at topleft onlayer background with dissolve
    hide oakley_ruin
    play music "soundtrack/theme.wav"
    play backAudio "lazerFire.wav" volume 0.2
    play backAudio2 "siren.wav" volume 0.2
    "Polaris is under siege."
    "Smoke billows amongst the buildings."
    play audio "shipFlyBy.wav" volume 1.0
    "A handful of BigCorp drop ships careen over the town."
    $ AddChatter(vig4_sc5_1_comment16)
    play audio "explosion.wav" volume 0.7
    "One of them catches fire and crashes into the buildings below, exploding as it collides with the ground."
    "Jennica hands me a set of binoculars."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc5_1_comment17)
    "The outskirts are almost entirely ablaze."
    "A handful of blockades have been set up throughout the town."
    "The people of Polaris exchange blaster fire with BigCorp enforcers."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc5_1_comment18)
    "They've got defensible positions, but there's no way they can withstand a siege."
    "I follow the blockades toward the town center."
    $ AddChatter(vig4_sc5_1_comment19)
    "The plaza is still decorated as if in celebration, but tools of war now join the streamers and banners."
    "Vega stands on a rooftop, firing into BC enforcers who get close."
    "Turrets and weapons are being positioned around the area."
    "That's when I see him."
    mS "MAC!"
    show teresa stream shock
    show jennica stream shock
    enS "What!?"
    pS "Where!?"
    mS "He's in the plaza!"
    if macPeace > macViolence:
        $ csEngagement += 1
        $ kcEngagement += 1
        "Wounded townsfolk are laid out in rows on the ground."
        mS "MAC is going along with someone else, helping to administer first aid to the wounded."
        $ AddChatter(vig4_sc5_1_comment21)
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
        $ AddChatter(vig4_sc5_1_comment20)
        "He's firing at will, taking out some of the dropships before they can even reach the town."
        menu:
            "He's firing at will, taking out some of the dropships before they can even reach the town."
            "Not backing down from a fight.":
                mS "Not backing down from a fight, I see."
                mS "Proud of you, MAC."
            "Why is he there?":
                mS "Why the hell is he there?"
                mS "He shouldn't be anywhere near the frontline."
    "Then I see Coil. He stands in front of the plaza's tower."
    $ AddChatter(vig4_sc5_1_comment22)
    "Making eye contact with Vega, he shouts something and then enters the immense structure."
    show jennica stream neutral
    show teresa stream neutral
    pS "Cap, what's going on?"
    "I remove the binoculars."
    mS "It looks like the Dragonflies have set up a command center in the plaza at the center of town."
    mS "Coil went into the tower, but Vega is staying at the blockades and fighting off BC troops."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc5_1_comment23)
    mS "I don't think they're going to last much longer."
    if vig4_defendPolaris == True:
        pS "Well then, we better get down there!"
        show teresa stream think
        enS "Knowing Coil, he's probably working on a plan."
        enS "We have to make sure he can complete whatever he's got up his sleeve."
        mS "Agreed."
        $ AddChatter(vig4_sc5_1_comment24)
        show teresa stream neutral
        mS "It's time."
        if viewershipHigh == True or viewershipMed == True:
            $ AddChatter(vig4_sc5_1_comment25)
        menu:
            mS "It's time."
            "For MAC.":
                $ kcEngagement += 1
                mS "This is for MAC."
                mS "No one messes with our family."
                $ AddChatter(vig4_sc5_1_comment26)
            "For the Galaxy.":
                $ csEngagement += 1
                mS "This is for the Galaxy."
                mS "BigCorp doesn't own us and they never will."
                $ AddChatter(vig4_sc5_1_comment26)
            "For the Oakley.":
                mS "BC broke our ship."
                mS "Now we're going to break them."
                mS "This is for the Oakley."
                $ AddChatter(vig4_sc5_1_comment26)
        mS "Let's move."
        $ AddChatter(vig4_sc5_1_comment27)
        hide teresa with dissolve
        hide jennica with dissolve
        $ AddChatter(vig4_sc5_1_comment28)
        stop music fadeout 2.0
        "The three of us jog down the ridge, weapons drawn, heading directly for the heart of the fire."
        stop backAudio fadeout 1.0
        stop backAudio2 fadeout 1.0
        jump vig4_sc6_defend_1
    elif vig4_attackPolaris == True and vig4_amaOffer == False:
        pS "Alright, Cap, what's the play?"
        mS "We use the chaos to our advantage."
        mS "Things are going to be messy in there. Be on guard, stay close, and we'll figure things out together."
        enS "Roger."
        pS "Can do."
        $ AddChatter(vig4_sc5_1_comment24)
        mS "It's time."
        if viewershipHigh == True or viewershipMed == True:
            $ AddChatter(vig4_sc5_1_comment25)
        menu:
            mS "It's time."
            "For MAC.":
                $ kcEngagement += 1
                mS "This is for MAC."
                mS "No one messes with our family."
                $ AddChatter(vig4_sc5_1_comment26)
            "For the Galaxy.":
                $ csEngagement += 1
                mS "This is for the Galaxy."
                mS "BigCorp doesn't own us and they never will."
                $ AddChatter(vig4_sc5_1_comment26)
            "For the Oakley.":
                mS "BC broke our ship."
                mS "Now we're gonna break them."
                mS "This is for the Oakley."
                $ AddChatter(vig4_sc5_1_comment26)
        mS "Let's move."
        $ AddChatter(vig4_sc5_1_comment27)
        hide jennica with dissolve
        hide teresa with dissolve
        $ AddChatter(vig4_sc5_1_comment28)
        "The three of us jog down the ridge, weapons drawn, heading directly for the heart of the fire."
        stop music fadeout 2.0
        stop backAudio fadeout 1.0
        stop backAudio2 fadeout 1.0
        jump vig4_sc6_attack_1
    elif vig4_attackPolaris == True and vig4_amaOffer == True:
        jump vig4_sc5_2

label vig4_sc5_2():
    play music "soundtrack/deadeye.wav" volume 0.6 fadein 1.0
    amaS "Sounds like we have to make our move now."
    if jennicaRomance == False and teresaRomance == False and viewershipHigh == True:
        $ AddChatter(vig4_sc5_2_comment1)
    show ama stream neutral at stream_center with dissolve
    $ reactTarget = "vig4_sc5_amashowsup"
    show screen streamerCommentary
    "Perched on a rock higher up the ridge, Ama sits with a rifle relaxed against her shoulder."
    if jennicaRomance == False and teresaRomance == False and viewershipHigh == True:
        $ AddChatter(vig4_sc5_2_comment2)
    show ama stream happy
    amaS "Hello ladies. Good to see you all again."
    if jennicaRomance == False and teresaRomance == False and viewershipHigh == True:
        $ AddChatter(vig4_sc5_2_comment3)
    show jennica stream angry
    "Ama drops off the rock and struts up to us."
    $ AddChatter(vig4_sc5_2_comment4)
    show ama stream neutral
    enS "Reyes."
    amaS "Prismari."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc5_2_comment5)
    hide screen streamerCommentary
    amaS "Jenn, it's good to see you again."
    pS "Wish I could say the same, Ama."
    if viewershipLow == True:
        $ viewershipHigh = True
        $ viewershipLow = False
        $ viewershipMed = False
        $ viewCount += 7
        $ AddChatter(vig4_sc5_2_comment11)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment12)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment13)
        $ AddChatter(vig4_sc5_2_comment14)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment15)
        $ AddChatter(vig4_sc5_2_comment16)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment17)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment18)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment19)
        $ AddChatter(vig4_sc5_2_comment20)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment21)
        $ reactTarget = "vig4_sc5_viewershipBump"
        show screen streamerCommentary
    elif viewershipMed == True:
        $ viewershipHigh = True
        $ viewershipLow = False
        $ viewershipMed = False
        $ viewCount += 4
        $ AddChatter(vig4_sc5_2_comment13)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment14)
        $ AddChatter(vig4_sc5_2_comment16)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment19)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment20)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment17)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment18)
        pause 0.5
        $ AddChatter(vig4_sc5_2_comment21)
        $ reactTarget = "vig4_sc5_viewershipBump"
        show screen streamerCommentary
    show ama stream happy
    amaS "Judging by the lack of firearms pointed at my head, Mozely has told you about our deal."
    enS "She mentioned it."
    pS "Don't mean we're happy about it."
    amaS "But she's the captain, right?"
    "Jennica and Teresa don't say anything."
    amaS "You've built a good crew, Mozely." 
    "Ama puts a hand on my shoulder."
    amaS "I'm proud of you."
    hide screen streamerCommentary
    menu:
        amaS "I'm proud of you."
        "Get your hand off me.":
            $ deadeyeApproval -= 1
            mS "Get your hand off me, Ama."
            show ama stream confused
            "She calmly retracts her arm."
            $ AddChatter(vig4_sc5_2_comment6)
            mS "We're working together for this mission. But we're not friends."
            amaS "Understood."
            show ama stream neutral
        "I learned from the best.":
            $ deadeyeApproval += 1
            mS "I learned from the best."
            "Ama pats my shoulder twice."
            amaS "Flatterer."
            show ama stream neutral
            $ AddChatter(vig4_sc5_2_comment7)
    amaS "Let's move. Can't be wasting time."
    show jennica stream crossed
    show teresa stream upset
    show ama stream confused
    enS "Hold it."
    pS "We're not following you."
    pS "It's Cap's call."
    $ AddChatter(vig4_sc5_2_comment8)
    stop music fadeout 4.0
    show ama stream happy
    show jennica stream neutral
    show teresa stream neutral
    "All three women turn to look at me."
    amaS "Hahahaha true loyalty, how about that?"
    amaS "Alright then, \"Captain,\" what's the play?"
    mS "We use the chaos to our advantage."
    mS "Things are going to be messy in there. Be on guard, stay close, and we'll figure things out together."
    enS "Roger."
    pS "Can do."
    "Jennica and Teresa look at Ama."
    show ama stream neutral
    $ AddChatter(vig4_sc5_2_comment9)
    amaS "I'll behave, don't worry."
    $ AddChatter(vig4_sc5_1_comment24)
    mS "It's time."
    $ AddChatter(vig4_sc5_1_comment25)
    menu:
        mS "It's time."
        "For MAC.":
            $ kcEngagement += 1
            mS "This is for MAC."
            mS "No one messes with our family."
            $ AddChatter(vig4_sc5_1_comment26)
        "For the Snakehawks.":
            $ pdEngagement += 1
            mS "This is for the Snakehawks and a new dawn."
            $ AddChatter(vig4_sc5_1_comment26)
        "For the Galaxy.":
            $ csEngagement += 1
            mS "This is for the Galaxy."
            mS "BigCorp doesn't own us and they never will."
            $ AddChatter(vig4_sc5_1_comment26)
        "For the Oakley.":
            mS "BC broke our ship."
            mS "Now we're going to break them."
            mS "This is for the Oakley."
            $ AddChatter(vig4_sc5_1_comment26)
    mS "Let's move."
    stop music fadeout 2.0
    $ AddChatter(vig4_sc5_2_comment10)
    hide jennica with dissolve
    hide teresa with dissolve
    hide ama with dissolve
    $ AddChatter(vig4_sc5_1_comment28)
    "The four of us jog down the ridge, weapons drawn, heading directly for the heart of the fire."
    stop backAudio fadeout 1.0
    stop backAudio2 fadeout 1.0
    jump vig4_sc6_attack_1_ama





###The next sequence splits into two separate scripts: v4_script_sc6_attack and v4_script_sc6_defend
###These scripts reconnect at the next set of code in scene 7 (vig4_sc7_2)





label vig4_sc7_2():
    $ viewCheck9 = viewCount
    play music "soundtrack/decisionTime.wav" volume 1.0
    cS "The time has come."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_2_comment1)
        pause 0.5
    $ AddChatter(vig4_sc7_2_comment2)
    play audio "macAlarmed.wav" volume 1.5
    macS "Moze!"
    show mac stream neutral at stream_right5mac with Dissolve (0.3)
    "I whip around to see MAC careening toward the open door."
    play audio "shield.wav" volume 1.5
    #"{b}WHOOOSH!{/b}"
    "A blue veil of light flashes as MAC tries to cross the threshold, then gets knocked back."
    "An energy shield."
    $ AddChatter(vig4_sc7_2_comment3)
    show vega stream gun at stream_left5 with dissolve
    vS "Pops!"
    "Vega rushes up the stairs and kneels down to MAC's side."
    $ AddChatter(vig4_sc7_2_comment4)
    hide vega with dissolve
    hide mac with dissolve
    cS "Captain Moze."
    show streamview with hpunch
    play audio "shipFlyBy.wav" volume 0.7
    "A sudden shudder from the windows overlooking Polaris."
    show tower_no_star_ship_stream at topleft onlayer background with dissolve
    hide tower_no_star_stream
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_2_comment5)
    cS "This is your moment."
    play audio "explosion.wav" volume 0.4
    "Outside, dropships explode in the air."
    $ AddChatter(vig4_sc7_2_comment6)
    # show tower_glass windows
    cS "Within you is a war, between the forces of good and those of evil."
    show ama stream neutral
    amaS "Don't listen to this guy, kid."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_2_comment7)
    play audio "fireBackground.wav" volume 0.5
    "Fire dances in the streets below."
    cS "You have a choice. You can put an end to this madness."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_2_comment8)
    amaS "You can't trust him."
    $ AddChatter(vig4_sc7_2_comment9)
    "The cruiser looms high above."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_2_comment10)
    cS "Or fall to your baser instincts and doom us all."
    $ AddChatter(vig4_sc7_2_comment11)
    amaS "After all we've been through, Mozely..."
    $ AddChatter(vig4_sc7_2_comment12)
    "Battle rages."
    $ AddChatter(vig4_sc7_2_comment13)
    "Then I see it."    
    $ reactTarget = "vig4_sc7_starshower"
    show screen streamerCommentary
    show tower_star_shower_ship_stream at topleft onlayer background with dissolve
    hide tower_no_star_ship_stream    
    "An arc of pale green light shimmering over the cruiser."
    "Then another."
    "And another."
    "Dozens. Hundreds. Thousands of glimmering lights, streaking across the sky."
    "They collide with the cruiser, thousands of tiny impacts exploding all at once."
    "Dropships are obliterated before they can even reach Polaris."
    "The star shower has come, the world illuminated in turquoise light."
    $ AddChatter(vig4_sc7_2_comment14)
    cS "What will it be, Moze?"
    hide screen streamerCommentary
    menu:
        cS "What will it be, Moze?"
        "Save Coil.":
            $ csEngagement += 3
            $ kcEngagement -= 2
            $ pdEngagement -= 3
            mS "You're right, Coil. This has gone too far."
            $ AddChatter(vig4_sc7_2_comment23)
            if viewershipHigh == True or viewershipMed == True:
                pause 0.5
                $ AddChatter(vig4_sc7_2_comment24)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_2_comment25)
            $ AddChatter(vig4_sc7_2_comment26)
            "I turn to Ama."
            if jennicaRomance == False and teresaRomance == False:
                $ AddChatter(vig4_sc7_2_comment27)
                pause 0.5
            $ AddChatter(vig4_sc7_2_comment28)
            stop music fadeout 1.0
            menu:
                "I turn to Ama."
                "It's over.":
                    $ AddChatter(vig4_sc7_2_comment31)
                    mS "Ama, it's over."
                "I'm sorry.":
                    $ AddChatter(vig4_sc7_2_comment31)
                    mS "Ama, I'm sorry."
            $ AddChatter(vig4_sc7_2_comment29)
            show ama stream angry
            "Ama glares at me, then Coil. Then her gaze falls back to me."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_2_comment30)
            "I can feel the hate like a heatwave."
            jump vig4_sc7_3_coil
        "Help Ama.":
            $ csEngagement -= 2
            $ kcEngagement += 2
            $ pdEngagement += 3
            mS "You're right, Ama. I can't trust him."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_2_comment15)
                pause 0.5
                $ AddChatter(vig4_sc7_2_comment16)
                pause 0.5
            $ AddChatter(vig4_sc7_2_comment17)
            $ AddChatter(vig4_sc7_2_comment18)
            "I turn to Coil."
            if jennicaRomance == False and teresaRomance == False:
                $ AddChatter(vig4_sc7_2_comment19)
                pause 0.5
            $ AddChatter(vig4_sc7_2_comment20)
            stop music fadeout 1.0
            menu:
                "I turn to Coil."
                "It's over.":
                    $ AddChatter(vig4_sc7_2_comment32)
                    mS "Coil, it's over."
                "I'm sorry.":
                    $ AddChatter(vig4_sc7_2_comment32)
                    mS "Coil, I'm sorry."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_2_comment21)
            "Coil sighs."
            $ AddChatter(vig4_sc7_2_comment22)
            cS "So be it."
            jump vig4_sc7_3_ama

label vig4_sc7_3_ama():
    # play badass climax music
    play music "soundtrack/finale.wav" volume 1.0
    "Everyone is still."
    show ama stream upset
    "Ama makes the first move, dropping her rifle and lunging at Coil."
    "He leans to the side, faster than I would expect his elderly physique to move."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_ama_comment1)
    menu:
        "He leans to the side, faster than I would expect his elderly physique to move."
        "Jump Coil.":
            "I leap at Coil, throwing a kick at his exposed side."
            $ AddChatter(vig4_sc7_3_ama_comment2)
            play audio "shield.wav" volume 1.0
            "It slows slightly at his shield, but doesn't stop completely."
            "He quickly spins away."
            $ AddChatter(vig4_sc7_3_ama_comment3)
        "Shoot Coil.":
            play audio "shield.wav" volume 1.0
            "I raise my pistol and fire two quick shots, but they dissipate into his shields."
            $ AddChatter(vig4_sc7_3_ama_comment2)
            cS "You should know that won't work, dear."
            $ AddChatter(vig4_sc7_3_ama_comment3)
    amaS "Over here!"
    "Ama continues her barrage, drawing a knife and stabbing at Coil's head."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_ama_comment4)
    "He dodges and leans away from the blade, then crouches into a stance with his palms open outward toward Ama."
    "Devices like shield generators are strapped to his palms."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_ama_comment5)
    hide ama with dissolve
    play audio "energyPulse.wav" volume 1.2
    "A burst of energy suddenly blasts from his palms, striking Ama in the chest and sending her and her knife flying."
    $ AddChatter(vig4_sc7_3_ama_comment6)
    "Sweat drips from my forehead."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_ama_comment7)
    "Coil's posture straightens. He starts to circle around me."
    "I parallel his movements, keeping us at a distance."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_ama_comment8)
    cS "I don't know what kind of life you think I've led."
    cS "But you're mistaken if you think I've been cooped up in a lab all these years."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_ama_comment9)
    menu:
        cS "But you're mistaken if you think I've been cooped up in a lab all these years."
        "Why don't you tell me about it?":
            mS "Oh yeah? Sounds interesting. Why don't you monologue about it."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_3_ama_comment10)
            cS "Just waiting for your friend."
        "Don't think you're invincible.":
            mS "You have a weakness, and we're going to exploit it."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_3_ama_comment10)
            cS "I'm sure you will."
    show ama stream death at stream_left with dissolve
    "Ama puts a hand on my shoulder."
    "Her other hand is holding her side."
    $ AddChatter(vig4_sc7_3_ama_comment11)
    show ama stream upset
    amaS "Sorry, kid, took a bad knock there. But I'm back in the hunt."
    amaS "Seems like guns won't work here. We'll have to do this the old-fashioned way."
    $ AddChatter(vig4_sc7_3_ama_comment12)
    play audio "macAlarmed.wav" volume 1.5
    macS "Captain!"
    show mac stream neutral at stream_center_mac with Dissolve(0.3)
    "MAC is just behind the energy shield, watching intently."
    "Vega is behind him, her hands covering her mouth."
    $ AddChatter(vig4_sc7_3_ama_comment13)
    macS "Be careful! Coil's shield generators are both defense {i}and{/i} offensive weapons!"
    $ AddChatter(vig4_sc7_3_ama_comment14)
    amaS "Yeah, we got that!"
    hide mac with dissolve
    "Coil takes a step towards us."
    cS "Do you even know what it means to sacrifice?"
    $ AddChatter(vig4_sc7_3_ama_comment15)
    "Another step."
    cS "All you do is take for yourself."
    $ AddChatter(vig4_sc7_3_ama_comment16)
    "Ama and I crouch into a ready stance."
    cS "You have no conviction."
    $ AddChatter(vig4_sc7_3_ama_comment17)
    menu:
        cS "You have no conviction."
        "Feint and let Ama take the lead.":
            cS "I also grew up in this galaxy."
            "I feint toward, Coil, catching his attention while Ama rushes him head on."
            "She pushes him back, not giving him room to fire his energy pulses."
            $ AddChatter(vig4_sc7_3_ama_comment18)
            "I rush past the two of them, trying to hit Coil from the back."
            "As I approach, he opens one palm in either of our directions."
            cS "I also know what it means to lose the ones you love."
            "I dive to the side, but Ama's already committed to an attack."
            play audio "energyPulse.wav" volume 1.2
            "The energy pulse rushes by me. But another one hits Ama directly in the chest, knocking her to the floor."
            hide ama with dissolve
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_3_ama_comment19)
            cS "And I know what it means to continue on in their stead."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_3_ama_comment20)
            "I'm on the floor facing Coil. He opens a palm in my direction."
            $ AddChatter(vig4_sc7_3_ama_comment21)
            "I don't have time to stand."
        "Charge and let Ama be back up.":
            "I charge in at Coil's side with a fist, while Ama pulls another knife from her boot and crosses behind me."
            "It's a classic move."
            play audio "shield.wav" volume 1.0
            "Coil steps into my attack, slowing my movement just enough to mess up my timing, then spins away."
            $ AddChatter(vig4_sc7_3_ama_comment18)
            cS "I also grew up in this galaxy."
            "Ama lunges at him with the knife."
            play audio "energyPulse.wav" volume 1.2
            "He opens one palm and hits her with an energy blast, knocking her to the floor."
            hide ama with dissolve
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_3_ama_comment19)
            cS "I also know what it means to lose the ones you love."
            "Coil takes aim at me."
            play audio "energyPulse.wav" volume 1.2
            "I dive out of the way as a pulse of energy rushes by me."
            cS "And I know what it means to continue on in their stead."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_3_ama_comment20)
            "I'm on the floor facing Coil. He opens a palm in my direction."
            $ AddChatter(vig4_sc7_3_ama_comment21)
            "I don't have time to stand."
    amaS "Moze!"
    show ama stream upset at stream_left with Dissolve(0.2)
    show ama stream upset at stream_right with move
    show ama stream upset with hpunch
    "Ama leaps in front of Coil, and thrusts her hand forward."
    play audio "energyPulse.wav" volume 1.2
    "A blast of energy slams her back to the floor."
    hide ama with Dissolve(0.5)
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_ama_comment22)
        pause 0.5
    $ AddChatter(vig4_sc7_3_ama_comment23)
    pause 0.5
    $ AddChatter(vig4_sc7_3_ama_comment24)
    mS "Ama!"
    cS "{i}aagghhhh!{/i}"
    "Then I notice it, a knife impaled through one of Coil's hands."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_ama_comment25)
    "Blood streaks down his arm. The device in his palm short circuits."
    "The thin veil of blue light around him sparks inconsistently."
    "Ama is motionless on the floor."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_ama_comment26)
    show coil stream neutral at stream_center with move
    "Coil and I lock eye contact."
    "Behind him, the ruin of the BC cruiser lists toward the ground of Polaris as the star shower pummels its hull."
    cS "Will you do what you have to do?"
    menu:
        cS "Will you do what you have to do?"
        "I will do what I want.":
            $ pdEngagement += 2
            $ kcEngagement += 1
            mS "No."
            mS "I want this."
            $ AddChatter(vig4_sc7_3_ama_comment27)
            "Coil nods."
            cS "Of course."
        "You gave me no choice.":
            $ pdEngagement -= 1
            $ kcEngagement -= 1
            mS "You didn't give me a choice."
            "Coil chuckles."
            cS "We always have a choice, Moze."
            $ AddChatter(vig4_sc7_3_ama_comment28)
    "I step forward."
    play audio "energyPulse.wav" volume 0.6
    "He raises his good hand toward me and fires a pulse."
    "But it's taking longer for the energy blast to charge. I easily dodge it."
    play audio "punch.wav" volume 1.0
    "My fist strikes his chest with barely any resistance."
    "Ramming my knee into his groin, I grab his coat by the back and throw him across the floor."
    "He tumbles and slams into the side of the wall."
    $ AddChatter(vig4_sc7_3_ama_comment29)
    vS "Pops! Get up!"
    $ AddChatter(vig4_sc7_3_ama_comment30)
    "I cross the room and stand over Coil."
    vS "Get up! Please!"
    "Coil reaches out his good hand."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_ama_comment31)
    play audio "energyPulse.wav" volume 0.6
    "I step back as the energy pulse sails harmlessly into the ceiling."
    stop music fadeout 4.0
    "Coil staggers to his feet."
    cS "Please. Just let her go."
    menu:
        cS "Please. Just let her go."
        "Your sins are hers.":
            $ outlaw += 1
            $ macViolence += 1
            mS "Your sins are hers."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_3_ama_comment32)
            cS "My sins?"
            "Coil chuckles."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_3_ama_comment33)
            cS "You don't know the half of them."
        "Would you, if you were me?":
            mS "Would you, if you were me?"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_3_ama_comment34)
            cS "I am not you."
            $ AddChatter(vig4_sc7_3_ama_comment35)
    "Coil lunges forward, ripping the knife out of his hand and slashing it toward my head."
    $ AddChatter(vig4_sc7_3_ama_comment36)
    "Blood spatters across my face."
    "But I don't blink."
    "I catch his wrists in my hands. And grip. Tight."
    "I can hear his bones cracking."
    "He drops to his knees."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_ama_comment37)
    "I turn his wrists. The knife points directly at his throat."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_ama_comment38)
        pause 0.5
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_ama_comment39)
    "He closes his eyes."
    cS "Elijah... Is that you?"
    "I thrust the blade forward."
    play audio "deathGasp.wav" volume 1.5
    "Coil's body slumps to the floor."
    "Blood pools around his throat."
    $ AddChatter(vig4_sc7_3_ama_comment40)
    pause 0.5
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_ama_comment41)
        pause 0.5
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_ama_comment42)
    $ reactTarget = "vig4_sc7_killcoil"
    show screen streamerCommentary
    "His eyes go cold. But there's an odd light to them. As if he was smiling."
    hide coil with Dissolve(2.0)
    show vega stream upset at stream_left with dissolve
    vS "No!"
    "The energy shield at the doorway dissipates. Vega rushes to Coil's side."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_ama_comment43)
    "She pulls his head into her lap."
    $ AddChatter(vig4_sc7_3_ama_comment44)
    vS "No. Don't go. Don't go. Don't leave me."
    $ AddChatter(vig4_sc7_3_ama_comment45)
    "Ama."
    hide vega with dissolve
    show ama stream death at stream_right with dissolve
    "I rush over to Ama's body and turn her onto her side."
    amaS "Ahhh, shit."
    hide screen streamerCommentary
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_ama_comment46)
    "She opens her eyes and looks right into mine."
    amaS "Did we get him?"
    menu:
        amaS "Did we get him?"
        "I did.":
            $ deadeyeApproval += 1
            mS "Well, I did the hard work."
            show ama stream happy
            amaS "Bullshit, you would've been toast if I didn't stab the old man."
        "Yes, we got him.":
            mS "Yeah, we got him."
            show ama stream happy
            amaS "Good. Old man was a pain in the ass."
    "Gingerly, I help Ama into a sitting position. She glances to the side."
    show ama stream neutral
    "MAC hasn't entered the room yet."
    amaS "Time to rebuild your family."
    $ AddChatter(vig4_sc7_3_ama_comment47)
    mS "Don't you mean our family?"
    "Ama shakes her head."
    $ AddChatter(vig4_sc7_3_ama_comment48)
    amaS "You were right. Snakehawks are dead."
    amaS "Right now, you have to rebuild the Oakley. I don't know if I fit that picture."
    $ AddChatter(vig4_sc7_3_ama_comment49)
    menu:
        amaS "Right now, you have to rebuild the Oakley. I don't know if I fit that picture."
        "You belong." if vig4_amaOffer == True:
            $ vig4_amaCrew = True
            mS "If you want a place in the crew, it's not too late."
            show ama stream happy
            $ AddChatter(vig4_sc7_3_ama_comment53)
            amaS "Heh, after all I've done? Jenn and Teresa will probably have something to say about that."
            $ AddChatter(vig4_sc7_3_ama_comment54)
            amaS "But I'll give it time. Not in any rush anymore."
            if deadeyeApproval < 4:
                $ AddChatter(vig4_sc7_3_ama_comment55)
            "An unbearable groaning sound suddenly reverberates across Polaris."
        "You're right.":
            $ vig4_amaCrew = False
            mS "You're right. But we're grateful for your help."
            show ama stream happy
            $ AddChatter(vig4_sc7_3_ama_comment53)
            amaS "Aah, you'll find some way to repay me I'm sure."
            $ AddChatter(vig4_sc7_3_ama_comment54)
            amaS "I know you never let a score go unsettled."
            if deadeyeApproval < 4:
                $ AddChatter(vig4_sc7_3_ama_comment55)
            "An unbearable groaning sound suddenly reverberates across Polaris."
        "I don't want to live without you." if deadeyeApproval >= 4 and vig4_amaOffer == True and jennicaRomance == False and teresaRomance == False:
            $ vig4_amaCrew = True
            mS "Ama, I don't want to live without you."
            "She looks at me, almost confused."
            show ama stream confused
            amaS "Mozely, I don't know what you're saying."
            menu:
                amaS "Mozely, I don't know what you're saying."
                "I love you, Ama.":
                    $ kcEngagement += 3
                    $ pdEngagement += 2
                    $ csEngagement += 1
                    $ amaRomance = True
                    mS "Ama, I love you."
                    mS "I know it doesn't make sense, bu—"
                    show ama stream happy
                    "She grabs my face with her two hands and pulls me into a kiss."
                    $ AddChatter(vig4_sc7_3_ama_comment57)
                    "I wrap my arms around her."
                    $ AddChatter(vig4_sc7_3_ama_comment58)
                    "In the distance, I hear an immense groaning sound that reverberates across Polaris."
                    $ AddChatter(vig4_sc7_3_ama_comment59)
                    if viewershipHigh == True or viewershipMed == True:
                        pause 0.5
                        $ AddChatter(vig4_sc7_3_ama_comment60)
                    "But I can't turn away."
                    "I'm enmeshed in this moment, this feeling, this heat."
                    "Finally, we separate."
                "Neither do I.":
                    $ kcEngagement -= 2
                    $ pdEngagement -= 1
                    mS "I don't either."
                    $ AddChatter(vig4_sc7_3_ama_comment56)
                    mS "But stick around, and we'll figure it out."
                    show ama stream happy
                    amaS "I guess I can manage that."
                    "An unbearable groaning sound suddenly reverberates across Polaris."
    play audio "explosion.wav" volume 1.5
    "We glance out the windows to watch as the hulk of the BC cruiser crumbles into flames."
    $ AddChatter(vig4_sc7_3_ama_comment61)
    amaS "Not bad, Moze. Not bad at all."
    "She tilts her head at MAC."
    show ama stream neutral
    amaS "Now go. He needs you."
    $ vig4_sc7_3_ama_comment56.click = False
    $ AddChatter(vig4_sc7_3_ama_comment62)
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
            mS "Are you glad to see me?"
            macS "I think so. But I am still processing the events I have witnessed."
            mS "MAC, can you ever forgive me?"
    "MAC looks down for a moment, then back up to my face."
    play audio "macSad.wav" volume 1.5
    macS "Am I a Snakehawk now?"
    "I smile."
    mS "Better, you're family."
    "MAC's face turns into a smile."
    macS "I'm glad to be with my family again."
    "I drop to my knees as he rushes into my arms."
    "I hold him tight and drop my face against his body."
    $ AddChatter(vig4_sc7_3_ama_comment63)
    mS "I missed you."
    $ AddChatter(vig4_sc7_3_ama_comment64)
    play audio "macHum.wav" volume 1.5
    macS "I missed you too, Moze."
    $ AddChatter(vig4_sc7_3_ama_comment65)
    "We step back and I stand up."
    show ama stream neutral at stream_right with dissolve
    amaS "Hate to ruin the moment, but we have one more piece of business to take care of."
    $ AddChatter(vig4_sc7_3_ama_comment66)
    "Ama is standing now. She points across the room."
    show vega stream upset at stream_left with dissolve
    "Vega sits, still cradling Coil's head in her hands."
    $ AddChatter(vig4_sc7_3_ama_comment67)
    "The tears that were streaking down her face have stopped."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_ama_comment68)
    "She is completely silent, staring into Coil's eyes."
    macS "Captain."
    macS "As a member of the Oakley family, may I request to handle this situation."
    menu:
        macS "As a member of the Oakley family, may I request to handle this situation."
        "Go ahead.":
            mS "Go on, MAC. Whatever you think is best."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_ama_comment69)
    "MAC turns and rolls toward Vega."
    $ AddChatter(vig4_sc7_3_ama_comment70)
    "As he approaches, she turns her attention toward him."
    vS "I won't let you get away with this."
    $ AddChatter(vig4_sc7_3_ama_comment71)
    "Her words are stiff."
    vS "You know that, right?"
    $ AddChatter(vig4_sc7_3_ama_comment72)
    macS "I know."
    if macViolence > macPeace:
        $ pdEngagement += 2
        $ kcEngagement += 1
        $ csEngagement -= 2
        $ vig4_MACKill = True
        play audio "lazer.wav" volume 5.0
        "MAC lifts his arm and fires a bolt of energy."
        "It lands square between Vega's eyes."
        "She slumps to the ground, her body falling on top of Coil's."
        $ AddChatter(vig4_sc7_3_ama_comment73)
        pause 0.5
        if viewershipHigh == True:
            $ AddChatter(vig4_sc7_3_ama_comment74)
        $ AddChatter(vig4_sc7_3_ama_comment75)
        hide vega with Dissolve(2.0)
        $ reactTarget = "vig4_sc7_mackillsvega"
        show screen streamerCommentary
        macS "Threat. Neutralized."
        $ AddChatter(vig4_sc7_3_ama_comment77)
        pause 0.5
        $ AddChatter(vig4_sc7_3_ama_comment78)
    else:
        $ pdEngagement += 1
        $ kcEngagement += 3
        $ csEngagement += 1
        macS "You have as much right to vengeance as they did."
        macS "But not today."
        if viewershipHigh == True:
            $ AddChatter(vig4_sc7_3_ama_comment79)
        macS "And maybe, in time, you will find peace."
        vS "There is no peace left. You took it all away."
        macS "Perhaps. But we can't know for certain."
        $ reactTarget = "vig4_sc7_macsparesvega"
        show screen streamerCommentary
        $ AddChatter(vig4_sc7_3_ama_comment80)
        macS "Bury your family, Vega. And take care."
        $ AddChatter(vig4_sc7_3_ama_comment81)
        "Vega doesn't say anything. She looks back to Coil's face, unmoving."
        hide vega with dissolve
    "MAC rolls up to me and Ama."
    play audio "macNeutral.wav" volume 1.5
    macS "We should go."
    mS "Yeah, we should."
    "Together, MAC, Ama, and I leave the room, and descend the tower."
    hide screen streamerCommentary
    hide ama with dissolve
    hide mac with dissolve
    jump vig4_epilogue_ama

label vig4_sc7_3_coil():
    #play badass climax music
    play music "soundtrack/finale.wav" volume 1.0
    "Everyone is still."
    show ama stream gun
    "Ama makes the first move, raising her rifle in my direction."
    $ AddChatter(vig4_sc7_3_coil_comment1)
    menu:
        "Ama makes the first move, raising her rifle in my direction."
        "Rush her.":
            "I lunge forward and grab the rifle, aiming it to the side."
            play audio "lazer.wav" volume 5.0
            "A round fires off, sailing into the ceiling above."
            "I reach for my pistol and pull it from the holster, but Ama quickly grabs me by the side and throws me to the ground."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_3_coil_comment2)
            "My pistol skids across the floor as I roll to a stop and look up."
        "Draw pistol.":
            "I draw my pistol."
            play audio "lazer.wav" volume 5.0
            "Before I can fire a shot though, a bullet from Ama strikes the pistol clean through, breaking the weapon."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_3_coil_comment2)
            amaS "Ah ah ah, can't end things too quickly, Mozely." 
    "Ama lifts the rifle to aim at me again."
    "Coil reaches his hands forward. Devices like shield generators are strapped to his palms."
    play audio "energyPulse.wav" volume 1.2
    "A burst of energy suddenly blasts from them, striking Ama's rifle and rending it to pieces."
    show ama stream angry
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_coil_comment3)
    "She takes a moment to look at the destroyed gun, then tosses it to the side."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_coil_comment4)
    amaS "Well aren't you just full of surprises?"
    cS "Don't assume that I've spent my entire life cooped up in a lab."
    "Ama straightens her back and cracks her knuckles."
    $ AddChatter(vig4_sc7_3_coil_comment5)
    "Ama charges in my direction as Coil's blasters charge."
    play audio "energyPulse.wav" volume 1.2
    "But it's a feint."
    "As the energy releases, Ama doubles back, heading toward Coil, while the energy blasts sail wide of her."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_coil_comment6)
    "Before Coil can move, Ama has closed the distance and swings."
    "It's a haymaker, and Coil wasn't ready."
    play audio "punch.wav" volume 1.5
    hide coil with Dissolve(0.3)
    "The blow is slowed by his shield, but the collision still sends Coil to the ground, sliding to a wall."
    $ AddChatter(vig4_sc7_3_coil_comment7)
    vS "Pops!"
    "Ama draws a knife from her boot."
    show ama stream happy
    amaS "Now then, Mozely. Where were we?"
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_coil_comment8)
    menu:
        amaS "Now then, Mozely. Where were we?"
        "I was busy killing you.":
            mS "I was in the middle of killing your sorry excuse for a hunter."
        "You were about to surrender.":
            mS "I think you were about to surrender."
    amaS "Hah! Isn't that rich?"
    show ama stream angry
    "Flicking the knife back and forth, Ama steps close to me and crouches into a fighting stance."
    $ AddChatter(vig4_sc7_3_coil_comment9)
    play audio "macAlarmed.wav" volume 1.5
    macS "Moze, be careful!"
    $ AddChatter(vig4_sc7_3_coil_comment10)
    amaS "All this chaos, this mess of your own making."
    amaS "Is this what you wanted, Mozely?"
    menu:
        amaS "Is this what you wanted, Mozely?"
        "I just wanted a family.":
            mS "I just wanted a family! That's all I ever wanted."
            $ AddChatter(vig4_sc7_3_coil_comment11)
            amaS "Good. Now you're going to watch me take it from you."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_3_coil_comment13)
        "I just want you to shut up.":
            mS "I just want you to shut up!"
            $ AddChatter(vig4_sc7_3_coil_comment12)
            amaS "Gladly."
    "Ama lunges with the knife."
    "I block and retaliate."
    "Lightning blows as we trade strikes."
    $ AddChatter(vig4_sc7_3_coil_comment14)
    "It's like how we trained together years ago on her ship."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_coil_comment15)
    "I see her now as I did then."
    "Fierce. Powerful. Dominant."
    "Overconfident."
    menu:
        "Overconfident."
        "Bait her into an attack.":
            "Time for a trick."
            "As she approaches for another strike, I let my left foot slip just a tad."
            $ AddChatter(vig4_sc7_3_coil_comment16)
            "She sees weakness, and pounces for the kill."
            "But it's a feint. I shift my weight to the side and swing my knife up toward her chest."
        "Go for an old reliable.":
            "There's an old reliable move."
            "As she approaches for another strike, I shift my weight to the side. Just slightly."
            $ AddChatter(vig4_sc7_3_coil_comment16)
            "The blade arcs throug the air, scratching my face."
            "But now there's an opening."
            "I swing my knife up toward her chest."
    play audio "punch.wav" volume 1.5
    "Ama's knee slams into my jaw before I realize what happened."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_coil_comment17)
    "She baited me."
    "I go tumbling across the floor."
    play audio "macAlarmed.wav" volume 1.5
    macS "Captain!"
    "I'm stunned, flat on my back on the ground."
    $ AddChatter(vig4_sc7_3_coil_comment18)
    "Ama steps up to me."
    show ama stream upset
    amaS "Ungrateful child!"
    amaS "After everything I did for you, all that I taught you."
    amaS "And you just throw it away!"
    amaS "Why couldn't you just listen to me!?"    
    "Ama crouches just above me, tilting her head sideways."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_coil_comment19)
    "Movement slowly starts to come back to my fingers."
    $ AddChatter(vig4_sc7_3_coil_comment20)
    amaS "Everything would have been fine. Would have been {i}good{/i}!"
    $ AddChatter(vig4_sc7_3_coil_comment21)
    "She exhales deeply."
    amaS "Remember, Mozely: you chose this."
    "She reaches her hand into the air, knife pointed straight at my chest."
    cS "No!"
    play audio "energyPulse.wav" volume 1.2
    "There's a bright streak across my vision as an energy pulse collides with Ama's chest."
    hide ama with dissolve
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_coil_comment22)
    show ama stream angry
    amaS "Maker—you're going to regret that old man."
    play backAudio "energyPulse.wav" volume 0.7
    play backAudio2 "repeatedPunches.wav" volume 0.8
    "I can't turn my head but I hear the sounds of battle to my right."
    "The charge of Coil's energy pulses, the sound of Ama's fists hitting flesh."
    vS "Pops!"
    play audio "macPester.wav" volume 1.5
    macS "Moze! Get up! Get up!"
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_coil_comment23)
    stop backAudio fadeout 1.0
    stop backAudio2 fadeout 1.0
    "Finally, I push myself into a sitting position."
    show ama stream neutral at stream_center with dissolve
    show coil stream neutral at stream_left with dissolve
    "Just in time to see Ama plunge her knife into Coil's chest."
    vS "No!"
    "Coil slumps to the ground, his back leaning against the wall."
    $ AddChatter(vig4_sc7_3_coil_comment24)
    hide coil with Dissolve(0.6)
    show ama stream death
    "Ama holds her side. One of her arms is almost limp."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_coil_comment25)
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
            $ AddChatter(vig4_sc7_3_coil_comment26)
            "Ama nods."
            show ama stream upset
            amaS "Good."
        "You gave me no choice.":
            $ pdEngagement -= 1
            $ kcEngagement -= 1
            mS "You didn't give me a choice."
            $ AddChatter(vig4_sc7_3_coil_comment27)
            show ama stream happy
            "Ama chuckles."
            amaS "Classic Mozely."
    show ama stream angry
    amaS "Let's finish it."
    "Resolve beats through my heart."
    "I step forward."
    "Ama swings her good arm at me."
    "But she's slow now."
    play audio "punch.wav" volume 1.2
    "I easily dodge it and thrust my fist into her chest."
    "Ramming my knee into her groin, I grab her by the back and throw her across the floor."
    "She tumbles and slams into the side of the wall."
    show ama stream death
    $ AddChatter(vig4_sc7_3_coil_comment28)
    "I cross the room and stand over Ama."
    "Gasping for air, she leans onto her back."
    $ AddChatter(vig4_sc7_3_coil_comment29)
    mS "Get up."
    stop music fadeout 4.0
    "Ama exhales, then turns onto her stomach and pushes herself to a standing position."
    amaS "Well, kid. Looks like our time's up."
    amaS "Will you take care of my ship?"
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_coil_comment30)
    menu:
        amaS "Will you take care of my ship?"
        "No.":
            mS "No. I want nothing to do with you."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_3_coil_comment31)
            "Ama nods."
            amaS "Fair."
        "You mean my ship.":
            mS "You mean {i}my{/i} ship."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_3_coil_comment32)
            "Ama nods."
            amaS "At least you learned something."
            $ AddChatter(vig4_sc7_3_coil_comment33)
    "Ama reaches down and pulls a blaster from her boot."
    $ AddChatter(vig4_sc7_3_coil_comment34)
    "But I don't blink."
    "I catch her wrist in my hands, pointing the blaster to the side."
    play audio "lazer.wav" volume 5.0
    #"She fires."
    "The bolt goes wide."
    "I hold her wrist, and grip. Tight."
    "I can hear her bones cracking."
    "She drops to her knees."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_coil_comment35)
    "I turn her wrist until the gun is pointed directly at her head."
    $ AddChatter(vig4_sc7_3_coil_comment36)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter(vig4_sc7_3_coil_comment37)
    "I place my finger over the trigger."
    "She looks me straight in the eyes."
    amaS "Be seeing you, Mozely."
    "I pull the trigger."
    play audio "lazer.wav" volume 5.0
    "Ama's body slumps to the floor."
    "Her eyes are cold. Lifeless."
    $ AddChatter(vig4_sc7_3_coil_comment38)
    pause 0.5
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_coil_comment39)
        pause 0.5
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_coil_comment40)
    "Dead."
    $ reactTarget = "vig4_sc7_killama"
    show screen streamerCommentary
    hide ama with Dissolve(2.0)
    show vega stream upset at stream_center with dissolve
    vS "Pops!"
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_coil_comment41)
    "The energy shield dissipates. Vega rushes to Coil's side."
    vS "No. Don't go. Don't go. Don't leave me."
    show coil stream neutral at stream_left with dissolve
    "Coil opens his eyes."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_coil_comment42)
    cS "It is okay, Vega."
    "Coil grips the blade with his hands and pulls it out."
    "A small spurt of blood pools in his shirt."
    cS "The blade did not cut too deep."
    hide screen streamerCommentary
    $ AddChatter(vig4_sc7_3_coil_comment43)
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_3_coil_comment44)
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
    play audio "explosion.wav" volume 1.5
    "We glance out the windows to watch as the hulk of the BC cruiser crumbles into flames."
    $ AddChatter(vig4_sc7_3_coil_comment45)
    "Coil glances to the side."
    show mac stream neutral at stream_right_mac with dissolve
    "MAC still hasn't crossed into the room yet."
    "Coil nods in his direction."
    $ AddChatter(vig4_sc7_3_coil_comment46)
    cS "Go on. He needs you."
    $ AddChatter(vig4_sc7_3_coil_comment47)
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
    play audio "macSad.wav" volume 1.5
    macS "Am I a Snakehawk now?"
    "I smile."
    mS "Better, you're family."
    "MAC's face turns into a smile."
    macS "I'm glad to be with my family again."
    "I drop to my knees as he rushes into my arms."
    "I hold him tight and drop my face against his body."
    $ AddChatter(vig4_sc7_3_coil_comment48)
    mS "I missed you."
    $ AddChatter(vig4_sc7_3_coil_comment49)
    play audio "macHum.wav" volume 1.5
    macS "I missed you too, Moze."
    $ AddChatter(vig4_sc7_3_coil_comment50)
    "We step back and I stand up."
    show coil stream neutral at stream_right with dissolve
    show vega stream happy at stream_left with dissolve
    "Coil leans against Vega as the two approach."
    vS "So, Pops, how's Moze's case for joining the Dragonflies look now?"
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_3_coil_comment51)
    if vig4_defendPolaris == True:
        cS "I would say it looks all but certain."
        cS "Captain Moze, Polaris may be in ruins, but its people will endure. In no small part thanks to your actions today."
        if viewershipHigh == True or viewershipMed == True:
            $ AddChatter(vig4_sc7_3_coil_comment52)
        cS "I am sorry for the trouble I caused you earlier. I did not realize the power of the bond you share with MAC."
        if viewershipHigh == True:
            $ AddChatter(vig4_sc7_3_coil_comment53)
        cS "We all owe our gratitude to you."
        $ AddChatter(vig4_sc7_3_coil_comment54)
        cS "You and your crew have earned your spot."
        menu:
            cS "You and your crew have earned your spot."
            "Organization isn't my style.":
                mS "I don't know. Working for organizations isn't really my style."
                $ AddChatter(vig4_sc7_3_coil_comment56)
                cS "Of course. We can find an arragenment that is amenable to your... \"distinct\" approach."
            "Thank you.":
                mS "Thank you for the offer. After all this, my crew and I will need some sanctuary."
                $ AddChatter(vig4_sc7_3_coil_comment56)
                cS "You shall have it."
    elif vig4_defendPolaris == False and vig4_killDflies == False:
        cS "The chances are certainly much higher now."
        cS "Although your methods are... messy, Captain Moze, without your presence, Vega and I would likely be dead."
        cS "We can offer you and your crew sanctuary while you rest and recover."
        $ AddChatter(vig4_sc7_3_coil_comment56)
        cS "You and your crew have earned that, at least."
    else:
        cS "The carnage from this battle won't go over well with the higher-ups."
        cS "But considering we'd be dead without her, I'd say we'll have to take her on board."
        cS "At least for the time being while we all catch our breath."
        $ AddChatter(vig4_sc7_3_coil_comment56)
    mS "And MAC?"
    "We all turn to look at him."
    play audio "macPester.wav" volume 1.5
    macS "I do not wish to leave my family again."
    $ AddChatter(vig4_sc7_3_coil_comment57)
    cS "You heard him."
    vS "Come on, there should be an old mercenary's empty ship somewhere in the ridge that we can commandeer."
    if macHope > macPessimism:
        play audio "macPing.wav" volume 1.5
        macS "Wait, what about Ama?"
        mS "What about her?"
        macS "We shouldn't leave her here."
        macS "She was a Snakehawk. She deserves a proper burial."
        $ reactTarget = "vig4_sc7_macamasburial"
        show screen streamerCommentary
        $ AddChatter(vig4_sc7_3_coil_comment58)
        menu:
            macS "She was a Snakehawk. She deserves a proper burial."
            "You're right, MAC.":
                "I look back at Ama's body."
                $ AddChatter(vig4_sc7_3_coil_comment59)
                "A chill runs down my spine."
                $ AddChatter(vig4_sc7_3_coil_comment60)
                "But she shouldn't be left here. It's not right."
                mS "You're right, MAC."
                $ AddChatter(vig4_sc7_3_coil_comment61)
                "I go over and lift Ama's body in my arms."
                "She's heavy. But I'm accustomed to the weight."
                "It's as if I've been carrying it for years."
    mS "Let's go."      
    hide screen streamerCommentary
    "Together, MAC, Coil, Vega, and I leave the room and descend the tower."
    hide vega with dissolve
    hide coil with dissolve
    hide mac with dissolve
    hide ama
    jump vig4_epilogue_coil

label vig4_epilogue_coil():
    play music "soundtrack/theme.wav"
    $ viewCheck10 = viewCount
    show ama_shiphub_stream at topleft onlayer background with dissolve
    hide tower_star_shower_ship_stream    
    $ AddChatter(vig4_sc7_epilogue_comment1)
    play backAudio "shipHum.wav" volume 0.3
    "The perpetual purr of space travel thrums through the ship."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_epilogue_comment2)
        pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment3)
    "I let my head fall back against the cushy seats behind me."
    $ AddChatter(vig4_sc7_epilogue_comment4)
    "Finally. At long last. My muscles relax."
    pS "And to think, Ama was rolling around the galaxy in such luxury!"
    enS "I know, I always assumed her ship would be a bit more spartan."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream happy at stream_right with dissolve
    $ AddChatter(vig4_sc7_epilogue_comment5)
    "Jennica and Teresa enter the ship's bridge."
    "They both have fresh scars, bandages, and stitches from the battle."
    $ AddChatter(vig4_sc7_epilogue_comment6)
    pS "Hey there, Cap!"
    enS "Salutations, Captain!"
    "They make mock salute poses."
    $ vig4_sc7_epilogue_comment4.click = False
    $ AddChatter(vig4_sc7_epilogue_comment7)
    menu:
        "They make mock salute poses."
        "At ease.":
            mS "At ease, crew."
            mS "You deserve to relax, after what you went through."
        "Make them hold it.":
            "I don't say anything."
            "Just stare at them for almost a minute."
            pS "Ya think she'll ever let us go?"
            enS "I don't know, but I'm starting to think this joke wasn't worth it."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_epilogue_comment8)
            "A short chuckle escapes from me."
            mS "At ease, crew."
            "The pair relax."
    "They move over and sit on the couch with me."
    if jennicaRomance == True:
        $ csEngagement += 1
        "Jennica sidles up next to me and leans her head on my shoulder."
        "I take her hand in mine."
        $ AddChatter(vig4_sc7_epilogue_comment9)
        pS "How ya feeling, Cap?"
    elif teresaRomance == True:
        $ kcEngagement += 1
        "Teresa sits down next to me and folds her legs over my lap."
        "I take her hand in mine."
        $ AddChatter(vig4_sc7_epilogue_comment10)
        enS "How are you feeling, Captain?"
    else:
        "They both relax into the cushions on either side of me."
        pS "How ya feeling, Cap?"
    "How am I feeling?"
    menu:
        "How am I feeling?"
        "Exhausted.":
            mS "I'm exhausted."
            mS "I think I could sleep for a month straight."
            $ AddChatter(vig4_sc7_epilogue_comment11)
            pS "I hear that."
            enS "I think I could go for a year in all honesty."
        "Relaxed.":
            mS "You know, I think I feel relaxed for the first time since..."
            mS "I can't remember."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_epilogue_comment12)
            pS "Good."
            $ AddChatter(vig4_sc7_epilogue_comment13)
            enS "You've earned it."
        "Sad.":
            mS "Honestly, I'm sad."
            enS "About Ama?"
            mS "Yeah."
            $ AddChatter(vig4_sc7_epilogue_coil_comment1)
            mS "I wish it didn't have to go that way."
            $ AddChatter(vig4_sc7_epilogue_coil_comment2)
            pS "It's a real shame, Cap."
            pS "But Ama made her choice a long time ago."
            $ AddChatter(vig4_sc7_epilogue_coil_comment3)
            enS "I won't tell you not to feel sad, but a lot of people are alive now because of you."
            enS "Just, don't forget that too."
            mS "Thanks you two. I mean it."
            $ AddChatter(vig4_sc7_epilogue_coil_comment4)
            enS "Anytime."
            pS "We've got your back."
    pS "I will say, despite the luxury, still doesn't hold a candle to the Oakley."
    enS "No way."
    play audio "macAffirmative.wav" volume 1.5
    macS "I am in agreement."
    $ AddChatter(vig4_sc7_epilogue_comment14)
    show mac stream neutral at stream_center_mac with dissolve
    macS "This ship is significantly less well stocked in terms of supplies."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_epilogue_comment15)
    macS "And there is a distinct lack of escape pods."
    enS "Considering our previous adventures, maybe that's a good thing."
    pS "Yeah, and at least the communications array is internal. Way less likely to get mucked up."
    $ AddChatter(vig4_sc7_epilogue_comment16)
    "MAC rolls up next to us."
    menu:
        "MAC rolls up next to us."
        "Come on up, MAC.":
            $ kcEngagement += 2
            mS "Come on, MAC, join the pile."
            play audio "macPester.wav" volume 1.5
            macS "Are you sure, Captain?"
            macS "Will my treads not stain the couch?"
            $ AddChatter(vig4_sc7_epilogue_comment17)
            pS "C'mon, kid, it's not even our couch!"
            enS "Yeah, join the family!"
            macS "Okay!"
            "Teresa, Jennica, and I bend down to lift MAC up."
            "We all roll back onto the couch in a pile, with MAC in the center."
            $ AddChatter(vig4_sc7_epilogue_comment18)
            show mac stream happy
            play audio "macHappy.wav" volume 1.5
            macS "Wheeee!"
            $ AddChatter(vig4_sc7_epilogue_comment19)
            macS "Being on the couch is fun."
            mS "It really is."
            $ AddChatter(vig4_sc7_epilogue_comment20)
            show mac stream neutral
            "We stay in the pile for several minutes until an idea strikes me."
            mS "Actually, give me one second."
            "I slide out and open a nearby closet."
        "Rub his head.":
            $ kcEngagement += 1
            mS "Come here, MAC."
            $ AddChatter(vig4_sc7_epilogue_comment19)
            play audio "macHum.wav" volume 1.5
            "I put my hand on his head and feel the vibrations thrumming through his body."
            "I feel his attention on me. It's like we're making eye contact."
            mS "You did good, MAC."
            mS "Really, really good."
            mS "I'm proud of you."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_epilogue_comment21)
            play audio "macHappy.wav" volume 1.5
            macS "Aww, Captain. Thank you."
            pS "Yeah, kid, you kept your cool."
            enS "I'm impressed."
            $ AddChatter(vig4_sc7_epilogue_comment20)
            mS "Actually, that gives me an idea."
            "I stand up from the couch and open a nearby closet."
    macS "What are you looking for, Captain."
    mS "Ama usually keeps a—{i}aha{/i}! Here it is!"
    "I pull down a silver bucket, set it down on the floor, and pop open the top."
    "It's red paint."
    mS "Figure we can commemorate the successful mission with MAC's first tattoo."
    $ AddChatter(vig4_sc7_epilogue_comment22)
    macS "Really!?"
    mS "Sure. Turn around there, let me find a good spot on you."
    $ AddChatter(vig4_sc7_epilogue_coil_comment5)
    pS "Oh no, come on Teresa, she's gonna need some help."
    enS "I'll say. Remember when I asked her to do a tattoo for me."
    pS "The sketches were so bad you completely backed out hahaha."
    mS "Hey, knock it off you two, that's an order!"
    enS "Alright, alright."
    pS "So, what's it gonna be, Cap?"
    "I stare at the clear space of MAC's back panel. What image would go perfectly there?"
    menu:
        "I stare at the clear space of MAC's back panel. What image would go perfectly there?"
        "A Snakehawk.":
            $ pdEngagement += 2
            mS "I've got the perfect thing."
            $ AddChatter(vig4_sc7_epilogue_coil_comment9)
            "Slowly, but surely I begin tracing the outline."
            show teresa stream think
            show jennica stream shock
            enS "I see what you're going for."
            pS "Oh no, not like that. You gotta make the curve wider."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_epilogue_coil_comment10)
            "I put the brush down."
            $ AddChatter(vig4_sc7_epilogue_coil_comment11)
            show teresa stream happy
            show jennica stream neutral
            mS "There, all done."
            mS "MAC, you're now the proud owner of a \"Snakehawk\" tattoo!"
            play audio "macPing.wav" volume 1.5
            macS "Snakehawk!? Really!?"
        "A Dragonfly.":
            $ csEngagement += 2
            mS "I've got the perfect thing."
            "Slowly, but surely I begin tracing the outline."
            $ AddChatter(vig4_sc7_epilogue_coil_comment6)
            show teresa stream think
            show jennica stream shock
            enS "I see what you're going for."
            pS "Come on, Cap, you don't want the lines to be perfectly straight."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_epilogue_coil_comment7)
            "I put the brush down."
            show jennica stream neutral
            show teresa stream happy
            mS "There, all done."
            $ AddChatter(vig4_sc7_epilogue_coil_comment8)
            mS "MAC, you're now the proud owner of a \"Dragonfly\" tattoo!"
            play audio "macPing.wav" volume 1.5
            macS "Dragonfly!? I hope they're as friendly as you all!"
        "The Oakley.":
            $ kcEngagement += 2
            mS "I've got the perfect thing."
            "Slowly, but surely I begin tracing the outline."
            $ AddChatter(vig4_sc7_epilogue_comment23)
            show teresa stream think
            show jennica stream shock
            enS "I see what you're going for."
            pS "It's abstract but good, Cap. You're really capturing her essence."
            $ AddChatter(vig4_sc7_epilogue_comment24)
            "I put the brush down."
            show teresa stream happy
            show jennica stream neutral
            mS "There, all done."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_epilogue_comment25)
            mS "MAC, you're now the proud owner of the first ever \"Oakley\" tattoo!"
            play audio "macPing.wav" volume 1.5
            macS "Oakley!? That's amazing!"
    "Without hesitation, MAC swerves around and wraps his arms around me."
    macS "Thank you, Captain."
    play audio "macLove.wav" volume 1.5
    macS "I love you."
    show jennica stream shock
    show teresa stream shock
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_epilogue_comment26)
        pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment27)
    $ AddChatter(vig4_sc7_epilogue_comment28)
    $ reactTarget = "vig4_epilogue_maclove"
    show screen streamerCommentary
    pS "Oh!"
    enS "Did that just happen?"
    "I lean into the hug from MAC."
    $ AddChatter(vig4_sc7_epilogue_comment29)
    menu:
        "I lean into the hug from MAC."
        "I love you too.":
            mS "I love you too, MAC."
            $ AddChatter(vig4_sc7_epilogue_comment30)
    show teresa stream happy
    show jennica stream neutral
    "Jennica and Teresa bend down and wrap their arms around us as well."
    $ AddChatter(vig4_sc7_epilogue_comment31)
    "Then the ship's alert system activates."
    $ AddChatter(vig4_sc7_epilogue_comment32)
    vS "Hello, crew, we'll be coming up on the coordinates soon. Y'all should come up here."
    mS "Come on, time to see the next adventure that awaits us."
    hide screen streamerCommentary
    hide mac with dissolve
    hide jennica with dissolve
    hide teresa with dissolve
    hide shiphub_stream with dissolve
    show cockpit_stream at topleft onlayer background with dissolve
    show jennica stream neutral at stream_left5 with dissolve
    show teresa stream neutral at stream_right5 with dissolve
    show coil stream neutral at stream_right with dissolve
    show vega stream neutral at stream_left with dissolve
    show mac stream neutral at stream_center_mac with dissolve
    "The four of us move up to the cockpit."
    "We're not in hyperspace anymore, just floating in the vast expanse of stars."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_epilogue_coil_comment12)
    enS "I don't see anything."
    pS "I'll say, looks like a whole lotta nothing."
    cS "Patience. We are exactly where we need to be."
    $ AddChatter(vig4_sc7_epilogue_coil_comment13)
    "A minute goes by as we scan the vastness of space."
    macS "Oh! I see it!"
    $ AddChatter(vig4_sc7_epilogue_coil_comment14)
    mS "See what?"
    play audio "macPing.wav" volume 1.5
    macS "There! It was a little flicker in front of one of the stars!"
    cS "He has sharp eyes."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_epilogue_coil_comment15)
    mS "What do you mean?"
    show vega stream happy
    vS "Just watch."
    "As I gaze into the vastness of space, I start to notice it too."
    "Some of the stars are flickering."
    show jennica stream shock
    show teresa stream think
    "Or rather, it's as if something is passing in front of them and obscuring them for a brief moment."
    "Then it starts."
    enS "What the—?"
    "Cascading from one end of the cockpit screen to another, ripples like waves distorting the light in front of us."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_epilogue_coil_comment16)
    "It fades into view slowly but surely, as the ripples dissipate further and further away."
    "A massive space station, twice the size of the Polaris moon, resolves into view."
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_epilogue_coil_comment17)
        pause 0.5
    $ AddChatter(vig4_sc7_epilogue_coil_comment18)
    pause 0.5
    $ AddChatter(vig4_sc7_epilogue_coil_comment19)
    "Ships the size of a BC cruiser drift into open hangar bays on the side of the station."
    pS "Wow."
    hide jennica with dissolve
    with hpunch
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
            play audio "macLove.wav" volume 1.5
            macS "Right, Captain Moze!"
        "Are you ready for an adventure?":
            "I put a hand on his head."
            mS "Are you ready for another adventure, MAC?"
            play audio "macLove.wav" volume 1.5
            macS "Ready, Captain Moze!"
    stop backAudio fadeout 2.0
    hide mac with Dissolve (2.0)
    hide cockpit_stream with dissolve
    jump vig4_signoff

label vig4_epilogue_ama():
    play music "soundtrack/theme.wav"
    $ viewCheck10 = viewCount
    show ama_shiphub_stream at topleft onlayer background with dissolve
    hide tower_star_shower_ship_stream  
    $ AddChatter(vig4_sc7_epilogue_comment1)
    play backAudio "shipHum.wav" volume 0.3
    "The perpetual purr of space travel thrums through the ship."
    if viewershipHigh == True or viewershipMed == True:    
        $ AddChatter(vig4_sc7_epilogue_comment2)
        pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment3)
    "I let my head fall back against the cushy seats behind me."
    $ AddChatter(vig4_sc7_epilogue_comment4)
    "Finally. At long last. My muscles relax."
    pS "To think, Ama was rollin' 'round the galaxy in such luxury!"
    enS "I know, I always assumed her ship would be a bit more spartan."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream happy at stream_right with dissolve
    $ AddChatter(vig4_sc7_epilogue_comment5)
    "Jennica and Teresa enter the ship's bridge."
    "They both have fresh scars, bandages, and stitches from the battle."
    $ AddChatter(vig4_sc7_epilogue_comment6)
    pS "Hey there, Cap!"
    enS "Salutations, Captain!"
    "They make mock salute poses."
    $ vig4_sc7_epilogue_comment4.click = False
    $ AddChatter(vig4_sc7_epilogue_comment7)
    menu:
        "They make mock salute poses."
        "At ease.":
            mS "At ease, crew."
            mS "You deserve to relax, after what you went through."
        "Make them hold it.":
            "I don't say anything."
            "Just stare at them for almost a minute."
            pS "Do ya think she'll ever let us go?"
            enS "I don't know, but I'm starting to think this joke wasn't worth it."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_epilogue_comment8)
            "A short chuckle escapes from me."
            mS "At ease, crew."
            "The pair relax."
    "They move over and sit on the couch with me."
    if jennicaRomance == True:
        "Jennica sidles up next to me and leans her head on my shoulder."
        "I take her hand in mine."
        $ AddChatter(vig4_sc7_epilogue_comment9)
        pS "How ya feelin', Cap?"
    elif teresaRomance == True:
        "Teresa sits down next to me and folds her legs over my lap."
        "I take her hand in mine."
        $ AddChatter(vig4_sc7_epilogue_comment10)
        enS "How are you feeling, Captain?"
    else:
        "They both relax into the cushions on either side of me."
        pS "How ya feelin', Cap?"
    "How am I feeling?"
    menu:
        "How am I feeling?"
        "Exhausted.":
            mS "I'm exhausted."
            mS "I think I could sleep for a month straight."
            $ AddChatter(vig4_sc7_epilogue_comment11)
            pS "I hear that."
            enS "I think I could go for a year in all honesty."
        "Relaxed.":
            mS "You know, I think I feel relaxed for the first time since..."
            mS "I can't remember."
            if viewershipHigh == True:    
                $ AddChatter(vig4_sc7_epilogue_comment12)
            pS "Good."
            $ AddChatter(vig4_sc7_epilogue_comment13)
            enS "You've earned it."
        "Sad.":
            mS "Honestly, I'm sad."
            enS "About Coil?"
            mS "Yeah."
            $ AddChatter(vig4_sc7_epilogue_ama_comment1)
            mS "I wish it didn't have to go that way."
            $ AddChatter(vig4_sc7_epilogue_ama_comment2)
            pS "It's a real shame, Cap."
            pS "But he made his choice a long time ago."
            $ AddChatter(vig4_sc7_epilogue_ama_comment3)
            enS "There were a lot of moments when he could have done things differently."
            enS "His path led him to this."
            mS "Thanks you two. I mean it."
            $ AddChatter(vig4_sc7_epilogue_ama_comment4)
            enS "Anytime."
            pS "We've got your back."
    if vig4_amaCrew == False:
        enS "You think Deadeye will be alright without her ship?"
        pS "She's resourceful. I'm sure she'll figure somethin' out."
        mS "I was surprised she was okay with us taking it."
        pS "Ya gotta love personal growth."
        enS "Even if it comes a little late."
        "Jennica scans the ship's hub room."
    pS "I will say, despite the luxury, doesn't hold a candle to the Oakley."
    enS "No way."
    play audio "macAffirmative.wav" volume 1.5
    macS "I am in agreement."
    $ AddChatter(vig4_sc7_epilogue_comment14)
    show mac stream neutral at stream_center_mac with dissolve
    macS "This ship is significantly less well stocked in terms of supplies."
    if viewershipHigh == True or viewershipMed == True:
        $ AddChatter(vig4_sc7_epilogue_comment15)
    macS "And there is a distinct lack of escape pods."
    enS "Considering our previous adventures, maybe that's a good thing."
    pS "Yeah, and at least the communications array is internal. Way less likely to get mucked up."
    $ AddChatter(vig4_sc7_epilogue_comment16)
    "MAC rolls up next to us."
    menu:
        "MAC rolls up next to us."
        "Come on up, MAC.":
            $ kcEngagement += 2
            mS "Come on, MAC, join the pile."
            play audio "macPester.wav" volume 1.5
            macS "Are you sure, Captain?"
            macS "Will my treads not stain the couch?"
            $ AddChatter(vig4_sc7_epilogue_comment17)
            pS "C'mon, kid, it's not even our couch!"
            enS "Yeah, join the family!"
            macS "Okay!"
            "Teresa, Jennica, and I bend down to lift MAC up."
            "We all roll back onto the couch in a pile, with MAC in the center."
            $ AddChatter(vig4_sc7_epilogue_comment18)
            show mac stream happy
            play audio "macHappy.wav" volume 1.5
            macS "Wheeee!"
            $ AddChatter(vig4_sc7_epilogue_comment20)
            macS "Being on the couch is fun."
            if vig4_MACKill == True:
                $ AddChatter(vig4_sc7_epilogue_ama_comment5)
                pause 0.5
                $ AddChatter(vig4_sc7_epilogue_ama_comment6)
            else:
                pass
            mS "It really is."
            show mac stream neutral
            "We stay in the pile for several minutes until an idea strikes me."
            mS "Actually, give me one second."
            "I slide out and open a nearby closet."
        "Rub his head.":
            $ kcEngagement += 1
            mS "Come here, MAC."
            $ AddChatter(vig4_sc7_epilogue_comment19)
            play audio "macHum.wav" volume 1.5
            "I put my hand on his head and feel the vibrations thrumming through his body."
            "I feel his attention on me. It's like we're making eye contact."
            mS "You did good, MAC."
            mS "Really, really good."
            mS "I'm proud of you."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_epilogue_comment21)
            play audio "macHappy.wav" volume 1.5
            macS "Aww, Captain. Thank you."
            pS "Yeah, kid, you kept your cool."
            enS "I'm impressed."
            $ AddChatter(vig4_sc7_epilogue_comment20)
            mS "Actually, that gives me an idea."
            "I stand up from the couch and open a nearby closet."
    macS "What are you looking for, Captain."
    mS "Ama usually keeps a—{i}aha{/i}! Here it is!"
    "I pull down a silver bucket, set it down on the floor, and pop open the top."
    "It's red paint."
    mS "Figure we can commemorate the successful mission with MAC's first tattoo."
    $ AddChatter(vig4_sc7_epilogue_comment22)
    macS "Really!?"
    mS "Sure. Turn around there, bud, let me find a good spot on you."
    if vig4_MACKill == True:
        $ AddChatter(vig4_sc7_epilogue_ama_comment7)
    else:
        $ AddChatter(vig4_sc7_epilogue_ama_comment8)
    pS "Oh no, come on Teresa, she's gonna need some help."
    enS "I'll say. Remember when I asked her to do a tattoo for me."
    pS "Sketches were so bad you completely backed out hahaha."
    mS "Hey, knock it off you two, that's an order!"
    enS "Alright, alright."
    pS "So, what's it gonna be, Cap?"
    "I stare at the clear space of MAC's back panel. What image would go perfectly there?"
    menu:
        "I stare at the clear space of MAC's back panel. What image would go perfectly there?"
        "A Snakehawk.":
            $ pdEngagement += 2
            mS "I've got the perfect thing."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_epilogue_ama_comment9)
            "Slowly, but surely I begin tracing the outline."
            enS "I see what you're going for."
            show teresa stream think
            pS "Oh no, not like that. You gotta make the curve wider."
            show jennica stream shock
            $ AddChatter(vig4_sc7_epilogue_ama_comment10)
            "I put the brush down."
            $ AddChatter(vig4_sc7_epilogue_ama_comment11)
            mS "There, all done."
            show jennica stream neutral
            show teresa stream happy
            mS "MAC, you're now the proud owner of a \"Snakehawk\" tattoo!"
            play audio "macPing.wav" volume 1.5
            macS "Snakehawk!? Really!?"
        #third tattoo?
        "The Oakley.":
            $ kcEngagement += 2
            mS "I've got the perfect thing."
            "Slowly, but surely I begin tracing the outline."
            $ AddChatter(vig4_sc7_epilogue_comment23)
            show teresa stream think
            show jennica stream shock
            enS "I see what you're going for."
            pS "It's abstract but good, Cap. You're really capturing her essence."
            $ AddChatter(vig4_sc7_epilogue_comment24)
            "I put the brush down."
            show jennica stream neutral
            show teresa stream happy
            mS "There, all done."
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_epilogue_comment25)
            mS "MAC, you're now the proud owner of the first ever \"Oakley\" tattoo!"
            play audio "macPing.wav" volume 1.5
            macS "Oakley!? That's amazing!"
    "Without hesitation, MAC swerves around and wraps his arms around me."
    macS "Thank you, Captain."
    play audio "macLove.wav" volume 1.5
    macS "I love you."    
    show jennica stream shock
    show teresa stream shock
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_epilogue_comment26)
        pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment27)
    $ AddChatter(vig4_sc7_epilogue_comment28)
    $ reactTarget = "vig4_epilogue_maclove"
    show screen streamerCommentary
    pS "Oh!"
    enS "Did that just happen?"
    "I lean into the hug from MAC."
    $ AddChatter(vig4_sc7_epilogue_comment29)
    menu:
        "I lean into the hug from MAC."
        "I love you.":
            mS "I love you too, MAC."
            $ AddChatter(vig4_sc7_epilogue_comment30)
    show jennica stream neutral
    show teresa stream happy
    "Jennica and Teresa bend down and wrap their arms around us as well."
    $ AddChatter(vig4_sc7_epilogue_comment31)
    "Then the ship's alert system activates."
    play audio "shipAlarmShort.wav" volume 1.0
    $ AddChatter(vig4_sc7_epilogue_comment32)
    if amaRomance == True:
        amaS "You all should come up here, there's something I could use some help with."
        mS "That sounds odd. Come on, let's go."
    else:
        pS "That's the contact alarm. Auto-pilot must've triggered cause a ship got in our range."
        mS "Let's go check it out."
    hide screen streamerCommentary
    hide mac with dissolve
    hide jennica with dissolve
    hide teresa with dissolve
    hide shiphub_stream with dissolve
    show cockpit_stream at topleft onlayer background with dissolve
    if vig4_amaCrew == True:
        show jennica stream neutral at stream_left with dissolve
        show teresa stream neutral at stream_right with dissolve
        show ama stream neutral at stream_left5 with dissolve
        show mac stream neutral at stream_right5mac with dissolve
        "The four of us move up to the cockpit."
        if viewershipHigh == True or viewershipMed == True:
            $ AddChatter(vig4_sc7_epilogue_ama_comment12)
        if amaRomance == True:
            "I step up behind Ama's chair, and reach for her hand."
            show ama stream happy
            "Almost automatically, as if we've been doing it for years, she takes it."
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_epilogue_ama_comment14)
        else:
            pass
        mS "What seems to be the trouble, Ama?"
        show ama stream confused
        amaS "Does anyone else see anything funny out there?"
        "The visual in the cockpit just shows empty space."
        pS "Looks like normal space stuff to me."
        enS "Nothing out of the ordinary I can see."
        amaS "Keep looking."
        "A minute goes by as we scan the vastness of space."
        amaS "There! Did anyone see that!"
        play audio "macPing.wav" volume 1.5
        macS "Oh! I see it!"
        $ AddChatter(vig4_sc7_epilogue_ama_comment15)
        mS "See what?"
        macS "It was a little flicker in front of one of the stars!"
        show ama stream neutral
        amaS "So I'm not going crazy."
        "As I gaze into the vastness of space, I start to notice it too."
        "Some of the stars are flickering."
        "Or rather, it's as if something is passing in front of them and obscuring them for a brief moment."
        "Then it starts."
        show teresa stream shock
        show jennica stream shock
        enS "What the—?"
        "Cascading from one end of the cockpit screen to another, ripples like waves distorting the light in front of us."
        if viewershipHigh == True or viewershipMed == True:
            $ AddChatter(vig4_sc7_epilogue_ama_comment16)
        "It fades into view slowly but surely, as the ripples dissipate further and further away."
        "A massive space station, the size of the Polaris moon, resolves into view."
        if viewershipHigh == True or viewershipMed == True:   
            $ AddChatter(vig4_sc7_epilogue_ama_comment17)
            pause 0.5
        if viewershipHigh == True:
            $ AddChatter(vig4_sc7_epilogue_ama_comment18)
            pause 0.5
        $ AddChatter(vig4_sc7_epilogue_ama_comment19)
        "Ships the size of the BC cruiser drift into open hangar bays on the side of the station."
        "Smaller ships depart the hangars."
        "They're heading in our direction."
        $ AddChatter(vig4_sc7_epilogue_ama_comment20)
        mS "What the hell is that!"
        show ama stream angry
        amaS "Dragonfly space station. Shit!"
        "Ama jams thrusters back and frenetically starts snapping switches on control consoles."
        "We immediately turn around and start flying away from the station."
        amaS "We've got to reverse fast before they hit us with a tractor beam."
        if viewershipHigh == True:
            $ AddChatter(vig4_sc7_epilogue_ama_comment21)
        show jennica stream neutral
        show teresa stream neutral
        amaS "Transferring control to co-pilot. Brown, you take over."
        "Jennica leaps into the co-pilot chair."
        pS "On it."
        mS "Teresa, head down to engines, make sure power is routed where we need it to go."
        enS "Aye aye, captain."
        hide teresa with dissolve
        hide jennica with dissolve
        "A tug at my sleeve."
        play audio "macPester.wav" volume 1.5
        macS "What about me?"
        menu:
            macS "What about me?"
            "Guns.":
                mS "MAC, you and I are going to handle the guns."
                if macViolence >= macPeace:
                    "I swear, his eyes light up."
                    $ AddChatter(vig4_sc7_epilogue_ama_comment22)
                    play audio "macHappy.wav" volume 1.5
                    macS "Guns! Oh boy!"
                else:
                    play audio "macAffirmative.wav" volume 1.5
                    macS "Understood."
                    $ AddChatter(vig4_sc7_epilogue_ama_comment22)
        "MAC turns and rolls off toward the turret controls to the side of the cockpit."
        if amaRomance == True:
            hide mac with dissolve
            "I move to follow, but a hand on my shoulder stops me."
            show ama stream happy
            amaS "Hey."
            "We kiss. Briefly. But passionately."
            amaS "Knock 'em dead, Mozely."
            $ AddChatter(vig4_sc7_epilogue_ama_comment23)
            "Smiling, I turn to follow MAC."
            hide ama with dissolve
            show mac stream neutral at stream_center_mac with dissolve
        else:
            hide ama with dissolve
    else:
        show jennica stream neutral at stream_left with dissolve
        show teresa stream neutral at stream_right with dissolve
        show mac stream neutral at stream__center_mac with dissolve
        "Jennica takes over control from the auto-pilot as we move up to the cockpit."
        if viewershipHigh == True or viewershipMed == True:
            $ AddChatter(vig4_sc7_epilogue_ama_comment13)
        "The visual in the cockpit just shows empty space."
        pS "Looks like normal space stuff to me."
        enS "Nothing out of the ordinary I can see."
        mS "Could it be a faulty alarm system?"
        macS "Let's wait and observe before we jump to conclusions."
        "A minute goes by as we scan the vastness of space."
        play audio "macPing.wav" volume 1.5
        macS "Oh! I see it!"
        $ AddChatter(vig4_sc7_epilogue_ama_comment15)
        mS "See what?"
        macS "It was a little flicker in front of one of the stars!"
        "As I gaze into the vastness of space, I start to notice it too."
        "Some of the stars are flickering."
        "Or rather, it's as if something is passing in front of them and obscuring them for a brief moment."
        "Then it starts."
        show jennica stream shock
        show teresa stream shock
        enS "What the—?"
        "Cascading from one end of the cockpit screen to another, ripples like waves distorting the light in front of us."
        if viewershipHigh == True or viewershipMed == True:
            $ AddChatter(vig4_sc7_epilogue_ama_comment16)
        "It fades into view slowly but surely, as the ripples dissipate further and further away."
        "A massive space station, the size of the Polaris moon, resolves into view."
        if viewershipHigh == True or viewershipMed == True:
            $ AddChatter(vig4_sc7_epilogue_ama_comment17)
            pause 0.5
        if viewershipHigh == True:
            $ AddChatter(vig4_sc7_epilogue_ama_comment18)
            pause 0.5
        $ AddChatter(vig4_sc7_epilogue_ama_comment19)
        "Ships the size of the BC cruiser drift into open hangar bays on the side of the station."
        "Smaller ships depart the hangars."
        "They're heading in our direction."
        $ AddChatter(vig4_sc7_epilogue_ama_comment20)
        mS "Shit! It's the Dragonflies!"
        "Jennica jams thrusters back and frenetically starts snapping switches on control consoles."
        if viewershipHigh == True:
            $ AddChatter(vig4_sc7_epilogue_ama_comment21)
        "We immediately turn around and start flying away from the station."
        show jennica stream angry
        show teresa stream neutral
        pS "We've got to reverse fast before they hit us with a tractor beam."
        mS "Teresa, head down to engines, make sure power is routed where we need it to go."
        enS "Aye aye, captain."
        hide teresa with dissolve
        hide jennica with dissolve
        "A tug at my sleeve."
        macS "What about me?"
        menu:
            macS "What about me?"
            "Guns.":
                mS "MAC, you and I are going to handle the guns."
                if macViolence >= macPeace:
                    "I swear, his eyes light up."
                    $ AddChatter(vig4_sc7_epilogue_ama_comment22)
                    play audio "macHappy.wav" volume 1.5
                    macS "Guns! Oh boy!"
                else:
                    play audio "macAffirmative.wav" volume 1.5
                    macS "Understood."
                    $ AddChatter(vig4_sc7_epilogue_ama_comment22)
        "MAC turns and immediately rushes off toward the turret controls. I follow right behind."
    "MAC has already engaged the turret controls on the side of the cockpit."
    "As he hops into one of the gunner seats, I take the position next to him."
    "We turn to each other."
    menu:
        "We turn to each other."
        "We'll face our future, together.":
            "I put a hand on his head."
            mS "Whatever's in store for us, we'll face it together. Right, MAC?"
            play audio "macLove.wav" volume 1.5
            macS "Right, Captain Moze!"
        "Are you ready for an adventure?":
            "I put a hand on his head."
            mS "Are you ready for another adventure, MAC?"
            play audio "macLove.wav" volume 1.5
            macS "Ready, Captain Moze!"
    "The ship lurches forward as we accelerate into space."
    hide mac with Dissolve (2.0)
    hide cockpit_stream with dissolve
    jump vig4_signoff

label vig4_signoff():
    $ narrator = reg_narrator
    $ macroChoice = True
    "The screen fades as the game's credits begin to roll."
    $ AddChatter(vig4_sc7_epilogue_comment33)
    pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment34)
    pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment35)
    pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment36)
    pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment37)
    "The game is over. What do you want to say to your viewers?"
    menu:
        "The game is over. What do you want to say to your viewers?"
        "We did it together!":
            player "Oh my god, Chat, we did it!"
            player "This has been such a journey, from the start on Cromuu all the way through Akar and now here."
            player "I couldn't have done it without all of you."
            player "Genuinely, I feel like we made this experience something special together."
            player "So thank you for joining me on this journey, it's been a blast!"
            $ AddChatter(vig4_sc7_epilogue_comment50)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_epilogue_comment51)
                pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_epilogue_comment52)
                pause 0.5
            $ AddChatter(vig4_sc7_epilogue_comment53)
            pause 0.5
            $ AddChatter(vig4_sc7_epilogue_comment54)
        "Thank you, chat!":
            player "Thank you, Chat, for sticking around till the end!"
            player "It's been such a crazy experience playing this game on stream and you all made it so worthwhile."
            player "Genuinely, a huge motivation for me this whole time was just logging on to hang with you all."
            player "It's been a real pleasure, and, yeah, just thanks again for making this so much fun!"
            $ AddChatter(vig4_sc7_epilogue_comment55)
            pause 0.5
            $ AddChatter(vig4_sc7_epilogue_comment56)
            pause 0.5
            $ AddChatter(vig4_sc7_epilogue_comment57)
            pause 0.5
            if viewershipHigh == True:
                $ AddChatter(vig4_sc7_epilogue_comment58)
                pause 0.5
            $ AddChatter(vig4_sc7_epilogue_comment59)
        "This game was so good!":
            player "Wow this game is so good!"
            player "Was a crazy experience streaming this for everyone but it was a ton of fun!"
            player "We got to meet some awesome characters, see some cool planets, and feel some intense emotions together."
            player "Honestly, this might even top Oakley 1."
            player "Thanks everyone for joining me on this journey, it's been a blast!"
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_epilogue_comment44)
                pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_epilogue_comment45)
                pause 0.5
            $ AddChatter(vig4_sc7_epilogue_comment46)
            pause 0.5
            $ AddChatter(vig4_sc7_epilogue_comment47)
            pause 0.5
            $ AddChatter(vig4_sc7_epilogue_comment48)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter(vig4_sc7_epilogue_comment49)
        "I'm a little underwhelmed!":
            player "Wow, so that's the end."
            player "Honestly, I'm a little underwhelmed."
            player "Like the characters, the music, the art and everything were really good."
            player "And I liked the story too."
            player "But idk, I don't think this quite topped Oakley 1 for me."
            player "Still had a great time! Especially hanging out with y'all. You really made this a special experience."
            player "So thank you everyone for joining me on this journey, it's been a blast!"
            $ AddChatter(vig4_sc7_epilogue_comment38)
            pause 0.5
            if viewershipHigh == True or viewershipMed == True:
                $ AddChatter(vig4_sc7_epilogue_comment39)
                pause 0.5
            $ AddChatter(vig4_sc7_epilogue_comment40)
            pause 0.5
            $ AddChatter(vig4_sc7_epilogue_comment41)
            pause 0.5
            $ AddChatter(vig4_sc7_epilogue_comment42)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter(vig4_sc7_epilogue_comment43)
    player "Chat, thank you so much for all the kind words."
    player "It's been an pleasure."
    player "You all take care!"
    if marshal > outlaw:
        $ AddChatter(vig4_sc7_epilogue_comment60)
    else:
        pass
    pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment61)
    if viewershipHigh == True or viewershipMed == True:
        pause 0.5
        $ AddChatter(vig4_sc7_epilogue_comment62)
    pause 0.5
    if marshal > outlaw:
        $ AddChatter(vig4_sc7_epilogue_comment71)
    else:
        pass
    pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment63)
    pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment64)
    $ AddChatter(vig4_sc7_epilogue_comment65)
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_epilogue_comment66)
    pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment67)
    pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment68)
    pause 1.0
    if viewershipHigh == True:
        $ AddChatter(vig4_sc7_epilogue_comment69)
        pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment70)
    pause 0.5
    $ AddChatter(vig4_sc7_epilogue_comment71)
    stop music fadeout 6.0
    "Slowly, but surely the chat in the stream winds down."
    "For the last time while streaming {i}Oakley 2: Settle the Score{/i}, you take off your headset, and sign off of Flinch."
    hide screen streamChat
    hide screen streamDetails
    scene black with dissolve
    jump vig4_macro_start

label vig4_macro_start():
    hide cockpit_stream
    $ vignette4 = True
    play music "soundtrack/postStreamGroove.wav" volume 0.8 loop fadein 2.0
    $ narrator = reg_narrator
    #$ macroNarration = True
    $ macroChoice = True
    if csEngagement > pdEngagement and csEngagement > kcEngagement:
        $ topfan = "Coriolis"
    elif kcEngagement > pdEngagement and kcEngagement >= csEngagement:
        $ topfan = "kitcat"
    elif pdEngagement >= kcEngagement and pdEngagement >= csEngagement:
        $ topfan = "pickledDragons"
    else:
        $ topfan = "Coriolis"
    "That was the last stream."
    "It's the moment of truth." 
    "Time to check Flinch."
    jump FlinchAnalytics_vig4

label vig4_macro_mod_1():
    $ menu = nvl_menu
    mod_nvl "Yoyoyo!"
    mod_nvl "Another great stream!"
    jump FlinchAnalytics_vig4

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

label vig4_macro_viewerChat_1(): #it would be cool for all three viewers to say something to you and vary it based on engagement levels
    nvl clear
    $ menu = nvl_menu
    scene discordview with dissolve
    $ screenComplete = False
    $ loopdView = True
    $ menu = nvl_menu
    if topfan == "Coriolis":
        "It's from Coriolis."
        cs_nvl "Hey [username]! Wanted to let you know how much I appreciate all your streams"
        cs_nvl "I know it's been a journey, and I just want you to know how fun it's been to go on this ride with you"
        cs_nvl "Truly, it's been a pleasure"
        cs_nvl "I'll see you at the next stream!"
        menu:
            "•Thank you!":
                player_nvl "Thank you so much, Coriolis!"
                player_nvl "It really means a lot that you've been sticking around since the beginning"
                player_nvl "See you at the next stream!"
            "•Say nothing.":
                "You decide not to reply."
                "Their comments speak for themselves."
    elif topfan == "kitcat":
        "It's from kitcat."
        kc_nvl "Hey [username], don't have much to say here, just wanted to say thanks again for all the streams!"
        kc_nvl "Can't believe I had never been to one of your streams before the first one for Oakley 2, and I'm so glad I stumbled into it"
        kc_nvl "It's been a really fun ride!"
        kc_nvl "Hope to see you around!"
        menu:
            "•Thank you!":
                player_nvl "Thank you so much, kitcat!"
                player_nvl "I really appreciated your positivity in the chat!"
                player_nvl "And I'm sure we'll see each other around!"
            "•Say nothing.":
                "You decide not to reply."
                "Their comments speak for themselves."
    elif topfan == "pickledDragons":
        "It's from pickledDragons."
        pd_nvl "Hey [username], just wanted to say thank you for all these streams"
        pd_nvl "It's been a lot of fun to watch you play the game and do things I wouldn't normally do"
        pd_nvl "Seriously, I don't know if I could've gone Outlaw as much as you did this playthrough"
        pd_nvl "So, on behalf of the whole chat, thank you for giving that a go!"
        pd_nvl "Hope to see you around!"
        menu:
            "•Thank you!":
                player_nvl "Thank you so much, pickledDragons!"
                player_nvl "I had a lot of fun hearing your perspective on the game!"
                player_nvl "I'm sure we'll see each other around!"
            "•Say nothing.":
                "You decide not to reply."
                "Their comments speak for themselves."
    else:
        "It's from Coriolis."
        cs_nvl "Hey [username]! Wanted to let you know how much I appreciate all your streams"
        cs_nvl "I know it's been a journey, and I just want you to know how fun it's been to go on this ride with you"
        cs_nvl "Truly, it's been a pleasure"
        cs_nvl "I'll see you at the next stream!"
        menu:
            "•Thank you!":
                player_nvl "Thank you so much, Coriolis!"
                player_nvl "It really means a lot that you've been sticking around since the beginning"
                player_nvl "See you at the next stream!"
            "•Say nothing.":
                "You decide not to reply."
                "Their comments speak for themselves."
    "It was nice of them to send a message."
    "You should check out blueit now. See what the rest of the community is saying about the finale."
    $ screenComplete = True
    #jump blueitVignette4_1
    call screen webNavigation_vig4
    scene bg black with dissolve

label FlinchAnalytics_vig4():
    $ menu = adv_menu
    $ screenComplete = False
    $ flinchView = True
    $ flinchCheck = 0
    if viewershipHigh == True:
        $ Affiliate = True
        $ followerGoal = 500
    elif viewershipMed == True:
        $ Affiliate = True
        $ followerGoal = 500
    else:
        $ Affiliate = False
        $ followerGoal = 0
    #scene flinch_v4screen with dissolve
    if Affiliate == True and vig3_viewership == "High":
        scene flinch_v4screen1 with dissolve
    elif Affiliate == True and vig3_viewership == "Low":
        scene flinch_v4screen2 with dissolve
    else:
        scene flinch_v4screen3 with dissolve
    show screen streamAnalytics_Details
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
    "You navigate to the Flinch analytics page."
    "And there it is."
    if Affiliate == False:
        "You missed Affiliate..."
        "9.4 average viewers."
        "You missed by less than one average viewer."
        "..."
        "How do you feel?"
        menu:
            "How do you feel?"
            "I feel horrible.":
                "Screw you, you stupid game. How do you think I feel?"
                "Like crap."
                "I put in all this work, all this time, and I didn't get what I wanted."
                "Does that mean it wasn't worth it?"
                menu:
                    "Does that mean it wasn't worth it?"
                    "It wasn't.":
                        "I see what you're trying to go for."
                        "That whole \"it's about the journey, not the destination\" cliche."
                        "And I get it."
                        "But I wanted this."
                        "{i}Real bad.{/i}"
                        "I'm sorry. I didn't mean to be that harsh."
                        "And I know it doesn't really matter in the long run."
                        "It's just..."
                        "I really wanted to make it this time."
                        "It sucks."
                    "No it was.":
                        "No, you're right. It was worth it."
                        "I got to make some interesting connections and explore the game in a way I normally wouldn't have."
                        "So it was still a worthwhile experience."
                        "But I didn't get the outcome I wanted."
                        "And that sucks."
                        "I know it doesn't really matter in the long run."
                        "I just really wanted to make it this time."
            "It doesn't matter.":
                "Strangely, it doesn't feel like it matters that much to you."
                "After all this time and all that work, maybe getting to Affiliate wasn't the goal."
                "Then what was the goal?"
                menu:
                    "Then what was the goal?"
                    "Community.":
                        "My goal was to build a sense of community with my stream."
                        "Whether Flinch's metrics reward that or not, I think I achieved that."
                        "And that's more important to me."
                    "Integrity.":
                        "I wanted to do this my way, not change just to get Flinch's recognition."
                        "I'm proud of myself for sticking to my guns."
                        "Even though I didn't get what I thought I wanted, I feel good about my choices."
                    "Having fun.":
                        "I just wanted to have fun."
                        "And Flinch's metrics don't reflect the joy I had during this experience."
                        "Whether it was the community I built, or the choices I made, I had fun doing it all."
            "I'm glad I didn't make it.":
                "It's strange, for some reason, you feel... happy to not make Affiliate."
                "Why is that?"
                menu:
                    "Why is that?"
                    "Flinch doesn't dictate my happiness.":
                        "I just wanted to have fun."
                        "And Flinch's metrics don't reflect the joy I had during this experience."
                        "Whether it was the community I built, or the choices I made, I had fun doing it all."
                        "I'm happy because Flinch doesn't get to dictate my happiness."
                    "My community is what matters.":
                        "My goal was to build a sense of community with my stream."
                        "Whether Flinch's metrics reward that or not, I think I achieved that."
                        "And that's more important to me."
                    "My integrity is what matters.":
                        "I wanted to do this my way, not change just to get Flinch's recognition."
                        "I'm proud of myself for sticking to my guns."
                        "Even though I didn't get what I thought I wanted, I feel good about my choices."
    else:
        "You did it!"
        if viewershipHigh == True:
            "Not only did you do it, you smashed the average viewership requirement!"
            "You probably didn't even have to do that last stream and you would have made it!"
        else:
            "It's not by that much, but you cleared the average viewership requirement!"
            "Good thing you had all those viewers for that last stream!"
        "Congratulations, Affiliate!"
        "How does it feel?"
        menu:
            "How does it feel?"
            "It feels good.":
                "It feels so good!"
                "I've been trying to get here for years!"
                "I know it's not much in the grand scheme of things, but just to be here after starting from nothing means a lot."
                "I'm proud of myself for persevering. And it just feels really good!"
            "It's a relief.":
                "It's more of a relief than anything."
                "This has been a weight on my back for a long time."
                "But now to finally be at the end of this journey, it feels like I can let go and just enjoy the ride again."
            "I'm so tired.":
                "I'm so tired."
                "This whole process has been such a grind."
                "I'm sure I'll be happy in a little bit."
                "But right now, I just want to sleep."
            "It's a bit disappointing.":
                "I don't know why exactly, but I feel... disappointed?"
                "Maybe this wasn't as important to me as I thought it was."
                "Maybe something changed over these past few weeks."
                "Maybe I'll feel differently in a couple days."
                "But right now it feels kind of hollow."
    "You could probably stare at this page for hours."
    $ renpy.sound.play("audio/ReceiveText.ogg")
    "But a message on Loop'd gets your attention."
    $ screenComplete = True
    call screen webNavigation_vig4
    #show screen viewershipButton_vig4
    #call screen streamAnalytics_vig4
    hide screen streamAnalytics_vig4 with dissolve

label blueitVignette4_1():
    $ menu = adv_menu
    scene blueit_v4screen at truecenter with dissolve
    $ screenComplete = False
    $ blueitView = True
    $ blueitPages = [] #this line can be deleted eventually. It's here temporarily to make testing a bit easier.
    $ blueitPages.append(vig4_bThread1)
    $ blueitPages.append(vig4_bThread2)
    if amaRomance == True:
        $ blueitPages.append(vig4_bThread3)
    $ blueitPages.append(vig4_bThread4)
    $ blueitPages.append(vig4_bThread5)
    $ blueitPages.append(vig4_bThread6)
    $ blueitPages.append(vig4_bThread7)
    "The Oakley 2 subblueit is buzzing with activity now that the final episode is released."
    "Time to see what people are saying!"
    jump blueitVignette4_2

label blueitVignette4_2():
    scene blueit_v4screen at truecenter
    show screen webNavigation_vig4
    if blueitCheck == 3:
        $ screenComplete = True
        "Hm, maybe it would be a good idea to write a post about your experience streaming the game."
    elif blueitCheck == 4:
        $ screenComplete = True
    elif blueitCheck == 5:
        $ screenComplete = True
        #"Hm, maybe it would be a good idea to write a post about your experience streaming the game. Once you've finished reading the posts you want to check out, of course."
    elif blueitCheck == 6:
        $ screenComplete = True
    elif blueitCheck == 7:
        $ screenComplete = True
        #"You should write a post about your experience streaming the game."
    elif blueitCheck >= 7:
        $ screenComplete = True
    else:
        pass
    call screen blueit
    return

label vig4_macro_writeUp():
    stop music fadeout 10.0
    scene blueit_finalpostlayout with dissolve
    show screen finalWriteUp
    "I should post something... It's kind of cheesy, but I think it might be a good way to sum up my experience."
    "Let me start with a small introduction."
    pause 1.0
    #$ summaryIntroduction = "Hey everyone! My name is [streamer] and I just finished streaming Oakley2! I wanted to share my thoughts on the end game for our lovely community of galactic cowboys."
    $ summaryIntroduction = "Hey everyone! My name is [streamer] and I just finished streaming Oakley2! I wanted to share my thoughts on the end game for our lovely community of galactic cowboys."
    $ addWriteUp(summaryIntroduction)
    "It's a good start."
    jump vig4_macro_writeUp_2
    
label vig4_macro_writeUp_2():
    #$ mozeReflection = ""
    "For the first part, I want to reflect on what it was like to play as Moze."
    menu:
        #"For the first part, I want to reflect on what it was like to play as Moze."
        "I lost myself in the character...":
            pause 1.0
            $ mozeReflection = "Playing as Moze… tbh it was weird how easily I slipped into Moze’s mindset. Like, the choices weren’t just in character – they were my choices. Moze’s inner turmoil really spoke to me and I found myself acting in unexpected ways because of it."
            $ addWriteUp(mozeReflection)
            "Is that what I want to say?"
            menu:
                #"Is that what I want to say?"
                "Yes.":
                    pass
                "No.":
                    jump vig4_macro_writeUp_2
        "I always felt a bit outside of Moze...":
            $ mozeReflection = "The PC design was interesting. Moze is like the kind of friend I love telling stories about and am decently worried for but I only reach out like 3 times a year max because I know she’d do more harm than good to my life. It felt more like I was putting on a costume when I played as her, or like I was trying to help my problematic friend figure out her life."
            $ addWriteUp(mozeReflection)
            "Is that what I want to say?"
            menu:
                #"Is that what I want to say?"
                "Yes.":
                    pass
                "No.":
                    jump vig4_macro_writeUp_2
        "Moze and I are nothing alike...":
            $ mozeReflection = "I came in I think with this idea of who the character would be, but the more I played the more Moze shifted. Her story isn’t one I relate to, or can even fathom for myself like in the slightest – but it was still a really fun ride. She and I may have nothing in common but I’ll always be rooting for my problematic captain!"
            $ addWriteUp(mozeReflection)
            "Is that what I want to say?"
            menu:
                #"Is that what I want to say?"
                "Yes.":
                    pass
                "No.":
                    jump vig4_macro_writeUp_2
    jump vig4_macro_writeUp_3

label vig4_macro_writeUp_3():
    #$ choiceReflection = ""
    "Okay, that was good. Now I should say something about the kinds of choices I was making in the game..."
    menu:
        #"Okay, that was good. Now I should say something about the kinds of choices I was making in the game..."
        "I just followed the momentum...":
            $ choiceReflection = "The game led me where I think we needed to go. I streamed the whole thing, and I think the chat hive mind plus what made sense with the story hit this nice synthesis where I felt less like a driver and more like a passenger of this well-crafted roller coaster."
            $ addWriteUp(choiceReflection)
            "Is that what I want to say?"
            menu:
                #"Is that what I want to say?"
                "Yes.":
                    pass
                "No.":
                    jump vig4_macro_writeUp_3
        "Making the hard choices was a breeze...":
            $ choiceReflection = "I steered the crew of the Oakley every step of the way. I streamed the whole thing and though not everyone agreed with my choices I stand by them; that’s what it means to be the captain I guess!"
            $ addWriteUp(choiceReflection)
            "Is that what I want to say?"
            menu:
                #"Is that what I want to say?"
                "Yes.":
                    pass
                "No.":
                    jump vig4_macro_writeUp_3
        "I froze a bit...":
            $ choiceReflection = "Man there were some tough moments in the sequel. I never knew what the ‘right’ move was. I streamed the whole game and sometimes chat would be a chorus of a million different opinions, and I wouldn’t be able to even tell you up from down let alone right choice vs wrong choice. We got through it though! Even if we did it mostly in panic mode."
            $ addWriteUp(choiceReflection)
            "Is that what I want to say?"
            menu:
                #"Is that what I want to say?"
                "Yes.":
                    pass
                "No.":
                    jump vig4_macro_writeUp_3
    jump vig4_macro_writeUp_4

label vig4_macro_writeUp_4():
    #$ streamReflection = ""
    "Oh, I should add something on the experience of streaming Oakley 2."
    menu:
        #"Oh, I should add something on the experience of streaming Oakley 2."
        "The chat shaped everything...":
            $ streamReflection = "I kept thinking I was making my own decisions but looking back now the chat definitely had a bigger pull than I thought. Their reactions, jokes, even silence… it shaped my entire playthrough. Upon reflection, it’s a bit scary how much power an audience has!"
            $ addWriteUp(streamReflection)
            "Is that what I want to say?"
            menu:
                #"Is that what I want to say?"
                "Yes.":
                    pass
                "No.":
                    jump vig4_macro_writeUp_4                
        "Streaming kept me grounded...":
            $ streamReflection = "Honestly? Chat helped me a ton. When things got too intense or felt like they were becoming almost personal, I looked over and saw my audience reacting with me. It felt less like a one-player game and more like a shared experience – not just playing for people but with a great group of friends!"
            $ addWriteUp(streamReflection)
            "Is that what I want to say?"
            menu:
                #"Is that what I want to say?"
                "Yes.":
                    pass
                "No.":
                    jump vig4_macro_writeUp_4
        "I didn't even notice chat half the time...":
            $ streamReflection = "The game was so fast-paced and immersive that I ended up being so locked in that I barely glanced at the chat. I know they were there and reacting/talking to each other but in the game moments I was too concentrated to notice. Not sure if that makes me a bad streamer or it shows how good Oakley 2 was…"
            $ addWriteUp(streamReflection)
            "Is that what I want to say?"
            menu:
                #"Is that what I want to say?"
                "Yes.":
                    pass
                "No.":
                    jump vig4_macro_writeUp_4
    jump vig4_macro_writeUp_5

label vig4_macro_writeUp_5():
    #$ affiliateReflection = ""
    if Affiliate == True:
        "I guess I'll finish it with my thoughts on making affiliate."
        menu:
            #"I guess I'll finish it with my thoughts on making affiliate."
            "I feel positive about achieving Affiliate...":
                $ affiliateReflection = "BUT I DID IT! WE MADE AFFILIATE FINALLY! And it feels oh-so good! It’s so funny: I went full dark mode for this stream and the chaos totally pulled people in. You know what though? I had so much fun. I never would have played like that off-stream so I’m grateful for the audience that pushed me to be so diabolical. I’m glad this is how it all worked out. I have no regrets, none at all."
                $ addWriteUp(affiliateReflection)
                "Is that what I want to say?"
                menu:
                    #"Is that what I want to say?"
                    "Yes.":
                        pass
                    "No.":
                        jump vig4_macro_writeUp_5
            "I feel kind of negative about achieving Affiliate...":
                $ affiliateReflection = "So, I made affiliate… and if I’m being real, though it feels weird admitting it, I’m not too thrilled. I don’t really feel good about the way I played the game… I wasn’t me: I played it up, leaned into some stuff I don’t normally do. It’s what got me to my goal, but now I’m feeling guilty instead of excited."
                $ addWriteUp(affiliateReflection)
                "Is that what I want to say?"
                menu:
                    #"Is that what I want to say?"
                    "Yes.":
                        pass
                    "No.":
                        jump vig4_macro_writeUp_5
    else:
        "I guess I'll finish it with my thoughts on not making affiliate."
        menu:
            "I guess I'll finish it with my thoughts on not making affiliate."
            "I'm feeling positive about not achieving affiliate...":
                $ affiliateReflection = "Didn’t hit affiliate in the end but I’m okay with it. I played how I wanted to play. I made the choices that felt honest and good, even if they didn’t blow the streaming world up. And honestly? I’d rather be me than gain an audience being something I’m not. I’m glad the game ended the way it did for my first stream of it!"
                $ addWriteUp(affiliateReflection)
                "Is that what I want to say?"
                menu:
                    #"Is that what I want to say?"
                    "Yes.":
                        pass
                    "No.":
                        jump vig4_macro_writeUp_5
            "I'm feeling negative about not achieving affiliate...":
                $ affiliateReflection = "Still not affiliate… I said this was going to be my last go at it. I checked the numbers hoping they would tick but they didn’t and ngl it does suck. I wanted this to be the stream that changed that… maybe I did play it too safe. Or maybe the way I play is just not something people want to watch."
                $ addWriteUp(affiliateReflection)
                "Is that what I want to say?"
                menu:
                    #"Is that what I want to say?"
                    "Yes.":
                        pass
                    "No.":
                        jump vig4_macro_writeUp_5
    jump vig4_macro_writeUp_6

label vig4_macro_writeUp_6():
    "That feels right."
    "Now I should come up with a title for the post."
    "Something catchy, but also something that reflects my journey."
    $ blueitPostTitle = renpy.input("What should I call the post? ", length = 40)
    "There. All done."
    "That feels like it sums up my experience appropriately."
    call screen closeComputer


label vig4_macro_brother_1():
    nvl clear
    $ menu = nvl_menu
    "Final test."
    jump endgame

label endgame():
    hide screen finalWriteUp with Dissolve(2.0)
    scene bg black with dissolve
    "I should go."
    "Been on this screen for a bit too long today."
    "Maybe I can hit up Jessie to grab some ramen."
    "And next week I take a flight back home for Thanksgiving."
    "Can't wait to catch up with El in person."
    pause 2.0
    scene game_main_menu with dissolve
    "Congratulations, you have finished {i}Stream Evil{/i}!"
    "On behalf of the entire team at mLab productions, we would like to say:"
    "THANK YOU!"
    "We hope you have a wonderful day!\n-Beck, Josh, Jules, Justin, and Mia"
    $ renpy.full_restart()