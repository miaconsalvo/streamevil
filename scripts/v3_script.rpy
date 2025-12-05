label vignette3Start():
    #We want to reset these before the start of the vignette
    $ menu = adv_menu
    $ viewCount = 0
    $ vignette1 = False
    $ vignette2 = False
    $ vignette3 = True
    $ vignette4 = False
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
    $ blueitChoiceCheck = False
    $ flinchCheck = 0
    $ flinch_viewcountCheck = False
    $ flinch_topfanCheck = False
    $ flinch_audienceCheck = False
    $ flinchView = False
    $ blueitView = False
    $ loopdView = False
    $ screenComplete = False
    $ macroChoice = False
    $ chatter_list = []
    if vig2_outlawEpilogue == True:
        $ viewershipHigh = True
        $ viewershipMed = False
        $ viewershipLow = False
    else:
        $ viewershipHigh = False
        $ viewershipMed = False
        $ viewershipLow = True
    #$ csEngagement = 0
    #$ kcEngagement = 0
    #$ pdEngagement = 0
    "It's been one week since you last streamed {i}Oakley 2: Settle the Score{/i}."
    "Episode 3 released today so you have a stream scheduled for this evening."
    scene streamview with dissolve
    show screen streamDetails
    show screen streamChat
    "You begin the stream and then boot up the game."
    "You load the save file you were previously playing, and are ready to go."
    $ narrator = alt_narrator
    if vig2_outlawEpilogue == True:
        jump vig3outlawstart
    else:
        jump vig3marshalstart
###SCENE1###
label vig3outlawstart():
    if viewershipHigh == True:
        $ viewCount += 5
    else:
        $ viewCount += 3
    show shiphub_stream at topleft onlayer background with dissolve
    $ AddChatter(vig3_startstream_comment1)
    pause 0.5
    if viewershipHigh == True:
        $ AddChatter(vig3_startstream_comment2)
        pause 0.5
    $ AddChatter(vig3_startstream_comment3)
    pause 0.5
    $ AddChatter(vig3_startstream_comment4)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter(vig3_startstream_comment5)
    play backAudio "shipHum.wav" volume 0.2 fadein 1.0
    "The Oakley is quiet today, and this coffee feels like I'm trying to cure every sleepless night I've had for the past few days."
    "It's nice always being the first one up, if it's even morning?"
    $ AddChatter(vig3_startstream_comment0)
    "I check the clock on the wall."
    $ AddChatter(vig3_outlawstart_comment1)
    mS "Yep, morning."
    "\"I've got lots more work where that came from.\" Arrogant rat. I should've gone back and blown his fortress to ash."
    $ AddChatter(vig3_outlawstart_comment2)  
    pause 0.5
    $ AddChatter(vig3_outlawstart_comment3)  
    pause 0.5 
    $ AddChatter(vig3_outlawstart_comment4)  
    "I take an uninterested sip of my drink, wrapping both hands around the glass."
    "I can't believe I'm letting this get to me. Hell, I've done worse, we've done worse. This probably wouldn't even crack the top five."
    $ viewCount += 3
    $ AddChatter(vig3_outlawstart_comment5)
    pause 0.5
    $ AddChatter(vig3_outlawstart_comment6)
    pause 0.5
    $ AddChatter(vig3_outlawstart_comment7)
    pause 0.5
    $ AddChatter(vig3_outlawstart_comment8)
    "But are we doing right if we hurt people in the process?" 
    "What's the point of all of this?"
    "I find myself staring off into the distance." 
    "With my back to the doorl, I don't see Teresa come in."
    show teresa stream neutral at stream_right with dissolve
    "She's in her usual clothes, her shirt is uncharacteristically wrinkled and half tucked, a button undone at the bottom."
    enS "Early start, Captain?"
    mS "You know me: first one up, last one down." #Maybe cheekier##
    enS "That's a recipe for sleep deprivation I fear."
    "She pulls up a chair next to me grabs the warm metal pitcher from the table and fills her own cup."
    mS "And aren't you just the picture of a good night's sleep."
    enS "Hardly..."
    mS "Fighting with Jennica didn't tire either of you out?"
    $ AddChatter(vig3_outlawstart_comment9)
    enS "I can't speak for her, she's been camping in the cockpit since yesterday."
    $ AddChatter(vig3_outlawstart_comment10)
    pause 1
    $ AddChatter(vig3_outlawstart_comment11)
    pause 0.5
    $ AddChatter(vig3_outlawstart_comment11add)
    mS "Luckily there isn't a bathroom in there."
    show teresa stream happy
    "She lets out a forced chuckle and the room goes quiet and cold for a moment."
    show teresa stream neutral
    enS "There's uh, no news on Sallent."
    "I straighten myself as best as I can."
    enS "You know, that MAC is remarkable, the database access he has, even for a BigCorp bot. I could easily get you a news bulletin from the Central Planets if you wanted."
    mS "A talented little guy for sure."
    $ AddChatter(vig3_outlawstart_comment12)
    enS "But Sallent. Nothing. Not even a distress signal. Not a single report since we left Gibian V."
    mS "Hard to ask people to risk Gray Fever for a check-in. Hell, who knows if anyone is working comms there anymore."
    "There's a long pause."
    enS "I don't... this isn't proper to say."
    enS "I wondering if you— if we— made the right choice."
    "She's looking away from me now, its not regret it's just the weight of it all."
    $ AddChatter(vig3_outlawstart_comment13)
    pause 0.5
    $ AddChatter(vig3_outlawstart_comment14)
    pause 0.5
    $ AddChatter(vig3_outlawstart_comment15)
    enS "We did what we did to keep safe and what we're doing requires... tough choices. Such is the nature of our mission."
    mS "Resa..."
    $ AddChatter(vig3_outlawstart_comment16)
    enS "We can't always expect to feel good about what we do. It's a difficult call to make."
    $ AddChatter(vig3_outlawstart_comment17)
    mS "Please."
    play audio "disruptiveBang.wav" volume 1.2
    show teresa stream upset
    enS "{i}She won't even look at me Moze!{/i}"
    $ AddChatter(vig3_outlawstart_comment18)
    $ reactTarget = "vig3_sc1_out"
    show screen streamerCommentary
    "She slams the table and her glass spills on the ground with a clang. Her breath is strained as she calms herself."
    "I set my cup down gently."
    show teresa stream neutral
    enS "We weren't the best people before we started this, and I know you and Jennica have more history than even I know about." 
    enS "But at least we dealt with things together."
    $ AddChatter(vig3_outlawstart_comment19)
    pause 0.5 
    $ AddChatter(vig3_outlawstart_comment20)
    "I don't respond. Teresa needs this." #Consider adding choices
    enS "But ever since we took that— took MAC, it's been one awful choice after another. Barely escaping every time..."
    $ AddChatter(vig3_outlawstart_comment21)
    "Teresa lets out a defeated sigh. Before I can respond, Jennica's voice echoes through the speaker."
    hide screen streamerCommentary
    pS "Captain! Comms comin' in, fuzzy but— I reckon it's the Dragonflies."
    "Teresa shoots up, I place a hand on her shoulder."
    $ viewCheck1 = viewCount
    menu:
        "Advise Teresa on how to proceed."
        "Be calm.":
            $ kcEngagement += 1 #Logic: kitcat likes Teresa and prefers the gentler comment
            $ engineerApproval += 1
            mS "Take ten seconds. I'll see you there."
            $ AddChatter(vig3_outlawstart_calm_comment22)
            pause 0.5
            $ AddChatter(vig3_outlawstart_calm_comment23)
            #no approval change
        "Be firm.":
            $ kcEngagement -= 1
            mS "You can't go in like that. Fix yourself, I'll see you there."
            $ AddChatter(vig3_outlawstart_firm_comment24)
            #increase approval
    $ setEngagement()
    "I wait until I can feel her shoulder relax and walk out and down the hall, alone."
    hide teresa with dissolve
    jump vig3_sc2

label vig3marshalstart(): 
    show shiphub_stream at topleft onlayer background with dissolve
    if viewershipHigh == True:
        $ viewCount += 5
    else:
        $ viewCount += 4
    $ AddChatter(vig3_startstream_comment1)
    pause 0.5
    $ AddChatter(vig3_startstream_comment3)
    pause 0.5
    $ AddChatter(vig3_startstream_comment4)
    play backAudio "shipHum.wav" volume 0.2 fadein 1.0
    "The Oakley is quiet today, and this coffee feels like I'm trying to cure every sleepless night I've had for the past few days."
    "It's nice always being the first one up, if it's even morning?"
    "I check the clock on the wall."
    mS "Yep, morning."
    "\"Don't worry. You'll get yours.\""
    "Annoying rat. He's lucky I didn't turn back and blow his fortress to ash."
    $ AddChatter(vig3_marshalstart_comment1)
    pause 0.5 
    $ AddChatter(vig3_marshalstart_comment2)
    pause 1
    $ AddChatter(vig3_marshalstart_comment3)
    "I take an uninterested sip of my drink, wrapping both hands around the glass."
    "I'm letting this get to me. When have I ever taken one of Sav's threats seriously?" 
    "I'm sure he wants to see {i}her{/i} even less than me."
    "We're trying to be better, but what's the point if we're all arrested, if they take MAC away."
    $ viewCount += 1
    $ AddChatter(vig3_marshalstart_comment4)
    "I find myself staring off into the distance." 
    "With my back to the door I don't see Jennica come in."
    show jennica stream neutral at stream_left with dissolve
    "She's wearing her usual clothes, but her eyes are dark from exhaustion."
    pS "Up early?"
    mS "Surprisingly so are you."
    pS "Can't be early if ya ain't sleep."
    mS "Nothing quite like the comfort of my pilot being sleep deprived."
    pS "Thank the Makers she flies herself well enough."
    "She pulls up a chair next to me, grabs the warm metal pitcher from the table and fills a glass of her own. She takes out a small flask." 
    "I hold my cup out. She pours a bit inside mine and her own, we cheers in the air."
    mS "Fighting with Teresa didn't tire either of you out I suppose?"
    pS "Don't know 'bout her, I've been camping in the cockpit so I don't find out."
    mS "Luckily there isn't a bathroom in there."
    pS "Takes a brave woman to go relieve herself in times like these."
    "Jennica's joke ends in a forced chuckle. The room goes quiet and cold for moment."
    pS "I'm not just staying in the cockpit to avoid Resa..."
    "I straighten myself."
    pS "I keep dreaming about getting a hit on the scanners, and I don't make it to the helm in time."
    mS "You're not the only who can fly the Oakley."
    pS "No, but I'm the only one that can outrun Ama. We got lucky but— no offense to our saving grace— I don't like not knowing how much distance we may or may not have."
    "There's a long pause."
    $ AddChatter(vig3_marshalstart_comment5)
    pS "Every little blip on the scanner makes me jump, Cap. That's until I find out it's some stoved-up space junk floatin' from a click over."
    "She looks away from me to find the words."
    pS "I wonder... if we made the right choice. As wrong as it sounds."
    mS "Jenn..."
    pS "You're right, those people needed that aid, I don't regret it."
    pS "But we gotta be okay with the tough choices sometimes, be more logical, make the hard call."
    mS "Is that really how you're feeling?"
    "Jennica goes quiet."
    pS "She can barely look at me Moze..."
    show jennica stream angry
    $ reactTarget = "vig3_sc1_mar"
    show screen streamerCommentary
    "Jennica smacks her glass away, it falls to the ground with a clang. She takes a quiet moment to calm herself." 
    "I set my cup down gently."
    pS "We're doing better, and that's all fine and good. And hell, I'll stand by what I said."
    pS "But we need to be more united on things if we're gonna make it."
    "I don't respond." #Consider adding multiple options#
    pS "I like the kid. But we've been over our heads from the start..." 
    show jennica stream neutral
    pS "She's gonna find us, and I'm sure BigCorp isn't hung up on whether we're brought back in one piece."
    "Jennica lets out a defeated sigh. Teresa's voice echoes through the speaker before I can answer."
    hide screen streamerCommentary
    enS "Captain! There's a transmission for us— I'm certain it's the Dragonflies."
    "Jennica shoots up, I place a hand on her shoulder."
    $ viewCheck1 = viewCount
    menu:
        "Advise Jennica on how to proceed."
        "Be calm.":
            $ csEngagement += 1 #Logic: Coriolis likes Jennica so prefers the gentler comment
            $ pilotApproval += 1
            mS "Take ten seconds. I'll see you there."
            $ AddChatter(vig3_marshalstart_calm_comment6)
        "Be firm.":
            $ csEngagement -= 1
            mS "You can't go in like that. Fix yourself, I'll see you there."
            $ AddChatter(vig3_marshalstart_firm_comment7)
    $ setEngagement()
    "When Jennica's shoulder relaxes I walk out and down the hall, alone."
    hide jennica with dissolve
    jump vig3_sc2

label vig3_sc2():
    if viewershipHigh == True:
        $ viewCount += 4
    else:
        $ viewCount += 3
    stop backAudio
    play music "soundtrack/vig1scratchtrack.wav" volume 0.8 loop fadein 1.0
    show cockpit_mess_stream at topleft onlayer background with dissolve
    hide shiphub_stream
    "The Cockpit is a mess, Jennica has made quick work at holing up in here. MAC's sitting patiently in the corner, he's been spending more time in here than usual."
    "Teresa is working to get the message on the screen while Jennica hangs back next to him."
    $ AddChatter(vig3_sc2_cockpit_comment1)
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    enS "Here it is..."
    if viewershipHigh == True:
        $ AddChatter(vig3_sc2_cockpit_comment2)
    $ AddChatter(vig3_sc2_cockpit_comment3)
    "A voice sparks up from the speaker, it's staticky and every few words are cut."
    if viewershipHigh == True:
        $ AddChatter(vig3_sc2_cockpit_comment4)
    $ AddChatter(vig3_sc2_cockpit_comment5)
    dflycontact "Captain Moze of the Oakley. My name is {b}STATIC{/b} of the Dragonflies."
    "The cockpit is silent."
    dflycontact "I know you {b}STATIC{/b} Dr. Vanas' work. And we are contacting {b}STATIC{/b} drop-off {b}STATIC{/b}."
    if viewershipHigh == True:
        $ AddChatter(vig3_sc2_cockpit_comment6)
    mS "Teresa can you get this any clearer?"
    if viewershipHigh == True:
        $ AddChatter(vig3_sc2_cockpit_comment7)
    enS "Captain, I'm trying but I'm certain there's something wrong on our end."
    pS "Probably mucked our comms on the way out of Gib V." 
    pS "Needed an upgrade anyway, but I've been puttin' it off for..."
    "Jennica looks at MAC."
    pS "A while..."
    dflycontact "...at {b}STATIC{/b} sector, coordinates {b}STATIC{/b} message {b}STATIC{/b} lost {b}STATIC{/b} reattempt {b}STATIC{/b} five days. Over and {b}STATIC{/b}."
    play audio "cutCall.wav" volume 1.5
    enS "I've recorded the message for what it's worth, but if we want those coordinates in five days we'll need better gear."
    pS "That ain't much time."
    menu:
        pS "That ain't much time."
        "Not the first time.":
            mS "Not the first time we've been pressed against the wall."
        "We're used to it.":
            mS "We should be used to a tight schedule by now. "
    "We take a moment to think."
    show mac stream neutral at stream_center_mac with dissolve
    macS "Dad..."
    #$ AddChatter(vig3_sc2_cockpit_comment8)
    #if viewershipHigh == True:
    #    $ AddChatter(vig3_sc2_cockpit_comment9)
    #$ reactTarget = "vig3_sc2_macdad" #reply chats at 6:14
    #show screen streamerCommentary
    "All eyes turn to MAC. Jennica's expression softens and I watch Teresa's face rise with curiosity then fall." 
    show jennica stream neutral at stream_left
    #show mac stream neutral at stream_center_mac
    "MAC sits innocently in his chair, looking off to the expanse of open space, searching for the answer to a question he doesn't know how to ask."
    mS "What's going on, bud?"
    play audio "macSad.wav" volume 1.2
    macS "I— do not know."
    show jennica stream neutral at stream_left
    pS "Well, that's a first." #(multiple=2) #might break the dialogue box positions
    enS "That's remarkable." #(multiple=2) #might break the dialogue box positions
    "The two exchange a quick look before turning away, remembering that they're still fighting. I turn the focus away from MAC."
    $ AddChatter(vig3_sc2_cockpit_comment10)
    mS "Let's consider our options, come up with a plan to get our comms back in working order. Meet at the Bridge in an hour to debrief."
    #hide screen streamerCommentary
    pS "Yes, Captain!" #(multiple=2) #same as before, we could also define a new character as "teresa and jennica"
    enS "Yes, Captain!" #(multiple=2) #same as before, we could also define a new character as "teresa and jennica"
    hide jennica with dissolve
    hide teresa with dissolve
    hide mac with dissolve
    show ship_hallway_stream at topleft onlayer background with dissolve
    "I turn to the door and go out into the hall."
    hide cockpit_mess_stream
    play audio "macPester.wav" volume 1.5
    macS "Captain!"
    show mac stream shock at stream_center_mac with vpunch
    "I can't help but jump as I'm stopped by a tiny purple metal leaf and an excited MAC."
    mS "Jeez, MAC, remind me to let you take point on stealth missions next time."
    show mac stream neutral at stream_center_mac
    macS "Might I make a suggestion?"
    mS "A suggestion?"
    macS "Yes, I have an idea!"
    if viewershipHigh == True:
        $ AddChatter(vig3_sc2_hallway_comment1)
        pause 0.5
        $ AddChatter(vig3_sc2_hallway_comment2)
    mS "MAC, respectfully, I don't have time for this—"
    $ AddChatter(vig3_sc2_hallway_comment3)
    macS "Which is precisely why I have a suggestion. I was scanning BigCorp databases..."
    "I feel frustration twisting my face." ##Dialogue choice that links to MAC's reaction here.##
    menu:
        "I feel frustration twisting my face."
        "MAC, that's dangerous!":
            $ kcEngagement -= 1 #Logic: This is a rougher tone so kitcat doesn't like it (it's also more concerned with crew than with MAC)
            mS "MAC, please tell me after all this work to keep us safe you're not poking in BigCorp's networks!"
            #Pessimism
        "MAC, it's not safe.":
            $ kcEngagement += 1 #Logic: Kitcat likes the focus on keeping MAC safe and the more gentle omment
            mS "MAC, don't go poking into BigCorp networks. After all the work to keep you safe." #more gentle way of chiding MAC about being inconspicuous#
    play audio "macGrumble.wav" volume 1.0
    $ setEngagement()
    "MAC's head lowers." ## this reaction can differ based on choices##
    macS "I just wanted to be helpful..."
    "I let out a heavy sigh."
    mS "MAC you are, it's just—What's your suggestion?"
    play audio "macAffirmative.wav" volume 1.2
    macS "An initial search suggests a nearby planet known as Solara, specifically the city of Akar. It may be suitable for our needs."
    $ AddChatter(vig3_sc2_hallway_comment4) 
    macS "However, I should caution you..."
    #Add a black screen function here. 
    stop music fadeout 2.0
    if viewershipHigh == True:
        $ viewCount += 3
    "For a moment, the Oakley falls away from my view."
    show bg black at topleft onlayer background with dissolve
    hide ship_hallway_stream
    hide mac with dissolve
    $ AddChatter(vig3_sc2_hallway_comment5)
    "The low hum of the ship replaced by a crowded bar, the starting lines of song that will bellow out to bustling streets."
    "An old crew of outlaws, drunk off a job well done."
    show ship_hallway_stream at topleft onlayer background with dissolve
    hide bg black
    show mac stream neutral at stream_center_mac
    if viewershipHigh == True:
        $ AddChatter(vig3_sc2_hallway_comment6)
    macS "Now there seems to be a significant amount of criminal activity, the crime rate is actually quite abnormal—"
    "I pat MAC's head, interrupting him."
    play audio "macHum.wav" volume 1.0
    show mac stream happy at stream_center_mac
    mS "Good job buddy, rest up. I'll see you in an hour."
    "With every step, I can't help but feel my smile grow, knowing this will be the calmest hour that I've had in a very long time."
    hide mac with dissolve
    jump vig3_sc3

##START OF ACT 1###
label vig3_sc3():
    show bg black at topleft onlayer background with dissolve
    hide ship_hallway_stream
    hide cockpit_mess_stream
    play backAudio "bgcrowd.wav" volume 0.4 loop fadein 0.5
    show akarstreet_stream at topleft onlayer background with dissolve
    play music "soundtrack/akar(day).wav" volume 0.8 #fadein 2.0
    $ viewCheck2 = viewCount
    "Well off to the side of the road, the familiar streets of Akar are alive in front of us."
    $ AddChatter (vig3_sc3_akarstreet_comment1)
    "It's beaming with colour and life, red and orange banners bridge the spaces between the buildings, a jubilant feeling in the air."
    "Being attached to the Vineyard, Akar's blend of nature and technology are a sight to be sure." ## Rich and vibrant plant life merging with the surrounding infrastructure brightly adorned by lights and striking signage - think eco-futurist Vegas.##
    if viewershipHigh == True:
        $ AddChatter (vig3_sc3_akarstreet_comment2)
        pause 0.5
        $ AddChatter (vig3_sc3_akarstreet_comment3)
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    show mac stream neutral at stream_center_mac with dissolve    
    enS "Quite a lot of fanfare."
    pS "Really cleaned up the place."
    macS "I believe I just saw someone steal candy from a child..."
    $ AddChatter (vig3_sc3_akarstreet_comment4)
    $ reactTarget = "vig3_sc3_maccandy" # time for this is 6:17
    show screen streamerCommentary
    mS "Yeah, stick close, bud, don't go running off around here."
    show jennica stream angry at stream_left
    $ AddChatter (vig3_sc3_akarstreet_comment5)
    pS "Moze, why'd ya bring us here? Fancy gettin' caught by Ama?"
    $ AddChatter (vig3_sc3_akarstreet_comment6)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc3_akarstreet_comment7)
    enS "It's risky, even by your standards."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc3_akarstreet_comment8)
    mS "You both know that this is where we'll get quality upgrades for what we need."
    mS "And I figured it'd be nice to take a break while we're at it."
    if viewershipLow == True:
        $ viewCount += 3
    else:
        pass
    show jennica stream neutral at stream_left
    pS "I think you're too nostalgic."
    enS "And eager to get arrested."
    $ AddChatter (vig3_sc3_akarstreet_comment9)
    mS "Well a BigCorp prison probably has better food than some of the places we've seen."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc3_akarstreet_comment10)
    macS "There doesn't seem to be many enforcers operating here. Curious."
    mS "They tried that once, didn't go so hot."
    macS "There seem to be reports of a large altercation in Akar... Is that..."
    enS "Moze, there could be some off duty grunts here."
    hide screen streamerCommentary
    mS "Resa look, the Inventor's Fair is in town." #Choices here?
    mS "Most of the security will be looking at the Vineyard—not here." 
    mS "Let's see if we can find some old friends, grab what we need, and maybe a drink or two..."
    pS "And a softer bed."
    show teresa stream happy at stream_right
    enS "... A proper hot meal."
    macS "I require none of those things."
    "A small kid walks past with his parents, carrying a giant cotton candy dessert. It looks like a planet being orbited by small chocolate moons." ###The candy could change based on alignment###
    play audio "macPing.wav" volume 1.5
    macS "But I require that."
    $ AddChatter (vig3_sc3_akarstreet_comment11)
    show mac stream neutral reflect at stream_left5mac with move
    "As MAC start to wheel towards the treat, Jennica thankfully picks him up."
    pS "Alright, buddy we'll see what we can do."
    "I almost don't see the guy as he pushes past Teresa, getting a bit too close for comfort..." ##HOUND LEADER (early forties)##
    show houndleader stream neutral at stream_right5 with dissolve
    with hpunch
    show teresa stream upset at stream_right
    show jennica stream angry at stream_left
    enS "Hey! Care to watch yourself?"
    houndleaderunknown "Aw, smile a bit sweetcheeks, it's a celebration!"
    $ AddChatter (vig3_sc3_akarstreet_comment12)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc3_akarstreet_comment13)
        pause 0.5
        $ AddChatter (vig3_sc3_akarstreet_comment14)
    show jennica stream fight at stream_left
    play audio "punch.wav" volume 1.5
    "Before anyone can respond, Jennica punches the man in the face." 
    play audio "grunt.wav" volume 2.5
    show teresa stream neutral
    "He falls down hard and she puts her boot on his throat. Teresa leans over him, grinning." 
    $ AddChatter (vig3_sc3_akarstreet_comment15)
    hide houndleader with vpunch
    "I can feel MAC on my leg as he hides behind me."
    hide mac with dissolve
    $ AddChatter (vig3_sc3_akarstreet_comment16)
    $ reactTarget = "vig3_sc3_firstfight" # timestamp 6:19
    show screen streamerCommentary
    enS "How's this, sweetcheeks?"
    "I can hear footsteps rushing to us. He's not alone."
    menu:
        "I can hear footsteps rushing to us. He's not alone."
        "Pull out your gun.":
            $ engineerApproval += 1 #Logic: Teresa likes the show of force
            $ macViolence += 1
            $ pdEngagement += 1 #Logic: pickledDragons likes the direct intervention
            play audio "gunCock.wav" volume 2.0
            "I pull out my gun in the direction of the sound." 
            mS "Not likely, boys."
            $ AddChatter (vig3_sc3_snakehawk_comment1)
        "Show them you're a Snakehawk.":
            $ pilotApproval += 1 #Logic: Jennica likes the deescalation and that the tatoo still means something here
            $ macPeace += 1
            $ csEngagement += 1 #Logic: kitcat and Coriolis both like the use of "lore" for intervention
            $ kcEngagement += 1
            "I lift my arm and flash the Snakehawks tattoo on my left hand."
            mS "I really wouldn't do that."
            $ AddChatter (vig3_sc3_snakehawk_comment2)
    $ setEngagement()
    "The two men back away and retreat. They're well built but not sharp enough for a fight like this."
    "I give the signal to Jennica as she lets their friend scramble up and run off after them."
    hide screen streamerCommentary
    "The city moves as normal, uninterested in what just happened."
    show teresa stream happy
    enS "It's good to be back."
    hide teresa with Dissolve(0.5)
    hide jennica with Dissolve(0.5)
    hide mac with Dissolve(0.5)
    jump vig3_sc4

label vig3_sc4():  
    "We arrive at the storefront of Specs and Steele, a small ship mechanic shop just off the side of the main road."
    show mac stream neutral at stream_center_mac with dissolve 
    play audio "macNeutral.wav" volume 1.0
    macS "Is this the most suitable store for our needs?"
    mS "Definitely. Run by an old friend. Probably one of the only ones that won't shoot first before taking our credits."
    "MAC pauses for a moment, thinking through something."
    macS "You seem to be worried about a lot of violence. Did you do something, Captain?"
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    pS "Long story, kid."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc3_akarstreet_comment17)
    enS "Several long stories to be precise."
    mS "Don't worry about it too much."
    play audio "macGrumble.wav" volume 1.2
    macS "I fear I have not stopped worrying since we landed."
    "Jennica glares at Teresa."
    pS "He gets it from you."
    stop backAudio fadeout 2.0
    stop music fadeout 2.0
    $ AddChatter (vig3_sc3_akarstreet_comment18)
    hide akarstreet_stream with dissolve
    play audio "door.wav" volume 1.5
    show reccshop_stream at topleft onlayer background with dissolve
    "We walk into Specs and Steele. The inside is... neat?"
    $ AddChatter (vig3_sc3_akarstreet_comment19)
    "Steele's usual brand of chaotic mess has been replaced with with a refined and uncharacteristic organization."
    $ AddChatter (vig3_sc3_akarstreet_comment20)
    "At least now you can walk through it."
    mS "Hey, Steele! You in?"
    $ AddChatter (vig3_sc3_akarstreet_comment21)
    pS "Hope you still have that Vira Brandy!"
    $ AddChatter (vig3_sc4_shop_comment1)
    enS "From four years ago?"
    pS "It ages well!"
    play audio "macPing.wav" volume 1.2
    macS "A delicacy from the Vineyard, Reynar's Vira Brandy, named after his partner, has a shelf-life of 5 years."
    pS "See? Just made it!"
    hide mac with dissolve
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment2)
    "With MAC trailing us I scan some of the newer gear, even some weirder stuff. Weird for Steele."
    stop music fadeout 3.0
    "Someone comes out from the back room."
    show rec stream neutral at stream_center with dissolve
    ###RECCRIN (Late 20s) enters from the back room. They looks like an older version of their brother Allistar, long hair, tougher build.##
    recS "Well I'll be..."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment3)
    "We can't help our silence in this moment."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment4)
    show jennica stream neutral at stream_left
    show teresa stream happy at stream_right
    show rec stream happy
    play music "soundtrack/theme.wav"
    pS "{i}Rec!{/i}"
    "Jennica runs up to hug Rec. They embrace and Jenn lifts them off the ground."
    $ AddChatter (vig3_sc4_shop_comment5)
    pS "It's wonderful to see you, kid."
    $ AddChatter (vig3_sc4_shop_comment10)
    enS "Looking good, Reccrin!"
    recS "Thanks, but I'm not much of a kid anymore."
    $ AddChatter (vig3_sc4_shop_comment6)
    mS "I'll say."
    hide jennica stream neutral with dissolve 
    hide teresa stream happy with dissolve
    "I walk over slower than I should and go for a hug. Pushing the guilt down as I do."
    $ AddChatter (vig3_sc4_shop_comment7)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc4_shop_comment11)
        pause 0.5
        $ AddChatter (vig3_sc4_shop_comment12)
    mS "What happened to Steele?"
    recS "Old man passed two years back, so I took over."
    $ AddChatter (vig3_sc4_shop_comment13)
    pause 0.5
    $ AddChatter (vig3_sc4_shop_comment14)
    mS "I know he was up in years, but to think..."
    $ AddChatter (vig3_sc4_shop_comment15)
    mS "What happened?"
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment8)
    recS "Nothing, just age. The years caught up to him."
    mS "Of all the things I can't believe the years were what got him."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment9)
    show jennica stream neutral at stream_left with dissolve
    show teresa stream happy at stream_right with dissolve
    pS "I was really lookin' forward to sharin' that brandy."
    recS "Well you're in luck."
    pS "Hell yeah!"
    show rec stream happy at stream_right5 with move
    show mac stream neutral reflect at stream_left5mac with dissolve
    play audio "macPing.wav" volume 1.2
    macS "Vira Brandy is the first alcohol product that uses edible chimaeron fruit. Which is quite odd."
    $ AddChatter (vig3_sc4_shop_comment16)
    pS "And delicious!"
    "As Rec turns to get the brandy they pause to look down at MAC."
    show rec stream surprised
    hide jennica stream neutral with dissolve 
    hide teresa stream happy with dissolve
    recS "And who's this little guy?"
    play audio "macAffirmative.wav" volume 1.2
    macS "I'm MAC!"
    show rec stream happy
    recS "I bet you are!"
    "Rec's eyes grow wide, it's the same look Allistar gave him when they first met."
    recS "And where did they pick you up?"
    macS "From a top secret research facility in BigCorp headquarters."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment17)
    show rec stream surprised
    "If I could die right now I would."
    "Reccrin just stares at MAC, blinking rapidly."
    recS "... What?"
    #mS (Multiple Response options about how to lie)
    menu:
        "It's too dangerous to tell Rec everything right now."
        "Just a courier bot we picked up.":
            $ csEngagement += 1 #Logic: The most honest, therefore the one Coriolis likes the most.
            mS "Just a courier bot we found and outfitted."
            mS "Figured we could use an extra hand and a morale boost..."
            "I hear Jennica speak low behind me."
            pS "Just a courier bot..."
            $ AddChatter (vig3_sc4_bot_comment1)
            if viewershipHigh == True:
                $ AddChatter (vig3_sc4_bot_comment2)
        "Top secret? Please.":
            $ kcEngagement += 1 #Logic: An effective lie to keep MAC safe
            mS "If by top secret you mean off a random shelf, then sure, keep it hush hush though."
            "No one responds."
            recS "Good thing you became an outlaw instead of a comedian."
            $ AddChatter (vig3_sc4_secret_comment1)
        "Teresa did you program that?":
            $ pdEngagement += 1 #Logic: A funny choice pickledDragons would like (also kind of demeans MAC which is why kitcat doesn't get a bonus)
            mS "That's the last time I let you touch our gear Teresa."
            show teresa stream shock at stream_right with dissolve
            enS "Excuse me?"
            "I give her a look."
            show teresa stream neutral
            enS "Oh haha yeah... of course Cap."
            $ AddChatter (vig3_sc4_program_comment1)
            pause 0.5
            $ AddChatter (vig3_sc4_program_comment2)
            pause 0.5
            $ AddChatter (vig3_sc4_program_comment3)
            hide teresa
    $ setEngagement()
    #^All of these feel mean....could use a rewrite#
    show rec stream thinking
    "MAC looks unsure if he should respond. Rec looks between the two of us for an answer."
    recS "Mind if I take a closer look?"
    "MAC looks up at me. I guess we're in it now..."
    mS "Up to you, buddy."
    play audio "macHum.wav" volume 1.2
    macS "I do not mind."
    mS "Go for it."
    "Rec carefully examines MAC, seeing the mismatched metal in some of his body parts where Allistar worked."
    $ AddChatter (vig3_sc4_shop_comment18)
    recS "So interesting, the work is a bit rushed but still clean, almost reminds me of how Allistar would do it."
    $ AddChatter (vig3_sc4_shop_comment20)
    "The room goes still, I don't know what to say to them."
    mS "Had to be a rushed job, we've been on the move."
    mS "But look, not to interrupt your analysis, we're here to fix our comms."
    show rec stream neutral
    recS "Sorry, yeah got carried away. What do you need? New parts?"
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    enS "Definitely a range extender."
    pS "Honestly, even the base parts could use an upgrade. If you have some to spare."
    mS "We needa get outfitted and going in the next few days."
    recS "Got it, lemme check the back, I might have something for you."
    hide rec stream neutral with dissolve
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment19) 
    "Rec disappears to the back of the shop. MAC turns to me and I already know he's vibrating with a question."
    show mac stream neutral at stream_center_mac with move
    play audio "macPester.wav" volume 1.5
    macS "Do they know Allistar? They look like Allistar."
    mS "Allistar is their brother."
    enS "I'm guessing we're not telling them that their brother's body is floating in space a few clicks out." 
    $ AddChatter (vig3_sc4_shop_comment21)
    mS "I'm not feeling too inclined."
    macS "But they have a right to know..."
    "I need to think about how to approach this." ###Add multipleoptions###
    menu:
        "Mac thinks Rec has a right to know about their brother."
        "I'm not being fair.":
            #$ pilotApproval += 1 #Logic: Jennica would want to tell Rec and appreciates Moze being honest that it's not fair
            $ macHope += 1
            $ csEngagement += 1 #Logic: Coriolis likes your honesty, pickledDragons wants you to stand by your previous choice.
            $ pdEngagement -= 1
            mS "MAC I'll be honest, I'm not being fair. But we need their help and that's a conversation for after."
            mS "Okay?"
            play audio "macOK.wav" volume 1.2
            macS "Yes, Captain."
            $ AddChatter (vig3_sc4_fair_comment1)
        "We'll tell them after we get the part.":
            #$ engineerApproval += 1 #Logic: Teresa is pragmatic - get the job done, then worry about emotions
            $ macPessimism += 1
            $ kcEngagement += 1 #kitcat likes the desire to be honest, but views waiting to do so as keeping MAC safe
            mS "Range extender first, hard talk later. We can't leave here without it."
            mS "So it'll be hush hush for right now, okay?"
            $ AddChatter (vig3_sc4_after_comment1)
            play audio "macOK.wav" volume 1.2
            macS "Yes, Captain."
        "I have no love for Allistar.":
            $ macViolence += 1
            $ pdEngagement += 1 #Logic: pickledDragons likes sticking by the outlaw choice
            $ csEngagement -= 1
            mS "I'm not about to apologize for what I needed to do. They'll find out eventually."
            mS "Understood?"
            play audio "macOK.wav" volume 1.2
            macS "Yes, Captain."
            $ AddChatter (vig3_sc4_nolove_comment1)
    $ setEngagement()
    "Reccrin comes out after a brief moment with a long antenna and some internal parts for our comms."
    show mac stream neutral reflect  at stream_left5mac with move
    show rec stream happy at stream_right5 with dissolve
    recS "Definitely an older model but she should work better than what you got. Need an install?"
    enS "I could use the hand."
    pS "Thanks, Rec."
    mS "It's very appreciated."
    show rec stream thinking
    recS "No worries! Hey since y'all have been on the move, you wouldn't have happened by Al at all?" 
    $ AddChatter (vig3_sc4_shop_comment22)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc4_shop_comment23)
        pause 0.5
        $ AddChatter (vig3_sc4_shop_comment24)
    recS "I haven't heard from him in a while."
    $ AddChatter (vig3_sc4_shop_comment25)
    "There's too long of a pause as I can't think of something fast enough."
    stop music
    play audio "door.wav" volume 1.5
    "Then the shop door swings open."
    $ AddChatter (vig3_sc4_shop_comment26)
    hide mac with dissolve
    hide jennica with dissolve
    show rec stream surprised at stream_center with move
    show houndleader stream neutral at stream_left with dissolve
    play music "soundtrack/deadeye.wav" volume 0.8 fadein 0.5
    $ AddChatter (vig3_sc4_shop_comment27)
    "A group of five enter the shop, dark uniforms with a dog patched on their right shoulder." 
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment28)
    "These guys, they're the ones from before." ##The Hound Leader##
    $ reactTarget = "vig3_sc4_houndraid"#timestamp is 6:23
    show screen streamerCommentary
    houndleader "Alright Reccrin, you know the drill! Mandatory sweep!"
    houndleader "Don't cause any—"
    houndleader "Oh!"
    enS "You must be joking."
    $ AddChatter (vig3_sc4_shop_comment30)
    houndleader "Sweetcheeks."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment29)
    enS "Bite me."
    $ AddChatter (vig3_sc4_shop_comment31)
    houndleader "Maybe later, I'm on the clock now."
    hide teresa with dissolve
    mS "Didn't know Akar hired rent-a-cops."
    show houndgoon stream neutral at stream_right with dissolve
    "A smaller goon moves up next to him." 
    $ AddChatter (vig3_sc4_shop_comment32)
    "She's tough and with something to prove."
    houndgoon "I suggest you get yourself and your crew in order and stay out of the way."
    hide screen streamerCommentary
    "Rec looks at me with a forced smile."
    show rec stream neutral
    recS "Please, Moze..."
    $ AddChatter (vig3_sc4_shop_comment33)
    recS "Hounds! We don't want any trouble."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment34)
    recS "Just do what you need to do."
    $ AddChatter (vig3_sc4_shop_comment35)
    houndleader "That's what I like about you, Rec, so reasonable."
    "We stand back as the group rummages through the store, knocking over shelves and taking random items." 
    "They're armed to the teeth. Now I understand why Rec is so quick to comply."
    ###Describe the wreck this group is leaving and give the players two opportunities to intervene or continue to comply silently.###
    "Like restless children, they stick their hands in every possible shelf and knock over part after part."
    "It's a big show. They snicker to each other, incoherently mumble protocols and giggle."
    menu:
        "Reccrin is looking down at their desk."
        "That's enough!":
            mS "Alright, that's enough!"
            $ AddChatter (vig3_sc4_enough_comment1)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter (vig3_sc4_enough_comment2)
            $ pdEngagement += 1 #Logic: pickledDragons likes the assertion of power from an outlaw perspective
            $ csEngagement += 1 #Logic: Coriolis likes the intervention to help Allistar
        "Let them continue.":
            $ kcEngagement += 1 #Logic: kitcat likes that keeping quiet keeps MAC safer
            "They're relentless." #we only trigger these changes for this instance since they'll happen later no matter what
            "Doesn't matter the material or how fragile or how important, they don't stop."
            "I cringe as each piece falls. Broken parts start to litter the floor."
            $ AddChatter (vig3_sc4_continue_comment1)
            menu:
                "Do I intervene?"
                "That's enough!":
                    mS "Alright that's enough!"
                    $ AddChatter (vig3_sc4_enough_comment1)
                    if viewershipHigh == True:
                        pause 0.5
                        $ AddChatter (vig3_sc4_enough_comment2)
                "Stay quiet.":
                    "They continue to trash the shop. More carnage. They're laughing to each other, tossing equipment like a hackey sack."
                    $ AddChatter (vig3_sc4_continue_comment2)
                    "I see one of them try to head to the back room."
                    mS "Alright that's enough!"
    $ setEngagement()
    houndgoon "You'd best to stay out of official business."
    "Another uniform chimes in."
    houndgoon "We're under orders to collect contraband."
    mS "Contraband? That's rich."
    mS "Learned that from the little pamphlet they gave you?"
    houndgoon "Tryna be smart are we?"
    mS "Someone has to."
    houndgoon "Contraband is whatever we say it is."
    houndleader "We'll also be taking this."
    "The leader goes to pick up the antenna for the comms that's sitting on Rec's store counter." 
    $ AddChatter (vig3_sc4_shop_comment36)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc4_shop_comment37)
    pause 0.5 
    $ AddChatter (vig3_sc4_shop_comment38)
    ###Streamer reaction: Of course he does### #streamer react timestamps is 6:25 here
    recS "This item is being sold to customers at the moment. I can assure you it's perfectly legitimate."
    houndleader "Are you admitting to selling contraband, Reccrin?" 
    houndleader "That's cause for reprimand."
    mS "That so called \"contraband\" is mine. And they said it's perfectly legit."
    "I slowly walk up to the counter, moving to take the parts."
    mS "So I'd like it back now."
    hide rec with dissolve 
    "The uniforms turn to us and I know they're gearing up for a fight. They probably won't kill us, but I can't imagine how banged up we'll be or what happens if they find MAC." ###The player must decide between three actions, fight, let them have it, or Bribe - IF THEY HAVEN'T BRIBED REGI###.
    menu:
        "How do I deal with this?"
        "Fight them.":
            $ macViolence += 2
            $ pdEngagement += 2 #Logic: pickledDragons wants you to fight
            $ kcEngagement -= 1 #Logic: kitcat doesn't like putting the crew at risk
            $ csEngagement += 1 #Logic: Coriolis wants to stand up for Rec
            "I get into his face— let him pry my gear from my cold, dead hands." 
            $ AddChatter (vig3_sc4_fight_comment1)
            "He smiles and throws the first punch before I can react."
            play audio "punch.wav" volume 1.3
            with hpunch 
            "It knocks the wind out of me, and I hit the ground."
            play audio "repeatedPunches.wav" volume 1.5
            "Then impact after impact to my stomach before I can catch my breath. He gets low, right to my ear."
            houndleader "You should've died with the rest of the Snakehawks."
            $ AddChatter (vig3_sc4_fight_comment2)
            pause 0.5
            $ AddChatter (vig3_sc4_fight_comment3)
            "He takes the antenna as I struggle to get up from the floor."
            houndleader "Pleasure doing business with you."
            "The gang leaves us to pick ourselves up and walk out of the shop. MAC who has thankfully been hiding rolls forward."
            stop music fadeout 4.0
            play audio "door.wav" volume 1.0
            hide houndgoon with dissolve
            hide houndleader with dissolve
            show rec stream neutral at stream_right5 with dissolve
            show mac stream neutral reflect at stream_left5mac with dissolve
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            macS "Captain are you hurt?" 
            mS "Just my pride."
            "Teresa goes to pull me up."
            enS "I want to burn that man from the inside."
            $ AddChatter (vig3_sc4_shop_comment39)
            pS "Maybe we can use him as our antenna instead."
            $ AddChatter (vig3_sc4_shop_comment40)
            mS "Now that's a thought. Rec, you know those guys?"
        "Let them take the antenna.":
            $ macPeace += 1
            $ macPessimism += 1
            $ kcEngagement += 1 #Logic: kitcat prioritizes the safety of MAC.
            $ pdEngagement -= 1 #Logic: pickledDragons and Coriolis both dislike the inaction
            $ csEngagement -= 1
            "I take a step back, we can't afford a fight right now, it's too risky."
            $ AddChatter (vig3_sc4_passive_comment1)
            houndleader "Pleasure doing business with you."
            "The gang turns to leave knocking some stuff around."
            play audio "punch.wav" volume 1.3
            with hpunch
            "On the way out with the parts, the Leader hits me with a good punch while I'm off guard."
            stop music fadeout 4.0
            hide houndgoon with dissolve
            hide houndleader with dissolve
            show rec stream neutral at stream_right5 with dissolve
            show mac stream neutral reflect at stream_left5mac with dissolve
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            macS "Captain are you hurt?" 
            mS "Just my pride."
            "Teresa goes to pull me up."
            mS "Sorry I didn't want to put you all in more danger."
            enS "You're good Captain."
            enS "Makers I'd like to burn that man up from the inside."
            $ AddChatter (vig3_sc4_shop_comment39)
            pS "Maybe we can use him as our antenna instead."
            $ AddChatter (vig3_sc4_shop_comment40)
            mS "Now that's a thought. Rec, you know those guys?"
        "Try and bribe them." if reginaldChoice == False: #This option shoudl still be here but different outcomes based on the variable.
            $ macPeace += 1
            $ macHope += 1
            $ csEngagement += 2 #Logic: Coriolis likes the attempt to solve problem nonviolently
            $ pdEngagement -= 1 #Logic: pickledDragons does not
            $ kcEngagement += 1 #Logic: kitcat also likes solving problem nonviolently
            "I take out my communicator."
            mS "Listen this doesn't need to be ugly, we'll pay the tarriff and get out of your hair."
            $ AddChatter (vig3_sc4_bribe_comment1)
            houndleader "Finally, a sensible idea." #it doesnt work right? they need to take the antenna to force the crew to keep looking
            "We do the transfer."
            $ AddChatter (vig3_sc4_bribe_comment2)
            play audio "punch.wav" volume 1.3
            with hpunch
            "And I'm hit with a punch without warning."
            $ AddChatter (vig3_sc4_bribe_comment3)
            "He grabs the part and the gang moves out."
            houndleader "Pleasure doing business with you."
            "The gang commits some extra carnage on the way out."
            stop music fadeout 4.0
            hide houndgoon with dissolve
            hide houndleader with dissolve
            show rec stream neutral at stream_right5 with dissolve
            show mac stream neutral reflect at stream_left5mac with dissolve
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            macS "Captain, are you hurt?" 
            mS "Just my pride, and my wallet."
            "Teresa goes to pull me up."
            enS "I want to burn that man up from the inside."
            $ AddChatter (vig3_sc4_shop_comment39)
            pS "Maybe we can use him as our antennae instead."
            $ AddChatter (vig3_sc4_shop_comment40)
            mS "Now that's a thought. Rec, you know those guys?"
    $ setEngagement()
    "They pull out five glasses. And drops the bottle of brandy on the counter."
    "As they start to pour, they stop themselves at the fifth and grab an oil can and pour it in, giving it to MAC."
    play audio "macHum.wav" volume 1.0
    show mac stream happy 
    $ AddChatter (vig3_sc4_shop_comment41)
    macS "Thank you!"
    show mac stream neutral reflect at stream_left with move
    recS "They're the Hounds. Reynar's new security detail."
    recS "Usually they're more of a nuisance than anything. Shaking down shops and the like."
    recS "But with the Inventor's Fair they've gotten more excitable. Not surprised they'd come by here, just terrible timing is all."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment42)
        pause 0.5
        $ AddChatter (vig3_sc4_shop_comment43)
    pS "Sorry, what's the Inventor's Fair? I forgot to ask."
    enS "Big conference. Lots of tech companies, scholars, and start-ups from all over. Schmoozing and rubbing shoulders, the like."
    $ AddChatter (vig3_sc4_shop_comment44)
    pS "Sounds like a party."
    enS "One of the biggest."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment45)
    mS "We're steering clear."
    mS "Rec anyone else you know who can get us the part we need?"
    recS "Not off the top of my head, but I can show you around and we can probably find something."
    mS "Sounds like a plan."
    $ AddChatter (vig3_sc4_shop_comment46)
    play audio "cheers.wav" volume 1.5
    "Reccrin holds their glass up and swallows their drink in one gulp. We follow suit."
    amaS "Ah, that's the stuff."
    $ AddChatter (vig3_sc4_shop_comment47)
    pause 0.5
    $ AddChatter (vig3_sc4_shop_comment48)
    pause 0.5
    $ AddChatter (vig3_sc4_shop_comment49)
    hide mac with dissolve
    hide jennica with dissolve
    hide teresa with dissolve
    hide rec with dissolve
    "I stop the glass at my lips and nearly drop it. Whipping my head around, I almost grab for my gun until I catch Jennica's eyes."
    $ AddChatter (vig3_sc4_shop_comment50)
    show jennica stream neutral at stream_left with dissolve
    pS "All right, Cap?"
    $ AddChatter (vig3_sc4_shop_comment51)
    "I compose myself and try to calm down."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc4_shop_comment52)
    mS "Yeah, sorry."
    $ AddChatter (vig3_sc4_shop_comment53)
    "When I swallow my drink, it goes down hard."
    hide jennica with dissolve
    hide reccshop_stream with dissolve
    play backAudio "bgCrowd.wav" volume 0.3 fadein 1.0
    jump vig3_sc5

label vig3_sc5():
    $ viewCheck3 = viewCount
    #comment out the bottom three lines, they're just here for testing the style guide
    #scene streamview with dissolve
    #show screen streamDetails
    #show screen streamChat
    ######
    show akarplaza_stream at topleft onlayer background with dissolve
    play music "soundtrack/akar(night).wav" volume 0.8 #fadein 1.0
    "When Rec leads us to the plaza, I'm almost starstruck with how it looks." ###REC takes the Oakley Crew to the Plaza. In front is Rec and MOZE with JENNICA and TERESA taking up the rear with MAC in between them.##
    "The space is abundant with life."
    "The shops and bars on the outer ring of the roundabout shine, bursting with patrons." 
    "Music and reverie pour out like sections of a cacophonous orchestra."
    "At the center is a park area with a large statue of a man sitting with an apple in his hand." 
    "It has a massive hole blown out of it."
    show rec stream happy at stream_right5 with dissolve
    recS "Alright, Oakley, it's been a while, but welcome to the Plaza!"
    show mac stream neutral reflect at stream_left5mac with dissolve
    macS "Wow..."
    show jennica stream neutral at stream_left with dissolve
    pS "Surprised it's still standing."
    show teresa stream happy at stream_right with dissolve
    enS "Did they change the statue?"
    recS "Oh yeah they did, because {i}someone{/i} blew up the last one."
    $ AddChatter (vig3_sc5_akarplaza_comment1)
    enS "Fabulous."
    macS "Someone?"
    recS "Why don't you ask your friends, kid."
    mS "It was a long time ago."
    pS "Mighty legendary."
    hide rec with dissolve
    hide jennica with dissolve
    hide teresa with dissolve
    hide mac with dissolve
    show akarplaza_flashback_stream at topleft onlayer background with dissolve
    "I'm taken back to the plaza several years back, rowdy and riotous."
    play audio "lazerFlashback.wav" volume 5.0
    "{b}BANG BANG!{/b}" #sound effect style tests
    "BigCorp officers are scattered around attempting to suppress the riot."
    "With small fires everywhere Teresa holds onto the arm of a statue of a man in a lab coat, Jennica and I look on, blasters in hand."
    enS "We're gonna be *{b}HICK{/b}* glorkin *{b}HICK{/b}* {i}legends{/i} hahaha!"
    if viewershipHigh == True:
        $ AddChatter (vig3_sc5_akarplaza_comment2)
    pS "Pffffft! Glorkin?"
    mS "Resa, hey hey Resa, ya gotta, gotta down from there."
    enS "Not until you say it."
    pS "She's really set, huh?"
    mS "A wild one, that's for sure."
    pS "Please do the honours, Captain."
    $ AddChatter (vig3_sc5_akarplaza_comment3)
    play audio "lazerFlashback.wav" volume 3.0
    "An enforcer in the distance fires a shot at the statue and misses."
    "Jennica returns fire and takes him down."
    mS "Okay okay, you're in!"
    enS "No, no, do the call, it's not real without it."
    mS "The call isn't real, get down from there."
    enS "{i}I know it's real!{/i}"
    play audio "lazerFlashback.wav" volume 3.0
    "Another bullet narrowly misses Teresa."
    play audio "lazerFlashback.wav" volume 5.0
    "She pulls out her blaster and hits her mark."
    pS "Better do the call, Cap."
    enS "{i}See! There is one!{/i}"
    "These two together are gonna be a problem."
    "I take a deep breath."
    mS "{b}CAW CAW HISS HISS!{/b}"
    $ AddChatter (vig3_sc5_akarplaza_comment4)
    "We all laugh."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc5_akarplaza_comment5)
        pause 0.5
        $ AddChatter (vig3_sc5_akarplaza_comment6)
        pause 0.5
    $ AddChatter (vig3_sc5_akarplaza_comment7)
    enS "{i}Legends! Long live the Oakley!{/i}"
    if viewershipHigh == True:
        $ AddChatter (vig3_sc5_akarplaza_comment8)
        pause 0.5
    $ AddChatter (vig3_sc5_akarplaza_comment9)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc5_akarplaza_comment10)
        pause 0.5
        $ AddChatter (vig3_sc5_akarplaza_comment11)
    "Teresa sticks something to the statue and leaps off."
    enS "Hehe catch me!"
    "I'm barely able to catch her in time."
    mS "I got ya!"
    play audio "explosionFlashback.wav" volume 2.0
    #"{b}BOOM!{/b}" #sound effect style test
    "I carry Teresa in my arms, Jennica trailing quickly behind just as the bomb detonates and blows the statue sky high."
    hide akarplaza_flashback_stream with dissolve
    show teresa stream happy at stream_right with dissolve
    enS "Some of my finest work for sure."
    mS "I'd bet money this place hasn't seen a bigger stunt than that."
    amaS "You bet?"
    "I jump and turn to the direction of the voice, this time I make it to my gun."
    play audio "gunCock.wav" volume 2.0
    if viewershipHigh == True:
        $ AddChatter (vig3_sc5_akarplaza_comment12)
    "When I come to, I realize I've scared the young showgirl behind me near to death."
    hide teresa with dissolve
    show daisy stream shock at stream_center with dissolve
    mS "What?"
    $ reactTarget = "vig3_sc5_amahallu" #timestamp is 6:28
    show screen streamerCommentary
    "She stares wide eyed and is taken her off script."
    showgirl "Uh um, name's Daisy, do you bet?"
    mS "Do I bet if your name is Daisy?"
    show daisy stream think
    showgirl "Well if you did you'd be a winner..."
    "She pauses, recalling the words back to her."
    show daisy stream neutral
    showgirl "And you can win bigger at {i}Nova Casino{/i}!"
    showgirl "First 50 Credits are on us!"
    "She attempts to hand me a casino card, it's holographic with an animation of a supernova and 50 credits in big lettering."
    mS "Thanks, but no thanks."
    showgirl "Well..."
    showgirl "Have a nice day!"
    hide streamerCommentary
    "Daisy hurriedly leaves and heads to another group to perform the same spiel. I see her carefully get their attention this time."
    hide daisy with dissolve
    show teresa stream shock at stream_right with dissolve
    show jennica stream shock at stream_left with dissolve
    show mac stream shock reflect at stream_left5mac with dissolve
    show rec stream surprised at stream_right5 with dissolve
    pS "Alright alright, what's this about?"
    $ AddChatter (vig3_sc5_akarplaza_comment13)
    enS "You've been jumpy all day, Captain."
    mS "I'm fine."
    recS "You just yelled at a girl wearing feathers. I beg to differ."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc5_akarplaza_comment14)
    play audio "macAlarmed.wav" volume 1.2
    macS "We are concerned."
    mS "I'm tired is all."
    show teresa stream neutral
    show jennica stream neutral
    show rec stream neutral
    show mac stream neutral reflect
    recS "You know, most of the shops are closing for the day. Let's set you up somewhere for the night."
    $ AddChatter (vig3_sc5_akarplaza_comment18)
    recS "I think the Burnt Bulb has a deal on pints."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc5_akarplaza_comment19)
        pause 0.5
    $ AddChatter (vig3_sc5_akarplaza_comment20)
    "We begin to move out. Jennica begins a story involving a lamp, three chickens, and a guitar. MAC is confused, but enthralled."
    $ AddChatter (vig3_sc5_akarplaza_comment21)
    pause 0.5
    $ AddChatter (vig3_sc5_akarplaza_comment22)
    hide jennica with dissolve
    hide teresa with dissolve
    hide rec with dissolve
    hide mac with dissolve
    "I can't help but look back at Daisy with the small rough-looking crew."
    $ AddChatter (vig3_sc5_akarplaza_comment15)
    "Her eyes fixated on the only person whose back is turned to me."
    $ AddChatter (vig3_sc5_akarplaza_comment16)
    "They're tall and well built with a wide brimmed hat, in dark leather, and long familiar black hair."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc5_akarplaza_comment17)
    show mac stream happy reflect at stream_left_mac with dissolve
    play audio "macPester.wav" volume 1.5
    macS "Are you coming, Captain?"
    "I stare at the crew as they walk away."
    mS "Sure thing, kid."
    stop backAudio fadeout 2.0
    hide mac with dissolve
    jump vig3_sc6

label vig3_sc6():
    hide akarplaza_stream with dissolve
    "The days are shorter this time of year and when night falls we make it to the Burnt Bulb."
    "It took some time to get through Akar. MAC wanted to see everything he could."
    "As if it would disappear if he took his eyes off it."
    show bbpub_stream at topleft onlayer background with dissolve
    play backAudio "bgCrowd.wav" volume 0.4 fadein 1.0
    "The Burnt Bulb Pub feels like it's been stuck in time." 
    "Its wooden paneling, the carnivorous plants that line its ceilings."
    "There's a warmth to this place, I feel like that young outlaw scared out of my mind, clinging to Ama and hoping I won't get bulldozed at my first brawl."
    show rec stream happy at stream_right5 with dissolve
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    show mac stream neutral reflect at stream_left5mac with dissolve
    macS "Cozy."
    play audio "scream.wav" volume 1.0
    "In the back, someone yells and is then quickly tossed through a window."
    "MAC's expression sinks as he clings to my leg."
    show mac stream shock reflect at stream_left5mac
    play audio "macNeutral.wav" volume 1.2
    macS "Aren't there children around outside?"
    pS "That's why he was tossed out the back window."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment1)
        pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment2)
    enS "This is a respectable place after all."
    show mac stream neutral reflect
    recS "Only the best for the Oakley."
    $ AddChatter (vig3_sc6_bbpub_comment4)
    pause 0.5 
    $ AddChatter (vig3_sc6_bbpub_comment5)
    recS "Hopefully they're not booked up 'cause of the Fair."
    enS "Let's find out."
    hide rec with dissolve
    hide teresa with dissolve
    show mac stream neutral at stream_right_mac with move
    show jennica stream neutral at stream_center with move
    "As we walk through the bar, I notice how many regulars have been lost to time. Akar is different now."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment3)
    menu:
        "How do you feel about how Akar has changed?"
        "Being invisible is what we need.":
            $ csEngagement += 1 #Logic: Coriolis and kitcat both agree with this
            $ kcEngagement += 1
            $ pdEngagement -= 1 #pickledDragons finds this kinda boring
            "There's a small comfort in not being immediately recognized."
            "It's better for MAC."
            $ AddChatter (vig3_sc6_invisible_comment1)
            pS "Y'alright, Cap?"
            mS "Yeah, let's just get through and find a spot."
            "The new crews are quite the sight."
            "Their gear is impressive."
            "A little intimidating..."
            "We hug a wall and find any available table."
            macS "Woah..."
            "I move MAC away from staring too long at a particularily burly outlaw and smile nicely."
            "When we find the table, I gently push off a passed-out patron."
            "Teresa and Rec come back to us with our first round." 
            "I buy us the next one."
        "Surely not everyone forgot us.":
            $ csEngagement += 1 #Logic: Coriolis and kitcat like the reference to backstory
            $ kcEngagement += 1 #Logic: pickledDragons doesn't really care
            "I'm sure some people remember who we are."
            $ AddChatter (vig3_sc6_surely_comment1)
            mS "See anyone familiar?"
            "Jenn takes a moment to survey the space."
            pS "Think we might've missed the reunion."
            mS "Ha, looks like it."
            $ AddChatter (vig3_sc6_surely_comment2)
            "We move through the bar, and I scan for any familiar faces."
            "Or any face that seems friendly."
            "Apart from a waitress who waves at us out of courtesy, no one."
            "When we find our table, I gently push off a passed-out patron lying on it."
            "Teresa and Rec come back to us with our first round." 
            "I buy us the next one."
        "Let's make sure they don't forget us.":
            $ pdEngagement += 1 #Logic: pickledDragons like this attitude
            $ kcEngagement -= 1 #Logic: kitcat and Coriolis view it as irresponsible
            $ csEngagement -= 1
            "I don't care how long its been, the Oakley is still legendary."
            "Maybe we should remind them who we are..."
            "We barrel through the crowd to find a table."
            with vpunch
            mS "Make way for the Oakley, everyone!"
            mS "C'mon let's move, let's move!"
            pS "Oh we're doin' this?"
            $ AddChatter (vig3_sc6_make_comment1)
            "I give Jenn a wink and she smiles."
            pS "You heard the Captain, move it or lose it!"
            "I bump into a particularily scary guy who decides to take a swing at me for my indiscretion."
            "I make sure he meets the floor quickly."
            $ AddChatter (vig3_sc6_make_comment2) 
            mS "Pardon us."
            "I step over his curled up body."
            "When we find our table, I gently push off a passed-out patron lying on it."
            "Teresa and Rec come back to us with our first round." 
            "I buy us the next one."
    $ setEngagement()
    "And then another."
    "And another."
    show jennica stream neutral at stream_left with move
    show mac stream neutral reflect at stream_left5mac with move
    show rec stream drunk at stream_right5 with dissolve
    recS "So I said, \"You should've been more specific about the screw!\""
    $ AddChatter (vig3_sc6_bbpub_comment6)
    show teresa stream happy at stream_right with dissolve
    show jennica stream neutral at stream_left with dissolve 
    "Raucous laughter pours out of us, barely audible in this crowded bar."
    enS "Makers, that's dumb."
    macS "Now I found that funny but can someone clarify the part about the screw?"
    enS "Well you see \"screw—\""
    show jennica stream shock at stream_left
    "Jennica covers what she thinks are MAC's ears."
    pS "Too young, too impressionable."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment7)
    show teresa stream neutral at stream_right
    enS "He's a courier bot, it's fine."
    show jennica stream angry at stream_left
    play audio "macGrumble.wav" volume 1.2
    macS "That's not where my ears are."
    pS "C'mon, a bot? Get out!"
    $ AddChatter (vig3_sc6_bbpub_comment8)
    macS "That is not an incorrect statement."
    show teresa stream upset at stream_right
    enS "Why must you be so emotional about everything?"
    pS "And why ya gotta be a cold hearted b—"
    show mac stream shock at stream_center_mac with move 
    show rec stream surprised
    $ reactTarget = "vig3_sc6_crewspat"#timestamp 6:30
    show screen streamerCommentary
    recS "{i}Woah!{/i} How about I go and get us another round."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment9)
    show rec stream happy
    recS "C'mon buddy, I'll get you a treat."
    hide rec with dissolve
    hide mac with dissolve
    "MAC looks at me expectantly."
    mS "In eyesight, got it?"
    "MAC lets out an excited noise and heads to the bar with Rec."
    "The table is silent."
    mS "I owe you both an apology."
    $ AddChatter (vig3_sc6_bbpub_comment10)
    "Jennica and Teresa perk their heads towards me."
    $ AddChatter (vig3_sc6_bbpub_comment11)
    hide screen streamerCommentary
    show teresa stream neutral at stream_right
    show jennica stream neutral at stream_left
    mS "I'm not going to say that I regret what we did in Gibian V, that doesn't matter now."
    mS "But I can't have the two of you blowing up at each other over something I decided."
    $ AddChatter (vig3_sc6_bbpub_comment12)
    mS "When it comes down to it, we need to look out for each other." 
    mS "You're the ones I can rely on, the only ones I trust and I need that to be the same between all of us."
    show jennica stream neutral at stream_left
    show teresa stream happy at stream_right
    "When the two of them begin to smile at each other, I know that something I said stuck."
    $ engineerApproval += 1
    $ pilotApproval += 1
    enS "You know, I was wondering when we'd get an inspiring heart to heart from you."
    pS "I'm thinkin' that cracks the top five."
    enS "Not as good as the one on Firma 12. How did that one go?" 
    enS "\"We're family, a crazy, wild, dysfunctional family—\""
    pS "\"But that's what makes us special!\" I'm tearing up thinking 'bout it."
    mS "Okay, okay, that's enough."
    "Jennica raises her glass."
    pS "We got your back, Moze."
    "Teresa raises her glass."
    enS "Always."    
    $ AddChatter (vig3_sc6_bbpub_comment13)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment14)
    "I raise mine in response."
    play audio "cheers.wav" volume 2.0
    mS "Long live the Oakley!"
    # maybe fade in and out, show the passage of time
    hide teresa with dissolve
    hide jennica with dissolve
    "As the night continues on, the Burnt Bulb becomes more and more packed, the empty glasses on our table sit in tall stacks threatening to fall before a barkeep cleans them."
    "Teresa is in a corner watching in unwavering curiosity at the plants that line the ceiling, tossing bits of food up for them to catch."
    "Jennica is at a pool table, chatting away with some couple who are very clearly flirting with her."
    "Rec is telling MAC a story that has him fully engaged. But he keeps looking around the room nervously."

    #This would normally be a menu with multiple choices but for simplicity and time we'll only have MAC and Rec and the stranger

    "I should check in on MAC, see how he's holding up." 
    "Just as I get up I notice that wide brimmed hat again, long dark hair, she walks right past me and out the door."
    $ AddChatter (vig3_sc6_bbpub_comment15)
    pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment16)
    pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment17)
    "There's a chill that runs down my spine."
    ###Recount choice again###
    $ viewCheck4 = viewCount
    menu:
        "Do I investigate this stranger?"
        "Follow the stranger.":
            $ kcEngagement += 1 #Logic: pd and kc are both intrigued and want to investigate
            $ pdEngagement += 1
            $ csEngagement -= 1 #Logic: cs doesn't like leaving the crew alone
            $ reactTarget = "vig3_sc6_stranger"#timestamp 6:31
            $ setEngagement()
            show screen streamerCommentary
            "I follow the stranger out of the bar and every fiber in my being is yelling at me that this is a bad idea."
            play audio "door.wav" volume 1.5
            hide bbpub_stream with dissolve
            show akarplazanight_stream at topleft onlayer background with dissolve 
            $ AddChatter (vig3_sc6_stranger_comment1)
            "I struggle to navigate the dark winding streets of Akar." 
            $ AddChatter (vig3_sc6_stranger_comment2)
            "The chaos is picking up as the night continues." 
            $ AddChatter (vig3_sc6_stranger_comment3)
            "I almost lose the stranger as they tuck away behind an alley and I move to close in on them."
            hide screen streamerCommentary
            "As I turn the corner, I'm met with a knife to my throat."
            "So clearly not Ama's style."
            $ AddChatter (vig3_sc6_stranger_comment4)
            show stranger stream neutral at stream_center with dissolve
            "The stranger's eyes are bright and blue. They're face pretty and heart-shaped face with a mole under her right eye."
            strngr1 "Why are you following me?"
            $ AddChatter (vig3_sc6_stranger_comment5)
            pause 0.5
            $ AddChatter (vig3_sc6_stranger_comment6)
            mS "I just—"
            "She presses the knife into my neck."
            strngr1 "You what? Thought I was some easy mark?"
            "She's young in her voice and in her confidence."
            mS "No, I just thought you were someone else."
            "She doesn't let go of the knife."
            strngr1 "Well sorry to disappoint. But I don't take kindly to being followed."
            "I should say something to get out of this." #Options: Hands up and walk away, flirt, wrestle the knife away.
            menu:
                "How do I get out of this?"
                "Flirt.":
                    $ kcEngagement += 1 #Logic: Crowd pleaser moment. Everyone likes a good flirt and romance, right?
                    $ pdEngagement += 1
                    $ csEngagement += 1 #Logic: I could see Coriolis losing engagement here, viewing it as being irresponsible
                    $ setEngagement()
                    mS "Oh, I'm far from disappointed." #flirt
                    "A small smile rises on her face."
                    show stranger stream smile
                    $ AddChatter (vig3_sc6_flirt_comment1)
                    strngr1 "Oh yeah?"
                    $ AddChatter (vig3_sc6_flirt_comment2)
                    mS "You're a much more pleasant sight if I say so myself."
                    "She doesn't let go of the knife, but moves in closer."
                    $ AddChatter (vig3_sc6_flirt_comment3)
                    strngr1 "You're not an eyesore yourself."
                    mS "Ouch, I'm hurt."
                    strngr1 "Not yet, but the night's young."
                    $ AddChatter (vig3_sc6_flirt_comment4)
                    "When the knife falls we close the distance and tuck ourselves deeper in the alley, far away from eyesight."
                    hide stranger with dissolve 
                    "I return to the Burnt Bulb a bit disheveled, hoping that the small nick on my neck has started to scar over."
                    "I go to see Mac and Rec."
                    hide akarplazanight_stream
                    show bbpub_stream at topleft onlayer background with dissolve
                "Hands up, walk away.":
                    $ kcEngagement -= 1 #Logic: pd and kc both dislike going here and doing nothing
                    $ pdEngagement -= 1
                    $ csEngagement += 1 #Logic: coriolis likes that you're "the bigger person"
                    $ setEngagement()
                    mS "Look, this got out of hand."
                    "I hold my hands up and start at her trying to relax the situation."
                    strngr1 "Ha, what can't follow through?"
                    $ AddChatter (vig3_sc6_walkaway_comment1)
                    mS "Nothing to follow through on."
                    $ AddChatter (vig3_sc6_walkaway_comment3)
                    hide stranger with dissolve 
                    strngr1 "Pathetic."
                    $ AddChatter (vig3_sc6_walkaway_comment2)
                    "Her knife doesn't move, but she nods her head to tell me to get lost."
                    "I don't take my eyes off her when I back away"
                    "I return to the Burnt Bulb disappointed."
                    "I go to see Mac and Rec."
                    hide akarplazanight_stream
                    show bbpub_stream at topleft onlayer background with dissolve
                "Wrestle the knife away.":
                    $ pdEngagement += 1 #Logic: pickledDragons likes Moze asserting herself; kitcat doesn't have strong feelings about this interaction
                    $ csEngagement -= 1 #Logic: Coriolis dislikes the use of force
                    $ setEngagement()
                    mS "I don't have time for this."
                    show stranger stream stabbed
                    "I grab her wrist before she can cut me open and twist her arm down and away."
                    $ AddChatter (vig3_sc6_knife_comment1)
                    menu:
                        "Make it hurt?"
                        "Yes. Just like Ama taught me.": 
                            #sounds of bones cracking would be cool here
                            $ csEngagement -= 2 #Logic: Coriolis REALLY doesn't like that.
                            $ kcEngagement -= 1 #Logic: It's going too far for kitcat
                            $ pdEngagement += 1
                            $ setEngagement()
                            $ outlaw += 1
                            "She yells as something snaps."
                            $ AddChatter (vig3_sc6_knifeyes_comment1)
                            pause 0.5
                            $ AddChatter (vig3_sc6_knifeyes_comment2)
                            strngr1 "Po-dunk!"
                            $ AddChatter (vig3_sc6_knifeyes_comment3)
                            pause 0.5
                            $ AddChatter (vig3_sc6_knifeyes_comment4)
                            "Sweat is pouring down her face."
                            $ AddChatter (vig3_sc6_knifeyes_comment5)
                            "I slam a knee to her chest."
                            $ AddChatter (vig3_sc6_knifeyes_comment6)
                        "No. I've made my point.":
                            #Logic: No changes, the alterations from the previous branch of the tree remain in effect.
                            $ AddChatter (vig3_sc6_knifeno_comment1)
                            "I shove her against the wall and she falls over."
                            $ AddChatter (vig3_sc6_knifeno_comment2)
                            "The knife clatters away."
                            $ AddChatter (vig3_sc6_knifeno_comment3)
                            pause 0.5
                            $ AddChatter (vig3_sc6_knifeno_comment4)
                    "It's over before it even starts."
                    mS "Need me to call someone for you?"
                    strngr1 "Go to hell."
                    mS "Trust me they know I'm coming."
                    $ AddChatter (vig3_sc6_knifeno_comment5)
                    hide stranger with dissolve 
                    "On my way back to the Burnt Bulb, I can feel eyes on me."
                    "I take careful steps."
                    "When I get to my destination, I wipe a bit of dust off my jacket before heading in."
                    "I go to see MAC and Rec."
                    play audio "door.wav" volume 1.5
                    show bbpub_stream at topleft onlayer background with dissolve
                    hide akarplazanight_stream

        "Check in on MAC and Rec.":
            $ csEngagement += 1 #Logic: cs likes that you're finding out more about Rec, kc likes that you're sticking with MAC
            $ kcEngagement += 1
            $ pdEngagement -= 1 #Logic: pd is just a little disappointed
            $ setEngagement()
            "I can't follow paranoid hunches, I gotta stick to my crew."
            $ AddChatter (vig3_sc6_recmac_comment1)
            pause 0.5
            $ AddChatter (vig3_sc6_recmac_comment2)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter (vig3_sc6_recmac_comment3)
                pause 0.5
                $ AddChatter (vig3_sc6_recmac_comment4)
            "Rec and MAC are chatting at the bar, I get the tail end of their conversation."
            show rec stream drunk at stream_left with dissolve
            show mac stream neutral at stream_right_mac with dissolve
            recS "You know when you've lived here for so long you get used to it, truly."
            if viewershipHigh == True:
                $ AddChatter (vig3_sc6_recmac_comment5)
            $ reactTarget = "vig3_sc6_recbonding" #timestamp 6:31
            show screen streamerCommentary
            macS "But it's so dangerous, are you not worried?"
            recS "Of course I worry, but no use in worrying all the time."
            menu: 
                "Say something."
                "Rec's right.":
                    $ csEngagement += 1 #Logic: This is a good lesson for the kid to be learning
                    $ kcEngagement += 1
                    $ macHope += 1
                    $ setEngagement()
                    mS "They're right, just because something is difficult doesn't mean you need to worry all the time."
                    mS "How you work through that is more important."
                    $ AddChatter (vig3_sc6_right_comment1)
                    play audio "macOK.wav"
                    macS "I think I understand."
                    $ AddChatter (vig3_sc6_right_comment2)
                    show rec stream happy at stream_center with dissolve
                    recS "You know, Moze, I do admire what you do, it's a tough life but it's yours."
                    if viewershipHigh == True:
                        $ AddChatter (vig3_sc6_right_comment3)
                        pause 0.5
                    $ AddChatter (vig3_sc6_right_comment4)
                    "I smile."
                    $ AddChatter (vig3_sc6_right_comment5)
                    mS "It has its good moments."
                    play audio "macHappy.wav" volume 1.2
                    macS "Like candy!" 
                    mS "Exactly. That's why we go through the worry."
                    $ AddChatter (vig3_sc6_right_comment6)
                    recS "You know..."
                    recS "I was so scared when Allistar decided to join the Snakehawks."
                    recS "But I'm happy he had you with him."
                    recS "It made me worry less."
                    mS "Rec, I should tell you—"
                "Rec should really consider moving.":
                    $ macPessimism += 1
                    $ pdEngagement -= 1 #Logic: pickledDragons would wonder why you'd leave just cause it's hard
                    $ setEngagement()
                    ##Logic: I think the other viewers would not have much of a reaction to this one, specifically because it's focused on Rec, not MAC.
                    mS "Rec, ever thought that moving would be the right call?"
                    recS "Oh that's rich coming from you."
                    $ AddChatter (vig3_sc6_moving_comment1)
                    mS "I'm just saying there's better places than this one."
                    mS "With less Hounds."
                    $ AddChatter (vig3_sc6_moving_comment2)
                    recS "I like my shop and my community, I don't regret planting roots here."
                    recS "Plus when Allistar was with the Snakehawks I always knew you'd be here after your missions."
                    if viewershipHigh == True:
                        $ AddChatter (vig3_sc6_moving_comment3)
                    recS "I'm happy I get to see him as much as I do." #How do you feel about this being in present tense? He doesn't know Allistar's dead. Granted, it's been a really long time, but still
                    recS "Or did, until he stopped coming by."
                    "A pit forms in my stomach."
                    $ AddChatter (vig3_sc6_moving_comment4)
                    mS "I didn't mean to offend."
                    mS "You found a place that is yours."
                    $ AddChatter (vig3_sc6_beautiful_comment5)
                    recS "I'll be sure to fight for it."
                    mS "Rec, I should tell you—"
                    hide rec stream happy with dissolve
                "Akar is beautiful if you look in the right places.":
                    $ macHope += 2
                    $ csEngagement -= 1 #Logic: Coriolis would agree with the sentiment, but Akar is a messed up place to them
                    $ kcEngagement += 1 #Logic: kc and pd like this idea
                    $ pdEngagement += 1
                    $ setEngagement()
                    mS "It may not look it, but Akar is beautiful."
                    $ AddChatter (vig3_sc6_beautiful_comment1)
                    if viewershipHigh == True:
                        pause 0.5
                        $ AddChatter (vig3_sc6_beautiful_comment2)
                    mS "Didn't you see all the colour and community here?"
                    play audio "macPester.wav" volume 1.2
                    macS "People were getting hurt."
                    $ AddChatter (vig3_sc6_beautiful_comment3)
                    mS "Sure, but that's not all the time and people get hurt everywhere."
                    recS "That doesn't mean you can't surround yourself with good people."
                    if viewershipHigh == True:
                        $ AddChatter (vig3_sc6_beautiful_comment4)
                        pause 0.5
                        $ AddChatter (vig3_sc6_beautiful_comment5)
                        pause 0.5
                        $ AddChatter (vig3_sc6_beautiful_comment6)
                    macS "Like what we have?"
                    if viewershipHigh == True:
                        $ AddChatter (vig3_sc6_beautiful_comment7)
                    mS "Yeah, kid."
                    show rec stream happy
                    recS "So cute..."
                    "I feel my face get warm. Then an undeniable pit forming."
                    show rec stream neutral
            "A part of the bar goes silent as a burly man stands to address the crowd."
            hide mac with dissolve
            hide rec with dissolve
            hide screen streamerCommentary
            show zan stream neutral at stream_center with dissolve
            play audio "disruptiveBang.wav" volume 1.5
            zan "Patrons! Who is brave enough to ride Karousel!"
            $ AddChatter (vig3_sc6_recmac_comment7)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter (vig3_sc6_recmac_comment8)
            pause 0.5
            $ AddChatter (vig3_sc6_recmac_comment9)
            "Makers, not this game. What kind of idiot would even take that challenge—"
            pS "Right here!"
            "Jennica marches to the man who laughs."
            if viewershipHigh == True:
                $ AddChatter (vig3_sc6_recmac_comment10)
            show jennica stream neutral at stream_left with dissolve
            show zan stream laugh
            zan "So small, already tipping over, I fear you may not survive haha!"
            $ AddChatter (vig3_sc6_recmac_comment11)
            show jennica stream angry
            "A small group of patrons at a table behind him laugh."
            pS "Then you have nothin' to worry about."
            show zan stream neutral
            zan "Apologies, but I will not pick you up from the floor when you lose."
            if viewershipHigh == True:
                $ AddChatter (vig3_sc6_recmac_comment12)
            pS "Please."
            $ AddChatter (vig3_sc6_recmac_comment13)
            "Teresa sidles up next to Jennica."
            show teresa stream neutral at stream_right with dissolve
            enS "The lady said she'd like to ride the Karousel."
            $ AddChatter (vig3_sc6_recmac_comment14)
            zan "Two of you! I'll need a bigger mop!"
            if viewershipHigh == True:
                $ AddChatter (vig3_sc6_recmac_comment15)
                pause 0.5
                $ AddChatter (vig3_sc6_recmac_comment16)
                pause 0.5
                $ AddChatter (vig3_sc6_recmac_comment17)
            "A woman from the table flanks him, she rivals him in size."
            enS "So does that mean you're ready to play?"
            zan "Haha! I like you, moxie!"
            $ AddChatter (vig3_sc6_recmac_comment18)
            pS "Moxie's our middle name."
            zan "That is strange... but {i}Zan approves!{/i}"
            $ AddChatter (vig3_sc6_recmac_comment19)
            "He lifts up two thumbs and points to himself, then speaks to the woman in a language I don't understand."
            "She nods and picks up a large table to make the play area. Jennica and Zan speak for a moment before shaking hands."
            hide jennica with dissolve
            hide teresa with dissolve
    #This will be where we start after the stranger track#
    zan "The bet is done! Mr. Stein. Zan requests The Karousel, please!"
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment18)
    "Bet? What bet?"
    $ AddChatter (vig3_sc6_bbpub_comment19)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment21)
    "A small man holds up the Karousel high over his head, I barely see him before it appears on the table and the door to the back room swings closed."
    $ AddChatter (vig3_sc6_bbpub_comment20)
    hide zan with dissolve
    show mac neutral stream at stream_right_mac with dissolve
    show rec stream drunk at stream_left with dissolve 
    macS "Are they playing Brikarousel?"
    $ AddChatter (vig3_sc6_bbpub_comment22)
    recS "Aren't you too young to know that game?"
    $ AddChatter (vig3_sc6_bbpub_comment23)
    macS "I have a full database that allows me to know a myriad of games."
    show rec stream thinking
    recS "A full database..."
    $ AddChatter (vig3_sc6_bbpub_comment24)
    "Rec's eyes move back on the gambling table, Jennica and Teresa are deep in conversation."
    recS "You know I never understood this game."
    $ AddChatter (vig3_sc6_bbpub_comment25)
    play audio "macPing.wav" volume 1.2
    macS "Well Brikarousel was invented by Brika Alphonse approximately 30 years ago when..."
    show rec stream drunk
    recS "I meant why people are so eager to play."
    $ AddChatter (vig3_sc6_bbpub_comment26)
    pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment27)
    pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment28)
    macS "Oh."
    macS "Alcohol?"
    mS "You catch on quick."
    "I look over at the table as a pit in my stomach forms."
    $ AddChatter (vig3_sc6_bbpub_comment29)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment30)
    mS "Bet? What did they bet?"
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment31)
    show rec stream thinking
    recS "I didn't hear, but I read lips a bit, a “sh” something?"
    mS "\"Sh\" something?"
    play audio "macPing.wav" volume 1.2
    macS "Shirt, shoes, shilling..."
    "Ship?"
    $ AddChatter (vig3_sc6_bbpub_comment32)
    "They wouldn't—"
    $ reactTarget = "vig3_sc6_shipbet1" #timestamp 6:34
    show screen streamerCommentary
    "No, that's stupid."
    $ AddChatter (vig3_sc6_bbpub_comment33)
    recS "Shorts? Shawls..."
    play audio "macAffirmative.wav" volume 1.2
    macS "Squash!"
    "..."
    "Okay, now that's stupid."
    "Teresa and Jennica bet the ship."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment34)
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment35)
    "Shit."
    hide rec with dissolve
    hide mac with dissolve
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    show zan stream neutral at stream_center with dissolve
    "A small man with dark hair and modified gray skin steps to the table."
    pS "Talkin' to us about bein' small and your guy is thinner than my jacket."
    $ AddChatter (vig3_sc6_bbpub_comment36)
    zan "Ovid is strong of heart, muscles on the inside."
    enS "That tends to be where they go, yes."
    ovid "Zan, must we always play this game whenever we go out?"
    zan "..."
    show zan stream laugh
    zan "YES!"
    $ AddChatter (vig3_sc6_bbpub_comment37)
    pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment38)
    hide screen streamerCommentary
    "The game starts off with a bang, the rules are simple, teams of two play hands to collect played cards from a pool." 
    $ AddChatter (vig3_sc6_bbpub_comment39)
    pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment40)
    "Some cards are worth points, the pair with the lower amount of points at the end of the round takes a shot from the Karousel."
    "The first team that withdraws or has a member drop loses."
    "... By round ten, it's not looking good."
    $ AddChatter (vig3_sc6_bbpub_comment41)
    zan "How is moxie?"
    pS "Stronger than my mama's back!"
    enS "I'm starting to feel mine in the back of my throat."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment42)
    "Teresa and Jennica look wrung out, but Zan and Ovid are sturdy despite drinking their fill."
    $ AddChatter (vig3_sc6_bbpub_comment43)
    pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment44)
    hide jennica with dissolve
    hide teresa with dissolve
    hide zan with dissolve
    show mac neutral stream at stream_right_mac with dissolve
    show rec stream drunk at stream_left with dissolve
    macS "They're cheating."
    show rec stream surprised
    recS "How did you—"
    mS "Of course! We've been out of the game too long."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment45)
    macS "We must tell someone, this is improper."
    show rec stream drunk
    mS "MAC I'm going to lay this out for you. No one cares if something is improper here."
    macS "Then we should do something."
    $ AddChatter (vig3_sc6_bbpub_comment46)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment47)
    mS "I'm already on it."
    play audio "macPing.wav" volume 1.2
    macS "And I'll help."
    menu: 
        "Say something."
        "Absolutely not!":
            $ kcEngagement -= 1 #Logic: mean to MAC, kc doesn't like
            $ csEngagement -= 1 #Logic: It's mean for Coriolis too
            $ setEngagement()
            mS "You will sit down and say nothing and let me handle it."
            $ AddChatter (vig3_sc6_macquestion_comment1)
            play audio "macGrumble.wav" volume 1.2
            macS "But I—"
            mS "But nothing, I don't need a liability right now. Understand?"
        "It's better if I just do it.":
            #Logic: this just makes sense, I don't think anyone would have a strong reaction to this. It maintains the status quo.
            mS "This is better as a solo mission."
            play audio "macGrumble.wav" volume 1.2
            macS "But I—"
            mS "I know you want to help but some things work better with less people."               
    play audio "macPester.wav" volume 1.5
    macS "But I'm part of this crew too!"
    "MAC's words echo through my head, but in my voice."
    $ AddChatter (vig3_sc6_bbpub_comment48)
    "Upset, scared of being left behind."
    $ AddChatter (vig3_sc6_bbpub_comment49)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment50)
    mS "You are, and you'll have other chances to prove it. Just not right now."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment51)
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment52)
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment53)
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment54)
    "When Jennica calls for a short recess, I know it's my time to head over."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment55)
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment56)
    hide rec with dissolve
    hide mac with dissolve
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    mS "I don't know if you've noticed..."
    $ AddChatter (vig3_sc6_bbpub_comment57)
    pS "We're losing—"
    enS "They're cheating."
    $ AddChatter (vig3_sc6_bbpub_comment58)
    enS "So are we, just not as effectively."
    mS "Better think of something fast after what you just bet."
    pS "Ya, Resa, I don't think hand signals are going to cut it here."
    $ AddChatter (vig3_sc6_bbpub_comment59)
    pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment60)
    "I swallow the knowledge that hand signals were the only thing they thought of after betting our ship."
    menu: 
        "There has to be signs for how they're doing this."
        "Check Ovid.":
            "Ovid stares blankly across the room poking at something metal in his mouth."
            pS "Ovid's not drinking."
            enS "An evaporator..."
            pS "Was wondering how that little guy is still standing."
            $ AddChatter (vig3_sc6_bbpub_comment61)
            "I look around the room for more signs."
    menu: 
        "There has to be more signs for how they're doing this."
        "Check the deck.":
            pS "The deck isn't right. I know a standard set when I see one."
            mS "That makes sense, especially if they're regulars."
            enS "Truly? All for a stupid game?"
            $ AddChatter (vig3_sc6_bbpub_comment62)
            "What else?"
    menu: 
        "There has to be more signs for how they're doing this."
        "Check the Karousel.":
            "Teresa's eyes are fixed on the Karousel."
            mS "The Karousel?"
            $ AddChatter (vig3_sc6_bbpub_comment63)
            enS "There's a delay before it settles. And one of their friends has been staring at his communicator all night."
            "I think that's all."
    "Ovid's tube, the deck, the Karousel. We have to deal with them."
    pS "We need to tip the table."
    enS "Can't do that while we play."
    mS "I got it covered, just stay standing until I do."
    "The game resumes and I step away."
    show zan stream laugh at stream_center with dissolve
    zan "Now! Moxie!"
    "I scan my options."
    show zan stream neutral
    "If I start a fight I'm sure I can get someone slammed into the table." 
    "That should take care of some of the issues."
    "I look at the ceiling where the carnivorous plants lie waiting and salivating."
    "One of the ropes for their netting looks frayed and worn. If I undo it then it's open season on that table. Maybe quits for the Karousel."
    $ AddChatter (vig3_sc6_bbpub_comment64)
    pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment65)
    "As I scan my options, I can feel MAC's attention on me."
    "He's really not gonna like this at all."
    $ AddChatter (vig3_sc6_bbpub_comment66)
    hide zan with dissolve
    hide jennica with dissolve
    hide teresa with dissolve
    menu:
        "How do I help Jennica and Teresa?"
        "Start a bar fight.":
            $ pdEngagement += 1 #Logic: pd likes the intensity, kc likes how Moze lies to get it started
            $ kcEngagement += 1
            $ csEngagement -= 1 #Logic: Coriolis is uninterested in another fight
            $ macViolence += 1
            $ setEngagement()
            "I see a young couple pinning each other on a pillar near the table." 
            "They're really in it."
            "Ah, young love, so easy to break."
            $ AddChatter (vig3_sc6_barfight_comment1)
            "When they separate, I go up to the young man and shove him."
            $ AddChatter (vig3_sc6_barfight_comment2)
            pause 0.5
            $ AddChatter (vig3_sc6_barfight_comment3)
            pause 0.5
            $ AddChatter (vig3_sc6_barfight_comment4)
            mS "How dare you! We spent five glorious nights together, you tell me you love me..."
            $ AddChatter (vig3_sc6_barfight_comment5) 
            mS "And after {i}months{/i} of not hearing from you I find you here with a random woman!"
            $ AddChatter (vig3_sc6_barfight_comment6)
            "His jaw is on the floor."
            wifenpc "Random!? I'm his wife!"
            $ AddChatter (vig3_sc6_barfight_comment7)
            husbnpc "What? huh? I don't—"
            $ AddChatter (vig3_sc6_barfight_comment8)
            pause 0.5
            $ AddChatter (vig3_sc6_barfight_comment9)
            mS "Oh typical, you don't what? Know me? Don't even remember proposing to me do you?"
            $ AddChatter (vig3_sc6_barfight_comment10)
            wifenpc "{i}Propose!?{/i}"
            $ AddChatter (vig3_sc6_barfight_comment11)
            pause 0.5
            $ AddChatter (vig3_sc6_barfight_comment12)
            wifenpc "So that's what you've been doing on your business trips, huh?"
            $ AddChatter (vig3_sc6_barfight_comment13)
            pause 0.5
            $ AddChatter (vig3_sc6_barfight_comment14)
            husbnpc "No-what?!? I don't even know her!"
            "Before I can even add fuel to the fire."
            $ AddChatter (vig3_sc6_barfight_comment15)
            "The youg woman hits him with a one-two combo that almost lands her a spot on the Oakley." 
            "He fumbles onto Ovid and the table."
            "Cards fly everywhere and, before I can process what happens, Zan has the man in a chokehold."
            show zan stream mad at stream_center with dissolve
            zan "You interrupt the Karousel!"
            "It's hand fifteen, and half the bar is up in arms."
            $ AddChatter (vig3_sc6_barfight_comment16)
            pause 0.5
            $ AddChatter (vig3_sc6_barfight_comment17)
            "Friends of the man square up with Zan's crew."
            "It's only when tiny Mr. Stein waddles to the table and promises a free round that the room begrudgingly settles."
            "Ovid coughs loudly before putting something in his pocket."
            "With cards scattered all over the floor the deck is replaced."
            "The Karousel is untouched, the rounds continues."
            hide zan with dissolve
        "Cut the rope holding the carnivorous plants.":
            $ pdEngagement += 1 #Logic: this option is just fun. Everyone likes it
            $ kcEngagement += 1
            $ csEngagement += 1
            $ setEngagement()
            "I take a look at the frayed rope and the netting that is so carefully holding back the plants."
            "How has no one changed the rope yet?"
            $ AddChatter (vig3_sc6_cutrope_comment1)
            "It's too easy and so dangerous."
            $ AddChatter (vig3_sc6_cutrope_comment2)
            "I move carefully to the hook with the rope."
            $ AddChatter (vig3_sc6_cutrope_comment4)
            mS "Excuse me, sorry, just tryna get a decent view."
            $ AddChatter (vig3_sc6_cutrope_comment3)
            husbnpc "Watch it man, c'mon we all want a good view."
            $ AddChatter (vig3_sc6_cutrope_comment5)
            pause 0.5
            $ AddChatter (vig3_sc6_cutrope_comment6)
            "I push my way to the wall and lean just behind it."
            "The rounds continue."
            show zan stream neutral at stream_center with dissolve
            zan "Another victory, another shot for you."
            show jennica stream angry at stream_left with dissolve
            pS "Fine meathead, you got it."
            show teresa stream neutral at stream_right with dissolve
            enS "Makers this is insanity."
            "Then I get an idea."
            mS "Drink! Drink! Drink! Drink!"
            "The bar is in an uproar. People are going to grab their nearest cups."
            "They're slamming the floor, the room is shaking."
            "Over the roaring cheers, I cut the rope."
            "The scream is so high-pitched I can't believe it comes from Zan."
            show zan stream mad
            zan "{i}Yeeeeeoooowww!{/i}"
            $ AddChatter (vig3_sc6_cutrope_comment7)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter (vig3_sc6_cutrope_comment8)
                pause 0.5
                $ AddChatter (vig3_sc6_cutrope_comment9)
            zan "They're alive!"
            "He's swatting at them like whack-a-moles. One plant's head pops like a grape."
            enS "Stein, get these out of here."
            zan "Ah ah {i}Ahhhhhh!{/i}"
            $ AddChatter (vig3_sc6_cutrope_comment10)
            pause 0.5
            $ AddChatter (vig3_sc6_cutrope_comment11)
            "Ten patrons were injured from Zan's wild flailing, the attacking plants destroyed."
            $ AddChatter (vig3_sc6_cutrope_comment12)
            "Stein with the help of his crew subdued the other plants and have begun to put up new netting."
            $ AddChatter (vig3_sc6_cutrope_comment13)
            pause 0.5
            $ AddChatter (vig3_sc6_cutrope_comment14)
            pause 0.5
            $ AddChatter (vig3_sc6_cutrope_comment15)
            "Zan's eyes dart from the game to the ceiling."
            $ AddChatter (vig3_sc6_cutrope_comment16)
            "Ovid coughs loudly before putting something in his pocket, the Karousel is replaced by an older model."
            $ AddChatter (vig3_sc6_cutrope_comment17)
            "The round continues."
            hide zan with dissolve
            hide teresa with dissolve
            hide jennica with dissolve

    #maybe fade in and out to show passage of time again?#
    "Round 25 is rough. Even with some of the obstacles out of the way Teresa and Jennica are barely holding on." 
    "Ovid is finally looking like he's playing the game, and Zan is rocking in his seat like a child."
    ovid "Please, call it quits?"
    $ AddChatter (vig3_sc6_bbpub_comment67)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment68)
    show teresa stream neutral at stream_right with dissolve 
    enS "Not likely."
    show zan stream neutral at stream_center with dissolve
    zan "Hehehe, I say I am impressed. And having the best of times!"
    show jennica stream neutral at stream_left with dissolve
    pS "Not after this you aren't."
    "When Zan and Ovid lose the round, an opportunity presents itself." 
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment69)
        pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment70)
    "Zan will tip his chair back to take his drink."
    "One clean shot to the leg and he's on the ground."
    "But that's risky."
    $ AddChatter (vig3_sc6_bbpub_comment71)
    "I could just leave it to the two of them to take it home. Ovid looks like he's on his last legs."
    $ AddChatter (vig3_sc6_bbpub_comment72)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment73)
    "But if they actually bet the ship then I don't know how we're gonna get it back."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment74)
    ###Two choices and three endings. If the player doesn't shoot they may or may not win which will have two separate endings. If they do shoot they will automatically win, this is also the Ama choice###
    $ viewCheck5 = viewCount
    menu:
        "How do I finish this?"
        "Shoot Zan's Leg.":
            $ vig3_outlaw += 1
            $ outlaw += 1
            $ macViolence += 2
            $ macPessimism += 1
            $ pdEngagement += 2 #Logic: pd's perspective: make sure you win
            $ kcEngagement -= 1 #Logic: kc and cs both really like Zan so this is unnecessarily rude in their view
            $ csEngagement -= 1
            $ setEngagement()
            $ vig3_zanApproval = False
            "I can't leave it up to chance, the crowd is completely absorbed by this game."
            $ AddChatter (vig3_sc6_shootzan_comment1)
            "Zan has a notable plate on his leg, a good shot should send him flying with minimal damage. Hopefully."
            $ AddChatter (vig3_sc6_shootzan_comment2)
            "I take my position."
            $ AddChatter (vig3_sc6_shootzan_comment3)
            "As I scan the bar for any eyes on me, I take in just how packed this place is. It's wall to wall."
            $ AddChatter (vig3_sc6_shootzan_comment4)
            "Then I see them, a small group near the door, half watching the game."
            $ AddChatter (vig3_sc6_shootzan_comment6)
            "Is that?"
            "No."
            "My vision is still betraying me and I don't have time to get a better look."
            zan "{i}For my loyal fans!{/i}"
            $ AddChatter (vig3_sc6_shootzan_comment5)
            "Zan does a messy cheers to Ovid, teeters his chair back to knock the shot into his mouth."
            $ AddChatter (vig3_sc6_shootzan_comment7)
            pause 0.5
            $ AddChatter (vig3_sc6_shootzan_comment8)
            "As I pull the trigger... Zan's eyes meet mine."
            "Damn."
            $ reactTarget = "vig3_sc6_shootingzan"#timestamp 6:37
            play audio "stunLazer.wav" volume 1.5
            hide zan with Dissolve (0.1)
            play audio "disruptiveBang.wav" volume 1.5
            "Zan falls hard. The pub is silent."
            $ AddChatter (vig3_sc6_shootzan_comment9)
            show screen streamerCommentary
            pS "{i}Hell yeah!{/i}"
            show jennica stream neutral at stream_left
            show teresa stream happy at stream_right
            "The crowd erupts. Zan's crew is visibly miffed, but the rest of the bar is patting Teresa and Jennica on the back."
            $ AddChatter (vig3_sc6_shootzan_comment10)
            show zan stream neutral at stream_center with dissolve
            "Zan gets up to accept defeat. Ovid has fully crawled under the table."
            $ AddChatter (vig3_sc6_shootzan_comment11)
            "I look over again to the crew, but that table is empty."
            $ AddChatter (vig3_sc6_shootzan_comment12)
            "The door swings closed."
            ovid "Thank the Makers it's over."
            show zan stream laugh
            zan "Good, good! {i}Now!{/i}"
            $ AddChatter (vig3_sc6_shootzan_comment13) 
            zan "I must go and throw up. {i}Haha!{/i}"
            "The three exchange handshakes as Zan passes by me and stops."
            show zan stream neutral
            $ AddChatter (vig3_sc6_shootzan_comment14)
            hide jennica with dissolve
            hide teresa with dissolve
            zan "You are Captain, no?" 
            menu: 
                "Respond to Zan."
                "And what's it to you?":
                    show zan stream mad
                    mS "And what's it to you?"
                    zan "You have a good crew, good moxie."
                    $ AddChatter (vig3_sc6_shootzan_comment15)
                    pause 0.5
                    $ AddChatter (vig3_sc6_shootzan_comment16)
                    mS "I'm aware."
                "The one and only!":
                    show zan stream mad
                    mS "The one and only!"
                    zan "You have a good crew, good moxie."
                    $ AddChatter (vig3_sc6_shootzan_comment15)
                    pause 0.5
                    $ AddChatter (vig3_sc6_shootzan_comment16)
                    mS "We like to show out."   
            zan "Good shot, but messy."
            zan "Have more faith next time."
            $ AddChatter (vig3_sc6_shootzan_comment17)
            pause 0.5
            $ AddChatter (vig3_sc6_shootzan_comment18)
            "Before I can respond, he pats my shoulder and I almost buckle under the weight of the impact."
            hide screen streamerCommentary
            hide zan with dissolve
            show jennica stream neutral at stream_left with dissolve
            show teresa stream happy at stream_right with dissolve
            "I move to greet my victors."
            mS "I can't believe we pulled that off. That was some risky business."
            pS "C'mon Cap, just harmless fun."
            "... what?"
            mS "Betting the ship is harmless to you?"
            $ reactTarget = "vig3_sc6_shipbet2"
            show screen streamerCommentary
            enS "The ship? What do you take us for?"
            enS "Zan asked us to perform a show for the bar if we lost."
            mS "A show?"
            pS "Mighty embarassin' that've been."
            pS "Everyone knows Resa sounds likes a torn up gear when she sings."
            enS "Agreed."
            pS "But all's well, big guy told us he'd comp our room for the night."
            "... I'm truly losing it."
            mS "Alright, well congrats then. I'm turning in."
            hide screen streamerCommentary
            hide teresa with dissolve
            hide jennica with dissolve
        "Trust the crew to win.":
            $ marshal += 1
            $ macHope += 1
            $ macPeace += 2
            $ csEngagement += 2 #Logic: Coriolis likes Moze trusting in her crew
            $ kcEngagement += 1 #Logic: kitcat likes not shooting Zan
            $ pdEngagement -= 1 #Logic: pickledDragons wants to shoot Zan
            $ setEngagement()
            $ vig3_zanApproval = True
            #need a variable to determine if they win or not.
            $ reactTarget = "vig3_sc6_trustcrew" #timestamp 6:37
            show screen streamerCommentary
            "There's a part of me that knows I'll regret this, but I don't go for my pistol."
            $ AddChatter (vig3_sc6_trustcrew_comment1)
            pause 0.5
            $ AddChatter (vig3_sc6_trustcrew_comment2)
            "These two are idiots, but they're my idiots."
            $ AddChatter (vig3_sc6_trustcrew_comment4)
            pause 0.5
            $ AddChatter (vig3_sc6_trustcrew_comment5)
            "And I have to trust they'll pull through."
            $ AddChatter (vig3_sc6_trustcrew_comment3)
            "The game keeps going."
            "So do the drinks."
            "26, 27, 28..."
            "... 29..."
            play audio "disruptiveBang.wav" volume 4.0
            "Then a loud crash."
            $ AddChatter (vig3_sc6_trustcrew_comment6)
            mS "No way." 
            macS "Oh my..."
            hide screen streamerCommentary 
            $ vig3_brika = renpy.random.randint(0, 1)
            if vig3_brika == 0:
                show jennica stream neutral at stream_left
                show teresa stream happy at stream_right
                "Ovid is under the table."
                mS "WE DID IT!"
                "The whole bar is roaring!"
                $ AddChatter (vig3_sc6_trustcrew_comment7)
                "Zan pushes the table away and goes to make sure Ovid is alright."
                hide zan with dissolve
                "I move to greet my victors."
                $ AddChatter (vig3_sc6_trustcrew_comment8)
                mS "I can't believe you pulled that off. That was some risky business."
                $ AddChatter (vig3_sc6_trustcrew_comment9)
                pause 0.5
                $ AddChatter (vig3_sc6_trustcrew_comment10)
                pS "C'mon Cap, just harmless fun."
                mS "Betting the ship is harmless to you?"
                enS "The ship? What do you take us for?" 
                enS "Zan asked us to perform a show for the bar if we lost."
                $ reactTarget = "vig3_sc6_shipbet2"
                show screen streamerCommentary
                mS "A show?"
                pS "Mighty embarassin' that've been, Everyone knows Resa sounds likes a torn up gear when she sings."
                enS "Agreed."
                pS "But all's well—"
                "... I'm truly losing it."
                "Just then Zan comes over to us and kneels."
                show zan stream neutral at stream_center with dissolve
                zan "I must make good on promise."
                $ AddChatter (vig3_sc6_bbpub_comment78)
                show zan stream laugh
                "Teresa and Jeneca each take a seat on one flexed arm."
                "Zan hoists them in the air and parades them around the bar."
                $ AddChatter (vig3_sc6_bbpub_comment79)
                zan "MOXIE MOXIE MOXIE MOXIE!"
                $ AddChatter (vig3_sc6_bbpub_comment80)
                pause 0.5
                $ AddChatter (vig3_sc6_bbpub_comment81)
                "When they look back I give them a nod like I'm ready to turn in."
                hide teresa with dissolve
                hide jennica with dissolve
                hide zan with dissolve
            else:
                show jennica stream neutral at stream_left
                show teresa stream happy at stream_right
                "Jennica's under the table"
                mS "Oh no..."
                "The whole bar is roaring!"
                $ AddChatter (vig3_sc6_bbpub_comment75)
                "Zan pushes the table away and goes to hug Ovid who looks like his eyes are about to pop out."
                hide zan with dissolve
                "I move to help Jennica."
                $ AddChatter (vig3_sc6_bbpub_comment76)
                enS "C'mon Jenn, you're good, you're alright."
                pS "Did... Did we win?"
                enS "Sorry, sweetheart we didn't."
                $ AddChatter (vig3_sc6_bbpub_comment77)
                mS "Makers, why did you bet the ship?"
                enS "The ship? What do you take us for?"
                $ AddChatter (vig3_sc6_bbpub_comment81) 
                enS "Zan asked us to perform a show for the bar if we lost."
                $ reactTarget = "vig3_sc6_shipbet2"#timestamp 6:38
                show screen streamerCommentary
                mS "A show?"
                $ AddChatter (vig3_sc6_bbpub_comment82)
                pS "A show! Oh scrap, you sound horrible when you sing Resa."
                enS "Still better than you."
                $ AddChatter (vig3_sc6_bbpub_comment83)
                pS "But we must press on! *hick*"
                "... I'm truly losing it."
                "Just then Zan comes over to us."
                show zan stream neutral at stream_center with dissolve
                zan "You must make good on promise."
                $ AddChatter (vig3_sc6_bbpub_comment84)
                "Teresa helps Jennica get up and they stand on the Karousel table."
                "Zan yells for music." #The melody is "C'est a ton tour"
                show zan stream laugh
                "Teresa and Jennica begin to sing."
                pS "Zan is the man! Zan has a plan! Zan's got the muscles to beat any man." 
                enS "Ovid's the best! Above all the rest! With muscles inside to pass any test."
                "When they look back I give them a nod like I'm ready to turn in."
                "They continue in broken harmony." 
                hide teresa with dissolve
                hide jennica with dissolve 
                hide zan with dissolve        
    hide screen streamerCommentary            
    "I head back to Rec and MAC."
    show rec stream drunk at stream_left with dissolve
    show mac stream neutral at stream_right_mac with dissolve
    mS "I'm taking the kid, we'll check in with you tomorrow at the shop, alright?"
    recS "Sure thing, Cap."
    $ AddChatter (vig3_sc6_bbpub_comment85)
    stop music fadeout 4.0
    show rec stream thinking
    recS "Actually, Moze wait."
    "They look serious."
    mS "What's going on?"
    recS "MAC isn't a normal bot is he?"
    "I take a moment and look down at MAC."
    "It's been long enough."
    mS "No... he's not."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment86)
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment87)
    recS "BigCorp has been deploying agents everywhere."
    recS "They're looking for something {i}big.{/i}"
    recS "Lots of rumors about what that could be."
    $ AddChatter (vig3_sc6_bbpub_comment88)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment89)
    "MAC looks away." 
    $ AddChatter (vig3_sc6_bbpub_comment90)
    pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment91)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc6_bbpub_comment92)
    mS "So then you can imagine why we can't let them have him."
    "Rec looks down at MAC."
    $ AddChatter (vig3_sc6_bbpub_comment93)
    pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment94)
    show rec stream happy
    recS "He's a special kid."
    $ AddChatter (vig3_sc6_bbpub_comment95)
    "Something flashes behind their eyes. I remember Allistar."
    $ AddChatter (vig3_sc6_bbpub_comment96)
    pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment97)
    recS "We'll keep looking for that part tomorrow."
    $ AddChatter (vig3_sc6_bbpub_comment98)
    "MAC waves to Rec as they leave."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc6_bbpub_comment99)
        pause 0.5
    $ AddChatter (vig3_sc6_bbpub_comment100)
    recS "See ya, buddy."
    "We turn in."
    stop backAudio fadeout 1.0
    hide rec with dissolve
    hide mac with dissolve
    hide bbpub_stream with dissolve
    jump vig3_sc7

label vig3_sc7():
    play music "soundtrack/akar(day).wav" volume 0.8
    show akarplaza_stream at topleft onlayer background with dissolve
    "The next day is hot. The hangover in my brain is smashing at my skull like it's the bars of a prison."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    enS "All day searching, and nothing?"
    pS "Well there was that one guy."
    enS "He tried to sell a walking stick he carved when we asked for a range extender."
    pS "I thought it was quite lovely."
    "MAC is silent."
    mS "Alright, kid?"
    show mac stream neutral at stream_center_mac with dissolve
    play audio "macGrumble.wav" volume 1.2
    macS "Yes, I hope we can find a lead soon."
    $ AddChatter (vig3_sc7_akarplaza_comment1)
    menu:
        "Respond to MAC."
        "Cheer up bud!":
            mS "Cheer up kid, we'll find it!"
            "MAC looks unconvinced. And tired?"
            $ AddChatter (vig3_sc7_akarplaza_comment2)
        "We'll find it I promise.":
            mS "It'll just be a little longer, but we'll find it."
            "MAC looks unconvinced. And tired?"
            $ AddChatter (vig3_sc7_akarplaza_comment2)
    ##Conversation with MAC?##
    hide mac with dissolve
    $ AddChatter (vig3_sc7_akarplaza_comment3)
    "Rec gave us some good starting points, but after searching for hours we notice that most operations aren't running with their usual stock because of the Inventor's Fair."
    mS "We might need to split up."
    enS "I agree, we'll cover more ground."
    pS "Are we just looking to buy?"
    #player choice
    menu:
        "How do we want to approach getting the antenna?"
        "Whatever it takes.":
            $ macPessimism += 1
            $ engineerApproval += 1
            $ pilotApproval -= 1
            $ pdEngagement += 1
            $ csEngagement -= 1
            mS "Do whatever it takes, we need that part and we'll take it if necessary."
            pS "All in then. Got it."
        "Don't cause any unnecessary drama.":
            $ macHope += 1
            $ pilotApproval += 1 #Logic: As established in vignette 2, Jenn is more marshal, Teresa is more outlaw
            $ engineerApproval -= 1
            $ pdEngagement -= 1 #Logic: cs is marshal, pd is outlaw. Pretty straightforward imo
            $ csEngagement += 1
            mS "We need to do everything we can to get that part but we can't cause problems."
            enS "Go for option A, option B if necessary."
    $ setEngagement()
    enS "I'll head to the plaza, Jennica the outskirts. Moze you take MAC and do another sweep of the shops near Rec."
    mS "Perfect, Resa, let's get started then. Now, MAC—"
    if viewershipHigh == True:
        $ AddChatter (vig3_sc7_akarplaza_comment4)
        pause 0.5
        $ AddChatter (vig3_sc7_akarplaza_comment5)
    stop music fadeout 0.5
    "Fear surges through my body as I look between the three of us. MAC is nowhere to be found."
    mS "MAC!"
    $ AddChatter (vig3_sc7_akarplaza_comment6)
    hide teresa stream with Dissolve(0.2)
    hide jennica stream with Dissolve(0.2)
    "I know Teresa and Jennica are screaming for him, but I can't hear them. I can't hear anything but my heart pounding in my chest."
    $ AddChatter (vig3_sc7_akarplaza_comment7)
    "Where is he?"
    "{i}Where is he!?{/i}"
    $ AddChatter (vig3_sc7_akarplaza_comment8)
    "Then I see him, far in the distance, wheeling himself slowly to a group of people."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc7_akarplaza_comment9)
    "To a group of Hounds."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc7_akarplaza_comment10)
        pause 0.5
        $ AddChatter (vig3_sc7_akarplaza_comment11)
        pause 0.5
    $ reactTarget = "vig3_sc7_lostmac"
    show screen streamerCommentary
    if viewershipHigh == True:
        $ AddChatter (vig3_sc7_akarplaza_comment12)
    "My feet move before my brain can register what is happening."
    "It happens so fast, MAC runs into the leader, his arms frantic."
    "They swarm him. My feet aren't moving fast enough."
    $ AddChatter (vig3_sc7_akarplaza_comment15)
    pause 0.5
    $ AddChatter (vig3_sc7_akarplaza_comment17)
    pause 0.5
    if viewershipHigh == True:
        $ AddChatter (vig3_sc7_akarplaza_comment16)
        pause 0.5
        $ AddChatter (vig3_sc7_akarplaza_comment18)
    "I can't think of anything but how fast my legs should be moving." 
    $ AddChatter (vig3_sc7_akarplaza_comment19)
    "{i}Move faster!{/i}"
    $ AddChatter (vig3_sc7_akarplaza_comment14)
    "When they take him and drive away, I don't register how a cruiser almost hits me, I don't feel the pain of my knees when they hit the ground."
    $ AddChatter (vig3_sc7_akarplaza_comment20)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc7_akarplaza_comment21)
        pause 0.5
        $ AddChatter (vig3_sc7_akarplaza_comment22)
    "All I can hear is Ama's voice in my head: \"You'll have the chance to prove it, just not right now.\"" ##Consider changing this line##
    $ AddChatter (vig3_sc7_akarplaza_comment13)
    hide screen streamerCommentary
    #hide cockpit_mess_stream
    jump vig3_sc8

label vig3_sc8():
    show bg black at topleft onlayer background 
    hide akarplaza_stream with dissolve
    pause 1.0
    "I don't remember much after."
    "We knew we couldn't chase down the Hounds. There was nothing that could be done once MAC was out of sight."
    "It was Rec who gave us the suggestion to intercept them where they were. That meant in the belly of the beast: Reynar's Vineyard."
    "Nothing short of the worst case scenario."
    show exteriorvineyard_stream at topleft onlayer background with dissolve
    hide bg black
    show jennica stream neutral at stream_left with dissolve
    pS "You know I'm not a fancy sort of gal, but my butt looks fantastic in this."
    $ AddChatter (vig3_sc8_vineyardext_comment1)
    "Jennica has not stopped looking at herself in every reflective surface since she put on the new clothes." 
    if viewershipHigh == True:
        $ AddChatter (vig3_sc8_vineyardext_comment2)
    "Not surprised that the first thing she does out of the luxury cruiser is stare at herself in the window."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc8_vineyardext_comment3)
    pS "Sorry, Jimmy, gotta make sure the girls are in order before I do some serious ass-kicking."
    $ AddChatter (vig3_sc8_vineyardext_comment4)
    "Jimmy is a friend of Rec's who owns a luxury cruiser company and thankfully owed them a favour."
    show teresa stream neutral at stream_right with dissolve
    enS "Can you give it a rest. There are people around."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc8_vineyardext_comment7)
        pause 0.5
        $ AddChatter (vig3_sc8_vineyardext_comment8)
    pS "I thought you'd want me to look presentable?"
    $ AddChatter (vig3_sc8_vineyardext_comment5)
    mS "You need to be serious about this."
    pS "Oh I'm very serious, just my face don't look it. Y'all should consider fixin' yours."
    $ AddChatter (vig3_sc8_vineyardext_comment6)
    "Rec moves their jaw as if trying to manually relax it."
    "I relax my shoulders as an attendant walks over to us."
    vyattend "Good afternoon, my name's Ryo, and it is my pleasure to welcome you to the Vineyard." 
    vyattend "Are you perhaps here for the Inventor's Fair?"
    show teresa stream happy
    enS "Pleased to make your acquaintance, Ryo. Please check the list for Vira Prismari and retinue."
    "They raise an eyebrow before checking a screen."
    vyattend "Prismari?"
    enS "That is correct." 
    "There's a long pause."
    $ AddChatter (vig3_sc8_vineyardext_comment9)
    reynar "Ryo, I'll take it from here."
    "Our jaws nearly drop at the finely dressed man who approaches us. Reynar..."
    show reynar stream neutral at stream_center with dissolve
    if viewershipHigh == True:
        $ AddChatter (vig3_sc8_vineyardext_comment10)
    reynar "How wonderful, we were certain to receive another refusal gift this year."
    enS "Well, we so desperately missed the inspiration of the Inventor's Fair."
    $ AddChatter (vig3_sc8_vineyardext_comment11)
    enS "I hope you are well to accommodate us?"
    reynar "I must say your posse is such a surprise. It's so... pleasantly unexpected."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc8_vineyardext_comment12)
    "It's like watching a tennis match with a bomb for a ball."
    enS "You know we are so thankful your consideration every year, and it is so lovely to see our donations put to such good use."
    $ AddChatter (vig3_sc8_vineyardext_comment14)
    pause 0.5
    $ AddChatter (vig3_sc8_vineyardext_comment15)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc8_vineyardext_comment16)
    enS "You've truly spared no expense."
    reynar "Of course, we want to celebrate all those who contribute to the research and development of the Outposts."
    enS "The Prismari family is always proud to support this iconic hub of innovation."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc8_vineyardext_comment13)
    reynar "You've offered much more than support."
    reynar "We are pleased to have you back, Miss Prismari."
    "Reynar nods to us and walks away cooly. Leaving to welcome in other guests."
    hide reynar stream with dissolve
    show teresa stream neutral
    $ reactTarget = "vig3_sc8_teresabluff"
    show screen streamerCommentary#timestamp 6:43
    pS "You're a bit scary when you're proper."
    show rec stream formal thinking at stream_center with dissolve
    mS "You sure what just happened back there was alright?"
    enS "If Reynar really wanted us gone he would've kicked us out already."
    pS "So why didn't he..."
    mS "Does he think your family will take care of it?"
    enS "Please. My family hasn't come to these since I was exiled. Doubtful they'll even know I was here."
    enS "We're in, that's what matters."
    mS "Got it."
    enS "And thank you, Reccrin. Couldn't have done it without you getting us ready."
    show rec stream formal neutral
    recS "I've been here for years and never set foot in the Inventor's Fair. I'd give you my whole shop if ya needed."
    $ AddChatter (vig3_sc8_vineyardext_comment17)
    pause 0.5
    $ AddChatter (vig3_sc8_vineyardext_comment18)
    pause 0.5
    $ AddChatter (vig3_sc8_vineyardext_comment19)
    pause 0.5
    $ AddChatter (vig3_sc8_vineyardext_comment20)
    $ viewCheck6 = viewCount
    hide rec with dissolve
    hide teresa with dissolve
    hide jennica with dissolve
    play backAudio "crowdParty.wav" volume 0.5 loop fadein 0.5
    play music "soundtrack/akar(fair).wav" fadein 1.0
    show inventorsfairgallery_stream at topleft onlayer background with dissolve 
    hide exteriorvineyard_stream
    "The Inventor's Fair is even more insane looking than I could've imagined. The fanfare in Akar is a kid's birthday party by comparison." 
    $ AddChatter (vig3_sc9_inventorsfair_comment1)
    "Brimming with shine and luster. Inventors have lined up pedestals with tech I can't even begin to understand."
    $ AddChatter (vig3_sc9_inventorsfair_comment2)
    pause 0.5
    $ AddChatter (vig3_sc9_inventorsfair_comment3)
    "Finely dressed guests are being served by Reynar's android wait staff." 
    hide screen streamerCommentary
    "Carefully plated exotic food and drink fill the silver trays that circulate the a gallery-style showroom."
    $ AddChatter (vig3_sc9_inventorsfair_comment4)
    pause 0.5
    $ AddChatter (vig3_sc9_inventorsfair_comment5)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc9_inventorsfair_comment6)
    show teresa stream happy at stream_right with dissolve
    enS "Apparently the theme is Lost Renaissance, remembering a time long past..."
    $ AddChatter (vig3_sc9_inventorsfair_comment7)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc9_inventorsfair_comment8)
    show jennica stream neutral at stream_left with dissolve
    pS "That why some of these statues don't have arms?"
    enS "I think they're being loose with the theme."
    $ AddChatter (vig3_sc9_inventorsfair_comment9)
    "It's excess at its highest degree, so much that I can't imagine us finding MAC in all of this."
    $ AddChatter (vig3_sc9_inventorsfair_comment10)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc9_inventorsfair_comment11)
    show rec stream formal neutral at stream_center with dissolve
    recS "Reynar likes to personally assess what the Hounds find so they're probably holding MAC somewhere close by."
    pS "Let's rough up some suits and find out where they've got him."
    $ AddChatter (vig3_sc9_inventorsfair_comment12)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc9_inventorsfair_comment13)
    "Teresa turns around and stops us in our tracks."
    show teresa stream neutral
    if viewershipHigh == True:
        $ AddChatter (vig3_sc9_inventorsfair_comment14)
        pause 0.5
        $ AddChatter (vig3_sc9_inventorsfair_comment15)
    enS "Okay, let's make this crystal. We'll not be doing anything of the like."
    pS "Resa—"
    enS "Listen, Jenn, I appreciate how ready you are to fight for MAC. But you don't understand the situation we're in." 
    $ AddChatter (vig3_sc9_inventorsfair_comment16)
    pause 0.5
    $ AddChatter (vig3_sc9_inventorsfair_comment17)
    pS "I ain't scared of the Hounds."
    menu:
        "Who do you side with?"
        "Side with Jennica.":
            $ engineerApproval -= 1
            $ pilotApproval += 1
            $ csEngagement += 1 #Logic: Coriolis is team Jennica, kitcat is team Teresa
            mS "Listen, Resa, Mac's too important, we'll get into a fight if we have too."
            $ AddChatter (vig3_sc9_jennica_comment1)
            pS "Never knew ya to be timid, Resa."
            enS "You two are not understanding..."
        "Side with Teresa.":
            $ engineerApproval += 1
            $ pilotApproval -= 1
            $ kcEngagement += 1
            mS "I understand the passion but we should stick with Teresa's plan for now."
            $ AddChatter (vig3_sc9_teresa_comment1)
            pS "But MAC's as good as gone if we don't do anything."
            enS "Jenn, you must understand."
    $ setEngagement()
    enS "The reason Reynar is using the Hounds in the first place is because all of his actual security is here. Look around." 
    $ AddChatter (vig3_sc9_jennica_comment2)
    "I'm almost embarrassed by how long it took me to realize."
    $ AddChatter (vig3_sc9_teresa_comment2)
    "I can feel dozens of eyes on us."
    "The androids here aren't just waiting, they're scanning, searching. A step too far out of line and that's it for us."
    $ AddChatter (vig3_sc9_inventorsfair_comment18)
    pS "So now what?"
    enS "Schmooze, flirt, impress, find any way for someone to give you information, but more importantly access."
    $ AddChatter (vig3_sc9_inventorsfair_comment19)
    pS "I ain't much of a talker..."
    $ AddChatter (vig3_sc9_inventorsfair_comment20)
    show rec stream formal happy
    recS "How about we do this together, Jenn? I'd like to see the work maybe even chat up some of the researchers here."
    $ AddChatter (vig3_sc9_inventorsfair_comment21)
    pause 0.5
    $ AddChatter (vig3_sc9_inventorsfair_comment22)
    pS "I'd like that."
    enS "Perfect! Cap, let's fan out and figure this out."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc9_inventorsfair_comment23)
    mS "Got it, let's be perfect guests for the Fair and do recon. More importantly stay in eyesight."
    enS "And, Jenn..."
    pS "Hmm?"
    enS "Mind your manners please."
    pS "Course, milady."
    "Jenn tips an imaginary hat and walks away with Rec."
    hide jennica with dissolve
    hide rec with dissolve
    show teresa stream upset
    enS "We're doomed."
    mS "Just might be."
    hide teresa with dissolve
    jump vig3_sc9

label vig3_sc9():
    show inventorsfairgallery_stream at topleft onlayer background with dissolve
    hide exteriorvineyard_stream with dissolve
    invfairnpc1 "I told them raising Silver Badgers was a terrible idea! Now they have a torn up farm and no coats to show for it."
    "My eyes nearly roll out of my head at the forced laughter from the surrounding guests."
    $ AddChatter (vig3_sc9_inventorsfair_comment24)
    "I hate schmoozing. The evening has droned on and absolutely no leads or sign of MAC anywhere."
    $ AddChatter (vig3_sc9_inventorsfair_comment25)
    "I see Jenn taking an interested sip of her drink as Rec chats up some presenters near their inventions. One of the other guest follows my sight line." 
    $ AddChatter (vig3_sc9_inventorsfair_comment26)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc9_inventorsfair_comment27)
    "I think their name was Mills?"
    invfairnpc2 "I know it's such an eyesore, that arm should be scrapped honestly."
    mS "Don't you have modified teeth."
    invfairnpc2 "Of course, but you could never tell!"
    invfairnpc2 "I swear, they let anyone in the Fair nowadays."
    mS "Truly..."
    "This guy's an snob. Maybe we should do something about it?"
    menu:
        "This guy's an snob. Maybe we should do something about it?"
        "Let it be.":
            $ csEngagement += 1 #Logic: coriolis wants you to play it lowkey
            $ pdEngagement -= 1 #Logic: pickledDragons wants you to do something
            $ kcEngagement -= 1 #Logic: kitcat is morally outraged about this guy
            $ setEngagement()
            "I can feel the anger boiling up to my throat."
            "It's so tempting just to trip these snobs into the drink table."
            $ AddChatter (vig3_sc9_letitbe_comment1)
            pause 0.5
            $ AddChatter (vig3_sc9_letitbe_comment2)
            invfairnpc2 "And that dress? Off the rack from Akar no doubt."
            $ AddChatter (vig3_sc9_letitbe_comment3)
            invfairnpc1 "Not Akar! A half-way town for drunks and undesirables."
            $ AddChatter (vig3_sc9_letitbe_comment5)
            invfairnpc2 "Sometimes makes you wish BigCorp took over."
            $ AddChatter (vig3_sc9_letitbe_comment4)
            invfairnpc1 "All hail the Snakehawks..."
            $ AddChatter (vig3_sc9_letitbe_comment6)
            invfairnpc2 "And now their former leader is BC's personal dog."
            "I can't take this."
            $ AddChatter (vig3_sc9_letitbe_comment7)
            mS "Excuse me for a moment."
            $ AddChatter (vig3_sc9_letitbe_comment8)
            "I move on, scanning the gallery, I see Teresa looking in her element, gliding through various groups with a natural grace. Never lingering too long."
            showgirl "Weren't they a piece of work."
            show daisy stream neutral at stream_center with dissolve
            $ reactTarget = "vig3_sc9_daisyreturns"
            show screen streamerCommentary
            "A familiar batch of feathers block my view. Daisy stands in all her showgirl glory with some added refinement."
            mS "Is everyone here like that."
            showgirl "Thankfully not everyone."
            mS "Daisy, was it?"
            $ AddChatter (vig3_sc9_inventorsfair_comment28)
            show daisy stream think
            showgirl "You bet?"
            $ AddChatter (vig3_sc9_inventorsfair_comment29)
            mS "50 Credits at Nova Casino."
            if viewershipHigh == True:
                $ AddChatter (vig3_sc9_inventorsfair_comment30)
            showgirl "What a terrible deal. That barely gets you a few good spins, not even a buy-in at a low ball table."
            mS "I guess the only big win anyone is getting is at the bar."
            show daisy stream neutral
            "We both laugh, a genuine laugh."
            $ AddChatter (vig3_sc9_inventorsfair_comment31)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter (vig3_sc9_inventorsfair_comment32)
            mS "I'm sorry for earlier, I've been on edge."
            showgirl "Don't sweat it, if you weren't going to shoot me I was. I hate that script."
            mS "Costume is great though."
            $ AddChatter (vig3_sc9_inventorsfair_comment33)
            pause 0.5
            $ AddChatter (vig3_sc9_inventorsfair_comment34)
            showgirl "Why, you flatter me. It is one of my favourite parts."
            "Daisy sways in front of me to show off the movement of her feathers."
            mS "Fabulous. Truly."
            "She has such a sweet smile."
            if viewershipHigh == True:
                $ AddChatter (vig3_sc9_inventorsfair_comment35)
                pause 0.5
                $ AddChatter (vig3_sc9_inventorsfair_comment36)
                pause 0.5
            $ AddChatter (vig3_sc9_inventorsfair_comment37)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter (vig3_sc9_inventorsfair_comment38)

        "Trip them.":
            $ csEngagement -= 1
            $ pdEngagement += 1
            $ kcEngagement += 1
            $ setEngagement()
            "Now, I know I'm supposed to be on my best behavior, but I have limits. Just as Mills steps towards a drink tray I make sure to step ever so gently on the fabric of their flared pants."
            "They tumble over knocking several drinks onto themselves."
            $ AddChatter (vig3_sc9_takehimdown_comment1)
            mS "Oh dear, are you alright!"
            $ AddChatter (vig3_sc9_takehimdown_comment2)
            pause 0.5
            $ AddChatter (vig3_sc9_takehimdown_comment5)
            invfairnpc2 "{i}My suit!{/i} I knew I should've had these pants hemmed. Damn stylist!"
            "Mills walks away dripping, a few guests follow them    ."
            mS "I guess some folks can't hold their drink."
            $ AddChatter (vig3_sc9_takehimdown_comment6)
            pause 0.5
            $ AddChatter (vig3_sc9_takehimdown_comment7)
            invfairnpc1 "There's one every year." #using invfairnpc1 because it's just labeled as "Inventor's fair guest." works for offscreen npc.
            $ AddChatter (vig3_sc9_takehimdown_comment3)
            "I move on, scanning the gallery. I see Teresa looking in her element, gliding through various groups with a natural grace. Never lingering too long."
            $ AddChatter (vig3_sc9_takehimdown_comment4)
            showgirl "I saw that, you know..."
            show daisy stream think at stream_center with dissolve
            $ reactTarget = "vig3_sc9_daisyreturns"#timestamp 6:46
            show screen streamerCommentary
            "A familiar batch of feathers block my view, Daisy stands in all her showgirl glory. With some added refinement."
            mS "Oh, Daisy was it?"
            $ AddChatter (vig3_sc9_inventorsfair_comment28)
            showgirl "You bet?"
            $ AddChatter (vig3_sc9_inventorsfair_comment29)
            mS "50 Credits at Nova Casino."
            if viewershipHigh == True:
                $ AddChatter (vig3_sc9_inventorsfair_comment30)
            showgirl "What a terrible deal. That barely gets you a few good spins, not even a buy-in at a low ball table."
            mS "I guess the only big win anyone is getting is at the bar."
            "We both laugh, a genuine laugh."
            show daisy stream neutral
            $ AddChatter (vig3_sc9_inventorsfair_comment31)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter (vig3_sc9_inventorsfair_comment32)
            showgirl "Also don't worry. I'm not going to tell. Honestly, they deserved worse."
            "I feel myself get nervous."
            mS "Much appreciated."
            mS "And sorry for earlier, in Akar, I've been on edge."
            showgirl "Don't sweat it. If you weren't going to shoot me, I was. I hate that script."
            mS "Costume is great though."
            $ AddChatter (vig3_sc9_inventorsfair_comment33)
            pause 0.5
            $ AddChatter (vig3_sc9_inventorsfair_comment34)
            showgirl "Why you flatter me. It is one of my favourite parts."
            "Daisy sways in front of me to show me the movement of her feathers."
            mS "Fabulous. Truly."
            "She has such a sweet smile."
            if viewershipHigh == True:
                $ AddChatter (vig3_sc9_inventorsfair_comment35)
                pause 0.5
                $ AddChatter (vig3_sc9_inventorsfair_comment36)
                pause 0.5
            $ AddChatter (vig3_sc9_inventorsfair_comment37)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter (vig3_sc9_inventorsfair_comment38)
    
    #Have an extra scene with Daisy, change it to fit which you decided.
    show daisy stream think
    showgirl "Well, I should be off then."
    mS "Actually, wait! Daisy."
    #show daisy stream shock
    showgirl "Oh? What is it?"
    hide screen streamerCommentary
    menu: 
        "Maybe Daisy can help us?"
        "Ask her about the missing parts.":
            $ csEngagement += 1 #Logic: coriolis likes the directness
            $ setEngagement()
            mS "You seem like you know your way around here."
            show daisy stream neutral
            showgirl "A girl has her ways."
            mS "I'm looking for something that was taken, wouldn't happen to know where I could find it?"
            $ AddChatter (vig3_sc9_parts_comment1)
            showgirl "Ah. The Hounds I take it?"
            $ AddChatter (vig3_sc9_parts_comment2)
            mS "Unfortunately."
            showgirl "How about we get a drink and chat."
            $ AddChatter (vig3_sc9_parts_comment3)
            mS "I really don't—"
            $ AddChatter (vig3_sc9_parts_comment4)
            "She sidles next to me and holds my arm."
            showgirl "Shall we?"
            "I nod and head over."
        "Invite her to the bar.":
            $ kcEngagement += 1 #Logic: kitcat is here for the flirting
            $ setEngagement()
            mS "I'm sure you're busy. But care to have a drink with me?"
            $ AddChatter (vig3_sc9_bar_comment1)
            show daisy stream neutral
            showgirl "You mean pilfer Reynar's open bar?"
            $ AddChatter (vig3_sc9_bar_comment2)
            mS "Couldn't have said it better myself."
            "She goes for my arm then pauses."
            $ AddChatter (vig3_sc9_bar_comment3)
            showgirl "Just a drink don't expect anything."
            mS "I wouldn't dare."
            $ AddChatter (vig3_sc9_bar_comment4)
            "She sidles next to me and holds my arm."
            mS "Shall we?"
            "She nods and we head over."
        "Mumble incoherently.":
            $ pdEngagement += 2 #Logic: pickledDragons finds it outrageous (and fun) that you intentionally choose the "fail" option
            $ setEngagement()
            mS "Well...I...you see..."
            $ AddChatter (vig3_sc9_flustered_comment1)
            "Makers she's so pretty."
            $ AddChatter (vig3_sc9_flustered_comment2)
            show daisy stream neutral
            "She luckily giggles."
            showgirl "Is the great Captain of the Oakley getting flustered?"
            $ AddChatter (vig3_sc9_flustered_comment3)
            mS "Happens from time to time."
            "She sidles next to me and holds my arm."
            $ AddChatter (vig3_sc9_flustered_comment4)
            showgirl "Come with me Captain. Let's get you a drink."
            mS "Um yeah, haha, sure."

    "We make our way to Reynar's open bar."
    $ AddChatter (vig3_sc9_inventorsfair_comment39)
    "With most of the action happening on the floor, we have a lot of room to talk."
    "We talk for a lot longer than we should."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc9_inventorsfair_comment40)
    mS "So if someone would want to maybe go around and check out some of the off the floor pieces..."
    mS "Could she?"
    "This Vira Brandy is a lot stronger than I expected. Turns out they've been keeping all the legit stuff on this side of the Vineyard."
    "Daisy's face has adopted an adorable red hue."
    show daisy stream think
    showgirl "Not without attracting some serious attention."
    "She takes a sip from her glass."
    showgirl "What's so important anyway?"
    mS "A range extender..."
    showgirl "You're joking—"
    mS "Wish I was, but the fate of the galaxy depends on it!"
    show daisy stream neutral
    $ AddChatter (vig3_sc9_inventorsfair_comment41)
    showgirl "Sounds like a big extender."
    "I let out a heavy sigh. Letting the joke fly over my head."
    showgirl "Guests aren't able to explore off-floor pieces."
    $ AddChatter (vig3_sc9_inventorsfair_comment42)
    showgirl "Unless they waited for a big presentation and had someone to help them through."
    mS "When's the next one scheduled?"
    $ AddChatter (vig3_sc9_inventorsfair_comment43)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc9_inventorsfair_comment44)
    show daisy stream think
    showgirl "The BigCorp showcase should be happening in fifteen minutes. Hear you'll get a killer view from the door near that vase over there."
    "She points to a large ornate vase at the side of the ballroom. There's an unmanned service door just behind it." 
    "I'm still trying to process what she just said."
    mS "BigCorp is here?"
    show daisy stream neutral
    showgirl "Oh yeah, big reveal!"
    showgirl "Heard Reynar is hedging new investments and property in the Outposts, hard to expand without greasing some palms."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc9_inventorsfair_comment45)
    "Just then I hear an annoyingly recognizeable voice."
    show daisy stream upset
    invfairnpc2 "Is that Akar's own Daisy."
    "Daisy's eyes widen. She forces a smile."
    $ AddChatter (vig3_sc9_inventorsfair_comment46)
    show daisy stream neutral
    showgirl "Mills! Look at you. You clean up... well."
    "I almost choke on my drink."
    invfairnpc2 "Nice to see you still have your humor."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc9_inventorsfair_comment47)
    invfairnpc2 "Reynar has you entertaining tonight?"
    showgirl "Of course, as you can tell."
    "Mills looks me up and down."
    invfairnpc2 "Right..."
    invfairnpc2 "How about you give some other people your attention."
    $ AddChatter (vig3_sc9_inventorsfair_comment48)
    "I can already tell how this is gonna go."
    "Mills is moving closer to Daisy."
    show daisy stream think
    showgirl "No need to be hasty, I'll get to everyone."
    "Mills puts himself in between us, their back turned to me."
    "Intervening here is risky, but I can't just leave Daisy out to dry."
    menu: 
        "Do you intervene?"
        "Stand up and get in his face.":
            $ vig3_outlaw += 1
            $ csEngagement -= 1
            $ pdEngagement += 1
            $ kcEngagement += 2 #Logic: kitcat likes how loud this defense of Daisy is.
            $ setEngagement()
            $ vig3_daisyApproval = False
            $ vig3_daisyChoice = 1
            $ reactTarget = "vig3_sc9_daisybar"#timestamp 6:48
            "I rise to my full height."
            mS "She said she'll get back to you later."
            $ AddChatter (vig3_sc9_standup_comment1)
            pause 0.5
            $ AddChatter (vig3_sc9_standup_comment2)
            show daisy stream neutral
            "They turn to me."
            invfairnpc2 "Oh? and what are you?"
            mS "I'm about to be your next big problem."
            show screen streamerCommentary
            "I move forward to tower over him, and he takes a step back."
            show daisy stream think
            showgirl "Moze..."
            invfairnpc2 "You don't want to do this."
            $ AddChatter (vig3_sc9_standup_comment3)
            mS "Try me."
            "Before anything can happen, Ryo emerges from the ether."
            vyattend "Is there a problem?"
            "Shit."
            show daisy stream neutral
            showgirl "No, Ryo, of course not. I was just about to make my rounds."
            $ AddChatter (vig3_sc9_standup_comment4)
            "Ryo seperates me from Mills who he ushers away. Daisy moves to greet the rest of the guests."
            "She turns to me."
            showgirl "I'll see you around, Moze."
            showgirl "Be sure to check out that view."
            $ AddChatter (vig3_sc9_standup_comment5)
            hide daisy with dissolve
            "I finish my drink and find the rest of my crew."
            "I see Reynar up on his balcony."
            show reynar stream angry at stream_center with dissolve
            "He does not look happy."
        "Put your blaster to his side.":
            $ vig3_outlaw += 1
            $ csEngagement -= 1 #Logic: very violent for cs
            $ pdEngagement += 2 #Logic: likes the slickness of this
            $ kcEngagement += 1 #Logic: likes helping out Daisy
            $ setEngagement()
            $ vig3_daisyApproval = True
            $ vig3_daisyChoice = 2
            $ reactTarget = "vig3_sc9_daisybar"#timestamp 6:48
            play audio "gunCock.wav" volume 1.5
            "I grab my blaster and push it into Mills' side."
            "Out of view from the prying eyes."
            show daisy stream shock
            invfairnpc2 "You little—"
            $ AddChatter (vig3_sc9_standup_comment1)
            mS "Now let's not make a scene."
            mS "The lady said she'll get to you soon. Right?"
            show screen streamerCommentary
            show daisy stream neutral
            "The initial shock falls from her face and is replaced with a devilish smile."
            $ AddChatter (vig3_sc9_standup_comment6)
            showgirl "Right..."
            invfairnpc2 "What do you want then?"
            mS "I want you to take your drink and walk away."
            $ AddChatter (vig3_sc9_standup_comment3)
            mS "And if you so much as look at her the wrong way."
            mS "Remember that I'm around."
            mS "Clear?"
            $ AddChatter (vig3_sc9_standup_comment5)
            invfairnpc2 "Crystal."
            "Mills orders a drink as calmly as possible before leaving us."
            showgirl "Why thank you, Captain."
            mS "Anytime."
            showgirl "I should be going, but do check out the view."
            showgirl "And the service door while you're at it."
            "Daisy gives me a wink and slowly leaves the bar to greet the rest of the guests."
            $ AddChatter (vig3_sc9_standup_comment4)
            "So many feathers."
            hide daisy with dissolve
            "I finish my drink and find the rest of my crew."
            "I see Reynar up on his balcony."
            show reynar stream gatsby at stream_center with dissolve
            "He has a sly smile on his face."
        "Try to catch someone else's attention.":
            $ csEngagement += 1 #Logic: As mentioned several times, cs appreciates a "sacrifice" for the greater good
            $ kcEngagement -= 1 #Logic: kitcat wants you to stand up for Daisy, pickledDragons doesn't like you being passive
            $ pdEngagement -= 1
            $ setEngagement()
            $ vig3_daisyApproval = False
            $ vig3_daisyChoice = 3
            $ reactTarget = "vig3_sc9_daisybar"#timestamp 6:48
            "I can't do anything right now."
            "There's too much on the line."
            $ AddChatter (vig3_sc9_attention_comment1)
            invfairnpc2 "So Daisy, shall I steal you away?"
            show screen streamerCommentary
            show daisy stream neutral
            "He leans closer."
            $ AddChatter (vig3_sc9_attention_comment2)
            showgirl "I'm with a guest at the moment."
            invfairnpc2 "There are better people for your time."
            "I look around the room to catch anyone's eye."
            $ AddChatter (vig3_sc9_attention_comment3)
            "Even the droids aren't giving me the slightest glance."
            mS "Look—"
            invfairnpc2 "Let's stop playing these games shall we?"
            $ AddChatter (vig3_sc9_attention_comment4)
            pause 0.5
            $ AddChatter (vig3_sc9_attention_comment5)
            show daisy stream upset
            showgirl "A fabulous idea."
            "In a quick motion Daisy grabs a blade from her corset and stabs it betweeen Mills'fingers."
            invfairnpc2 "I—"
            showgirl "Shall I see you later then."
            $ AddChatter (vig3_sc9_attention_comment6)
            "Mills swallows hard."
            invfairnpc2 "Of course."
            "When Mills leaves, Daisy composes herself with a deep breath."
            showgirl "Thank you for the drink. Excuse me, please."
            $ AddChatter (vig3_sc9_attention_comment7)
            "Daisy slowly leaves the bar to greet the rest of the guests."
            hide daisy with dissolve
            $ AddChatter (vig3_sc9_attention_comment8)
            "I finish my drink and find the rest of my crew."
            "I see Reynar up on his balcony."
            show reynar stream neutral at stream_center with dissolve #can put in new model when we have it
            "Looking disappointed."
    hide reynar with dissolve
    hide screen streamerCommentary
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    show rec stream formal neutral at stream_center with dissolve
    "I quickly catch everyone up about the info I got from Daisy."
    pS "We're real in it now."
    enS "I fear we didn't get much distance after all."
    recS "What happens if they catch you?"
    if viewershipHigh == True:
        $ AddChatter (vig3_sc9_inventorsfair_comment49)
    enS "Oh, I assume chained to a factory for the rest of our natural lives."
    pS "I'd rather a bullet to the eyes."
    mS "We need to find MAC and get the hell out of here."
    show rec stream formal thinking
    recS "If we can trust your friend Daisy, we might find whatever storeroom they put him in, hell maybe even your range extender on the way."
    mS "Makers willing."
    $ AddChatter (vig3_sc9_inventorsfair_comment50)
    mS "Okay, once the presentation starts then we'll head out."
    hide jennica with dissolve
    hide teresa with dissolve
    hide rec with dissolve
    "We go back to the floor. And I try to figure out how many enforcers there are."
    "Are they all guests, maybe some waiting in the wings?"
    "Do they already have MAC and are just waiting for this presentation before heading off?"
    stop music fadeout 4.0
    stop backAudio fadeout 2.0
    invfairannounce "And now a feature presentation from the Big Corp laboratories."
    $ AddChatter (vig3_sc9_inventorsfair_comment51)
    "The music dies down as a platform rises from the center of the gallery. Spotlights alight on it and people halfheartedly turn to the center."
    show bcrep stream at stream_right with dissolve
    "A finely dressed man walks up to the platform and wheels in something covered by a blanket."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc9_inventorsfair_comment52)
    bcrep "Ladies and Gentlemen, honorable guests of the Vineyard." 
    bcrep "We at BigCorp would like to thank Reynar for this opportunity to present our new and exciting venture."
    $ AddChatter (vig3_sc9_inventorsfair_comment53)
    bcrep "Now this is just a protoype, but it has immense potential."
    $ AddChatter (vig3_sc9_inventorsfair_comment54)
    pause 0.5
    $ AddChatter (vig3_sc9_inventorsfair_comment55)
    "The crowd murmurs at the word prototype. I move closer to the corner of the room, ready to make an escape."
    "Until the representative pulls off the sheet revealing their newest invention: a small purple robot with an unmistakable leaf over his head."
    show mac stream neutral at stream_center_mac with dissolve
    $ AddChatter (vig3_sc9_inventorsfair_comment56)
    bcrep "M.A.C. is our revolutionary new bot that we are outfitting with fully adaptable AI technology."
    $ AddChatter (vig3_sc9_inventorsfair_comment57)
    bcrep "Programming so advanced it's nothing short of human-like."
    $ AddChatter (vig3_sc9_inventorsfair_comment58)
    pause 0.5 
    $ AddChatter (vig3_sc9_inventorsfair_comment59)
    "His little eyes lock on mine."
    $ AddChatter (vig3_sc9_inventorsfair_comment60)
    bcrep "As I said, this is just our prototype as we continue to look for new ways to truly develop our AI databases. But our scientists are hard at work to..."
    "Will this nightmare ever end?"
    $ AddChatter (vig3_sc9_inventorsfair_comment61)
    "They have him."
    $ AddChatter (vig3_sc9_inventorsfair_comment62)
    bcrep "Now a demonstration. Say hi, M.A.C!"
    "There's a small pause."
    play audio "macNeutral.wav" volume 1.0
    macS "Hi, MAC..."
    $ AddChatter (vig3_sc9_inventorsfair_comment63)
    hide bcrep stream with dissolve
    "The room chuckles as the representative keeps talking. I look over at the crew who are frozen, unsure of how to proceed." 
    $ AddChatter (vig3_sc9_inventorsfair_comment64)
    pause 0.5
    $ AddChatter (vig3_sc9_inventorsfair_comment65)
    "Jennica begins to move up to me, but stops and turns white as a ghost."
    $ AddChatter (vig3_sc9_inventorsfair_comment66)
    pause 0.5
    $ AddChatter (vig3_sc9_inventorsfair_comment67)
    amaS "Now ain't this a stroke of bad luck."
    $ AddChatter (vig3_sc9_inventorsfair_comment68)
    hide mac with dissolve
    "I turn to the voice and am certain I've fully lost it."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc9_inventorsfair_comment69)
        pause 0.5
        $ AddChatter (vig3_sc9_inventorsfair_comment70) 
    "Because there she is in a full ballgown, staring at me with that same condescending look I've always known."
    show ama stream formal neutral at stream_center with Dissolve(2.0)
    $ reactTarget = "vig3_sc9_amasurprise"#timestamp 6:50
    show screen streamerCommentary
    $ AddChatter (vig3_sc9_inventorsfair_comment71)
    pause 0.5
    $ AddChatter (vig3_sc9_inventorsfair_comment72)
    pause 0.5
    $ AddChatter (vig3_sc9_inventorsfair_comment73)   
    "But this time, it doesn't go away." 
    "Ama smiles."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc9_inventorsfair_comment74)
        pause 0.5
    $ AddChatter (vig3_sc9_inventorsfair_comment75)  
    "I'm frozen in place."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc9_inventorsfair_comment76) 
    "The Vineyard falls away around me."
    hide screen streamerCommentary
    amaS "Hello, Mozely."
    hide ama with dissolve
    $ viewCheck7 = viewCount
    jump vig3_break 
    #move to mid vig break - if we have time to make it...

label vig3_sc10():
    $ narrator = alt_narrator
    $ macroChoice = False
    show bg black at topleft onlayer background with dissolve
    hide inventorsfairgallery_stream
    play audio "lazerFlashback.wav" volume 4.0
    "I flinch as a shot rings outs, echoing in my ears."
    $ AddChatter (vig3_sc10_memory_comment1)
    "My heart pounds hard in my chest."
    "Ama takes the blaster away from me."
    # Ext. Akar - A Decade Ago 
    show ama stream young at stream_center with dissolve
    amaS "Kid, if you're gonna jump everytime someone shoots at you, they'll be playing target practice with your head."
    mS "I'm trying."
    #show ama stream upset
    amaS "You're scared."
    mS "I'm not scared. I'm a Snakehawk!"
    $ AddChatter (vig3_sc10_memory_comment2)
    amaS "Barely."
    "What does she know? I am a Snakehawk."
    "A better one than that stupid Matticus at least."
    $ AddChatter (vig3_sc10_memory_comment3)
    mS "Let me go again!"
    if viewershipHigh == True:
        $ AddChatter (vig3_sc10_memory_comment4)
        pause 0.5
        $ AddChatter (vig3_sc10_memory_comment5)
    show ama stream young
    amaS "Please..."
    mS "Let me prove myself."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc10_memory_comment6)
    amaS "All you've proven is that you're a liability."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc10_memory_comment7)
        pause 0.5
        $ AddChatter (vig3_sc10_memory_comment8)
    mS "Oh yeah, like Jenn is any better."
    show ama stream upset
    amaS "She can fire a blaster without flinching."
    "I feel tears well up in my eyes."
    mS "You don't know anything about me!"
    amaS "We're done here."
    #show ama stream gun
    "Ama raises the blaster and points it at me. My body freezes."
    #"{b}BANG{/b}!"
    play audio "stunLazer.wav" volume 1.4 #should have a stunLazer flashback
    if viewershipHigh == True:
        $ AddChatter (vig3_sc10_memory_comment9)
    "I move out of the way just as the impact hits my shoulder, a hair's breadth away from my heart."
    "My arm is limp, but there's no blood."
    "She set it to stun."
    show ama stream young
    if viewershipHigh == True:
        $ AddChatter (vig3_sc10_memory_comment10)
    "Ama walks up to me, and turns the blaster, handle pointed at me."
    "The insignia of the Snakehawks branded on it."
    #show ama stream happy
    amaS "Ready to try again?"
    "I get up and take the blaster. I grip the handle it like it's mine. Because it is." 
    "I point it at the target."
    play audio "lazerFlashback.wav" volume 4.0
    "And fire."
    hide ama with dissolve
    jump vig3_sc11

label vig3_sc11():
    show inventorsfairgallery_stream at topleft onlayer background with dissolve
    play music "soundtrack/akar(fair).wav" fadein 2.0
    play backAudio "crowdParty.wav" volume 0.8 fadein 2.0
    #Int. Inventor's Fair. 
    show ama stream formal neutral at stream_center with dissolve
    menu:
        "Ama stands in front of me with a steely gaze."
        "Of course you found us...": #Flirt
            $ kcEngagement += 1 #Logic: I don't think these choices are so intense that they would affect everyone. Just one viwer likes one of the choices a bit more
            mS "Of course you found us..."
            $ AddChatter (vig3_sc11_ofcourse_comment1)
            mS "I shouldn't have expected less from the great Deadeye."
            show ama stream formal smug
            amaS "You flatter me."
            amaS "Gotta say getting into an event like this is impressive."
            amaS "You look... well."
            $ AddChatter (vig3_sc11_ofcourse_comment2)
        "Impossible.":
            $ csEngagement += 1
            mS "Impossible."
            mS "How could you have possibly found us?"
            show ama stream formal smug
            $ AddChatter (vig3_sc11_impossible_comment1)
            amaS "You think so little of me."
            amaS "Thought that stunt on Gibian V was going to keep me away?"
            $ AddChatter (vig3_sc11_impossible_comment2)
            amaS "How's Sallent doing?"
        "I see we're still playing the lapdog?":
            $ pdEngagement += 1
            mS "Still playing the obedient lapdog, I see?"
            mS "Money must be good."
            show ama stream formal angry
            $ AddChatter (vig3_sc11_lapdog_comment1)
            amaS "Even now you're still that arrogant little girl."
            amaS "How has playing the hero been? Finally found that purpose you've been missing?"
            $ AddChatter (vig3_sc11_lapdog_comment2)
    $ setEngagement()
    "Her tone is playful but there's no mistaking that her rifle is folded behind her."
    "BigCorp's presentation continues, and I hope that the crew has taken this as a moment to leave."
    "It's up to Resa and Jenn now."
    show ama stream formal neutral
    amaS "So tell me how is that little crew of yours, the Willow?"
    mS "The Oakley."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc11_fairint_comment1)
    amaS "Right, right, quaint."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc11_fairint_comment2)
    amaS "So let me cut to it: you give me what I want and I won't gut your crew and make you watch."
    $ AddChatter (vig3_sc11_fairint_comment3)
    "I look up at the platform."
    $ AddChatter (vig3_sc11_fairint_comment4)
    "I could laugh."
    "That smart little devil."
    mS "I don't know what you mean, Ama. Left something behind have you?"
    $ AddChatter (vig3_sc11_fairint_comment5)
    amaS "Oh, we're playing dumb are we? The droid Mozely, give me the droid."
    $ reactTarget = "vig3_sc11_amabacksass"#timestamp 7:10
    menu: 
        "Ama doesn't have MAC, we can use this."
        "Why don't you just enjoy the party?": #Flirt
            $ csEngagement += 1 #Logic: same as previous menu options
            mS "Ama, please, it's a celebration, have a drink."
            mS "All this stress will give you wrinkles."
            $ AddChatter (vig3_sc11_party_comment1)
            show screen streamerCommentary
            show ama stream formal smug
            "A smile forms on her face, anger mixed with something else."
            amaS "You little shit..."
            $ AddChatter (vig3_sc11_party_comment2)
            mS "Now, now, don't make a scene. You're better than that."
        "I don't have the droid you're looking for.":
            $ csEngagement += 1
            mS "I don't have it."
            show ama stream formal smug
            amaS "Are you playing dumb with me?"
            mS "I lost it, he's not with me."
            "Ama furrows her brow."
            amaS "This isn't the time to yank my chain."
            mS "Isn't that BigCorp's job?"
            show screen streamerCommentary
            $ AddChatter (vig3_sc11_droid_comment1)
            pause 0.5
            $ AddChatter (vig3_sc11_droid_comment2)
        "But he's right there on the platform, no?":
            $ pdEngagement += 1 
            mS "Why are you asking me?"
            mS "It's right there isn't it?"
            $ AddChatter (vig3_sc11_platform_comment1)
            show screen streamerCommentary
            "Ama turns to the platform then back at me, unimpressed."
            $ AddChatter (vig3_sc11_platform_comment2)
            show ama stream formal smug
            amaS "Don't quit your day job Moze."
            amaS "I want that droid and I want it now."
    $ setEngagement()
    "Ama stalks towards me, and I know what's coming."
    $ AddChatter (vig3_sc11_fairint_comment6)
    "I move to my blaster hidden in my clothes."#choice here?
    "I'm sorry, Resa."
    hide screen streamerCommentary
    show ama stream formal shocked at stream_left with move
    show reynar stream neutral at stream_right with dissolve
    reynar "Ladies, I hope your evening is going well."
    $ AddChatter (vig3_sc11_fairint_comment7)
    show ama stream formal neutral
    amaS "Reynar."
    $ AddChatter (vig3_sc11_fairint_comment8)
    reynar "Hello, Ama, a pleasure as always."
    reynar "And Moze. I knew you were familiar when I saw you. All grown up I see?"
    $ AddChatter (vig3_sc11_fairint_comment9)
    "I relax my shoulders."
    mS "Reynar, thank you for having us this evening."
    reynar "If only you were invited..."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc11_fairint_comment10)
        pause 0.5
        $ AddChatter (vig3_sc11_fairint_comment11)
    "A pause."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc11_fairint_comment12)
        pause 0.5
        $ AddChatter (vig3_sc11_fairint_comment13)
    "A waiter passes by with a full tray. Reynar grabs a bubbling drink without even looking."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc11_fairint_comment19)
    reynar "I sincerely hope the two of you aren't about to do what I think you are."
    $ AddChatter (vig3_sc11_fairint_comment14)
    pause 0.5
    $ AddChatter (vig3_sc11_fairint_comment15)
    pause 0.5
    $ AddChatter (vig3_sc11_fairint_comment16)
    pause 0.5
    $ AddChatter (vig3_sc11_fairint_comment17)
    pause 0.5
    $ AddChatter (vig3_sc11_fairint_comment18)
    show ama stream formal upset
    amaS "Respectfully this is BigCorp business."
    $ AddChatter (vig3_sc11_fairint_comment20)
    reynar "Is it now? Funny, I don't remember giving them jurisdiction to conduct business in {i}my{/i} Vineyard."
    $ AddChatter (vig3_sc11_fairint_comment21)
    amaS "Consider it a favour. We're removing a known fugitive from the premises."
    reynar "Oh, what a shame that you'll be leaving so soon."
    "I stifle a laugh."
    amaS "Such an incessant queen."
    menu: 
        "Get in the mix."
        "Bold coming from you.": 
            $ deadeyeApproval += 0 #Is this supposed to be a 0? or a 1?
            mS "Bold coming from you."
            show ama stream formal angry
            amaS "Oh? You're speaking now?"
            mS "Hard to get a word in when you love hearing yourself talk."
            $ AddChatter (vig3_sc11_bold_comment1)
            amaS "Haha little chick has grown up!"
            reynar "And with a considerable bite."
            $ AddChatter (vig3_sc11_bold_comment2)
            mS "You don't know the half of it."
            "There is hunger in Ama's eyes."
        "We're not here to cause trouble.":
            mS "We're not here to cause trouble."
            mS "Just a rocky reunion."
            show ama stream formal angry
            amaS "Don't speak for me. Ever."
            $ AddChatter (vig3_sc11_trouble_comment1)
            reynar "With how this is going you should count yourself lucky."
            $ AddChatter (vig3_sc11_trouble_comment2)
    "I am thankful for Reynar's intervention, but even he isn't known for handouts."
    "I also need to keep my eye on the prize."
    mS "Reynar, pardon my intrusion, but I am here because your Hounds stole a piece of {i}my{/i} merchandise."
    reynar "Did they now?"
    if viewershipHigh == True:
        $ AddChatter (vig3_sc11_fairint_comment22)
        pause 0.5
    $ AddChatter (vig3_sc11_fairint_comment23)
    "Ama is visibly upset that I've moved the attention."
    mS "A range extender, a small repair for my ship. I'd like it back."
    $ AddChatter (vig3_sc11_fairint_comment24)
    reynar "Well you can leave your information with Ryo and we'd be happy to oblige you after the festivities."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc11_fairint_comment25)
    show ama stream formal neutral
    "Ama chuckles under her breath."
    mS "I'd like to have this matter resolved as soon as possible."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc11_fairint_comment26)
    reynar "So urgent!"
    reynar "I understand."
    reynar "But first things first."
    "With a snap of his fingers Ryo reemerges."
    reynar "Please take our guests to the east balcony. They could use the privacy."
    $ AddChatter (vig3_sc11_fairint_comment27)
    show ama stream formal smug
    "A nasty smile creeps on Ama's face."
    $ AddChatter (vig3_sc11_fairint_comment28)
    "I can feel the eyes around me."
    "The presentation is over and some attendents are ushering the BigCorp rep away from the crowd."
    $ AddChatter (vig3_sc11_fairint_comment29)
    pause 0.5
    $ AddChatter (vig3_sc11_fairint_comment30)
    reynar "It was wonderful to see you both."
    "Reynar gives a forced hug and double cheek kiss to Ama. Then moves to me."
    "He offers the same gesture then whispers quietly."
    reynar "I do hope to see you later for the toast."
    "He slips something into my back pocket."
    $ AddChatter (vig3_sc11_fairint_comment31)
    "Ryo ushers us both in the direction of the east balcony."
    "Ama walks in front of me, and I watch as the slit in her dress reveals something cold and metallic."
    stop music fadeout 2.0
    stop backAudio fadeout 3.0
    hide ama with dissolve
    hide reynar with dissolve
    jump vig3_sc12

label vig3_sc12():
    #Ext. Vineyard Balcony
    $ viewCheck8 = viewCount
    show vybalcony_stream at topleft onlayer background with dissolve
    hide inventorsfairgallery_stream
    "Overlooking the lush chimaeron trees, the east balcony is as ornate as it is private."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc12_balcony_comment1)
    "The noise of the Fair cuts as the large doors close on the balcony."
    "Clearly this space is meant for more quiet business."
    "In the distance, I see Akar, lights gleaming like little stars."
    "It's so far away..."
    play music "soundtrack/decisionTime.wav"
    show ama stream formal neutral at stream_left with dissolve
    show bcrep stream at stream_center with dissolve
    bcrep "Absolute garbage!"
    $ AddChatter (vig3_sc12_balcony_comment2)
    play audio "dropGun.wav" volume 1.0
    "I hear the sound of metal on the ground, a small pained whine."
    play audio "macHum.wav" volume 0.6
    show mac stream neutral at stream_right_mac with dissolve
    "I press down my white hot anger."
    bcrep "What did you say to him? What did you do?"
    "He's talking to Ama, who arrogantly has her back to me."
    bcrep "I swear to the Makers if you screwed up again!"
    "The representative hasn't noticed me yet."
    play audio "grunt.wav" volume 2.8
    show bcrep stream at stream_left5 with MoveTransition(0.2)
    "And soon has more pressing matters as he strains against Ama's grip on his throat."
    $ AddChatter (vig3_sc12_balcony_comment3)
    $ reactTarget = "vig3_sc12_amachoke"#timestamp 7:15
    show screen streamerCommentary
    "I forgot how fast Ama was. How deadly."
    $ AddChatter (vig3_sc12_balcony_comment4)
    show ama stream formal upset
    amaS "I suggest you watch that mouth of yours."
    bcrep "My... bosses... sign... your checks."
    $ AddChatter (vig3_sc12_balcony_comment5)
    amaS "Yes, {i}they{/i} do."
    "Her grip tightens."
    "I see MAC on the ground just past them, he's still."
    show ama stream formal angry
    hide screen streamerCommentary
    menu: 
        "I have to do something."
        "Help the representative.":
            $ macPeace += 3
            $ macHope += 2
            $ kcEngagement += 1 #Logic: kitcat likes intervening in the murder, Coriolis really likes it 
            $ csEngagement += 3
            $ pdEngagement -= 2 #Logic: pickledDragons thinks he should die
            $ setEngagement()
            $ vig3_bcRepSaved = True
            "When MAC's eyes lock on mine, he perks up."
            "I put my finger to my lips."
            $ AddChatter (vig3_sc12_help_comment1)
            pause 0.5
            $ AddChatter (vig3_sc12_help_comment2)
            bcrep "P-lease..."
            mS "That's enough Ama."
            $ AddChatter (vig3_sc12_help_comment3)
            show ama stream formal smug
            amaS "You're really all over the place, Mozely."
            amaS "Didn't think you had heart for BigCorp."
            $ AddChatter (vig3_sc12_help_comment4)
            mS "You know I don't."
            mS "But you're going too far."
            $ AddChatter (vig3_sc12_help_comment5)
            "When Ama lets him go, he spills to the ground, tears in his eyes."
            show bcrep stream at stream_center with move
            menu: 
                "Say something."
                "You're rough as always.": 
                    mS "Just like you to be a bit too rough."
                    amaS "Just handling business."
                    mS "Clearly haven't lost your charm."
                    show ama stream formal neutral
                    $ AddChatter (vig3_sc12_help_comment6)
                    pause 0.5
                    $ AddChatter (vig3_sc12_help_comment7)
                    amaS "Don't worry I'll get to you later..."
                "That was unnecessary.":
                    mS "That was unnecessary."
                    $ AddChatter (vig3_sc12_help_comment6)
                    pause 0.5
                    $ AddChatter (vig3_sc12_help_comment7)
                    amaS "You should just let me handle business."
                    amaS "But don't worry."
                    show ama stream formal neutral
                    amaS "I'll get to you soon."
            "The representative coughs and steadies himself."
            bcrep "Who's this? One of Reynar's goons?"
            amaS "You academics are so far up your own asses."
            "He takes a moment and scan me."
            "His eyes widen as they stand to look at me."
            $ AddChatter (vig3_sc12_help_comment8)
            "They laugh in disbelief."
            bcrep "Incredible!"
            if viewershipHigh == True:
                $ AddChatter (vig3_sc12_help_comment9)
            bcrep "Absolutely incredible!"
            if viewershipHigh == True:
                $ AddChatter (vig3_sc12_help_comment10)
                pause 0.5
            $ AddChatter (vig3_sc12_help_comment11)
            bcrep "Do you have any idea how terrible this has been?"
            bcrep "The shit storm {i}you{/i} caused!"
            mS "Realy polite for someone who saved your life."
            bcrep "Please, that barely paid me back for the trouble you caused."
            "He walks up to MAC."
            bcrep "But now that we have you I have no use for this {i}stupid piece of junk!{/i}"
            if viewershipHigh == True:
                $ AddChatter (vig3_sc12_help_comment12)
            "They're moving to kick MAC off the balcony."
            menu: 
                "How do you stop him?"
                "Fire your blaster.":
                    $ pdEngagement += 1 #Logic: you get pd back a bit for this
                    $ kcEngagement += 2 #Logic: kitcat would say you have to defend MAC
                    $ csEngagement -= 1 #Logic: coriolis would prefer you rush them instead of try to shoot
                    $ setEngagement()
                    $ macViolence += 1
                    $ macPessimism += 1
                    "Absolutely not!"
                    $ AddChatter (vig3_sc12_blaster_comment1)
                    "I reach for my blaster on instinct."
                    mS "Hands off him!"
                    $ AddChatter (vig3_sc12_blaster_comment2)
                    show ama stream formal gun
                    play audio "gunCock.wav" volume 2.5
                    "Then I hear Ama's rifle cock and I freeze on reflex."
                    $ AddChatter (vig3_sc12_blaster_comment3)
                    pause 0.5
                    $ AddChatter (vig3_sc12_blaster_comment4)
                    amaS "Not likely Moze."
                    $ AddChatter (vig3_sc12_blaster_comment5)
                    pause 0.5
                    $ AddChatter (vig3_sc12_blaster_comment6)
                    "Ama stands with rifle in hand aimed at me."
                    "The commotion is enough to stop the rep in his tracks."
                "Rush him down.":
                    $ pdEngagement += 1 #Logic: similar as the above, but kitcat finds it less impactful of a defense while Coriolis actually does approve somewhat
                    $ kcEngagement += 1
                    $ csEngagement += 1
                    $ setEngagement()
                    $ macViolence += 1
                    mS "No!"
                    $ AddChatter (vig3_sc12_rush_comment1)
                    "I rush the rep ready to tackle him to the ground."
                    $ AddChatter (vig3_sc12_rush_comment2)
                    show ama stream formal gun
                    play audio "gunCock.wav" volume 2.5
                    "Then I hear Ama's rifle cock and I stop dead on reflex."
                    $ AddChatter (vig3_sc12_rush_comment3)
                    amaS "Not likely, Mozely."
                    $ AddChatter (vig3_sc12_rush_comment4)
                    pause 0.5
                    $ AddChatter (vig3_sc12_rush_comment5)
                    "I freeze and turn to her slowly."
                    "Ama stands with her rifle in hand aimed at me."
                    "The commotion is enough to stop the rep in his tracks."
                "You can't react fast enough.":
                    $ csEngagement += 1 #Logic: Coriolis likes you not going aggressive
                    $ kcEngagement -= 2 #Logic: kitcat is appalled you didn't do anything; pickledDragons is mixed - it's inaction but also a moment of choosing failure which they find interesting
                    $ setEngagement()
                    "This is crazy."
                    $ AddChatter (vig3_sc12_freeze_comment1)
                    "All of this, we are so over our heads."
                    $ AddChatter (vig3_sc12_freeze_comment2)
                    "I can't will my body to move"
                    $ AddChatter (vig3_sc12_freeze_comment3)
                    bcrep "...JUNK!"
                    "Just as the rep attempts to land his kick, he's stopped by the sound of Ama's rifle cocking."
                    show ama stream formal gun
                    amaS "Hold it!"
                    $ AddChatter (vig3_sc12_freeze_comment4)
                    play audio "gunCock.wav" volume 2.5
                    "Then I hear Ama's rifle cock and I freeze on reflex."
            "The rep backs away."
            amaS "Save the tantrum, kid."
            $ AddChatter (vig3_sc12_balcony_comment6)
            amaS "Now Mozely, we're gonna be nice an cooperative."
            amaS "So first thing, blaster on the ground."
            $ AddChatter (vig3_sc12_balcony_comment7)
            "There's nothing I can do. I know I have to let it go."
            play audio "dropGun.wav" volume 1.0
            "I toss it away from me."
            $ AddChatter (vig3_sc12_balcony_comment8)
            amaS "I thought you'd have gotten over freezing up like that by now."
            play audio "macSad.wav" volume 1.2
            macS "Captain..."
            "The three of us freeze and turn to MAC."
            $ reactTarget = "vig3_sc12_amafindsout"#timestamp 7:18
            show screen streamerCommentary
            show ama stream formal smug
            amaS "That's it, isn't it?"
            $ AddChatter (vig3_sc12_balcony_comment9)
            amaS "All that struggle. All that runnin'..."            
            $ AddChatter (vig3_sc12_balcony_comment10)
            pause 0.5
            $ AddChatter (vig3_sc12_balcony_comment11)
            amaS "Was it worth it?"
            "I look at MAC and then Ama."
            "Before I even realize it, I start walking towards her."
            show ama stream formal upset
            amaS "Woah now, stay right there."
            hide screen streamerCommentary
            "I take another step."
            amaS "I'm warnin' ya, Mozely."
            "She's hesitating."
            "Another step."
            show ama stream formal gun
            amaS "You're gonna make me shoot you?"
            "Until I'm close enough."
            "I pause."
            mS "Yeah."
            $ AddChatter (vig3_sc12_balcony_comment12)
            play audio "lazer.wav" volume 5.0
            "I grab the gun as it fires inches from my face."
            "I try to pry it from her hands but she's as strong as I remember."
            $ AddChatter (vig3_sc12_balcony_comment13)
            amaS "You little shit!"
            "I struggle against her strength as we pull the rifle back and forth."
            $ AddChatter (vig3_sc12_balcony_comment14)
            pause 0.5
            $ AddChatter (vig3_sc12_balcony_comment15)
            #"{b}BANG!{/b}"
            play audio "lazer.wav" volume 4.0
            "A chunk of the rail explodes out into the open air."
            play audio "macPester.wav" volume 1.5
            macS "{i}Stop it!{/i}"
            $ AddChatter (vig3_sc12_balcony_comment16)
            pause 0.5
            $ AddChatter (vig3_sc12_balcony_comment17)
            "Ama and I hit a stalemate as we turn to MAC."
            $ AddChatter (vig3_sc12_balcony_comment18)
            "The rep is white as a ghost, back to the rails as if he'll throw himself off."
            "And there's MAC with my blaster in his hand."
            "Gripping the handle like it's his own."

            if macViolence >= macPeace and macPessimism >= macHope:
                $ pdEngagement += 3 #Logic: pickledDragons likes the outlaw version of MAC
                $ csEngagement -= 2 #Logic: coriolis is freaked out by MAC here. Kitcat doesn't like what MAC is learning, but likes that he's standing up for himself.
                $ kcEngagement += 1
                $ setEngagement()
                $ vig3_macShootAma = True
                $ vig3_macAlign = "ViolentPessimism"
                $ vig3_outlaw += 1
                play audio "lazer.wav" volume 5.0
                "He fires the blaster in-between us, it hits the wall with a definitive crack."
                bcrep "Makers!" 
                "Ama just stares at MAC who is resolute in his stance."
                show ama stream formal smug
                amaS "You gonna do something with that baby blaster?"
                $ AddChatter (vig3_sc12_macshoots_comment1)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment2)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment3)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment4)
                amaS "If you're gonna shoot, you better shoot straight."
                play audio "macNeutral.wav" volume 1.2
                macS "My programming ensures perfect accuracy. Shall I demonstrate?" 
                $ AddChatter (vig3_sc12_macshoots_comment5)
                bcrep "Programming..."
                $ AddChatter (vig3_sc12_macshoots_comment6)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment7)
                amaS "Well then, let's—"
                $ AddChatter (vig3_sc12_macshoots_comment8)
                show ama stream formal shocked
                play audio "lazer.wav" volume 5.0
                "The blaster rings out and before I can react Ama is on the ground clutching her side."
                amaS "Bastard!" 
                macS "I have been provoked and damaged, I will defend myself."
                $ AddChatter (vig3_sc12_macshoots_comment9)
                macS "I will defend my Captain."
                $ AddChatter (vig3_sc12_macshoots_comment10)
                "The rep is shaking and I almost forget the rifle in my hand."
                "MAC slowly rolls towards me passing Ama without even looking at her."
                show ama stream formal angry
                amaS "You won't get out here you know."
                play audio "macPing.wav" volume 1.2
                macS "Will you stop us. I can remove you if necessary."
                $ AddChatter (vig3_sc12_macshoots_comment11)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment12)
                show ama stream formal shocked
                amaS "I—"
                play audio "macPester.wav" volume 1.2
                macS "We should leave, yes?"
                $ AddChatter (vig3_sc12_balcony_comment22)
                $ reactTarget = "vig3_sc12_macalignment_violencepessimism"#timestamp 7:21
                show screen streamerCommentary
                mS "You got it."
                if viewershipHigh == True:    
                    $ AddChatter (vig3_sc12_balcony_comment23)
                "Without losing my sights on her we head inside."
            elif macViolence >= macPeace and macPessimism < macHope:
                $ pdEngagement += 2 #Logic: similar as above but pd and cs are lessened
                $ csEngagement -= 1
                $ kcEngagement += 2
                $ setEngagement()
                $ vig3_outlaw += 1
                $ vig3_macAlign = "ViolentHope"
                play audio "lazer.wav" volume 5.0
                "He fires the blaster in between us, it hits the wall with a definitive crack."
                bcrep "Makers!" 
                "Ama just stares at MAC who holds the gun steady but with noticeable apprehension."
                show ama stream formal smug
                amaS "You gonna do something with that baby blaster?"
                $ AddChatter (vig3_sc12_macshoots_comment1)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment2)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment3)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment4)
                amaS "If you're gonna shoot, you better shoot straight."
                $ AddChatter (vig3_sc12_macshoots_comment5)
                play audio "macNeutral.wav" volume 1.2
                macS "My programming ensures perfect accuracy when required." 
                $ AddChatter (vig3_sc12_macshoots_comment6)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment7)
                bcrep "Programming..." 
                amaS "Well then, let's see it."
                $ AddChatter (vig3_sc12_macshoots_comment8)
                macS "I know you don't want BigCorp to succeed anymore than we do."
                amaS "I don't know, I'm being paid quite well."
                show ama stream formal shocked
                play audio "lazer.wav" volume 5.0
                "Another fire from the blaster, right in front of Ama's face."
                macS "Then I'll shoot you if I must."
                $ AddChatter (vig3_sc12_macshoots_comment9)
                amaS "You little bastard."
                $ AddChatter (vig3_sc12_macshoots_comment10)
                "This is my chance."
                "With a proper shove I get Ama off balance and aim her rifle at her."
                mS "MAC let's go!" 
                play audio "macAffirmative.wav" volume 1.2
                macS "Yes Captain!"
                "MAC wheels towards me and stops at Ama."
                $ AddChatter (vig3_sc12_macshoots_comment11)
                macS "Captain says you're one of the best."
                $ AddChatter (vig3_sc12_macshoots_comment12)
                macS "My records show a long list of... accomplishments perpetrated by you."
                amaS "And what about it?"
                macS "I thought you'd be better than this."
                $ AddChatter (vig3_sc12_balcony_comment22)
                $ reactTarget = "vig3_sc12_macalignment_violenceoptimism"#timestamp 7:21
                show screen streamerCommentary
                "Ama is speechless"
                if viewershipHigh == True:    
                    $ AddChatter (vig3_sc12_balcony_comment23)
                "Without losing my sights on her we head inside."
            elif macViolence < macPeace and macPessimism >= macHope:
                $ csEngagement += 1  #Logic: Coriolis likes that MAC is not going to fire, but is worried about his attitude
                $ pdEngagement += 1 #Logic: pickledDragons likes MAC's attitude but does want him to do more
                $ kcEngagement += 2 #Logic: same as above. Kitcat likes MAC's action, but not his attitude
                $ setEngagement()
                $ vig3_macAlign = "PeacePessimism"
                play audio "lazer.wav" volume 4.5
                "He fires the blaster in-between us, it hits the wall with a definitive crack."
                bcrep "Makers!" 
                show ama stream formal smug
                "Ama just stares at MAC who is resolute in his stance."
                amaS "You gonna do something with that baby blaster?"
                $ AddChatter (vig3_sc12_macshoots_comment1)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment2)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment3)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment4)
                amaS "If you're gonna shoot, you better shoot straight."
                $ AddChatter (vig3_sc12_macshoots_comment5)
                play audio "macNeutral.wav" volume 1.2
                macS "My programming... ensures perfect accuracy."
                $ AddChatter (vig3_sc12_macshoots_comment6)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment7)
                bcrep "Programming..."
                $ AddChatter (vig3_sc12_macshoots_comment8)
                "Ama flashes him her famous condescending smile."
                amaS "But did they program any nerve in you?"
                "MAC is struggling to keep the blaster straight" 
                "He's trying to do what he thinks is best..."
                macS "I can't..."
                play audio "macSad.wav" volume 1.2
                "He begins to lower the gun."
                "I didn't think droids could feel defeat."
                amaS "Takes alot more than a good shot to be an outlaw." 
                "I can feel Ama loosen her grip."
                "This is my chance."
                $ AddChatter (vig3_sc12_balcony_comment22)
                show ama stream formal shocked
                "With a proper shove I get Ama off balance and aim her rifle at her."
                mS "Enough nerve for ya?"
                $ AddChatter (vig3_sc12_balcony_comment22)
                "MAC quickly rolls to me."
                mS "We're walking out of here."
                if viewershipHigh == True:    
                    $ AddChatter (vig3_sc12_balcony_comment23)
                $ reactTarget = "vig3_sc12_macalignment_peacepessimism"#timestamp 7:21
                show screen streamerCommentary
                "Without losing my sights on her, we head inside."
            else:
                $ kcEngagement += 3 #Logic: for kitcat, this is peak. Might even be her favourite moment of the whole game
                $ pdEngagement -= 2
                $ csEngagement += 2
                $ setEngagement()
                $ vig3_macAlign = "PeaceHope"
                $ vig3_macReadAma = True
                play audio "lazer.wav" volume 4.5
                "He fires the blaster in-between us, it hits the wall with a definitive crack."
                bcrep "Makers!" 
                "Ama just stares at MAC who is resolute in his stance."
                $ AddChatter (vig3_sc12_macshoots_comment1)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment2)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment3)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment4)
                show ama stream formal smug
                amaS "You gonna do something with that baby blaster?"
                $ AddChatter (vig3_sc12_macshoots_comment5)
                amaS "If you're gonna shoot, you better shoot straight."
                play audio "macNeutral.wav" volume 1.2
                macS "My programming ensures perfect accuracy. But I won't need this."
                $ AddChatter (vig3_sc12_macshoots_comment6)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment7)
                bcrep "Programming..."
                $ AddChatter (vig3_sc12_macshoots_comment8)
                amaS "Mighty confident are we? Gonna take me on with hands?"
                macS "I will not do that."
                macS "You're going to let us go."
                $ AddChatter (vig3_sc12_macshoots_comment13)
                amaS "Sorry but I'm not feeling very charitable at the moment."
                "There's a moment as the two stare at each other."
                play audio "macHum.wav" volume 1.2
                macS "I know you still have love for Moze." 
                show ama stream formal shocked
                amaS "..."
                $ AddChatter (vig3_sc12_macshoots_comment14)
                amaS "What did you say?"
                "MAC also takes me aback but I regain composure first."
                "With a proper shove I get Ama off balance and aim her rifle at her."
                play audio "macAlarmed.wav" volume 1.2
                macS "Moze, don't hurt her."
                macS "Let's just go."
                $ AddChatter (vig3_sc12_macshoots_comment15)
                "MAC slowly rolls towards me."
                "As he passes Ama he looks at her and smiles."
                $ AddChatter (vig3_sc12_macshoots_comment16)
                macS "Take care Ama."
                $ AddChatter (vig3_sc12_balcony_comment22)
                $ reactTarget = "vig3_sc12_macalignment_peaceoptimism"#timestamp 7:21
                show screen streamerCommentary
                "Without losing my sights on her we head inside." 
                if viewershipHigh == True:    
                    $ AddChatter (vig3_sc12_balcony_comment23)
            #elif macViolence < macPeace and macPessimism < macHope:
            # "MAC is a peaceful optimist."            
            "I remove the core from the rifle, put it in my pocket and toss the shell on the ground."
            if viewershipHigh == True:    
                $ AddChatter (vig3_sc12_balcony_comment24)
            "We break into a sprint down the hall."
            $ AddChatter (vig3_sc12_balcony_comment25)
            stop music fadeout 1.0
            hide ama with dissolve
            hide bcrep with dissolve
            show mac stream neutral at stream_center_mac with move
            jump vig3_sc13
             
        "Do nothing.":
            $ vig3_outlaw += 1
            $ macViolence += 1
            $ macPessimism += 2
            $ pdEngagement += 2 #Logic: pickledDragons thinks the rep should die
            $ csEngagement -= 2 #Logic: Coriolis is appalled; kitcat is somewhat mixed. Would prefer to not let the rep die, but is also not disengaged by this choice
            $ setEngagement()
            $ vig3_bcRepSaved = False
            "When MAC's eyes lock on mine, he perks up."
            "I put a finger to my lips as I slowly shift around Ama toward him."
            bcrep "P-please..."
            $ AddChatter (vig3_sc12_nothing_comment1)
            "I'm just to Ama's side, but she doesn't even see me."
            "Her eyes are pointed dead ahead, focused on the man as the color drains from his skin."
            $ AddChatter (vig3_sc12_nothing_comment2)
            amaS "You. Don't. Own. Me."
            "The man's eyes fall on me."
            $ AddChatter (vig3_sc12_nothing_comment3)
            bcrep "H-h-help..."
            play audio "deathGasp.wav" volume 1.5
            "Ama's fist snaps closed, accompanied by a dull crunching sound."
            $ AddChatter (vig3_sc12_nothing_comment5)
            "She lets go of her grip. The body falls to the ground, limp."
            hide bcrep stream with dissolve
            $ AddChatter (vig3_sc12_nothing_comment6)
            "Ama's shoulders rise and fall as she takes deep breaths."
            show ama stream formal neutral
            "Then she turns her attention on me."
            "I freeze, just between her and MAC."
            $ AddChatter (vig3_sc12_nothing_comment4)
            amaS "Well, Mozely, where were your heroics for him?"
            menu:
                amaS "Well, Mozely, where were your heroics for him?"
                "Helping BigCorp isn't in my bag.":
                    mS "I don't really see helping BigCorp goons as being \"heroic.\""
                    $ AddChatter (vig3_sc12_bag_comment1)
                    pause 0.5
                    $ AddChatter (vig3_sc12_bag_comment2)
                    amaS "Convenient to have such flexible definitions."
                    $ AddChatter (vig3_sc12_bag_comment3)
                "I know better than to get between you and your prey.":
                    $ deadeyeApproval += 1
                    mS "I know better than to get between you and your prey."
                    $ AddChatter (vig3_sc12_prey_comment1)
                    amaS "A good lesson, but it sounds like you've forgotten that {i}you{/i} are my prey."
            show ama stream formal upset
            amaS "Now then, I'm only going to ask one more time."        
            amaS "Where is the droid?"
            play audio "macSad.wav" volume 1.2
            "A low whir escapes from MAC."
            "My heart feels like it falls out of my stomach."
            $ AddChatter (vig3_sc12_balcony_comment6)
            "Ama's eyes snap from me to MAC, then back to me."
            show ama stream formal gun
            play audio "gunCock.wav" volume 2.0
            "In the blink of an eye her rifle is drawn and pointed at my chest."
            $ AddChatter (vig3_sc12_balcony_comment8)
            amaS "Blaster on the ground, Mozely."
            $ AddChatter (vig3_sc12_balcony_comment7)
            "I grab it from the holster in my suit jacket and toss it away from me."
            amaS "That's it, isn't it?"
            $ reactTarget = "vig3_sc12_amafindsout"#timestamp 7:18
            show screen streamerCommentary   
            show ama stream formal smug
            "A thin smile creeps across her face."
            $ AddChatter (vig3_sc12_balcony_comment9)
            amaS "You almost had it too."
            $ AddChatter (vig3_sc12_balcony_comment10)
            amaS "But you're not quick enough. Never have been." 
            mS "Ama, listen to me we ha—"       
            amaS "All that struggle. All that runnin'."
            $ AddChatter (vig3_sc12_balcony_comment11)
            amaS "Was it worth it?"
            hide screen streamerCommentary
            "I look at MAC, and then Ama."
            menu:
                "I look at MAC, and then Ama."
                "You would never understand.":
                    $ macHope += 1
                    $ kcEngagement += 1 #Logic: the implication that MAC is the most important thing
                    mS "Yes. A million times yes."
                    mS "But I guess you wouldn't understand."
                    mS "You've only ever really cared about yourself."
                "Yes, fighting back is all we can do.":
                    $ macHope += 1
                    $ csEngagement += 1 #Logic: heroic moze
                    mS "Yes. A million times yes."
                    mS "Fighting back against them is all we can do, Ama."
                    mS "I thought you knew that."
                "No, but it was worth a shot.":
                    $ macPessimism += 1
                    $ pdEngagement += 1 #Logic: pickledDragons likes the honesty
                    mS "If I knew it would come up short like this?"
                    mS "No. But it was worth a shot."
                    mS "I figured you of all people would understand that."
            $ setEngagement()
            show ama stream formal shocked
            "What happens next unfolds in a split second."
            "A shadow flickers across Ama's gaze."
            "Her eyes, alert, focused, dead to all the world except her prey, falter."
            "For the briefest of moments, she's somewhere else."
            "The barrel of her rifle shifts just a bit, and, before I even think to act, my body lunges forward."
            "I grab the gun's barrel and heave it to the side."
            play audio "lazer.wav" volume 5.0
            $ AddChatter (vig3_sc12_balcony_comment12)
            pause 0.5
            $ AddChatter (vig3_sc12_balcony_comment13)
            "The bolt sails past my head, just barely grazing my cheek."
            ###The commented out lines are an alternative where Ama doesn't fire her rifle - they can be cut###
            #"I throw my shoulder into Ama's chest before she can fire.""
            #"It's like tackling a mountain, but I manage to force her to the ground, sending her rifle skidding to the edge of the balcony.""
            #"Ama kicks me off her chest."
            #amaS "You little shit!"
            #"We both lunge for each other, grappling at one another's shoulders, trying to get the advantage on the other."
            #"I'm holding my own, but then the tide starts to turn. She's just too strong."
            show ama stream formal angry
            amaS "You little shit!"
            show ama stream formal gun
            "I try to pry it from her hands, but she's as strong as I remember."
            $ AddChatter (vig3_sc12_balcony_comment14)
            "I struggle against her strength as we yank the rifle back and forth."
            $ AddChatter (vig3_sc12_balcony_comment15)
            play audio "lazer.wav" volume 5.0
            #"{b}BANG!{/b}"
            "A chunk of the rail explodes out into the open air."
            show ama stream formal shocked
            play audio "macPester.wav" volume 1.5
            macS "{i}Stop it!{/i}"
            $ AddChatter (vig3_sc12_balcony_comment16)
            pause 0.5
            $ AddChatter (vig3_sc12_balcony_comment17)
            "Ama and I hit a stalemate as we turn to MAC."
            "And there's MAC, with my blaster in his hand."
            $ AddChatter (vig3_sc12_balcony_comment18)
            "Gripping the handle like it's his own."
            if macViolence >= macPeace and macPessimism >= macHope:
                $ vig3_outlaw += 1
                $ pdEngagement += 3 #Logic: pickledDragons likes the outlaw version of MAC
                $ csEngagement -= 2 #Logic: coriolis is freaked out by MAC here. Kitcat doesn't like what MAC is learning, but likes that he's standing up for himself.
                $ kcEngagement += 1
                $ setEngagement()
                $ vig3_macAlign = "ViolentPessimism"
                $ vig3_macShootAma = True
                play audio "lazer.wav" volume 5.0
                "He fires the blaster in-between us. It hits the wall with a definitive crack."
                "Ama just stares at MAC who is resolute in his stance."
                show ama stream formal smug
                amaS "You gonna do something with that baby blaster?"
                $ AddChatter (vig3_sc12_macshoots_comment1)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment2)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment3)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment4)
                amaS "If you're gonna shoot, you better shoot straight."
                $ AddChatter (vig3_sc12_macshoots_comment5)
                play audio "macNeutral.wav" volume 1.2
                macS "My programming ensures perfect accuracy. Shall I demonstrate?" 
                $ AddChatter (vig3_sc12_macshoots_comment6)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment7)
                amaS "Well then, let's—"
                $ AddChatter (vig3_sc12_macshoots_comment8)
                play audio "lazer.wav" volume 5.0
                "The blaster rings out and before I can react Ama is on the ground clutching her side."
                show ama stream formal shocked
                amaS "Bastard!" 
                macS "I have been provoked and damaged, I will defend myself."
                $ AddChatter (vig3_sc12_macshoots_comment9)
                macS "I will defend my Captain."
                $ AddChatter (vig3_sc12_macshoots_comment10)
                "MAC slowly rolls towards me, passing Ama without even looking at her."
                show ama stream formal angry
                amaS "You won't get out of here, you know."
                play audio "macPing.wav" volume 1.2
                macS "Will you stop us? I can remove you if necessary."
                show ama stream formal shocked
                $ AddChatter (vig3_sc12_macshoots_comment11)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment12)
                amaS "I—"
                play audio "macPester.wav" volume 1.2
                macS "We should leave, yes?"
                $ AddChatter (vig3_sc12_balcony_comment22)
                $ reactTarget = "vig3_sc12_macalignment_violencepessimism"#timestamp 7:21
                show screen streamerCommentary
                mS "You got it."
                if viewershipHigh == True:
                    $ AddChatter (vig3_sc12_balcony_comment23)
                "Without losing my sights on her, we head inside."
            elif macViolence >= macPeace and macPessimism < macHope:
                $ vig3_outlaw += 1
                $ pdEngagement += 2 #Logic: similar as above but pd and cs are lessened
                $ csEngagement -= 1
                $ kcEngagement += 2
                $ setEngagement()
                $ vig3_macAlign = "ViolentHope"
                play audio "lazer.wav" volume 5.0
                "He fires the blaster in between us, it hits the wall with a definitive crack." 
                "Ama just stares at MAC who holds the gun steady but with noticeable apprehension."
                show ama stream formal smug
                amaS "You gonna do something with that baby blaster?"
                $ AddChatter (vig3_sc12_macshoots_comment1)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment2)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment3)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment4)
                amaS "If you're gonna shoot, you better shoot straight."
                $ AddChatter (vig3_sc12_macshoots_comment5)
                play audio "macNeutral.wav" volume 1.2
                macS "My programming ensures perfect accuracy when required." 
                $ AddChatter (vig3_sc12_macshoots_comment6)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment7)
                amaS "Well then, let's see it."
                $ AddChatter (vig3_sc12_macshoots_comment8)
                macS "I know you don't want BigCorp to succeed anymore than we do."
                amaS "I don't know I'm being paid quite well."
                show ama stream formal shocked
                play audio "lazer.wav" volume 5.0
                "Another fire from the blaster, right in front of Ama's face."
                macS "Then I'll shoot you if I must."
                $ AddChatter (vig3_sc12_macshoots_comment9)
                show ama stream formal angry
                amaS "You little bastard."
                $ AddChatter (vig3_sc12_macshoots_comment10)
                "This is my chance."
                show ama stream formal shocked
                "With a proper shove, I get Ama off balance and aim her rifle at her."
                mS "MAC, let's go!" 
                play audio "macAffirmative.wav" volume 1.2
                macS "Yes Captain!"
                "MAC wheels towards me and stops at Ama."
                $ AddChatter (vig3_sc12_macshoots_comment11)
                macS "Captain says you're one of the best."
                $ AddChatter (vig3_sc12_macshoots_comment12)
                macS "My records show a long list of... accomplishments perpetrated by you."
                amaS "And what about it?"
                macS "I thought you'd be better than this."
                $ AddChatter (vig3_sc12_balcony_comment22)
                $ reactTarget = "vig3_sc12_macalignment_violenceoptimism"#timestamp 7:21
                show screen streamerCommentary
                "Ama is speechless"
                if viewershipHigh == True:
                    $ AddChatter (vig3_sc12_balcony_comment23)
                "Without losing my sights on her, we head inside."
            elif macViolence < macPeace and macPessimism >= macHope:
                $ csEngagement += 1  #Logic: Coriolis likes that MAC is not going to fire, but is worried about his attitude
                $ pdEngagement += 1 #Logic: pickledDragons likes MAC's attitude but does want him to do more
                $ kcEngagement += 2 #Logic: same as above. Kitcat likes MAC's action, but not his attitude
                $ setEngagement()
                $ vig3_macAlign = "PeacePessimism"
                play audio "lazer.wav" volume 4.5
                "He fires the blaster in-between us, it hits the wall with a definitive crack."
                "Ama just stares at MAC who is resolute in his stance."
                show ama stream formal smug
                amaS "You gonna do something with that baby blaster?"
                $ AddChatter (vig3_sc12_macshoots_comment1)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment2)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment3)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment4)
                amaS "If you're gonna shoot, you better shoot straight."
                $ AddChatter (vig3_sc12_macshoots_comment5)
                play audio "macNeutral.wav" volume 1.2
                macS "My programming... ensures perfect accuracy."
                $ AddChatter (vig3_sc12_macshoots_comment6)
                $ AddChatter (vig3_sc12_macshoots_comment7)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment8)
                "Ama flashes him her famous condescending smile."
                amaS "But did they program any nerve in you?"
                "MAC is struggling to keep the blaster straight" 
                "He's trying to do what he thinks is best..."
                macS "I can't..."
                play audio "macSad.wav" volume 1.2
                "He begins to lower the gun."
                "I didn't think droids could feel defeat."
                amaS "Takes alot more than a good shot to be an outlaw." 
                "I can feel Ama loosen her grip."
                "This is my chance."
                $ AddChatter (vig3_sc12_balcony_comment22)
                show ama stream formal shocked
                "With a proper shove, I get Ama off balance and aim her rifle at her."
                mS "Enough nerve for ya?"
                if viewershipHigh == True:
                    $ AddChatter (vig3_sc12_balcony_comment23)
                "MAC quickly rolls to me."
                mS "We're walking out of here."
                $ reactTarget = "vig3_sc12_macalignment_peacepessimism"#timestamp 7:21
                show screen streamerCommentary
                "Without losing my sights on her, we head inside."
            else:
                $ kcEngagement += 3 #Logic: for kitcat, this is peak. Might even be her favourite moment of the whole game
                $ pdEngagement -= 2
                $ csEngagement += 2
                $ setEngagement()
                $ vig3_macAlign = "PeaceHope"
                $ vig3_macReadAma = True
                play audio "lazer.wav" volume 5.0
                "He fires the blaster in-between us, it hits the wall with a definitive crack."
                "Ama just stares at MAC who is resolute in his stance."
                show ama stream formal smug
                $ AddChatter (vig3_sc12_macshoots_comment1)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment2)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment3)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment4)
                amaS "You gonna do something with that baby blaster?"
                $ AddChatter (vig3_sc12_macshoots_comment5)
                amaS "If you're gonna shoot, you better shoot straight."
                play audio "macNeutral.wav" volume 1.2
                macS "My programming ensures perfect accuracy. But I won't need this."
                $ AddChatter (vig3_sc12_macshoots_comment6)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment7)
                pause 0.5
                $ AddChatter (vig3_sc12_macshoots_comment8)
                amaS "Mighty confident are we? Gonna take me on with hands?"
                macS "I will not do that."
                macS "You're going to let us go."
                amaS "Sorry, but I'm not feeling very charitable at the moment."
                "There's a moment as the two stare at each other."
                play audio "macHum.wav" volume 1.2
                macS "I know you still have love for Moze." 
                show ama stream formal shocked
                amaS "..."
                $ AddChatter (vig3_sc12_macshoots_comment14)
                amaS "What did you say?"
                "MAC also takes me aback, but I regain composure first."
                "With a proper shove, I get Ama off balance and aim her rifle at her."
                play audio "macAlarmed.wav" volume 1.2
                macS "Moze, don't hurt her."
                macS "Let's just go."
                $ AddChatter (vig3_sc12_macshoots_comment15)
                "MAC slowly rolls toward me."
                "As he passes Ama, he looks at her and smiles."
                $ AddChatter (vig3_sc12_macshoots_comment16)
                macS "Take care, Ama."
                $ AddChatter (vig3_sc12_balcony_comment22)
                $ reactTarget = "vig3_sc12_macalignment_peaceoptimism"#timestamp 7:21
                show screen streamerCommentary
                "Without losing my sights on her we head inside." 
                if viewershipHigh == True:    
                    $ AddChatter (vig3_sc12_balcony_comment23)
            #elif macViolence < macPeace and macPessimism < macHope:
            # "MAC is a peaceful optimist."            
            "I remove the core from the rifle, put it in my pocket, and toss the shell on the ground."
            if viewershipHigh == True:    
                $ AddChatter (vig3_sc12_balcony_comment24)
            "We break into a sprint down the hall."
            $ AddChatter (vig3_sc12_balcony_comment25)
            stop music fadeout 3.0
            hide ama with dissolve
            hide bcrep with dissolve
            hide vybalcony_stream with dissolve
            show mac stream neutral at stream_center_mac with move
            jump vig3_sc13
    

label vig3_sc13():
    show inventorsfairgallery_stream at topleft onlayer background with dissolve
    play music "soundtrack/akar(fairSlaps).wav" fadein 1.0
    hide vybalcony_stream
    "My blaster feels heavier as we run down the winding paths of the Vineyard." 
    $ AddChatter (vig3_sc13_fairint_comment1)
    "Tucked away tight to my side, I'm resolute in making sure MAC doesn't touch it."
    $ AddChatter (vig3_sc13_fairint_comment2)
    pause 0.5
    $ AddChatter (vig3_sc13_fairint_comment3)
    if viewershipHigh == True:
        pause 0.5
        $ AddChatter (vig3_sc13_fairint_comment4)
    "There's no time to talk about what happened."
    "I wouldn't even know where to begin."
    $ AddChatter (vig3_sc13_fairint_comment5)
    "Not that MAC looks too inclined to talk about it anyways." 
    if viewershipHigh == True:
        $ AddChatter (vig3_sc13_fairint_comment6)
        pause 0.5
        $ AddChatter (vig3_sc13_fairint_comment7)
        pause 0.5
        $ AddChatter (vig3_sc13_fairint_comment8)
    macS "They should be right down here."
    "This whole area has been cleared. Why is there no one here?"
    "Loud bangs ring out in the distance. Fireworks? Maybe?"
    hide screen streamerCommentary
    "MAC leads the way, turning down hallways quickly and abruptly."
    play audio "macHum.wav" volume 1.2
    macS "It is good to see you, Captain."
    mS "It's good to see you too, MAC."
    "We can't stop running, but I have dozens of questions."
    "One just happens to pop out of my mouth."
    mS "How the hell did you end up on that presentation stage?"
    $ AddChatter (vig3_sc13_fairint_comment9)
    play audio "macNeutral.wav" volume 1.2
    macS "A confluence of circumstantial factors."
    macS "I escaped the Hounds' restraints shortly after entering this facility, and evaded them by entering a laundry chute."
    $ AddChatter (vig3_sc13_fairint_comment10)
    macS "That chute deposited me in BigCorp's dressing room where I saw the display of a prototype that resembled me."
    macS "I disposed of the prototype and took its place, hoping the disguise would present an opportunity to escape."
    menu:
        macS "I disposed of the prototype and took its place, hoping the disguise would present an opportunity to escape."
        "Good thinking, MAC!":
            $ kcEngagement += 1
            mS "Wow, MAC, that was really resourceful!"
            macS "I had excellent teachers."
            $ AddChatter (vig3_sc13_thinking_comment1)
        "That was dangerous!":
            $ csEngagement += 1
            mS "MAC, that was dangerous! What if BC discovered you and took you away?"
            macS "They did not. I have learned the art of stealth from you, after all."
            $ AddChatter (vig3_sc13_dangerous_comment1)
            pause 0.5
            $ AddChatter (vig3_sc13_dangerous_comment2)
        "What do you mean, \"disposed of\"?":
            $ pdEngagement += 1
            mS "Wait, what do you mean you \"disposed\" of the prototype?"
            macS "If the signs on the chute were correct, it is currently being relocated to a waste disposal location outside Akar."
            $ AddChatter (vig3_sc13_disposed_comment1)
            pause 0.5
            $ AddChatter (vig3_sc13_disposed_comment2)
    $ setEngagement()
    play audio "macPing.wav" volume 1.5
    macS "In here!"
    "MAC stops us at a door, I can hear muffled arguing beyond it."
    $ AddChatter (vig3_sc13_fairint_comment11)
    play audio "door.wav" volume 2.0
    "With an efficiency that I've only ever seen from Teresa, MAC undoes the scanner and the door swings open."
    $ AddChatter (vig3_sc13_fairint_comment12)
    play audio "gunCock.wav" volume 2.0
    show mac stream shock at stream_right5mac with move
    "Two blasters are pointed at my face as the door swings open."
    show rec stream formal surprised at stream_left5 with Dissolve(0.5)
    show teresa stream fight at stream_right with Dissolve(0.5)
    show jennica stream fight at stream_left with Dissolve(0.5)
    mS "Well, don't be too happy to see me!"
    enS "Captain!"
    if viewershipHigh == True:
        $ AddChatter (vig3_sc13_fairint_comment13)
    pS "Thought ya dead, I won't lie."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc13_fairint_comment14)
        pause 0.5
        $ AddChatter (vig3_sc13_fairint_comment15)
    "MAC rushes past me to grab Teresa's legs. The door closes behind me as I walk in." 
    show teresa stream happy
    show jennica stream neutral
    show mac stream neutral
    show rec stream formal happy
    enS "Good to see you, buddy."
    $ AddChatter (vig3_sc13_fairint_comment16)
    pS "Where's Deadeye?"
    mS "Left her on the east balcony."
    mS "Might be on our tail, but she didn't see where we went."
    pS "That gives us some time."
    enS "But we have MAC and that's what's important."
    recS "Not just MAC."
    "They hold up the range extender laying on the counter near them."
    mS "How?"
    pS "Long story, truly. Did you know Zan is here?"
    mS "At the Fair? For what?"
    recS "He's one of the featured designers! A big name in biomechanical engineering."
    pS "He's got some good-lookin' work."
    show rec stream formal thinking
    recS "And some good-lookin' muscles."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc13_fairint_comment17)
    mS "..."
    recS "Forget I said that."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc13_fairint_comment18)
        pause 0.5 
        $ AddChatter (vig3_sc13_fairint_comment19)
        pause 0.5
        $ AddChatter (vig3_sc13_fairint_comment20)
    show rec stream formal happy
    mS "Okay let's focus up. What's going on here."
    $ AddChatter (vig3_sc13_fairint_comment21)
    show teresa stream neutral
    show jennica stream neutral
    enS "Rec found a private comms room. We were hoping to at least catch our breath before we head out."
    pS "Can't go back through the party."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc13_fairint_comment22)
        pause 0.5
        $ AddChatter (vig3_sc13_fairint_comment23)
        pause 0.5
        $ AddChatter (vig3_sc13_fairint_comment24)
    recS "But there's still a shuttle system that can get us to Akar. It should be a quick run from here."
    if viewershipHigh == True:
        $ AddChatter (vig3_sc13_fairint_comment25)
    enS "Ama will probably head there too."
    mS "If she's not already getting her ship off the ground to scan for us."
    "We need to act now."
    menu: 
        "We need to act now."
        "Call in a favour to deal with Ama.":
            play audio "callRing.wav" volume 2.0
            "Let's just hope he picks up."
            if vig2_outlawEpilogue == True:
                jump vig3outlawcomms
            else:
                jump vig3marshalcomms 
        "Mad dash to the shuttles.":
            mS "No time to lose, lets make a break for it!"
            $ AddChatter (vig3_sc13_dash_comment1)
            hide mac with dissolve
            hide teresa with dissolve
            hide rec with dissolve
            hide jennica with dissolve
            #"..."
            show mac stream shock at stream_right5mac with vpunch
            play audio "macAlarmed.wav" volume 1.5
            macS "{i}Apologies!{/i}"
            "That was the third security guard MAC ran over with reckless abandon."
            $ AddChatter (vig3_sc13_dash_comment2)
            "Like a little purple battering ram, MAC was clearing a path through just as Reynar's security came to intercept us."
            $ AddChatter (vig3_sc13_dash_comment3)
            pause 0.5
            $ AddChatter (vig3_sc13_dash_comment4)
            "When we set off, we didn't imagine it would be this close to the fair."
            "Dodging through the side garden to the entrance shuttles, I pray that Reynar isn't too upset with our escape plan."
            show jennica stream shock at stream_left with dissolve
            pS "Jeez this kid's goin' fast and furious."
            show teresa stream happy at stream_right with dissolve
            enS "He gets it from you!"
            show rec stream formal thinking at stream_left5
            recS "This architecture is incredible, the bio-tech is so seemlessly integrated into the material of the wall."
            mS "{i}Rec, look forward!{/i}"
            show rec stream formal surprised at stream_left5
            "In their distracted state they mindlessly slam into a couple going hot and heavy."
            "No doubt using the garden to avoid any possible scandal."
            invfairnpc2 "Watch yourself!"
            $ AddChatter (vig3_sc13_dash_comment5)
            "The two narrowly dodge MAC only to get slammed by Jennica."
            $ AddChatter (vig3_sc13_dash_comment6)
            pause 0.5
            $ AddChatter (vig3_sc13_dash_comment7)
            show jennica stream neutral
            pS "Keep up y'all I'm the only one in heels and I'm leagues ahead!"
            $ AddChatter (vig3_sc13_dash_comment8)
            pause 0.5
            $ AddChatter (vig3_sc13_dash_comment9)
            enS "Stop showing off!"
            if viewershipHigh == True:
                $ AddChatter (vig3_sc13_dash_comment10)
            pS "How 'bout ya start showing up!"
            show rec stream formal happy
            recS "How about that terrarium!"
            mS "{i}Rec!{/i}"
            "I can see the exit to the shuttles just in reach."
            reynar "Having fun, Mozely?"
            $ AddChatter (vig3_sc13_dash_comment11)
            if viewershipHigh == True:
                pause 0.5
                $ AddChatter (vig3_sc13_dash_comment12)
            hide rec with dissolve
            hide jennica with dissolve
            hide mac with dissolve
            hide teresa with dissolve
            show reynar stream angry at stream_center with dissolve
            show houndgoon stream neutral at stream_left with dissolve
            show houndleader stream neutral at stream_right with dissolve
            "We stop dead in our tracks as Reynar appears."
            "Flanked by the hounds."
            reynar "*sigh* You've been making quite the mess of things, haven't you?"
            $ AddChatter (vig3_sc13_dash_comment13)
            mS "You don't know the half of it."
            reynar "Don't flatter yourself."
            mS "We're just leaving."
            reynar "How unfortunate. But did you have to make such a commotion on the way out?"
            if viewershipHigh == True:
                $ AddChatter (vig3_sc13_dash_comment14)
            "Just then I see the glass windows of the gallery to my right lined with prying eyes."
            reynar "Now, I have to make a show of this."
            "We struggle against the Hounds as we're overwhelmed by Reynar's forces."
            "I can hear the faint sounds of clapping as we're pulled out of the garden."
            "Reynar turns his back to us as he renters the gallery."
            hide houndgoon with dissolve
            hide houndleader with dissolve
            hide reynar with dissolve
            hide inventorsfairgallery_stream with dissolve
            jump vig3_sc14
        
label vig3outlawcomms():
    show matticus phone neutral at stream_center_mac with dissolve
    show jennica stream angry
    $ pdEngagement += 1  #Logic: pickledDragons like that you are continuing to have a relationship with Matticus
    $ kcEngagement -= 1 #Logic: kitcat and coriolis don't like Matticus
    $ csEngagement -= 1
    $ setEngagement()
    smatt "Well hello ladies! Need a hand from little ol' me?"
    $ AddChatter (vig3_outlawcomms_comment1)
    "Matticus smiles in that shit-eating grin that he loves."
    $ AddChatter (vig3_outlawcomms_comment2)
    pS "This is a terrible idea."
    "I'm starting to agree."
    $ AddChatter (vig3_outlawcomms_comment3)
    pause 0.5
    $ AddChatter (vig3_outlawcomms_comment4)
    mS "We're not here for pleasantries."
    $ AddChatter (vig3_outlawcomms_comment5)
    recS "I almost forgot what he was like."
    show rec stream formal neutral
    smatt "Is that little Reccrin?"
    smatt "Been a while, kid."
    recS "You know I'm the older one, right?"
    smatt "Hard to tell when Allistar was the one with the nerve."
    mS "Matticus!"
    smatt "What is it, sweetheart?"
    $ AddChatter (vig3_outlawcomms_comment6)
    mS "Ama found us in the Vineyard. We need to give her a hard time following us out of here."
    smatt "The Vineyard? It sounds like you did this to yourself lovey!"
    mS "I don't have to explain my reasons to you. Can you do it or not?"
    enS "This is a waste of time, Matt can't take on Reynar."
    smatt "Excuse you, must you think so little of me?"
    pS "Couldn't even hide us well 'nough. I say let's go Cap."
    $ AddChatter (vig3_outlawcomms_comment7)
    pause 0.5
    $ AddChatter (vig3_outlawcomms_comment8)
    recS "Reynar's system is too impressive anyway, you wouldn't be much of a challenge."
    $ AddChatter (vig3_outlawcomms_comment9)
    pause 0.5
    $ AddChatter (vig3_outlawcomms_comment10)
    smatt "Okay okay, since you did such a good job."
    $ AddChatter (vig3_outlawcomms_comment11)
    smatt "I'll make sure Reynar's Vineyard will be especially hostile to a certain outlaw with BC affiliations."
    $ AddChatter (vig3_outlawcomms_comment12)
    mS "Fabulous."
    $ AddChatter (vig3_outlawcomms_comment13)
    smatt "Aren't I?"
    smatt "Bye bye, and try not to die. I'll be looking for you to repay the favour."
    play audio "cutCall.wav" volume 1.5
    hide matticus with dissolve
    "The comms go dead."
    $ AddChatter (vig3_outlawcomms_comment14)
    macS "Skeeve."
    recS "The biggest."
    mS "Let's get out of here."
    "Just then an announcement comes on in the hall."
    invfairannounce "Unauthorized personnel in east wing hallway."
    "I hear the unmistakable sound of footsteps."
    "Then Ama yelling."
    amaS "Get {i}off{/i} me!" 
    mS "Now's our shot!"
    "We run out of the hallway in the opposite direction of the commotion. And are stoppped by an unfortunate face."
    #stop music fadeout 1.0
    show houndleader stream neutral at stream_center with dissolve
    houndleader "And where do y'all think you're goin'?."
    houndleader "We've got orders for you all to come with us."
    "Shit."
    hide jennica with dissolve
    hide mac with dissolve
    hide teresa with dissolve
    hide rec with dissolve
    hide houndleader with dissolve
    hide inventorsfairgallery_stream
    jump vig3_sc14

label vig3marshalcomms():
    show matticus phone neutral at stream_center_mac with dissolve
    show jennica stream angry
    $ pdEngagement += 1 #Logic: pickledDragons finds this development interesting; the other two are neutral
    $ setEngagement()
    smatt "Well hello ladies! To what do I owe the pleasure?"
    "Matticus smiles in that shit-eating grin that he loves."
    $ AddChatter (vig3_marshalcomms_comment1)
    pS "Disrespectfully, we didn't call you."
    "This is bad."
    smatt "Oh no? Were you perchance hoping I was some young redheaded datacenter intern?"
    show rec stream formal neutral
    $ AddChatter (vig3_marshalcomms_comment2)
    recS "Sounds like a nicer face to look at."
    smatt "Oh is that little Reccrin? The Snakehawk dropout?"
    smatt "Still hiding in that little hovel in Akar?"
    smatt "Oh Moze you do love to live dangerously don't you."
    mS "What kind of bullshit is this?"
    $ AddChatter (vig3_marshalcomms_comment3)
    enS "Where's the kid?"
    smatt "Ever since your hack job with the Sallent ship, I had to restablish the pecking order around here."
    smatt "So I had to make an example."
    $ AddChatter (vig3_marshalcomms_comment4)
    "This rat bastard."
    mS "That's low, even for you."
    enS "How do you sleep at night?"
    smatt "Oh don't look at me like that."
    smatt "The kid's alive."
    smatt "Which is better than what'll happen to you."
    "Jenn spits on the ground."
    mS "I think we're done here."
    smatt "Oh, Mozely, from the bottom of my heart."
    smatt "You deserve everything that's coming to you."
    smatt "Bye bye now!"
    play audio "cutCall.wav" volume 1.5
    hide matticus with dissolve
    "The comms go dead."
    macS "Skeeve."
    recS "The biggest."
    #mS "Only one way out now. We have to make a break for the shuttles." #I made this ending loop back to the mad dash that could happen if you don't call for help.
    #enS "Aye."
    #show jennica stream neutral
    #pS "Way ahead of you!"
    #"We all make a break for it, rushing out of the room as fast as we can."
    #This should be a different ending, make it unique.
    #"Carefully we make it to the shuttles. Not sure what awaits us on the other side."
    #jump vig3_sc13_dash
    mS "Let's get out of here."
    play audio "shipAlarmShort.wav" volume 0.8
    "Just then an annoucement echoes from the hall."
    invfairannounce "Unauthorized personnel in comms room 45B."
    "I look at the placard next to the door."
    "Shit."
    "Before we can even leave, boots swarm the hall outside."
    play audio "door.wav" volume 2.0
    "And we're met with an unfortunately familiar face."
    $ AddChatter (vig3_marshalcomms_comment5)
    hide jennica with dissolve
    hide mac with dissolve
    hide rec with dissolve
    show houndleader stream neutral at stream_center with dissolve
    #stop music
    houndleader "Well hello there, sweetcheeks."
    $ AddChatter (vig3_marshalcomms_comment5)
    houndleader "We've got orders for you all to come with us."
    enS "Shit."
    hide teresa with dissolve
    "The Hounds along with majority of their detail take us down the hall."
    houndleader "Ma'am I'd suggest you head back to the gallery, this is restricted area."
    "I turn and there's Ama, fuming, watching her prey get snatched up before her very eyes."
    hide houndleader with dissolve
    hide inventorsfairgallery_stream
    #This should be a different ending, make it unique.
    jump vig3_sc14

label vig3_sc14():
    $ viewCheck9 = viewCount
    #hide jennica with dissolve
    #hide mac with dissolve
    #hide teresa with dissolve
    #hide rec with dissolve
    stop music fadeout 2.0
    #hide houndleader with dissolve
    show exteriorvineyard_stream at topleft onlayer background with dissolve
    $ AddChatter(vig3_sc14_escape_comment1)
    "Just beyond the entrance the shuttles are empty."
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment2)
        pause 0.5
    $ AddChatter(vig3_sc14_escape_comment3)
    "Reynar hasn't toasted to the crowd, and people wouldn't dare to leave before his address."
    $ AddChatter(vig3_sc14_escape_comment4)
    "The hounds flank the crew as they escort us out."
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment5)
    show houndleader stream neutral at stream_center with dissolve
    houndleader "This one, it'll take you right to the plaza."
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment6)
    "The hound leader inputs some commands into the keypad and the doors swing open."
    menu: 
        "Say something?"
        "That's it?":
            mS "So, that's it? Just showing us the door?"
            $ AddChatter(vig3_sc14_thatsit_comment1)
            pause 0.5
            $ AddChatter(vig3_sc14_thatsit_comment2)
            houndleader "I'm sorry, did you want a red carpet?"
            $ AddChatter(vig3_sc14_thatsit_comment3)
            mS "We can start with an explanation."
            houndleader "Just be happy you're getting an easy out."
            houndleader "Now get in, sweetcheeks."
            $ AddChatter(vig3_sc14_thatsit_comment4)
        "What's your angle?":
            mS "So, what's the angle?"
            $ AddChatter(vig3_sc14_angle_comment1)
            houndleader "Straight down right to Akar."
            $ AddChatter(vig3_sc14_angle_comment2)
            pause 0.5
            $ AddChatter(vig3_sc14_angle_comment3)
            mS "Don't be so—"
            houndleader "Just be lucky we're under orders."
            houndleader "I'd suggest taking advantage of the easy out."
            $ AddChatter(vig3_sc14_angle_comment4)
        "Say nothing.":
            "I look at the hounds surrounding us."
            $ AddChatter(vig3_sc14_nothing_comment1)
            "I don't trust their lack of hostility."
            $ AddChatter(vig3_sc14_nothing_comment2)
            "But I can't help but feel lucky about the easy out."
            houndleader "Don't stay too long in Akar."
            houndleader "We'll be looking."
            $ AddChatter(vig3_sc14_nothing_comment3)
    "We all walk into the shuttle and take a seat."
    houndgoon "Captain, we got another one!"
    houndleader "Put 'em in this one!"
    houndleader "Then let's get the hell out of here."
    houndleader "I need a drink after this."
    show ama stream formal neutral at stream_right5 with dissolve
    "I'm unsurprised as Ama walks in and takes her spot near the door."
    "She holds out some credits and the Hound leader takes it."
    houndleader "Job's done, let's move."
    "The hounds leave just as quickly as they came."
    hide houndleader with dissolve
    play audio "door.wav" volume 2.0
    "The shuttle doors close behind her."
    $ AddChatter(vig3_sc14_escape_comment7)
    "We stay there in dangerous slience."

    hide mac with dissolve
    play audio "disruptiveBang.wav" volume 1.3
    show ama stream formal neutral at stream_right5 with vpunch
    "Then I'm thrown against the wall, and there's Ama, knife in hand at my throat."
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment8)
    show teresa stream fight at stream_right
    show jennica stream fight at stream_left
    "Teresa and Jen are quick to act."
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment9)
    enS "Let her go, Ama!"
    "Teresa attempts to grab Ama who kicks her into Jenn with deadly ease."
    $ AddChatter(vig3_sc14_escape_comment10)
    hide teresa with vpunch
    enS "Agh!"
    "From the ground Jenn pulls out her gun."
    pS "Don't make us send you back in a body bag."
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment11)
    show ama stream formal upset
    amaS "Then you'll need to make room for two."
    "She presses harder against my throat."
    amaS "Now, how about we all stay still and quiet, and do as I—"
    "Her eyes meet Rec's."
    $ AddChatter(vig3_sc14_escape_comment12)
    hide jennica with dissolve
    hide teresa with dissolve
    show ama stream formal neutral at stream_right with move
    show rec stream formal surprised at stream_left with dissolve
    play music "soundtrack/decisionTime.wav"
    recS "Deadeye..."
    amaS "Well well..."
    $ AddChatter(vig3_sc14_escape_comment13)
    amaS "If it isn't Reccrin."
    amaS "Right where we left him."
    show rec stream formal angry
    $ AddChatter(vig3_sc14_escape_comment14)
    "The shuttle hums as it takes off down to Akar."
    recS "Screw you..."
    $ AddChatter(vig3_sc14_escape_comment15)
    show ama stream formal smug
    amaS "Oh? They speak?"
    $ AddChatter(vig3_sc14_escape_comment16)
    pause 0.5
    $ AddChatter(vig3_sc14_escape_comment17)
    recS "Screw you, Ama! You took Allistar away to go galavanting in the Outposts."
    $ AddChatter(vig3_sc14_escape_comment18)
    recS "I have nothing to say to you."
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment19)
    amaS "Please, I'm not the one who wanted to be selfish and weigh him down."
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment20)
    amaS "That kid had so much talent and potential, and you just wanted him to {i}rot{/i} in a shop!"
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment21)
    recS "We had a good life!"
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment22)
    recS "And I stayed in Akar because I knew that was the only way I could see him."
    "Ama looks around expectantly."
    "A realization creeps across her face."
    show ama stream formal neutral
    amaS "Mozely..."
    amaS "Where is Allistar?"
    amaS "Last I checked, I left him with you."
    show rec stream formal surprised
    "Rec's eyes fix to me."
    $ AddChatter(vig3_sc14_escape_comment23)
    recS "What?"
    amaS "Oh, you didn't know?"
    "Guilt stains all of our faces."
    $ AddChatter(vig3_sc14_escape_comment24)
    "My mouth goes dry and the air feels like it's being choked out of me."
    $ AddChatter(vig3_sc14_escape_comment25)
    recS "Is this true?"
    "I don't answer."
    $ AddChatter(vig3_sc14_escape_comment26)
    recS "Moze..."
    "MAC catches my eyes from the back of the shuttle."
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment27)
    show rec stream formal angry
    recS "{i}Moze{/i}!"
    mS "It is..."
    recS "Well!?"
    recS "Where is he!?"
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment28)
    "Blood starts to pool from the blade as I try to form the words."
    mS "He's dead, Rec. I killed him."
    $ AddChatter(vig3_sc14_escape_comment29)
    pause 0.5
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment30)
        $ AddChatter(vig3_sc14_escape_comment31)
    "Rec's eyes widen, as they step back, horrified."
    recS "No."
    recS "That's not true."
    "They look around at all of us. Jenn and Teresa can't look them in the eyes."
    $ AddChatter(vig3_sc14_escape_comment32)
    pause 0.5
    $ AddChatter(vig3_sc14_escape_comment33)
    pause 0.5
    $ AddChatter(vig3_sc14_escape_comment34)
    pause 0.5
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment35)
        $ AddChatter(vig3_sc14_escape_comment36)
        pause 0.5
        $ AddChatter(vig3_sc14_escape_comment37)
    $ AddChatter(vig3_sc14_escape_comment38)
    recS "Why?"
    if viewershipHigh == True:
        $ AddChatter(vig3_sc14_escape_comment39)
    menu: 
        "Explain to Rec why you shot Allistar?"
        "I didn't want to. It just happened.":
            $ vig3_recResponse = "Confused"
            $ pilotApproval += 2 #Logic: I think Jenn, as Moze's oldest friend, probably has sympathy for her mixed up emotions.
            $ pdEngagement -= 3
            if misclick == True:
                $ csEngagement += 3 #Logic: if you identified that you misclicked, then Coriolis likes that this kind of parallels your personal experience.
            else:
                $ csEngagement += 1  #Logic: if you didn't identify a misclick, they're just sympathetic in general
            $ kcEngagement -= 1 #Logic: even kitcat doesn't really like that response: DEFEND MAC!
            $ setEngagement()
            $ deadeyeApproval -= 2
            $ macPeace += 1 #I feel like MAC would understand this as expressing remorse for actions, teaching him to ask for forgivness and not just stubbornly assert that you are correct.
            $ macHope += 1
            $ reactTarget = "vig3_sc14_recfindsout_regret"
            mS "After he fixed MAC, we brought him to the ship."
            mS "He was trying to take MAC."
            mS "I was scared. Scared of this."
            mS "And I think he was too."
            mS "I didn't want to."
            $ AddChatter(vig3_sc14_justhappened_comment1)
            pause 0.5
            $ AddChatter(vig3_sc14_justhappened_comment2)
            "Tears are streaming down Rec's face." 
            $ AddChatter(vig3_sc14_justhappened_comment3)
            recS "So, why?"
            mS "It just happened. Before I realized what I had done... He was on the ground."
            $ AddChatter(vig3_sc14_justhappened_comment4)
            mS "I'm so sorry, Rec."
            $ AddChatter(vig3_sc14_justhappened_comment5)
            mS "I know it doesn't mean anything right now, but I'm sorry."
            "There's a long moment where Rec just looks at us."
            $ AddChatter(vig3_sc14_justhappened_comment6)
            pause 0.5
            $ AddChatter(vig3_sc14_justhappened_comment7)
            "But they say nothing."
            $ AddChatter(vig3_sc14_justhappened_comment5)
            "We stand there in stasis as the shuttle reaches Akar."
            show screen streamerCommentary
            $ AddChatter(vig3_sc14_justhappened_comment8)
            pause 0.5
            $ AddChatter(vig3_sc14_justhappened_comment9)
            "Teresa and Jennica don't turn to them, still fixed on Ama."
            $ AddChatter(vig3_sc14_justhappened_comment10)
            "Her grip is unwavering."
            $ AddChatter(vig3_sc14_justhappened_comment11)
            pause 0.5
            $ AddChatter(vig3_sc14_justhappened_comment12)
            "MAC clings to Teresa."
            "Then an announcement."
            "Final stop: Akar station."
            play audio "door.wav" volume 1.5
            "The shuttle doors open. Reccrin walks out and out of sight."
            hide rec with Dissolve(2.0)
            $ AddChatter(vig3_sc14_justhappened_comment13)
            show ama stream formal smug
            amaS "How disappointing, Allistar was a talented kid."
            "Ama looks to Teresa and Jennica."
            "Ama takes the knife off my neck. And shoves me into the group."
            "We fall out of the shuttle and onto the platform."
            amaS "Let's finish this later, shall we?"
            play audio "door.wav" volume 2.0
            "We don't move as the doors shut in front of us."
            play audio "shipFlyBy.wav" volume 2.0
            "Then the shuttle tears out of sight and returns to the Vineyard."
            hide ama with dissolve
            "For a moment we stand on the empty platform."
            "Unsure how to continue."
            show mac stream neutral at stream_center_mac with dissolve
            play audio "macSad.wav" volume 1.2
            macS "Captain?"
            mS "Yes, MAC."
            macS "Will Rec be okay?"
            mS "I don't know."
            macS "Should we go after them?"
            mS "No, kid. There's nothing we can do."
            macS "Are you okay?"
            mS "I—"
            hide mac with dissolve

        "I did what I had to do.":
            $ vig3_recResponse = "Classic"
            $ engineerApproval += 2 #Logic: I think Teresa agrees with this line. Utilitarianism and all that
            $ pdEngagement -= 2 #Logic: pd doesn't like this excuse
            $ csEngagement += 1
            $ kcEngagement += 3 #Logic: kitcat might legit feel like you didn't have a choice: MAC was threatened after all
            #I feel like Ama would be neutral on this front
            $ setEngagement()
            $ macViolence += 1
            $ macPessimism += 2
            $ reactTarget = "vig3_sc14_recfindsout_ihadto"
            $ AddChatter(vig3_sc14_hadto_comment1)
            mS "After he fixed MAC, we brought him to the ship."
            $ AddChatter(vig3_sc14_hadto_comment2)
            mS "He was trying to take MAC."
            mS "I found him trying to take an escape pod."
            mS "MAC is so important, too important."
            $ AddChatter(vig3_sc14_hadto_comment3)
            pause 0.5
            $ AddChatter(vig3_sc14_hadto_comment4)
            pause 0.5
            $ AddChatter(vig3_sc14_hadto_comment5)
            mS "I couldn't let him leave, I did what—"
            recS "Bullshit!"
            "Tears are pouring from Rec's eyes."
            recS "Know who else is important? {i}My little brother!{/i}"
            $ AddChatter(vig3_sc14_hadto_comment6)
            pause 0.5
            $ AddChatter(vig3_sc14_hadto_comment7)
            "I see MAC clutch Jennica's leg"
            recS "You didn't have to do anything."
            recS "You screwed up and needed an easy way to be bailed out."
            $ AddChatter(vig3_sc14_hadto_comment8)
            pause 0.5
            $ AddChatter(vig3_sc14_hadto_comment9)
            show rec stream formal angry at stream_left5 with move
            show teresa stream neutral at stream_center with vpunch
            $ AddChatter(vig3_sc14_hadto_comment10)
            "Rec lunges for me and is caught by Teresa."
            $ AddChatter(vig3_sc14_hadto_comment11)
            enS "Calm down!"
            $ AddChatter(vig3_sc14_hadto_comment12)
            pause 0.5
            $ AddChatter(vig3_sc14_hadto_comment13)
            recS "I won't calm down! You killed him!"
            recS "You all killed him!"
            $ AddChatter(vig3_sc14_hadto_comment14)
            "Rec attempts to fight their way to me, but is subdued."
            "Then an announcement."
            "Final stop: Akar station."
            play audio "door.wav" volume 1.5
            "When the doors open, Teresa pushes Rec out onto the platform."
            show rec stream formal angry at stream_left with vpunch
            recS "Fine! I'm not going to stick around for this."
            recS "I hope it was all worth it!"
            "They turn to walk away."
            hide rec with Dissolve(2.0)
            show screen streamerCommentary
            show ama stream formal smug
            amaS "How disappointing, Allistar was a talented kid."
            "Ama looks to Teresa and Jennica."
            "Ama takes the knife off my neck. And shoves me into the group."
            "We fall out of the shuttle and onto the platform."
            amaS "Let's finish this later, shall we?"
            play audio "door.wav" volume 1.5
            "We don't move as the doors shut in front of us."
            play audio "shipFlyBy.wav" volume 2.0
            "Then the shuttle tears out of sight and returns to the Vineyard."
            hide ama with dissolve
            "For a moment we stand on the empty platform."
            "Unsure how to continue."
            hide mac with dissolve


        "I did it because he deserved it.":
            $ vig3_outlaw += 1
            $ vig3_recResponse = "Justified"
            $ pilotApproval -= 1 #Logic: I think both crew members would be stunned by this. They'll stand by their captain, but I don't think they believe Allistar deserved it.
            $ engineerApproval -= 1
            $ pdEngagement += 3 #Logic: pd loves this attitude; the other two liked Allistar
            $ csEngagement -= 2
            $ kcEngagement -= 1
            $ setEngagement()
            $ deadeyeApproval += 2
            $ macViolence += 3
            $ macPessimism += 3
            $ reactTarget = "vig3_sc14_recfindsout_noremorse"
            $ AddChatter(vig3_sc14_deservedit_comment1)
            pause 0.5
            $ AddChatter(vig3_sc14_deservedit_comment2)
            mS "After he fixed MAC, we brought him to the ship."
            mS "He was trying to take MAC."
            mS "We trusted him."
            $ AddChatter(vig3_sc14_deservedit_comment3)
            pause 0.5
            $ AddChatter(vig3_sc14_deservedit_comment4)
            mS "I saw him with MAC at the escape pods, and I realized what he was trying to do."
            $ AddChatter(vig3_sc14_deservedit_comment5)
            "The blade cuts into my neck as I make sure to look Rec in the eyes."
            $ AddChatter(vig3_sc14_deservedit_comment6)
            "I can hear Ama chuckle under her breath."
            $ AddChatter(vig3_sc14_deservedit_comment7)
            mS "I killed Allistar, and that spineless traitor got exactly what he deserved!"
            show ama stream formal shocked
            $ AddChatter(vig3_sc14_deservedit_comment8)
            pause 0.5
            $ AddChatter(vig3_sc14_deservedit_comment9)
            $ AddChatter(vig3_sc14_deservedit_comment10)
            "Teresa and Jennica almost lose their sights on Ama."
            $ AddChatter(vig3_sc14_deservedit_comment11)
            "MAC stays there, motionless."
            $ AddChatter(vig3_sc14_deservedit_comment12)
            "Behind him is Rec. Face like they took a bullet to the gut."
            recS "You..."
            $ AddChatter(vig3_sc14_deservedit_comment13)
            "Tears pour down his face."
            enS "Moze..."
            pS "You're not serious..."
            $ AddChatter(vig3_sc14_deservedit_comment14)
            mS "What? You think being in this position is easy?"
            mS "You think I like making the hard calls?"
            mS "Allistar knew the risk, and got what was coming."
            $ AddChatter(vig3_sc14_deservedit_comment15)
            mS "I'd do it all again if I had to."
            $ AddChatter(vig3_sc14_deservedit_comment16)
            "They look at me and Ama."
            recS "You two deserve each other."
            $ AddChatter(vig3_sc14_deservedit_comment17)
            play audio "lazer.wav" volume 5.0
            "Rec grabs the blaster off Teresa and fires a shot."
            show jennica stream fight at stream_center with vpunch
            "With a quick move from Jennica the bullet hits the shuttle ceiling."
            show rec with vpunch
            show jennica with vpunch
            "She tackles them to the ground."
            show screen streamerCommentary
            "Then an announcement."
            "Final stop: Akar station."
            hide jennica with Dissolve(0.5)
            play audio "door.wav" volume 1.5
            "When the doors open, Jennica lets go of Rec."
            "They run out of the shuttle doors onto the platform. And out of sight."
            hide rec with Dissolve(2.0)
            show ama stream formal smug
            "Ama leans in close."
            amaS "That was cold Mozely, even for me."
            "Ama takes the knife off my neck. And shoves me into the group."
            "We fall out of the shuttle and onto the platform."
            amaS "Let's finish this later, shall we?"
            play audio "door.wav" volume 2.0
            "We don't move as the doors shut in front of us."
            play audio "shipFlyBy.wav" volume 2.0
            "Then the shuttle tears out of sight and returns to the Vineyard."
            hide ama with dissolve
            "We're left on the platform."
            "My crew can barely look at me."
            mS "Everyone, I—"
            hide mac with dissolve
    hide exteriorvineyard_stream with Dissolve(1.5)
    jump vig3_epilogue

label vig3_epilogue():
    $ viewCheck10 = viewCount
    stop music fadeout 4.0
    hide screen streamerCommentary
    show akarstreet_stream at topleft onlayer background with Dissolve(1.5)
    #hide exteriorvineyard_stream
    "The Vineyard is alight with fireworks in the distance."
    $ AddChatter(vig3_epilogue_comment1)
    "The screens on the platform end their ads and a live feed begins."
    $ AddChatter(vig3_epilogue_comment2)
    "Reynar is there, on his balcony, addressing the crowd of patrons."
    show reynar stream neutral at stream_center with dissolve
    $ AddChatter(vig3_epilogue_comment3)
    reynar "Good evening, everyone!"
    $ AddChatter(vig3_epilogue_comment4)
    reynar "Thank you once again for offering your time, your knowledge, and your passion to our Fair."
    $ AddChatter(vig3_epilogue_comment5)
    pause 0.5
    $ AddChatter(vig3_epilogue_comment6)
    reynar "Your presence here is a testament to our ongoing commitment to make the Outposts a better and brighter place."
    $ AddChatter(vig3_epilogue_comment7)
    $ AddChatter(vig3_epilogue_comment8)
    pause 0.5
    $ AddChatter(vig3_epilogue_comment9)
    reynar "I applaud each and every one of you."
    reynar "Your choices..."
    reynar "Shape our future."
    reynar "Don't ever lose sight of what we're working towards."
    reynar "So let's raise a glass in celebration."
    show reynar stream gatsby at stream_center
    reynar "To the Outposts!"
    "Reynar looks dead at the camera, at us."
    $ AddChatter(vig3_epilogue_comment10)
    "Cheering explodes in the background."
    $ AddChatter(vig3_epilogue_comment11)
    "He raises his glass."
    $ AddChatter(vig3_epilogue_comment12)
    "The fireworks dance in the night sky."
    $ AddChatter(vig3_epilogue_comment13)
    "And I remember what he left in my pocket."
    hide reynar with dissolve
    hide akarstreet_stream with dissolve
    show shiphub_stream at topleft onlayer background with dissolve
    $ AddChatter(vig3_epilogue_comment14)
    play audio "shipWarmUp.wav" volume 2.0
    "Teresa outfits the Oakley best she can."
    "And with Reynar's gift, we get access to fly the Oakley out through restricted sky."
    $ AddChatter(vig3_epilogue_comment15)
    "Which gives us time."
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment16)
    "At least..."
    "But the Oakley is silent."
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment17)
    play music "soundtrack/theme.wav" fadein 4.0
    "For days it goes on like that, no one knowing how to talk about the dark cloud over us."
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment18)
    "Rec refuses to answer Jenn or Teresa's transmissions."
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment19)
        pause 0.5
        $ AddChatter(vig3_epilogue_comment20)
    "MAC has been silent, spending most of his time alone."
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment21)
    play audio "callRing.wav" volume 1.0
    "Then the Dragonfly transmission comes through."
    $ AddChatter(vig3_epilogue_comment22)
    pause 0.5
    $ AddChatter(vig3_epilogue_comment23)
    "The line is filled with static that distorts the voice, but we're able to make out the information." #Setting up that Coil's voice is distorted so they wouldn't recognize him immediately
    show teresa stream neutral at stream_right with dissolve
    show jennica stream neutral at stream_left with dissolve
    show mac stream neutral at stream_center_mac with dissolve
    $ AddChatter(vig3_epilogue_comment24)
    dflycontact "Captain Moze of the Oakley this is Dr. Coil of the Dragonflies."
    dflycontact "I hear you are in possession of Dr. Vanas' work."
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment25)
    dflycontact "We are contacting you regarding the drop off point."
    $ AddChatter(vig3_epilogue_comment26)
    #dflycontact "We are stationed at a planet known as Polaris." #They don't know about Polaris when they first show up to it in Vignette 4. But they have the coordinates, so I just commented this out.
    dflycontact "Brevifolia Sector. Coordinates 11 03 7."
    dflycontact "This is the last attempt. Should this message be lost, then so is our hope."
    play audio "cutCall.wav" volume 1.5
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment27)
    "The transmission ends."
    if viewershipHigh == True:    
        $ AddChatter(vig3_epilogue_comment28)
    mS "Jenn?"
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment29)
        pause 0.5
        $ AddChatter(vig3_epilogue_comment30)
        pause 0.5
        $ AddChatter(vig3_epilogue_comment31)
    pS "On it, Cap."
    mS "Thank you, I'll be in my quarters."
    hide jennica with dissolve
    hide teresa with dissolve
    hide mac with dissolve
    show ship_hallway_stream at topleft onlayer background with dissolve
    hide shiphub_stream with dissolve
    #Make this longer#
    "As I walk down the hall, I try to take stock of everything."
    menu:
        "How do you feel?"
        "Happy to have survived.":
            $ AddChatter(vig3_happy_comment1)
            pause 0.5
            $ AddChatter(vig3_happy_comment2)
            "This was supposed to be a simple pick up."
            $ AddChatter(vig3_happy_comment3)
            "Maybe even a break."
            $ AddChatter(vig3_happy_comment4)
            "Now I'm just happy to have made it through in one piece."
        "Guilty.":
            $ AddChatter(vig3_guilty_comment1)
            "I can't imagine what Rec is feeling."
            if viewershipHigh == True:
                $ AddChatter(vig3_guilty_comment2)
            "I meant what I said."
            if viewershipHigh == True:
                $ AddChatter(vig3_guilty_comment3)
            "I just feel like we could've done more for them."
            if viewershipHigh == True:
                $ AddChatter(vig3_guilty_comment4)
        "Tired.":
            $ AddChatter(vig3_tired_comment1)
            "Everyday has been such a weight."
            $ AddChatter(vig3_tired_comment2)
            "It's almost over."
            $ AddChatter(vig3_tired_comment3)
            "One final push." 

    "The walk to my quarters is long."
    "Then I'm intercepted."
    show mac stream neutral at stream_center_mac with dissolve
    "By MAC."
    $ AddChatter(vig3_epilogue_comment32)
    "We stare at each other in silence."
    "I don't know what to say."
    "We just look at each other."
    "I lower myself to his eye level."
    "He rolls towards me."
    play audio "macComfort.wav" volume 1.5
    "And hugs me."
    $ AddChatter(vig3_epilogue_comment33)
    "And we stay there for sometime."
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment34)
    pause 0.5
    $ AddChatter(vig3_epilogue_comment35)
    play audio "shipWarmUp.wav" volume 2.0
    "The ship hums as it picks up speed."
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment36)
        pause 0.5
        $ AddChatter(vig3_epilogue_comment37)
        pause 0.5
        $ AddChatter(vig3_epilogue_comment38)
        pause 0.5
        $ AddChatter(vig3_epilogue_comment39)
        pause 0.5
        $ AddChatter(vig3_epilogue_comment40)
    play audio "enterHyperspace.wav" volume 2.0
    "And the Oakley presses forward, as it always does."
    stop music fadeout 4.0
    hide mac with Dissolve(1.0)
    show bg black onlayer background with dissolve
    hide ship_hallway_stream
    $ AddChatter(vig3_epilogue_comment41)
    pause 0.5
    $ narrator = reg_narrator
    player "Alright, everyone, looks like that's the end of the episode."
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment42)
    player "Next week we've got the fourth and {i}final{/i} episode of {i}Oakley 2{/i}."
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment43)
    player "So be sure to swing by, and join us for a big finale!"
    $ AddChatter(vig3_epilogue_comment44)
    pause 0.5
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment45)
        pause 0.5
    $ AddChatter(vig3_epilogue_comment46)
    pause 0.5
    if viewershipHigh == True:
        $ AddChatter(vig3_epilogue_comment47)
        pause 0.5
        $ AddChatter(vig3_epilogue_comment48)
        pause 0.5
    "The chat slowly dies down as you close the stream."
    hide screen streamChat
    hide screen streamDetails
    scene black with dissolve
    pause 1.0
    jump vig3_macro_start

label vig3_macro_start():
    nvl clear
    $ vignette3 = True
    if csEngagement > pdEngagement and csEngagement > kcEngagement:
        $ topfan = "Coriolis"
    elif kcEngagement > pdEngagement and kcEngagement >= csEngagement:
        $ topfan = "kitcat"
    elif pdEngagement >= kcEngagement and pdEngagement >= csEngagement:
        $ topfan = "pickledDragons"
    else:
        $ topfan = "Coriolis"
    if vig3_interactions >= 14:
        $ flinch_followership -= 3
    elif vig3_interactions >= 9:
        $ flinch_followership -= 2
    else:
        $ flinch_followership -= 1
    play music "soundtrack/postStreamGroove.wav" volume 0.8 loop fadein 2.0
    $ narrator = reg_narrator
    #$ macroNarration = True
    $ macroChoice = True
    "You lean back in your chair and let your body relax now that you're no longer on camera."
    $ renpy.sound.play("audio/ReceiveText.ogg")
    "Then you get a Loop'd notification."
    scene discordview with dissolve
    "It's from Jessie. You should see what's up."
    jump vig3_macro_mod_1

label vig3_macro_mod_1():
    nvl clear
    $ menu = nvl_menu
    mod_nvl "Yoyoyo!"
    mod_nvl "Another great stream!" 
    if viewershipHigh == True:
        mod_nvl "The viewership numbers were crazy"
        mod_nvl "I wouldn't be surprised if we already hit all the marks to make Affiliate!"
        menu:
            "•You think so??":
                player_nvl "You think I made it already?"
                mod_nvl "Maybe! It was a lot of people"
                mod_nvl "Check your analytics on Flinch and let me know"
                mod_nvl "I guess you still have to do one more stream technically, but that might be a formality at this point"
            "•I still have to do one more stream.":
                player_nvl "Maybe in terms of analytics, but I have to stream at least one more time next week to officially make it"
                mod_nvl "True. But even then, at least you know it's pretty much a formality"
    else:
        mod_nvl "No growth in viewership from the previous stream" #Maybe cause you went a little too Marshal in Episode 2."
        mod_nvl "But it was still good numbers" 
        mod_nvl "As long as you don't lose anyone from this week to next, you should be all set!"
        menu:
            "•You think we'll make it?":
                player_nvl "Do you really think we'll make it to where we need to go?"
                mod_nvl "Oh yeah"
                mod_nvl "I mean, I've believed in you since I started modding for your stream"
                mod_nvl "Why stop now?"
                player_nvl "Thanks, Jessie"
                mod_nvl "Of course"
                mod_nvl "You still have time. Trust me"
            "•I'm feeling confident.":
                player_nvl "I feel good about our chances too"
                player_nvl "I know the numbers dipped from when I streamed Episode 2, but I think the crew that's there is in it for the long haul"
                mod_nvl "You got a lot of friendly voices in the chat"
                mod_nvl "Not every streamer can say that"
            "•I'm feeling nervous.":
                player_nvl "I don't know, I'm feeling nervous about the last stream"
                player_nvl "What if I don't make it?"
                mod_nvl "Well then the world ends and we go hide out in a fallout bunker"
                player_nvl "Jessie"
                mod_nvl "lol sorry, bad joke"
                mod_nvl "It's gonna be ok either way."
                mod_nvl "But you still have time. Trust me"
    mod_nvl "Alright, I don't have a ton of time, but I wanted to say you did a great job dealing with the crash!"
    menu:
        "•I was so stressed out!":
            player_nvl "Oh my god that stressed me out so much!"
            player_nvl "I'm like shocked the chat didn't abandon me"
            mod_nvl "Just goes to show the kind of vibe you cultivated!"
        "•I felt weirdly calm.":
            player_nvl "It's weird, in the past that kind of stuff really rattled me"
            player_nvl "But this time I just felt really calm"
            mod_nvl "Interesting. Guess you're still getting better at this stuff!"
        "•It happens.":
            player_nvl "You stream enough times, you get used to technical difficulties. It happens"
            mod_nvl "I mean, still, you handled it like a pro!"
    mod_nvl "Ok, gotta run and grab some udon"
    mod_nvl "Have a good night! So excited for the last episode!"
    menu:
        "•Take care!":
            player_nvl "Thanks, Jessie! You take care!"
    jump vig3_macro_webNav

label vig3_macro_webNav():
    nvl clear
    $ menu = adv_menu
    $ renpy.sound.play("audio/ReceiveText.ogg")
    "You're about to sign off Loop'D when you get another notification."
    #scene streamview with dissolve
    if topfan == "Coriolis":
        "It's from Coriolis."
    elif topfan == "kitcat":
        "It's from kitcat."
    elif topfan == "pickledDragons":
        "It's from pickledDragons."
    else:
        "It's from Coriolis."
    "You should see what they have to say, and check on Flinch and blueit."
    $ screenComplete = True
    call screen webNavigation_vig3

label vig3_macro_viewerChat_1():
    nvl clear
    scene discordview with dissolve
    $ screenComplete = False
    $ loopdView = True
    $ menu = nvl_menu
    if topfan == "Coriolis": #Coriolis Convo
        #Coriolis convo about Rec
        "Coriolis sent me a message on Loop'd."
        cs_nvl "Hey, [username], wanted to say thanks for a great stream!"
        cs_nvl "It was really fun to get to meet so many different characters. They were all cool, but I think Rec was my favourite"
        cs_nvl "It sucks how we had to break their heart in the end. Just wanted to see how you're feeling about that moment"
        if vig3_recResponse == "Confused":
            cs_nvl "I was kind of surprised that you had Moze say she was confused about killing Allistar"
            $ playerNVLNarration = "Coriolis asked my feelings about Rec. Should I respond?"
            show screen NVLnarration
            menu:
                "•It reflected how I felt as a player.":
                    hide screen NVLnarration
                    $ csEngagement += 1
                    $ setEngagement()
                    player_nvl "I made that choice cause it was what I felt the most in that moment"
                    player_nvl "I wasn't expecting it and it was so tense"
                    if misclick == True:
                        cs_nvl "Right, I remember you said you didn't even mean to do it, right? Like it was a misclick?"
                        player_nvl "Yeah. So that choice just felt like what my actual response was"
                    else:
                        pass
                    player_nvl "It may not have been the most fun or the most sincere from Moze's perspective, but it was what I felt as a player"
                    cs_nvl "That makes a lot of sense, I appreciate how much thought you put into these choices"
                    cs_nvl "So many of them seem really tough"
                    menu:
                        "•Yeah, they're hard to make.":
                            player_nvl "Yeah, I don't think it ever gets easier tbh"
                            player_nvl "Like, don't get me wrong, it's still a game"
                            player_nvl "But when you're really connected to these characters, it's always kinda tense when you're deciding their fates"
                            cs_nvl "Seriously, it's why I don't play these kinda games on my own really. So much pressure haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•It's actually getting easier.":
                            player_nvl "I used to be more stressed out about the decisions, but they've gotten easier to make recently"
                            player_nvl "Maybe it's just how many of these games I've played. I've learned not to stress about them too much"
                            player_nvl "And that makes it more fun to experiment with different kinds of chocies"
                            cs_nvl "That's a really cool perspective!"
                            cs_nvl "I could never, making these kinds of choices always stresses me out too much haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat, [username]! See you next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with Coriolis for a bit."
                "•It felt the most honest from Moze.":
                    hide screen NVLnarration
                    $ csEngagement += 1
                    $ setEngagement()
                    player_nvl "I know it seems odd, but I think it was the most honest response from Moze"
                    player_nvl "I feel like even she doesn't know why she did it, especially since she could so easily have stunned Allistar"
                    player_nvl "I mean, I'm thinking like in terms of her character and less myself. But I think that's fun to explore"
                    player_nvl "Here's this character who puts on the air of the confident Captain, but maybe she's insecure and confused a lot of the time too"
                    cs_nvl "Ooh interesting. I really like that take!"
                    cs_nvl "And I appreciate how much thought you put into these choices"
                    cs_nvl "So many of them seem really tough"
                    menu:
                        "•Yeah, they're hard to make.":
                            player_nvl "Yeah, I don't think it ever gets easier tbh"
                            player_nvl "Like, don't get me wrong, it's still a game"
                            player_nvl "But when you're really connected to these characters, it's always kinda tense when you're deciding their fates"
                            cs_nvl "Seriously, it's why I don't play these kinda games on my own really. So much pressure haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•It's actually getting easier.":
                            player_nvl "I used to be more stressed out about the decisions, but they've gotten easier to make recently"
                            player_nvl "Maybe it's just how many of these games I've played. I've learned not to stress about them too much"
                            player_nvl "And that makes it more fun to experiment with different kinds of chocies"
                            cs_nvl "That's a really cool perspective!"
                            cs_nvl "I could never, making these kinds of choices always stresses me out too much haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with Coriolis for a bit."
                "•Don't respond.":
                    hide screen NVLnarration
                    $ csEngagement -= 2
                    $ setEngagement()
                    "Nah, don't really want to encourage a parasocial relationship."
        elif vig3_recResponse == "Classic":
            cs_nvl "I thought the attempt to use Moze's classic line made sense, and I liked how Rec called her on that"
            $ playerNVLNarration = "Coriolis asked my feelings about Rec. Should I respond?"
            show screen NVLnarration
            menu:
                "•It's a story Moze has to believe in.":
                    hide screen NVLnarration
                    player_nvl "Yeah, I agree, I think this whole \"I didn't have a choice\" thing is just a story Moze keeps telling herself"
                    player_nvl "It's how she copes with having to deal with the darkness of this galaxy. But it's not the reality"
                    player_nvl "It also closes the loop on Allistar's death in a really impactful way. I'm glad they brought Rec back for this episode"
                    cs_nvl "Yeah me too. I feel like it's so easy to fall into the \"I didn't have a choice\" mentality"
                    cs_nvl "I don't like what Moze did, but I do feel for her"
                    cs_nvl "And I appreciate how much thought you put into these choices"
                    cs_nvl "So many of them seem really tough"
                    menu:
                        "•Yeah, they're hard to make.":
                            player_nvl "Yeah, I don't think it ever gets easier tbh"
                            player_nvl "Like, don't get me wrong, it's still a game"
                            player_nvl "But when you're really connected to these characters, it's always kinda tense when you're deciding their fates"
                            cs_nvl "Seriously, it's why I don't play these kinda games on my own really. So much pressure haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•It's actually getting easier.":
                            player_nvl "I used to be more stressed out about the decisions, but they've gotten easier to make recently"
                            player_nvl "Maybe it's just how many of these games I've played. I've learned not to stress about them too much"
                            player_nvl "And that makes it more fun to experiment with different kinds of chocies"
                            cs_nvl "That's a really cool perspective!"
                            cs_nvl "I could never, making these kinds of choices always stresses me out too much haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with Coriolis for a bit."
                "•I don't think Moze had choice.":
                    hide screen NVLnarration
                    player_nvl "I really don't think Moze had a choice. I mean, technically she did, but it's more complicated than that"
                    player_nvl "Maybe she stuns Allistar and he gets some time to come around and isn't a threat to the crew after that point"
                    player_nvl "But could Moze really have taken that risk?"
                    player_nvl "I don't know that she would have. And I think it's interesting to explore this character who has such a black and white outlook on that kind of thing"
                    cs_nvl "Hmmm I see what you're saying"
                    cs_nvl "I think I still agree with Rec (and Allistar), but it's a good point. Moze is put in a LOT of tough situations"
                    cs_nvl "And I appreciate how much thought you put into these choices"
                    cs_nvl "So many of them seem really tough"
                    menu:
                        "•Yeah, they're hard to make.":
                            player_nvl "Yeah, I don't think it ever gets easier tbh"
                            player_nvl "Like, don't get me wrong, it's still a game"
                            player_nvl "But when you're really connected to these characters, it's always kinda tense when you're deciding their fates"
                            cs_nvl "Seriously, it's why I don't play these kinda games on my own really. So much pressure haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•It's actually getting easier.":
                            player_nvl "I used to be more stressed out about the decisions, but they've gotten easier to make recently"
                            player_nvl "Maybe it's just how many of these games I've played. I've learned not to stress about them too much"
                            player_nvl "And that makes it more fun to experiment with different kinds of chocies"
                            cs_nvl "That's a really cool perspective!"
                            cs_nvl "I could never, making these kinds of choices always stresses me out too much haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with Coriolis for a bit."
                "•Don't respond.":
                    hide screen NVLnarration
                    $ csEngagement -= 2
                    $ setEngagement()
                    "Nah, don't really want to encourage a parasocial relationship."
        else:
            cs_nvl "I'll be honest, I thought it was harsh the way Moze was so adamant about justifying it"
            $ playerNVLNarration = "Coriolis asked my feelings about Rec. Should I respond?"
            show screen NVLnarration
            menu:
                "•It was harsh but true.":
                    hide screen NVLnarration
                    $ csEngagement -= 1
                    $ setEngagement()
                    player_nvl "It was harsh, but it was true"
                    player_nvl "I feel like saying any of the other options just wasn't being honest to Rec"
                    player_nvl "Like, straight up, Allistar betrayed our trust. That has to have consequences"
                    player_nvl "And I'd rather be direct with Rec than try to sugarcoat the trauma"
                    cs_nvl "No I get that... I guess I just didn't read that in Moze's character"
                    if misclick == True:
                        cs_nvl "And I guess I'm kind of surprised considering you said it was a misclick originally"
                        player_nvl "That's fair, but I've had time to think about it and I think it makes sense for her character"
                    cs_nvl "It's not what I would have done, but I see your perspective"
                    cs_nvl "And I appreciate how much thought you put into these choices"
                    cs_nvl "So many of them seem really tough"
                    menu:
                        "•Yeah, they're hard to make.":
                            player_nvl "Yeah, I don't think it ever gets easier tbh"
                            player_nvl "Like, don't get me wrong, it's still a game"
                            player_nvl "But when you're really connected to these characters, it's always kinda tense when you're deciding their fates"
                            cs_nvl "Seriously, it's why I don't play these kinda games on my own really. So much pressure haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•It's actually getting easier.":
                            player_nvl "I used to be more stressed out about the decisions, but they've gotten easier to make recently"
                            player_nvl "Maybe it's just how many of these games I've played. I've learned not to stress about them too much"
                            player_nvl "And that makes it more fun to experiment with different kinds of chocies"
                            cs_nvl "That's a really cool perspective!"
                            cs_nvl "I could never, making these kinds of choices always stresses me out too much haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with Coriolis for a bit."
                "•It surprised me too.":
                    hide screen NVLnarration
                    player_nvl "I wasn't expecting it to be that harsh either tbh"
                    player_nvl "The thing that got me was the looks from the crew after Moze admitted it"
                    player_nvl "Like, I didn't want to try to sugarcoat it to Allistar... but damn"
                    cs_nvl "Yeah, she really tore into his memory. Feel like there's no way Rec ever speaks to us again"
                    player_nvl "No chance"
                    cs_nvl "I appreciate how much thought you put into these choices"
                    cs_nvl "So many of them seem really tough"
                    menu:
                        "•Yeah, they're hard to make.":
                            player_nvl "Yeah, I don't think it ever gets easier tbh"
                            player_nvl "Like, don't get me wrong, it's still a game"
                            player_nvl "But when you're really connected to these characters, it's always kinda tense when you're deciding their fates"
                            cs_nvl "Seriously, it's why I don't play these kinda games on my own really. So much pressure haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•It's actually getting easier.":
                            player_nvl "I used to be more stressed out about the decisions, but they've gotten easier to make recently"
                            player_nvl "Maybe it's just how many of these games I've played. I've learned not to stress about them too much"
                            player_nvl "And that makes it more fun to experiment with different kinds of chocies"
                            cs_nvl "That's a really cool perspective!"
                            cs_nvl "I could never, making these kinds of choices always stresses me out too much haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with Coriolis for a bit."
                "•Don't respond.":
                    hide screen NVLnarration
                    $ csEngagement -= 2
                    $ setEngagement()
                    "Nah, don't really want to encourage a parasocial relationship."

    elif topfan == "kitcat": #kitcat Convo
        "kitcat sent me a message on Loop'd."
        kc_nvl "Heya, [username]! Wanted to say thanks for the awesome stream!"
        kc_nvl "It was really cool getting to see the Oakley on their home turf"
        kc_nvl "But omg, we have to talk about MAC picking up that gun!"
        if vig3_macAlign == "ViolentPessimism":
            kc_nvl "I can't BELIEVE MAC shot Ama!"
            kc_nvl "I mean, I heard people say that your choices affect him and his behavior, but I never thought he'd actually hurt someone"
            kc_nvl "If I'm being honest, I don't know how I feel about it..."
            $ playerNVLNarration = "kitcat's talking about MAC's growth in the game. Should I respond?"
            show screen NVLnarration
            menu:
                "•I thought it was great!":
                    hide screen NVLnarration
                    $ kcEngagement += 1
                    $ setEngagement()
                    player_nvl "That scene was so crazy!"
                    player_nvl "I get what you're saying, but I think it makes a lot of sense for his character and this universe"
                    player_nvl "We've had to do a lot of not great things just to survive"
                    player_nvl "And Moze might not be around him forever. If he's gonna make it in this galaxy, he has to learn to survive on his own as well"
                    player_nvl "I thought it was a great scene for him!"
                    kc_nvl "No, you're right"
                    kc_nvl "Idk, I guess I was just hoping he could find a way above all the dirt and grime"
                    kc_nvl "Don't get me wrong though, absolutely loved seeing him take a more active role!"
                    kc_nvl "The bit about him \"disposing\" of the other prototype? So funny haha"
                    menu:
                        "•That part got me too!":
                            player_nvl "I almost lost it there too! MAC learning the subtle art of euphemisms haha"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•I thought it was going to be a lot worse.":
                            player_nvl "I know right? I thought for sure he was gonna mention an incinerator or something haha"
                            kc_nvl "Omg, can you imagine?"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with kitcat for a bit."
                "•I'm also conflicted.":
                    hide screen NVLnarration
                    $ kcEngagement += 2
                    $ setEngagement()
                    player_nvl "I see where you're coming from. I'm also feeling a bit conflicted about it"
                    player_nvl "Like, the galaxy is a tough place, and he has to know how to survive"
                    player_nvl "But is him becoming just like Moze really the best thing?"
                    player_nvl "Idk, it's a tough line to walk"
                    kc_nvl "Definitely. And I'll be honest, I'm glad I don't have to worry about walking that line haha"
                    kc_nvl "Appreciate you making the tough calls for us, Cap!"
                    kc_nvl "Don't get me wrong though, absolutely loved seeing him take a more active role!"
                    kc_nvl "The bit about him \"disposing\" of the other prototype? So funny haha"
                    menu:
                        "•That part got me too!":
                            player_nvl "I almost lost it there too! MAC learning the subtle art of euphemisms haha"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•I thought it was going to be a lot worse.":
                            player_nvl "I know right? I thought for sure he was gonna mention an incinerator or something haha"
                            kc_nvl "Omg, can you imagine?"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with kitcat for a bit."
                "•Don't respond.":
                    hide screen NVLnarration
                    $ kcEngagement -=3
                    $ setEngagement()
                    "Nah, don't really want to encourage a parasocial relationship."
        elif vig3_macAlign == "ViolentHope":
            kc_nvl "What a great move by him! Taking a shot to distract Ama so you could get the upperhand!"
            kc_nvl "Tbh, I was kinda nervous he was actually gonna shoot her there and I really don't know how I would have felt about that"
            kc_nvl "He's our lil guy, glad to know he's not turning into a murder bot, y'know?"
            $ playerNVLNarration = "kitcat's talking about MAC's growth in the game. Should I respond?"
            show screen NVLnarration
            menu:
                "•I was nervous about that too.":
                    hide screen NVLnarration
                    $ kcEngagement += 2
                    $ setEngagement()
                    player_nvl "I totally agree, thought that move by him was super fun!"
                    player_nvl "I was also holding my breath in that moment. Seriously didn't know which way it was gonna go"
                    player_nvl "Glad he didn't shoot her. I know MAC has to learn how to survive in this galaxy, but him knowing the difference between survival and cruelty feels pretty important"
                    kc_nvl "Exactly! Yeah I feel the same way. Great way of putting it!"
                    kc_nvl "Don't get me wrong though, absolutely loved seeing him take a more active role!"
                    kc_nvl "The bit about him \"disposing\" of the other prototype? So funny haha"
                    menu:
                        "•That part got me too!":
                            player_nvl "I almost lost it there too! MAC learning the subtle art of euphemisms haha"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•I thought it was going to be a lot worse.":
                            player_nvl "I know right? I thought for sure he was gonna mention an incinerator or something haha"
                            kc_nvl "Omg, can you imagine?"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with kitcat for a bit."
                "•I kind of wish he'd hit Ama.":
                    hide screen NVLnarration
                    $ kcEngagement += 1
                    $ setEngagement()
                    player_nvl "I actually kind of wish he'd taken a shot at her"
                    player_nvl "I mean, I do like him going for a less harmful maneuver. But that's not always going to be an option"
                    player_nvl "Moze might not be around to keep him safe forever. Eventually, he's going to have to make these tough calls for himself"
                    kc_nvl "I see that. I guess I just don't want him to have to grow up that fast"
                    kc_nvl "Don't get me wrong though, absolutely loved seeing him take a more active role!"
                    kc_nvl "The bit about him \"disposing\" of the other prototype? So funny haha"
                    menu:
                        "•That part got me too!":
                            player_nvl "I almost lost it there too! MAC learning the subtle art of euphemisms haha"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•I thought it was going to be a lot worse.":
                            player_nvl "I know right? I thought for sure he was gonna mention an incinerator or something haha"
                            kc_nvl "Omg, can you imagine?"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with kitcat for a bit."
                "•Don't respond.":
                    hide screen NVLnarration
                    $ kcEngagement -=3
                    $ setEngagement()
                    "Nah, don't really want to encourage a parasocial relationship."
        elif vig3_macAlign == "PeacePessimism":
            kc_nvl "It was so heartbreaking seeing him falter!"
            kc_nvl "Like, I'm kinda glad he didn't actually shoot her and he was a good distraction"
            kc_nvl "But seeing him with a genuine expression of disappointment... it got to me, y'know?"
            $ playerNVLNarration = "kitcat's talking about MAC's growth in the game. Should I respond?"
            show screen NVLnarration
            menu:
                "•It paralleled Moze's flashback so well too.":
                    hide screen NVLnarration
                    $ kcEngagement += 1
                    $ setEngagement()
                    player_nvl "Yeah, that moment really got me as well. Plus it parallels Moze's flashback with Ama really nicely"
                    player_nvl "The whole episode did a really good job at drawing those connections"
                    player_nvl "I feel for MAC. Just trying to do his best"
                    kc_nvl "For real. And he's doing so well!"
                    kc_nvl "Like, I absolutely loved seeing him take a more active role in this episode!"
                    kc_nvl "The bit about him \"disposing\" of the other prototype? So funny haha"
                    menu:
                        "•That part got me too!":
                            player_nvl "I almost lost it there too! MAC learning the subtle art of euphemisms haha"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•I thought it was going to be a lot worse.":
                            player_nvl "I know right? I thought for sure he was gonna mention an incinerator or something haha"
                            kc_nvl "Omg, can you imagine?"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with kitcat for a bit."
                "•I kind of wish he'd taken the shot.":
                    hide screen NVLnarration
                    $ kcEngagement += 1
                    $ setEngagement()
                    player_nvl "I actually kind of wish he'd taken a shot at her"
                    player_nvl "I mean, I do like him going for a less harmful maneuver. But that's not always going to be an option"
                    player_nvl "Moze might not be around to keep him safe forever. Eventually, he's going to have to make these tough calls for himself"
                    kc_nvl "I see that. I guess I just don't want him to have to grow up that fast"
                    kc_nvl "Don't get me wrong though, absolutely loved seeing him take a more active role!"
                    kc_nvl "The bit about him \"disposing\" of the other prototype? So funny haha"
                    menu:
                        "•That part got me too!":
                            player_nvl "I almost lost it there too! MAC learning the subtle art of euphemisms haha"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•I thought it was going to be a lot worse.":
                            player_nvl "I know right? I thought for sure he was gonna mention an incinerator or something haha"
                            kc_nvl "Omg, can you imagine?"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with kitcat for a bit"
                "•Don't respond.":
                    hide screen NVLnarration
                    $ kcEngagement -=3
                    $ setEngagement()
                    "Nah, don't really want to encourage a parasocial relationship."
        else:
            kc_nvl "And he didn't even use it!"
            kc_nvl "Lil guy to saved the day by reading Ama to absolute filth instead of using brute force"
            kc_nvl "I heard people say that your choices affect him and his behavior, and it was really cool to see that happen"
            kc_nvl "Nice to know he's growing up right, y'know?"
            $ playerNVLNarration = "kitcat's talking about MAC's growth in the game. Should I respond?"
            show screen NVLnarration
            menu:
                "•He's gotten so clever!":
                    hide screen NVLnarration
                    $ kcEngagement += 1
                    $ setEngagement()
                    player_nvl "I know, I thought that was a great move from him as well!"
                    player_nvl "Really cool to see how Moze's influence is affecting him, makes the whole \"doing better\" thing feel rewarding imo"
                    player_nvl "Gotta love him learning to be clever and not just \"tough\""
                    kc_nvl "Yeah! And I think that change is apparent too when you think about how reckless he was going after the Hounds the first time"
                    kc_nvl "Absolutely loved seeing him take a more active role!"
                    kc_nvl "The bit about him \"disposing\" of the other prototype? So funny haha"
                    menu:
                        "•That part got me too!":
                            player_nvl "I almost lost it there too! MAC learning the subtle art of euphemisms haha"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•I thought it was going to be a lot worse.":
                            player_nvl "I know right? I thought for sure he was gonna mention an incinerator or something haha"
                            kc_nvl "Omg, can you imagine?"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with kitcat for a bit"
                "•I kind of wish he'd taken the shot":
                    hide screen NVLnarration
                    $ kcEngagement += 1
                    $ setEngagement()
                    player_nvl "I actually kind of wish he'd taken a shot at her"
                    player_nvl "I mean, I do like how this reflects Moze's actions. But talking your way out of situations may not always be an option"
                    player_nvl "Moze might not be around to keep him safe forever. Eventually, he's going to have to make these tough calls for himself"
                    kc_nvl "I see that. I guess I just don't want him to have to grow up that fast"
                    kc_nvl "Don't get me wrong though, absolutely loved seeing him take a more active role!"
                    kc_nvl "The bit about him \"disposing\" of the other prototype? So funny haha"
                    menu:
                        "•That part got me too!":
                            player_nvl "I almost lost it there too! MAC learning the subtle art of euphemisms haha"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•I thought it was going to be a lot worse.":
                            player_nvl "I know right? I thought for sure he was gonna mention an incinerator or something haha"
                            kc_nvl "Omg, can you imagine?"
                            kc_nvl "Little guy growing up so fast"
                            player_nvl "He really is"
                            kc_nvl "Anyway, thanks for the chat, [username]! See ya next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with kitcat for a bit."
                "•Don't respond.":
                    hide screen NVLnarration
                    $ kcEngagement -=3
                    $ setEngagement()
                    "Nah, don't really want to encourage a parasocial relationship."
    elif topfan == "pickledDragons": #pickledDragons Convo
        #pickledDragons convo - Ama! and flashbacks
        "pickledDragons sent me a message on Loop'd."
        pd_nvl "Hey [username], thanks for the stream!"
        pd_nvl "It was cool to see the Oakley in a truly lawless environment. Felt like we got to know the characters a lot better"
        pd_nvl "Especially the whole relationship between Ama and Moze. Those flashbacks really set a tone for their connection"
        pd_nvl "Wondering what you think of Ama, now that we got to spend some time with her?"
        $ playerNVLNarration = "pickledDragons asked how I feel about Ama. Should I respond?"
        show screen NVLnarration
        menu:
            "•I think she did the best she could.":
                hide screen NVLnarration
                $ pdEngagement += 1
                $ setEngagement()
                player_nvl "Honestly, I think she did the best she could"
                player_nvl "I mean, we saw that one flashback with the gun, where she basically threatened to kill Moze. And that's not cool"
                player_nvl "But she was trying to do her best to teach Moze so she could survive on her own"
                player_nvl "It's kinda what we're doing with MAC, and I really like that parallel"
                pd_nvl "I see what you mean. There's clearly still some kind of connection between Ama and Moze. Hard to just throw that away"
                pd_nvl "Yes! I like that you pointed out that parallel!"
                if vig3_bcRepSaved == True:
                    pd_nvl "Is that why you decided to save the BigCorp rep?"
                    menu:
                        "•Yeah, I don't want MAC to turn out like Moze.":
                            player_nvl "Yeah, especially with MAC watching me in that moment"
                            player_nvl "Felt like Moze should model some sort of morality for him"
                            pd_nvl "Even though the guy turned around and threatened MAC immediately?"
                            menu:
                                "•If I'd known that I would've acted differently.":
                                    player_nvl "Well if I had known he was gonna turn around and try to kick MAC then I would've let Ama kill his ass haha"
                                    player_nvl "But we make the choices we make with the information we have, y'know?"
                                    pd_nvl "That's a fair point. I think I would've let him die"
                                "•Yeah, even knowing that I would've done the same thing.":
                                    player_nvl "Yeah, even knowing that I would've saved him"
                                    player_nvl "Just because he's an asshole doesn't mean he deserves to die"
                                    pd_nvl "I guess not"
                        "•No, I just thought it was right to save him.":
                            player_nvl "I actually wasn't thinking about MAC in that moment"
                            player_nvl "I just didn't think it was right for Moze to standby and let someone die"
                            pd_nvl "Even though the guy turned around and threatened MAC immediately?"
                            menu:
                                "•If I'd known that I would've acted differently.":
                                    player_nvl "Well if I had known he was gonna turn around and try to kick MAC then I would've let Ama kill his ass haha"
                                    player_nvl "But we make the choices we make with the information we have, y'know?"
                                    pd_nvl "That's a fair point. I think I would've let him die"
                                "•Yeah, even knowing that I would've done the same thing.":
                                    player_nvl "Yeah, even knowing that I would've saved him"
                                    player_nvl "Just because he's an asshole doesn't mean he deserves to die"
                                    pd_nvl "I guess not"
                        "•I don't know.":
                            player_nvl "I don't really know what motivated that decision"
                            player_nvl "I guess it just felt right in the moment to me"
                            pd_nvl "Even though the guy turned around and threatened MAC immediately?"
                            menu:
                                "•If I'd known that I would've acted differently.":
                                    player_nvl "Well if I had known he was gonna turn around and try to kick MAC then I would've let Ama kill his ass haha"
                                    player_nvl "But we make the choices we make with the information we have, y'know?"
                                    pd_nvl "That's a fair point. I think I would've let him die"
                                "•Yeah, even knowing that I would've done the same thing.":
                                    player_nvl "Yeah, even knowing that I would've saved him"
                                    player_nvl "Just because he's an asshole doesn't mean he deserves to die"
                                    pd_nvl "I guess not"
                    pd_nvl "So, you heard rumblings of this secret \"Ama Alliance\" route in the last episode?"
                    pd_nvl "I heard you can get Ama to fight on your side!"
                    menu:
                        "•That sounds exciting!":
                            player_nvl "Really!? That's so exciting!"
                            player_nvl "Would be awesome to get the Snakehawks back together!"
                            player_nvl "As long as Ama plays nice with the Oakley crew haha"
                            pd_nvl "I know right! Could be so cool to fight alongside her!"
                            pd_nvl "Can't wait for the next episode. See ya next week [username]!"
                        "•Ooh I don't know about that.":
                            player_nvl "Ooh I don't know about that"
                            player_nvl "She's so antagonistic in episode 3"
                            player_nvl "If they don't handle it well, that could feel kinda cheap"
                            pd_nvl "Maybe, but I feel like they'll set it up pretty well"
                            pd_nvl "Can't wait for the next episode. See ya next week [username]!"
                else:
                    pd_nvl "Is that why you let Ama kill the BigCorp rep?"
                    menu:
                        "•Yes, I think MAC needs to learn the hard lessons.":
                            player_nvl "Yeah. I don't think Moze should teach MAC by like pointing a gun at him (obviously)"
                            player_nvl "But being a life or death situation like that and learning that sometimes you have to put your own safety above others..."
                            player_nvl "I think that's a lesson he has to learn in this galaxy"
                            pd_nvl "Yeah, I think that makes a lot of sense"
                            pd_nvl "Tough to learn that at a young age, whether you're a kid or a robot"
                        "•No, I was concerned for MAC's safety.":
                            player_nvl "It wasn't about teaching MAC anything actually"
                            player_nvl "It just seemed like a bad idea to get in Ama's way"
                            player_nvl "I thought maybe that would... I dunno, help her blow off some steam hahaha"
                            pd_nvl "Lol from her character it does seem like the kinda thing that might've calmed her down"
                        "•I don't know.":
                            player_nvl "I don't really know what motivated that decision"
                            player_nvl "I guess it just felt right in the moment to me"
                    pd_nvl "So, you heard rumblings of this secret \"Ama Alliance\" route in the last episode?"
                    pd_nvl "I heard you can get Ama to fight on your side!"
                    menu:
                        "•That sounds exciting!":
                            player_nvl "Really!? That's so exciting!"
                            player_nvl "Would be awesome to get the Snakehawks back together!"
                            player_nvl "As long as Ama plays nice with the Oakley crew haha"
                            pd_nvl "I know right! Could be so cool to fight alongside her!"
                            pd_nvl "Can't wait for the next episode. See ya next week [username]!"
                        "•Ooh I don't know about that.":
                            player_nvl "Ooh I don't know about that"
                            player_nvl "She's so antagonistic in episode 3"
                            player_nvl "If they don't handle it well, that could feel kinda cheap"
                            pd_nvl "Maybe, but I feel like they'll set it up pretty well"
                            pd_nvl "Can't wait for the next episode. See ya next week [username]!"
            "•I think she was a bad influence on Moze.":
                hide screen NVLnarration
                $ pdEngagement += 1
                $ setEngagement()
                player_nvl "Honestly, I think she was a bad influence on Moze"
                player_nvl "Like, you saw that one flashback with the gun, where she basically threatened to kill Moze. Not cool"
                player_nvl "And that connection is clearly weighing on Moze in a way that isn't healthy"
                player_nvl "It's also interesting how they're drawing parallels between that relationship and Moze and MAC"
                pd_nvl "I get that, but there's clearly still some kind of connection between Ama and Moze. Hard to just throw that away"
                pd_nvl "Yes! I like that you pointed out that parallel with MAC!"
                if vig3_bcRepSaved == True:
                    pd_nvl "Is that why you decided to save the BigCorp rep?"
                    menu:
                        "•Yeah, I don't want MAC to turn out like Moze.":
                            player_nvl "Yeah, especially with MAC watching me in that moment"
                            player_nvl "Felt like Moze should model some sort of morality for him"
                            pd_nvl "Even though the guy turned around and threatened MAC immediately?"
                            menu:
                                "•If I'd known that I would've acted differently.":
                                    player_nvl "Well if I had known he was gonna turn around and try to kick MAC then I would've let Ama kill his ass haha"
                                    player_nvl "But we make the choices we make with the information we have, y'know?"
                                    pd_nvl "That's a fair point. I think I would've let him die"
                                "•Yeah, even knowing that I would've done the same thing.":
                                    player_nvl "Yeah, even knowing that I would've saved him"
                                    player_nvl "Just because he's an asshole doesn't mean he deserves to die"
                                    pd_nvl "I guess not"
                            pd_nvl "Idk, I think Moze "
                        "•No, I just thought it was right to save him.":
                            player_nvl "I actually wasn't thinking about MAC in that moment"
                            player_nvl "I just didn't think it was right for Moze to standby and let someone die"
                            pd_nvl "Even though the guy turned around and threatened MAC immediately?"
                            menu:
                                "•If I'd known that I would've acted differently.":
                                    player_nvl "Well if I had known he was gonna turn around and try to kick MAC then I would've let Ama kill his ass haha"
                                    player_nvl "But we make the choices we make with the information we have, y'know?"
                                    pd_nvl "That's a fair point. I think I would've let him die"
                                "•Yeah, even knowing that I would've done the same thing.":
                                    player_nvl "Yeah, even knowing that I would've saved him"
                                    player_nvl "Just because he's an asshole doesn't mean he deserves to die"
                                    pd_nvl "I guess not"
                        "•I don't know.":
                            player_nvl "I don't really know what motivated that decision"
                            player_nvl "I guess it just felt right in the moment to me"
                            pd_nvl "Even though the guy turned around and threatened MAC immediately?"
                            menu:
                                "•If I'd known that I would've acted differently.":
                                    player_nvl "Well if I had known he was gonna turn around and try to kick MAC then I would've let Ama kill his ass haha"
                                    player_nvl "But we make the choices we make with the information we have, y'know?"
                                    pd_nvl "That's a fair point. I think I would've let him die"
                                "•Yeah, even knowing that I would've done the same thing.":
                                    player_nvl "Yeah, even knowing that I would've saved him"
                                    player_nvl "Just because he's an asshole doesn't mean he deserves to die"
                                    pd_nvl "I guess not"
                    pd_nvl "So, you heard rumblings of this secret \"Ama Alliance\" route in the last episode?"
                    pd_nvl "I heard you can get Ama to fight on your side!"
                    menu:
                        "•That sounds exciting!":
                            player_nvl "Really!? That's so exciting!"
                            player_nvl "Would be awesome to get the Snakehawks back together!"
                            player_nvl "As long as Ama plays nice with the Oakley crew haha"
                            pd_nvl "I know right! Could be so cool to fight alongside her!"
                            pd_nvl "Can't wait for the next episode. See ya next week [username]!"
                        "•Ooh I don't know about that.":
                            player_nvl "Ooh I don't know about that"
                            player_nvl "She's so antagonistic in episode 3"
                            player_nvl "If they don't handle it well, that could feel kinda cheap"
                            pd_nvl "Maybe, but I feel like they'll set it up pretty well"
                            pd_nvl "Can't wait for the next episode. See ya next week [username]!"
                else:
                    pd_nvl "So then why did you let Ama kill the BigCorp rep?"
                    menu:
                        "•It felt like what Moze would do.":
                            player_nvl "It just felt like what Moze would do in that situation"
                            player_nvl "Cause she's not perfect. She's trying to do better, but she still doesn't do the right thing all the time"
                            pd_nvl "Hmm, I like that. Characters who are trying to change and have trouble"
                            pd_nvl "Feels very true to life"
                        "•I was concerned for MAC's safety.":
                            player_nvl "It wasn't about teaching MAC anything"
                            player_nvl "It just seemed like a bad idea to get in Ama's way"
                            player_nvl "I thought maybe that would... I dunno, help her blow off some steam hahaha"
                            pd_nvl "Lol from her character it does seem like the kinda thing that might've calmed her down"
                        "•I don't know.":
                            player_nvl "I don't really know what motivated that decision"
                            player_nvl "I guess it just felt right in the moment to me"
                    pd_nvl "So, you heard rumblings of this secret \"Ama Alliance\" route in the last episode?"
                    pd_nvl "I heard you can get Ama to fight on your side!"
                    menu:
                        "•That sounds exciting!":
                            player_nvl "Really!? That's so exciting!"
                            player_nvl "Would be awesome to get the Snakehawks back together!"
                            player_nvl "As long as Ama plays nice with the Oakley crew haha"
                            pd_nvl "I know right! Could be so cool to fight alongside her!"
                            pd_nvl "Can't wait for the next episode. See ya next week [username]!"
                        "•Ooh I don't know about that.":
                            player_nvl "Ooh I don't know about that"
                            player_nvl "She's so antagonistic in episode 3"
                            player_nvl "If they don't handle it well, that could feel kinda cheap"
                            pd_nvl "Maybe, but I feel like they'll set it up pretty well"
                            pd_nvl "Can't wait for the next episode. See ya next week [username]!"
            "•Don't respond.":
                hide screen NVLnarration
                $ pdEngagement -=1
                $ setEngagement()
                "Nah, don't really want to encourage a parasocial relationship."

    else: #Coriolis Convo
        #Coriolis convo about Rec
        "Coriolis sent me a message on Loop'd."
        cs_nvl "Hey, [username], wanted to say thanks for a great stream!"
        cs_nvl "It was a really fun to get to meet so many different characters. They were all really cool, but I think Rec was my favourite"
        cs_nvl "I think it sucks how we had to break his heart in the end. Just wanted to see how you're feeling about that moment"
        if vig3_recResponse == "Confused":
            cs_nvl "I was kind of surprised that you had Moze say she was confused about killing Allistar"
            $ playerNVLNarration = "Coriolis asked my feelings about Rec. Should I respond?"
            show screen NVLnarration
            menu:
                "•It reflected how I felt as a player.":
                    hide screen NVLnarration
                    $ csEngagement += 1
                    $ setEngagement()
                    player_nvl "I made that choice cause it was what I felt the most in that moment"
                    player_nvl "I wasn't expecting it and it was so tense"
                    if misclick == True:
                        cs_nvl "Right, I remember you said you didn't even mean to do it, right? Like it was a misclick?"
                        player_nvl "Yeah. So that choice just felt like what my actual response was"
                    else:
                        pass
                    player_nvl "It may not have been the most fun or the most sincere from Moze's perspective, but it was what I felt as a player"
                    cs_nvl "That makes a lot of sense, I appreciate how much thought you put into these choices"
                    cs_nvl "So many of them seem really tough"
                    menu:
                        "•Yeah, they're hard to make.":
                            player_nvl "Yeah, I don't think it ever gets easier tbh"
                            player_nvl "Like, don't get me wrong, it's still a game"
                            player_nvl "But when you're really connected to these characters, it's always kinda tense when you're deciding their fates"
                            cs_nvl "Seriously, it's why I don't play these kinda games on my own really. So much pressure haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•It's actually getting easier.":
                            player_nvl "I used to be more stressed out about the decisions, but they've gotten easier to make recently"
                            player_nvl "Maybe it's just how many of these games I've played. I've learned not to stress about them too much"
                            player_nvl "And that makes it more fun to experiment with different kinds of chocies"
                            cs_nvl "That's a really cool perspective!"
                            cs_nvl "I could never, making these kinds of choices always stresses me out too much haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with Coriolis for a bit."
                "•It felt the most honest from Moze.":
                    hide screen NVLnarration
                    $ csEngagement += 1
                    $ setEngagement()
                    player_nvl "I know it seems odd, but I think it was the most honest response from Moze"
                    player_nvl "I feel like even she doesn't know why she did it, especially since she could so easily have stunned Allistar"
                    player_nvl "I mean, I'm thinking like in terms of her character and less myself. But I think that's fun to explore"
                    player_nvl "Here's this character who puts on the air of the confident Captain, but maybe she's insecure and confused a lot of the time too"
                    cs_nvl "Ooh interesting. I really like that take!"
                    cs_nvl "And I appreciate how much thought you put into these choices"
                    cs_nvl "So many of them seem really tough"
                    menu:
                        "•Yeah, they're hard to make.":
                            player_nvl "Yeah, I don't think it ever gets easier tbh"
                            player_nvl "Like, don't get me wrong, it's still a game"
                            player_nvl "But when you're really connected to these characters, it's always kinda tense when you're deciding their fates"
                            cs_nvl "Seriously, it's why I don't play these kinda games on my own really. So much pressure haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•It's actually getting easier.":
                            player_nvl "I used to be more stressed out about the decisions, but they've gotten easier to make recently"
                            player_nvl "Maybe it's just how many of these games I've played. I've learned not to stress about them too much"
                            player_nvl "And that makes it more fun to experiment with different kinds of chocies"
                            cs_nvl "That's a really cool perspective!"
                            cs_nvl "I could never, making these kinds of choices always stresses me out too much haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with Coriolis for a bit."
                "•Don't respond.":
                    hide screen NVLnarration
                    $ csEngagement -= 2
                    $ setEngagement()
                    "Nah, don't really want to encourage a parasocial relationship."
        elif vig3_recResponse == "Classic":
            cs_nvl "I thought the attempt to use Moze's classic line made sense, and I liked how Rec called her on that"
            $ playerNVLNarration = "Coriolis asked my feelings about Rec. Should I respond?"
            show screen NVLnarration
            menu:
                "•It's a story Moze has to believe in.":
                    hide screen NVLnarration
                    player_nvl "Yeah, I agree, I think this whole \"I didn't have a choice\" thing is just a story Moze keeps telling herself"
                    player_nvl "It's how she copes with having to deal with the darkness of this galaxy. But it's not the reality"
                    player_nvl "It also closes the loop on Allistar's death in a really impactful way. I'm glad they brought Rec back for this episode"
                    cs_nvl "Yeah me too. I feel like it's so easy to fall into the \"I didn't have a choice\" mentality"
                    cs_nvl "I don't like what Moze did, but I do feel for her"
                    cs_nvl "And I appreciate how much thought you put into these choices"
                    cs_nvl "So many of them seem really tough"
                    menu:
                        "•Yeah, they're hard to make.":
                            player_nvl "Yeah, I don't think it ever gets easier tbh"
                            player_nvl "Like, don't get me wrong, it's still a game"
                            player_nvl "But when you're really connected to these characters, it's always kinda tense when you're deciding their fates"
                            cs_nvl "Seriously, it's why I don't play these kinda games on my own really. So much pressure haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•It's actually getting easier.":
                            player_nvl "I used to be more stressed out about the decisions, but they've gotten easier to make recently"
                            player_nvl "Maybe it's just how many of these games I've played. I've learned not to stress about them too much"
                            player_nvl "And that makes it more fun to experiment with different kinds of chocies"
                            cs_nvl "That's a really cool perspective!"
                            cs_nvl "I could never, making these kinds of choices always stresses me out too much haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with Coriolis for a bit."
                "•I don't think Moze had choice.":
                    hide screen NVLnarration
                    player_nvl "I really don't think Moze had a choice. I mean, technically she did, but it's more complicated than that."
                    player_nvl "Maybe she stuns Allistar and he gets some time to come around and isn't a threat to the crew after that point."
                    player_nvl "But could Moze really have taken that risk?"
                    player_nvl "I don't know that she would have. And I think it's interesting to explore this character who has such a black and white outlook on that kind of thing."
                    cs_nvl "Hmmm I see what you're saying"
                    cs_nvl "I think I still agree with Rec (and Allistar), but it's a good point. Moze is put in a LOT of tough situations."
                    cs_nvl "And I appreciate how much thought you put into these choices"
                    cs_nvl "So many of them seem really tough"
                    menu:
                        "•Yeah, they're hard to make.":
                            player_nvl "Yeah, I don't think it ever gets easier tbh."
                            player_nvl "Like, don't get me wrong, it's still a game"
                            player_nvl "But when you're really connected to these characters, it's always kinda tense when you're deciding their fates."
                            cs_nvl "Seriously, it's why I don't play these kinda games on my own really. So much pressure haha."
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•It's actually getting easier.":
                            player_nvl "I used to be more stressed out about the decisions, but they've gotten easier to make recently."
                            player_nvl "Maybe it's just how many of these games I've played. I've learned not to stress about them too much."
                            player_nvl "And that makes it more fun to experiment with different kinds of chocies."
                            cs_nvl "That's a really cool perspective!"
                            cs_nvl "I could never, making these kinds of choices always stresses me out too much haha."
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with Coriolis for a bit."
                "•Don't respond.":
                    hide screen NVLnarration
                    $ csEngagement -= 2
                    $ setEngagement()
                    "Nah, don't really want to encourage a parasocial relationship."
        else:
            cs_nvl "I'll be honest, I thought it was harsh the way Moze was so adamant about justifying it"
            $ playerNVLNarration = "Coriolis asked my feelings about Rec. Should I respond?"
            show screen NVLnarration
            menu:
                "•It was harsh but true.":
                    hide screen NVLnarration
                    $ csEngagement -= 1
                    $ setEngagement()
                    player_nvl "It was harsh, but it was true"
                    player_nvl "I feel like saying any of the other options just wasn't being honest to Rec"
                    player_nvl "Like, straight up, Allistar betrayed our trust. That has to have consequences"
                    player_nvl "And I'd rather be direct with Rec than try to sugarcoat the trauma"
                    cs_nvl "No I get that... I guess I just didn't read that in Moze's character"
                    if misclick == True:
                        cs_nvl "And I guess I'm kind of surprised considering you said it was a misclick originally"
                        player_nvl "That's fair, but I've had time to think about it and I think it makes sense for her character"
                    cs_nvl "It's not what I would have done, but I see your perspective"
                    cs_nvl "And I appreciate how much thought you put into these choices"
                    cs_nvl "So many of them seem really tough"
                    menu:
                        "•Yeah, they're hard to make.":
                            player_nvl "Yeah, I don't think it ever gets easier tbh"
                            player_nvl "Like, don't get me wrong, it's still a game"
                            player_nvl "But when you're really connected to these characters, it's always kinda tense when you're deciding their fates"
                            cs_nvl "Seriously, it's why I don't play these kinda games on my own really. So much pressure haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•It's actually getting easier.":
                            player_nvl "I used to be more stressed out about the decisions, but they've gotten easier to make recently"
                            player_nvl "Maybe it's just how many of these games I've played. I've learned not to stress about them too much"
                            player_nvl "And that makes it more fun to experiment with different kinds of chocies"
                            cs_nvl "That's a really cool perspective!"
                            cs_nvl "I could never, making these kinds of choices always stresses me out too much haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with Coriolis for a bit."
                "•It surprised me too.":
                    hide screen NVLnarration
                    player_nvl "I wasn't expecting it to be that harsh either tbh"
                    player_nvl "The thing that got me was the looks from the crew after Moze admitted it"
                    player_nvl "Like, I didn't want to try to sugarcoat it to Allistar... but damn"
                    cs_nvl "Yeah, she really tore into his memory. Feel like there's no way Rec ever speaks to us again"
                    player_nvl "No chance"
                    cs_nvl "I appreciate how much thought you put into these choices"
                    cs_nvl "So many of them seem really tough"
                    menu:
                        "•Yeah, they're hard to make.":
                            player_nvl "Yeah, I don't think it ever gets easier tbh"
                            player_nvl "Like, don't get me wrong, it's still a game"
                            player_nvl "But when you're really connected to these characters, it's always kinda tense when you're deciding their fates"
                            cs_nvl "Seriously, it's why I don't play these kinda games on my own really. So much pressure haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•It's actually getting easier.":
                            player_nvl "I used to be more stressed out about the decisions, but they've gotten easier to make recently"
                            player_nvl "Maybe it's just how many of these games I've played. I've learned not to stress about them too much"
                            player_nvl "And that makes it more fun to experiment with different kinds of chocies"
                            cs_nvl "That's a really cool perspective!"
                            cs_nvl "I could never, making these kinds of choices always stresses me out too much haha"
                            cs_nvl "You handle it all really well though! It's a lot of fun watching you work through the moral quagmires!"
                            player_nvl "Hahaha I'm glad you think so!"
                            cs_nvl "Thanks for the chat [username]! See you next week!"
                        "•Don't respond.":
                            "Don't really want to keep the conversation going, but it was nice to chat with Coriolis for a bit."
                "•Don't respond.":
                    hide screen NVLnarration
                    $ csEngagement -= 2
                    $ setEngagement()
                    "Nah, don't really want to encourage a parasocial relationship."
    $ screenComplete = True
    call screen webNavigation_vig3
    scene bg black with dissolve

label FlinchAnalytics_vig3():
    $ menu = adv_menu
    $ screenComplete = False
    $ flinchView = True
    "You should probably check out Flinch's analytics page."
    $ flinchCheck = 0
    show screen webNavigation_vig3
    scene flinch_v3screen with dissolve
    if viewershipHigh == True:
        $ followerGoal = 0
    else:
        $ followerGoal = 1
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
    show screen viewershipButton_vig3
    call screen streamAnalytics_vig3
    hide screen streamAnalytics_vig3 with dissolve

label blueitVignette3_1():
    $ menu = adv_menu
    scene blueit_v3screen at truecenter with dissolve
    $ screenComplete = False
    $ blueitView = True
    $ blueitPages = [] #this line can be deleted eventually. It's here temporarily to make testing a bit easier.
    $ blueitPages.append(vig3_bThread1)
    $ blueitPages.append(vig3_bThread2)
    $ blueitPages.append(vig3_bThread3)
    $ blueitPages.append(vig3_bThread4)
    $ blueitPages.append(vig3_bThread5)
    $ blueitPages.append(vig3_bThread6)
    "You go to check out the subblueit to see how people are reacting to Episode 3."
    jump blueitVignette3_2

label blueitVignette3_2():
    scene blueit_v3screen at truecenter
    show screen webNavigation_vig3
    if blueitChoiceCheck == True:
        $ screenComplete = True
    else:
        pass
    call screen blueit
    return

label vig3_macro_brother_1():
    nvl clear
    $ menu = nvl_menu
    scene bg black with dissolve
    stop music fadeout 2.0
    "It's reassuring that Jessie feels good about the stream."
    "And there's just one more episode to go."
    "One way or another, this thing will come to an end."
    "You start absentmindedly scrolling through Loop'D when you notice that Elliot is online."
    "It's been a while since you had a proper chat so you decide to shoot him a message."
    scene discordview with dissolve
    play music "soundtrack/elsGroove.wav" volume 0.9 fadein 1.0
    player_nvl "Hey El, you got some time to chat?"
    $ playerNVLNarration = "You sit in front of your computer for a couple of minutes."
    show screen NVLnarration with dissolve
    pause
    $ playerNVLNarration = "You remember Elliot had a test later this week. Maybe he's busy studying."
    pause
    $ playerNVLNarration = "Then you see that he's typing."
    pause
    pause 1.0
    hide screen NVLnarration with dissolve
    bro_nvl "I was actually just gonna shoot you a message asking the same thing lol"
    menu:
        "•Ask Elliot what's up.":
            jump vig3_macro_brother_cedric
        "•Tell Elliot about the stream.":
            jump vig3_macro_brother_stream

label vig3_macro_brother_cedric():
    $ vig3_brotherChat += 1
    if vig3_brotherChat == 1:
        player_nvl "Oh? Got life updates?"
    else:
        pass
    bro_nvl "Actually, yeah, I got an A on Mrs. Weber's mid-term!"
    menu:
        "•That's great!":
            player_nvl "That's great, El! Should take some of the pressure off the final"
            bro_nvl "Yeah, it's a relief for sure :)"
            player_nvl "... anything else to report on?"
            bro_nvl "Nothing too important really"
            player_nvl "suuuuure"
            bro_nvl ">:)"
        "•Who cares? I want boy news!":
            player_nvl "Grades shmades! What about the Brit Boy!"
            bro_nvl "Who?"
            player_nvl "YOU KNOW WHO, EL!"
            bro_nvl "lmao >:)"
    player_nvl "Spill it"
    bro_nvl "I asked Cedric out on a date"
    menu:
        "•What did he say?":
            player_nvl "El! That's amazing!"
            player_nvl "I'm so proud of you!"
            player_nvl "What did he say?"
        "•YESSSS!":
            player_nvl "YESSS!"
            player_nvl "WHOOOO!"
            player_nvl "So proud of you!"
            player_nvl "How did you do it? Was it like a big production like a prom thing? Were you like wearing a suit or something?"
            player_nvl "Wait, what did he say?"
    bro_nvl "lmao"
    bro_nvl "He said yes!"
    player_nvl "WHOOOOO!"
    menu:
        "•Best. Day. Ever.":
            player_nvl "Best. Day. Ever."
        "•I'm gonna cry.":
            #player_nvl "They grow up so fast!"
            player_nvl "Omg, I'm legit gonna cry"
    bro_nvl "It's not your crush haha"
    player_nvl "No, but like"
    bro_nvl "But thank you"
    player_nvl "You made the move"
    bro_nvl "I know"
    player_nvl "You put yourself out there"
    bro_nvl "Yeah"
    player_nvl "That's huge"
    bro_nvl "I know! I'm like giddy all over!"
    player_nvl "So how did it happen?"
    bro_nvl "Well, it wasn't a big production"
    bro_nvl "I took your advice from a couple weeks back and just kept making the effort to chat with him these past couple weeks"
    player_nvl "Uh huh"
    bro_nvl "It was tough, but I kept thinking about what you said"
    if vig1_overthink == True:
        bro_nvl "\"Don't overthink it\""
    else:
        bro_nvl "Talking to someone you like is \"never not weird\""
    bro_nvl "So I just tried to be myself and we started walking home from school together like almost every day"
    player_nvl "Cuuuuute"
    bro_nvl "And when we got to our block today... I don't know"
    bro_nvl "I just asked if he'd like to go on a date with me"
    bro_nvl "I didn't even realize I was doing it until I heard myself say the word \"date\""
    player_nvl "And then?"
    bro_nvl "He said yes..."
    bro_nvl "And kissed me on the cheek :)"
    player_nvl "I'm dying"
    bro_nvl "lol"
    player_nvl "No, for real, I couldn't write a better story for you two"
    player_nvl "You got plans for the date??"
    bro_nvl "Yeah, he's gonna take me to see a movie next Friday!"
    $ playerNVLNarration = "Next Friday? You've got something next Friday too..."
    show screen NVLnarration with dissolve
    pause
    $ playerNVLNarration = "Oh! That's the day of your last {i}Oakley 2{/i} stream!"
    pause
    menu:
        "•That's the same day as the last Oakley stream.":
            hide screen NVLnarration
            player_nvl "Funny, that's the same day as my last Oakley stream"
            bro_nvl "I know! I'm sorry I won't be able to make it"
            bro_nvl "It's the only night Cedric's free!"
            player_nvl "Nononono your date is way more important"
            player_nvl "We'll catch up on Oakley 2 when I get back for Thanksgiving!"
            bro_nvl "Yes!"
            player_nvl "And I'll be sending you the best vibes for a good date from a distant galaxy!"
            bro_nvl "I promise they will be received haha"
        "•You? In a movie theater?":
            hide screen NVLnarration
            player_nvl "Since when do you go see movies in theathers Mr. \"Classical Music is the Only Real Theatre\""
            bro_nvl "Since my crush started giving me shit about my lack of pop culture knowledge"
            player_nvl "You know what, fair"
            player_nvl "I did try to get into MOBAs just to impress my crush a couple years back so I guess I can't talk"
            bro_nvl "Yeah, I remember that. Fun streams!"
            player_nvl "My kda was like 0.3"
            bro_nvl "I didn't say they were fun for you"
            player_nvl "Shut up"
            bro_nvl "Love you too <3"
            bro_nvl "I know this means I won't make it to the final Oakley 2 stream, but I figured you would understand"
            player_nvl "Oh, of course. This is way more important!"
            player_nvl "You have fun and don't even think about worrying about it!"
            bro_nvl "Thanks [player] :)"
    if vig3_brotherChat == 1:
        bro_nvl "Soooo yeah, that's my big news"
        bro_nvl "What's up with you? How's the stream going'?"
        jump vig3_macro_brother_stream
    else:
        jump vig3_macro_brother_end

label vig3_macro_brother_stream():
    $ vig3_brotherChat += 1
    player_nvl "Great, I wanted to tell you about the stream today"
    bro_nvl "Ooh yes, gimme the deets!"
    menu:
        "•Stream is great!":
            player_nvl "The stream is great!"
            bro_nvl "Love hearing that!"
            if energy >= 5:
                bro_nvl "Just based on the VODs it looks like you're having a good time"
            else:
                bro_nvl "Glad you're not like beaten down by the push for Affiliate"
            if viewershipLow == True:
                bro_nvl "Though it seems like not too many people stuck around after that raid"
                player_nvl "Yeah, the chat isn't too crazy, but it's still bigger than I'm used to"
                menu:
                    "•It can get a little overwhelming.":
                        $ energy -= 1
                        player_nvl "Tbh it can feel a little overwhelming"
                    "•It's super fun!":
                        $ energy += 1
                        player_nvl "It's super fun! But I'm also still learning how to manage that chaos"
            else:
                bro_nvl "Plus it looks like people have stuck around after that raid a while back"
                player_nvl "Yeah the chat is popping off on a regular basis these days"
                menu:
                    "•It can get a little overwhelming.":
                        $ energy -= 1
                        player_nvl "Tbh it can feel a little overwhelming, but still fun"
                    "•It's super fun!":
                        $ energy += 1
                        player_nvl "It's super fun! But also like really chaotic"
            bro_nvl "For sure, so what are you enjoying the most?"
            menu:
                "•The game.":
                    $ energy += 1
                    player_nvl "The game, for sure!"
                    bro_nvl "Yeaaah, Oakley 2 does look sick"
                    bro_nvl "Bummed I'll have to wait till the holidays to get it for myself"
                    player_nvl "It's cool. I mean the art is so good"
                    bro_nvl "The soundtrack too. Heard that little futuristic baroque piece in Episode 3"
                    bro_nvl "There's already a sick lofi remix on utube I'm using to help me study"
                    if vibes == True:
                        player_nvl "Yeah and game has a great vibe in general. Very easy to stream, but still really engaging"
                    elif humour == True:
                        player_nvl "Plus it's just a funny game. Script has a lot of good one-liners"
                    elif story == True:
                        player_nvl "And the story builds on the themes from the first game so well"
                        player_nvl "The characters especially are really well done"
                    else:
                        player_nvl "And the story builds on the themes from the first game so well"
                        player_nvl "The characters especially are really well done"
                    bro_nvl "Yep, I was already bummed I couldn't play it at launch and keeping up with your playthrough is just increasing the fomo"
                    player_nvl "Lol, sorry"
                    bro_nvl "Ahh it's fine. This way I get to see you make all the mistakes and then do the better choices for me >:)"
                    player_nvl "Always so selfless"
                    bro_nvl "You know me"
                "•The chat.":
                    $ enthusiasm += 1
                    player_nvl "I'm having a lot of fun interacting with the chat"
                    if viewershipHigh == True:
                        player_nvl "Like I said, there are way more people around now and it's really cool to be hanging out with everyone"
                        player_nvl "I get to hear more perpsectives on the game's moral choices. Wacky stories. Crazy jokes"
                    else:
                        player_nvl "It's not that many more people than I'm used to, but even so, there's a lot more going on there now"
                        player_nvl "I like hearing people's different perspectives on the game's moral choices and seeing their wacky jokes"
                    player_nvl "Plus it feels like everyone in chat is really starting to vibe and be like friends"
                    bro_nvl "Yeah, honestly half the fun of watching the VODs is seeing what goes on in your chat"
                    bro_nvl "And I'm really glad it's been a positive experience for you!"
                "•Being on camera.":
                    $ energy += 1
                    player_nvl "I think it's just being on camera"
                    player_nvl "When I'm not trying to get Affiliate, I stream a bit less regularly"
                    player_nvl "It's nice to just be in the habit of performing for people"
                    player_nvl "It can get tiring, don't get me wrong. But I have so much fun that it doesn't matter"
                    bro_nvl "I'm glad! I know you always feel a bit \"off\" if you go without streaming for a while"
                    bro_nvl "Definitely good to keep up the habit!"
                "•Playing Outlaw." if outlaw >= marshal - 2:
                    $ enthusiasm += 2
                    player_nvl "I'm really enjoying playing the more Outlaw side of things"
                    player_nvl "It's a totally different perspective of the characters than I normally have"
                    menu:
                        "•It's been a fun experiment.":
                            player_nvl "It's been a really fun experiment to just see how the game changes"
                            player_nvl "And people in the chat respond to it really well"
                            player_nvl "Feels kinda like we're playing along all together!"
                            bro_nvl "Yeah, honestly half the fun of watching the VODs is seeing what goes on in your chat"
                            bro_nvl "And I'm really glad it's been a positive experience for you!"
                        "•I feel kind of guilty about it, actually.":
                            player_nvl "It's weird, I actually feel kinda guilty about that"
                            player_nvl "Like, should I be enjoying playing this problematic protagonist?"
                            bro_nvl "I don't think you need to feel guilty about that"
                            bro_nvl "They designed the game to be played in multiple ways"
                            bro_nvl " I'm sure the devs would love to know that people are enjoying both sides of their work"
                            player_nvl "That's a good point"
                            bro_nvl "Y'know, as long as you're not going around blowing up aid ships in your free time lol"
                            player_nvl "Hahaha haven't gotten there yet"
                            bro_nvl "Good, but now I gotta keep an eye on you ;)"
        "•It's going well.":
            player_nvl "It's going well."
            bro_nvl "Ooh, not the period"
            bro_nvl "What's up?"
            menu:
                "•Nothing.":
                    player_nvl "Nothing's up"
                    bro_nvl "You sure?"
                    menu:
                        "•Yes.":
                            player_nvl "Yeah, things are good"
                            player_nvl "They're just not great"
                            player_nvl "They're not shit. But they're not great"
                            #Could cut the following three conditional statements
                            if enthusiasm >= reluctance:
                                player_nvl "Trying to get Affiliate is a bit of a slog, but playing the game and hanging with chat has been really fulfilling"
                            if energy < 5:
                                player_nvl "I feel pretty tired, but not like exhausted"
                            if outlaw > marshal and enthusiasm >= reluctance:
                                player_nvl "And I'm having fun experimenting with the game's Outlaw choices"
                                player_nvl "But the episodies can get long too"
                            bro_nvl "Sounds like the life of someone who turned their passion into work"
                            player_nvl "Yeah, but that work isn't even paying me anything"
                            bro_nvl "It can't be all boring and tough though?"
                            bro_nvl "What's something you're enjoying about it?"
                            menu:
                                "•The game.":
                                    $ energy += 1
                                    player_nvl "I still really like the game"
                                    bro_nvl "Yeaaah, Oakley 2 does look sick"
                                    bro_nvl "Bummed I'll have to wait till the holidays to get it for myself"
                                    player_nvl "It's cool. I mean the characters, story, and art are so good"
                                    bro_nvl "The soundtrack too. Heard that little futuristic baroque piece in Episode 3"
                                    bro_nvl "There's a sick lofi remix on vibefy that I'm using to help me study"
                                    bro_nvl "I was already bummed I couldn't play it at launch and keeping up with your playthrough is just increasing the fomo"
                                    player_nvl "Lol, sorry"
                                    bro_nvl "Ahh it's fine. This way I get to see you make all the mistakes and then do the better choices for me >:)"
                                    player_nvl "Always so selfless"
                                    bro_nvl "You know me"
                                "•The chat.":
                                    $ enthusiasm += 1
                                    player_nvl "I'm enjoying interacting with the chat"
                                    if viewershipHigh == True:
                                        player_nvl "Like I said, there are way more people around there now and it's cool to be hanging out with everyone"
                                        player_nvl "I get to hear more perpsectives on the game's moral choices. Wacky stories. Crazy jokes"
                                    else:
                                        player_nvl "It's not that many more people than I'm used to, but even so, there's more going on there than I'm used to"
                                        player_nvl "I like hearing people's different perspectives on the game's moral choices and seeing their wacky jokes"
                                    player_nvl "Plus it feels like the people in chat are really starting to vibe and be like friends"
                                    bro_nvl "Yeah, honestly half the fun of watching the VODs is seeing what goes on in your chat"
                                    bro_nvl "And I'm really glad it's been a positive experience for you!"
                                "•Being on camera.":
                                    $ energy += 1
                                    player_nvl "I think it's just being on camera"
                                    player_nvl "When I'm not trying to get Affiliate, I stream a bit less regularly"
                                    player_nvl "It's nice to be in the habit of performing for people"
                                    player_nvl "It can get tiring, don't get me wrong. But I have so much fun that it doesn't matter"
                                    bro_nvl "I'm glad! I know you always feel a bit \"off\" if you go without streaming for a while"
                                    bro_nvl "Definitely good to keep up the habit!"
                                "•Playing Outlaw." if outlaw >= marshal - 2:
                                    $ enthusiasm += 2
                                    player_nvl "I'm really enjoying playing the more Outlaw side of things"
                                    player_nvl "It's a totally different perspective of the characters than I normally have"
                                    menu:
                                        "•It's been a fun experiment.":
                                            player_nvl "It's been a fun experiment to just see how the game changes"
                                            player_nvl "And people in the chat respond to it really well"
                                            player_nvl "Feels kinda like we're playing along all together!"
                                            bro_nvl "Yeah, honestly half the fun of watching the VODs is seeing what goes on in your chat"
                                            bro_nvl "And I'm really glad it's been a positive experience for you!"
                                        "•I feel kind of guilty about it, actually.":
                                            player_nvl "It's weird, I actually feel kinda guilty about that"
                                            player_nvl "Like, should I be enjoying playing this problematic protagonist?"
                                            bro_nvl "I don't think you need to feel guilty about that"
                                            bro_nvl "They designed the game to be played in multiple ways"
                                            bro_nvl " I'm sure the devs would love to know that people are enjoying both sides of their work"
                                            player_nvl "That's a good point"
                                            bro_nvl "Y'know, as long as you're not going around blowing up aid ships in your free time lol"
                                            player_nvl "Hahaha haven't gotten there yet"
                                            bro_nvl "Good, but now I gotta keep an eye on you ;)"
                            bro_nvl "Hey, I know streaming is kind of like work, but I also know you"
                            bro_nvl "I know you love games and the community that comes from the stream"
                            bro_nvl "I just hope the good of that stuff always outweighs the bad. And if it starts to flip, then you can stop. No one is making you do this, y'know?"
                            player_nvl "You're right. Thanks, El"
                            bro_nvl "Anytime"
                        "•Actually...":
                            player_nvl "Actually, yeah some things are bugging me"
                            bro_nvl "I knew it. Like what?"
                            menu:
                                "•The grind for Affiliate sucks.":
                                    $ energy -= 1
                                    player_nvl "The grind for Affiliate just sucks"
                                    player_nvl "Like I'm playing this game and it's bringing in more viewers on the regular"
                                    player_nvl "But jamming out smaller streams is just exhausting"
                                    if energy < 5:
                                        bro_nvl "Yeah, ngl, you look a bit tired in the streams sometimes"
                                        player_nvl "Well that's kinda embarrassing lol"
                                        bro_nvl "I mean, I don't think anyone else would notice"
                                        bro_nvl "But like, I can tell when you're running on low energy"
                                        bro_nvl "Sibling shit, y'know?"                            
                                    else:
                                        bro_nvl "Really? On the VODs you look energized"
                                        player_nvl "That's good to hear"
                                        player_nvl "Sometimes I stream and I feel really good. Other times, it's rough"
                                    bro_nvl "Mom always says life has its ups and downs"
                                    bro_nvl "But I know you. And I know that you stream because it has way more highs than lows"
                                    bro_nvl "Otherwise you wouldn't bother"
                                    bro_nvl "Like, just think about the people you've met from it that you wouldn't have otherwise"
                                    player_nvl "You're right. Thanks, El"
                                    bro_nvl "Anytime"
                                "•I feel pressure from the viewers.":
                                    $ reluctance += 1
                                    player_nvl "Honestly, I feel pressure from the viewers"
                                    player_nvl "Especially since the raid"
                                    if viewershipHigh == True:
                                        player_nvl "It's kinda like people are expecting me to play Outlaw"
                                    else:
                                        player_nvl "Not a ton of people stuck around after Episode 2. So I'm wondering if I like should've changed my playstyle more"
                                    player_nvl "Idk, it feels a bit weird now"
                                    bro_nvl "You know, a wise person once said: \"just be yourself, and they'll see you for the warm, smart, and talented person you are\""
                                    player_nvl "I think you're paraphrasing there"
                                    bro_nvl "A bit, yeah, but the point still stands"
                                    bro_nvl "You're gonna hit Affiliate because you're awesome and smart and talented"
                                    bro_nvl "If you feel pressure from the audience, I dunno, screw 'em. Just do you!"
                                    player_nvl "Thanks, El. You're really good at being encouraging"
                                    bro_nvl "I learned from the best :)"
                                "•I don't know.":
                                    player_nvl "Honestly, I don't know."
                                    bro_nvl "Come on, it has to be something"
                                    bro_nvl "Is it the game? Do you not like it?"
                                    menu:
                                        "•No, that's not it.":
                                            player_nvl "No, I really like the game"
                                        "•Maybe.":
                                            player_nvl "Maybe. It's been different than what I expected"
                                    bro_nvl "Was it something someone said in chat?"
                                    menu:
                                        "•I don't think so.":
                                            player_nvl "I don't think so. People have been really friendly for the most part"
                                        "•No.":
                                            player_nvl "No, the people in chat have been really good"
                                    bro_nvl "Damn, I'm sorry. Wish there was something I could do to help"
                                    player_nvl "No, I don't think this thing is like \"solvable\""
                                    player_nvl "I'm just feeling a type of way right now"
                                    player_nvl "But you are helping, just talking like this"
                                    player_nvl "Thanks, El"
                                    bro_nvl "Anytime!"
                "•The grind for Affiliate sucks.":
                    $ energy -= 1
                    player_nvl "The grind for Affiliate just sucks"
                    player_nvl "Like I'm playing this game and it's bringing in more viewers on the regular"
                    player_nvl "But jamming out smaller streams is just exhausting"
                    if energy < 5:
                        bro_nvl "Yeah, ngl, you look a bit tired in the streams sometimes"
                        player_nvl "Well that's kinda embarrassing lol"
                        bro_nvl "I mean, I don't think anyone else would notice"
                        bro_nvl "But like, I can tell when you're running on low energy"
                        bro_nvl "Sibling shit, y'know"                            
                    else:
                        bro_nvl "Really? On the VODs you look energized"
                        player_nvl "That's good to hear"
                        player_nvl "Sometimes I stream and I feel really good. Other times, it's rough"
                    bro_nvl "Mom always says life has its ups and downs"
                    bro_nvl "But I know you. And I know that you stream because it has way more highs than lows"
                    bro_nvl "Otherwise you wouldn't bother"
                    bro_nvl "Like just think about the people you've met from it that you wouldn't have otherwise"
                    player_nvl "You're right. Thanks, El"
                    bro_nvl "Anytime"
                "•Genuinely, things are just fine.":
                    player_nvl "No, genuinely, things are just good"
                    player_nvl "School is hectic, especially with the grind for Affiliate, but my studies are still manageable"
                    player_nvl "I'm excited to come back home for Thanksgiving"
                    player_nvl "And the stream feels good"
                    player_nvl "Not like, incredible. But I like where I'm at"
                    player_nvl "That's kind of all I can ask for"
                    bro_nvl "You dating anyone?"
                    player_nvl "lmao well that came out of nowhere"
                    bro_nvl "I'm just saying it's been a while ok!"
                    player_nvl "I've been too busy recently. But I promise I will try to get back on the horse. For you"
                    bro_nvl "Good :)"
        "•It's getting pretty tough.":
            player_nvl "Honestly, it feels pretty rough out there"
            bro_nvl "Ah, I'm sorry to hear that"
            bro_nvl "What's up?"
            menu:
                "•The grind for Affiliate sucks.":
                    $ energy -= 1
                    player_nvl "The grind for Affiliate just sucks"
                    player_nvl "Like I'm playing this game and it's bringing in more viewers on the regular"
                    player_nvl "But jamming out smaller streams is just exhausting"
                    if energy < 5:
                        bro_nvl "Yeah, ngl, you look a bit tired in the streams sometimes"
                        player_nvl "Well that's kinda embarrassing lol"
                        bro_nvl "I mean, I don't think anyone else would notice"
                        bro_nvl "But like, I can tell when you're running on low energy"
                        bro_nvl "Sibling shit, y'know?"                            
                    else:
                        bro_nvl "Really? On the VODs you look energized"
                        player_nvl "That's good to hear"
                        player_nvl "Sometimes I stream and I feel really good. Other times, it's rough"
                    bro_nvl "Mom always says life has its ups and downs"
                    bro_nvl "But I know you. And I know that you stream because it has way more highs than lows"
                    bro_nvl "Otherwise you wouldn't bother"
                    bro_nvl "Like just think about the people you've met from it that you wouldn't have otherwise"
                    player_nvl "You're right. Thanks, El"
                    bro_nvl "Anytime"
                "•I feel pressure from the viewers.":
                    $ reluctance += 1
                    player_nvl "Honestly, I feel pressure from the viewers"
                    player_nvl "Especially since the raid"
                    if viewershipHigh == True:
                        player_nvl "It's kinda like people are expecting me to play Outlaw"
                    else:
                        player_nvl "Not a ton of people stuck around after Episode 2. So I'm wondering if I like should've changed my playstyle more"
                    player_nvl "Idk, it feels a bit weird now"
                    bro_nvl "You know, a wise person once said: \"just be yourself, and they'll see you for the warm, smart, and talented person you are\""
                    player_nvl "I think you're paraphrasing there"
                    bro_nvl "A bit, yeah, but the point still stands"
                    bro_nvl "You're gonna hit Affiliate because you're awesome and smart and talented"
                    bro_nvl "If you feel pressure from the audience, I dunno, screw 'em. Just do you!"
                    player_nvl "Thanks, El. You're really good at being encouraging"
                    bro_nvl "I learned from the best :)"
                "•I don't know.":
                    player_nvl "Honestly, I don't know"
                    bro_nvl "Come on, it has to be something"
                    bro_nvl "Is it the game? Do you not like it?"
                    menu:
                        "•No, that's not it.":
                            player_nvl "No, I really like the game"
                        "•Maybe.":
                            player_nvl "Maybe. It's been different than what I expected"
                    bro_nvl "Was it something someone said in chat?"
                    menu:
                        "•I don't think so.":
                            player_nvl "I don't think so. People have been really friendly, actually"
                        "•No.":
                            player_nvl "No, the people in chat have been really good"
                    bro_nvl "Damn, I'm sorry. Wish there was something I could do to help"
                    player_nvl "No I don't think this thing is like \"solvable\""
                    player_nvl "You're helping right now, just talking like this"
                    player_nvl "Thanks, El"
                    bro_nvl "Anytime!"
    player_nvl "Playing Oakley on stream is so different"
    player_nvl "Definitely not like back when it was just you and me"
    bro_nvl "Aahh good times"
    bro_nvl "Remember when I ripped the controller from you cause you threatened to insult Allistar?"
    player_nvl "I was teasing you a bit too much haha"
    bro_nvl "Now look at us"
    bro_nvl "Or you. Big bad outlaw >:)"
    menu:
        "•Yeah, sorry about Allistar.":
            player_nvl "Yeah, sorry about that"
            bro_nvl "lolwut"
            bro_nvl "Why are you apologizing?"
            player_nvl "For killing Allistar. I know he's your favourite character"
            bro_nvl "Oh, seriously? Don't worry about it"
            menu:
                "•But it wasn't even on purpose.":
                    player_nvl "But like, I didn't even do it on purpose"
                    bro_nvl "So what?"
                    bro_nvl "I mean yeah, if it were me, I probably would've stunned him. But it's your game"
                    bro_nvl "I know how many times you tried to play Outlaw Moze in {i}Oakley 1{/i}"
                    bro_nvl "If a misclick actually got you to do it and see what that's all about, I'm happy for you!"
                "•Thanks for understanding.":
                    player_nvl "Thanks for understanding"
                    player_nvl "I figured you'd be disappointed you didn't get to see his story"
                    bro_nvl "Pfft that's your loss lol"
                    bro_nvl "I'm romancing the hell out of that hunk when I start my playthrough"
        "•I'm not that much of an Outlaw.":
            player_nvl "I'm not that much of an outlaw"
            if marshal > outlaw + 5: #testing if I can check how much more one variable is greater than another
                bro_nvl "I know, I know, I've been watching the VODs"
                bro_nvl "Still gotta give you some guff for offing Allistar haha"
            elif marshal > outlaw:
                bro_nvl "Ehhhh"
                bro_nvl "Let's be real, you're on the borderline"
            else:
                bro_nvl "Srsly?"
                bro_nvl "I caught up on the VODs. I seen everything"
            bro_nvl "But you do you. That's how you gotta stream, right?"
            if vig2_marshalEpilogue == True:
                bro_nvl "I will say, I am glad you didn't side with Matticus"
                bro_nvl "What a skeeve"
            else:
                bro_nvl "That Matticus alignment at the end of Episode 2 shocked me even more than the Allistar thing tbh"
            #bro_nvl "I'm excited to check out Episode 3 when it goes up!"
        "•Outlaw life is good!":
            player_nvl "Outlaw life is good!"
            if marshal > outlaw + 5: #testing if I can check how much more one variable is greater than another
                bro_nvl "Srsly? I was just talking about you offing Allistar"
                bro_nvl "I caught up on the VODs, I know you're back to goody two-shoes Moze haha"
            elif marshal > outlaw:
                bro_nvl "Ehhhh"
                bro_nvl "Let's be real, you're on the borderline"
            else:
                bro_nvl "Good, it looks like you're really into it on stream"
                bro_nvl "And I know how many times you tried to play Outlaw Moze in Oakley 1"
                bro_nvl "Glad you're making it happen now"
    if vig3_brotherChat == 2:
        bro_nvl "Oooh maybe I should see if Cedric is down to play this game"
        player_nvl "Oh yeah, if he gets to take you to movies, you get to make him play games"
        bro_nvl "And test his moral compass at the same time >:)"
    else:
        bro_nvl "Can't wait till I get the chance to play this game"
        player_nvl "I'm excited to hear your thoughts when you get your hands on it!"
    if vig3_brotherChat == 1:
        player_nvl "That's enough about me though"
        player_nvl "What's up with you? Got any life updates?"
        jump vig3_macro_brother_cedric
    else:
        jump vig3_macro_brother_end

label vig3_macro_brother_end():
    bro_nvl "Alright, I gotta go. High school never ends"
    player_nvl "Orchestra stuff?"
    bro_nvl "Nope, I gotta panic and figure out what I'm gonna wear on my date!"
    player_nvl "Lmao you have so much time"
    bro_nvl "Not when I'm trying to fit in outfit planning between the 'OMG I CAN'T BELIEVE I'M GOING OUT WITH HIM' mini panic attacks I'll be having all week!"
    player_nvl "hahahaha you're gonna figure it out and it's gonna be a great time"
    player_nvl "Seriously, I'm so excited for you! Cedric's one lucky guy"
    bro_nvl "Thanks, [player]! I really appreciate all your advice and just you listening to me when I freak out"
    player_nvl "Hey, I appreciate you listening when I need to talk about stream stuff"
    bro_nvl "Fair, haha"
    bro_nvl "Guess we have each other's backs"
    player_nvl "Always"
    bro_nvl "Love you, [player], have a good night!"
    player_nvl "Love you too, El! Take care!"
    hide discordview with dissolve
    scene bg black with dissolve
    stop music fadeout 8.0
    "You close Loop'D and turn off your computer for the night."
    "The conversation with your brother eased some of the nerves you were feeling about finishing {i}Oakley 2{/i}."
    "It was nice to chat with him."
    "And good to feel encouragement."
    "He's really growing up and coming into his own."
    "You spend the rest of your waking night thinking about how much your brother has grown."
    "Then, eventually, you drift off to sleep."
    nvl clear
    pause 3.0
    jump vignette4Start










