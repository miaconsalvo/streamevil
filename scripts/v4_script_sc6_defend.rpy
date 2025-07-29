####This script contains the code for the Polaris Defense route of Vignette 4 up until Moze makes her choice about siding with Coil and Ama

label vig4_sc6_defend_1():
    show vig1_town_stream onlayer background with dissolve
    hide targetbase_stream
    "The dull roar of battle echoes in the distance."
    "No danger on the roofs."
    "No enemies on the street."
    $ viewCount += 1
    $ AddChatter(vig4_sc6_defend_1_comment1)
    mS "All clear."
    $ AddChatter(vig4_sc6_defend_1_comment2)
    "Jennica, Teresa, and I jog down the street, sticking close to cover and keeping our eyes up for any enemies."
    "The buildings on the outskirts of Polaris are ruined, but the heat of the battle is near the plaza."
    show jennica stream neutral at stream_left with dissolve
    pS "Think they can hold the plaza?"
    mS "We won't know till we get there."
    $ vig4_sc6_defend_1_comment1.click = False
    $ AddChatter(vig4_sc6_defend_1_comment3)
    show teresa stream shock at stream_right with dissolve
    enS "Shit, patrol! Get down!"
    hide teresa with dissolve
    hide jennica with dissolve
    "The three of us dive over the rubble of a nearby building and and crouch behind the ruined stones."
    $ AddChatter(vig4_sc6_defend_1_comment4)
    "A low rumble gets closer, muddying the sound of several voices."
    "One breaks through, shouting."
    $ AddChatter(vig4_sc6_defend_1_comment5)
    enforcer "Halt! Halt I said!"
    show bc_enforcer at stream_center with dissolve
    "I peek over the ruins."
    "A squad BC enforcers round the corner and stop just a few meters away."
    #show hover tank at stream_left
    "Behind them, the source of the rumbling: an immense hover tank drives into view, its laborious engine humming."
    enforcer "Alright, you heard the orders. We're going to lock this area down and wait for the next assault."
    enforcer "Then we hit those Dragonflies with full force, break their barricade, and get the goods."
    enforcer "Remember: if you see a droid, don't shoot it. BigCorp wants it in safe custody {i}undamaged{/i}."
    enforcer "Kill everyone else."
    $ AddChatter(vig4_sc6_defend_1_comment6)
    hide bc_enforcer with dissolve
    show jennica stream angry at stream_left with dissolve
    pS "Piece of shit."
    show teresa stream neutral at stream_right with dissolve
    enS "Sounds like BC used a first assault to soften up the defenses. The next wave is the real attack."
    pS "And with that tank--"
    enS "It might be checkmate."
    "We need to stop that tank. Or..."
    $ AddChatter(vig4_sc6_defend_1_comment7)
    menu:
        "We need to stop that tank. Or..."
        "Steal the tank.":
            mS "We're going to steal that tank."
    show jennica stream shock
    show teresa stream shock
    mS "That thing will pulverize whatever defenses Polaris has. But it can also push back BigCorp if it's on our side."
    $ AddChatter(vig4_sc6_defend_1_comment8)
    enS "It's a light squad. We might be able to pull it off."
    pS "It's a risk. But it could pay off big."
    $ AddChatter(vig4_sc6_defend_1_comment9)
    show jennica stream fight
    show teresa stream fight
    mS "Get ready. I'll draw their attention, you two take the tank."
    pS "Aye aye."
    enS "Roger."
    hide jennica with dissolve
    hide teresa with dissolve
    "Staying in cover, Jennica and Teresa cycle around the rubble, getting as close to the tank as possible without revealing themselves."
    "I shift down the ruins, moving away from the tank."    
    "There are just six BC enforcers standing next to the tank."
    "It's now or never."
    menu:
        "It's now or never."
        "Fire.":
            pass
    play music "soundtrack/saveTheGalaxy.wav"
    play audio "lazer.wav"
    "Whipping around the cover, I take aim and fire two quick shots."
    if vig4_nickName_bool == True:
        $ AddChatter(vig4_sc6_defend_1_comment10)
    else:
        $ AddChatter(vig4_sc6_defend_1_comment11)
    play audio "lazer.wav"
    "Two BC enforcers drop dead as the rest scramble for cover."
    "I rush to a piece of cover opposite the tank, drawing the enforcers' attention as their fire cascades by me."
    "Out of the corner of my eye, I see Jennica and Teresa leap onto the tank."
    "The sound of charging resonates in the tank's central cannon as it turns to aim at me."
    "Then Jennica grabs the cannon's barrel and heaves it to the side, pointing it up and away."
    $ AddChatter(vig4_sc6_defend_1_comment12)
    "Teresa stabs something into the tank's top hatch. Smoke spurts out from the metal."
    "I exchange fire with the enforcers."
    "They have the numbers, but not the skill."
    "In a few seconds, I waste the three enforcers in front of me while Jennica and Terea pummel the tank crew into submission."
    $ AddChatter(vig4_sc6_defend_1_comment13)
    #"I take out two of them easily, leaving the last one diving for cover."
    #"Jennica and Teresa are busy pummeling the tank crew on the ground."
    #"There's nowhere to run. No help coming for him. He can't escape."
    #"I move out of cover and advance toward his position."
    #play audio "lazer.wav"
    hide bc_enforcer with dissolve
    #"The second his head peeks up, I blast his skull with a bolt."
    #"He drops dead."
    "A simple maneuver."
    "Holstering my blaster, I watch Jennica and Teresa climb inside the tank and survey the bodies on the ground."
    "One, two, three, four, five..."
    "Where's the sixth?"
    enforcer "Freeze!"
    show bc_enforcer at stream_center with dissolve
    "An enforcer taps my back with his gun."
    $ AddChatter(vig4_sc6_defend_1_comment14)
    enforcer "Tell your crew to stand down!"
    mS "Easy."
    enforcer "I'm giving the orders here!"
    play audio "lazer.wav"
    hide bc_enforcer with dissolve
    $ AddChatter(vig4_sc6_defend_1_comment15)
    "The enforcer goes silent as his body falls to the ground."
    vS "Never thought I'd be the one to save you, Captain."
    show vega stream neutral at stream_center with dissolve
    play music "soundtrack/polaris.wav"
    $ AddChatter(vig4_sc6_defend_1_comment16)
    "I whip around to see Vega standing just a few meters away, smoke spilling out from a rifle in her hands."
    mS "Vega!"
    $ reactTarget = "vig4_sc6_defend_findingvega"
    show screen streamerCommentary
    vS "Hello, Captain Moze."
    "Her weapon is still drawn, aiming at me."
    $ AddChatter(vig4_sc6_defend_1_comment17)
    show dflyGuard at stream_right with dissolve
    "Additional Dragonflies emerge from behind her, they aim rifles at Jennica and Teresa who stand on the tank with their arms raised in the air."
    $ AddChatter(vig4_sc6_defend_1_comment18)
    vS "What are you doing back here?"
    $ AddChatter(vig4_sc6_defend_1_comment19)
    menu:
        vS "What are you doing back here?"
        "We're here to protect MAC.":
            $ kcEngagement += 1
            mS "We're here to protect MAC."
            hide screen streamerCommentary
            $ AddChatter(vig4_sc6_defend_1_comment20)
            mS "BigCorp can't get away with him."
            mS "So we want to make sure whatever your \"Pops\" is planning happens."
        "We're here to save Polaris.":
            $ csEngagement += 1
            mS "We're here to save Polaris."
            hide screen streamerCommentary
            $ AddChatter(vig4_sc6_defend_1_comment20)
            mS "We have to show BigCorp that they can't take our freedom without a fight."
    "Vega holds for a moment."
    $ AddChatter(vig4_sc6_defend_1_comment21)
    "The sounds of battle in the distance start to quiet down."
    $ AddChatter(vig4_sc6_defend_1_comment22)
    "The first attack is coming to an end."
    $ AddChatter(vig4_sc6_defend_1_comment23)
    "Vega lowers her weapon, and the other Dragonflies do the same."
    vS "I didn't expect you to come back."
    if outlaw > marshal:
        vS "And to be honest, I don't know if I'm glad that you did."
        $ AddChatter(vig4_sc6_defend_1_comment24)
    else:
        pass
    vS "But we need you."
    hide dflyGuard with dissolve
    "She walks past me toward the tank and I follow her."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    vS "Big gun. You and your crew know how to use it?"
    pS "Please, I can drive anythin'"
    enS "It's a cannon, not rocket science."
    enS "And I understand rocket science too."
    vS "Good."
    vS "We repelled BigCorp's first attack, but we know they're not going to give up."
    "She puts a hand on the vehicle."
    vS "With this, we might stand a chance."
    vS "Right now Coil is putting the final touches on our backup plan."
    mS "Which is?"
    vS "The plaza tower can be convered into a rocket."
    $ AddChatter(vig4_sc6_defend_1_comment25)
    vS "We'll defend it long enough to make sure preparations are ready for launch."
    vS "Then everyone who can make it will enter the tower and take off."
    $ AddChatter(vig4_sc6_defend_1_comment26)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_1_comment27)
    enS "And where's MAC in all this?"
    vS "For safety, he's been taken into the tower already."
    vS "BC won't use artillery. Don't want to risk hitting MAC."
    $ AddChatter(vig4_sc6_defend_1_comment28)
    vS "If we can hold them on the ground, we can win."
    pS "So we're the bait?"
    vS "No. We're the wall."      
    $ AddChatter(vig4_sc6_defend_1_comment29)  
    "Vega turns and signals to the other Dragonflies."
    "They hesitate for a moment, then disperse, rushing down the street toward the plaza."
    vS "And you, Captain Moze, are our keystone."
    $ AddChatter(vig4_sc6_defend_1_comment30)  
    "Vega climbs up onto the tank."
    vS "I'll be your navigator. But we don't have a lot of time."
    $ AddChatter(vig4_sc6_defend_1_comment31) 
    vS "BC's sure to--"
    "As Vega speaks, a siren goes up from Polaris's plaza."
    "Drop ships swarm out of the Cruiser, angling toward the town."
    $ AddChatter(vig4_sc6_defend_1_comment32)
    vS "Shit, I thought we'd have a bit more time."
    vS "Captain, catch."
    "Vega tosses me a metal disc. I catch it cleanly out of the air."
    vS "We have a few minutes. Use them wisely."
    "She turns and lowers herself into the tank."
    hide vega with dissolve
    "Jennica and Teresa turn to me."
    pS "What?"
    enS "\"Use them wisely?\""
    macS "Hello--Vega, did you call me?"
    "That voice! It's coming from the disc!"
    $ AddChatter(vig4_sc6_defend_1_comment33)
    "I open my palm and hold it out in front of me."
    "A blue hologram projects up from the disc."
    show maccall neutral at stream_center_mac with dissolve
    play music "soundtrack/theme.wav"
    $ reactTarget = "vig4_sc6_both_maccall"
    show screen streamerCommentary
    "It's MAC."
    mS "MAC!"
    $ AddChatter(vig4_sc6_defend_1_comment34)
    "Jennica and Teresa leap down from the tank and crowd around me."
    pS "Hey, little guy!"
    enS "Good to see you, MAC."
    macS "Captain? Moze? Is it really you?"
    $ AddChatter(vig4_sc6_defend_1_comment35)
    menu:
        macS "Captain? Moze? Is it really you?"
        "We came back for you!":
            mS "Yes, MAC! We came back for you!"
        "We came to keep you safe!":
            mS "Yes, MAC! We came back to ensure you're safety."
    mS "Are you okay? Are you hurt?"
    hide screen streamerCommentary
    if rudeMACGoodbye == True:
        macS "Why do you care? Wasn't this just your mission?"
        $ AddChatter(vig4_sc6_defend_1_comment36)
        "The world goes cold."
        enS "That's not fair, MAC."
        pS "We're a family."
        macS "It's what {i}she{/i} said."
        $ AddChatter(vig4_sc6_defend_1_comment37)
        menu:
            macS "It's what {i}she{/i} said."
            "I'm sorry, MAC.":
                $ kcEngagement += 2
                $ csEngagement += 1
                mS "I'm sorry, MAC."
                mS "I didn't mean it."
                mS "I thought that would make saying goodbye easier."
                mS "But it just made it hurt more."
                mS "I regretted saying it the second the words left my mouth."
                mS "We're here for you now, whatever you need. However we can help."
                mS "Just tell us where you are, and we'll be there for you. Always."
                $ AddChatter(vig4_sc6_defend_1_comment38)
                "MAC pauses for a moment. As if pondering what I've said."
            "The job's not finished.":
                $ kcEngagement -= 1
                $ pdEngagement += 1
                mS "It is a job MAC, and it was, without a doubt, personal."
                mS "But the job's not done."
                mS "BC is here for you, and we're not going to let them take you away."
                mS "I finish what I start. And making sure you're safe, isn't finished yet."
                $ AddChatter(vig4_sc6_defend_1_comment39)
                mS "So tell us where you are. Tell us how we can help you."
                "MAC pauses for a moment. As if pondering what I've said."
    macS "I am okay."
    macS "But Coil has brought me away from the fighting."
    if macViolence >= macPeace:
        macS "And I was doing such a good job with the turret!"
        $ AddChatter(vig4_sc6_defend_1_comment40)
        menu:
            macS "And I was doing such a good job with the turret!"
            "I know, I saw!":
                mS "I know MAC, I saw it!"
                mS "You were incredible."
            "It's for the best MAC.":
                mS "It's for the best MAC."
                mS "We have to keep you safe."
                mS "But I'm proud of you for fighting so hard."
    else:
        macS "And I was helping so many people with the first aid!"
        $ AddChatter(vig4_sc6_defend_1_comment41)
        menu:
            macS "And I was helping so many people with the first aid!"
            "I know, I saw!":
                mS "I know MAC, I saw it!"
                mS "You were incredible."
            "It's for the best MAC.":
                mS "It's for the best MAC."
                mS "We have to keep you safe."
                mS "But I'm proud of you for protecting people."
    macS "Thank you, Captain!"
    mS "MAC, I'm--"
    "The sirens get louder."
    "I look up. The dropships are approaching."
    $ AddChatter(vig4_sc6_defend_1_comment42)
    macS "Captain?"
    menu:
        macS "Captain?"
        "We're going to make it through this.":
            mS "We're going to make it through this MAC."
            mS "I don't know how. But we will."
            $ AddChatter(vig4_sc6_defend_1_comment43)
            if macHope >= macPessimism:
                macS "I believe you, Moze."
                macS "I know you'll figure it out."
                $ AddChatter(vig4_sc6_defend_1_comment46)
            else:
                macS "The odds are not in our favor."
                macS "But they have not been since you found me."
                $ AddChatter(vig4_sc6_defend_1_comment46)
        "These scumbags are going to regret this.":
            mS "These BC scumbags are going to regret picking this fight."
            mS "We're going to rip them to shreds."
            $ AddChatter(vig4_sc6_defend_1_comment43)
            if macViolence >= macPeace:
                macS "Shreds!"
                $ AddChatter(vig4_sc6_defend_1_comment44)
            else:
                macS "Defeating them is our priority."
                macS "The state of their bodies afterwards less so."
                $ AddChatter(vig4_sc6_defend_1_comment45)
    macS "It is good to hear from you, Moze."
    mS "You too, MAC."
    mS "We'll talk soon."
    pS "Be good, kid!"
    enS "Take care of yourself!"
    hide maccall with dissolve
    "The hologram shivers, then fades."
    "I look up to the sky and the approaching dropships. The cruiser poised over Polaris like a hammer above an anvil."
    mS "Then I turn to my crew."
    if teresaRomance == True:
        "Teresa steps up next to me. She takes my hand in hers and squeezes."
        $ AddChatter(vig4_sc6_defend_1_comment48)
    elif jennicaRomance == True:
        "Jennica steps up next to me. She takes my hand in hers and squeezes."
        $ AddChatter(vig4_sc6_defend_1_comment47)
    else:
        pass
    "The wave of destruction rushes towards us."
    mS "We stop them here."
    hide jennica with dissolve
    hide teresa with dissolve
    jump vig4_sc6_defend_2

label vig4_sc6_defend_2():
    show vega stream neutral at stream_right5 with dissolve
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    "I climb into the tank last."
    "Jennica is already sitting in a chair near the front while Vega sits to one side, peering through a scope."
    "Teresa situates herself off to one side, monitoring several screens."
    "I settle into a chair in the center."
    mS "How're we looking, Jenn?"
    pS "Fine, Cap, doesn't look too complex. We just gotta work as a team."
    $ AddChatter(vig4_sc6_defend_2_comment1)
    pS "I'll take maneuverin'. Teresa, take care of our shields and engine power."
    enS "Makes sense."
    pS "Vega, if you're on navigation, use that scope and give me directions."
    vS "Gotcha."
    pS "Cap, you stay in the center, be our spotter and operate the main cannon."
    mS "Roger, let's roll out."
    $ AddChatter(vig4_sc6_defend_2_comment2)
    pS "Aye aye."
    "The tank accelerates as Jennica shifts the sticks in front of her forward."
    "I turn to Vega."
    mS "Welcome to the Oakley, Vega."
    if outlaw > marshal:
        vS "Don't worry, it's just temporary."
        $ AddChatter(vig4_sc6_defend_2_comment3)
    else:
        vS "It's a pleasure!"
        $ AddChatter(vig4_sc6_defend_2_comment4)
    "As Vega directs us toward the plaza, we pass by ruined, burning buildings."
    "Even as its people defend it, Polaris lies in ruins."
    #show plaza onlayer background with dissolve
    #hide previous scene
    "We arrive at the plaza's perimeter, just in front of the central barriade." 
    "Dragonflies stand atop the barricade, cheering at our arrival."
    vS "They know we might have a chance now."
    mS "Might."
    pS "Eyes up, we've got dropships!"
    "A clatter of blaster fire rattles against the tank's shell as a BC dropship flies over head."
    $ AddChatter(vig4_sc6_defend_2_comment5)
    enS "Shields holding firm."
    vS "Guess they figured out we aren't friendly."
    "Looking through a monitor, I see dropships landing at the outskirts of Polaris and dropping off battalions of BC enforcers."
    "Dragonflies move across the ruined rooftops, and rush past the tank on the ground to take cover in the ruins of the street."
    $ AddChatter(vig4_sc6_defend_2_comment6)
    "They bring the fight to the approaching army, firing at the advancing BC army."
    "The true battle for Polaris begins."
    play music "soundtrack/saveTheGalaxy.wav"
    "A dropship careens down toward the central street, as if to fly directly overhead."
    mS "Vega, use the machine guns and hit the enforcers with suppressing fire."
    $ AddChatter(vig4_sc6_defend_2_comment7)
    "The rapid fire of the machine guns sail out into the night."
    "I initiate the firing procedure and grip the cannon's controls."
    "The tank vibrates as the cannon charges. The whole vehicle thrums with energy."
    "The vehicle jerks back as the cannon fires."
    "A stream of blue light blasts out from the cannon."
    "It collides with the dropship, creating a fireball in the sky."
    $ AddChatter(vig4_sc6_defend_2_comment8)
    "As the pieces crash into Polaris, additional flames catch fire on the buildings."
    $ AddChatter(vig4_sc6_defend_2_comment9)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_2_comment10)
    show bc_enforcer at stream_left5 with dissolve
    "A horde of BC enforcers stream down the road toward us, a hail of blaster bolts clatter on our hull."
    enS "Shields slowly dropping but we're still at 90\%."
    vS "BC scum!"
    "Vega turns the machine gun on the battalions and lets loose, bolts of blue light ripping into the frontlines."
    $ AddChatter(vig4_sc6_defend_2_comment11)
    "I charge the cannon again and unleash its blast at another dropship." 
    "Its shell also slams into the ground, this time close to us."
    show vig1_town_stream with hpunch
    "The explosion shakes the tank."
    $ AddChatter(vig4_sc6_defend_2_comment12)
    "We keep the stream of fire up while Jennica tries to keep us a moving target."
    "But it's a losing battle."
    "Even with the tank, the wave of BC troops doesn't stop."
    $ AddChatter(vig4_sc6_defend_2_comment13)
    "Up above, a steady stream of dropships continues to descend from the cruiser."
    hide bc_enforcer with dissolve
    "The Dragonflies ahead of us start to be pushed back."
    $ AddChatter(vig4_sc6_defend_2_comment14)
    "A group at the head of the pack on the ground are pinned by blaster fire."
    "A call comes in over Vega's communicator."
    $ AddChatter(vig4_sc6_defend_2_comment15)
    dflyGuard "Vega, come in! We're pinned down, need assista--"
    play audio "cutCall.wav"
    $ AddChatter(vig4_sc6_defend_2_comment16)
    "The audio gets cut as an explosion throws dirt over the frontline."
    vS "Shit! Moze, we need to cover their retreat!"
    "The dirt and smoke clears over the frontline squad."
    "Suddenly, I recognize them." 
    show dflyGuard at stream_left5 with dissolve
    "They're the squad that held Teresa and Jennica captive during the festival."
    $ AddChatter(vig4_sc6_defend_2_comment17)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_2_comment18)
    vS "Moze! We have to help them!"
    $ AddChatter(vig4_sc6_defend_2_comment19)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_2_comment20)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_2_comment21)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_2_comment22)
    menu:
        vS "Moze! We have to help them!"
        "Abandon the frontline. Pull back to the barricade.":
            $ pdEngagement += 2
            $ kcEngagement += 1
            $ csEngagement -=2
            $ outlaw += 1
            jump vig4_sc6_defend_3_barricade
        "Support the frontline. Leave the barricade":
            $ pdEngagement -= 1
            $ kcEngagement -= 1
            $ csEngagement += 2
            $ marshal += 1
            jump vig4_sc6_defend_3_frontline

##*Should we have some reactions here in these sections?

label vig4_sc6_defend_3_barricade():
    hide dflyGuard with dissolve
    mS "Vega, we can't afford to. If we leave this position, the barricade falls and we lose everything."
    $ AddChatter(vig4_sc6_defend_3_barricade_comment1)
    "The BigCorp assault batters against our defenses."
    $ AddChatter(vig4_sc6_defend_3_barricade_comment2)
    enS "Shields are at 75\%. We move forward, we risk putting ourselves in critical danger."            
    vS "But they're my friends!"
    $ AddChatter(vig4_sc6_defend_3_barricade_comment3)
    mS "I'm sorry, Vega. We can't risk it. Order all your forces to retreat."
    "Vega holds for one moment, staring out the tank windows at the onslaught of the BC army."
    "Then picks up a communicator. Her voice projects out from the tank."
    $ AddChatter(vig4_sc6_defend_3_barricade_comment4)
    vS "All forces, retreat! Back to the barricade!"
    mS "Jenn, hold us here to cover the retreat."
    $ AddChatter(vig4_sc6_defend_3_frontline_comment4)
    pS "Roger!"
    "Vega and I keep firing into the swarm of BC soldiers."
    $ AddChatter(vig4_sc6_defend_3_frontline_comment5)
    "The Dragonflies surrounding the tank turn and rush back toward the barricade."
    $ AddChatter(vig4_sc6_defend_3_frontline_comment6)
    "The forces on the rooftops do the same, but many of them are cut down as soon as they retreat."
    "Some of them make it back."
    $ AddChatter(vig4_sc6_defend_3_barricade_comment5)
    show dflyGuard at stream_left5 with dissolve
    "The squads at the frontline have no such luxury."
    "Anyone who turns to run is immediately shot in the back."
    "The remainder stay at the frontline, firing desperately into the opposing army."
    $ AddChatter(vig4_sc6_defend_3_barricade_comment6)
    "One by one, they fall to the ground, until there's one soldier left standing."
    $ AddChatter(vig4_sc6_defend_3_barricade_comment7)
    "As he starts to turn to try to retreat, something lands at his feet."
    $ AddChatter(vig4_sc6_defend_3_barricade_comment8)
    "He has one brief moment to look up in our direction."
    hide dflyGuard with Dissolve(0.5)
    #play audio explosion
    "Fire engulfs him. His body flails to the ground, writhing."
    $ AddChatter(vig4_sc6_defend_3_barricade_comment9)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_3_barricade_comment10)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_3_barricade_comment11)
    menu:
        "How does it feel?"
        "Got what they deserved.":
            $ pdEngagement += 1
            "They got what they deserved."
            $ AddChatter(vig4_sc6_defend_3_barricade_comment5)
        "I couldn't risk the barricade.":
            $ kcEngagement += 1
            "The barricade is too important. I couldn't risk it on them."
            $ AddChatter(vig4_sc6_defend_3_barricade_comment6)
    show vig1_town_stream with vpunch
    "A grenade explodes at our side."
    enS "Shields are at 60\%. We can maintain this position for a bit longer."
    vS "Scumbags!"
    "Vega screams as she lays on the trigger for the machine gun."
    "Bolts rip into the BC army, tearing up the frontline."
    "The cannon discharges, distintegrating a line of BC enforcers in an instant."
    "The Dragonflies have all left the frontlines. They fire back at the BC army from the barricade."
    enS "Shields holding at 45\%."
    mS "Alright, time to reposition, find a way to recharge those shields."
    show vig1_town_stream with hpunch
    "The tank jerks to the side as an explosion detonates on our side."
    $ AddChatter(vig4_sc6_defend_3_frontline_comment12)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_3_frontline_comment14)
    jump vig4_sc6_defend_4

label vig4_sc6_defend_3_frontline():
    mS "Jenn, push forward! We have to support the frontline so they have time to retreat!"
    $ AddChatter(vig4_sc6_defend_3_frontline_comment1)
    pS "Roger!"
    "Jenn pushes the throttle ahead and we careen forward, rushing past Dragonflies as they dive out of the way."
    $ AddChatter(vig4_sc6_defend_3_frontline_comment2)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_3_frontline_comment3)
    vS "Thank you, Moze."
    enS "Shields at 75\%. We don't have a lot of room for error here!"
    vS "Hit them harder than they can hit us!"
    $ AddChatter(vig4_sc6_defend_3_frontline_comment4)
    "Vega lays on the machine guns as I fire another blast from the cannon."
    $ AddChatter(vig4_sc6_defend_3_frontline_comment5)
    "Jennica pulls the tank into a stop just at the front edge of the Dragonfly forces."
    "The hail of fire is more intense here. The rattle of bolts is constant."
    enS "Shields at 65\% and dropping quickly!"
    $ AddChatter(vig4_sc6_defend_3_frontline_comment6)
    mS "Vega, if they don't move now, we're all dead!"
    vS "I know!"
    "Vega lifts a communicator from her side."
    $ AddChatter(vig4_sc6_defend_3_frontline_comment7)
    vS "Get out of there, now! We'll cover you!"
    "The Dragonfly squad turns their back on the BC army and starts rushing back toward the barricade."
    "One of them, their leader, glances at us. Even though he can't see me, it's as if we're making eye contact."
    "He nods quickly."
    $ AddChatter(vig4_sc6_defend_3_frontline_comment8)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_3_frontline_comment9)
    hide dflyGuard with dissolve
    menu:
        "How does it feel?"
        "They didn't deserve to die.":
            $ csEngagement += 1
            "They were just doing their job. That doesn't mean they deserve to die."
            $ AddChatter(vig4_sc6_defend_3_frontline_comment10)
        "Lucky bastard.":
            $ kcEngagement += 1
            $ pdEngagement += 1
            "They're lucky I didn't leave them to die."
            $ AddChatter(vig4_sc6_defend_3_frontline_comment11)
    show vig1_town_stream with vpunch
    "A grenade explodes at our side."
    pS "Damn, maneuverability is getting a little wonky. How much longer do we have to stay out here?"
    vS "Just a little while to cover the retreat."
    enS "Shields are down to 45\%. We're sitting ducks!"
    mS "Keep firing!"
    "The cannon discharges into the encroaching swarm, disintegrating a line of soldiers in an instant."
    "Vega's machine guns keep the closest enemies at bay."
    "But then the machine guns stop firing."
    $ AddChatter(vig4_sc6_defend_3_frontline_comment12)
    vS "Crap, they're overheated!"
    pS "So we only have the cannon?"
    enS "Shields at 25\%!"
    $ AddChatter(vig4_sc6_defend_3_frontline_comment13)
    mS "It'll have to do, Jenn, pull us back to the barricade!"
    "I fire one last blast from the cannon." 
    $ AddChatter(vig4_sc6_defend_3_frontline_comment14)
    "It rips through a drop ship that collides into the street, taking more soldiers out with it."
    pS "Aye!"
    "The tank rumbles as Jennica pulls it in reverse, slamming it back toward the barricade as fast as it can go."
    "We peel into a stop, just a few meters from the barricade."
    mS "Teresa, find a way to recharge those shields. Jenn I nee--"
    jump vig4_sc6_defend_4

label vig4_sc6_defend_4():
    vS "Shit, contact on the rooftop!"
    show bc_enforcer at stream_left5
    "I glance through a monitor just in time to see it: a BC enforcer with a rocket launcher."
    $ AddChatter(vig4_sc6_defend_4_comment1)
    "I reach for the cannon, but it's too late."
    "Smoke streaks through the air."
    $ AddChatter(vig4_sc6_defend_4_comment2)
    show vig1_town_stream with hpunch
    "The rocket slams into the tank's side."
    "Alarms start blaring, red lights flashing all around the tank's interior."
    enS "Shields at 5\%! Another hit like that and we're dead!"
    "The enforcer is loading another rocket."
    mS "Everyone, out of the tank, now!"
    hide vega with dissolve
    "Teresa throws open the top hatch and helps Vega scramble out first."
    $ AddChatter(vig4_sc6_defend_4_comment3)
    hide jennica with dissolve
    hide teresa with dissolve
    "Jennica and Teresa follow quickly."
    "The enforcer finishes loading."
    $ AddChatter(vig4_sc6_defend_4_comment4)
    "I quickly lift myself out of the hatch and glance to my side."
    "The launcher is aimed directly at the tank."
    "I leap to the ground and rush toward the barricade."
    hide bc_enforcer with dissolve
    "Behind me, I feel the heat against my back as the rocket detonates against the tank."
    "A shockwave ripples out, sending me flying through the air and rolling into the dirt."
    "Picking myself up, I turn around to see the hull of the tank engulfed in flames."
    $ AddChatter(vig4_sc6_defend_4_comment5)
    "The BC army marches up from the distance."
    vS "Come on!"
    show vega stream neutral at stream_center with dissolve
    "Vega grabs me by the hand and pulls me up as we sprint the final few feet to the barricade."
    "We clamber over and slide down the other end as people climb to shoot back at the approaching enemies."
    $ AddChatter(vig4_sc6_defend_4_comment6)
    hide vega with dissolve
    "Taking a couple steps back from the barricade, I drop to one knee, glancing around me."
    $ vig4_sc6_defend_4_comment5.click = False
    "The town is engulfed in glame."
    "Ash and embers fall all around me."
    "Heat radiates on my skin."
    jump vig4_sc6_defend_5

label vig4_sc6_defend_5():
    vS "Moze!"
    show vega stream neutral at stream_left with dissolve
    vS "What do we do?"
    $ AddChatter(vig4_sc6_defend_5_comment1)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_5_comment2)
    "Just then, the thrum of a ship screeches over head."
    "I look up in time to see a dropship pull into a hover above us."
    show bc_enforcer at stream_center with Dissolve (0.5)
    "Two BigCorp enforcers leap out, one of them tackling me to the ground."
    $ AddChatter(vig4_sc6_defend_5_comment3)
    hide vega with dissolve
    "Above me, an explosion."
    $ AddChatter(vig4_sc6_defend_5_comment4)
    "Sheets of metal collide all around me as the fireball heats up my face."
    "I try to stand up, but the enforcer grapples me."
    "He grabs me by the throat and lifts me into the air."
    "I flail at his arms, scratch at his face, but he's massive and I can't get purchase."
    $ AddChatter(vig4_sc6_defend_5_comment5)
    hide vig1_town_stream with Dissolve(2.0)
    "The periphery of my vision starts to go dark."
    $ AddChatter(vig4_sc6_defend_5_comment6)
    hide bc_enforcer with dissolve
    "The world disappears."
    pause 1.0
    mS "{i}gasp{/i}"
    show vig1_town_stream with Dissolve(0.5)
    "Then I fall to the floor as something thuds next to me."
    "Staggering to my knees, I see that the enforcer has a smoking hole in the back of his head."
    show vega stream neutral at stream_left with Dissolve(0.5)
    show bc_enforcer at stream_center with Dissolve(0.5)
    "Behind him, Vega grapples with the other enforcer."
    "I draw the pistol from the dead body's belt and fire."
    "The bolt hits the enforcer in the chest, giving Vega the chance to draw a knife from her belt and stab it into his neck."
    hide bc_enforcer with dissolve
    "She falls to her hands and knees, gasping for air."
    "I look around. The rest of the Dragonflies are focused on defending the barricades."
    "No one's even looking at us."
    $ AddChatter(vig4_sc6_defend_5_comment7)
    "Who shot my assailant?"
    "Then I see it."
    $ AddChatter(vig4_sc6_defend_5_comment8)
    "A shadow drops from a building in the plaza and enters the tower."
    $ AddChatter(vig4_sc6_defend_5_comment9)
    "I stagger to my feet."
    mS "Vega, I have to go."
    show vega at stream_center with dissolve
    vS "What? What do you mean \"go?\""
    vS "We have to fight!"
    pS "Moze!"
    show teresa stream neutral at stream_right with dissolve
    show jennica stream neutral at stream_left with dissolve
    enS "Are you okay?"
    "Jennica and Teresa rush to my side, helping me steady myself."
    mS "MAC. She's trying to take MAC."
    vS "You saw someone go in there?"
    "I nod."
    vS "Who?"
    menu:
        vS "Who?"
        "My business.":
            mS "It's my business. Mine alone."
            "Jennica and Teresa look at each other."
            pS "Sorry, Vega. But this is personal."
            $ AddChatter(vig4_sc6_defend_5_comment10)
        "A hunter.":
            mS "A hunter."
            "Jennica and Teresa look at each other."
            pS "Sorry, Vega. But this is personal."
            $ AddChatter(vig4_sc6_defend_5_comment10)
        "Ama Deadeye Reyes.":
            mS "Ama Deadeye Reyes."
            $ AddChatter(vig4_sc6_defend_5_comment10)
            "Vega's eyes go wide."
            vS "No! But Coil's in the tower!"
    mS "I'll go. I can handle this."
    $ AddChatter(vig4_sc6_defend_5_comment11)
    pause 0.5
    $ AddChatter(vig4_sc6_defend_5_comment12)
    mS "You have to stay here. You have to stop them."
    $ AddChatter(vig4_sc6_defend_5_comment13)
    "We turn to look at the flames that lick at Polaris."
    $ AddChatter(vig4_sc6_defend_5_comment14)
    mS "Somehow."
    if vig2_outlawEpilogue == True:
        $ pdEngagement += 3
        $ kcEngagement += 2
        $ csEngagement += 1
        $ vig4_reggieReturn = True
        unknown "Ugh, and here I thought you all would have toughened up in the last two weeks."
        "A familiar voice...but from where?"
        $ AddChatter(vig4_sc6_defend_5_comment15)
        enS "Captain, we're being hailed by a new signal, I don't--"
        hide vega with dissolve
        show vig1_town_stream with hpunch
        "A ship suddenly streaks overhead, careening toward the BC dropships."
        $ AddChatter(vig4_sc6_defend_5_comment16)
        "Its wings open into attack formation as green bolts of light rip into a dropship, sending it to the ground."
        "Three more fighters fly by immediately after. Then another. Then another."
        $ AddChatter(vig4_sc6_defend_5_comment17)
        "A fleet of attack ships."
        pS "Who the--that's one hell of a pilot?"
        show reginald at stream_center with dissolve
        $ AddChatter(vig4_sc6_defend_5_comment18)
        goon "I really don't get paid enough for this shit."
        show jennica stream shock at stream_left
        pS "Reginald!?"
        $ AddChatter(vig4_sc6_defend_5_comment19)
        goon "Matticus sends his regards."
        goon "Said he had a debt that needed paying off."
        $ AddChatter(vig4_sc6_defend_5_comment20)
        show jennica stream neutral
        "The swarm of attack ships engage the BC dropships, destroying them."
        $ AddChatter(vig4_sc6_defend_5_comment21)
        goon "So take care of whatever you got to do down there. We'll handle the air shit."
        $ AddChatter(vig4_sc6_defend_5_comment22)
        $ vig4_sc6_defend_5_comment19.click = False
        menu:
            goon "So take care of whatever you got to do on the ground. We'll handle the air shit."
            "Thank you.":
                mS "Reginald...thank you."
                goon "Now don't go getting soft on me."
                goon "You just do your job and I'll do mine."
                goon "Even though it's a massive pain."
                $ AddChatter(vig4_sc6_defend_5_comment23)
                mS "Copy that."
            "Affirmative.":
                mS "Copy that."
        "A handful of attack ships break formation, streaking fire along Polaris's ground and ripping into the BC troops."
        "Exposed to fire by the air, the BC forces have to regroup while the Dragonflies cheer and go on the offensive."
        "But the Cruiser remains resolute in the air. Dozens of more ships emerge from its hangars, this time attack ships and bombers."
        "The battle has just begun."
        hide reginald with dissolve
    else: #could also be an elif for Reynar's Approval. Could also pass this "else" so that Zan always triggers. But that feels like too much.
        $ pdEngagement += 1
        $ kcEngagement += 3
        $ csEngagement += 2 
        unknown "MOXIE!"
        pS "Cap, we're pickin' up a new signal!"
        hide vega with dissolve
        #if vig2_outlawEpilogue == True:
        #    pS "Cap, we're pickin' up another signal!"
        show teresa stream shock
        $ AddChatter(vig4_sc6_zan_comment1)
        enS "Wait, that has to be--"
        show zan stream at stream_right5 with dissolve
        zan "Have no fear! The great Dr. Zan is here!"
        $ AddChatter(vig4_sc6_zan_comment2)
        "A half dozen sounds like thunderclaps boom out as six ships exit hyperspace all around Polaris."
        zan "For my loyal fans!"
        $ AddChatter(vig4_sc6_zan_comment3)
        "Immense guns emerge from the ships, opening fire on BC's forces."
        enS "Zan!? What are you doing here?"
        if vig3_daisyApproval == True:
            showgirl "This beats the hell out of working the Nova Casino beat!"
            show showgirl stream at stream_left5 with dissolve
            showgirl "Reynar heard some trouble was brewing roundabout these coordinates."
            $ AddChatter(vig4_sc6_zan_comment4)
            showgirl "Thought y'all could use some help!"
            mS "Daisy? But I thought--"
            showgirl "One second, dear. Zan, the photon pulse is primed!"
        else:
            show houndleader at stream_left5 with dissolve
            houndleader "Reynar heard some trouble was brewing in this area."
            $ AddChatter(vig4_sc6_zan_comment5)
            houndleader "Guess he figured you could use some help."
            mS "The Hounds? But I thought--"
            #$ AddChatter(vig4_sc6_zan_comment11)
            houndleader "One second, sweetcheeks. Zan, the photon pulse is primed."
        show teresa stream neutral
        zan "Fantastic! Show them the muscles of Akar!"
        $ AddChatter(vig4_sc6_zan_comment6)
        "The cannon on the lead ship in the formation starts to glow."
        "Then a wave of green light ripples away from the ship like a shockwave."
        "Every BC ship touched by the pulse drops out of the sky."
        $ AddChatter(vig4_sc6_zan_comment7)
        hide houndleader with dissolve
        hide showgirl with dissolve
        "Exposed to fire by the air, the BC forces have to regroup while the Dragonflies cheer and go on the offensive."
        "But the Cruiser remains resolute in the air. Dozens of more ships emerge from its hangars, this time attack ships and bombers."
        "The battle has just begun."
        #if vig2_outlawEpilogue == True:
        #    "Reginald's fighters careen up into the sky, angling to do battle with BC's forces."
        zan "You go, do what you must."
        zan "We will handle corporate stooges."
        menu:
            zan "We will handle corporate stooges."
            "Thank you.":
                mS "Thank you, Zan."
                zan "It is no problem."
                zan "Now, show them your mama's back!"
                mS "My wha--."
                pS "Our Moxie."
                zan "Moxie!"
                $ AddChatter(vig4_sc6_zan_comment8)
                pause 0.5
                $ AddChatter(vig4_sc6_zan_comment9)
                mS "Ah, right. Copy that!"
                $ AddChatter(vig4_sc6_zan_comment10)
            "Affirmative.":
                mS "Copy that!"
                $ AddChatter(vig4_sc6_zan_comment10)
        hide zan with dissolve
    show vega stream neutral at stream_center with dissolve
    #else:
    #    "Vega pauses for a moment."
    #    vS "Go, Moze."
    #    vS "We'll do what we have to do out here."
    #    enS "We will too."
    vS "Captain, you should get a move on."
    vS "The Dragonflies will hold the ground, make sure you don't have anymore suprises."
    enS "We will too."
    $ AddChatter(vig4_sc6_defend_5_comment24)
    enS "If BC takes the plaza it won't matter what you do up there, we'll all be toast."
    $ AddChatter(vig4_sc6_defend_5_comment25)
    pS "You go get the kid. We'll keep a path clear down here."
    $ AddChatter(vig4_sc6_defend_5_comment26)
    menu:
        pS "You go get the kid. We'll keep a path clear down here."
        "I'm not leaving you.":
            mS "No way, you two are coming with me! I'm not leaving you!"
            enS "You're not leaving anything."
            pS "We're just splittin' up to make the mission succeed."
            jenter "We've got this."
            if jennicaRomance == True:
                "Jennica steps up close to me. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                $ AddChatter(vig4_sc6_defend_5_comment28)
                pS "Go do what you do best, Moze."
            elif teresaRomance == True:
                "Teresa steps up close to me. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                $ AddChatter(vig4_sc6_defend_5_comment27)
                show teresa stream happy
                enS "Go do what you do best, Moze."                
            else:
                pass
            mS "I want a clean escape route when I come down with MAC."
            pS "You betcha."
            enS "Affirmative."
        "Thank you.":
            mS "Jenn, Resa, I--"
            if jennicaRomance == True:
                "Jennica steps up close to me. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                $ AddChatter(vig4_sc6_defend_5_comment28)
                pS "Go do what you do best, Moze."
            elif teresaRomance == True:
                "Teresa steps up close to me. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                $ AddChatter(vig4_sc6_defend_5_comment27)
                show teresa stream happy
                enS "Go do what you do best, Moze."                
            else:
                pass
            mS "Thank you. And be careful. I want a clean escape route when I come down with MAC."
            pS "You betcha."
            enS "Affirmative."
    "I turn my back on the three women and face the tower, rushing toward its immense doors."
    hide vega with dissolve
    hide teresa with dissolve
    hide jennica with dissolve
    jump vig4_sc7_1_defend

label vig4_sc7_1_defend():
    hide vig1_town_stream with dissolve
    "As soon as the doors close behind me, the sounds of battle become muffled."
    "The tower is utterly silent."
    $ AddChatter(vig4_sc7_1_defend_comment1)
    "A series of stairs winds up toward the high ceiling."
    $ AddChatter(vig4_sc7_1_defend_comment2)
    "Each step feels like an eternity."
    "A chance to think about the steps that brought me here."
    "Allistar."
    $ AddChatter(vig4_sc7_1_defend_comment3)
    "Matticus."
    if vig2_marshalEpilogue == True:
        $ AddChatter(vig4_sc7_1_defend_comment5)
    else:
        $ AddChatter(vig4_sc7_1_defend_comment4)
    "Rec."
    $ AddChatter(vig4_sc7_1_defend_comment6)
    "Ama."
    "Jennica."
    "Teresa."
    "MAC."
    "Every person. Every choice."
    "Here I am."
    $ AddChatter(vig4_sc7_1_defend_comment7)
    "The stairs flatten out."
    "There's a wide room in front of me, and two voices shouting within."
    amaS "Just tell me where the robot is, or I'll kill you like I did your friends outside."
    $ AddChatter(vig4_sc7_1_defend_comment8)
    "I step across the threshold into a wide room."
    show vig2_datacenter_stream onlayer background with dissolve
    show coil stream neutral at stream_right with dissolve
    show ama stream neutral at stream_left with dissolve
    hide vig1_town_stream
    "Coil stands in the center, in front of a massive computer console."
    $ AddChatter(vig4_sc7_1_defend_comment9)
    "Ama holds her rifle, aiming it at Coil's back."
    $ AddChatter(vig4_sc7_1_defend_comment10)
    cS "I will never tell you, and you will never find him."
    amaS "Sounds like you're just stalling."
    cS "Precisely."
    "Coil turns around and faces me."
    cS "Well, Moze, I'm glad you made it."
    "His face looks haggard, his eyes bloodshot."
    $ reactTarget = "vig4_sc6_defend_finding_coil"
    show screen streamerCommentary
    $ AddChatter(vig4_sc7_1_defend_comment11)
    "Ama whips around, aiming her rifle at me."
    $ AddChatter(vig4_sc7_1_defend_comment12)
    amaS "Good to see you, kid."
    amaS "Was wondering when you would finish playing around outside and join us."
    amaS "Took you longer than expected."
    menu:
        amaS "Took you longer than expected."
        "Thanks for saving me.":
            mS "I appreciate you saving me earlier."
            mS "Will make this even sweeter."      
        "Being a decent person takes time.":
            mS "Being a decent person can take a bit of time."
            mS "Not that you'd know anything about that."
    $ AddChatter(vig4_sc7_1_defend_comment13)
    amaS "Watch your tongue, kid."   
    amaS "I'm calling the shots here." 
    cS "So you think."
    "Ama trains her gaze back on Coil as he steps away from the device and in front of the two of us."  
    cS "Tell me truthfully, Moze. What was your plan in coming here?"
    hide screen streamerCommentary
    menu:
        cS "Tell me truthfully, Moze. What was your plan in coming here?"
        "I came for MAC.":
            $ kcEngagement += 1
            mS "I came for MAC."
            mS "I'm not leaving without him."
            $ AddChatter(vig4_sc7_1_defend_comment14)
            "Coil sighs."
            cS "I assumed that was the case."
            cS "I must say I am disappointed."
            $ AddChatter(vig4_sc7_1_defend_comment15)
            if vig4_defendPolaris == True:
                cS "Although, without you, we probably would already be overrun."
            cS "MAC is gone."
            amaS "Bullshit."
            amaS "If that were true you wouldn't still be here."
            cS "How perceptive. And yet you still have no idea what you're doing."
            $ AddChatter(vig4_sc7_1_defend_comment16)
            cS "Flailing around in the darkness with no purpose."
            $ AddChatter(vig4_sc7_1_defend_comment17)
        "I came to help.":
            $ csEngagement += 1
            mS "I came to help fight off BigCorp."
            cS "And you have done an admirable job." 
            cS "Without you, we probably would already be overrun."
    amaS "I've heard enough!"
    "Ama moves to fire her rifle."
    $ AddChatter(vig4_sc7_1_defend_comment18)
    menu:
        "Ama moves to fire her rifle."
        "Ama, no!":
            mS "Ama no!"
            "Too late."
            "Ama fires."
            play audio "lazer.wav"
            "The bolt diffuses harmlessly into his shield."
        "Say nothing.":
            "The rifle is ready."
            "Ama fires."
            play audio "lazer.wav"
            "The bolt diffuses harmlessly into his shield."
    $ AddChatter(vig4_sc7_1_defend_comment19)
    "Eyes wide, Ama fires again. And again."
    "The bolts continue to be absored."
    $ AddChatter(vig4_sc7_1_defend_comment20)
    jump vig4_sc7_2