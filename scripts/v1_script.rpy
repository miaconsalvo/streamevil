label vignette1Start():
    $ vignette1 = True
    $ vignette2 = False
    $ vignette3 = False
    $ vignette4 = False
    scene streamview
    show screen streamChat
    show screen streamDetails
    show vig1_town_stream at topleft onlayer background with dissolve
    $ narrator = alt_narrator
    $ viewCheck1 = 2
    $ viewCheck2 = 3
    $ viewCheck3 = 4
    $ viewCheck4 = 6
    $ viewCheck5 = viewCount
    jump returnToWorkshop

label returnToWorkshop():
    play music "soundtrack/allistar.wav" volume 1.0 loop fadein 1.0
    show screen chatTutorial2
    call screen streamFreeze
    "Thermal paste in hand I return to Allistar's workshop."
    show vig1_allistar_workshop at topleft onlayer background with dissolve
    hide vig1_town_stream
    show mac stream at stream_center_mac with dissolve
    show allistar stream neutral at stream_right with dissolve
    "MAC is in the center of the room, a faint trill of classical music whistles from his voice box."
    "Allistar sits on a chair behind the droid, still working on the open circuit panel in MAC's back." 
    aS "Moze, did you know MAC likes music?" 
    aS "It has recordings of every Beethoven symphony stored in its memory banks."
    play audio "macAffirmative.wav" volume 1.5
    macS "Ludwig van Beethoven was my father's favorite composer."
    $ AddChatter(vig1_sc2_comment1)
    pause 0.5
    aS "\"Father\"?"
    macS "Yes, Dr. Cog. He built and educated me. Before he died that is."
    aS "Cog. Why do I know that name?"
    mS "He was BigCorp's head of research and development. Was working on a top secret project before he ran off with company secrets."
    aS "What project?"
    "Allistar looks up to me, then back to MAC."
    aS "I'm working on it, aren't I?"
    mS "Yes."
    "Allistar pauses, his head hanging."
    "He reaches his hand out."
    aS "Thermal paste."
    "I pass him the tube."
    show allistar stream thinking
    aS "Do you ever think about the Snakehawks, Moze? What the old crew was, what we became?"
    menu:
        aS "Do you ever think about the Snakehawks, Moze? What the old crew was, what we became?"
        "Not really.":
            mS "I don't dwell on the past much. These days I have to keep my attention on the present."
            aS "Almost seems like a luxury."
        "We were a family.":
            $ macHope += 1
            mS "It's simple: Ama took care of us and we took care of each other. We were all we had. A family."
            aS "And now that family's completely disintegrated."
        "We were just a bunch of people getting by.":
            $ macHope -= 1
            mS "We were always just a bunch of people who needed somewhere to go. And Ama was a good leader, paid well."
            aS "Surprising to hear from you considering how close you were with Deadeye. And that Jennica's stuck around with you."
    aS "I've been thinking a lot about our legacy ever since Deadeye's heist on BigCorp went wrong."
    aS "The Snakehawks are all dead, except a few of us, and now the great Ama \"Deadeye\" Reyes is a lapdog for BigCorp."
    aS "BC's grip on their planets has tightened, and a lot of people blame us. When they think of \"Snakehawks\" they just think of pain."
    aS "They {i}hate{/i} us here."
    show screen chatTutorial
    $ AddChatter(vig1_sc2_comment2)
    pause 0.5
    mS "Why did you come here if they hate us so much?"
    aS "Guilt, I suppose. I wanted to go somewhere quiet."
    hide screen chatTutorial
    $ vig1_sc2_comment2.click = False
    $ vig1_sc2_comment2_csSH.click = False
    $ vig1_sc2_comment2_csAma.click = False
    aS "People didn't trust me for a while. That's what this tattoo is good for these days."
    aS "Most townsfolk still don't like me, but they are grateful for my work." 
    aS "I can live with that."
    aS "But I keep thinking, what could the Snakehawks..."
    aS "What could {i}we{/i} have accomplished if we tried to be more than a gang of outlaws."
    show allistar stream neutral
    "He leans back from MAC and starts screwing the metal plate back in."
    aS "All done. Circuits should be resistant to electricity and overheating now."
    "MAC rolls forward into a clear space in the room."
    macS "System functions restored to normal.\nProbability of celebration: 100\%."
    play audio "macSpin.wav" volume 1.5
    "The music from MAC's voice box crescendoes as he begins spinning rapidly in place."
    $ AddChatter(vig1_sc2_comment4)
    pause 0.5
    play audio "macHappy.wav" volume 1.5
    macS "Thank you, Dr. Collins!"
    aS "Hahaha I'm no doctor, but you're very welcome."
    menu:
        aS "Hahaha I'm no doctor, but you're very welcome."
        "He's kind of endearing.":
            mS "He gets to you, doesn't he?"
    aS "Yes, I suppose he does."
    jump shipCall

label shipCall:
    $ viewCheck6 = viewCount
    "I put a hand on Allistar's shoulder."
    mS "Thanks for your help, Al. We'll be on our way now."
    play audio "callRing.wav" volume 1.5
    #"{i}beep beep beeeep{/i}"
    "My communicator rings. Jennica's voice crackles out."
    pS "Moze? We've got some trouble: there's a long range caller insisting on speaking with you."
    pS "Says they want to warn us about something. Teresa confirmed it's not BigCorp."
    mS "Patch the call through."
    "Faint static crunches as the lines switch."
    mS "This is Captain Moze of the Oakley. Who is this?"
    play music "soundtrack/deadeye.wav" volume 1.0 loop fadein 4.0
    amaS "My dear Mozely. It's good to hear your voice again."
    show allistar stream mad
    "I almost drop the communicator. Allistar goes stiff, his eyes wide with disbelief."
    aS "Deadeye."
    mS "Ama? Why are you calling?"
    $ AddChatter(vig1_sc2_comment5)
    pause 0.5
    amaS "So direct, Mozely. I always liked that about you." 
    amaS "Your penchant for sloppy scores, however, has gotten tiresome."
    amaS "BigCorp authorities have identified your vessel docked in the spaceport of Grand Junction on Cromuu."
    amaS "Several squads have been dispatched to apprehend you and your crew." 
    mS "Why are you telling me this?"
    amaS "BC hired me to hunt you down and return that little droid you've stolen."
    amaS "It's nothing personal, dear. Just business."
    amaS "Of course, I won't get any reward if BC apprehends you themselves." 
    amaS "So why don't you run along to your little ship and set sail."
    amaS "Oh, and take Allistar with you." 
    amaS "BigCorp has labeled him an accomplice, and I'd hate for him to suffer in a prison on your account."
    show allistar stream thinking
    amaS "Take care, Mozely. Do try to make this hunt interesting."
    play audio "cutCall.wav" volume 1.5
    "The line cuts. The room is silent."
    macS "Captain? You appear distressed."
    play audio "callRing.wav" volume 1.5
    "Another ring from the communicator. It's Teresa; her voice is frantic and rushed."
    enS "Captain! We just identified several BC land cruisers heading toward Grand Junction."
    play backAudio "lazerFireCall.wav" volume 1.0 loop
    "The sound of blaster fire erupts through the coms."
    pS "Light speeders have already dropped a couple squads in the port. They're firing on the ship!"
    enS "We can hold them off for a bit, but you have to get back here before those cruisers or we're done for!"
    pS "Shit, Teresa, guard that ramp! I'll cover you with the turrets!"
    stop backAudio
    play audio "cutCall.wav" volume 1.5
    "The line cuts."
    "Adrenaline floods my body."
    mS "Time to move. MAC, let's go."
    "Allistar does not move."
    aS "Moze, what have you done?"
    menu:
        aS "Moze, what have you done?"
        "What I had to do.":
            $ macHope -= 1
            mS "I did what I had to do."
            mS "BigCorp {i}cannot{/i} get hold of MAC."
            mS "They didn't leave me with a choice."
        "Saved the galaxy.":
            $ macHope += 1 
            mS "I saved the galaxy."
            mS "We don't know what BC wants with MAC, but we know it's bad."
            mS "We {i}cannot{/i} let them get hold of him."
    "Allistar is perfectly still."
    show allistar stream mad
    "Then he rushes to a nearby drawer, lifts out a blaster, and sets it to stun."
    aS "It's a straight shot to the spaceport. Our best bet is a full sprint."
    $ AddChatter(vig1_sc2_comment6)
    pause 0.5
    "I follow Allistar to the front door. He grips the handle."
    macS "Captain, what's happening?"
    menu:
        macS "Captain, what's happening?"
        "The bad people are here.":
            mS "The bad people who want to take you away are here."
            mS "But Allistar and I are not going to let that happen."
            mS "We're going to run back to the ship. Just stay close to me and if I tell you to run, don't stop until you get the ship."
        "Everything's going to be okay.":
            mS "We've run into a bit of trouble, but it's okay, Allistar and I can handle it."
            mS "We're going to run back to the ship. Just stay close to me and if I tell you to run, don't stop until you get the ship."
    play audio "macAffirmative.wav" volume 1.5
    "MAC hums back an affirmative beep."
    aS "You ready?"
    "What should I set my blaster to?"
    $ vig1_sc2_comment6.click = False
    jump setBlasterVig1

label setBlasterVig1():
    $ narrator = alt_narrator
    #$ macroChoice = False
    menu:
        "What should I set my blaster to?"
        "Set blaster to stun":
            mS "Ready."
        "Set blaster to lethal":
            $ narrator = reg_narrator
            "Hm, that feels a bit unnecessary. They're just regular goons after all."
            #$ narrator = alt_narrator
            jump setBlasterVig1
    "Allistar nods and swings the door open. Light bursts into my eyes."
    hide mac with Dissolve (0.1)
    hide allistar with Dissolve (0.1)
    jump streetShootout

label streetShootout:
    play music "soundtrack/savethegalaxy.wav" volume 1.0 loop fadein 1.5
    show vig1_town_stream at topleft onlayer background with Fade(0.5, 0.5, 0.5, color="#FFFFFF")
    hide vig1_allistar_workshop
    "Allistar, MAC, and I rush into the deserted main street of Grand Junction."
    "My feet pound against the hardpacked ground. The spaceport is dead ahead of us."
    show bc_enforcer at stream_center with dissolve
    "And so are BigCorp goons, six enforcers wearing telltale blue and grey uniforms."
    play backAudio "lazerFire.wav" volume 1.5 loop
    "We shoot on instinct, blaster bolts streaking across the desert sand."
    "I dive into cover around the side of a building as they return fire."
    $ AddChatter(vig1_sc2_comment7)
    pause 0.5
    "The enforcers disperse. One takes a speeder and veers off while three duck into the alleys."
    "Two advance down the main street toward us."
    hide bc_enforcer with dissolve
    play backAudio "lazerFire.wav" volume 0.6
    mS "BC scum."
    aS "Moze!"
    show allistar stream mad at stream_right with Dissolve (0.5)
    "Allistar ducks into cover behind some nearby barrels."
    aS "We can't get pinned down!"
    "A light bump taps me on the knee."
    show mac stream at stream_center_mac with Dissolve(0.5)
    macS "Affirmative, our survival rate in the current situation is 5\%."
    menu:
        macS "Affirmative, our survival rate in the current situation is 5\%."
        "Good initiave, MAC.":
            $ macHonesty += 1
            $ kcEngagement += 1
            mS "I'm glad you're trying to help, MAC."
            "A bolt collides in the dirt. I fire a shot back and hit an enforcer right between the eyes, knocking them to the floor."
            mS "But we need something more than probabilities right now."
        "Not helping!":
            $ macHonesty -= 1
            mS "Not helping, MAC!"
            "A bolt collides in the dirt.  I fire a shot back and hit an enforcer right between the eyes, knocking them to the floor."
            $ AddChatter(vig1_sc2_comment8_kc)
            pause 0.5
            mS "Can you locate those other enforcers?"
    macS "Right."
    mS "Thank you."
    play audio "macPing.wav" volume 1.5
    macS "No, Captain. Right. As in East."
    "I glance to my right. There's a single enforcer riding a light speeder between buildings. It's making a beeline for MAC."
    aS "Moze, on the building!"
    "Two enforcers have taken up positions on a building directly in front of us and are moving to get a shot on Allistar."
    "The remaining enforcer on the ground is closing on my cover."
    "They're advancing fast."
    $ AddChatter(vig1_sc2_comment9)
    pause 0.5
    $ AddChatter(vig1_sc2_comment10)
    $ reactTarget = "vig1_sc2_combatReact" #We need to set this so the reaction button will direct to the label we want to go to
    $ viewCheck7 = viewCount
    menu:
        "They're advancing fast."
        "Fire on rooftop (protect Allistar)":
            $ csEngagement += 1
            "I turn my attention to the rooftop threat."
            "Mine and Annatar's fire forces them into cover, but not before one of them takes a hit and falls off the back of the building."
            "The last one pokes their head up and Allistar hits them right between the eyes."
            show bc_enforcer at stream_left with Dissolve(0.3)
            stop backAudio
            "At that moment the ground enforcer rounds the corner, about to fire."
            hide allistar with Dissolve (0.3)
            mS "MAC, run!"
            hide mac with Dissolve(0.3)
            show bc_enforcer at stream_center with move
            "Knocking the blaster out of his hand, I tackle him to the ground."
            "We roll over one another as he reaches for his gun."
            "He's too slow."
            "I pull my pistol to his chest and fire two rapid shots."
            play audio "lazer.wav" volume 5.0
            pause 0.4
            play audio "lazer.wav" volume 5.0
            hide bc_enforcer with Dissolve (0.3)
            "Struggling to my feet, I look up to see MAC rolling quickly down the street toward the port."
            "Then the speeder rushes past me, bearing down on MAC."
            $ AddChatter(vig1_sc2_comment11)
            pause 0.5
            "I fire at it, but every shot goes wide."
            "The speeder is almost at MAC, the enforcer reaching down to lift him up."
            play audio "lazer.wav" volume 6.0
            "A blaster bolt collides with the back of the speeder, turning the engine into a fireball and sending the enforcer flying through the air."
            "He skids into the dirt and lays still."
            show allistar stream mad at stream_right with Dissolve (0.5)
            "I turn back around. Allistar holds a smoking blaster upright."
            show screen chatTutorial2
            show screen streamerCommentary
            aS "Lucky shot."
            mS "Are you good?"
            aS "Yeah. You?"
            "I nod and we rush off toward MAC."
            hide screen streamerCommentary
            hide screen chatTutorial2
        "Fire at speeder (protect MAC)":
            $ kcEngagement += 1
            "I fire at the speeder, sending bolts directly into the metal."
            $ AddChatter(vig1_sc2_comment11)
            pause 0.5
            "They force the vehicle off balance as the nose dips into the sand, sending the enforcer flying through the air and skidding into the hard dirt."
            "The enforcers on the rooftop bear down on us."
            "Allistar and I quickly return fire from our precarious position, forcing them into cover."
            "A hail of blaster bolts go in both directions, but as they move to get closer, I manage to land a shot in one of their chests, knocking them down."
            show bc_enforcer at stream_left with Dissolve(0.3)
            stop backAudio
            enforcer "Freeze!"
            hide allistar with Dissolve(0.3)
            "The enforcer on the ground rounds the corner, but that single word of hesitation gives me just enough time."
            "I dive forward as they try to fire."
            mS "MAC, run!"
            play audio "lazer.wav" volume 5.0
            hide mac with Dissolve(0.3)
            "The blast goes wide and I tackle him to the ground."
            show bc_enforcer at stream_center with move
            "We roll over each other. Biting, punching, kicking. But he lands on top of me and wraps his hands around my throat."
            "He starts squeezing as I frantically push my hands up against his face, trying to find purchase, trying to knock him off."
            play audio "lazer.wav" volume 4.0
            enforcer "Aiieea!"
            hide bc_enforcer with Dissolve (0.3)
            "The enforcer reels up and falls to the ground."
            show allistar stream mad at stream_right with Dissolve (0.5)
            "Allistar holds his right shoulder gingerly, a light trail of smoke from a blaster bolt flickers in the air."
            "He grimaces."
            show screen chatTutorial2
            #$ AddCommentary(vig1_sc2_streamer1)
            show screen streamerCommentary
            aS "Lucky shot."
            mS "Allistar, are you okay?"
            aS "My shoulder's messed up, but I'll live."
            "I nod and we rush off toward MAC."
            hide screen streamerCommentary
            hide screen chatTutorial2
        "Fire at ground enforcer (protect Moze)":
            "I pop back around the corner to fire at the enforcer on the ground."
            "They take cover in response and we trade shots back and forth, until they make the mistake of holding their shoulder out in the open."
            "I hit it with a direct shot, taking them out of the battle."
            "As they slump to the ground, the enforcers on the building bear down on us."
            mS "MAC, run!"
            hide mac with Dissolve(0.3)
            "I dive behind cover next to Allistar, hoping to draw their fire."
            "It works and a rain of blaster fire falls upon me and Allistar as MAC rolls toward the spaceport."
            "A shot grazes Allistar's shoulder. He grimaces."
            "A break in the hail of bullets."
            "Popping out of cover, Allistar and I land two quick shots while the enforcers are out in the open."
            "They fall limply to the ceiling."
            stop backAudio
            "As Allistar and I stand up from the cover, the speeder careens past us, bearing down on MAC."
            $ AddChatter(vig1_sc2_comment11)
            pause 0.5
            "I fire at it, but every shot goes wide."
            "The speeder is almost at MAC, the enforcer reaching down to lift him up."
            play audio "lazer.wav" volume 6.0
            "A blaster bolt collides with the back of the speeder, turning the engine into a fireball and sending the enforcer flying through the air."
            "He skids into the dirt and lays still."
            "Allistar holds his shoulder, wincing in pain."
            show screen chatTutorial2
            show screen streamerCommentary
            aS "Lucky shot."
            mS "Allistar, are you okay?"
            aS "My shoulder's messed up, but I'll live."
            "I nod and we rush off toward MAC."
            hide screen streamerCommentary
            hide screen chatTutorial2
    hide allistar with Dissolve(0.5)
    show mac stream at stream_center_mac with Dissolve (0.5)
    mS "MAC!"
    "MAC stops and turns to face us."
    macS "Captain, the probability of our safe escape has risen to nearly 100\%!"
    stop music fadeout 2.0
    #$ renpy.music.set_volume(0.2, 1)
    #play music "audio/soundtrack/decisionTime.wav" volume 0.5 fadein 1.0 loop
    #stop music
    "As MAC finishes, I see it out of the corner of my eye."
    "A rifle perched delicately on a roof. The shooter hidden from view."
    "MAC is completely exposed, one shot will destroy him."
    $ AddChatter(vig1_sc2_comment14)
    pause 0.5
    "I glance back down and see a tank of fuel next to the building."
    "A blaster bolt could send the whole place to Hell."
    "Then I see through the window, a couple cowering in the corner."
    "I process the information in less than a second, then react."
    jump saveMAC

label saveMAC():
    menu:
        "I process the information in less than a second, then react."
        "Dive in front of the shot.":
            $ kcEngagement += 1
            $ macViolence -= 1
            #$ renpy.music.set_volume(1.0)
            "The thought doesn't even linger in my mind."
            "I take one more step then dive in front of MAC."
            play audio "lazer.wav" volume 7.0
            "The sound of a rifle firing resonates behind me."
            "Pain explodes in my left shoulder as I fall to the ground."
            aS "Moze!"
            macS "Captain!?"
            play audio "lazer.wav" volume 2.0
            "The sound of another shot fired and a body hitting the ground from a great height."
            show allistar stream neutral at stream_right with dissolve
            $ AddChatter(vig1_sc2_comment15)
            pause 0.5
            "Allistar crouches beside me and wraps my right arm over his shoulder."
            mS "The sniper?"
            aS "I got him."
            macS "Captain, your vitals have spiked."
            mS "I'm fine, MAC."
            macS "But my sensors indicate you are in great pain."
            menu:
                macS "But my sensors indicate you are in great pain."
                "I'm {i}fine{/i}.":
                    $ macHonesty -= 1
                    "I grimace."
                    mS "MAC, I said I'm {i}fine{/i}."
                    play audio "macSad.wav" volume 1.5
                    "MAC whirs lowly and tilts his head downward."
                "I am in pain.":
                    $ macHonesty += 1
                    "I grimace."
                    mS "I am in pain, MAC."
                    mS "But we have to go."
                    play audio "macPing.wav" volume 1.0
            "Allistar helps me to my feet."
            aS "Can you run?"
            mS "I'm going to have to."
            stop music fadeout 4.0
            hide mac with dissolve
            hide allistar with dissolve
            jump spacePortEscape
        "Blow up the house.":
            $ houseExplosion = 0
            $ houseExplosion += 1
            $ narrator = reg_narrator
            "Killing civilians? Couldn't be me."
            $ narrator = alt_narrator
            if houseExplosion >= 3:
                pass
                #AddChatter(kitcat comment about time)
            jump saveMAC

label spacePortEscape():
    play music "soundtrack/savethegalaxy.wav" volume 1.0 fadein 1.0 loop
    show vig1_spaceport at topleft onlayer background with dissolve
    hide vig1_town_stream
    $ viewCheck8 = viewCount
    if houseExplosion >= 1:
        $ AddChatter(vig1_sc2_comment16)
        pause 0.5
    play backAudio "lazerFire.wav" volume 0.7 loop
    "Rushing through the spaceport gate, we fire at enforcers trying to block our way."
    "The Oakley is under siege, its mounted turrets firing wildy."
    show teresa stream shock at stream_center with dissolve
    "Teresa is in cover inside the ship, popping out occasionally to shoot at advancing enforcers."
    "She catches sight of us and turns around to shout something into the ship."
    $ vig1_sc2_comment16.click = False
    "We dispatch two enforcers on our way as the turret's rate of fire increases."
    "The enforcers have to take shelter while we rush up the ramp and into the ship."
    enS "They're inside! Jennica, get us out of here!"
    pS "Copy!"
    hide teresa with dissolve
    show jennica stream angry at stream_center with dissolve
    "We all rush up to the ship's bridge as Jennica begins liftoff procedures."
    show allistar stream neutral at stream_right with Dissolve (0.5)
    show mac stream at stream_left_mac with Dissolve(0.5)
    pause 0.5
    stop backAudio fadeout 16.0
    pS "Nice of y'all to join us. Remind me to never visit Cromuu again."
    "Just as the ship begins to push off the ground, four immense BigCorp cruisers crest over a nearby hill."
    mS "Jennica? We have to go {i}now{/i}!"
    pS "I know, I know, I see them too!"
    play audio "jetLaunch.wav" volume 4.0
    play backAudio "jetEngines.wav" volume 1.0
    "Jennica slams a thruster forward and the ship lurches into the air."
    "Bolts fire from the cruisers and detonate all around us as we ascend into the atmosphere."
    stop music fadeout 4.0
    stop backAudio fadeout 4.0
    "And then the attack stops. The turbulence on the ship dissipates. We're floating in space."
    "Jennica breathes a sigh of relief and punches something in on a keypad."
    "With a flick of a switch, the Oakley lurches forward into hyperspace. Away from Cromuu and Grand Junction."
    hide jennica with dissolve
    hide mac with dissolve
    hide allistar with dissolve
    jump councilDebrief

label councilDebrief():
    play music "soundtrack/vig1scratchtrack.wav" volume 0.7 loop fadein 1.0
    show shiphub_stream at topleft onlayer background with dissolve
    hide vig1_spaceport
    show teresa stream neutral at stream_right with dissolve
    show jennica stream neutral at stream_left with dissolve
    pS "We've been in hyperspace for about an hour. And we got out before the cruisers were within range of us." 
    $ AddChatter(vig1_sc3_comment1)
    pause 0.5
    pS "We should be clear of any BC tracking devices."
    enS "\"Should\" be. Deadeye shouldn't have been able to track us to Cromuu in the first place."
    mS "We'll need to be more careful in the future, and find a way to stay under the radar."
    pS "Any ideas?"
    mS "Maybe. I need to think."
    "We're all quiet. No {i}bzzrts{/i}, no random facts about our past lives or percentage calculations."
    "...no MAC."
    mS "Does anyone know where MAC is?"
    play backAudio "shipAlarm.wav" volume 1.0
    shipcom "Attention crew, escape pod procedure activated."
    $ viewCount += 1
    $ AddChatter(vig1_sc3_raid_comment1)
    pause 1.0
    $ viewCount += 2
    $ AddChatter(vig1_sc3_raid_comment2)
    pause 1.0
    $ viewCount += 5
    $ AddChatter(vig1_sc3_raid_comment3)
    pause 0.3
    $ AddChatter(vig1_sc3_raid_comment4)
    $ narrator = reg_narrator
    "Woah, that view count can't be right."
    $ renpy.music.set_volume(0.4, 1,"backAudio")
    pause 0.05
    $ viewCount += 17
    $ AddChatter(vig1_sc3_raid_comment5)
    pause 0.7
    $ AddChatter(vig1_sc3_raid_comment6)
    pause 0.5
    $ AddChatter(vig1_sc3_raid_comment7)
    pause 0.7
    $ AddChatter(vig1_sc3_raid_comment8)
    pause 0.8
    $ narrator = alt_narrator
    mS "Shit, what trouble is he getting into now."
    "I rush out of the council room."
    hide teresa with dissolve
    hide jennica with dissolve
    stop backAudio
    $ narrator = reg_narrator
    $ renpy.sound.play("audio/ReceiveText.ogg")
    pause 0.5
    "A private notification on Clamor from my mod, Jessie."
    #insert discord sound effect
    call screen discordNotification
    $ viewCount += 8
    $ AddChatter(vig1_sc3_raid_comment9)
    pause 0.8
    $ AddChatter(vig1_sc3_raid_comment10)
    pause 0.7
    $ AddChatter(vig1_sc3_comment2)
    pause 0.5
    $ AddChatter(vig1_sc3_raid_comment11)
    pause 0.7
    $ AddChatter(vig1_sc3_raid_comment12)
    pause 0.7
    $ AddChatter(vig1_sc3_raid_comment13)
    pause 0.7
    "A raid!? I have to say something."
    $ macroChoice = True
    menu:
        "A raid!? I have to say something."
        "What's up guys!":
            player "What's up guys!"
            player "Great to have new friends in chat."
        "Wow, that's a lot of people.":
            player "Wow, that's a lot of people."
            player "Hope y'all are ready for some fun!"
        "Welcome.":
            player "Hi everyone, welcome to chat!"
            player "I'm pumped to have y'all!"
    player "For all the new folks, I'm [streamer]."
    menu:
        "My stream is story-focused.":
            $ story = True
            player "I've been streaming for almost three years now, usually RPGs, every now and then some action games."
            player "Usually we like to chat about the game's writing."
            player "What we like about the stories, details to critique, theories about where the narrative's going, things like that."
            menu:
                player "What we like about the stories, details to critique, theories about where the narrative's going, things like that."
                "Let's go!":
                    player "So welcome aboard, and let's settle some scores!"
        "My stream loves a good joke.":
            $ humour = True
            player "I've been streaming for almost three years now, usually RPGs and occasionally a multiplayer shooter."
            player "Chat's always the spot for some solid memes and funny bits!"
            player "Good jokes keep me on my toes and helps us all be entertained."
            menu:
                player "Good jokes keep me on my toes and helps us all be entertained."
                "Let's go!":
                    player "So welcome aboard, and let's settle some scores!"
        "My stream is all about vibes":
            $ vibes = True
            player "I've been streaming for almost three years now, usually RPGs and some small indie games too."
            player "We're all about chill vibes hear."
            player "So we take it easy and just go wherever the games take us!"
            menu:
                player "So we take it easy and just go wherever the games take us!"
                "Let's go!":
                    player "So welcome aboard, and let's settle some scores!"
    $ AddChatter(vig1_sc3_comment3_bandit0)
    call screen raidFreeze
    "Shit, was that cringey?"
    $ viewCheck9 = viewCount
    $ macroChoice = False    
    $ narrator = alt_narrator
    jump escapePodConfrontation

label escapePodConfrontation:
    show ship_hallway at topleft onlayer background with dissolve
    hide shiphub_stream
    $ macroChoice = False
    "I run down the halls of the ship and leap over the railing leading down to the escape pod bay."
    #$ AddChatter(vig1_sc3_comment4)
    "As I near the pods, I hear Allistar's voice."
    aS "Come on Mac, you can trust me. We can live a safe life. You don't have to be on the run all the time."
    macS "But Captain said to stay close to her."
    aS "I know Mac. But Moze isn't always right. This place is dangerous."
    $ AddChatter(vig1_sc3_comment5)
    "I turn the corner."
    play music "soundtrack/decisionTime.wav" volume 1.2
    show allistar stream thinking at stream_right with dissolve
    show mac stream at stream_center_mac with dissolve
    "MAC is in the center of the hall. Allistar has one foot inside an open escape pod."
    $ AddChatter(vig1_sc3_comment6)
    "As I step into the light, Allistar sees me and reaches for MAC." 
    "I pull my blaster and point it at him, but by the time I do he has already grabbed MAC, and is holding him in the air in front of him."
    $ AddChatter(vig1_sc3_comment7)
    mS "What are you doing, Allistar?"
    show allistar stream mad
    aS "I'm getting {i}out{/i} of this crazy life, Moze."
    $ AddChatter(vig1_sc3_comment8)
    aS "You saw what happened just now!"
    aS "Ama said BC was going to hold me as an accomplice. What do you think that means they're going to do to Grand Junction?"
    aS "That's beside the ruin we left of the spaceport. Or the people who got hurt in the crossfire."
    if allistarSuspicious == True:
        $ AddChatter(vig1_sc3_suspicion_callback)
    mS "I know. None of that was right. But we didn't have a choice."
    aS "We {i}always{/i} have a choice."
    $ AddChatter(vig1_sc3_comment9)
    mS "If BC gets MAC, things are only going to get worse."
    $ AddChatter(vig1_sc3_comment10)
    aS "Things are already worse!"
    aS "They get worse everywhere we go!"
    $ AddChatter(vig1_sc3_comment11)
    aS "No, everywhere {i}you{/i} go."
    $ AddChatter(vig1_sc3_comment12)
    aS "You just go anywhere you want, do anything you want, and try to justify it by saying, \"I didn't have a choice.\""
    $ AddChatter(vig1_sc3_comment13)
    mS "I've heard enough."
    $ AddChatter(vig1_sc3_comment14)
    pause 1.0
    $ AddChatter(vig1_sc3_comment15)
    pause 1.0
    $ AddChatter(vig1_sc3_comment16)
    pause 1.0
    menu:
        mS "I've heard enough."
        "Kill Allistar":
            $ macViolence += 1
            $ pdEngagement += 3
            $ csEngagement -= 1
            $ kcEngagement += 2
            $ narrator = reg_narrator
            "Hmm, I don't know if I want to kill Allistar."
            "I go to select the stun option."
            play audio "disruptiveBang.wav" volume 6.0
            show streamview with vpunch
            "But as I hover the mouse over the choice, a loud bang comes from down the apartment above me."
            "I jolt a little bit."
            "My cursor slips."
            "The words \"Kill Allistar\" glow red in the game's UI."
            $ narrator = alt_narrator
        "Stun Allistar":
            $ pdEngagement += 3
            $ csEngagement -= 1
            $ kcEngagement += 2
            $ narrator = reg_narrator
            "I go to select the stun option."
            show streamview with vpunch
            play audio "disruptiveBang.wav" volume 6.0
            "But as I hover the mouse over the choice, a loud bang comes from down the apartment above me."
            "I jolt a little bit."
            "My cursor slips."
            "The words \"Kill Allistar\" glow red in the game's UI."
            $ narrator = alt_narrator
    play audio "lazer.wav" volume 5.0
    $ macViolence += 1
    "I fire a bolt. It lands right between Allistar's eyes."
    "He slumps to the ground."
    hide allistar with dissolve
    $ AddChatter(vig1_sc3_shot_comment1)
    pause 0.4
    $ AddChatter(vig1_sc3_shot_comment2)
    pause 0.5
    $ AddChatter(vig1_sc3_shot_comment3)
    pause 0.5
    $ narrator = reg_narrator
    $ macroChoice = True
    "I killed Allistar...What do I do?"
    $ macroChoice = True
    menu:
        "I killed Allistar...What do I do?"
        "\"That was a mistake!\"":
            $ misclick = True
            $ pdEngagement -= 1
            player "Wait, no!"
            player "I misclicked!"
            $ AddChatter(vig1_sc3_shot_mistake_comment1)
            pause 0.5
            $ AddChatter(vig1_sc3_shot_mistake_comment2)
            pause 1.0
            $ AddChatter(vig1_sc3_shot_mistake_comment3)
            pause 0.5
            "I'm on stream, I can't go back now."
        "Play it off":
            player "Consider this score settled."
            $ AddChatter(vig1_sc3_shot_cool_comment1)
            pause 0.5
            $ AddChatter(vig1_sc3_shot_cool_comment2)
            pause 0.5
            "I'm on stream, I can't go back now."
        "Shout":
            player "Woooooah!"
            player "Chat! Chat is he dead!?"
            $ AddChatter(vig1_sc3_shot_shout_comment1)
            pause 0.5
            $ AddChatter(vig1_sc3_shot_shout_comment2)
            pause 0.8
            $ AddChatter(vig1_sc3_shot_shout_comment3)
            pause 0.5
            $ omegaDead = True
            $ AddChatter(vig1_sc3_shot_shout_comment4)
            pause 0.5
    $ narrator = alt_narrator
    $ viewCheck10 = viewCount
    "MAC hits the floor and rolls to the other end of the hall behind a crate."
    hide mac with Dissolve(0.5)
    "I go over to Allistar's body. It's limp and cold."
    "But I still feel the weight of his eyes."
    "I can't tell if they're frightened or judging."
    $ AddChatter(vig1_sc3_shot_comment4)
    pause 0.5
    "I activate my com."
    mS "Teresa, Jennica, Allistar tried to activate an escape pod and take MAC away."
    pS "He did what!?"
    $ AddChatter(vig1_sc3_shot_comment5)
    pause 0.5
    enS "Why!?"
    pS "Are you okay!?"
    mS "I am, but Allistar..."
    mS "I had to kill him."
    enS "{i}WHAT{/i}!?"
    pS "Allistar's dead!?"
    mS "I had to protect my crew. He was a threat we can't afford."
    enS "I understand Cap, it's just...I can't believe it."
    pS "Is MAC okay?"
    mS "I don't know. I could use some help with the body."
    enS "Roger, I'll be right down."
    $ AddChatter(vig1_sc3_shot_comment6)
    pause 0.5
    show mac stream at stream_center_mac with Dissolve (0.5)
    #play music "soundtrack/vig1scratchtrack.wav" volume 0.7 loop fadein 1.0
    "I gently move toward MAC and crouch down in front of him."
    mS "Hey, I'm sorry about that."
    macS "Is he...is he dead?"
    "I glance back at the body."
    mS "Yes."
    if omegaDead == True:
        $ AddChatter(vig1_sc3_shot_comment7)
        pause 0.5
    macS "Why?"
    mS "He threatened you. He made his choice."
    macS "But, did he have to die?"
    $ AddChatter(vig1_sc3_shot_comment8)
    pause 0.5
    $ macroChoice = False
    menu:
        macS "But, did he have to die?"
        "I didn't have a choice.":
            $ macHope -= 1
            mS "There wasn't another way."
            mS "Not one where I could guarantee your safety."
        "It's safer this way.":
            $ macViolence += 1
            mS "It's safer than the alternative."
            mS "I have to take care of my crew."
    macS "So this ship is still safe?"
    $ AddChatter(vig1_sc3_shot_comment9)
    pause 0.5
    "I reach out my hand toward Mac."
    mS "I'll make sure it is."
    $ macroChoice = True
    hide mac with Dissolve(1.2)
    hide ship_hallway_stream with Dissolve(1.2)
    $ narrator = reg_narrator
    stop music fadeout 15.0
    "The screen fades as the episode ends."
    #show oakleyresultsv1 at topleft onlayer background with dissolve:
    #    zoom 0.82
    $ AddChatter(vig1_sc3_shot_comment10)
    pause 0.5
    player "Oookay stream, guess we're closing out on a pretty intense note today."
    $ AddChatter(vig1_sc3_shot_comment11)
    pause 0.5
    $ AddChatter(vig1_sc3_shot_comment12)
    pause 0.5
    "How do I sign off from here?"
    menu:
        "How do I sign off from here?"
        "Shout out the day one viewers.":
            $ csEngagement += 1
            player "Shout out to the viewers who were here from the beginning!"
            $ AddChatter(vig1_sc3_end_olds_comment1)
            pause 0.5
            player "Y'all saw a crazy progression today."
            player "And also thanks to 8bitBANDIT and the new folks."
            player "This chat popped off today"
            $ AddChatter(vig1_sc3_end_olds_comment2)
            pause 0.5
        "Thanks to the new folks.":
            $ pdEngagement += 1
            player "Huge thanks to 8bitBANDIT and the new folks!"
            player "Y'all got to see some crazy stuff today."
            $ AddChatter(vig1_sc3_end_olds_comment2)
            pause 0.5
            player "And to the og viewers, this was a wild ride, thanks for sticking it out with me!"
        "Next episode should be crazy.":
            $ kcEngagement += 1
            player "This next episode is shaping up to be crazy."
            $ AddChatter(vig1_sc3_end_next_comment1)
            pause 0.5
            player "Thanks to everyone in chat!"
    $ AddChatter(vig1_sc3_signoff_comment1)
    pause 0.5
    player "This was awesome and I hope to see y'all around next time!"
    $ AddChatter(vig1_sc3_signoff_comment2)
    pause 0.7
    $ viewCount -= 5
    $ AddChatter(vig1_sc3_signoff_comment3)
    pause 0.5
    $ AddChatter(vig1_sc3_signoff_comment4)
    pause 2.0
    $ viewCount -= 6
    $ AddChatter(vig1_sc3_signoff_comment5)
    pause 1.0
    $ viewCount -= 2
    $ AddChatter(vig1_sc3_signoff_comment6)
    pause 0.5
    $ viewCount -= 3
    $ AddChatter(vig1_sc3_signoff_comment7)
    $ viewCount -= 7
    pause 0.5
    $ AddChatter(vig1_sc3_signoff_comment8)
    pause 0.5
    $ viewCount -= 5
    $ AddChatter(vig1_sc3_signoff_comment9)
    pause 0.5
    $ viewCount -= 8
    $ AddChatter(vig1_sc3_signoff_comment10)
    pause 0.5
    #hide oakleyresultsv1 with dissolve
    #hide vig1_allistar_workshop
    "As the viewers leave the stream, you deactivate your webcam and sign off of Flinch."
    play music "soundtrack/postStreamGroove.wav" volume 0.7 loop fadein 2.0
    hide screen streamDetails
    hide screen streamChat
    hide streamview with Dissolve(2.0)
                  
    jump modConvo_Day1

label modConvo_Day1():
    $ chatter_list = [ ] #This should always be set to blank after a stream is finished
    $ macroChoice = True
    $ narrator = reg_narrator
    $ menu = nvl_menu
    "That was crazy."
    "The most viewers you ever had in stream before was thirteen."
    "And that felt like a ton."
    $ renpy.sound.play("audio/ReceiveText.ogg")
    "Another Clamor notification?"
    scene discord with dissolve
    "It's Jessie."
    mod_nvl "Yoooooo"
    mod_nvl "That was nuts!"
    mod_nvl "8bitBANDIT brought in so many people"
    mod_nvl "You hit like 35 viewers?"
    jump modConvo_Day1_Bandit

label modConvo_Day1_Bandit():
    menu:
        "•Who's 8bitBandit?" if askBandit == False:
            $ askBandit = True
            streamer_nvl "Who's 8bitBandit?"
            mod_nvl "She's like a mid-tier streamer, plays a lot of RPGs"
            mod_nvl "Apparently she was streaming this day one too"
            mod_nvl "Lucky for us!"
            jump modConvo_Day1_Bandit
        "•That was overwhelming.":
            $ energy -= 1
            streamer_nvl "Ngl that was so overwhelming"
            streamer_nvl "I was shaking so much"
            mod_nvl "You played it off well!"
            streamer_nvl "Actually? It wasn't like cringey or awkward?"
            mod_nvl "I mean...maybe a little XD"
            mod_nvl "But it was like the endearing kind of awkward!"
            streamer_nvl "Lmao thanks"
            mod_nvl "Gotchu b"
        "•That was so cool!":
            $ energy += 1
            streamer_nvl "That was so cool!"
            streamer_nvl "Almost triple the most viewers I ever had"
            streamer_nvl "The chat was wild, I could barely keep up"
            mod_nvl "I thought you played it off well!"
            mod_nvl "Cool, calm, and collected" 
            mod_nvl "Just like Moze lol"
            streamer_nvl "Actually? It wasn't like cringey or awkward?"
            mod_nvl "I mean...maybe a little XD"
            mod_nvl "But it was like the endearing kind of awkward!"
            streamer_nvl "Lmao thanks"
            mod_nvl "Gotchu b"
    mod_nvl "But omg, that moment when you killed Allistar"
    if misclick == True:
        mod_nvl "Even though you didn't mean to do it, it reallly got the chat going"
    else:
        mod_nvl "Blew my mind, didn't see that coming at all"
    menu:
        "•I thought about reloading":
            streamer_nvl "My first instinct was to reload a save"
            streamer_nvl "But I didn't think that would feel right"
            mod_nvl "For sure, plus the chat was eating it up"
            mod_nvl "They {i}feasted{/i} on that"
        "•I just had to roll with it":
            streamer_nvl "I didn't meant to do that!"
            streamer_nvl "I just had to roll with it"
            if misclick == True:
                mod_nvl "Considering it was an accident, you handled it well"
                mod_nvl "Idk what I would've done in that situation"
                mod_nvl "Chat seemed to love it tho"
            else:
                mod_nvl "I didn't notice"
                mod_nvl "I glanced away for a sec cause I was like \"Oh for sure going stun\""
                mod_nvl "Then I looked back and just {i}death{/i} lol"
                mod_nvl "Chat seemed to love it tho"
    mod_nvl "I guess 8bitBANDIT went the Marshal route there"
    mod_nvl "There's a blueit thread and apparently like 95\% of people stunned Allistar"
    menu:
        "•That makes sense":
            streamer_nvl "Makes a lot of sense"
            streamer_nvl "He is a fan favorite"
            mod_nvl "People love their hunky mechanics"
        "•Really?":
            streamer_nvl "Really? I know he's a fan fave"
            streamer_nvl "But like threatening to take MAC"
            streamer_nvl "I would've guessed more people would go lethal there"
    menu:
        "•I just had an idea":
            streamer_nvl "Actually, that might give me an idea"
    mod_nvl "Oh?"
    streamer_nvl "How many viewers do I need to average per week to get to Affiliate?"
    mod_nvl "10"
    mod_nvl "I remember cause you wound up at 9 last time and {i}just{/i} missed it"
    streamer_nvl "Right"
    streamer_nvl "So, what do you think about this"
    menu:
        "•What if I play Outlaw?":
            streamer_nvl "What if I play Outlaw?"
    mod_nvl "Playing against type?"
    streamer_nvl "Like, people seemed really surprised by it"
    streamer_nvl "And you said almost everyone took the Marshal route this episode"
    #streamer_nvl "So almost everyone else is going to see the story where Allistar's alive and not the one where he's dead"
    streamer_nvl "Maybe I can fill that niche"
    mod_nvl "Hmmm it's not outrageous"
    mod_nvl "Could be a good generate some buzz for Affiliate"
    mod_nvl "And I know you said this kinda felt like your last push for it"
    mod_nvl "But do you want to do that?"
    mod_nvl "You were really excited to play this game"
    menu:
        "•I don't know.":
            $ reluctance += 1
            streamer_nvl "Yeah, idk was just a thought"
            streamer_nvl "Maybe I'll sleep on it, see how I'm feeling when the next episode rolls around"
            mod_nvl "True, no reason to make up your mind right now"
        "•Why not?":
            streamer_nvl "Yea, I mean why not?"
            streamer_nvl "I can always replay the game later on my own time"
            mod_nvl "True, it's just one playthrough"
        "•It sounds fun!":
            $ enthusiasm += 1
            streamer_nvl "Actually, it sounds kinda fun"
            streamer_nvl "Especially the way the chat reacted, it could be exciting!"
            mod_nvl "For sure, if you're feeling jazzed then I say go for it!"
    streamer_nvl "I do really want to get Affiliate"
    mod_nvl "I know"
    streamer_nvl "Like even if I don't do any streaming after that, at least to get somewhere after 3 years"
    mod_nvl "Yeah"
    streamer_nvl "It would feel validating"
    mod_nvl "It's not a crazy idea"
    mod_nvl "Maybe check out the game's subblueit, see how people are talking about it"
    streamer_nvl "Ya a lil bit of research"
    mod_nvl "Write it off as \"work\" while you're procrastinating on studying for that comp sci test"
    menu:
        "•I forgot about that":
            streamer_nvl "shiiiiiit"
            streamer_nvl "I forgot about that"
            mod_nvl "That's why I'm here! To keep your ass in line"
            mod_nvl "In game and in life apparently lol"
            streamer_nvl "Shut up"
            mod_nvl "Love you too b"
        "•I'm not stressed about that":
            streamer_nvl "Ah, I'm not worried about that"
            streamer_nvl "Material's not too complex"
            mod_nvl "Ooooh look at me, my name is [player] and I'm a badass who corrects college profs"
            streamer_nvl "That only happened one time"
            mod_nvl "Ya, thus proving my point"
            streamer_nvl "Shut up"
            mod_nvl "Love you too b"
    mod_nvl "Alright, I gotta go, gonna grab some ramen with the boys"
    menu:
        "•Goodnight!":
            streamer_nvl "For sure, have a good dinner!"
            streamer_nvl "And thanks for the chat, really appreciate it"
    mod_nvl "Anytime"
    mod_nvl "Take care!"
    streamer_nvl "You too, night!"
    nvl clear #necessary when transitioning to other conversations
    jump FlinchAnalytics

label FlinchAnalytics():
    $ menu = adv_menu
    "Jessie's right, checking out the game's subblueit would be a good call."
    "But first you decide to look at your analytics overview for the stream."
    scene flinch_screen with dissolve
    #The six lines below this allow us to change who the topfan is
    #if csEngagement >= kcEngagement and csEngagement >= pdEngagement:
    #    $ topfan = "Coriolis"
    #elif kcEngagement > csEngagement and kcEngagement > pdEngagement:
    #    $ topfan = "kitcat"
    #else:
    #    $ topfan = "pickledDragons"
    #For this particular vignette though, we want it to be Coriolis
    $ topfan = "Coriolis"
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
    show screen viewershipButton
    call screen streamAnalytics
    hide screen streamAnalytics with dissolve
    jump blueitVignette1

label blueitVignette1():
    #scene Reddit with dissolve - would show reddit scene but we're not going to bother
    hide screen viewershipButton
    scene blueit_screen at truecenter with dissolve
    $ blueitPages.append(vig1_bThread1)
    $ blueitPages.append(vig1_bThread2)
    $ blueitPages.append(vig1_bThread3)
    $ blueitPages.append(vig1_bThread4)
    "I should see what people are saying about the Allistar choice and maybe see what else has the community's attention."
    jump blueitVignette1_2

label blueitVignette1_2():
    scene blueit_screen at truecenter
    call screen blueit
    return

label vig1_brother_1():
    $ menu = nvl_menu
    nvl clear
    scene bg black with dissolve
    "As you close Blueit, you remember that you're little brother asked to chat at 9:30."
    "It's 8pm so you have a bit of time."
    "You decide to make a late dinner and start catching up on the new season of Iron Goddess."
    "After finishing an episode, you wash your dishes then sit back down at your computer and shoot Elliot a message."
    scene discord with dissolve
    player_nvl "Hey El! How's it going?"
    bro_nvl "Hey [player], things are good!"
    bro_nvl "School is busy, but I'm managing. There's a concert coming up for orchestra that I'm kinda anxious about tbh"
    menu:
        "•Is it the conductor again?":
            player_nvl "Ahhh"
            player_nvl "Is Doc Frida getting on your guys' case again?"
            bro_nvl "Always"
            bro_nvl "You know how she gets before a concert"
            bro_nvl "At least she doesn't throw chalk any more"
            player_nvl "gotta love personal growth lol"
        "•You're going to be great!":
            player_nvl "You're gonna do great!"
            player_nvl "You're way better than I was at your age mr. 1st violin ;)"
            bro_nvl "Thanks, mom and dad say the same thing"
            bro_nvl "I just gotta practice to make sure, y'know"
            player_nvl "For sure, for sure"
    player_nvl "So is this what was on your mind?"
    player_nvl "Or was it something else?"
    $ playerNVLNarration = "Elliot takes a couple of minutes to respond."
    show screen NVLnarration with dissolve
    pause
    pause 1.0
    hide screen NVLnarration with dissolve
    bro_nvl "Something else"
    menu:
        "•Is everything ok?":
            player_nvl "Is everything ok?"
            player_nvl "That was a long pause to type two words"
            bro_nvl "Yeah, everything's ok"
        "•What's up?":
            player_nvl "You can tell me anything El. What's up?"
    bro_nvl "I'm just kinda embarrased"
    player_nvl "Of what?"
    bro_nvl "Well, I sort of have this crush"
    menu:
        "•YES!":
            player_nvl "YOOOOO!"
            player_nvl "What's his name?"
            player_nvl "Do you have a picture?"
            player_nvl "Nvm just gimme his insta, I'll stalk the shit out of him"
            bro_nvl "[player]!"
            player_nvl "Srysry just joshing haha"
            player_nvl "That's awesome!"
            player_nvl "Tell me about him!"
        "•That's not embarrassing":
            player_nvl "Lol El, there's nothing embarrassing about that"
            player_nvl "What's his name? What's he like"
    bro_nvl "His name is Cedric. He's a new student, family just moved here from England"
    player_nvl "Oooh exotic"
    bro_nvl "And he plays cello"
    bro_nvl "We actually sit next to each other in orchestra"
    player_nvl "Cute!"
    bro_nvl "Shut up"
    player_nvl "Love you too b"
    bro_nvl "I wanted to ask some advice"
    bro_nvl "How do you like, talk to people that you like without it feeling...weird?"
    menu:
        "•It's always weird":
            player_nvl "I mean, it's never not weird really"
            player_nvl "That's the thing"
        "•Don't overthink it":
            player_nvl "The main thing is not to overthink it"
    player_nvl "You just have to be yourself"
    bro_nvl "I know"
    bro_nvl "But being myself is being shy"
    bro_nvl "And being shy doesn't get me anywhere!"
    player_nvl "You don't have to be outgoing or do anything big"
    player_nvl "You just have to get the ball rolling and be honest"
    player_nvl "Ask him about things. What are his hobbies, what does he want to study in college"
    player_nvl "What's his theory about how Doc Frida gets that crazy hair"
    player_nvl "I know it takes some courage, but once you start you can get the chance to show him the real you (the one I know isn't that shy anyways)"
    bro_nvl "I guess that makes sense"
    menu:
        "•What do you like about him?":
            player_nvl "Well, what do you like about him?"
            bro_nvl "Well...he's hot"
            player_nvl "Doesn't hurt lol"
            bro_nvl "But he's also funny and really sweet!"
        "•Have you guys talked much?":
            player_nvl "Have you two talked much?"
            bro_nvl "Not a ton"
            bro_nvl "You know how busy orchestra is"
            bro_nvl "But he's funny and really sweet!"
    $ playerNVLNarration = "Elliot describes how he and Cedric walked home from school today and chatted the whole way."
    show screen NVLnarration with dissolve
    pause
    $ playerNVLNarration = "Elliot's nervous that he ended the conversation abruptly when they passed his home."
    pause
    $ playerNVLNarration = "He's really into this guy. More than you've heard him be before."
    pause
    hide screen NVLnarration with dissolve
    player_nvl "It's not that big a deal, El."
    player_nvl "Next time you see Cedric, just strike up a conversation"
    player_nvl "Ask him about what he likes and be yourself"
    player_nvl "Then he'll see you for the kind, warm, smart, and talented person you are"
    player_nvl "And if he doesn't, then that's his loss"
    bro_nvl "Ok, this is making me feel a bit better"
    bro_nvl "Thanks, [player]"
    player_nvl "I'm glad!"
    jump vig1_brother_2

label vig1_brother_2():
    bro_nvl "So, today was the launch of Oakley 2"
    bro_nvl "How'd the stream go???"
    bro_nvl "Sry I couldn't make it, gonna catch up on the VOD later!"
    menu:
        "•I got raided!":
            $ energy += 1
            player_nvl "It was crazy! I got raided by a bigger streamer today and had like 40 people in chat"
            bro_nvl "No way!"
            player_nvl "Yeah, it was at the end of the first episode"
            player_nvl "Before that it was just the regulars, and this new person called \"kitcat\""
            bro_nvl "Ah man, wish I could've been there live"
            bro_nvl "Sounds like a great way to start the race for Affiliate!"
        "•Stream was ok":
            $ energy -= 1
            player_nvl "Stream was ok"
            player_nvl "I only had like 4 viewers in chat for most of it"
            player_nvl "Not ideal for the first week of the Affiliate hunt"
            player_nvl "But then I got raided and had like 40 people in chat"
            bro_nvl "No way!"
            player_nvl "It got kinda overwhelming tbh"
            bro_nvl "Aw I'm sorry to hear that"
            bro_nvl "Wish I could've been there live to support you"
            bro_nvl "Sounds like a pretty good way to start the race for Affiliate though, no?"
    player_nvl "Yeah, it's definitely picked up my average viewer count"
    bro_nvl "Do you think some people will stay from the raid?"
    menu:
        "•I think so":
            player_nvl "Yeah I think so"
            player_nvl "They seemed to be into the stream"
            bro_nvl "Not surprised, you're awesome"
            player_nvl "And they didn't immediately leave when I said something cringey"
        "•I don't know":
            player_nvl "I don't know, I feel like a lot of them will still watch the other streamer play Oakley 2"
            player_nvl "But maybe one or two will stick around?"
            player_nvl "At least they didn't leave immediately when I said something cringey"
    bro_nvl "Lolol"
    bro_nvl "Of course not!"
    bro_nvl "A bit of cringe is part of the [username] stream charm!"
    player_nvl "Shut up"
    bro_nvl "Love you too b"
    bro_nvl "Alright, I think I gotta hit the hay"
    bro_nvl "Got a test tomorrow in chemistry"
    player_nvl "With Mrs. Webber?"
    bro_nvl "Yep"
    player_nvl "Oof, good luck"
    bro_nvl "Thanks, have a good night!"
    menu:
        "•Love you":
            player_nvl "Love you, El!"
    bro_nvl "Love you too, [player]!"
    stop music fadeout 4.0
    hide discord with dissolve

    "You say goodnight to Elliot then brush your teeth and get in bed."
    "After watching a couple more episodes of Iron Goddess on your phone, you start scrolling through social media."
    "A couple posts are advertising the hot new game \"Oakley 2: Settle the Score.\""
    "You turn off the phone and close your eyes, ready to fall asleep."
    "Just as your eyes start to get heavy, a memory comes to you, almost like a dream."
    "It's three years ago, you're still living back home, and you and Elliot are sitting in front of a TV."
    "You hand a game controller to Elliot."
    player "Alright El, your turn."
    elliotflashback "But we have to decide together!"
    player "It's ok, whatever you think is best: Allistar or Matticus, who's the right ally?"
    elliotflashback "Well, it has to be Allistar, he's so hot!"
    player "But you think they're all hot."
    elliotflashback "Are you gonna tell me I'm wrong?"
    player "Hahahahahaha"
    elliotflashback "Hahahahahaha"
    "You fall asleep with the sound of your brother's laughter in your ears."
    pause 3.0
    #have to restore defaults before the next vignette
    $ chatter_list = [ ]
    nvl clear
    $ menu = adv_menu
    jump vignette2Start
    return
