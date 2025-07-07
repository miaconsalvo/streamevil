####This script contains the code for the Polaris Attack routes of Vignette 4 up until Moze makes her choice about siding with Coil and Ama

###Attacking Polaris with Ama
label vig4_sc6_attack_1_ama():
    show vig1_town_stream onlayer background with dissolve
    hide targetbase_stream
    "Polaris burns."
    "The dull roar of battle echoes in the distance."
    "We make our way quickly down the clear street, hopping between pieces of cover as we do so."
    "No danger on the roofs."
    "No enemies on the street."
    "In the distance, the sounds of battle start to quiet."
    show teresa stream shock at stream_right with dissolve
    enS "Shit, patrol, get down!"
    hide jennica with dissolve
    hide teresa with dissolve
    "The four of us dive over the rubble of a nearby building and crouch behind the ruined stones."
    "A low hum gets closer, muddying the sound of several voices."
    "One breaks through, shouting."
    enforcer "Halt! Halt I said!"
    show bc_enforcer at stream_center with dissolve
    "I peek over the ruins."
    "A battalion of two dozen BC enforcers surround a crowd of hostage Dragonfly soldiers."
    "Behind them, the source of the rumbling: an immense hover tank, laborious engine purring over the sounds of warfare."
    enforcer "Alright, you heard the orders." 
    enforcer "Tank squadron locks this sector down and the rest of you are with me."
    enforcer "Once the next assault begins, we hit those Dragonflies with full force."
    "He glares over the captives."
    enforcer "And our new friends here are going to help us \"convince\" them they should surrender."
    enforcer "Remember: if you see a droid, don't shoot it. BigCorp wants it in safe custody {i}undamaged{/i}."
    enforcer "Kill everyone else."
    hide bc_enforcer with dissolve
    show jennica stream angry at stream_left with dissolve
    pS "Bastard."
    show teresa stream neutral at stream_right with dissolve
    enS "Position looks bad. We can't leave here without exposing ourselves."
    show ama at stream_center with dissolve
    amaS "You're thinking too small."
    "Ama points at the hover tank."
    amaS "We take that, we don't have to worry about hiding and cover anymore."
    menu:
        amaS "We take that, we don't have to worry about hiding and cover anymore."
        "You can't be serious.":
            mS "You can't be serious, Ama."
            amaS "Think about it, we get more firepower, safety from enemy fire."
            amaS "Who's going to be able to stop us?"
            amaS "I think it's genius."
        "Genius.":
            mS "Genius idea."
    enS "I don't know if I'd go that far."
    pS "We still have to steal the damn thing."
    amaS "Simple, wait for that group to wander off, then take out the crew. Easy maneuver."
    hide ama with dissolve
    pS "No way, if we're doing this then we should help those people."
    enS "Wait a minute, look at that guy!"
    show customs agent at stream_center with dissolve
    "Teresa points at one of the captive Dragonflies."
    enS "Isn't that?"
    pS "Oh yeah! That's the bastard who roughed us up at the festival."
    enS "Guess he and his squad were more talk than bite after all."
    pS "They're still hostages. We should help them."
    hide customs agent with dissolve
    show ama at stream_center with dissolve
    amaS "Well, Mozely, what's the call?"
    menu:
        amaS "Well, Mozely, what's the call?"
        "We're saving the hostages first.":
            jump vig4_sc6_attack_1_assault_ama
        "Wait for the group to split.":
            jump vig4_sc6_attack_1_split_ama

label vig4_sc6_attack_1_assault_ama():
    mS "Jennica's right. We can't let BC hold those hostages."
    mS "We take the tank, but we're also not letting this battalion get away."
    pS "Thanks, Cap."
    mS "Jennica and Teresa, take care of the tank. Ama, we'll take the battalion."
    "Ama sighs and hoists her rifle into her shoulder."
    amaS "You're lucky I'm gonna be well paid after this mess."
    enS "You'll be lucky to get anything out of this, Reyes."
    mS "Enough, get in position."
    "The battalion is about to move on."
    enforcer "Alright you maggots, break time's over. Time to get moving."
    "It's now or never."
    menu:
        "It's now or never."
        "Open Fire.":
            pass
    mS "Now!"
    play audio "lazer.wav"
    "I pop out of cover and fire two quick shots, landing them directly into the backs of two enforcers."
    play audio "lazer.wav"
    "Ama does the same, taking out the lead enforcer, while Jennica and Teresa stay in cover and shift along the side of the rubble."
    hide jennica with dissolve
    hide teresa with dissolve
    show ama at stream_right with dissolve
    show bc_enforcer at stream_center with dissolve
    "There's a moment of pause before the rain of blaster fire hits mine and Ama's position."
    amaS "Hope this isn't suicide, Mozely."
    "I hear the tank rumble as it shifts its position. The sound of a shot charging resonates from its chamber."
    mS "Just follow my lead."
    "I rush out of cover, leaping over the rubble as the tank's blast erupts."
    "The explosion propels me through the air."
    "Landing in the dirt, I roll quickly as blaster bolts thud into the ground around me."
    "I slam my back into another piece of ruined building as Ama strafes to my side."
    "Rifle poised in hand, she fires at a constant, controlled rate, tagging a handful of enforcers before she too has to duck behind cover."
    "She tilts her head in the direction of the tank."
    amaS "Got a pretty good crew, Mozely."
    "I peek just over the rubble as a shot whizzes past my head."
    "The tank is charging its cannon again and turning to aim at our position."
    "But Teresa and Jennica have already climbed on top of it."
    "Teresa stabs something into its top hatch while Jennica grabs the cannon and drags it to aim at a group of nearby enforcers."
    "The shot fires, sending the enforcers flying into the air as the top hatch of the tank pops open."
    "Amdist the chaos, the captive Dragonflies have dispersed."
    "Some ran into the shelter of buildings while others have started brawling with BC goons."
    "Teresa and Jennica have dragged some goons out of the tank hatch and are busy pummeling them on the ground."
    "Seven BC enforcers are closing in on mine and Ama's position."
    "Ama winks at me."
    amaS "Shall we."
    menu:
        amaS "Shall we."
        "Let's dance.":
            mS "Let's dance."
        "Bet I get more.":
            mS "Bet you I tag more than you."
            amaS "You're on, kid."
    "I whip around the cover, firing shots immediately down the street."
    "One of the enforcers goes down as a grenade lands behind my cover."
    "I roll to the side, away from the explosion and fire back."
    "Ama has appeared around the corner and is advancing toward the enforcers."
    "No fear. Just the constant repeating of her rifle."
    "I blast back at our enemies, rushing toward them with reckless abandon."
    "Two drop before I get in close to the final one."
    "Tackling him to the ground, I pull up and look him in the eyes."
    "He puts his hands up in front of his face."
    "I fire two quick shots into his chest."
    "His body goes cold."
    hide bc_enforcer with dissolve
    "The world around me has gone quiet again."
    "Standing up, I see the Dragonflies gathering around one another."
    "The ones who lived."
    "Some lay motionless on the ground."
    "The sounds of battle in the distance are starting to quiet."
    "Ama steps up next to me."
    amaS "Pretty good shots Moze. Accuracy could use some work though."
    menu:
        amaS "Pretty good shots Moze. Accuracy could use some work though."
        "I got more.":
            mS "Who cares."
            mS "By my count, I got four and you got three."
            amaS "Oh ho, still got that fierceness in you, I see."
            "She grins at me."
            amaS "Just like old times."
        "Yours is slipping.":
            mS "Yours isn't what it used to be either."
            amaS "You calling me \"old,\" kid?"
            mS "I didn't say that."
            mS "Though it's true."
            amaS "Ahahaha."
            amaS "Careful Mozely, age begets wisdom."
    dflyGuard "Captain Moze?"
    show customs agent at stream_center with dissolve
    "The leader of the Dragonflies squad approaches me."
    dflyGuard "We thought we were dead."
    "He glances at the bodies in the street."
    dflyGuard "We didn't all make it, but you gave us a chance to fight back."
    dflyGuard "I know we didn't leave on the best of terms. But, thank you for saving us."
    menu:
        dflyGuard "I know we didn't leave on the best of terms. But, thank you for saving us."
        "You were just doing your job.":
            mS "You were just doing your job. I understand what that's like."
            dflyGuard "I appreciate your understanding."
            dflyGuard "Will you join us to defend the plaza?"
            amaS "We have business elsewhere."
            "The Dragonfly guard looks Ama up and down."
            "He's about to say something, then thinks better of it."
            dflyGuard "Of course."
            dflyGuard "Good luck, Captain."
            "He turns and rejoins his comrades. Together, they walk down the street toward the plaza."
            hide customs agent with dissolve
        "It wasn't about you.":
            mS "You're welcome, but it wasn't about you."
            mS "I deprived BC of strategic leverage."
            "He looks taken aback."
            dflyGuard "Ah, I see."
            dflyGuard "Will you join us to defend the plaza?"
            amaS "We have business elsewhere."
            "The Dragonfly guard looks Ama up and down."
            "He's about to say something, then thinks better of it."
            dflyGuard "Of course."
            dflyGuard "Good luck, Captain."
            "He turns and rejoins his comrades. Together, they walk down the street toward the plaza."
            hide customs agent with dissolve
        "I wanted to kill you myself.":
            $ vig4_killDflies = True
            mS "Don't thank me. I just wanted the pleasure of killing you myself."
            play audio "lazer.wav"
            hide customs agent with Dissolve(0.5)
            "The guard has half a second to look stunned before a blaster bolt rips through his skull."
            "The rest of the Dragonflies look up, confusion rampant on their faces as Ama and I draw our weapons."
            "Our blasters echo in the night."
            "Each of the Dragonflies drops to the ground. Dead."
    "Ama claps me on the back."
    amaS "That's the Mozely I remember."
    amaS "Now, let's see the vessel we have commandeered!"
    hide teresa with dissolve
    hide ama with dissolve
    jump vig4_sc6_attack_2

label vig4_sc6_attack_1_split_ama():
    mS "Ama's right, if we're going to do this we have to do it smart."
    mS "We'll wait for the battalion to split off, then take the tank when it's just a skeleton crew."
    mS "Jennica and Teresa, take care of the tank. Ama, we'll take the leftover squad."
    amaS "Strike from a place of advantage. Good."
    enS "Behind you."
    pS "Of all the hostages we've met, I won't regret letting BC keep these ones."
    mS "Get in position."
    hide teresa with dissolve
    hide jennica with dissolve
    "Staying in cover, Jennica and Teresa cycle around the rubble, getting as close to the tank as possible without revealing themselves."
    show ama at stream_right with move
    "Ama and I duck close together."
    enforcer "Alright you maggots, break time's over. Time to get moving."
    "The sound of dozens of steps as the battalion moves off down the road."
    "Slowly, but surely, they turn the corner. Disappearing out of sight and earshot."
    "I chance a glance over the rubble."
    show bc_enforcer at stream_center with dissolve
    "There's just seven BC enforcers standing next to the tank."
    "Ama winks at me."
    amaS "Time for a show."
    menu:
        amaS "Time for a show."
        "Let's dance.":
            mS "Let's dance."
        "Bet I get more.":
            mS "Bet you I tag more than you."
            amaS "You're on, kid."
    play audio "lazer.wav"
    "Whipping around the cover, I take aim and fire two quick shots."
    play audio "lazer.wav"
    "Ama follows that with a blast from her rifle."
    "Two BC enforcers drop dead as the rest scramble for cover."
    "Ama and I advance confidently. My pistol firing rapidly alongside the steady cadence of her rifle."
    "Out of the corner of my eye, I see Jennica and Teresa leap onto the tank."
    "The sound of charging resonates in its central cannon as it turns to aim at Ama and me."
    "Then Jennica grabs the cannon's barrel and heaves it to the side, pulling the metal barrel to point it up and away."
    "Teresa stabs something into the tank's top hatch and smoke begins spurting out from the metal."
    "Ama and I keep advancing on the enforcers who cower behind cover."
    "But there's nowhere to hide."
    "The second one of them peeks around a corner, a bolt lands between their eyes."
    "There's nowhere to run. No help coming for them. They can't escape."
    "We rip them to shreds, leaving none standing."
    hide bc_enforcer with dissolve
    "Jennica and Teresa are busy pummeling the tank crew on the ground."
    "A simple maneuver."
    "The sounds of battle in the distance are starting to quiet."
    "Ama steps up next to me."
    amaS "Pretty good shots Moze. Accuracy could use some work though."
    menu:
        amaS "Pretty good shots Moze. Accuracy could use some work though."
        "I got more.":
            mS "Who cares."
            mS "By my count, I got four and you got three."
            amaS "Oh ho, still got that fierceness in you, I see."
            "She grins at me."
            amaS "Just like old times."
        "Yours is slipping.":
            mS "Yours isn't what it used to be either."
            amaS "You calling me \"old,\" kid?"
            mS "I didn't say that."
            mS "Though it's true."
            amaS "Ahahaha."
            amaS "Careful Mozely, age begets wisdom."
    show teresa stream neutral at stream_center with dissolve
    enS "You two want to keep chattering or do you want to see our prize."
    "Ama claps me on the back."
    amaS "Yes, let's see the vessel we have commandeered!"
    hide teresa with dissolve
    hide ama with dissolve
    jump vig4_sc6_attack_2_ama

label vig4_sc6_attack_2_ama():
    show jennica stream neutral at stream_left with dissolve
    "As I climb in through the tank's hatch, Jennica is already sitting in a chair near the front."
    "She's examining a string of buttons and sticks in front of her."
    mS "Any idea how to drive this thing, Jenn?"
    pS "Sure, Cap, doesn't look too complex. We'll just have to work as a team."
    pS "I'll take maneuvering. Teresa, take care of our shields and engine power."
    show teresa stream neutral at stream_right with dissolve
    enS "Makes sense."
    pS "Ama, take control of the machine guns."
    show ama at stream_center with dissolve
    amaS "Music to my ears."
    pS "Cap, you stay in the center, be our spotter and take the main cannon."
    mS "Roger, let's roll out."
    pS "Aye aye."
    play audio "callRing.wav"
    "As Jennica goes to move the tank forward, a ring suddenly echoes in the tank."
    enS "Someone is calling us."
    pS "On a BigCorp frequency?"
    enS "No. It's not BigCorp, but it has access to their comms?"
    amaS "It's the robot! Answer it!"
    "Teresa inputs something into a screen on her side."
    "At the front of the tank, a blue hologram slowly starts to take shape."
    show mac stream neutral at stream_center_mac with dissolve
    "It's MAC."
    mS "MAC!"
    pS "Hey, little guy!"
    enS "Good to see you, MAC."
    macS "Captain? Moze? I expected it was you. Stealing a tank is very much your style."
    menu:
        macS "Captain? Moze? I expected it was you. Stealing a tank is very much your style."
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
    macS "But Coil has brought me into the plaza tower and away from the fighting."
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
    cS "That's enough, MAC."
    play audio "cutCall.wav"
    hide mac with dissolve
    "The signal is cut short."
    enS "That was Coil's voice."
    pS "No doubt. So he has our boy at the top of the tower."
    amaS "The barricades they have set up around the plaza will be a bit of trouble, but we can handle them."
    mS "We won't have to on our own."
    pS "Cap?"
    mS "That enforcer said BC was preparing a second assault. This first one must have just been to soften up Polaris's defenses."
    mS "When BC launches their next attack, we can use the chaos to break through and get into the tower."
    amaS "Oh, I {i}like{/i} this plan, Mozely."
    enS "Efficient and clever."
    pS "A lot of people are going to die. But I guess that's unavoidable at this point."
    mS "As long as we get MAC. That's what matters."
    "As I finish speaking, a siren rings out from Polaris's plaza."
    "I peer through the tank's scope at the Cruiser hovering in the night sky."
    "A line of dropships have begun careening through the air to Polaris."
    mS "The second attack is starting."
    amaS "Just in time."
    mS "Agreed. Jenn, take us toward the plaza."
    "The tank accelerates as Jennica shifts the sticks in front of her forward."
    "We glide smoothly over the ground as a calm before the storm settles over Polaris."
    hide ama with dissolve
    hide jennica with dissolve
    hide teresa with dissolve
    jump vig4_sc6_attack_3_ama

label vig4_sc6_attack_3_ama():
    "Smoke billows all around us as we navigate Polaris's ruined roads."
    "Flames lick at the sides of buildings."
    "Even in the tank, we can feel the heat from outside."
    "The sounds of battle have struck up again. And they get louder with each second we advance."
    mS "Everyone, get ready."
    "We turn onto the main street."
    "Chaos erupts."
    "A dropship screeches by overhead, turrets strafing positions defended by Dragonflies."
    "The Dragonflies have consolidated their defenses behind an enormous barricade blocking the main street into the plaza."
    "A swarm of BC enforcers march down the street."
    "Blaster fire streaks in both directions."
    "As we emerge onto the street, the BC forces suddenly cheer."
    pS "They think we're on their side."
    enS "We are in their tech."
    amaS "Use it to our advantage, right, Mozely?"
    menu:
        amaS "Use it to our advantage, right, Mozely?"
        "Pretend to be with BigCorp, attack the Dragonflies.":
            $ vig4_killDflies = True
            mS "Ama's right. Keep our weapons aimed at the Dragonfly position."
            mS "Jennica, get us there as quick as you can without being suspcious."
            pS "Roger, Cap."
            "The tank advances on the barricade."
            "Shots from the Dragonflies start to rattle against our hull."
            enS "Shields are at 95\%."
            amaS "Oh I've been waiting for this!"
            "Ama grabs the machine gun controls and whips it around, aiming for the squads positioned on nearby rooftops."
            "The rapid fire of the machine gun tears into the squads, sending them into a retreat."
            show vig1_town_stream with hpunch
            "A grenade explodes next to us, engulfing some BC enforcers in flames and shaking our hull."
            enS "Tough hit but shields are still at 85\% and holding."
            "I grip the cannon controls and point at a squad of Dragonflies huddled behind nearby cover."
            "The whole tank thrums with energy as the cannon charges."
            "A beam of blue light bursts from the cannon, striking through the rubble."
            "A pillar of flame erupts into the air where the cannon impacted the ground."
            "There's no evidence of the Dragonflies who were hiding behind cover."
            mS "Jenn, keep us moving."
            "We're slowly advancing toward the head of the BC army."
            "Ama hasn't let go of the machine gun trigger. Almost all of the Dragonflies are hidden behind cover."
            "A group tries to take shots at us from a rooftop."
            "I aim the cannon at the base of the building."
            "The thrum of energy."
            "The blue light."
            "Another pillar of flame and the memory of human presence."
            "We keep advancing."
            enS "Contact on the rooftops!"
            show vig1_town_stream with hpunch
            "Another detonation on the side of the tank."
            "I whip a monitor around to view the assailants."
            "It's a group of Dragonflies armed with rocket launchers a couple of buildings away from us."
            "They're reloading the launchers and preparing for another volley."
            mS "Teresa, direct shields against those launchers. Ama--"
            amaS "I know, I know, I see them!"
            "Ama aims the machine gun at the direction of the squad and begins firing, but too late."
            show vig1_town_stream with hpunch
            "Another rocket streaks through the air and collides with us just as the bolts from the machine gun rip into their bodies."
            mS "Resa, how're we doing?"
            enS "Bad hits. We're at 40\% shields, but holding. We just don't want to take two more of those."
            pS "Cap! We're almost at the barricade!"
            "I turn to look ahead."
            "She's right, we're closing in."
            mS "Alright, Resa, direct our power into engine thrusts and tell me when it's ready to go. We're going to ram through it."
            enS "Are you sure that's--"
            amaS "Oh, yes!"
            mS "Just do it!"
            mS "Jenn, hit the thurst forward. Hard!"
            pS "Aye aye, Cap!" 
            "The main cannon charges. Our engines hum with excitement."
            enS "Ready, captain!"
            mS "Launch!"
            "Fire erupts from the cannon at the same time as we rush forward."
            "The barricade shatters as the cannon's blast collides with it."
            "Our shields sparkle, the tank ramming into the wall and splitting it apart."
        "Attack BigCorp, rush the barricade.":
            mS "No. BigCorp is still the enemy."
            mS "Jenn, get us to that barricade as fast as you can."
            pS "Aye!"
            mS "Resa, keep those shields up."
            enS "Roger, we're at 95\% currently!"
            mS "Ama, open fire on any BC goons you see."
            amaS "I don't like losing the surprise, but I do like killing some BC goons."
            "Ama grabs the machine gun controls and whips it around, aiming for the squads enforcers at the frontline."
            "As the tank accelerates forward, confusion spreads throughout the BC army, throwing them into disarray."
            "Our shields continue to take hits from both sides as blaster fire rattles against our hull."
            show vig1_town_stream with hpunch
            "A grenade explodes at our side, shaking the tank slightly."
            enS "Shields are at 80\%. We're taking a lot of hits."
            "A dropship begins to aim down toward us."
            mS "We can dish them out too."
            "I grip the controls for the main cannon."
            "The whole tank thrums with energy as the cannon charges."
            "A beam of blue light bursts from the cannon, striking the dropship out of the sky."
            "The ship explodes in a fireball as wreckage falls into Polaris, crashing into the BC swarm."
            mS "Jenn, how are we doing?"
            pS "We're close, just a bit further!"
            enS "Captain, we're starting to take less fire from the Dragonflies."
            show vig1_town_stream with hpunch
            "Another detonation on the side of the tank."
            "I whip a monitor around to view the assailants."
            "It's a group of BC enforcers armed with rocket launchers." 
            "They're on a building near the back of the attack force."
            "They're reloading the launchers and preparing for another volley."
            "I whip the main cannon controls around, aiming them at the base of the building."
            "The cannon charges."
            "The rocket streaks through the air."
            "The beam of blue light strikes the building as another pillar of flame erupts into the night air."
            show vig1_town_stream with hpunch
            "The rocket detonates close to us, but not a direct hit."
            enS "Shields are at 60\%."
            pS "Cap! We're almost at the barricade!"
            "I turn to look ahead."
            "She's right, we're closing in."
            mS "Alright, Resa, direct our power into engine thrusts and tell me when it's ready to go. We're going to ram through it."
            enS "Are you sure that's--"
            amaS "Oh, yes!"
            mS "Just do it!"
            mS "Jenn, hit the thurst forward. Hard!"
            pS "Aye aye, Cap!" 
            "The main cannon charges. Our engines hum with excitement."
            enS "Ready, captain!"
            mS "Launch!"
            "Fire erupts from the cannon at the same time as we rush forward."
            "The barricade shatters as the cannon's blast collides with it."
            "Our shields sparkle, the tank ramming into the wall and splitting it apart."
        "Attack both Dragonflies and BigCorp.":
            $ vig4_killDflies = True
            mS "Screw it." 
            mS "Jenn, get us to that barricade as fast as you can."
            pS "Aye aye."
            mS "Resa, keep our shields up."
            enS "Roger, we're at 95\% currently!"
            mS "Ama, fire at will."
            amaS "Oh I've been waiting for this!"    
            "Ama grabs the machine gun controls and whips it around."
            "The bolts of machine gun rounds tear into soliders: BC enforcers and Dragonflies alike."
            "Ama fires in quick, succinct burst. Striking Dragonflies on the rooftops, then BC enforcers on the ground."
            "It's a methodical madness. One I'm familiar with."
            "Confusion spreads through both sides as blaster fire pings off the tank's sides."
            enS "Shields are at 90\%, Captain."
            "I grip the controls for the main cannon. The entire tank thrums with energy as it charges."
            show vig1_town_stream with hpunch
            "Above, a dropship aims down toward our position, turrets sending fire against our hull."
            "A beam of blue light bursts from the cannon, striking the dropship out of the sky."
            "The ship explodes in a fireball as wreckage falls into Polaris, crashing into the BC swarm."
            mS "Jenn, how are we doing?"
            pS "We're close, just a bit further!"
            show vig1_town_stream with hpunch
            "An explosion suddenly detonates against our side."
            mS "Teresa, report!"
            "I whip the monitor around, looking for the assailants."
            enS "Shields are down to 60\%. We're taking fire from both sides and losing energy rapidlly!"
            "I locate the smoke streaking through the air."
            "Dragonflies on a nearby building are loading rocket launchers."
            "I drop the cannon to aim at the base of the building, charging up another blast."
            "But I'm too late."
            "A bright flashing rocket streaks toward us just as I fire the cannon."
            show vig1_town_stream with hpunch
            "The rocket impacts on our side, but at the same time, the tank's blast detonates on the building."
            "A pillar of flame erupts into the sky as the edifice crumbles to the ground."
            amaS "They're throwing grenades!"
            "Ama lays on the machine gun full auto as BC enforcers break ranks to move toward our position."
            "Most of them are cut down, but a couple are able to lob grenades that land at our side."
            show vig1_town_stream with hpunch
            "They detonate, jostling the vehicle."
            enS "Shields are down to 30\%! We can't take much more of this!"
            pS "Cap! We're almost at the barricade!"
            "I turn to look ahead."
            "She's right, we're closing in."
            mS "Alright, Resa, direct our power into engine thrusts and tell me when it's ready to go. We're going to ram through it."
            enS "Are you sure that's--"
            amaS "Oh, yes!"
            mS "Just do it!"
            mS "Jenn, hit the thurst forward. Hard!"
            pS "Aye aye, Cap!" 
            "The main cannon charges. Our engines hum with excitement."
            enS "Ready, captain!"
            mS "Launch!"
            "Fire erupts from the cannon at the same time as we rush forward."
            "The barricade shatters as the cannon's blast collides with it."
            "Our shields sparkle, the tank ramming into the wall and splitting it apart."
    "The tank rushes into the plaza as Jennica slams the controls to the side, and we go almost completely sideways."
    "The tank isn't supposed to go this fast. And it's not supposed to turn this hard."
    "But Jennica wrangles it under control as we careen to a stop at the base of the tower."
    "I open the top hatch and scramble out."
    "The barricade at the end of the plaza begins to crumble as the Dragonflies disperse."
    "BC closes in on the plaza."
    "More dropships stream down from the cruiser."
    "We don't have much time."
    "War has come."
    menu:
        "War has come."
        "This is it.":
            mS "This is it. The end of the road."
        "We're not making it out of this.":
            mS "I don't know if I see a way out of this."
    mS "This is where our score gets settled."
    show ama at stream_right with dissolve
    amaS "Then let's make sure it's settled in our favor."
    "Ama hops out of the tank, standing opposite me."
    "Suddenly, I feel something. Standing here. At war. With her."
    "It's comfort. Like we've been here before."
    menu:
        "It's comfort. Like we've been here before."
        "Reject the feeling.":
            "No. This is different. And I refuse to let her into my life again."
        "Embrace the feeling.":
            mS "Ama."
            "She looks at me."
            mS "It's good to have you here."
            "She winks."
            amaS "Good to be here, kid."
    "We both turn to look at the burning horizon, as Polaris crumbles."
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
        show reginald stream bigmad at stream_center with dissolve
        goon "I really don't get paid enough for this shit."
        show jennica stream shock at stream_left with dissolve
        pS "Reginald!?"
        goon "Matticus sends his regards."
        goon "Said he had a debt that needed paying off."
        show jennica stream neutral
        "The swarm of attack ships engage the BC dropships, delaying their advance."
        goon "So take care of whatever you got to do on the ground. We'll handle the air shit."
        menu:
            goon "So take care of whatever you got to do on the ground. We'll handle the air shit."
            "Thank you.":
                mS "Reginald...thank you."
                goon "Now don't go getting soft on me."
                goon "You just do your job and I'll do mine."
                goon "Even though it's a massive pain."
                mS "Copy that."
            "Affirmative.":
                mS "Copy that."
        hide reginald with dissolve
    #if vig3_marshalChoice == True:
    else:
        show jennica stream neutral at stream_left with dissolve
    pS "Uh, gang, you're gonna want to move." 
    mS "Not without you two."
    show teresa stream neutral at stream_center with dissolve
    enS "Negative, Captain."
    mS "What!?"
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
                "Jennica suddenly comes up from the tank. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                pS "Go do what you do best, Moze."
            elif teresaRomance == True:
                "Teresa suddenly comes up from the tank. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                show teresa stream happy
                enS "Go do what you do best, Moze."                
            else:
                pass
            mS "Guys...thank you. And be careful. I want a clean escape route when I come down with MAC."
            pS "You betcha."
            enS "Affirmative."
        "Thank you.":
            mS "Jenn, Resa, I--"
            if jennicaRomance == True:
                "Jennica suddenly comes up from the tank. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                pS "Go do what you do best, Moze."
            elif teresaRomance == True:
                "Teresa suddenly comes up from the tank. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                show teresa stream happy
                enS "Go do what you do best, Moze."                
            else:
                pass
            mS "Thank you. And be careful. I want a clean escape route when I come down with MAC."
            pS "You betcha."
            enS "Affirmative."
    hide jennica with dissolve
    hide teresa with dissolve
    "I hop down to the ground."
    "Ama steps up to my side."
    amaS "Ready?"
    mS "Ready."
    "Ama and I rush toward the tower's tall doors."
    "Behind us, we hear shouts of BC enforcers as they pour into the plaza, the echo of blaster fire."
    "And the warm vibration of a tank's cannon charging up to full power."
    jump vig4_sc7_1_attack_ama

label vig4_sc7_1_attack_ama():
    hide vig1_town_stream with dissolve
    "As soon as the doors close behind us, the sounds of battle become muffled."
    "The tower is utterly silent."
    "A distant voice calls from up above."
    cS "Up here. Come along."
    "Ama and I follow a series of stairs that winds up to the top of the tower."
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
    "Ama and I step across the threshold into a wide room."
    show vig2_datacenter_stream onlayer background with dissolve
    show coil at stream_left with dissolve
    "Coil stands in the center, in front of a massive computer console."
    cS "Well, you made it."
    "Coil turns to face us. His face looks haggard, his eyes bloodshot."
    menu:
        "Coil turns to face us. His face looks haggard, his eyes bloodshot."
        "Where is MAC?":
            mS "Where is MAC?"
            cS "Always so direct."
            cS "MAC is no longer any of your concern, Moze."
            cS "You delivered him, he is our responsibility."
            cS "And he is safe."
            if macViolence > macPeace:
                cS "You know he insisted on operating a turret when BigCorp arrived."
                cS "Said he would \"make those BC scum pay.\""
                mS "Operating a turret on the frontlines. Is that really what you consider \"safe\"?"
                cS "No. But he insisted."
                cS "And as I'm sure you're aware, he can be quite strong-willed."
                cS "He got it from you after all."
                amaS "Mozely can be quite stubborn."
                cS "I meant the bloodlust."
                "Ama tilts her head."
                amaS "That too."
            else:
                cS "You know he insisted on providing first aid to the people who were first injured by BigCorp's assault."
                cS "Said he had to \"take care of the people around him.\""
                mS "Being a frontline medic isn't exactly what I would consider \"safe.\""
                cS "No. But he insisted." 
                cS "And I'm sure you're aware he can be quite strong-willed."
                cS "He got it from you after all."
                amaS "Mozely can be quite stubborn."
                cS "I meant the altruistic urge to help other people."
                "Ama tilts her head."
                amaS "Guess that has been a phase recently."
        "Got a plan for getting out of this?":
            mS "So, do you have a plan for getting out of this."
            cS "I do."
            cS "The top of this tower can be converted into a makeshift rocket."
            cS "We will be able to finish the mission, where you failed."
            mS "And you're okay with all of Polaris dying while you escape?"
            cS "It breaks my heart."
            cS "But we have done what we could. What we were supposed to do."
            cS "MAC is no longer any of your concern, Moze."
            cS "You delivered him, he is our responsibility."
            if macViolence > macPeace:
                cS "You know he insisted on operating a turret when BigCorp arrived."
                cS "Said he would \"make those BC scum pay.\""
                mS "Operating a turret on the frontlines. Is that really what you consider \"safe\"?"
                cS "No. But he insisted."
                cS "And as I'm sure you're aware, he can be quite strong-willed."
                cS "He got it from you after all."
                amaS "Mozely can be quite stubborn."
                cS "I meant the bloodlust."
                "Ama tilts her head."
                amaS "That too."
            else:
                cS "You know he insisted on providing first aid to the people who were first injured by BigCorp's assault."
                cS "Said he had to \"take care of the people around him.\""
                mS "Being a frontline medic isn't exactly what I would consider \"safe.\""
                cS "No. But he insisted." 
                cS "And I'm sure you're aware he can be quite strong-willed."
                cS "He got it from you after all."
                amaS "Mozely can be quite stubborn."
                cS "I meant the altruistic urge to help other people."
                "Ama tilts her head."
                amaS "Guess that has been a phase recently."
    "Coil steps away from the devices and directly in front of me and Ama."
    cS "Tell me truthfully, Moze. What was your plan in coming here?"
    menu:
        cS "Tell me truthfully, Moze. What was your plan in coming here?"
        "I came for MAC.":
            mS "I came for MAC."
            mS "I'm not leaving without him."
            "Coil sighs."
            cS "I assumed that was the case."
            cS "I'm disappointed. After everything that happened, you couldn't just walk away."
            cS "MAC is gone."
            amaS "Bullshit."
            amaS "If that were true you wouldn't still be here."
        "I came to help.":
            mS "I came to help, to fight off BigCorp."
            "Coil tilts his head, as if inspecting me."
            cS "Help?"
            cS "I think we've had enough of your \"help.\""
            cS "You had to come back and visit more destruction upon us."
            if vig4_killDflies == True:
                cS "You killed my men because you wanted to, didn't you?"
                cS "You never even thought about helping us."
            else:
                cS "And is this why you've brought this hunter?"
                "He gestures at Ama."
                cS "This \"Deadeye.\""
                amaS "Good to know the name means something all the way out here."
                cS "It means a half-life. A ghost who has no place in this galaxy anymore."
                amaS "I'll show you what this ghost is capable of."
                cS "I'm sure you will."
            cS "Is this what your help means, Moze?"
    "Ama suddenly draws her rifle and aims at Coil."
    menu:
        "Ama suddenly draws her rifle and aims at Coil."
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




#####Attacking Polaris without Ama #######region 





label vig4_sc6_attack_1():
    show vig1_town_stream onlayer background with dissolve
    hide targetbase_stream
    "Polaris burns."
    "The dull roar of battle echoes in the distance."
    "We make our way quickly down the clear street, hopping between pieces of cover as we do so."
    "No danger on the roofs."
    "No enemies on the street."
    "In the distance, the sounds of battle start to quiet."
    show teresa stream shock at stream_right with dissolve
    enS "Shit, patrol, get down!"
    hide jennica with dissolve
    hide teresa with dissolve
    "The four of us dive over the rubble of the building and and crouch behind the ruined stones."
    "A low hum gets closer, muddying the sound of several voices."
    "One breaks through, shouting."
    enforcer "Halt! Halt I said!"
    show bc_enforcer at stream_center with dissolve
    "I peek over the ruins."
    "A battalion of two dozen BC enforcers surround a crowd of hostage Dragonfly soldiers."
    "Behind them, the source of the rumbling: an immense hover tank, laborious engine purring over the sounds of warfare."
    enforcer "Alright, you heard the orders." 
    enforcer "Tank squadron locks this sector down and the rest of you are with me."
    enforcer "Once the next assault begins, we hit those Dragonflies with full force."
    "He glares over the captives."
    enforcer "And our new friends here are going to help us \"convince\" them they should surrender."
    enforcer "Remember: if you see a droid, don't shoot it. BigCorp wants it in safe custody {i}undamaged{/i}."
    enforcer "Kill everyone else."
    hide bc_enforcer with dissolve
    show jennica stream angry at stream_left with dissolve
    pS "Bastard."
    show teresa stream neutral at stream_right with dissolve
    enS "Position looks bad. We can't leave here without exposing ourselves."
    "My eye catches the tank."
    "There aren't that many enforers watching it. Most are focused on the captives."
    mS "We could go for the tank."
    pS "What!?"
    enS "And I thought I suggested the bold moves."
    mS "Their guards are lax, too focused on the captives."
    pS "Sure, but we still can't take a whole battalion on our own."
    enS "We could wait for that group to leave, then take out the crew."
    pS "No way, if we're doing this then we should help those people."
    enS "Wait a minute, look at that guy!"
    show customs agent at stream_center with dissolve
    "Teresa points at one of the captive Dragonflies."
    enS "Isn't that?"
    pS "Oh yeah! That's the bastard who roughed us up at the festival."
    enS "Guess he and his squad were more talk than bite after all."
    pS "They're still hostages. We should help them."
    hide customs agent with dissolve
    enS "What's the call, Captain?"
    menu:
        enS "What's the call, Captain?"
        "We're saving the hostages first.":
            jump vig4_sc6_attack_1_assault
        "Wait for the group to split.":
            jump vig4_sc6_attack_1_split

label vig4_sc6_attack_1_assault():
    mS "Jennica's right. We can't let BC hold those hostages."
    mS "We take the tank, but we're also not letting this battalion get away."
    pS "Thanks, Cap."
    mS "Jennica, Teresa, take care of the tank. I'll distract the battalion."
    enS "Affirmative."
    pS "Be careful, Cap."
    hide jennica with dissolve
    hide teresa with dissolve
    "Teresa and Jennica shift position around the rubble while I move further away from them."
    enforcer "Alright you maggots, break time's over. Time to get moving."
    "It's now or never."
    menu:
        "It's now or never."
        "Open Fire.":
            pass
    mS "Now!"
    play audio "lazer.wav"
    "I pop out of cover and fire two quick shots, landing them directly into the backs of two enforcers."
    play audio "lazer.wav"
    show bc_enforcer at stream_center with dissolve
    "Jennica and Teresa stay in cover and shift along the side of the rubble."
    "There's a moment of pause before the rain of blaster fire hits my position."
    "I hear the tank rumble as it shifts its position. The sound of a shot charging resonates from its chamber."
    "I rush out of cover, leaping over the rubble as the tank's blast erupts."
    "The explosion propels me through the air."
    "Landing in the dirt, I roll quickly as blaster bolts thud into the ground where I was just a moment before."
    "I slam my back into another piece of ruined building."
    "As I do so, I watch Jennica and Teresa scramble up the back of the unguarded tank."
    "The enforcers are all focused on me."
    "They don't even notice as Teresa stabs something into its top hatch." 
    "The cannon begins to charge again, but Jennica grabs it and drags it to aim at a group of nearby enforcers"
    "The shot fires, sending the enforcers flying into the air as the top hatch of the tank pops open."
    "Amdist the chaos, the Dragonflies have dispersed."
    "Some ran into the shelter of buildings while others have started brawling with BC goons."
    "Teresa and Jennica drag some goons out of the hatch."
    "Jennica scrambles inside while Teresa makes quick work of them with her pistol."
    "Some of the BC troops are retreating back to the tank, but the bulk of them advance on my position."
    menu:
        "Some of the BC troops are retreating back to the tank, but the bulk of them advance on my position."
        "Use smoke as a distraction.":
            "I pull a smoke grenade from my pocket and quickly throw it to the ground."
            "Smoke billows all around me as the battalion stalls in the stret, unsure of what to do."
            "I dive out of the smoke towards other cover, landing a couple of shots in an enforcer as I do so."
        "Fire back and move to cover.":
            "I whip around the cover, firing shots into an enforcer's chest before dropping back into a new position."
    "The Dragonflies have converged on the bulk of the battalion, striking them with stones they picked up from the ground."
    "The enforcers' attention has shifted away from me."
    "I start to move toward the fighting."
    enforcer "Freeze!"
    "An enforcer is behind me. He taps my back with his gun."
    enforcer "Tell your crew to stand down!"
    play audio "lazer.wav"
    hide bc_enforcer with dissolve
    "The enforcer goes silent. I hear his body fall to the ground."
    "Whipping around, I don't see anyone around me."
    "Jennica and Teresa have fully taken over the tank, and the people of Polaris have routed the battalion."
    "A shadow moves."
    "Faintly, on a rooftop in the distance, silhouetted by fire, a dark figure drops from a building to the ground."
    "And vanishes."
    dflyGuard "Captain Moze?"
    show customs agent at stream_center with dissolve
    "The leader of the Dragonflies squad approaches me."
    dflyGuard "We thought we were dead."
    "He glances at the bodies in the street."
    dflyGuard "We didn't all make it, but you gave us a chance to fight back."
    dflyGuard "I know we didn't leave on the best of terms. But, thank you for saving us."
    menu:
        dflyGuard "I know we didn't leave on the best of terms. But, thank you for saving us."
        "You were just doing your job.":
            mS "You were just doing your job. I understand what that's like."
            dflyGuard "I appreciate your understanding."
            dflyGuard "Will you join us to defend the plaza?"
            mS "We have business elsewhere."
            "The Dragonfly guard looks from me to the tank."
            "He's about to say something, then thinks better of it."
            dflyGuard "Of course."
            dflyGuard "Good luck, Captain."
            "He turns and rejoins his comrades. Together, they walk down the street toward the plaza."
            hide customs agent with dissolve
        "It wasn't about you.":
            mS "You're welcome, but it wasn't about you."
            mS "I deprived BC of strategic leverage."
            "He looks taken aback."
            dflyGuard "Ah, I see."
            dflyGuard "Will you join us to defend the plaza?"
            mS "We have business elsewhere."
            "The Dragonfly guard looks from me to the tank."
            "He's about to say something, then thinks better of it."
            dflyGuard "Of course."
            dflyGuard "Good luck, Captain."
            "He turns and rejoins his comrades. Together, they walk down the street toward the plaza."
            hide customs agent with dissolve
        "I wanted to kill you myself.":
            $ vig4_killDflies = True
            mS "Don't thank me. I just wanted the pleasure of killing you myself."
            play audio "lazer.wav"
            hide customs agent with Dissolve(0.5)
            "The guard has half a second to look stunned before a blaster bolt rips through his skull."
            "The rest of the Dragonflies look up, confusion rampant on their faces as I draw my weapon."
            play audio "lazer.wav"
            "Six blaster shots echo in the night."
            "Each of the Dragonflies drops to the ground. Dead."
    "I turn my back on the quiet street, and stride toward the tank."
    jump vig4_sc6_attack_2

label vig4_sc6_attack_1_split():
    mS "Teresa's right, if we're going to do this we have to do it smart."
    mS "We'll wait for the battalion to split off, then take the tank when it's just a skeleton crew."
    mS "Jennica and Teresa, take care of the tank. I'll distract what's left of the squad."
    enS "Behind you."
    pS "I don't like it, but we'll get it done."
    mS "Get in position."
    hide teresa with dissolve
    hide jennica with dissolve
    "Staying in cover, Jennica and Teresa cycle around the rubble, getting as close to the tank as possible without revealing themselves."
    "I shift down the cover, moving away from the tank."
    enforcer "Alright you maggots, break time's over. Time to get moving."
    "The sound of dozens of steps as the battalion moves off down the road."
    "Slowly, but surely, they turn the corner. Disappearing out of sight and earshot."
    "I chance a glance over the rubble."
    show bc_enforcer at stream_center with dissolve
    "There's just six BC enforcers standing next to the tank."
    "It's now or never."
    menu:
        "It's now or never."
        "Fire.":
            pass
    play audio "lazer.wav"
    "Whipping around the cover, I take aim and fire two quick shots."
    play audio "lazer.wav"
    "Two BC enforcers drop dead as the rest scramble for cover."
    "I rush to a piece of cover opposite the tank, drawing the enforcers' attention as their bullets cascade by me."
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
    "The second his head peeks up, I blast his skull with a bolt."
    hide bc_enforcer with dissolve
    "He drops dead."
    "A simple maneuver."
    "Holstering my blaster, watch Jennica and Teresa climb inside the tank and survey the bodies on the ground."
    "One, two, three, four, five..."
    "Where's the sixth?"
    enforcer "Freeze!"
    "An enforcer taps my back with his gun."
    enforcer "Tell your crew to stand down!"
    mS "Easy."
    enforcer "I'm giving the orders here!"
    play audio "lazer.wav"
    hide bc_enforcer with dissolve
    "The enforcer goes silent. I hear his body fall to the ground."
    "Whipping around, I don't see anyone around me."
    "A shadow moves."
    "Faintly, on a rooftop in the distance, silhouetted by fire, a dark figure drops from a building to the ground."
    "And vanishes."
    enS "Hey, captain?"
    "I whip around, drawing my pistol."
    show teresa stream shock at stream_center with dissolve
    "The barrel of my blaster points directly at Teresa's forehead."
    "Woah woah, easy."
    "I exhale deeply and holster my gun."
    mS "Sorry, Resa. That was..."
    show teresa stream neutral
    enS "Are you okay?"
    menu:
        enS "Are you okay?"
        "I thought I saw something.":
            mS "Yeah, I'm okay."
            mS "But I thought I saw someone."
            enS "Who?"
            mS "I don't know. Someone shot an enforcer that had me dead to rights."
            "I gesture toward the buildings in the distance."
            "Teresa looks down the street."
            enS "A Dragonfly sniper, maybe?"
            mS "Maybe."
            enS "At least you're safe."
            enS "Shall we, inspect the vessel we just comandeered?"
        "Yeah, I'm good.":
            mS "Yeah, yeah, I'm good."
            enS "Okay, glad to hear it..."
            enS "Shall we, inspect the vessel we just comandeered?"
    mS "Yeah, let's go."
    hide teresa with dissolve
    jump vig4_sc6_attack_2

label vig4_sc6_attack_2():
    show jennica stream neutral at stream_left with dissolve
    "As I climb in through the tank's hatch, Jennica is already sitting in a chair near the front."
    "She's examining a string of buttons and sticks in front of her."
    mS "Any idea how to drive this thing, Jenn?"
    pS "Sure, Cap, doesn't look too complex. We'll just have to work as a team."
    pS "I'll take maneuvering. Teresa, take care of our shields and engine power."
    pS "You can also reach over and use those machine guns if we need them."
    show teresa stream neutral at stream_right with dissolve
    enS "Makes sense."
    pS "Cap, you stay in the center, be our spotter and control the main cannon."
    pS "You can also fire the main cannon from the side there."
    mS "Roger, let's roll out."
    pS "Aye aye."
    play audio "callRing.wav"
    "As Jennica goes to move the tank forward, a ring suddenly echoes in the tank."
    enS "Someone is calling us."
    pS "On a BigCorp frequency?"
    enS "No. It's not BigCorp, but it has access to their comms?"
    "Access to BigCorp tech? Not affiliated with them?"
    mS "Answer it!"
    "Teresa inputs something into a screen on her side."
    "At the front of the tank, a blue hologram slowly starts to take shape."
    show mac stream neutral at stream_center_mac with dissolve
    "It's MAC."
    mS "MAC!"
    pS "Hey, little guy!"
    enS "Good to see you, MAC."
    macS "Captain? Moze? I expected it was you. Stealing a tank is very much your style."
    menu:
        macS "Captain? Moze? I expected it was you. Stealing a tank is very much your style."
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
    macS "But Coil has brought me into the plaza tower and away from the fighting."
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
    cS "That's enough, MAC."
    play audio "cutCall.wav"
    hide mac with dissolve
    "The signal is cut short."
    enS "That was Coil's voice."
    pS "No doubt. So he has our boy at the top of the tower."
    enS "The barricades they have set up around the plaza will be a bit of trouble, but we can handle them."
    mS "We won't have to on our own."
    pS "Cap?"
    mS "That enforcer said BC was preparing a second assault. This first one must have just been to soften up Polaris's defenses."
    mS "When BC launches their next attack, we can use the chaos to break through and get into the tower."
    enS "Efficient and clever."
    pS "A lot of people are going to die. But I guess that's unavoidable at this point."
    mS "As long as we get MAC. That's what matters."
    "As I finish speaking, a siren rings out from Polaris's plaza."
    "I peer through the tank's scope at the Cruiser hovering in the night sky."
    "A line of dropships have begun careening through the air to Polaris."
    mS "The second attack is starting. Jenn, take us toward the plaza."
    "The tank accelerates as Jennica shifts the sticks in front of her forward."
    "We glide smoothly over the ground as a calm before the storm settles over Polaris."
    hide jennica with dissolve
    hide teresa with dissolve
    jump vig4_sc6_attack_3

label vig4_sc6_attack_3():
    "Smoke billows all around us as we navigate Polaris's ruined roads."
    "Flames lick at the sides of buildings."
    "Even in the tank, we can feel the heat from outside."
    "The sounds of battle have struck up again. And they get louder with each second we advance."
    mS "Everyone, get ready."
    "We turn onto the main street."
    "Chaos erupts."
    "A dropship screeches by overhead, turrets strafing positions defended by Dragonflies."
    "The Dragonflies have consolidated their defenses behind an enormous barricade blocking the main street into the plaza."
    "A swarm of BC enforcers march down the street."
    "Blaster fire streaks in both directions."
    "As we emerge onto the street, the BC forces suddenly cheer."
    pS "They think we're on their side."
    enS "We are in their tech."
    pS "What's the play, Cap?"
    menu:
        pS "What's the play, Cap?"
        "Pretend to be with BigCorp, attack the Dragonflies.":
            $ vig4_killDflies = True
            mS "Keep our weapons aimed at the Dragonfly position."
            mS "Jennica, get us there as quick as you can without being suspcious."
            pS "Roger, Cap."
            "The tank advances on the barricade."
            "Shots from the Dragonflies start to rattle against our hull."
            enS "Shields are at 95\%."
            mS "Good. Teresa, use that machine gun. Hit any Dragonflies that look like threats."
            enS "Roger!"
            "Teresa grabs the machine gun controls and aims for the Dragonfly squads positioned on nearby rooftops."
            "The rapid fire of the machine gun tears into the squads, sending them into a retreat."
            show vig1_town_stream with hpunch
            "A grenade explodes next to us, engulfing some BC enforcers in flames and shaking our hull."
            enS "Tough hit but shields are still at 85\% and holding."
            "I grip the cannon controls and point at a squad of Dragonflies huddled behind nearby cover."
            "The whole tank thrums with energy as the cannon charges."
            "A beam of blue light bursts from the cannon, striking through the rubble."
            "A pillar of flame erupts into the air where the cannon impacted the ground."
            "There's no evidence of the Dragonflies who were hiding behind cover."
            mS "Jenn, keep us moving."
            "We're slowly advancing toward the head of the BC army."
            "Teresa's fire with the machine guns have forced almost all of the Dragonflies into cover."
            "A group tries to take shots at us from a rooftop."
            "I aim the cannon at the base of the building."
            "The thrum of energy."
            "The blue light."
            "Another pillar of flame and the memory of human presence."
            "We keep advancing."
            enS "Contact on the rooftops!"
            show vig1_town_stream with hpunch
            "Another detonation on the side of the tank."
            "I whip a monitor around to view the assailants."
            "It's a group of Dragonflies armed with rocket launchers a couple of buildings away from us."
            "They're reloading the launchers and preparing for another volley."
            mS "Teresa, take them down!"
            enS "I'm trying!"
            "Teresa aims the machine gun at the direction of the squad and begins firing, but too late."
            show vig1_town_stream with hpunch
            "Another rocket streaks through the air and collides with us just as the bolts from the machine gun rip into their bodies."
            mS "Resa, how're we doing?"
            enS "Bad hits. We're at 40\% shields, but holding. We can't take many more of those."
            pS "Cap! We're almost at the barricade!"
            "I turn to look ahead."
            "She's right, we're closing in."
            mS "Alright, Resa, direct our power into engine thrusts and tell me when it's ready to go. We're going to ram through it."
            enS "Are you sure that's--"
            mS "Just do it!"
            mS "Jenn, hit the thurst forward. Hard!"
            pS "Aye aye, Cap!" 
            "The main cannon charges. Our engines hum with excitement."
            enS "Ready, captain!"
            mS "Launch!"
            "Fire erupts from the cannon at the same time as we rush forward."
            "The barricade shatters as the cannon's blast collides with it."
            "Our shields sparkle, the tank ramming into the wall and splitting it apart."
        "Attack BigCorp, rush the barricade.":
            mS "No. BigCorp is still the enemy."
            mS "Jenn, get us to that barricade as fast as you can."
            pS "Aye!"
            enS "Our shields are at 95\% currently!"
            mS "Good. Resa, open fire on any BC goons you see."
            enS "Roger!"
            "Teresa grabs the machine gun controls and aims for the enforcers at the frontline."
            "As the tank accelerates forward, confusion spreads throughout the BC army, throwing them into disarray."
            "Our shields continue to take hits from both sides as blaster fire rattles against our hull."
            show vig1_town_stream with hpunch
            "A grenade explodes at our side, shaking the tank slightly."
            enS "Shields are at 80\%. We're taking a lot of hits."
            "A dropship begins to aim down toward us."
            mS "We can dish them out too."
            "I grip the controls for the main cannon."
            "The whole tank thrums with energy as the cannon charges."
            "A beam of blue light bursts from the cannon, striking the dropship out of the sky."
            "The ship explodes in a fireball as wreckage falls into Polaris, crashing into the BC swarm."
            mS "Jenn, how are we doing?"
            pS "We're close, just a bit further!"
            enS "Captain, we're starting to take less fire from the Dragonflies."
            show vig1_town_stream with hpunch
            "Another detonation on the side of the tank."
            "I whip a monitor around to view the assailants."
            "It's a group of BC enforcers armed with rocket launchers." 
            "They're on a building near the back of the attack force."
            "They're reloading the launchers and preparing for another volley."
            "I whip the main cannon controls around, aiming them at the base of the building."
            "The cannon charges."
            "The rocket streaks through the air."
            "The beam of blue light strikes the building as another pillar of flame erupts into the night air."
            show vig1_town_stream with hpunch
            "The rocket detonates close to us, but not a direct hit."
            enS "Shields are at 60\%."
            pS "Cap! We're almost at the barricade!"
            "I turn to look ahead."
            "She's right, we're closing in."
            mS "Alright, Resa, direct our power into engine thrusts and tell me when it's ready to go. We're going to ram through it."
            enS "Are you sure that's--"
            mS "Just do it!"
            mS "Jenn, hit the thurst forward. Hard!"
            pS "Aye aye, Cap!" 
            "The main cannon charges. Our engines hum with excitement."
            enS "Ready, captain!"
            mS "Launch!"
            "Fire erupts from the cannon at the same time as we rush forward."
            "The barricade shatters as the cannon's blast collides with it."
            "Our shields sparkle, the tank ramming into the wall and splitting it apart."
        "Attack both Dragonflies and BigCorp.":
            $ vig4_killDflies = True
            mS "Screw it." 
            mS "Jenn, get us to that barricade as fast as you can."
            pS "Aye!"
            enS "Our shields are at 95\% currently!"
            mS "Good. Resa, open fire at will."
            enS "Roger!"
            "Teresa grabs the machine gun controls and whips it around."
            "The bolts of machine gun rounds tear into soliders: BC enforcers and Dragonflies alike."
            "Teresa lays on the trigger hard, striking Dragonflies on the rooftops, then BC enforcers on the ground."
            "Confusion spreads through both sides as blaster fire pings off the tank's sides."
            enS "Shields are at 90\%, Captain."
            "I grip the controls for the main cannon. The entire tank thrums with energy as it charges."
            show vig1_town_stream with hpunch
            "Above, a dropship aims down toward our position, turrets sending fire against our hull."
            "A beam of blue light bursts from the cannon, striking the dropship out of the sky."
            "The ship explodes in a fireball as wreckage falls into Polaris, crashing into the BC swarm."
            mS "Jenn, how are we doing?"
            pS "We're close, just a bit further!"
            show vig1_town_stream with hpunch
            "An explosion suddenly detonates against our side."
            mS "Teresa, report!"
            "I whip the monitor around, looking for the assailants."
            enS "Shields are down to 60\%. We're taking fire from both sides and losing energy rapidlly!"
            "I locate the smoke streaking through the air."
            "Dragonflies on a nearby building are loading rocket launchers."
            "I drop the cannon to aim at the base of the building, charging up another blast."
            "But I'm too late."
            "A bright flashing rocket streaks toward us just as I fire the cannon."
            show vig1_town_stream with hpunch
            "The rocket impacts on our side, but at the same time, the tank's blast detonates on the building."
            "A pillar of flame erupts into the sky as the edifice crumbles to the ground."
            pS "They're throwing grenades!"
            "Teresa fires the machine gun full auto as BC enforcers break ranks to move toward our position."
            "Most of them are cut down, but a couple are able to lob grenades that land at our side."
            show vig1_town_stream with hpunch
            "They detonate, jostling the vehicle."
            enS "Shields are down to 30\%! We can't take much more of this!"
            pS "Cap! We're almost at the barricade!"
            "I turn to look ahead."
            "She's right, we're closing in."
            mS "Alright, Resa, direct our power into engine thrusts and tell me when it's ready to go. We're going to ram through it."
            enS "Are you sure that's--"
            mS "Just do it!"
            mS "Jenn, hit the thurst forward. Hard!"
            pS "Aye aye, Cap!" 
            "The main cannon charges. Our engines hum with excitement."
            enS "Ready, captain!"
            mS "Launch!"
            "Fire erupts from the cannon at the same time as we rush forward."
            "The barricade shatters as the cannon's blast collides with it."
            "Our shields sparkle, the tank ramming into the wall and splitting it apart."
    "The tank rushes into the plaza as Jennica slams the controls to the side, and we go almost completely sideways."
    "The tank isn't supposed to go this fast. And it's not supposed to turn this hard."
    "But Jennica wrangles it under control as we careen to a stop at the base of the tower."
    "I open the top hatch and scramble out."
    "The barricade at the end of the plaza begins to crumble as the Dragonflies disperse."
    "BC closes in on the plaza."
    "More dropships stream down from the cruiser."
    "We don't have much time."
    "War has come."
    menu:
        "War has come."
        "This is it.":
            mS "This is it. The end of the road."
        "We're not making it out of this.":
            mS "I don't know if I see a way out of this."
    mS "This is where our score gets settled."
    "I watch the burning horizon as Polaris crumbles."
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
        show reginald stream bigmad at stream_center with dissolve
        goon "I really don't get paid enough for this shit."
        show jennica stream shock at stream_left with dissolve
        pS "Reginald!?"
        goon "Matticus sends his regards."
        goon "Said he had a debt that needed paying off."
        show jennica stream neutral
        "The swarm of attack ships engage the BC dropships, delaying their advance."
        goon "So take care of whatever you got to do on the ground. We'll handle the air shit."
        menu:
            goon "So take care of whatever you got to do on the ground. We'll handle the air shit."
            "Thank you.":
                mS "Reginald...thank you."
                goon "Now don't go getting soft on me."
                goon "You just do your job and I'll do mine."
                goon "Even though it's a massive pain."
                mS "Copy that."
            "Affirmative.":
                mS "Copy that."
        hide reginald with dissolve
    #if vig3_marshalChoice == True:
    else:
        show jennica stream neutral at stream_left with dissolve
    pS "Cap, you're gonna want to move." 
    mS "Not without you two."
    show teresa stream neutral at stream_center with dissolve
    enS "Negative, Captain."
    mS "What!?"
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
                "Jennica suddenly comes up from the tank. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                pS "Go do what you do best, Moze."
            elif teresaRomance == True:
                "Teresa suddenly comes up from the tank. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                show teresa stream happy
                enS "Go do what you do best, Moze."                
            else:
                pass
        "Thank you.":
            mS "Jenn, Resa, I--"
            if jennicaRomance == True:
                "Jennica suddenly comes up from the tank. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                pS "Go do what you do best, Moze."
            elif teresaRomance == True:
                "Teresa suddenly comes up from the tank. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                show teresa stream happy
                enS "Go do what you do best, Moze."                
            else:
                pass
            mS "Thank you. And be careful. I want a clean escape route when I come down with MAC."
            pS "You betcha."
            enS "Affirmative."
    hide jennica with dissolve
    hide teresa with dissolve
    "I hop down to the ground and rush toward the tower's tall doors."
    "Behind me, I hear the shouts of BC enforcers as they pour into the plaza, the echo of blaster fire."
    "And the warm vibration of a tank's cannon charging up to full power."
    jump vig4_sc7_1_attack

label vig4_sc7_1_attack():
    hide vig1_town_stream with dissolve
    "As soon as the doors close behind me, the sounds of battle become muffled."
    "The tower is utterly silent."
    "A distant voice calls from up above."
    cS "Up here. Come along."
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
    "There's a wide room in front of me, and two voices shouting within."
    "I step across the threshold into a wide room."
    show vig2_datacenter_stream onlayer background with dissolve
    show coil at stream_left with dissolve
    "Coil stands in the center, in front of a massive computer console."
    cS "Well, you made it."
    if vig4_killDflies == True:
        cS "You had to murder some good people to do it. But you arrived."
    else:
        pass
    "Coil turns to face us. His face looks haggard, his eyes bloodshot."
    menu:
        "Coil turns to face us. His face looks haggard, his eyes bloodshot."
        "Where is MAC?":
            mS "Where is MAC?"
            cS "Always so direct."
            cS "MAC is no longer any of your concern, Moze."
            cS "You delivered him, he is our responsibility."
            cS "And he is safe."
            if macViolence > macPeace:
                cS "You know he insisted on operating a turret when BigCorp arrived."
                cS "Said he would \"make those BC scum pay.\""
                mS "Operating a turret on the frontlines. Is that really what you consider \"safe\"?"
                cS "No. But he insisted."
                cS "And as I'm sure you're aware, he can be quite strong-willed."
                cS "He got it from you after all."
                amaS "Mozely can be quite stubborn."
                show ama at stream_right with dissolve
                "I whip around."
                "Ama steps into the wide room, rifle drawn, aimed directly at Coil."
                cS "I meant the bloodlust."
                "Ama tilts her head."
                amaS "That too."
            else:
                cS "You know he insisted on providing first aid to the people who were first injured by BigCorp's assault."
                cS "Said he had to \"take care of the people around him.\""
                mS "Being a frontline medic isn't exactly what I would consider \"safe.\""
                cS "No. But he insisted." 
                cS "And I'm sure you're aware he can be quite strong-willed."
                cS "He got it from you after all."
                amaS "Mozely can be quite stubborn."
                show ama at stream_right with dissolve
                "I whip around."
                "Ama steps into the wide room, rifle drawn, aimed directly at Coil."
                cS "I meant the altruistic urge to help other people."
                "Ama tilts her head."
                amaS "Guess that has been a phase recently."
        "Got a plan for getting out of this?":
            mS "So, do you have a plan for getting out of this."
            cS "I do."
            cS "The top of this tower can be converted into a makeshift rocket."
            cS "We will be able to finish the mission, where you failed."
            mS "And you're okay with all of Polaris dying while you escape?"
            cS "It breaks my heart."
            cS "But we have done what we could. What we were supposed to do."
            cS "MAC is no longer any of your concern, Moze."
            cS "You delivered him, he is our responsibility."
            if macViolence > macPeace:
                cS "You know he insisted on operating a turret when BigCorp arrived."
                cS "Said he would \"make those BC scum pay.\""
                mS "Operating a turret on the frontlines. Is that really what you consider \"safe\"?"
                cS "No. But he insisted."
                cS "And as I'm sure you're aware, he can be quite strong-willed."
                cS "He got it from you after all."
                amaS "Mozely can be quite stubborn."
                show ama at stream_right with dissolve
                "I whip around."
                "Ama steps into the wide room, rifle drawn, aimed directly at Coil."
                cS "I meant the bloodlust."
                "Ama tilts her head."
                amaS "That too."
            else:
                cS "You know he insisted on providing first aid to the people who were first injured by BigCorp's assault."
                cS "Said he had to \"take care of the people around him.\""
                mS "Being a frontline medic isn't exactly what I would consider \"safe.\""
                cS "No. But he insisted." 
                cS "And I'm sure you're aware he can be quite strong-willed."
                cS "He got it from you after all."
                show ama at stream_right with dissolve
                "I whip around."
                "Ama steps into the wide room, rifle drawn, aimed directly at Coil."
                amaS "Mozely can be quite stubborn."
                cS "I meant the altruistic urge to help other people."
                "Ama tilts her head."
                amaS "Guess that has been a phase recently."
    "Ama turns her gaze on me."
    amaS "Hello Mozely, it's good to see you again."
    amaS "I suppose I should thank you for leading me here."
    menu:
        amaS "I suppose I should thank you for leading me here."
        "You're a bad hunter.":
            mS "You did always need my help to get anything done."      
        "Was wondering when you would show up.":
            mS "I was wondering when you would show up."
            mS "Slower than I expected."
    amaS "Watch your tongue, kid."   
    amaS "I'm calling the shots here." 
    cS "So you think."
    "Ama trains her gaze back on Coil as he steps away from the device and in front of me and Ama." 
    cS "Tell me truthfully, Moze. What was your plan in coming here?"
    menu:
        cS "Tell me truthfully, Moze. What was your plan in coming here?"
        "I came for MAC.":
            mS "I came for MAC."
            mS "I'm not leaving without him."
            "Coil sighs."
            cS "I assumed that was the case."
            cS "I'm disappointed. After everything that happened, you couldn't just walk away."
            cS "MAC is gone."
            amaS "Bullshit."
            amaS "If that were true you wouldn't still be here."
            cS "How perceptive. And yet you still have no idea what you're doing."
            cS "Flailing around in the darkness with no purpose."
        "I came to help.":
            mS "I came to help, to fight off BigCorp."
            "Coil tilts his head, as if inspecting me."
            cS "Help?"
            cS "I think we've had enough of your \"help.\""
            cS "You had to come back and visit more destruction upon us."
            if vig4_killDflies == True:
                cS "You killed my men because you wanted to, didn't you?"
                cS "You never even thought about helping us."
            else:
                cS "But it's always so hard to know with you, isn't it, Moze."
                cS "Here we stand, in the midst of a war. And you happen to be at the center of it."
            cS "Is this what your help means, Moze?"
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