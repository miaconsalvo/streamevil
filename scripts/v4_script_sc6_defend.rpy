####This script contains the code for the Polaris Defense route of Vignette 4 up until Moze makes her choice about siding with Coil and Ama

label vig4_sc6_defend_1():
    show vig1_town_stream onlayer background with dissolve
    hide targetbase_stream
    "The dull roar of battle echoes in the distance."
    "No danger on the roofs."
    "No enemies on the street."
    mS "Let's move."
    "Jennica, Teresa, and I jog down the street, sticking close to cover and keeping our eyes up for any enemies."
    "The buildings on the outskirts of Polaris are ruined, but the heat of the battle is near the plaza."
    "In the distance, the sounds of battle start to quiet down."
    show jennica stream neutral at stream_left with dissolve
    pS "Think they can hold the plaza?"
    mS "We won't know till we get there."
    show teresa stream shock at stream_right with dissolve
    enS "Shit, patrol! Get down!"
    hide teresa with dissolve
    hide jennica with dissolve
    "The three of us dive over the rubble of a nearby building and and crouch behind the ruined stones."
    "A low rumble gets closer, muddying the sound of several voices."
    "One breaks through, shouting."
    enforcer "Halt! Halt I said!"
    show bc_enforcer at stream_center with dissolve
    "I peek over the ruins."
    "A squad BC enforcers round the corner and stop just a few meters away."
    "Behind them, the source of the rumbling: an immense hover tank drives into view, its laborious engine humming."
    enforcer "Alright, you heard the orders. We're going to lock this area down and wait for the next assault."
    enforcer "Then we hit those Dragonflies with full force, break their barricade, and get the goods."
    enforcer "Remember: if you see a droid, don't shoot it. BigCorp wants it in safe custody {i}undamaged{/i}."
    enforcer "Kill everyone else."
    hide bc_enforcer with dissolve
    show jennica stream angry at stream_left with dissolve
    pS "Piece of shit."
    show teresa stream neutral at stream_right with dissolve
    enS "Sounds like BC used a first assault to soften up the defenses. The next wave is the real attack."
    pS "And with that tank--"
    enS "It might be checkmate."
    "We need to stop that tank. Or..."
    menu:
        "We need to stop that tank. Or..."
        "Steal the tank.":
            mS "We're going to steal that tank."
    show jennica stream shock
    show teresa stream shock
    mS "That thing will pulverize whatever defenses Polaris has. But it can also push back BigCorp if it's on our side."
    enS "It's a light squad. We might be able to pull it off."
    pS "It's a risk. But it could pay off big."
    show jennica stream neutral
    show teresa stream neutral
    mS "Get ready. I'll draw their attention, you two take the tank."
    pS "Aye aye."
    enS "Roger."
    hide jennica with dissolve
    hide teresa with dissolve
    "Staying in cover, Jennica and Teresa cycle around the rubble, getting as close to the tank as possible without revealing themselves."
    "I shift down the cover, moving away from the tank."    
    "There are just six BC enforcers standing next to the tank."
    "It's now or never."
    menu:
        "It's now or never."
        "Fire.":
            pass
    play audio "lazer.wav"
    "Whipping around the cover, I take aim and fire two quick shots."
    play audio "lazer.wav"
    "Two BC enforcers drop dead as the rest scramble for cover."
    "I rush to a piece of cover opposite the tank, drawing the enforcers' attention as their fire cascades by me."
    "Out of the corner of my eye, I see Jennica and Teresa leap onto the tank."
    "The sound of charging resonates in its central cannon as it turns to aim at me."
    "Then Jennica grabs the cannon's barrel and heaves it to the side, pointing it up and away."
    "Teresa stabs something into the tank's top hatch and smoke begins spurting out from the metal."
    "I exchange fire with the enforcers."
    "They have the numbers, but not the skill."
    "I take out two of them easily, leaving the last one diving for cover."
    "Jennica and Teresa are busy pummeling the tank crew on the ground."
    "There's nowhere to run. No help coming for him. He can't escape."
    "I move out of cover and advance toward his position."
    play audio "lazer.wav"
    hide bc_enforcer with dissolve
    "The second his head peeks up, I blast his skull with a bolt."
    "He drops dead."
    "A simple maneuver."
    "Holstering my blaster, I watch Jennica and Teresa climb inside the tank and survey the bodies on the ground."
    "One, two, three, four, five..."
    "Where's the sixth?"
    enforcer "Freeze!"
    show bc_enforcer at stream_center with dissolve
    "An enforcer taps my back with his gun."
    enforcer "Tell your crew to stand down!"
    mS "Easy."
    enforcer "I'm giving the orders here!"
    play audio "lazer.wav"
    hide bc_enforcer with dissolve
    "The enforcer goes silent as his body falls to the ground."
    vS "Never thought I'd be the one to save you, Captain."
    show vega at stream_center with dissolve
    "I whip around to see Vega standing just a few meters away, smoke spilling out from a rifle in her hands."
    mS "Vega!"
    vS "Hello, Captain Moze."
    "Her weapon is still drawn, aiming at me."
    "Additional Dragonflies emerge from behind her, they aim rifles at Jennica and Teresa who stand on the tank with their arms raised in the air."
    vS "What are you doing back here?"
    menu:
        vS "What are you doing back here?"
        "We're here to protect MAC.":
            mS "We're here to protect MAC."
            mS "BigCorp can't get away with him."
            mS "So we want to make sure whatever your \"Pops\" is planning happens."
        "We're here to save Polaris.":
            mS "We're here to save Polaris."
            mS "We have to show BigCorp that they can't take our freedom without a fight."
    "Vega holds for a moment."
    "The sounds of battle in the distance are almost completely gone."
    "She lowers her weapon, and the other Dragonflies do the same."
    vS "I didn't expect you to come back."
    if outlaw > marshal:
        vS "And to be honest, I don't know if I'm glad that you did."
    else:
        pass
    vS "But we need you."
    "She walks past me toward the tank and I follow her."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    vS "Big gun. Think you and your crew know how to use it?"
    pS "Please, I can drive anything!"
    enS "It's a cannon, not rocket science."
    enS "And I understand rocket science too."
    vS "Good."
    vS "We repelled BigCorp's first attack, but we know they're not going to give up."
    "She puts a hand on the vehicle."
    vS "With this, we might stand a chance."
    vS "Right now Coil is putting the final touches on our backup plan."
    mS "Which is?"
    vS "The plaza tower can be convered into a rocket."
    vS "We'll defend it long enough to make sure preparations are ready for launch."
    vS "Then everyone who can make it will enter the tower and take off."
    enS "And where's MAC in all this?"
    vS "For safety, he's been taken into the tower already."
    vS "They won't use artillery. Don't want to risk hitting MAC."
    vS "So if we can hold them on the ground, we can win."
    pS "So we're the bait?"
    vS "No. We're the wall."        
    "Vega turns and signals to the other Dragonflies."
    "They hesitate for a moment, then disperse, rushing down the street toward the plaza."
    vS "And you, Captain Moze, are our keystone."
    "Vega climbs up onto the tank."
    vS "I'll be your navigator. But we don't have a lot of time."
    vS "BC's sure to--"
    "As Vega speaks, a siren goes up from Polaris's plaza."
    "We all turn our attention back to the cruiser."
    "Drop ships swarm out, angling toward the town."
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
    "I open my palm and hold it out in front of me."
    "A blue hologram projects up from the disc."
    show mac stream neutral at stream_center_mac with dissolve
    "It's MAC."
    mS "MAC!"
    "Jennica and Teresa leap down from the tank and crowd around me."
    pS "Hey, little guy!"
    enS "Good to see you, MAC."
    macS "Captain? Moze? Is it really you?"
    menu:
        macS "Captain? Moze? Is it really you?"
        "We came back for you!":
            mS "Yes, MAC! We came back for you!"
        "We came to keep you safe!":
            mS "Yes, MAC! We came back to ensure you're safety."
    mS "Are you okay? Are you hurt?"
    if rudeMACGoodbye == True:
        macS "Why do you care? Wasn't this just your mission?"
        "The world goes cold."
        enS "That's not fair, MAC."
        pS "We're a family."
        macS "It's what {i}she{/i} said."
        menu:
            macS "It's what {i}she{/i} said."
            "I'm sorry, MAC.":
                mS "I'm sorry, MAC."
                mS "I didn't mean it."
                mS "I thought that saying that to you would make saying goodbye easier."
                mS "But it just made it hurt more."
                mS "I regretted saying it the second the words left my mouth."
                mS "We're here for you now, whatever you need. However we can help."
                mS "Just tell us where you are, and we'll be there for you. Always."
                "MAC pauses for a moment. As if pondering what I've said."
            "The job's not finished.":
                mS "It is a job MAC, and it was, without a doubt, personal."
                mS "But the job's not done."
                mS "BC is here for you, and we're not going to let them take you away."
                mS "I finish what I start. And making sure you're safe, isn't finished yet."
                mS "So tell us where you are. Tell us how we can help you."
                "MAC pauses for a moment. As if pondering what I've said."
    macS "I am okay."
    macS "But Coil has brought me away from the fighting."
    if macViolence >= macPeace:
        macS "And I was doing such a good job with the turret!"
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
    macS "Captain?"
    menu:
        macS "Captain?"
        "We're going to make it through this.":
            mS "We're going to make it through this MAC."
            mS "I don't know how. But we will."
            if macHope >= macPessimism:
                macS "I believe you, Moze."
                macS "I know you'll figure it out."
            else:
                macS "The odds are not in our favor."
                macS "But they have not been since you found me."
        "These scumbags are going to regret this.":
            mS "These BC scumbags are going to regret picking this fight."
            mS "We're going to rip them to shreds."
            if macViolence >= macPeace:
                macS "Shreds!"
            else:
                macS "Defeating them is our priority."
                macS "The state of their bodies afterwards less so."
    macS "It is good to hear from you, Moze."
    mS "You too, MAC."
    mS "We'll talk soon."
    pS "Be good, kid!"
    enS "Take care of yourself!"
    hide mac with dissolve
    "The hologram shivers, then fades."
    "I look up to the sky. The approaching dropships, then turn to my crew."
    if teresaRomance == True:
        "Teresa steps up next to me. She takes my hand in hers and squeezes."
    elif jennicaRomance == True:
        "Jennica steps up next to me. She takes my hand in hers and squeezes."
    else:
        pass
    "The wave of destruction rushes towards us."
    mS "We stop them here."
    "The three of us turn and climb inside the tank."
    hide jennica with dissolve
    hide teresa with dissolve
    jump vig4_sc6_defend_2

label vig4_sc6_defend_2():
    show vega at stream_center with dissolve
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    "I climb into the tank last."
    "Jennica is already sitting in a chair near the front while Vega sits to one side peering through a scope."
    "Teresa situates herself off to one side, monitoring several screens."
    "I settle into a chair in the center."
    mS "How're we looking, Jenn?"
    pS "Fine, Cap, doesn't look too complex. We'll just have to work as a team."
    pS "I'll take maneuvering. Teresa, take care of our shields and engine power."
    enS "Makes sense."
    pS "Vega, if you're on navigation, take that scope and give me directions."
    vS "Gotcha."
    pS "Cap, you stay in the center, be our spotter and operate the main cannon."
    mS "Roger, let's roll out."
    pS "Aye aye."
    "The tank accelerates as Jennica shifts the sticks in front of her forward."
    "I turn to Vega."
    mS "Welcome to the Oakley, Vega."
    "She smiles back at me."
    if outlaw > marshal:
        vS "Don't worry, it's just temporary."
    else:
        vS "It's a pleasure!"
    pS "Vega, where should I be heading?"
    vS "Back to the plaza, we still have time to join the perimeter defense."
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
    enS "Shields holding firm."
    vS "Guess they figured out we aren't friendly."
    "Looking through a monitor, I see dropships landing at the outskirts of Polaris and dropping off battalions of BC enforcers."
    "Dragonflies move across the ruined rooftops, and rush past the tank to take cover in the ruins of the street."
    "They bring the fight to the approaching army, firing at the BC battalions."
    "The true battle for Polaris begins."
    "A dropship careens down toward the central street, as if to fly directly overhead."
    mS "Vega, use the machine guns and hit the enforcers with suppressing fire."
    "The rapid fire of the machine guns sail out into the night."
    "I initiate the firing procedure and grip the cannon's controls."
    "The tank vibrates as the cannon charges. The whole vehicle thrums with energy."
    "It jerks back as the cannon fires."
    "A stream of blue light blasts out from the cannon."
    "It collides with the dropship, creating a fireball in the sky."
    "As the pieces crash into Polaris, additional flames catch fire on the buildings."
    "Smoke billows as BC encroaches."
    "A horde of BC enforcers stream down the road toward us, a hail of blaster bolts clatter on our hull."
    enS "Shields slowly dropping but we're still at 90\%."
    vS "BC scum!"
    "Vega turns the machine gun on the battalions and lets loose, bolts of blue light ripping into the frontlines."
    "I charge the cannon again and unleash its blast at another dropship." 
    "Its shell also slams into the ground, this time close to us."
    show vig1_town_stream with hpunch
    "The explosion shakes the tank."
    "We keep the stream of fire up while Jennica tries to keep us a moving target in the street."
    "But it's a losing battle."
    "Even with the tank, the wave of BC troops doesn't stop."
    "Up above, a steady stream of dropships continues to descend from the cruiser."
    "The Dragonflies ahead of us start to be pushed back."
    "A group at the head of the pack on the ground are pinned by blaster fire."
    "A call comes in over Vega's communicator."
    dflyGuard "Vega, come in! We're pinned down, need assista--"
    play audio "cutCall.wav"
    "The audio gets cut as an explosion throws dirt over the frontline."
    vS "Shit! Moze, we need to cover their retreat!"
    "The dirt and smoke clears over the frontline squad."
    "Suddenly, I recognize them." 
    "They're the squad that held Teresa and Jennica captive during the festival."
    vS "Moze! We have to help them!"
    menu:
        vS "Moze! We have to help them!"
        "Leave the frontline. Pull back to the barricade.":
            jump vig4_sc6_defend_3_barricade
        "Support the frontline. Leave the barricade":
            jump vig4_sc6_defend_3_frontline

label vig4_sc6_defend_3_barricade():
    mS "Vega, we can't afford to. If we leave this position, the barricade falls and we lose everything."
    "The BigCorp assault batters against our defenses."
    enS "Shields are at 75\%. We move forward, we risk putting ourselves in critical danger."            
    vS "But they're my friends!"
    mS "I'm sorry, Vega. We can't risk it. Order all your forces to retreat."
    "Vega holds for one moment, staring out the tank windows at the onslaught of the BC army."
    "Then picks up a communicator. Her voice projects out from the tank."
    vS "All forces, retreat! Back to the barricade!"
    mS "Jenn, hold us here to cover the retreat."
    pS "Roger!"
    "Vega and I keep firing into the swarm of BC soldiers."
    "The Dragonflies surrounding the tank turn and rush back toward the barricade."
    "The forces on the rooftops do the same, but many of them are cut down as soon as they retreat."
    "Some of them make it back."
    "The squads at the frontline have no such luxury."
    "Anyone who turns to run is immediately shot in the back."
    "The remainder stay at the frontline, firing desperately into the opposing army."
    "One by one, they fall to the ground, until there's one soldier left standing."
    "As he starts to turn to try to retreat, something lands at his feet."
    "He has one brief moment to look up in our direction."
    #play audio explosion
    "Fire engulfs him. His body flails to the ground, writhing."
    menu:
        "How does it feel?"
        "Got what they deserved.":
            "They got what they deserved."
        "I couldn't risk the barricade.":
            "The barricade is too important. I couldn't risk it on them."
    show vig1_town_stream with vpunch
    "A grenade explodes at our side."
    enS "Shields are at 60\%. We can maintain this position for a bit longer."
    vS "Scumbags!"
    "Vega screams as she lays on the trigger for the machine gun."
    "Bolts rip into the BC army, tearing up the frontline."
    "I charge another blast from the cannon."
    "The cannon discharges, distintegrating a line of BC enforcers in an instant."
    "The Dragonflies have all left the frontlines. They fire back at the BC army from the barricade."
    enS "Shields holding at 45\%."
    mS "Alright, time to reposition, find a way to recharge those shields."
    show vig1_town_stream with hpunch
    "The tank jerks to the side as an explosion detonates on our side."
    jump vig4_sc6_defend_4

label vig4_sc6_defend_3_frontline():
    mS "Jenn, push forward! We have to support the frontline so they have time to retreat!"
    pS "Roger!"
    "Jenn pushes the throttle ahead and we careen forward, rushing past Dragonflies as they dive out of the way."
    vS "Thank you, Moze."
    enS "Shields at 75\%. We don't have a lot of room for error here."
    vS "Hit them harder than they can hit us!"
    "Vega lays on the machine guns again as I fire another blast from the cannon."
    "The streets of Polaris are pockmarked with craters." 
    "Some from grenades and rocket launchers, some from our own cannon."
    "Jennica pulls the tank into a stop just at the front edge of the Dragonfly forces."
    "The hail of fire is more intense here. The rattle of bolts is constant."
    enS "Shields at 65\% and dropping quickly!"
    mS "Vega, if they don't move now, we're all dead!"
    vS "I know!"
    "Vega lifts a communicator from her side."
    vS "Get out of here, now! We'll cover you!"
    "The Dragonfly squad turns their back on the fire and starts rushing back toward the barricade."
    "One of them, their leader, glances at us. Even though he can't see me, it's as if we're making eye contact."
    "He nods quickly."
    menu:
        "How does it feel?"
        "They didn't deserve to die.":
            "They were just doing their job. That doesn't mean they deserve to die."
        "Lucky bastard.":
            "They're lucky I didn't leave them for dead."
    show vig1_town_stream with vpunch
    "A grenade explodes at our side."
    pS "Damn, maneuverability is getting a little wonky. How much longer do we have to stay out here?"
    vS "Just a little while longer to cover the retreat."
    enS "Shields are down to 45\%. We're sitting ducks out here!"
    mS "Keep firing!"
    "The cannon discharges into the encroaching swarm, disintegrating a line of soldiers in an instant."
    "Vega's machine guns keep the closest enemies at bay."
    "But then the machine guns stop firing."
    vS "Crap, they're overheated!"
    pS "So we only have the cannon?"
    enS "Shields at 25\%!"
    mS "It'll have to do, Jenn, pull us back to the barricade!"
    "I fire one last blast from the cannon." 
    "It rips through a drop ship that collides into the street, taking more soldiers out with it."
    pS "Aye!"
    "The tank rumbles as Jennica pulls it in reverse, slamming it back toward the barricade as fast as it can go."
    "We peel into a stop, just a few meters from the barricade."
    mS "Teresa, find a way to recharge those shields. Jenn I nee--"
    jump vig4_sc6_defend_4

label vig4_sc6_defend_4():
    vS "Shit, contact on the rooftop!"
    "I glance through a monitor just in time to see it: a BC enforcer with a rocket launcher."
    "I reach for the cannon, but it's too late."
    "Smoke streaks through the air."
    show vig1_town_stream with hpunch
    "The rocket slams into the tank's side."
    "Alarms start blaring, red lights flashing all around the tank's interior."
    enS "Shields at 5\%! Another hit like that and we're dead!"
    "The enforcer is loading another rocket."
    mS "Everyone, out of the tank, now!"
    hide vega with dissolve
    "Teresa throws open the top hatch and helps Vega scramble out first."
    hide jennica with dissolve
    hide teresa with dissolve
    "Jennica and Teresa follow quickly."
    "The enforcer has finished loading."
    "I quickly lift myself out of the hatch and glance to my side."
    "The launcher is aimed directly at the tank."
    "I leap to the ground and rush toward the barricade."
    "Behind me, I feel the heat against my back as the rocket detonates against the tank."
    "A shockwave ripples out, sending me flying through the air and rolling into the dirt."
    "Picking myself up, I turn around to see the hull of the tank engulfed in flames."
    "The BC army marches up from the distance."
    vS "Come on!"
    show vega at stream_center with dissolve
    "Vega grabs me by the hand and pulls me up, sprinting the final few feet to the barricade."
    "We clamber over and slide down the other end as people climb to shoot back at the approaching enemies."
    hide vega with dissolve
    "Taking a couple steps back from the barricade, I drop to one knee, glancing around me."
    "Polaris burns."
    "Ash and embers fall all around me."
    "Heat radiates on my skin."
    jump vig4_sc6_defend_5

label vig4_sc6_defend_5():
    vS "Moze!"
    show vega at stream_left with dissolve
    vS "What do we do?"
    "Just then, the thrum of a ship screeches over head."
    "I look up in time to see a dropship pull into a hover above us."
    show bc_enforcer at stream_center with Dissolve (0.5)
    "Two BigCorp enforcers drop out."
    "One of them tackles me to the ground."
    hide vega with dissolve
    "Above me, an explosion."
    "Sheets of metal collide all around me as the fireball heats up my face."
    "I try to stand up, but the enforcer grapples me."
    "He grabs me by the throat and lifts me into the air."
    "I flail at his arms, scratch at his face, but he's massive and I can't get purchase."
    "The periphery of my vision starts to go dark."
    hide bc_enforcer with dissolve
    "The world disappears."
    pause 1.0
    mS "{i}gasp{/i}"
    "Then I fall to the floor as something thuds next to me."
    "Staggering to my knees, I see that the enforcer has a smoking hole in the back of his head."
    show vega at stream_left with Dissolve(0.5)
    show bc_enforcer at stream_center with Dissolve(0.5)
    "Behind him, Vega grapples with the other enforcer."
    "I draw the pistol from the dead body's belt and fire."
    "The bolt hits the enforcer in the chest, giving Vega the chance to draw a knife from her belt and stab it into his neck."
    hide bc_enforcer with dissolve
    "She falls to her hands and knees, gasping for air."
    "I look around. The rest of the Dragonflies are focused on defending the barricades."
    "No one's even looking at us."
    "Who could have shot my assailant?"
    "Then I see it."
    "A shadow drops from a building in the plaza and enters the tower."
    "I stagger to my feet."
    mS "Vega, I have to go."
    show vega at stream_center with dissolve
    vS "What? What do you mean \"go?\""
    vS "We have to fight!"
    enS "Moze!"
    show teresa stream neutral at stream_right with dissolve
    show jennica stream neutral at stream_left with dissolve
    pS "Cap, are you okay?"
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
        "A hunter.":
            mS "A hunter."
            "Jennica and Teresa look at each other."
            pS "Sorry, Vega. But this is for Moze to handle herself."
        "Ama Deadeye Reyes.":
            mS "Ama Deadeye Reyes."
            "Vega's eyes go wide."
            vS "No! But Coil's in the tower!"
    mS "I'll go. I can handle this."
    mS "You have to stay here. You have to stop them."
    "We turn to look at the flames that lick at Polaris."
    mS "Somehow."
    if vig2_outlawEpilogue == True:
        "unknown voice" "Uh god, and here I thought you all would have toughened up in the last two weeks."
        "A familiar voice...but from where?"
        enS "Captain, we're being hailed by a new signal, I don't--"
        show vig1_town_stream with hpunch
        "A ship suddenly streaks overhead, careening toward the BC dropships."
        "Its wings open into attack formation as green bolts of light rip into a dropship, sending it to the ground."
        "Three more fighers fly by immediately after. Then another. Then another."
        "A fleet of attack ships."
        pS "Who the--that's one hell of a pilot?"
        show reginald at stream_center with dissolve
        goon "I really don't get paid enough for this shit."
        show jennica stream shock at stream_left with dissolve
        pS "Reginald!?"
        goon "Matticus sends his regards."
        goon "Said he had a debt that needed paying off."
        show jennica stream neutral
        "The swarm of attack ships engage the BC dropships, destroying them."
        goon "So take care of whatever you got to do down there. We'll handle this."
        menu:
            goon "So take care of whatever you got to do on the ground. We'll handle the air shit."
            "Thank you.":
                mS "Reginald...thank you."
                goon "Now don't go getting soft on me."
                goon "You just do your job and I'll do mine."
                goon "Even though it's a massive pain.."
                mS "Copy that."
            "Affirmative.":
                mS "Copy that."
        "A handful of attack ships break formation, streaking fire along Polaris's ground and ripping into the BC troops."
        "Exposed to fire by the air, the BC forces have to regroup while the Dragonflies cheer and go on the offensive."
        hide reginald with dissolve
    #if vig3_marshalChoice == True:
    else:
        "Vega pauses for a moment."
        vS "Go, Moze."
        vS "We'll do what we have to do out here."
        enS "We will too."
    enS "If BC takes the plaza it will not matter what you do up there, we'll all be toast."
    pS "You go get the kid. We'll keep a path clear down here."
    menu:
        pS "You go get the kid. We'll keep a path clear down here."
        "I'm not leaving you.":
            mS "No way, I'm not leaving you two!"
            enS "You're not leaving anything."
            pS "We're just splitting up to make the mission succeed."
            "Jennica and Teresa" "We've got this."
            if jennicaRomance == True:
                "Jennica steps up close to me. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                pS "Go do what you do best, Moze."
            elif teresaRomance == True:
                "Teresa steps up close to me. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                show teresa stream happy
                enS "Go do what you do best, Moze."                
            else:
                pass
        "Thank you.":
            mS "Jenn, Resa, I--"
            if jennicaRomance == True:
                "Jennica steps up close to me. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                pS "Go do what you do best, Moze."
            elif teresaRomance == True:
                "Teresa steps up close to me. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
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
    "A series of stairs that winds up to the top of the tower."
    "Each step feels like an eternity."
    "A chance to think about the steps that brought me here."
    "Allistar."
    "Matticus."
    "Rec."
    "Ama."
    "Jennica."
    "Teresa."
    "MAC."
    "Every person. Every choice."
    "Here I am."
    "The stairs flatten out."
    "Two Dragonflies with bullet holes in their chest lie on the floor."
    "There's a wide room in front of me, and two voices shouting within."
    amaS "Just tell me where the robot is, or I'll kill you like I did your friends outside."
    "I step across the threshold into a wide room."
    show vig2_datacenter_stream onlayer background with dissolve
    show coil at stream_left with dissolve
    show ama at stream_right with dissolve
    "Coil stands in the center, in front of a massive computer console."
    "Ama holds her rifle, aiming it at Coil's back."
    cS "I will never tell you, and you will never find him."
    amaS "Sounds like you're just stalling."
    cS "Precisely."
    "Coil turns around and faces me."
    cS "Well, Moze, I'm glad you made it."
    "His face looks haggard, his eyes bloodshot."
    "Ama whips around to aim her rifle at me."
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
    amaS "Watch your tongue, kid."   
    amaS "I'm calling the shots here." 
    cS "So you think."
    "Ama trains her gaze back on Coil as he steps away from the device and in front of the two of us."  
    cS "Tell me truthfully, Moze. What was your plan in coming here?"
    menu:
        cS "Tell me truthfully, Moze. What was your plan in coming here?"
        "I came for MAC.":
            mS "I came for MAC."
            mS "I'm not leaving without him."
            "Coil sighs."
            cS "I assumed that was the case."
            cS "I must say I am disappointed."
            if vig4_defendPolaris == True:
                cS "Although, without you, we probably would already have been overrun."
            cS "MAC is gone."
            amaS "Bullshit."
            amaS "If that were true you wouldn't still be here."
            cS "How perceptive. And yet you still have no idea what you're doing."
            cS "Flailing around in the darkness with no purpose."
        "I came to help.":
            mS "I came to help, to fight off BigCorp."
            cS "And you have done an admirable job." 
            cS "Without you, we probably would already have been overrun."
    amaS "I've heard enough!"
    "Ama moves to fire her rifle."
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
    "Eyes wide, Ama fires again. And again."
    "The bolts continue to be absored."
    jump vig4_sc7_2