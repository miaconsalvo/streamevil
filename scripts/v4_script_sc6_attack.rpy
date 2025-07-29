####This script contains the code for the Polaris Attack routes of Vignette 4 up until Moze makes her choice about siding with Coil and Ama

###Attacking Polaris with Ama
label vig4_sc6_attack_1_ama():
    show vig1_town_stream onlayer background with dissolve
    hide targetbase_stream
    "Polaris burns."
    $ viewCount += 1
    $ AddChatter(vig4_sc6_attack_1_ama_comment1)
    "The dull roar of battle echoes in the distance as we navigate the town's outskirts."
    $ AddChatter(vig4_sc6_attack_1_ama_comment2)
    "No enemies on the street. No danger on the roofs."
    "We make our way quickly down the clear street, hopping between pieces of cover as we do so."
    show teresa stream shock at stream_right with dissolve
    enS "Shit, patrol, get down!"
    $ AddChatter(vig4_sc6_attack_1_ama_comment3)
    hide teresa with dissolve
    $ vig4_sc6_attack_1_ama_comment1.click = False
    "The four of us dive over the rubble of a nearby building and crouch behind the ruined stones."
    "A low rumble gets closer, muddying the sound of several voices."
    $ AddChatter(vig4_sc6_attack_1_ama_comment4)
    "One breaks through, shouting."
    $ AddChatter(vig4_sc6_attack_1_ama_comment5)
    enforcer "Halt! Halt I said!"
    show bc_enforcer at stream_center with dissolve
    "I peek over the ruins."
    "A battalion of two dozen BC enforcers surround a crowd of hostage Dragonfly soldiers."
    "Behind them, the source of the rumbling: an immense hover tank, laborious engine purring over the sounds of warfare."
    enforcer "Alright, you heard the orders." 
    enforcer "Tank squadron locks this sector down. The rest of you are with me."
    enforcer "Once the next assault begins, we hit those Dragonflies with full force."
    "He glares over the captives."
    enforcer "And our new friends here are going to help us \"convince\" them they should surrender."
    enforcer "Remember: if you see a droid, don't shoot it. BigCorp wants it in safe custody {i}undamaged{/i}."
    enforcer "Kill everyone else."
    $ AddChatter(vig4_sc6_attack_1_ama_comment6)
    hide bc_enforcer with dissolve
    show jennica stream angry at stream_left with dissolve
    pS "Bastard."
    show teresa stream neutral at stream_right with dissolve
    enS "Position looks bad. We can't leave here without exposing ourselves."
    show ama stream neutral at stream_left5 with dissolve
    amaS "You're thinking too small."
    $ AddChatter(vig4_sc6_attack_1_ama_comment7)
    "Ama points at the hover tank."
    amaS "We take that, we don't have to worry about hiding and cover anymore."
    $ AddChatter(vig4_sc6_attack_1_ama_comment8)
    menu:
        amaS "We take that, we don't have to worry about hiding and cover anymore."
        "You can't be serious.":
            mS "You can't be serious, Ama."
            amaS "Think about it, we get more firepower, safety from enemy fire."
            amaS "Who's going to be able to stop us?"
            amaS "I think it's genius."
            $ AddChatter(vig4_sc6_attack_1_ama_comment9)
        "Genius.":
            mS "Genius idea."
            $ AddChatter(vig4_sc6_attack_1_ama_comment9)
    enS "I don't know if I'd go that far."
    pS "We still have to steal the damn thing."
    amaS "Simple, wait for that group to wander off, then take out the crew. Easy maneuver."
    $ AddChatter(vig4_sc6_attack_1_ama_comment10)
    pS "No way, if we're doing this then we should help those people."
    enS "Wait a minute, look at that guy!"
    show dflyGuard at stream_right5 with dissolve
    "Teresa points at one of the captive Dragonflies."
    enS "Isn't that?"
    pS "Oh yeah! That's the guy who roughed us up at the festival."
    $ AddChatter(vig4_sc6_attack_1_ama_comment11)
    enS "Guess he and his squad were more bark than bite after all."
    $ AddChatter(vig4_sc6_attack_1_ama_comment12)
    pS "They're still hostages. We should help them."
    $ AddChatter(vig4_sc6_attack_1_ama_comment13)
    hide dflyGuard with dissolve
    amaS "Well, Mozely, what's the call?"
    $ AddChatter(vig4_sc6_attack_1_ama_comment14)
    menu:
        amaS "Well, Mozely, what's the call?"
        "We're saving the hostages.":
            #$ deadeyeApproval -= 1 ##Do we want to make it hard to romance Ama?
            $ csEngagement += 2
            $ kcEngagement += 1
            $ pdEngagement -= 1
            $ marshal += 1
            jump vig4_sc6_attack_1_assault_ama
        "Wait for the group to split.":
            $ deadeyeApproval += 1
            $ csEngagement -= 1
            $ kcEngagement -= 1
            $ pdEngagement += 2
            $ outlaw += 1
            jump vig4_sc6_attack_1_split_ama

label vig4_sc6_attack_1_assault_ama():
    mS "Jennica's right. We can't let BC hold those hostages."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment1)
    pause 0.5
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment2)
    mS "We take the tank, but we're also not letting this battalion get away."
    pS "Thanks, Cap."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment3)
    mS "Jennica and Teresa, take care of the tank. Ama, we'll take the battalion."
    "Ama sighs and hoists her rifle into her shoulder."
    amaS "You're lucky I'll be well paid after this mess."
    enS "You'll be lucky to get anything out of this, Reyes."
    mS "Enough, get in position."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment4)
    hide jennica with dissolve
    hide teresa with dissolve
    "Staying in cover, Jennica and Teresa cycle around the rubble, getting as close to the tank as possible without revealing themselves."
    show ama at stream_left with move
    "Ama and I shift down the ruins, moving away from the tank." 
    "The battalion is about to move on."
    show bc_enforcer at stream_center with dissolve
    enforcer "Alright you maggots, break time's over. Time to get moving."
    "It's now or never."
    menu:
        "It's now or never."
        "Open Fire.":
            pass
    mS "Now!"
    play audio "lazer.wav"
    "I pop out of cover and fire two quick shots, landing them directly into the backs of two enforcers."
    if vig4_nickName_bool == True:
        $ AddChatter(vig4_sc6_attack_1_assault_ama_comment5)
    else:
        $ AddChatter(vig4_sc6_attack_1_assault_ama_comment6)
    play audio "lazer.wav"
    "Ama does the same, taking out the lead enforcer, while Jennica and Teresa stay in cover and shift along the side of the rubble."
    "There's a moment of pause before the rain of blaster fire hits mine and Ama's position."
    amaS "Hope this isn't suicide, Mozely."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment7)
    "I hear the tank rumble as it shifts its position. The sound of a shot charging resonates from its chamber."
    mS "Just follow my lead."
    "I rush out of cover, leaping over the rubble as the tank's blast erupts."
    "The explosion propels me through the air."
    "Landing in the dirt, I roll quickly as blaster bolts thud into the ground around me."
    "I slam my back into another piece of ruined building as Ama strafes to my side."
    "Rifle poised in hand, she fires at a constant, controlled rate, tagging a handful of enforcers before she too has to duck behind cover."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment8)
    "She tilts her head in the direction of the tank."
    amaS "Got a pretty good crew, Mozely."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment9)
    "I peek just over the rubble as a shot whizzes past my head."
    "The tank is charging its cannon again and turning to aim at our position."
    "But Teresa and Jennica have already climbed on top of it."
    "Teresa stabs something into its top hatch while Jennica grabs the cannon and drags it to aim at a group of nearby enforcers."
    "The shot fires, sending the enforcers flying into the air as the top hatch of the tank pops open."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment10)
    "Amdist the chaos, the captive Dragonflies have dispersed."
    "Some run into the shelter of buildings while others start brawling with BC goons."
    "Teresa and Jennica have dragged some goons out of the tank hatch and are busy pummeling them on the ground."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment11)
    "Seven BC enforcers are closing in on mine and Ama's position."
    "Ama winks at me."
    amaS "Shall we."
    menu:
        amaS "Shall we."
        "Let's dance.":
            $ deadeyeApproval += 1
            mS "Let's dance."
        "Bet I get more.":
            $ deadeyeApproval += 2
            mS "Bet you I tag more than you."
            amaS "You're on, kid."
    if jennicaRomance == False and teresaRomance == False:
        $ AddChatter(vig4_sc6_attack_1_assault_ama_comment12)
    "I whip around the cover, firing shots immediately down the street."
    "One of the enforcers goes down as a grenade lands behind my cover."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment13)
    "I roll to the side, away from the explosion and fire back."
    "Ama has appeared around the corner and is advancing toward the enforcers."
    "No fear. Just the constant repeating of her rifle."
    "I blast back at our enemies, rushing toward them with reckless abandon."
    "Two drop before I get in close to the final one."
    "Tackling him to the ground, I pull up and look him in the eyes."
    "He puts his hands up in front of his face."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment14)
    "I fire two quick shots into his chest."
    "His body goes cold."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment15)
    hide bc_enforcer with dissolve
    "The world around me has gone quiet again."
    "Standing up, I see the Dragonflies gathering around one another."
    "The ones who lived."
    "Some lay motionless on the ground."
    "The sounds of battle in the distance are quieting down."
    "Ama steps up next to me."
    amaS "Pretty good shots Moze. Accuracy could use some work though."
    menu:
        amaS "Pretty good shots Moze. Accuracy could use some work though."
        "I got more.":
            mS "Who cares."
            mS "By my count, I got four and you got three."
            amaS "Oh ho, still got that fierceness in you, I see."
            if jennicaRomance == False and teresaRomance == False:
                $ AddChatter(vig4_sc6_attack_1_assault_ama_comment16)
            "She grins at me."
            amaS "Just like old times."
        "Yours is slipping.":
            $ deadeyeApproval += 1
            mS "Yours isn't what it used to be either."
            amaS "You calling me \"old,\" kid?"
            mS "I didn't say that."
            mS "Though it's true."
            if jennicaRomance == False and teresaRomance == False:
                $ AddChatter(vig4_sc6_attack_1_assault_ama_comment16)
            amaS "Ahahaha."
            amaS "Careful Mozely, age begets wisdom."
    if jennicaRomance == False and teresaRomance == False:
        $ AddChatter(vig4_sc6_attack_1_assault_ama_comment17)
    dflyGuard "Captain Moze?"
    show dflyGuard at stream_center with dissolve
    "The leader of the Dragonflies squad approaches me."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment18)
    dflyGuard "We thought we were dead."
    "He glances at the bodies in the street."
    dflyGuard "We didn't all make it, but you gave us a chance to fight back."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment19)
    dflyGuard "I know we didn't leave on the best of terms. But, thank you for saving us."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment20)
    pause 0.5
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment21)
    pause 0.5
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment22)
    menu:
        dflyGuard "I know we didn't leave on the best of terms. But, thank you for saving us."
        "You were just doing your job.":
            $ csEngagement += 1
            $ pdEngagement -= 1
            mS "You were just doing your job. I understand what that's like."
            $ reactTarget = "vig4_sc6_attack_sparedflies"
            show screen streamerCommentary
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment23)
            dflyGuard "I appreciate your understanding."
            dflyGuard "Will you join us to defend the plaza?"
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment25)
            amaS "We have business elsewhere."
            "The Dragonfly looks Ama up and down."
            "He's about to say something, then thinks better of it."
            dflyGuard "Of course."
            dflyGuard "Good luck, Captain."
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment26)
            "He turns and rejoins his comrades. Together, they walk down the street toward the plaza."
            hide screen streamerCommentary
            hide customs agent with dissolve
        "It wasn't about you.":
            $ pdEngagement += 1
            $ csEngagement -= 1
            mS "You're welcome, but it wasn't about you."
            $ reactTarget = "vig4_sc6_attack_sparedflies"
            show screen streamerCommentary
            mS "I deprived BC of strategic leverage."
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment24)
            "He looks taken aback."
            dflyGuard "Ah, I see."
            dflyGuard "Will you join us to defend the plaza?"
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment25)
            amaS "We have business elsewhere."
            "The Dragonfly guard looks Ama up and down."
            "He's about to say something, then thinks better of it."
            dflyGuard "Of course."
            dflyGuard "Good luck, Captain."
            hide screen streamerCommentary
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment26)
            "He turns and rejoins his comrades. Together, they walk down the street toward the plaza."
            hide customs agent with dissolve
        "I wanted to kill you myself.":
            $ deadeyeApproval += 1
            $ csEngagement -= 2
            $ pdEngagement += 2
            $ vig4_killDflies = True
            mS "Don't thank me. I just wanted the pleasure of killing you myself."
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment27)
            play audio "lazer.wav"
            hide dflyGuard with Dissolve(0.5)
            "The guard has half a second to look stunned before a blaster bolt rips through his skull."
            $ reactTarget = "vig4_sc6_attack_killdflies"
            show screen streamerCommentary
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment28)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment29)
            "The rest of the Dragonflies look up, confusion rampant on their faces as Ama and I draw our weapons."
            "Our blasters echo in the night."
            "Each of the Dragonflies drops to the ground. Dead."
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment30)
            hide screen streamerCommentary
    "Ama claps me on the back."
    amaS "That's the Mozely I remember."
    amaS "Now, let's see the vessel we've commandeered!"
    hide ama with dissolve
    jump vig4_sc6_attack_2_ama

label vig4_sc6_attack_1_split_ama():
    mS "Ama's right, if we're going to do this we have to do it smart."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment1)
    mS "We'll wait for the battalion to split off, then take the tank when it's just a skeleton crew."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment2)
    mS "Jennica and Teresa, take care of the tank. Ama, we'll take the leftover squad."
    amaS "Strike from a place of advantage. Good."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment3)
    enS "Behind you."
    pS "Of all the hostages we've met, I won't regret letting BC keep these ones."
    mS "Get in position."
    hide teresa with dissolve
    hide jennica with dissolve
    "Staying in cover, Jennica and Teresa cycle around the rubble, getting as close to the tank as possible without revealing themselves."
    show ama stream neutral at stream_left with move
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
            $ deadeyeApproval += 1
            mS "Let's dance."
        "Bet I get more.":
            $ deadeyeApproval += 2
            mS "Bet you I tag more than you."
            amaS "You're on, kid."
    if jennicaRomance == False and teresaRomance == False:
        $ AddChatter(vig4_sc6_attack_1_split_ama_comment12)
    play audio "lazer.wav"
    "Whipping around the cover, I take aim and fire two quick shots."
    if vig4_nickName_bool == True:
        $ AddChatter(vig4_sc6_attack_1_split_ama_comment4)
    else:
        $ AddChatter(vig4_sc6_attack_1_split_ama_comment5)
    play audio "lazer.wav"
    "Ama follows that with a blast from her rifle."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment6)
    "Two BC enforcers drop dead as the rest scramble for cover."
    "Ama and I advance confidently. My pistol firing rapidly alongside the steady cadence of her rifle."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment8)
    "Out of the corner of my eye, I see Jennica and Teresa leap onto the tank."
    "The sound of charging resonates in its central cannon as it turns to aim at Ama and me."
    "Then Jennica grabs the cannon's barrel and heaves it to the side, pulling the metal barrel to point it up and away."
    "Teresa stabs something into the tank's top hatch and smoke spurts out from the metal."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment10)
    "Ama and I keep advancing on the enforcers who cower behind cover."
    "But there's nowhere to hide."
    "The second one of them peeks around a corner, a bolt lands between their eyes."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment14)
    "There's nowhere to run. No help coming for them. They can't escape."
    "We rip them to shreds, leaving none standing."
    hide bc_enforcer with dissolve
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment15)
    "Jennica and Teresa are busy pummeling the tank crew on the ground."
    "A simple maneuver."
    "The sounds of battle in the distance are start to quiet."
    "Ama steps up next to me."
    amaS "Pretty good shots Moze. Accuracy could use some work though."
    menu:
        amaS "Pretty good shots Moze. Accuracy could use some work though."
        "I got more.":
            mS "Who cares."
            mS "By my count, I got four and you got three."
            amaS "Oh ho, still got that fierceness in you, I see."
            if jennicaRomance == False and teresaRomance == False:
                $ AddChatter(vig4_sc6_attack_1_split_ama_comment16)
            "She grins at me."
            amaS "Just like old times."
        "Yours is slipping.":
            $ deadeyeApproval += 1
            mS "Yours isn't what it used to be either."
            amaS "You calling me \"old,\" kid?"
            mS "I didn't say that."
            mS "Though it's true."
            if jennicaRomance == False and teresaRomance == False:
                $ AddChatter(vig4_sc6_attack_1_split_ama_comment16)
            amaS "Ahahaha."
            amaS "Careful Mozely, age begets wisdom."
    if jennicaRomance == False and teresaRomance == False:    
        $ AddChatter(vig4_sc6_attack_1_split_ama_comment17)
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
    $ AddChatter(vig4_sc6_attack_2_ama_comment1)
    mS "Any idea how to drive this thing, Jenn?"
    pS "Sure, Cap, doesn't look too complex. We just gotta work as a team."
    $ AddChatter(vig4_sc6_attack_2_ama_comment2)
    pS "I'll take drivin'. Teresa, take care of our shields and engine power."
    show teresa stream neutral at stream_right with dissolve
    enS "Makes sense."
    pS "Ama, you get the machine guns."
    show ama stream neutral at stream_left5 with dissolve
    amaS "Music to my ears."
    $ AddChatter(vig4_sc6_attack_2_ama_comment3)
    pS "Cap, you stay in the center, be our spotter and control the main cannon."
    mS "Roger, let's roll out."
    pS "Aye aye."
    play audio "callRing.wav"
    "As Jennica goes to move the tank forward, a ring suddenly echoes in the tank."
    enS "Someone is hailing us."
    pS "On a BigCorp frequency?"
    enS "No. It's not BigCorp, but it has access to their comms?"
    $ AddChatter(vig4_sc6_attack_2_ama_comment4)
    amaS "It's the robot! Answer it!"
    "Teresa inputs something into a screen on her side."
    "At the front of the tank, a blue hologram slowly starts to take shape."
    show maccall neutral at stream_right5mac with dissolve
    "It's MAC."
    $ reactTarget = "vig4_sc6_both_maccall"
    show screen streamerCommentary
    $ AddChatter(vig4_sc6_attack_2_ama_comment5)
    mS "MAC!"
    pS "Hey, little guy!"
    enS "Good to see you, MAC!"
    macS "Captain? Moze? I expected it was you. Stealing a tank is very much your style."
    $ AddChatter(vig4_sc6_attack_2_ama_comment6)
    menu:
        macS "Captain? Moze? I expected it was you. Stealing a tank is very much your style."
        "We came back for you!":
            mS "Yes, MAC! We came back for you!"
        "We came to keep you safe!":
            mS "Yes, MAC! We came back to ensure you're safety."
    mS "Are you okay? Are you hurt?"
    hide screen streamerCommentary
    if rudeMACGoodbye == True:
        macS "Why do you care? Wasn't this just your mission?"
        $ AddChatter(vig4_sc6_attack_2_ama_comment7)
        "The world goes cold."
        enS "That's not fair, MAC."
        pS "We're a family."
        macS "It's what {i}she{/i} said."
        $ AddChatter(vig4_sc6_attack_2_ama_comment8)
        menu:
            macS "It's what {i}she{/i} said."
            "I'm sorry, MAC.":
                $ kcEngagement += 1
                $ csEngagement += 1
                mS "I'm sorry, MAC."
                mS "I didn't mean it."
                mS "I thought that would make saying goodbye easier."
                mS "But it just made it hurt more."
                mS "I regretted saying it the second the words left my mouth."
                mS "We're here for you now, whatever you need. However we can help."
                mS "Just tell us where you are, and we'll be there for you. Always."
                $ AddChatter(vig4_sc6_attack_2_ama_comment9)
                "MAC pauses for a moment. As if pondering what I've said."
            "The job's not finished.":
                $ kcEngagement -= 1
                $ pdEngagement += 1
                mS "It is a job MAC, and it was, without a doubt, personal."
                mS "But the job's not done."
                mS "BC is here for you, and we're not going to let them take you away."
                mS "I finish what I start. And making sure you're safe, isn't finished yet."
                $ AddChatter(vig4_sc6_attack_2_ama_comment10)
                mS "So tell us where you are. Tell us how we can help you."
                "MAC pauses for a moment. As if pondering what I've said."
    macS "I am okay."
    macS "But Coil has brought me into the plaza tower and away from the fighting."
    if macViolence >= macPeace:
        macS "And I was doing such a good job with the turret!"
        $ AddChatter(vig4_sc6_attack_2_ama_comment11)
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
        $ AddChatter(vig4_sc6_attack_2_ama_comment12)
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
    $ AddChatter(vig4_sc6_attack_2_ama_comment13)
    play audio "cutCall.wav"
    hide maccall with dissolve
    "The signal is cut short."
    enS "That was Coil's voice."
    $ AddChatter(vig4_sc6_attack_2_ama_comment14)
    pS "No doubt. So he has MAC at the top of the tower."
    amaS "The barricades they set up around the plaza will be a bit of trouble, but we can handle them."
    $ AddChatter(vig4_sc6_attack_2_ama_comment15)
    mS "We won't have to on our own."
    $ AddChatter(vig4_sc6_attack_2_ama_comment16)
    pS "Cap?"
    mS "That enforcer said BC was preparing a second assault." 
    mS "This first one must have just been to soften up Polaris's defenses."
    mS "When BC launches their next attack, we can use the chaos to break through and get into the tower."
    amaS "Oh, I {i}like{/i} this plan, Mozely."
    $ AddChatter(vig4_sc6_attack_2_ama_comment17)
    enS "Efficient and clever."
    pS "A lot of people are going to die. But I guess that's unavoidable at this point."
    $ AddChatter(vig4_sc6_attack_2_ama_comment18)
    mS "As long as we get MAC. That's what matters."
    "As I finish speaking, a siren rings out from Polaris's plaza."
    "I peer through the tank's scope at the Cruiser hovering in the night sky, like a hammer poised above an anvil."
    "A line of dropships careen through the air to Polaris."
    $ AddChatter(vig4_sc6_attack_2_ama_comment19)
    mS "The second attack is starting."
    amaS "Just in time."
    mS "Agreed. Jenn, take us to the plaza."
    $ AddChatter(vig4_sc6_attack_2_ama_comment20)
    "The tank accelerates and we glide smoothly over the ground. On our way to battle."
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
    $ AddChatter(vig4_sc6_attack_3_ama_comment1)
    "We turn onto the main street."
    "Instant chaos."
    "A BC dropship screeches by overhead, turrets strafing positions defended by Dragonflies."
    $ AddChatter(vig4_sc6_attack_3_ama_comment2)
    "The Dragonflies have consolidated their defenses behind an enormous barricade blocking the main street into the plaza."
    "A swarm of BC enforcers march down the street."
    "Blaster fire streaks in both directions."
    "As we emerge onto the street, the BC army suddenly cheers."
    $ AddChatter(vig4_sc6_attack_3_ama_comment3)
    pause 0.5
    $ AddChatter(vig4_sc6_attack_3_ama_comment4)
    pS "They think we're on their side."
    $ AddChatter(vig4_sc6_attack_3_ama_comment5)
    enS "We are in their tech."
    $ AddChatter(vig4_sc6_attack_3_ama_comment6)
    amaS "Use it to our advantage, right, Mozely?"
    $ AddChatter(vig4_sc6_attack_3_ama_comment7)
    menu:
        amaS "Use it to our advantage, right, Mozely?"
        "Pretend to be with BigCorp, attack the Dragonflies.":
            $ vig4_killDflies = True
            $ deadeyeApproval += 2
            $ pdEngagement += 2
            $ csEngagement -= 2
            $ kcEngagement -= 1
            $ reactTarget = "vig4_sc6_attack_barricadesurprise"
            show screen streamerCommentary
            mS "Ama's right. Keep our weapons aimed at the Dragonfly position."
            $ AddChatter(vig4_sc6_attack_3_ama_comment9)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_3_ama_comment8)
            mS "Jennica, get us there as quick as you can without being suspcious."
            pS "Roger, Cap."
            "The tank advances on the barricade."
            $ AddChatter(vig4_sc6_attack_3_ama_comment10)
            "Shots from the Dragonflies start to rattle against our hull."
            enS "Shields are at 95\%."
            hide screen streamerCommentary
            $ AddChatter(vig4_sc6_attack_3_ama_comment11)
            amaS "Oh I've been waiting for this!"
            "Ama grabs the machine gun controls and whips it around, aiming for the squads positioned on nearby rooftops."
            "The rapid fire of the machine gun tears into the squads, sending them into a retreat."
            $ AddChatter(vig4_sc6_attack_3_ama_comment12)
            show vig1_town_stream with hpunch
            "A grenade explodes next to us, engulfing sending BC enforcers flying and shaking our hull."
            enS "Tough hit but shields are still at 85\% and holding."
            "I grip the cannon controls and point at a squad of Dragonflies huddled behind nearby cover."
            "The whole tank thrums with energy as the cannon charges."
            $ AddChatter(vig4_sc6_attack_3_ama_comment13)
            "A beam of blue light bursts from the cannon, striking through the rubble."
            "A pillar of flame erupts into the air where the cannon impacts the ground."
            "There's no evidence of the Dragonflies who were hiding behind cover."
            $ AddChatter(vig4_sc6_attack_3_ama_comment14)
            mS "Jenn, keep us moving."
            "We slowly advance at the head of the BC army."
            $ AddChatter(vig4_sc6_attack_3_ama_comment15)
            "Ama hasn't let go of the machine gun trigger. Almost all of the Dragonflies duck behind cover."
            "A group tries to take shots at us from a rooftop."
            "I aim the cannon at the base of the building."
            "The thrum of energy."
            "The blue light."
            "Another pillar of flame and the memory of human presence."
            $ AddChatter(vig4_sc6_attack_3_ama_comment16)
            "We keep advancing."
            enS "Contact on the rooftops!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment17)
            show vig1_town_stream with hpunch
            "Another detonation on the side of the tank."
            "I whip a monitor around to view the assailants."
            $ AddChatter(vig4_sc6_attack_3_ama_comment18)
            "It's a group of Dragonflies armed with rocket launchers a couple of buildings away from us."
            "They're reloading the launchers and preparing another volley."
            mS "Teresa, direct shields against those launchers. Ama--"
            $ AddChatter(vig4_sc6_attack_3_ama_comment19)
            amaS "I know, I see them too!"
            "Ama aims the machine gun at the direction of the squad and begins firing, but it's too late."
            show vig1_town_stream with hpunch
            "Another rocket streaks through the air and collides with us just as the bolts from the machine gun rip into their bodies."
            mS "Resa, how're we doing?"
            enS "Bad hits. We're at 45\% shields, but holding. We just don't want to take two more of those."
            pS "Cap! We're almost at the barricade!"
            "I turn to look ahead."
            $ vig4_sc6_attack_3_ama_comment19.click = False
            $ AddChatter(vig4_sc6_attack_3_ama_comment20)
            "Jenn's right, we're closing in."
            mS "Alright, Resa, direct our power into engine thrusts and tell me when it's ready to go. We're going to ram through it."
            enS "Are you sure that's--"
            amaS "Oh, yes!"
            mS "Just do it!"
            mS "Jenn, hit the thurst forward. Hard!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment21)
            pS "Aye aye, Cap!" 
            "The main cannon charges. Our engines hum with excitement."
            enS "Ready, captain!"
            mS "Launch!"
            "Fire erupts from the cannon at the same time as we rush forward."
            "The barricade shatters as the cannon's blast collides with it."
            $ AddChatter(vig4_sc6_attack_3_ama_comment22)
            "Our shields sparkle, the tank ramming into the wall and splitting it apart."
            $ AddChatter(vig4_sc6_attack_3_ama_comment23)
        "Attack BigCorp, rush the barricade.":
            $ deadeyeApproval -= 1
            $ pdEngagement -= 1
            $ csEngagement += 1
            $ kcEngagement -= 1
            $ reactTarget = "vig4_sc6_attack_barricadeassault"
            show screen streamerCommentary
            mS "No. BigCorp is still the enemy."
            $ AddChatter(vig4_sc6_attack_3_ama_comment24)
            mS "Jenn, get us to that barricade as fast as you can."
            pS "Aye!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment10)
            mS "Resa, keep those shields up."
            $ AddChatter(vig4_sc6_attack_3_ama_comment11)
            enS "Roger, we're at 95\% currently!"
            mS "Ama, open fire on any BC goons you see."
            amaS "I don't like losing the element of surprise, but I do like killing some BC goons."
            $ AddChatter(vig4_sc6_attack_3_ama_comment12)
            "Ama grabs the machine gun controls and whips it around, aiming for the enforcers at the frontline."
            "As the tank accelerates forward, confusion spreads throughout the BC army, throwing them into disarray."
            $ AddChatter(vig4_sc6_attack_3_ama_comment25)
            "Our shields continue to take hits from both sides as blaster fire rattles against our hull."
            show vig1_town_stream with hpunch
            "A grenade explodes at our side, shaking the tank slightly."
            enS "Shields are at 70\%. We're taking a lot of hits."
            $ AddChatter(vig4_sc6_attack_3_ama_comment26)
            "A dropship angles toward us."
            mS "We can dish them out too."
            "I grip the controls for the main cannon."
            "The whole tank thrums with energy as it charges."
            "A beam of blue light bursts from the cannon, striking the dropship out of the sky."
            "The ship explodes in a fireball as wreckage falls into Polaris, crashing into the BC swarm."
            hide screen streamerCommentary
            $ AddChatter(vig4_sc6_attack_3_ama_comment27)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_3_ama_comment29)
            mS "Jenn, how are we doing?"
            pS "We're close, just a bit further!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment28)
            enS "Captain, we're starting to take less fire from the Dragonflies."
            show vig1_town_stream with hpunch
            "Another detonation on the side of the tank."
            "I whip a monitor around to view the assailants."
            "It's a group of BC enforcers armed with rocket launchers." 
            $ AddChatter(vig4_sc6_attack_3_ama_comment30)
            "They're on a rooftop near the back of the attack force."
            "They're reloading the launchers and preparing for another volley."
            $ AddChatter(vig4_sc6_attack_3_ama_comment31)
            "I whip the main cannon controls around, aiming them at the base of the building."
            "The cannon charges."
            "The rocket streaks through the air."
            "The beam of blue light strikes the building as a pillar of flame erupts into the night."
            show vig1_town_stream with hpunch
            "The rocket detonates close to us, but not a direct hit."
            $ AddChatter(vig4_sc6_attack_3_ama_comment32)
            enS "Shields are at 30\%! Another hit and we're toast!"
            pS "Cap! We're almost at the barricade!"
            "I turn to look ahead."
            "She's right, we're closing in."
            $ AddChatter(vig4_sc6_attack_3_ama_comment33)
            mS "Alright, Resa, direct our power into engine thrusts and tell me when it's ready to go. We're going to ram through it."
            enS "Are you sure that's--"
            $ AddChatter(vig4_sc6_attack_3_ama_comment19)
            amaS "Oh, yes!"
            mS "Just do it!"
            mS "Jenn, hit the thurst forward. Hard!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment21)
            pS "Aye aye, Cap!" 
            "The main cannon charges. Our engines hum with excitement."
            enS "Ready, captain!"
            mS "Launch!"
            "Fire erupts from the cannon at the same time as we rush forward."
            "The barricade shatters as the cannon's blast collides with it."
            $ AddChatter(vig4_sc6_attack_3_ama_comment22)
            "Our shields sparkle, the tank ramming into the wall and splitting it apart."
            $ AddChatter(vig4_sc6_attack_3_ama_comment23)
        "Attack both Dragonflies and BigCorp.":
            $ vig4_killDflies = True
            $ pdEngagement += 1
            $ csEngagement -= 1
            $ kcEngagement += 1
            $ reactTarget = "vig4_sc6_attack_barricadechaos"
            show screen streamerCommentary
            mS "Screw it."
            $ AddChatter(vig4_sc6_attack_3_ama_comment34)
            mS "Jenn, get us to that barricade as fast as you can."
            $ AddChatter(vig4_sc6_attack_3_ama_comment35)
            pS "Aye aye."
            $ AddChatter(vig4_sc6_attack_3_ama_comment10)
            mS "Resa, keep those shields up."
            $ AddChatter(vig4_sc6_attack_3_ama_comment11)
            enS "Roger, we're at 95\% currently!"
            mS "Ama, fire at will."
            amaS "Oh I've been waiting for this!"    
            $ AddChatter(vig4_sc6_attack_3_ama_comment12)
            "Ama grabs the machine gun controls and whips it around."
            "The bolts of machine gun rounds tear into soliders: BC enforcers and Dragonflies alike."
            $ AddChatter(vig4_sc6_attack_3_ama_comment36)
            "Ama fires in quick, succinct burst. Striking Dragonflies on the rooftops, then BC enforcers on the ground."
            "It's a methodical madness. One I'm familiar with."
            $ AddChatter(vig4_sc6_attack_3_ama_comment37)
            "Confusion spreads through both sides as blaster fire pings off the tank's shell."
            enS "Shields are at 85\%, Captain."
            "I grip the controls for the main cannon. The entire tank thrums with energy as it charges."
            hide screen streamerCommentary
            show vig1_town_stream with hpunch
            "Above, a dropship aims down toward our position, turrets sending fire against our hull."
            "A beam of blue light bursts from the cannon, striking the dropship out of the sky."
            $ AddChatter(vig4_sc6_attack_3_ama_comment38)
            "The ship explodes in a fireball as wreckage falls into Polaris, crashing into the BC swarm."
            mS "Jenn, how are we doing?"
            $ AddChatter(vig4_sc6_attack_3_ama_comment39)
            pS "We're close, just a bit further!"
            show vig1_town_stream with hpunch
            "An explosion suddenly detonates against our side."
            mS "Teresa, report!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment30)
            "I whip the monitor around, looking for the assailants."
            enS "Shields are down to 60\%. We're taking fire from both sides and losing energy rapidlly!"
            "I locate the smoke streaking through the air."
            "Dragonflies on a nearby building are loading rocket launchers."
            $ AddChatter(vig4_sc6_attack_3_ama_comment40)
            "I drop the cannon to aim at the base of the building, charging up another blast."
            "But I'm too late."
            "A bright flashing rocket streaks toward us just as I fire the cannon."
            show vig1_town_stream with hpunch
            "The rocket impacts on our side, but at the same time, the tank's blast detonates on the building."
            "A pillar of flame erupts into the sky as the edifice crumbles to the ground."
            $ AddChatter(vig4_sc6_attack_3_ama_comment41)
            amaS "They're throwing grenades!"
            "Ama lays on the machine gun full auto as BC enforcers break ranks to move toward our position."
            "Most of them are cut down, but a couple are able to lob grenades that land at our side."
            show vig1_town_stream with hpunch
            "They detonate, jostling the vehicle."
            $ AddChatter(vig4_sc6_attack_3_ama_comment42)
            enS "Shields are down to 30\%! We can't take much more of this!"
            pS "Cap! We're almost at the barricade!"
            "I turn to look ahead."
            $ AddChatter(vig4_sc6_attack_3_ama_comment19)
            "She's right, we're closing in."
            mS "Alright, Resa, direct our power into engine thrusts and tell me when it's ready to go. We're going to ram through it."
            enS "Are you sure that's--"
            amaS "Oh, yes!"
            mS "Just do it!"
            mS "Jenn, hit the thurst forward. Hard!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment21)
            pS "Aye aye, Cap!" 
            "The main cannon charges. Our engines hum with excitement."
            enS "Ready, captain!"
            mS "Launch!"
            "Fire erupts from the cannon at the same time as we rush forward."
            "The barricade shatters as the cannon's blast collides with it."
            $ AddChatter(vig4_sc6_attack_3_ama_comment22)
            "Our shields sparkle, the tank ramming into the wall and splitting it apart."
            $ AddChatter(vig4_sc6_attack_3_ama_comment23)
    "The tank isn't supposed to go this fast. And it's not supposed to turn this hard."
    "But Jennica wrangles it under control as we careen to a stop at the base of the tower."
    $ AddChatter(vig4_sc6_attack_3_ama_comment43)
    "I open the top hatch and scramble out."
    "The barricade at the entrance to the plaza begins to crumble as the Dragonflies disperse."
    $ AddChatter(vig4_sc6_attack_3_ama_comment44)
    "BC closes in on the plaza."
    $ AddChatter(vig4_sc6_attack_3_ama_comment45)
    "More dropships stream down from the cruiser."
    $ AddChatter(vig4_sc6_attack_3_ama_comment46)
    "We don't have much time."
    "War has come."
    $ AddChatter(vig4_sc6_attack_3_ama_comment48)
    menu:
        "War has come."
        "This is it.":
            mS "This is it. The end of the road."
        "We're not making it out of this.":
            mS "I don't know if I see a way out of this."
    mS "This is where our score gets settled."
    $ AddChatter(vig4_sc6_attack_3_ama_comment49)
    pause 0.5
    $ AddChatter(vig4_sc6_attack_3_ama_comment50)
    pause 0.5
    $ AddChatter(vig4_sc6_attack_3_ama_comment51)
    show ama stream neutral at stream_left5 with dissolve
    amaS "Then let's make sure it's settled in our favor."
    "Ama hops out of the tank, standing opposite me."
    "Suddenly, I feel something. Standing here. At war. With her."
    "It's comfort. Like we've been here before."
    if jennicaRomance == False and teresaRomance == False:
        $ AddChatter(vig4_sc6_attack_3_ama_comment52)
    menu:
        "It's comfort. Like we've been here before."
        "Reject the feeling.":
            "No. This is different. And I refuse to let her into my life again."
            $ AddChatter(vig4_sc6_attack_3_ama_comment53)
        "Embrace the feeling.":
            $ deadeyeApproval += 1
            mS "Ama."
            "She looks at me."
            mS "It's good to have you here."
            "She winks."
            amaS "Good to be here, kid."
    $ AddChatter(vig4_sc6_attack_3_ama_comment54)
    "We both turn to look at the burning horizon as Polaris crumbles."
    if vig2_outlawEpilogue == True:
        $ pdEngagement += 3
        $ kcEngagement += 2
        $ csEngagement += 1
        $ vig4_reggieReturn = True
        unknown "Ugh, and here I thought you all would have toughened up in the last two weeks."
        hide ama with dissolve
        "A familiar voice...but from where?"
        $ AddChatter(vig4_sc6_defend_5_comment15)
        enS "Captain, we're being hailed by a new signal, I don't--"
        show vig1_town_stream with hpunch
        "A ship suddenly streaks overhead, careening toward the BC dropships."
        $ AddChatter(vig4_sc6_defend_5_comment16)
        "Its wings open into attack formation as green bolts of light rip into a dropship, sending it to the ground."
        "Three more fighters fly by immediately after. Then another. Then another."
        $ AddChatter(vig4_sc6_defend_5_comment17)
        "A fleet of attack ships."
        pS "Who the--that's one hell of a pilot?"
        show reginald stream bigmad at stream_center with dissolve
        $ AddChatter(vig4_sc6_defend_5_comment18)
        goon "I really don't get paid enough for this shit."
        show jennica stream shock at stream_left with dissolve
        pS "Reginald!?"
        $ AddChatter(vig4_sc6_defend_5_comment19)
        goon "Matticus sends his regards."
        goon "Said he had a debt that needed paying off."
        $ AddChatter(vig4_sc6_defend_5_comment20)
        show jennica stream neutral
        "The swarm of attack ships engage the BC dropships, delaying their advance."
        $ AddChatter(vig4_sc6_defend_5_comment21)
        goon "So take care of whatever you got to do on the ground. We'll handle the air shit."
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
        hide reginald with dissolve
        show teresa stream neutral at stream_right with dissolve
    #if vig3_marshalChoice == True:
    else:
        $ pdEngagement += 1
        $ kcEngagement += 3
        $ csEngagement += 2 
        unknown "MOXIE!"
        hide ama with dissolve
        show jennica stream neutral at stream_left with dissolve
        pS "Cap, we're pickin' up a new signal!"
        #if vig2_outlawEpilogue == True:
        #    pS "Cap, we're pickin' up another signal!"
        show teresa stream shock at stream_right with dissolve
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
        show jennica stream neutral at stream_left with dissolve
    show ama at stream_center with dissolve
    pS "Uh, gang, y'all should get a move on." 
    mS "Not without you two."
    show teresa stream neutral at stream_right with dissolve
    enS "Negative, Captain."
    mS "What!?"
    $ AddChatter(vig4_sc6_defend_5_comment24)
    enS "If BC takes the plaza it won't matter what you do up there, we'll all be toast."
    $ AddChatter(vig4_sc6_defend_5_comment25)
    pS "You go get the kid. We'll keep a path clear down here."
    $ AddChatter(vig4_sc6_defend_5_comment26)
    menu:
        pS "You go get the kid. We'll keep a path clear down here."
        "I'm not leaving you.":
            mS "No way, I'm not leaving you two!"
            enS "You're not leaving anything."
            pS "We're just splittin' up to make the mission succeed."
            "Jennica and Teresa" "We've got this."
            if jennicaRomance == True:
                $ csEngagement += 1
                "Jennica suddenly comes up from the tank. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                $ AddChatter(vig4_sc6_defend_5_comment28)
                pS "Go do what you do best, Moze."
            elif teresaRomance == True:
                $ kcEngagement += 2
                "Teresa suddenly comes up from the tank. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                $ AddChatter(vig4_sc6_defend_5_comment27)
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
                $ AddChatter(vig4_sc6_defend_5_comment28)
                pS "Go do what you do best, Moze."
            elif teresaRomance == True:
                "Teresa suddenly comes up from the tank. She faces me dead on."
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
    hide jennica with dissolve
    hide teresa with dissolve
    "I hop down to the ground."
    show ama at stream_left with move
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
    $ AddChatter(vig4_sc7_1_defend_comment1)
    "A distant voice calls from above."
    cS "Up here. Come along."
    $ AddChatter(vig4_sc7_1_defend_comment2)
    "Ama and I follow a series of stairs that winds up to the top of the tower."
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
    "Jennica."
    "Teresa."
    "MAC."
    "Every person. Every choice."
    "Here I am."
    $ AddChatter(vig4_sc7_1_defend_comment7)
    "The stairs flatten out."
    "Ama and I step across the threshold into a wide room."
    $ AddChatter(vig4_sc7_1_defend_comment9)
    show vig2_datacenter_stream onlayer background with dissolve
    show coil stream neutral at stream_right with dissolve
    "Coil stands in the center, in front of a massive computer console."
    $ AddChatter(vig4_sc7_1_defend_comment10)
    cS "Well, you made it."
    if vig4_killDflies == True:
        cS "You had to murder some good people to do it." 
        cS "But you arrived."
        $ AddChatter(vig4_sc7_1_attack_ama_comment1)
    else:
        pass
    "Coil turns to face us. His face looks haggard, his eyes bloodshot."
    $ AddChatter(vig4_sc7_1_defend_comment11)
    $ reactTarget = "vig4_sc6_attack_finding_coil"
    show screen streamerCommentary
    menu:
        "Coil turns to face us. His face looks haggard, his eyes bloodshot."
        "Where is MAC?":
            mS "Where is MAC?"
            $ AddChatter(vig4_sc7_1_attack_ama_comment2)
            cS "Always so direct."
            cS "MAC is no longer any of your concern, Moze."
            cS "You delivered him, he is our responsibility."
            $ AddChatter(vig4_sc7_1_attack_ama_comment3)
            cS "And he is safe."
            if macViolence > macPeace:
                cS "You know he insisted on operating a turret when BigCorp arrived."
                cS "Said he would \"make those BC scum pay.\""
                $ AddChatter(vig4_sc7_1_attack_ama_comment4)
                mS "Sitting in a turret on the frontlines. Is that really what you consider \"safe\"?"
                cS "No. But he insisted."
                cS "And as I'm sure you're aware, he can be quite strong-willed."
                cS "He got it from you after all."
                amaS "Mozely can be quite stubborn."
                cS "I meant the bloodlust."
                $ AddChatter(vig4_sc7_1_attack_ama_comment5)
                "Ama tilts her head."
                $ AddChatter(vig4_sc7_1_attack_ama_comment6)
                hide screen streamerCommentary
                amaS "That too."
            else:
                cS "You know he insisted on providing first aid to the people who were first injured by BigCorp's assault."
                cS "Said he had to \"take care of the people around him.\""
                $ AddChatter(vig4_sc7_1_attack_ama_comment4)
                mS "Being a frontline medic isn't exactly what I would consider \"safe.\""
                cS "No. But he insisted." 
                cS "And I'm sure you're aware he can be quite strong-willed."
                cS "He got it from you after all."
                amaS "Mozely can be quite stubborn."
                cS "I meant the altruistic urge to help other people."
                $ AddChatter(vig4_sc7_1_attack_ama_comment5)
                "Ama tilts her head."
                $ AddChatter(vig4_sc7_1_attack_ama_comment6)
                amaS "Guess that has been a phase recently."
                hide screen streamerCommentary
                $ AddChatter(vig4_sc7_1_attack_ama_comment9)
        "Got a plan for getting out of this?":
            mS "So, do you have a plan for getting out of this."
            cS "I do."
            cS "The top of this tower can be converted into a makeshift rocket."
            cS "We will be able to finish the mission, where you failed."
            $ AddChatter(vig4_sc7_1_attack_ama_comment7)
            mS "And you're okay with all of Polaris dying while you escape?"
            cS "It breaks my heart."
            cS "But we have done what we could. What we were supposed to do."
            $ AddChatter(vig4_sc7_1_attack_ama_comment8)
            cS "MAC is no longer any of your concern, Moze."
            cS "You delivered him, he is our responsibility."
            $ AddChatter(vig4_sc7_1_attack_ama_comment3)
            if macViolence > macPeace:
                cS "You know he insisted on operating a turret when BigCorp arrived."
                cS "Said he would \"make those BC scum pay.\""
                $ AddChatter(vig4_sc7_1_attack_ama_comment4)
                mS "Sitting in a turret on the frontlines. Is that really what you consider \"safe\"?"
                cS "No. But he insisted."
                cS "And as I'm sure you're aware, he can be quite strong-willed."
                cS "He got it from you after all."
                amaS "Mozely can be quite stubborn."
                cS "I meant the bloodlust."
                $ AddChatter(vig4_sc7_1_attack_ama_comment5)
                "Ama tilts her head."
                $ AddChatter(vig4_sc7_1_attack_ama_comment6)
                hide screen streamerCommentary
                amaS "That too."
            else:
                cS "You know he insisted on providing first aid to the people who were first injured by BigCorp's assault."
                cS "Said he had to \"take care of the people around him.\""
                $ AddChatter(vig4_sc7_1_attack_ama_comment4)
                mS "Being a frontline medic isn't exactly what I would consider \"safe.\""
                cS "No. But he insisted." 
                cS "And I'm sure you're aware he can be quite strong-willed."
                cS "He got it from you after all."
                amaS "Mozely can be quite stubborn."
                cS "I meant the altruistic urge to help other people."
                $ AddChatter(vig4_sc7_1_attack_ama_comment5)
                "Ama tilts her head."
                $ AddChatter(vig4_sc7_1_attack_ama_comment6)
                amaS "Guess that has been a phase recently."
                hide screen streamerCommentary
                $ AddChatter(vig4_sc7_1_attack_ama_comment9)
    "Coil steps away from the devices and directly in front of me and Ama."
    cS "Tell me truthfully, Moze. What was your plan in coming here?"
    menu:
        cS "Tell me truthfully, Moze. What was your plan in coming here?"
        "I came for MAC.":
            $ kcEngagement += 1
            mS "I came for MAC."
            mS "I'm not leaving without him."
            $ AddChatter(vig4_sc7_1_defend_comment14)
            "Coil sighs."
            cS "I assumed that was the case."
            cS "I'm disappointed. After everything that happened, you couldn't just walk away."
            $ AddChatter(vig4_sc7_1_defend_comment15)
            cS "MAC is gone."
            amaS "Bullshit."
            amaS "If that were true you wouldn't still be here."
            cS "How perceptive. And yet you still have no idea what you're doing."
            $ AddChatter(vig4_sc7_1_defend_comment16)
            cS "Flailing around in the darkness with no purpose."
            $ AddChatter(vig4_sc7_1_defend_comment17)
        "I came to help.":
            mS "I came to help, to fight off BigCorp."
            $ AddChatter(vig4_sc7_1_attack_ama_comment10)
            "Coil tilts his head, as if inspecting me."
            cS "Help?"
            $ AddChatter(vig4_sc7_1_attack_ama_comment11)
            cS "I think we've had enough of your \"help.\""
            cS "You had to come back and visit more destruction upon us."
            $ AddChatter(vig4_sc7_1_attack_ama_comment12)
            if vig4_killDflies == True:
                cS "You killed my men because you wanted to, didn't you?"
                $ AddChatter(vig4_sc7_1_attack_ama_comment13)
                cS "You never even thought about helping us."
            else:
                cS "And is this why you've brought this hunter?"
                "He gestures at Ama."
                cS "This \"Deadeye.\""
                amaS "Good to know the name means something all the way out here."
                cS "It means a half-life. A ghost who has no place in this galaxy anymore."
                $ AddChatter(vig4_sc7_1_defend_comment16)
                amaS "I'll show you what this ghost is capable of."
                $ AddChatter(vig4_sc7_1_defend_comment17)
                cS "I'm sure you will."
            cS "Is this what your help means, Moze?"
    "Ama suddenly draws her rifle and aims at Coil."
    $ AddChatter(vig4_sc7_1_defend_comment18)
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
    $ AddChatter(vig4_sc7_1_defend_comment19)
    "Eyes wide, Ama fires again. And again."
    "Every shot is absorbed by the shield."
    $ AddChatter(vig4_sc7_1_defend_comment20)
    jump vig4_sc7_2




#####Attacking Polaris without Ama #######region 





label vig4_sc6_attack_1():
    show vig1_town_stream onlayer background with dissolve
    hide targetbase_stream
    "Polaris burns."
    $ viewCount += 1
    $ AddChatter(vig4_sc6_attack_1_ama_comment1)
    "The dull roar of battle echoes in the distance as we navigate the town's outskirts."
    $ AddChatter(vig4_sc6_attack_1_ama_comment2)
    "No enemies on the street."
    "No danger on the roofs."
    "We make our way quickly down the clear street, hopping between pieces of cover as we do so."
    $ vig4_sc6_attack_1_ama_comment1.click = False
    show teresa stream shock at stream_right with dissolve
    enS "Shit, patrol, get down!"
    $ AddChatter(vig4_sc6_attack_1_ama_comment3)
    hide teresa with dissolve
    "The three of us dive over the rubble of the building and crouch behind the ruined stones."
    "A low rumble gets closer, muddying the sound of several voices."
    $ AddChatter(vig4_sc6_attack_1_ama_comment4)
    "One breaks through, shouting."
    $ AddChatter(vig4_sc6_attack_1_ama_comment5)
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
    $ AddChatter(vig4_sc6_attack_1_ama_comment6)
    hide bc_enforcer with dissolve
    show jennica stream angry at stream_left with dissolve
    pS "Bastard."
    show teresa stream neutral at stream_right with dissolve
    enS "Position looks bad. We can't leave here without exposing ourselves."
    "My eye catches the tank."
    "There aren't that many enforers watching it. Most are focused on the captives."
    mS "We could go for the tank."
    $ AddChatter(vig4_sc6_attack_1_ama_comment7)
    pS "What!?"
    enS "And I thought I suggested the bold maneuvers."
    $ AddChatter(vig4_sc6_attack_1_ama_comment8)
    mS "Their guards are lax, too focused on the captives."
    $ AddChatter(vig4_sc6_attack_1_ama_comment9)
    pS "Sure, but we still can't take a whole battalion on our own."
    enS "We could wait for that group to leave, then take out the crew."
    $ AddChatter(vig4_sc6_attack_1_ama_comment10)
    pS "No way, if we're doing this then we should help those people."
    enS "Wait a minute, look at that guy!"
    show dflyGuard at stream_center with dissolve
    "Teresa points at one of the captive Dragonflies."
    enS "Isn't that?"
    pS "Oh yeah! That's the guy who roughed us up at the festival."
    $ AddChatter(vig4_sc6_attack_1_ama_comment11)
    enS "Guess he and his squad were more bark than bite after all."
    $ AddChatter(vig4_sc6_attack_1_ama_comment12)
    pS "They're still hostages. We should help them."
    $ AddChatter(vig4_sc6_attack_1_ama_comment13)
    hide dfly guard with dissolve
    enS "What's the call, Captain?"
    $ AddChatter(vig4_sc6_attack_1_ama_comment14)
    menu:
        enS "What's the call, Captain?"
        "We're saving the hostages first.":
            $ csEngagement += 1
            $ kcEngagement += 1
            $ pdEngagement -= 1
            $ marshal += 1
            jump vig4_sc6_attack_1_assault
        "Wait for the group to split.":
            $ csEngagement -= 1
            $ kcEngagement -= 1
            $ pdEngagement += 1
            $ outlaw += 1
            jump vig4_sc6_attack_1_split

label vig4_sc6_attack_1_assault():
    mS "Jennica's right. We can't let BC hold those hostages."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment1)
    pause 0.5
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment2)
    mS "We take the tank, but we're also not letting this battalion get away."
    pS "Thanks, Cap."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment3)
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
    play audio "lazer.wav"
    "I pop out of cover and fire two quick shots, landing them directly into the backs of two enforcers."
    play audio "lazer.wav"
    if vig4_nickName_bool == True:
        $ AddChatter(vig4_sc6_attack_1_assault_ama_comment5)
    else:
        $ AddChatter(vig4_sc6_attack_1_assault_ama_comment6)
    show bc_enforcer at stream_center with dissolve
    "Jennica and Teresa stay in cover and shift along the side of the rubble."
    "There's a moment of pause before the rain of blaster fire hits my position."
    "I hear the tank rumble as it shifts its position. The sound of a shot charging resonates from its chamber."
    "I rush out of cover, leaping over the rubble as the tank's blast erupts."
    "The explosion propels me through the air."
    "Landing in the dirt, I roll quickly as blaster bolts thud into the ground where I was just a moment before."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment13)
    "I slam my back into another piece of ruined building."
    "As I do so, I watch Jennica and Teresa scramble up the back of the unguarded tank."
    "The enforcers are all focused on me."
    "They don't even notice as Teresa stabs something into its top hatch." 
    "The cannon begins to charge again, but Jennica grabs it and drags it to aim at a group of nearby enforcers."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment10)
    "The shot fires, sending the enforcers flying into the air as the top hatch of the tank pops open."
    "Amdist the chaos, the Dragonflies disperse."
    "Some run into the shelter of buildings while others start brawling with BC goons."
    "Teresa and Jennica drag some goons out of the hatch."
    "Jennica scrambles inside while Teresa makes quick work of them with her pistol."
    "Some of the BC troops are retreating back to the tank, but the bulk of them advance on my position."
    "But it's too late for them."
    "The Dragonflies have converged on the bulk of the battalion, striking them with stones they picked up from the ground."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment11)
    "The enforcers' attention shifts away from me."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment14)
    "I start to move toward the fighting."
    enforcer "Freeze!"
    "An enforcer taps my back with his gun."
    $ AddChatter(vig4_sc6_attack_1_assault_comment1)
    enforcer "Tell your crew to stand down!"
    play audio "lazer.wav"
    hide bc_enforcer with dissolve
    "The enforcer goes silent. I hear his body fall to the ground."
    "Whipping around, I don't see anyone around me."
    $ AddChatter(vig4_sc6_attack_1_assault_comment2)
    "Jennica and Teresa have fully taken over the tank, and the people of Polaris have routed the battalion."
    "A shadow moves."
    "Faintly, on a rooftop in the distance and silhouetted by fire, a dark figure drops to the ground."
    "And vanishes."
    $ AddChatter(vig4_sc6_attack_1_assault_comment3)
    dflyGuard "Captain Moze?"
    show dflyguard at stream_center with dissolve
    "The leader of the Dragonflies squad approaches me."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment18)
    dflyGuard "We thought we were dead."
    "He glances at the bodies in the street."
    dflyGuard "We didn't all make it, but you gave us a chance to fight back."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment19)
    dflyGuard "I know we didn't leave on the best of terms. But, thank you for saving us."
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment20)
    pause 0.5
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment21)
    pause 0.5
    $ AddChatter(vig4_sc6_attack_1_assault_ama_comment22)
    menu:
        dflyGuard "I know we didn't leave on the best of terms. But, thank you for saving us."
        "You were just doing your job.":
            $ csEngagement += 1
            $ pdEngagement -= 1
            $ reactTarget = "vig4_sc6_attack_sparedflies"
            show screen streamerCommentary
            mS "You were just doing your job. I understand what that's like."
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment23)
            dflyGuard "I appreciate your understanding."
            dflyGuard "Will you join us to defend the plaza?"
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment25)
            mS "We have business elsewhere."
            "The Dragonfly guard looks from me to the tank."
            "He's about to say something, then thinks better of it."
            dflyGuard "Of course."
            dflyGuard "Good luck, Captain."
            $ AddChatter(vig4_sc6_attack_1_assault_comment4)
            "He turns and rejoins his comrades. Together, they walk down the street toward the plaza."
            hide screen streamerCommentary
            hide dflyguard with dissolve
        "It wasn't about you.":
            $ pdEngagement += 1
            $ csEngagement -= 1
            mS "You're welcome, but it wasn't about you."
            mS "I deprived BC of strategic leverage."
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment24)
            "He looks taken aback."
            dflyGuard "Ah, I see."
            dflyGuard "Will you join us to defend the plaza?"
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment25)
            mS "We have business elsewhere."
            "The Dragonfly guard looks from me to the tank."
            "He's about to say something, then thinks better of it."
            dflyGuard "Of course."
            dflyGuard "Good luck, Captain."
            "He turns and rejoins his comrades. Together, they walk down the street toward the plaza."
            hide dflyguard with dissolve
        "I wanted to kill you myself.":
            $ csEngagement -= 2
            $ pdEngagement += 2
            $ reactTarget = "vig4_sc6_attack_killdflies"
            show screen streamerCommentary
            $ vig4_killDflies = True
            mS "Don't thank me. I just wanted the pleasure of killing you myself."
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment27)
            play audio "lazer.wav"
            hide dflyguard with Dissolve(0.5)
            "The guard has half a second to look stunned before a blaster bolt rips through his skull."
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment28)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment29)
            "The rest of the Dragonflies look up, confusion rampant on their faces as I draw my weapon."
            play audio "lazer.wav"
            "Six blaster shots echo in the night."
            "Each of the Dragonflies drops to the ground. Dead."
            $ AddChatter(vig4_sc6_attack_1_assault_ama_comment30)
            hide screen streamerCommentary
    "I turn my back on the quiet street, and stride toward the tank."
    jump vig4_sc6_attack_2

label vig4_sc6_attack_1_split():
    mS "Teresa's right, if we're going to do this we have to do it smart."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment1)
    mS "We'll wait for the battalion to split off, then take the tank when it's just a skeleton crew."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment2)
    mS "Jennica and Teresa, take care of the tank. I'll distract what's left of the squad."
    enS "Behind you."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment3)
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
    if vig4_nickName_bool == True:
        $ AddChatter(vig4_sc6_attack_1_split_ama_comment4)
    else:
        $ AddChatter(vig4_sc6_attack_1_split_ama_comment5)
    "Two BC enforcers drop dead as the rest scramble for cover."
    "I rush to a piece of cover opposite the tank, drawing the enforcers' attention as their bullets cascade by me."
    "Out of the corner of my eye, I see Jennica and Teresa leap onto the tank."
    "The sound of charging resonates in its central cannon as it turns to aim at me."
    "Then Jennica grabs the cannon's barrel and heaves it to the side, pointing it up and away."
    "Teresa stabs something into the tank's top hatch and smoke spurts out from the metal."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment10)
    "I exchange fire with the enforcers."
    "They have the numbers, but not the skill."
    "I take out two of them easily, leaving the last one diving for cover."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment13)
    "Jennica and Teresa are busy pummeling the tank crew on the ground."
    "There's nowhere to run. No help coming for him. He can't escape."
    "I move out of cover and advance toward his position."
    "The second his head peeks up, I blast his skull with a bolt."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment14)
    hide bc_enforcer with dissolve
    "He drops dead."
    "A simple maneuver."
    $ AddChatter(vig4_sc6_attack_1_split_ama_comment15)
    "Holstering my blaster, I watch Jennica and Teresa climb inside the tank and survey the bodies on the ground."
    "One, two, three, four, five..."
    "Where's the sixth?"
    enforcer "Freeze!"
    "An enforcer taps my back with his gun."
    $ AddChatter(vig4_sc6_attack_1_assault_comment1)
    enforcer "Tell your crew to stand down!"
    mS "Easy."
    enforcer "I'm giving the orders here!"
    play audio "lazer.wav"
    hide bc_enforcer with dissolve
    "The enforcer goes silent. I hear his body fall to the ground."
    "Whipping around, I don't see anyone around me."
    $ AddChatter(vig4_sc6_attack_1_assault_comment2)
    "A shadow moves."
    "Faintly, on a rooftop in the distance and silhouetted by fire, a dark figure drops to the ground."
    "And vanishes."
    $ AddChatter(vig4_sc6_attack_1_assault_comment3)
    enS "Hey, captain?"
    "I whip around, drawing my pistol."
    show teresa stream shock at stream_center with dissolve
    "The barrel of my blaster points directly at Teresa's forehead."
    enS "Woah woah, easy."
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
            $ AddChatter(vig4_sc6_attack_1_assault_comment5)
            enS "At least you're safe."
            enS "Shall we, inspect the vessel we just comandeered?"
        "Yeah, I'm good.":
            mS "Yeah, yeah, I'm good."
            enS "Okay, glad to hear it..."
            $ AddChatter(vig4_sc6_attack_1_assault_comment5)
            enS "Shall we, inspect the vessel we just comandeered?"
    mS "Yeah, let's go."
    hide teresa with dissolve
    jump vig4_sc6_attack_2

label vig4_sc6_attack_2():
    show jennica stream neutral at stream_left with dissolve
    "As I climb in through the tank's hatch, Jennica is already sitting in a chair near the front."
    "She's examining a string of buttons and sticks in front of her."
    $ AddChatter(vig4_sc6_attack_2_ama_comment1)
    mS "Any idea how to drive this thing, Jenn?"
    pS "Sure, Cap, doesn't look too complex. We just gotta work as a team."
    $ AddChatter(vig4_sc6_attack_2_ama_comment2)
    pS "I'll take drivin'. Teresa, take care of our shields and engine power."
    show teresa stream neutral at stream_right with dissolve
    pS "Resa, you can also use those machine guns if we need 'em."
    enS "Makes sense."
    pS "Cap, you stay in the center, be our spotter and control the main cannon."
    mS "Roger, let's roll out."
    pS "Aye aye."
    play audio "callRing.wav"
    "As Jennica goes to move the tank forward, a ring suddenly echoes in the tank."
    enS "Someone is calling us."
    pS "On a BigCorp frequency?"
    enS "No. It's not BigCorp, but it has access to their comms?"
    $ AddChatter(vig4_sc6_attack_2_ama_comment4)
    "Access to BigCorp tech? Not affiliated with them?"
    mS "Answer it!"
    "Teresa inputs something into a screen on her side."
    "At the front of the tank, a blue hologram slowly starts to take shape."
    show mac stream neutral at stream_center_mac with dissolve
    "It's MAC."
    $ AddChatter(vig4_sc6_attack_2_ama_comment5)
    mS "MAC!"
    pS "Hey, little guy!"
    enS "Good to see you, MAC."
    $ reactTarget = "vig4_sc6_both_maccall"
    show screen streamerCommentary
    macS "Captain? Moze? I expected it was you. Stealing a tank is very much your style."
    $ AddChatter(vig4_sc6_attack_2_ama_comment6)
    menu:
        macS "Captain? Moze? I expected it was you. Stealing a tank is very much your style."
        "We came back for you!":
            mS "Yes, MAC! We came back for you!"
        "We came to keep you safe!":
            mS "Yes, MAC! We came back to ensure you're safety."
    mS "Are you okay? Are you hurt?"
    if rudeMACGoodbye == True:
        macS "Why do you care? Wasn't this just your mission?"
        $ AddChatter(vig4_sc6_attack_2_ama_comment7)
        "The world goes cold."
        enS "That's not fair, MAC."
        pS "We're a family."
        macS "It's what {i}she{/i} said."
        $ AddChatter(vig4_sc6_attack_2_ama_comment8)
        menu:
            macS "It's what {i}she{/i} said."
            "I'm sorry, MAC.":
                $ kcEngagement += 1
                $ csEngagement += 1
                mS "I'm sorry, MAC."
                mS "I didn't mean it."
                mS "I thought that would make saying goodbye easier."
                mS "But it just made it hurt more."
                mS "I regretted saying it the second the words left my mouth."
                mS "We're here for you now, whatever you need. However we can help."
                mS "Just tell us where you are, and we'll be there for you. Always."
                $ AddChatter(vig4_sc6_attack_2_ama_comment9)
                "MAC pauses for a moment. As if pondering what I've said."
            "The job's not finished.":
                $ kcEngagement -= 1
                $ pdEngagement += 1
                mS "It is a job MAC, and it was, without a doubt, personal."
                mS "But the job's not done."
                mS "BC is here for you, and we're not going to let them take you away."
                mS "I finish what I start. And making sure you're safe, isn't finished yet."
                $ AddChatter(vig4_sc6_attack_2_ama_comment10)
                mS "So tell us where you are. Tell us how we can help you."
                "MAC pauses for a moment. As if pondering what I've said."
    macS "I am okay."
    hide screen streamerCommentary
    macS "But Coil has brought me into the plaza tower and away from the fighting."
    if macViolence >= macPeace:
        macS "And I was doing such a good job with the turret!"
        $ AddChatter(vig4_sc6_attack_2_ama_comment11)
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
        $ AddChatter(vig4_sc6_attack_2_ama_comment12)
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
    $ AddChatter(vig4_sc6_attack_2_ama_comment13)
    play audio "cutCall.wav"
    hide mac with dissolve
    "The signal is cut short."
    enS "That was Coil's voice."
    $ AddChatter(vig4_sc6_attack_2_ama_comment14)
    pS "No doubt. So he has MAC at the top of the tower."
    enS "The barricades they have set up around the plaza will be a bit of trouble."
    $ AddChatter(vig4_sc6_attack_2_ama_comment15)
    mS "We won't have to handle them on our own."
    $ AddChatter(vig4_sc6_attack_2_ama_comment16)
    pS "Cap?"
    mS "That enforcer said BC was preparing a second assault. This first one must have just been to soften up Polaris's defenses."
    mS "When BC launches their next attack, we can use the chaos to break through and get into the tower."
    $ AddChatter(vig4_sc6_attack_2_ama_comment17)
    enS "Efficient and clever."
    pS "A lot of people are gonna die. But I guess that's unavoidable at this point."
    $ AddChatter(vig4_sc6_attack_2_ama_comment18)
    mS "As long as we get MAC. That's what matters."
    "As I finish speaking, a siren rings out from Polaris's plaza."
    "I peer through the tank's scope at the Cruiser hovering in the night sky."
    "A line of dropships have begun careening through the air to Polaris."
    $ AddChatter(vig4_sc6_attack_2_ama_comment19)
    mS "The second attack is starting. Jenn, take us to the plaza."
    $ AddChatter(vig4_sc6_attack_2_ama_comment20)
    "The tank accelerates and we glide smoothly over the ground as a calm before the storm settles over Polaris."
    hide jennica with dissolve
    hide teresa with dissolve
    jump vig4_sc6_attack_3

label vig4_sc6_attack_3():
    "Smoke billows all around us as we navigate Polaris's ruined roads."
    "Flames lick at the sides of buildings."
    "Even in the tank, we can feel the heat from outside."
    "The sounds of battle have struck up again. And they get louder with each second we advance."
    mS "Everyone, get ready."
    $ AddChatter(vig4_sc6_attack_3_ama_comment1)
    "We turn onto the main street."
    "Instant chaos."
    "A dropship screeches by overhead, turrets strafing positions defended by Dragonflies."
    $ AddChatter(vig4_sc6_attack_3_ama_comment2)
    "The Dragonflies have consolidated their defenses behind an enormous barricade blocking the main street into the plaza."
    "A swarm of BC enforcers march down the street."
    "Blaster fire streaks in both directions."
    "As we emerge onto the street, the BC army suddenly cheers."
    $ AddChatter(vig4_sc6_attack_3_ama_comment3)
    pause 0.5
    $ AddChatter(vig4_sc6_attack_3_ama_comment4)
    pS "They think we're on their side."
    $ AddChatter(vig4_sc6_attack_3_ama_comment5)
    enS "We are in their tech."
    $ AddChatter(vig4_sc6_attack_3_ama_comment6)
    pS "What's the play, Cap?"
    $ AddChatter(vig4_sc6_attack_3_ama_comment7)
    menu:
        pS "What's the play, Cap?"
        "Pretend to be with BigCorp, attack the Dragonflies.":
            $ vig4_killDflies = True
            $ pdEngagement += 2
            $ csEngagement -= 2
            $ reactTarget = "vig4_sc6_attack_barricadesurprise"
            show screen streamerCommentary
            mS "Keep our weapons aimed at the Dragonfly position."
            $ AddChatter(vig4_sc6_attack_3_ama_comment9)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_3_ama_comment8)
            mS "Jennica, get us there as quick as you can without being suspcious."
            pS "Roger, Cap."
            "The tank advances on the barricade."
            $ AddChatter(vig4_sc6_attack_3_ama_comment10)
            "Shots from the Dragonflies start to rattle against our hull."
            enS "Shields are at 95\%."
            $ AddChatter(vig4_sc6_attack_3_ama_comment11)
            mS "Good. Teresa, use that machine gun. Hit any Dragonflies that look like threats."
            enS "Roger!"
            "Teresa grabs the machine gun controls and aims for the Dragonfly squads positioned on nearby rooftops."
            "The rapid fire of the machine gun tears into the squads, sending them into a retreat."
            hide screen streamerCommentary
            show vig1_town_stream with hpunch
            "A grenade explodes next to us, sending BC enforcers flying and shaking our hull."
            enS "Tough hit but shields are still at 85\% and holding."
            "I grip the cannon controls and point at a squad of Dragonflies huddled behind nearby cover."
            "The whole tank thrums with energy as the cannon charges."
            $ AddChatter(vig4_sc6_attack_3_ama_comment13)
            "A beam of blue light bursts from the cannon, striking through the rubble."
            "A pillar of flame erupts into the air where the cannon impacted the ground."
            "There's no evidence of the Dragonflies who were hiding behind cover."
            $ AddChatter(vig4_sc6_attack_3_ama_comment14)
            mS "Jenn, keep us moving."
            "We advance slowly at the head of the BC army."
            $ AddChatter(vig4_sc6_attack_3_ama_comment15)
            "Teresa's fire with the machine guns have forced almost all of the Dragonflies into cover."
            "A group tries to take shots at us from a rooftop."
            "I aim the cannon at the base of the building."
            "The thrum of energy."
            "The blue light."
            "Another pillar of flame and the memory of human presence."
            $ AddChatter(vig4_sc6_attack_3_ama_comment16)
            "We keep advancing."
            enS "Contact on the rooftops!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment17)
            show vig1_town_stream with hpunch
            "Another detonation on the side of the tank."
            "I whip a monitor around to view the assailants."
            $ AddChatter(vig4_sc6_attack_3_ama_comment18)
            "It's a group of Dragonflies armed with rocket launchers a couple of buildings away from us."
            "They're reloading the launchers and preparing for another volley."
            mS "Teresa, take them down!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment19)
            enS "I'm trying!"
            "Teresa aims the machine gun at the direction of the squad and begins firing, but too late."
            show vig1_town_stream with hpunch
            "Another rocket streaks through the air and collides with us just as the bolts from the machine gun rip into their bodies."
            mS "Resa, how're we doing?"
            enS "Bad hits. We're at 40\% shields, but holding. We can't take many more of those."
            pS "Cap! We're almost at the barricade!"
            "I turn to look ahead."
            $ vig4_sc6_attack_3_ama_comment19.click = False
            $ AddChatter(vig4_sc6_attack_3_ama_comment20)
            "She's right, we're closing in."
            mS "Alright, Resa, direct our power into engine thrusts and tell me when it's ready to go. We're going to ram through it."
            $ AddChatter(vig4_sc6_attack_3_ama_comment21)
            enS "Are you sure that's--"
            mS "Just do it!"
            mS "Jenn, hit the thurst forward. Hard!"
            pS "Aye aye, Cap!" 
            "The main cannon charges. Our engines hum with excitement."
            enS "Ready, captain!"
            mS "Launch!"
            "Fire erupts from the cannon at the same time as we rush forward."
            "The barricade shatters as the cannon's blast collides with it."
            $ AddChatter(vig4_sc6_attack_3_ama_comment22)
            "Our shields sparkle, the tank ramming into the wall and splitting it apart."
            $ AddChatter(vig4_sc6_attack_3_ama_comment23)
        "Attack BigCorp, rush the barricade.":
            $ pdEngagement -= 1
            $ csEngagement += 1
            $ kcEngagement -= 1
            $ reactTarget = "vig4_sc6_attack_barricadeassault"
            show screen streamerCommentary
            mS "No. BigCorp is still the enemy."
            $ AddChatter(vig4_sc6_attack_3_ama_comment24)
            mS "Jenn, get us to that barricade as fast as you can."
            pS "Aye!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment10)
            enS "Our shields are at 95\% currently!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment10)
            mS "Good. Resa, open fire on any BC goons you see."
            enS "Roger!"
            "Teresa grabs the machine gun controls and aims for the enforcers at the frontline."
            "As the tank accelerates forward, confusion spreads throughout the BC army, throwing them into disarray."
            $ AddChatter(vig4_sc6_attack_3_ama_comment25)
            "Our shields continue to take hits from both sides as blaster fire rattles against our hull."
            hide screen streamerCommentary
            show vig1_town_stream with hpunch
            "A grenade explodes at our side, shaking the tank slightly."
            enS "Shields are at 70\%. We're taking a lot of hits."
            $ AddChatter(vig4_sc6_attack_3_ama_comment26)
            "A dropship begins to aim down toward us."
            mS "We can dish them out too."
            "I grip the controls for the main cannon."
            "The whole tank thrums with energy as the cannon charges."
            "A beam of blue light bursts from the cannon, striking the dropship out of the sky."
            "The ship explodes in a fireball as wreckage falls into Polaris, crashing into the BC swarm."
            $ AddChatter(vig4_sc6_attack_3_ama_comment27)
            pause 0.5
            $ AddChatter(vig4_sc6_attack_3_ama_comment29)
            mS "Jenn, how are we doing?"
            pS "We're close, just a bit further!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment28)
            enS "Captain, we're starting to take less fire from the Dragonflies."
            show vig1_town_stream with hpunch
            "Another detonation on the side of the tank."
            "I whip a monitor around to view the assailants."
            "It's a group of BC enforcers armed with rocket launchers."
            $ AddChatter(vig4_sc6_attack_3_ama_comment30) 
            "They're on a building near the back of the attack force."
            "They're reloading the launchers and preparing for another volley."
            $ AddChatter(vig4_sc6_attack_3_ama_comment31)
            "I whip the main cannon controls around, aiming them at the base of the building."
            "The cannon charges."
            "The rocket streaks through the air."
            "The beam of blue light strikes the building as another pillar of flame erupts into the night air."
            show vig1_town_stream with hpunch
            "The rocket detonates close to us, but not a direct hit."
            $ AddChatter(vig4_sc6_attack_3_ama_comment32)
            enS "Shields are at 30\%."
            pS "Cap! We're almost at the barricade!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment33)
            "I turn to look ahead."
            $ AddChatter(vig4_sc6_attack_3_ama_comment19)
            "She's right, we're closing in."
            mS "Alright, Resa, direct our power into engine thrusts and tell me when it's ready to go. We're going to ram through it."
            enS "Are you sure that's--"
            mS "Just do it!"
            mS "Jenn, hit the thurst forward. Hard!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment21)
            pS "Aye aye, Cap!" 
            "The main cannon charges. Our engines hum with excitement."
            $ vig4_sc6_attack_3_ama_comment19.click = False
            enS "Ready, captain!"
            mS "Launch!"
            "Fire erupts from the cannon at the same time as we rush forward."
            "The barricade shatters as the cannon's blast collides with it."
            $ AddChatter(vig4_sc6_attack_3_ama_comment22)
            "Our shields sparkle, the tank ramming into the wall and splitting it apart."
            $ AddChatter(vig4_sc6_attack_3_ama_comment23)
        "Attack both Dragonflies and BigCorp.":
            $ vig4_killDflies = True
            $ pdEngagement += 1
            $ csEngagement -= 1
            $ kcEngagement += 1
            $ reactTarget = "vig4_sc6_attack_barricadechaos"
            show screen streamerCommentary
            mS "Screw it."
            $ AddChatter(vig4_sc6_attack_3_ama_comment34) 
            mS "Jenn, get us to that barricade as fast as you can."
            $ AddChatter(vig4_sc6_attack_3_ama_comment35)
            pS "Aye!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment10)
            enS "Our shields are at 95\% currently!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment11)
            mS "Good. Resa, open fire at will."
            enS "Roger!"
            "Teresa grabs the machine gun controls and whips it around."
            "The bolts of machine gun rounds tear into soliders: BC enforcers and Dragonflies alike."
            $ AddChatter(vig4_sc6_attack_3_ama_comment36)
            "Teresa lays on the trigger hard, striking Dragonflies on the rooftops, then BC enforcers on the ground."
            "Confusion spreads through both sides as blaster fire pings off the tank's sides."
            enS "Shields are at 90\%, Captain."
            "I grip the controls for the main cannon. The entire tank thrums with energy as it charges."
            hide screen streamerCommentary
            show vig1_town_stream with hpunch
            "Above, a dropship aims down toward our position, turrets sending fire against our hull."
            "A beam of blue light bursts from the cannon, striking the dropship out of the sky."
            $ AddChatter(vig4_sc6_attack_3_ama_comment38)
            "The ship explodes in a fireball as wreckage falls into Polaris, crashing into the BC swarm."
            mS "Jenn, how are we doing?"
            $ AddChatter(vig4_sc6_attack_3_comment39)
            pS "We're close, just a bit further!"
            show vig1_town_stream with hpunch
            "An explosion suddenly detonates against our side."
            $ AddChatter(vig4_sc6_attack_3_ama_comment30)
            mS "Teresa, report!"
            "I whip the monitor around, looking for the assailants."
            enS "Shields are down to 60\%. We're taking fire from both sides and losing energy rapidlly!"
            "I locate the smoke streaking through the air."
            "Dragonflies on a nearby building are loading rocket launchers."
            $ AddChatter(vig4_sc6_attack_3_ama_comment40)
            "I drop the cannon to aim at the base of the building, charging up another blast."
            "But I'm too late."
            "A bright flashing rocket streaks toward us just as I fire the cannon."
            show vig1_town_stream with hpunch
            "The rocket impacts on our side, but at the same time, the tank's blast detonates on the building."
            "A pillar of flame erupts into the sky as the edifice crumbles to the ground."
            $ AddChatter(vig4_sc6_attack_3_ama_comment41)
            pS "They're throwing grenades!"
            "Teresa fires the machine gun full auto as BC enforcers break ranks to move toward our position."
            "Most of them are cut down, but a couple are able to lob grenades that land at our side."
            show vig1_town_stream with hpunch
            "They detonate, jostling the vehicle."
            $ AddChatter(vig4_sc6_attack_3_ama_comment42)
            enS "Shields are down to 30\%! We can't take much more of this!"
            pS "Cap! We're almost at the barricade!"
            "I turn to look ahead."
            $ AddChatter(vig4_sc6_attack_3_ama_comment19)
            "She's right, we're closing in."
            mS "Alright, Resa, direct our power into engine thrusts and tell me when it's ready to go. We're going to ram through it."
            enS "Are you sure that's--"
            mS "Just do it!"
            mS "Jenn, hit the thurst forward. Hard!"
            $ AddChatter(vig4_sc6_attack_3_ama_comment21)
            pS "Aye aye, Cap!" 
            "The main cannon charges. Our engines hum with excitement."
            $ vig4_sc6_attack_3_ama_comment19.click = False
            enS "Ready, captain!"
            mS "Launch!"
            "Fire erupts from the cannon at the same time as we rush forward."
            "The barricade shatters as the cannon's blast collides with it."
            $ AddChatter(vig4_sc6_attack_3_ama_comment22)
            "Our shields sparkle, the tank ramming into the wall and splitting it apart."
            $ AddChatter(vig4_sc6_attack_3_ama_comment23)
    "The tank isn't supposed to go this fast. And it's not supposed to turn this hard."
    "But Jennica wrangles it under control as we careen to a stop at the base of the tower."
    $ AddChatter(vig4_sc6_attack_3_ama_comment43)
    "I open the top hatch and scramble out."
    "The barricade at the end of the plaza begins to crumble as the Dragonflies disperse."
    $ AddChatter(vig4_sc6_attack_3_ama_comment44)
    "BC closes in on the plaza."
    $ AddChatter(vig4_sc6_attack_3_ama_comment45)
    "More dropships stream down from the cruiser."
    $ AddChatter(vig4_sc6_attack_3_ama_comment46)
    "We don't have much time."
    "War has come."
    $ AddChatter(vig4_sc6_attack_3_ama_comment48)
    menu:
        "War has come."
        "This is it.":
            mS "This is it. The end of the road."
        "We're not making it out of this.":
            mS "I don't know if I see a way out of this."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    mS "This is where our score gets settled."
    $ AddChatter(vig4_sc6_attack_3_ama_comment49)
    pause 0.5
    $ AddChatter(vig4_sc6_attack_3_ama_comment50)
    pause 0.5
    $ AddChatter(vig4_sc6_attack_3_ama_comment51)
    "I watch the burning horizon as Polaris crumbles."
    if vig2_outlawEpilogue == True:
        $ pdEngagement += 3
        $ kcEngagement += 2
        $ csEngagement += 1
        unknown "Ugh, and here I thought you all would have toughened up in the last two weeks."
        "A familiar voice...but from where?"
        $ AddChatter(vig4_sc6_defend_5_comment15)
        enS "Captain, we're being hailed by a new signal, I don't--"
        show vig1_town_stream with hpunch
        "A ship suddenly streaks overhead, careening toward the BC dropships."
        $ AddChatter(vig4_sc6_defend_5_comment16)
        "Its wings open into attack formation as green bolts of light rip into a dropship, sending it to the ground."
        "Three more fighters fly by immediately after. Then another. Then another."
        $ AddChatter(vig4_sc6_defend_5_comment17)
        "A fleet of attack ships."
        pS "Who the--that's one hell of a pilot?"
        show reginald stream bigmad at stream_center with dissolve
        $ AddChatter(vig4_sc6_defend_5_comment18)
        goon "I really don't get paid enough for this shit."
        show jennica stream shock at stream_left
        pS "Reginald!?"
        $ AddChatter(vig4_sc6_defend_5_comment19)
        goon "Matticus sends his regards."
        goon "Said he had a debt that needed paying off."
        $ AddChatter(vig4_sc6_defend_5_comment20)
        show jennica stream neutral
        "The swarm of attack ships engage the BC dropships, delaying their advance."
        $ AddChatter(vig4_sc6_defend_5_comment21)
        goon "So take care of whatever you got to do on the ground. We'll handle the air shit."
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
        hide reginald with dissolve
    else:
        $ pdEngagement += 1
        $ kcEngagement += 3
        $ csEngagement += 2 
        unknown "MOXIE!"
        pS "Cap, we're pickin' up a new signal!"
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
    pS "Cap, you're gonna want to get a move on." 
    mS "Not without you two."
    show teresa stream neutral at stream_right with dissolve
    enS "Negative, Captain."
    mS "What!?"
    $ AddChatter(vig4_sc6_defend_5_comment24)
    enS "If BC takes the plaza it won't matter what you do up there, we'll all be toast."
    $ AddChatter(vig4_sc6_defend_5_comment25)
    pS "You go get the kid. We'll keep a path clear down here."
    $ AddChatter(vig4_sc6_defend_5_comment26)
    menu:
        pS "You go get the kid. We'll keep a path clear down here."
        "I'm not leaving you.":
            mS "No way, I'm not leaving you two!"
            enS "You're not leaving anything."
            pS "We're just splittin' up to make the mission succeed."
            "Jennica and Teresa" "We've got this."
            if jennicaRomance == True:
                $ csEngagement += 1
                "Jennica suddenly comes up from the tank. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                $ AddChatter(vig4_sc6_defend_5_comment28)
                pS "Go do what you do best, Moze."
            elif teresaRomance == True:
                $ kcEngagement += 2
                "Teresa suddenly comes up from the tank. She faces me dead on."
                "I can't move."
                "She grabs my head and pulls me in for a kiss."
                $ AddChatter(vig4_sc6_defend_5_comment27)
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
                $ AddChatter(vig4_sc6_defend_5_comment28)
                pS "Go do what you do best, Moze."
            elif teresaRomance == True:
                "Teresa suddenly comes up from the tank. She faces me dead on."
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
    $ AddChatter(vig4_sc7_1_defend_comment1)
    "A distant voice calls from up above."
    cS "Up here. Come along."
    $ AddChatter(vig4_sc7_1_defend_comment2)
    "A series of stairs that winds up to the top of the tower."
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
    "I step across the threshold into a wide room."
    $ AddChatter(vig4_sc7_1_defend_comment9)
    show vig2_datacenter_stream onlayer background with dissolve
    show coil stream neutral at stream_left with dissolve
    "Coil stands in the center, in front of a massive computer console."
    $ AddChatter(vig4_sc7_1_defend_comment10)
    cS "Well, you made it."
    if vig4_killDflies == True:
        cS "You had to murder some good people to do it. But you arrived."
        $ AddChatter(vig4_sc7_1_attack_ama_comment1)
    else:
        pass
    "Coil turns to face us. His face looks haggard, his eyes bloodshot."
    $ reactTarget = "vig4_sc6_attack_finding_coil"
    show screen streamerCommentary
    menu:
        "Coil turns to face us. His face looks haggard, his eyes bloodshot."
        "Where is MAC?":
            mS "Where is MAC?"
            $ AddChatter(vig4_sc7_1_attack_ama_comment2)
            cS "Always so direct."
            cS "MAC is no longer any of your concern, Moze."
            cS "You delivered him, he is our responsibility."
            $ AddChatter(vig4_sc7_1_attack_ama_comment3)
            cS "And he is safe."
            if macViolence > macPeace:
                cS "You know he insisted on operating a turret when BigCorp arrived."
                cS "Said he would \"make those BC scum pay.\""
                $ AddChatter(vig4_sc7_1_attack_ama_comment4)
                mS "Sitting in a turret on the frontlines. Is that really what you consider \"safe\"?"
                cS "No. But he insisted."
                cS "And as I'm sure you're aware, he can be quite strong-willed."
                cS "He got it from you after all."
                hide screen streamerCommentary
                amaS "Mozely can be quite stubborn."
                show ama stream neutral at stream_right with dissolve
                "I whip around."
                "Ama steps into the wide room, rifle drawn, aimed directly at Coil."
                cS "I meant the bloodlust."
                $ AddChatter(vig4_sc7_1_attack_ama_comment5)
                "Ama tilts her head."
                $ AddChatter(vig4_sc7_1_attack_ama_comment6)
                amaS "That too."
            else:
                cS "You know he insisted on providing first aid to the people who were first injured by BigCorp's assault."
                cS "Said he had to \"take care of the people around him.\""
                $ AddChatter(vig4_sc7_1_attack_ama_comment4)
                mS "Being a frontline medic isn't exactly what I would consider \"safe.\""
                cS "No. But he insisted." 
                cS "And I'm sure you're aware he can be quite strong-willed."
                cS "He got it from you after all."
                hide screen streamerCommentary
                amaS "Mozely can be quite stubborn."
                show ama stream neutral at stream_right with dissolve
                "I whip around."
                "Ama steps into the wide room, rifle drawn, aimed directly at Coil."
                cS "I meant the urge to help other people."
                $ AddChatter(vig4_sc7_1_attack_ama_comment5)
                "Ama tilts her head."
                $ AddChatter(vig4_sc7_1_attack_ama_comment6)
                amaS "Guess that has been a phase recently."
                $ AddChatter(vig4_sc7_1_attack_ama_comment9)
        "Got a plan for getting out of this?":
            mS "So, do you have a plan for getting out of this."
            cS "I do."
            cS "The top of this tower can be converted into a makeshift rocket."
            cS "We will be able to finish the mission, where you failed."
            $ AddChatter(vig4_sc7_1_attack_ama_comment7)
            mS "And you're okay with all of Polaris dying while you escape?"
            cS "It breaks my heart."
            cS "But we have done what we could. What we were supposed to do."
            $ AddChatter(vig4_sc7_1_attack_ama_comment8)
            cS "MAC is no longer any of your concern, Moze."
            cS "You delivered him, he is our responsibility."
            $ AddChatter(vig4_sc7_1_attack_ama_comment3)
            if macViolence > macPeace:
                cS "You know he insisted on operating a turret when BigCorp arrived."
                cS "Said he would \"make those BC scum pay.\""
                $ AddChatter(vig4_sc7_1_attack_ama_comment4)
                mS "Sitting in a turret on the frontlines. Is that really what you consider \"safe\"?"
                cS "No. But he insisted."
                cS "And as I'm sure you're aware, he can be quite strong-willed."
                cS "He got it from you after all."
                amaS "Mozely can be quite stubborn."
                show ama stream neutral at stream_right with dissolve
                "I whip around."
                "Ama steps into the wide room, rifle drawn, aimed directly at Coil."
                cS "I meant the bloodlust."
                $ AddChatter(vig4_sc7_1_attack_ama_comment5)
                "Ama tilts her head."
                $ AddChatter(vig4_sc7_1_attack_ama_comment6)
                amaS "That too."
            else:
                cS "You know he insisted on providing first aid to the people who were first injured by BigCorp's assault."
                cS "Said he had to \"take care of the people around him.\""
                $ AddChatter(vig4_sc7_1_attack_ama_comment4)
                mS "Being a frontline medic isn't exactly what I would consider \"safe.\""
                cS "No. But he insisted." 
                cS "And I'm sure you're aware he can be quite strong-willed."
                cS "He got it from you after all."
                show ama stream neutral at stream_right with dissolve
                "I whip around."
                "Ama steps into the wide room, rifle drawn, aimed directly at Coil."
                amaS "Mozely can be quite stubborn."
                cS "I meant the altruistic urge to help other people."
                $ AddChatter(vig4_sc7_1_attack_ama_comment5)
                "Ama tilts her head."
                $ AddChatter(vig4_sc7_1_attack_ama_comment6)
                amaS "Guess that has been a phase recently."
                $ AddChatter(vig4_sc7_1_attack_ama_comment9)
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
            $ kcEngagement += 1
            mS "I came for MAC."
            mS "I'm not leaving without him."
            $ AddChatter(vig4_sc7_1_defend_comment14)
            "Coil sighs."
            cS "I assumed that was the case."
            cS "I'm disappointed. After everything that happened, you couldn't just walk away."
            $ AddChatter(vig4_sc7_1_defend_comment15)
            cS "MAC is gone."
            amaS "Bullshit."
            amaS "If that were true you wouldn't still be here."
            cS "How perceptive. And yet you still have no idea what you're doing."
            $ AddChatter(vig4_sc7_1_defend_comment16)
            cS "Flailing around in the darkness with no purpose."
            $ AddChatter(vig4_sc7_1_defend_comment17)
        "I came to help.":
            $ csEngagement += 1
            mS "I came to help, to fight off BigCorp."
            $ AddChatter(vig4_sc7_1_attack_ama_comment10)
            "Coil tilts his head, as if inspecting me."
            cS "Help?"
            cS "I think we've had enough of your \"help.\""
            cS "You had to come back and visit more destruction upon us."
            $ AddChatter(vig4_sc7_1_attack_ama_comment12)
            if vig4_killDflies == True:
                cS "You killed my men because you wanted to, didn't you?"
                $ AddChatter(vig4_sc7_1_attack_ama_comment13)
                cS "You never even thought about helping us."
            else:
                cS "But it's always so hard to know with you, isn't it, Moze."
                cS "Here we stand, in the midst of a war. And you happen to be at the center of it."
            cS "Is this what your help means, Moze?"
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
    "Every shot is absorbed by the shield."
    $ AddChatter(vig4_sc7_1_defend_comment20)
    jump vig4_sc7_2