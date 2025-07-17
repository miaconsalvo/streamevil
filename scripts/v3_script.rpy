label vignette3Start():
    #We want to reset these before the start of the vignette
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
    $ blueitView = False
    $ loopdView = False
    $ screenComplete = False
    $ macroChoice = False
    $ chatter_list = []
    #narrator needs to be set to alt_narrator in the next label as well
    #We now use the "scene" function to show the streamview
    #This makes it constantly viewable without being affected by transitions between labels
    #show streamview
    "It's been four weeks since you last streamed Oakley 2."
    "Episode 3 just dropped so it's time to get back into it."
    scene streamview with dissolve
    show screen streamDetails
    show screen streamChat
    "You begin the stream and then boot up the game."
    #$ reactTarget = "vig2_sc1_openingstream"
    #show screen streamerCommentary
    "You load the save file you were previously playing, and are ready to go."
    $ narrator = alt_narrator
    if vig2_outlawEpilogue == True:
        jump vig3outlawstart
    else:
        jump vig3marshalstart
###SCENE1###
label vig3outlawstart():
    show shiphub_stream at topleft onlayer background with dissolve
    "The Oakley is quiet today, and this coffee feels like I'm trying to cure every sleepless night I've had for the past few days."
    "It's nice always being the first one up, if it's even morning?"
    "I check the clock on the wall"
    mS "Yep, morning."
    "\"I've got lots more work where that came from.\" Arrogant rat. I should've gone back and blown his fortress to ash."
    "I take an uninterested sip of my drink wrapping both hands around the glass."
    "I can't believe I'm letting this get to me. Hell I've done worse, we've done worse. This probably wouldn't even crack the top five."
    "But are we doing right if we hurt people in the process?" 
    "What's the point of all of this?"
    "I find myself staring off into the distance." 
    "With my back to the door I don't see Teresa come in."
    show teresa stream neutral at stream_right with dissolve
    "She's in her usual clothes, her shirt is uncharacteristically wrinkled and half tucked, a button undone at the bottom."
    enS "Early start Captain?"
    mS "You know me, first one up, last one down." #Maybe cheekier##
    enS "That's a recipe for sleep deprivation I fear."
    "She pulls up a chair next to me grabs the warm metal pitcher from the table and fills her own cup."
    mS "And aren't you just the picture of a good night's sleep."
    enS "Hardly..."
    mS "Fighting with Jennica didn't tire either of you out?"
    enS "I can't speak for her, she's been camping in the cockpit since yesterday."
    mS "Luckily there isn't a bathroom in there."
    show teresa stream happy
    "She lets out a forced chuckle and the room goes quiet and cold for moment."
    show teresa stream neutral
    enS "There's uh, no news on Sallent."
    "I straighten myself as best as I can."
    enS "You know, that MAC is remarkable, the database access he has, even for a BigCorp bot. I could easily get you a news bulletin from the Central Planets if you wanted."
    mS "A talented little guy for sure."
    enS "But Sallent. Nothing. Not even a distress signal. Not a single report since we left Gibian V."
    mS "Hard to ask people to risk Gray Fever for a check-in. Hell, who knows if anyone is working Comms there anymore."
    "There's a long pause."
    enS "I don't...this isn't proper to say."
    enS "I wondering if you - if we - made the right choice."
    "She's looking away from me now, its not regret it's just the weight of it all."
    enS "We did what we did to keep safe and what we're doing requires... tough choices. Such is the nature of our mission."
    mS "Resa..."
    enS "We can't always expect to feel good about what we do. It's a difficult call to make."
    mS "Please."
    show teresa stream upset
    enS "SHE WON'T EVEN LOOK AT ME MOZE!"
    $ reactTarget = "vig3_sc1_out"
    show screen streamerCommentary
    "She slams the table and her glass spills on the ground with a clang spilling. Her breath is strained as she calms herself."
    "I set my cup down gently."
    show teresa stream neutral
    enS "We weren't the best people before we started this, and I know you and Jennica have more history than even I know about." 
    enS "But at least we dealt with things together."
    "I don't respond. Teresa needs this." #Consider adding choices
    enS "But ever since we took that- took MAC, it's been one awful choice after another. Barely escaping every time..."
    "Teresa lets out a defeated sigh. Before I can respond Jennica's voice echoes through the speaker."
    hide screen streamerCommentary
    pS "Captain! Comms comin' in, fuzzy but - I reckon it's the Dragonflies."
    "Teresa shoots up, I place hand on her shoulder."
    menu:
        "Be calm":
            mS "Take ten seconds. I'll see you there."
            #no approval change
        "Be firm":
            mS "You can't go in like that. Fix yourself, I'll see you there."
            #increase approval
    "I wait until I can feel her shoulder relax and walk out and down the hall, alone."
    hide teresa with dissolve
    jump vig3_sc2

label vig3marshalstart(): 
    show shiphub_stream at topleft onlayer background with dissolve
    "The Oakley is quiet today, and this coffee feels like I'm trying to cure every sleepless night I've had for the past few days."
    "It's nice always being the first one up, if it's even morning?"
    "I check the clock on the wall"
    mS "Yep, morning."
    "\"Don't worry. You'll get yours.\""
    "Annoying rat. He's lucky I didn't turn back and blow his fortress to ash."
    "I take an uninterested sip of my drink wrapping both hands around the glass."
    "I'm letting this get to me. When have I ever taken one of Sav's threats seriously?" 
    "I'm sure he wants to see {b}her{/b} even less than me."
    "We're trying to be better, but what's the point if we're all arrested, if they take MAC away."
    "I find myself staring off into the distance." 
    "With my back to the door I don't see Jennica come in."
    show jennica stream neutral at stream_right with dissolve
    "She's wearing her usual clothes but her eyes dark from exhaustion."
    pS "Up early?"
    mS "Surprisingly so are you."
    pS "Can't be early if ya ain't sleep."
    mS "Nothing quite like the comfort of my pilot being sleep deprived."
    pS "Thank the Makers she flies herself well enough."
    "She pulls up a chair next to me, grabs the warm metal pitcher from the table and fills a glass of her own. She takes out a small flask." 
    "I hold my cup out she pours a bit inside mine and her own, we cheers in the air."
    mS "Fighting with Teresa didn't tire either of your out I suppose?"
    pS "Don't know 'bout her, I've been camping in the cockpit so I don't find out."
    mS "Luckily there isn't a bathroom in there."
    pS "Takes a brave woman to go relieve herself in times like these."
    "Jennica's joke ends in a forced chuckle. The room goes quiet and cold for moment."
    pS "I'm not just staying in the cockpit to avoid Resa..."
    "I straighten myself."
    pS "I keep dreaming about getting a hit on the scanners, and I don't make it to the helm in time."
    mS "You're not the only who can fly the Oakley."
    pS "No, but I'm the only one that can outrun Ama. We got lucky but - no offense to our saving grace - I don't like not knowing how much distance we may or may not have."
    "There's a long pause."
    pS "Every little blip on the scanner make me jump, Cap. That's until I find out it's some stoved-up space junk floatin' from a click over."
    "She looks away from me to find the words."
    pS "I wonder...if we made the right choice. As wrong as it sounds."
    mS "Jenn..."
    pS "You're right, those people needed that aid, I don't regret it."
    pS "But we gotta be okay with the tough choices sometimes, be more logical, make the hard call."
    mS "Is that really how you feeling?"
    "Jennica goes quiet."
    pS "She can barely look at me Moze..."
    show jennica stream angry
    $ reactTarget = "vig3_sc1_mar"
    show screen streamerCommentary
    "Jennica smacks her glass away, it falls to the ground with a clang. She takes a quiet moment to calm herself." 
    "I set my cup down gently."
    pS "We're doing better, and that's all fine and good. And hell I'll stand by what I said."
    pS "But we need to be more united on things if we're gonna make it."
    "I don't respond." #Consider adding multiple options#
    pS "I like the kid. But we've been over our heads from the start..." 
    show jennica stream neutral
    pS "She's gonna find us, and I'm sure BigCorp isn't hung up on whether we're brought back in one piece."
    "Jennica lets out a defeated sigh. Teresa's voice echoes through the speaker before I can answer."
    hide screen streamerCommentary
    enS "Captain! There's a transmission for us - I'm certain it's the Dragonflies."
    "Jennica shoots up, I place a hand on her shoulder."
    menu:
        "Be calm":
            mS "Take ten seconds. I'll see you there."
        "Be firm":
            mS "You can't go in like that. Fix yourself, I'll see you there."
    "When Jennica's shoulder relaxes I walk out and down the hall, alone."
    hide jennica with dissolve
    jump vig3_sc2

label vig3_sc2():
    show cockpit_stream at topleft onlayer background with dissolve
    hide shiphub_stream
    "The Cockpit is a mess, Jennica has made quick work at holing up in here. MAC's been sitting patiently in the corner, he's been spending more time in here than usual."
    "Teresa is working to get the message on the screen while Jennica hangs back next to him."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    enS "Here it is..."
    "A voice sparks up from the speaker, it's staticky and every few words is cut."
    dflycontact "Captain Moze of the Oakley. My name is {b}static{/b} of the Dragonflies."
    "The cockpit is silent."
    dflycontact "I know you {b}static{/b} Dr. Vanas' work. And we are contacting {b}static{/b} drop-off {b}static{/b}"
    mS "Teresa can you get this any clearer?!?"
    enS "Captain I'm trying but I'm certain there's something wrong on our end."
    pS "Probably mucked our Comms on the way out of Gib V." 
    pS "Needed an upgrade anyway, but I've been puttin' it off for..."
    "Jennica looks at MAC"
    pS "A while..."
    dflycontact "...at a planet known as {b}static{/b} sector, coordinates {b}static{/b} message {b}static{/b} lost {b}static{/b} reattempt {b}static{/b} five days. Over and {b}static{/b}."
    enS "I've recorded the message for what its worth but if we want those coordinates in five days we'll need better gear."
    pS "That ain't much time."
    menu:
        "Not the first time.":
            mS "Not the first time we've been pressed against the wall."
        "We're used to it.":
            mS "We should be used to a tight schedule by now. "
    "We take a moment to think."
    show mac stream shock at stream_center_mac with dissolve
    macS "Dad..."
    $ reactTarget = "vig3_sc2_macdad"
    show screen streamerCommentary
    "All eyes turn to MAC, Jennica's expression softens and I watch Teresa's face rises with curiosity then fall." 
    show jennica stream neutral at stream_left
    show mac stream neutral at stream_center_mac
    "MAC sits innocently in his chair, looking off to the expanse of open space searching for the answer to a question he doesn't know how to ask."
    mS "What's going on bud?"
    macS "I- do not know."
    show jennica stream neutral at stream_left
    pS "Well that's a first." #(multiple=2) #might break the dialogue box positions
    enS "That's remarkable." #(multiple=2) #might break the dialogue box positions
    "The two exchange a quick look before turning away, remembering that they're still fighting. I turn the focus away from MAC."
    mS "Let's consider our options, come up with a plan to get our Comms back in working order. Meet at the Bridge in an hour to debrief."
    hide screen streamerCommentary
    pS "Yes, Captain!" #(multiple=2) #same as before, we could also define a new character as "teresa and jennica"
    enS "Yes, Captain!" #(multiple=2) #same as before, we could also define a new character as "teresa and jennica"
    hide jennica with dissolve
    hide teresa with dissolve
    "I turn to the door and go out into the hall. I'm stopped by a tiny purple metal leaf and an excited MAC"
    hide cockpit_stream with dissolve
    show ship_hallway_stream at topleft onlayer background with dissolve
    macS "Captain!"
    show mac stream shock at stream_center_mac with dissolve
    "I can't help but jump."
    mS "Jeez MAC, remind me to let you take point on stealth missions next time."
    show mac stream neutral at stream_center_mac with dissolve
    macS "Might I make a suggestion?"
    mS "A suggestion?"
    macS "Yes I have ideas!"
    mS "MAC respectfully, I don't have time for this-"
    macS "Which is precisely why I have a suggestion, see I was scanning BigCorp databases..."
    "I feel frustration twisting my face." ##Dialogue choice that links to MAC's reaction here.##
    menu:
        "MAC that's dangerous!":
            mS "MAC please tell me after all this work to keep us safe you're not poking in BigCorp's networks!"
            #Pessimism
        "MAC it's not safe":
            mS "MAC don't go poking into BigCorp networks. After all the work the keep you safe." #more gentle way of chiding MAC about being inconspicuous#
    "MAC's head lowers" ## this reaction can differ based on choices##
    macS "I just wanted to be helpful..."
    "I let out a heavy sigh."
    mS "MAC you are it's just- What's your suggestion?"
    macS "An initial search suggests a nearby planet known as Solara, specifically the city of Akar. It may be suitable for our needs." 
    macS "However I should caution you..."
    #Add a black screen function here. 
    "For a moment, the Oakley falls away from my view."
    "The low hum of the ship replaced by a crowded bar, the starting lines of song that will bellow out to bustling streets."
    "An old crew of Outlaws, drunk off a job well done."
    macS "Now there seems to be a significant amount of criminal activity, the crime rate is actually quite abnormal-"
    "I pat MAC's head interrupting him."
    show mac stream happy at stream_center_mac
    mS "Good job buddy, rest up. I'll see you in an hour."
    "With every step I can't help but feel my smile grow, knowing this will be the calmest hour that I've had in a very long time."
    hide mac with dissolve
    hide ship_hallway_stream
    jump vig3_sc3

##START OF ACT 1###
label vig3_sc3():
    show akarstreet_stream at topleft onlayer background with dissolve
    hide cockpit_stream
    "Well off to side of the road, the familiar streets of Akar are alive in front of us."
    "It's beaming with colour and life, red and orange banners bridge the spaces between the buildings a jubilant feeling in the air."
    "Being attached to the Vineyard, Akar's blend of nature and technology are a sight to be sure." ## Rich and vibrant plant life merging with the surrounding infrastructure brightly adorned by lights and striking signage - think eco-futurist Vegas.##
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    show mac stream neutral at stream_center_mac with dissolve    
    enS "Quite a lot of fanfare."
    pS "Really cleaned up the place."
    macS "I believe I just saw someone steal candy from a child..."
    $ reactTarget = "vig3_sc3_maccandy"
    show screen streamerCommentary
    mS "Yeah stick close bud, don't go running off around here."
    show jennica stream angry at stream_left
    pS "Moze why'd ya bring us here? Fancy gettin' caught by Ama?"
    enS "It's risky even by your standards."
    mS "You both know that this is where we'll get quality upgrades for what we need."
    mS "And I figured it'd be nice to take a break while we're at it."
    show jennica stream neutral at stream_left
    pS "I think you're too nostalgic."
    enS "And eager to get arrested."
    mS "Well a BigCorp prison probably has better food than some of the places we've seen."
    macS "There doesn't seem to be many enforcers operating here. Curious."
    mS "Yeah they tried that once, didn't go so hot."
    macS "There seems to be reports of a large altercation in Akar...Is that..."
    enS "Moze, there could be some off duty grunts here."
    hide screen streamerCommentary
    mS "Resa look, the Inventor's Fair is in town." #Choices here?
    mS "Most of the security will be looking at the Vineyard- not here." 
    mS "Let's see if we can find some old friends, grab what we need, and maybe a drink or two..."
    pS "And a softer bed."
    show teresa stream happy at stream_right
    enS "...A proper hot meal."
    macS "I require none of those things."
    "A small kid walks past with his parents carrying a giant cotton candy dessert. It looks like a planet being orbited by small chocolate moons." ###The candy could change based on alignment###
    macS "But I require that."
    "As MAC start to wheel towards the treat Jennica thankfully picks him up."
    pS "Alright buddy we'll see what we can do."
    show mac stream neutral at stream_left5mac with move
    "I almost didn't see the guy as he pushes past Teresa, getting a bit too close for comfort..." ##HOUND LEADER (early forties)##
    show teresa stream upset at stream_right
    show jennica stream angry at stream_left
    enS "Hey! Care to watch yourself?"
    show houndleader stream neutral at stream_right5 with dissolve
    houndleaderunknown "Aw, smile a bit sweetcheeks, it's a celebration!"
    show jennica stream fight at stream_left
    "Before anyone can respond, Jennica punches the man in the face. He falls down hard and she puts her boot on his throat, Teresa leans over grinning." 
    hide houndleader with dissolve
    "I can feel MAC on my leg as he hides behind me."
    $ reactTarget = "vig3_sc3_firstfight"
    show screen streamerCommentary
    enS "How's this, sweetcheeks?"
    "I can hear footsteps rushing to us. He's not alone."
    menu:
        "Pull out your gun.":
            $ macViolence += 1
            "I pull out my gun in the direction of the sound." 
            mS "Not likely boys."
        "Show them you're a Snakehawk":
            $ macPeace += 1
            "I lift my arm and flash the Snakehawks tattoo on my left hand."
            mS "I really wouldn't do that."
    show houndgoon stream neutral at stream_right5 with dissolve 
    "The two men back away and fall back, they're well built but not sharp enough for a fight like this."
    "I give the signal to Jennica as she lets their friend scramble up and run."
    hide houndgoon with dissolve
    hide screen streamerCommentary
    "The city moves as normal, uninterested in what just happened."
    enS "It's good to be back."
    hide teresa with Dissolve(0.5)
    hide jennica with Dissolve(0.5)
    hide mac with Dissolve(0.5)
    jump vig3_sc4

label vig3_sc4():
    show mac stream neutral at stream_center_mac with dissolve   
    "We arrive at the storefront of Specs and Steele, a small body shop just off the side of the main road."
    macS "Is this the most suitable store for our needs?"
    mS "Definitely. Run by an old friend. Probably one of the only ones that won't shoot first before taking our credits."
    "MAC pauses for a moment, thinking through something."
    macS "You seem to be worried about a lot violence. Did you do something Captain?"
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    pS "Long story kid."
    enS "Several long stories to be precise."
    mS "Don't worry about it too much."
    macS "I fear I have not stopped worrying since we landed."
    "Jennica glares at Teresa."
    pS "He gets it from you."
    hide akarstreet_stream with dissolve
    show reccshop_stream at topleft onlayer background with dissolve
    "We walk into Specs and Steele the inside is...neat?"
    "Steele's usual brand of chaotic mess has been replaced with with a refined and uncharacteristic organization."
    "At least now you can walk through it."
    mS "Hey Steele! You in?"
    pS "Hope you still have that Vira Brandy!"
    enS "From four years ago?"
    pS "It ages well!"
    macS "A delicacy from the Vineyard, Reynar's Vira Brandy - named after his partner - has a shelf-life of 5 years."
    pS "See? Just made it!"
    hide mac with dissolve
    "With MAC trailing us I scan some of the newer gear, even some weirder stuff, weird for Steele."
    "Someone comes out from the back room."
    show rec stream neutral at stream_center with dissolve
    ###RECCRIN (Late 20s) enters from the back room. They looks like an older version of their brother Allistar, long hair, tougher build.##
    recS "Well I'll be..."
    "We can't help our silence in this moment."
    show jennica stream neutral at stream_left
    show teresa stream happy at stream_right
    show rec stream happy
    pS "REC!"
    "Jennica runs up to hug Rec, they embrace and Jenn lifts them off the ground."
    pS "It's wonderful to see you kid."
    enS "Looking good, Reccrin!"
    recS "Thanks but I'm not much of a kid anymore."
    mS "I'll say."
    hide jennica stream neutral with dissolve 
    hide teresa stream happy with dissolve
    "I walk over slower than I should and go for a hug. Pushing the guilt down as I do."
    mS "What happened to Steele?"
    recS "Old man passed two years back, so I took over."
    mS "I know he was up in years but to think."
    mS "What happened?"
    recS "Nothing, just age, the years caught up to him."
    mS "Oh all the things I can't believe the years were what got him."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream happy at stream_right with dissolve
    pS "I was really lookin' forward to sharin' that brandy."
    recS "Well you're in luck."
    pS "Hell yeah!"
    show rec stream happy at stream_right5 with move
    show mac stream neutral at stream_left5mac with dissolve
    macS "Vira Brandy is the first alcohol product that uses edible chimaeron fruit. Which is quite odd."
    pS "And delicious!"
    "As Rec turns to get the brandy they pause to look down at MAC."
    show rec stream surprised
    hide jennica stream neutral with dissolve 
    hide teresa stream happy with dissolve
    recS "And who's this little guy?"
    macS "I'm MAC!"
    show rec stream happy
    recS "I bet you are!"
    "Rec's eyes grow wide, it's the same look Allistar gave him when they first met."
    recS "And where did they pick you up?"
    macS "From a top secret research facility in BigCorp headquarters."
    show rec stream surprised
    "If I could die right now I would."
    "Reccrin just stares at MAC blinking rapidly."
    recS "... What?"
    #mS (Multiple Response options about how to lie)
    menu:
        "It's too dangerous to tell Rec everything right now."
        "Just a courier bot we picked up.":
            mS "Just a courier bot we found and outfitted."
            mS "Figured we could use an extra hand and a morale boost..."
            "I hear Jennica speak low behind me."
            pS "Just a courier bot..."
        "Top secret? Please.":
            mS "If by top secret you mean off a random shelf, then sure, keep it hush hush though."
            "No one responds."
            recS "Good thing you became an Outlaw instead of a comedian."
            show rec stream happy
        "Teresa did you program that?":
            mS "That's the last time I let you touch our gear Teresa."
            enS "Excuse me?"
            "I give her a look."
            enS "Oh haha yeah... of course Cap."
    #^All of these feel mean....could use a rewrite#
    show rec stream thinking
    "MAC looks unsure if he should respond. Rec looks between the two of us for an answer."
    recS "Mind if I take a closer look?"
    "MAC looks up at me. I guess we're in it now...."
    mS "Up to you buddy."
    macS "I do not mind."
    mS "Go for it."
    "Rec carefully examines MAC, seeing the mismatched metal in some of his body parts where Allistar worked."
    recS "So interesting, the work is a bit rushed but still clean, almost reminds me of how Allistar would do it."
    "The room goes still I don't know what to say to them."
    mS "Had to be a rushed job, we've been on the move."
    mS "But look not to interrupt your analysis, we're here to fix our Comms."
    show rec stream neutral
    recS "Sorry yeah got carried away. What do you need? New parts?"
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    enS "Definitely a range extender."
    pS "Honestly even the base parts could use an upgrade. If you have some to spare."
    mS "We needa get outfitted and going in the next few days."
    recS "Got it, lemme check the back, I might have something for you."
    hide rec stream neutral with dissolve 
    "Rec disappears to the back of the shop. MAC turns to me and I already know he's vibrating with a question."
    show mac stream neutral at stream_center_mac with move
    macS "Do they know Allistar? They look like Allistar."
    mS "Allistar is their brother."
    enS "I'm guessing we're not telling them that their brother's body is floating in space a few clicks out." 
    mS "I'm not feeling too inclined."
    macS "But they have a right to know..."
    "I need to think about how to approach this." ###Add multipleoptions###
    menu:
        "Mac thinks Rec has a right to know about their brother."
        "I'm not being fair.":
            $ macHope += 1
            mS "MAC I'll be honest, I'm not being fair. But we need their help and that's a conversation for after."
            mS "Okay?"
            macS "Yes Captain."
        "We'll tell them after we get the part":
            $ macPessimism += 1
            mS "Range extender first, hard talk later. We can't leave here without it."
            mS "So it'll be hush hush for right now, okay?"
            macS "Yes Captain."
        "I have no love for Allistar":
            $ macViolence += 1
            mS "I'm not about to apologize for what I needed to do. They'll find out eventually."
            mS "Understood?"
            macS "Yes Captain."
    "Reccrin comes out after a brief moment with a long antennae and some internal parts for our Comms."
    show mac stream neutral at stream_left5mac with move
    show rec stream happy at stream_right5 with dissolve
    recS "Definitely an older model but she should work better than what you got. Need an install?"
    enS "I could use the hand."
    pS "Thanks Rec."
    mS "It's very appreciated."
    show rec stream thinking
    recS "No worries! Hey since y'all have been on the move, you wouldn't have happened by Al at all?" 
    recS "I haven't heard from him in while."
    "There's too long of a pause that I can't think of something fast enough."
    "Then the shop door swings open."
    hide mac with dissolve
    hide jennica with dissolve
    show rec stream surprised at stream_center with move
    show houndleader at stream_left with dissolve
    "A group of five enter the shop, dark uniforms with a dog patched on their right shoulder." 
    "These guys, they're ones from before." ##The Hound Leader##
    $ reactTarget = "vig3_sc4_houndraid"
    show screen streamerCommentary
    houndleader "Alright Reccrin, you know the drill! Mandatory sweep!"
    houndleader "Don't cause any-"
    houndleader "Oh!"
    enS "You must be joking."
    houndleader "Sweetcheeks."
    enS "Bite me."
    houndleader "Maybe later, I'm on the clock now."
    hide teresa with dissolve
    mS "Didn't know Akar hired rent-a-cops."
    show houndgoon at stream_right with dissolve
    "A smaller Hound moves up next to him" 
    "She's tough and with something to prove."
    houndgoon "I suggest you get yourself and your crew in order and stay out of the way."
    hide screen streamerCommentary
    "Rec looks at me with a forced smile."
    show rec stream neutral
    recS "Please Moze..."
    recS "Hounds! We don't want any trouble."
    recS "Just do what you need to do."
    houndleader "That's what I like about you Rec, so reasonable."
    "We stand back as the group rummages through the store, knocking over shelves and taking random items." 
    "They're armed to the teeth and now I understand why Rec is so quick to comply."
    ###Describe the wreck this group is leaving and give the players two opportunities to intervene or continue to comply silently.###
    "Like restless children they stick their hands in every possible shelf and knock over part after part."
    "It's a big show they snicker to each other, incoherently mumble protocols and giggle."
    menu:
        "Reccrin is looking down at their desk."
        "That's enough!":
            mS "Alright that's enough!"
        "Let them continue":
            "They're relentless."
            "Doesn't matter the material or how fragile or how important, they don't stop."
            "I cringe as each piece falls. Broken parts start to litter the floor."
            menu:
                "Do I intervene?"
                "That's enough!":
                    mS "Alright that's enough!"
                "Stay quiet.":
                    "They continue to trash the shop. More carnage. They're laughing to each other, tossing equipment like a hackey sac."
                    "I see one of them try to head to the back room."
                    mS "Alright that's enough!"
    mS "Alright that's enough!"
    houndgoon "You'd be best to stay out of official business."
    "Another uniform chimes in."
    houndgoon "We're under order to collect contraband."
    mS "Contraband? That's rich."
    mS "Learned that from the little pamphlet they gave you?"
    houndgoon "Tryna be smart are we?"
    mS "Someone has to."
    houndgoon "Contraband is whatever we say it is."
    houndleader "We'll also be taking this."
    "The Hound's leader goes to pick up the antennae for the Comms that's sitting on Rec's store counter." 
    ###Streamer reaction: Of course he does###
    recS "This item is being sold to customers at the moment. I can assure you it's perfectly legitimate."
    houndleader "Are you admitting to selling contraband Reccrin?" 
    houndleader "That's cause for reprimand."
    mS "That so called \"contraband\" is mine. And they said it's perfectly legit."
    "I slowly walk up to the counter moving to take the parts."
    mS "So I'd like it back now."
    hide rec with dissolve 
    "The uniforms turn to us and I know they're gearing up for a fight. They probably won't kill us, but I can't imagine how banged up we'll be or what happens if they find MAC." ###The player must decide between three actions, fight, let them have it, or Bribe - IF THEY HAVEN'T BRIBED REGI###.
    menu:
        "How do I deal with this?"
        "Fight them.":
            $ macViolence += 1
            "I get into his face - let him pry my gear from my cold dead hands." 
            "He smiles and throws the first punch before I can react." 
            "It knocks the wind out of me and I hit the ground."
            "Then impact after impact to my stomach before I can catch my breath. He gets low, right to my ear."
            houndleader "You should've died with the rest of the Snakehawks."
            "He takes the antennae as I struggle to get up from the floor."
            houndleader "Pleasure doing business with you."
            "The Hounds leave us to pick ourselves up and walk out of the shop. MAC who has thankfully been hiding rolls forward."
            hide houndgoon with dissolve
            hide houndleader with dissolve
            show rec stream neutral at stream_right5 with dissolve
            show mac stream neutral at stream_left5mac with dissolve
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            macS "Captain are you hurt?" 
            mS "Just my pride."
            "Teresa goes to pull me up."
            enS "I want to burn that man from the inside."
            pS "Maybe we can use him as our antennae instead."
            mS "Now that's a thought. Rec, you know those guys?"
        "Let them take the antenna.":
            $ macPessimism += 1
            "I take a step back, we can't afford a fight right now, it's too risky."
            houndleader "Pleasure doing business with you."
            "The Hounds turn to leave knocking some stuff around."
            "On the way out with the parts, the Leader hits me with a good punch while I'm off guard."
            hide houndgoon with dissolve
            hide houndleader with dissolve
            show rec stream neutral at stream_right5 with dissolve
            show mac stream neutral at stream_left5mac with dissolve
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            macS "Captain are you hurt?" 
            mS "Just my pride."
            "Teresa goes to pull me up."
            mS "Sorry I didn't want to put you all in more danger."
            enS "You're good Captain."
            enS "Makers I'd like to burn that man up from the inside."
            pS "Maybe we can use him as our antennae instead."
            mS "Now that's a thought. Rec, you know those guys?"
        "Try and bribe them" if reginaldChoice == False: #This option shoudl still be here but different outcomes based on the variable.
            $ macPeace += 1
            "I take out my communicator,"
            mS "Listen this doesn't need to be ugly, we'll pay the tarriff and get out of your hair."
            houndleader "Finally a sensible idea." #it doesnt work right? they need to take the antenna to force the crew to keep looking
            "We do the transfer."
            "And I'm hit wiht a pucnh without warning."
            "He grabs the part and the Hounds move out."
            houndleader "Pleasure doing business with you."
            "The Hounds commit some extra carnage on the way out."
            hide houndgoon with dissolve
            hide houndleader with dissolve
            show rec stream neutral at stream_right5 with dissolve
            show mac stream neutral at stream_left5 with dissolve
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            macS "Captain are you hurt?" 
            mS "Just my pride, and my wallet."
            "Teresa goes to pull me up."
            enS "I want to burn that man up from the inside."
            pS "Maybe we can use him as our antennae instead."
            mS "Now that's a thought. Rec, you know those guys?"
    "They pull out five glasses. And drop a bottle of brandy on the counter."
    "As they start to pour, they stop themselves at the fifth and grab an oil can and pour it in giving it to MAC."
    show mac stream happy 
    macS "Thank you!"
    show mac stream neutral at stream_left with move
    recS "They're the Hounds. Reynar's new security detail."
    recS "Usually they're more of nuisance than anything. Shaking down shops and the like."
    recS "But with the Inventor's Fair they've gotten more excitable. Not surprised they'd come by here just terrible timing is all."
    pS "Sorry what's the Inventor's Fair? I forgot to ask."
    enS "Big conference. Lots of tech companies, scholars, and start-ups from all over. Schmoozing and rubbing shoulders, the like."
    pS "Sounds like a party."
    enS "One of the biggest."
    mS "We're steering clear."
    mS "Rec anyone else you know who can get us the part we need?"
    recS "Not top of mind but I can show you around and we can probably find something."
    mS "Sounds like a plan."
    "Reccrin holds their glass up and swallows their drink in one gulp. We follow suit."
    amaS "Ah that's the stuff."
    hide jennica with dissolve
    hide teresa with dissolve
    hide rec with dissolve
    hide mac with dissolve
    "I stop the glass at my lips and nearly drop it. Whipping my head around I almost grab for my gun until I catch Jennica's eyes."
    show jennica stream neutral at stream_left with dissolve
    pS "All right, Cap?"
    "I compose myself and try to calm down."
    mS "Yeah, sorry."
    "When I swallow my drink, it goes down hard."
    hide jennica with dissolve
    jump vig3_sc5

label vig3_sc5():
    hide reccshop_stream
    show akarplaza_stream at topleft onlayer background with dissolve 
    "When Rec leads us to the plaza I'm almost startstruck with how it looks." ###REC takes the Oakley Crew to the Plaza. In front is Rec and MOZE with JENNICA and TERESA taking up the rear with MAC in between them.##
    "The space is abundant with life."
    "The shops and bars on the outer ring of the roundabout shine, bursting with patrons." 
    "Music and reverie pour out like sections of a cacophonous orchestra."
    "At the center is a park area that sits a large statue of a man sitting with an apple in his hand." 
    "It has a massive hole blown out of it."
    show rec stream happy at stream_right5 with dissolve
    recS "Alright Oakley it's been a while but welcome to the Plaza!"
    show mac stream neutral at stream_left5mac with dissolve
    macS "Wow...."
    show jennica stream neutral at stream_left with dissolve
    pS "Surprised it's still standing."
    show teresa stream happy at stream_right with dissolve
    enS "Did they change the statue?"
    recS "Oh yeah they did, because *someone* blew up the last one."
    enS "Fabulous."
    macS "Someone?"
    recS "Why don't you ask your friends kid."
    mS "It was a long time ago."
    pS "Mighty legendary."
    hide rec with dissolve
    hide jennica with dissolve
    hide teresa with dissolve
    hide mac with dissolve
    "I'm taken back to the plaza several years back, rowdy and riotous."
    "BigCorp officers are scattered around attempting to suppress the riot."
    "With small fires everywhere Teresa ont the arm of a statue of a man in a lab coat, Jennica and I look on, blasters in hand."
    enS "We're gonna be *HICK* glorkin *HICK* LEGENDS HAHA!!!"
    pS "Pffffft! Glorkin?"
    mS "Resa hey hey Resa, ya gotta, gotta down from there."
    enS "Not until you say it."
    pS "She's really set huh."
    mS "A wild one, that's for sure."
    pS "Please do the honors Captain."
    "An enforcer in the distance fires a shot at the statue and misses."
    "Jennica returns fire and takes him down."
    mS "Okay okay, you're in!"
    enS "No, no, do the call, it's not real without it."
    mS "The call isn't real, get down from there."
    enS "I KNOW IT'S REAL!"
    "Another bullet narrowly misses Teresa"
    "She pulls out her blaster and hits her mark."
    pS "Better do the call Cap."
    enS "SEE!!! THERE IS ONE!!"
    "These two together are gonna be a problem."
    "I take a deep breath."
    mS "CAW CAW HISS HISS"
    "We all laugh"
    enS "LEGENDS!! LONG LIVE THE OAKLEY!!!"
    "Teresa sticks something to the statue and leaps off."
    enS "Hehe catch me!"
    "I'm barely able to catch her in time."
    mS "I got ya!"
    "I carry Teresa in my arms, Jennica trailing quickly behind just as the bomb detonates and blows the statue sky high."
    show teresa stream happy at stream_right with dissolve
    enS "Some of my finest work for sure."
    mS "I'd bet money this place hasn't seen a bigger stunt than that."
    amaS "...You bet?"
    "I jump and turn to the direction of the voice, this time I make it to my gun."
    "When I come to I realize I've scared the young showgirl behind me near to death."
    hide teresa with dissolve
    show showgirl stream at stream_center with dissolve
    mS "What?"
    $ reactTarget = "vig3_sc5_amahallu"
    show screen streamerCommentary
    "She stares wide eyed and is taken her off script."
    showgirl "Uh um, name's Daisy, do you bet?"
    mS "Do I bet if your name is Daisy?"
    showgirl "Well if you did you'd be a winner..."
    "She pauses, recalling the words back to her."
    showgirl "and you can win bigger at NOVA CASINO!"
    showgirl "First 50 Credits are on us!"
    "She attempts to hand me a casino card, it's holographic with an animation of a supernova and 50 credits in big lettering."
    mS "Thanks but no thanks."
    showgirl "Well.."
    showgirl "Have a nice day!"
    hide streamerCommentary
    "Daisy hurriedly leaves and heads to another group to perform the same spiel. I see her carefully get their attention this time."
    hide showgirl with dissolve
    show teresa stream shock at stream_right with dissolve
    show jennica stream shock at stream_left with dissolve
    show mac stream shock at stream_left5mac with dissolve
    show rec stream surprised at stream_right5 with dissolve
    pS "Alright alright, what's this about?"
    enS "You've been anxious all day Captain."
    mS "I'm fine."
    recS "You just yelled at girl wearing feathers, I beg to differ."
    macS "We are concerned."
    mS "I'm tired is all."
    show teresa stream neutral
    show jennica stream neutral
    show rec stream neutral
    show mac stream neutral
    recS "You know most of the shops are closing for the day. Let's set you up somewhere for the night."
    recS "I think the Burnt Bulb has a deal on pints."
    "We begin to move out. Jennica begins a story involving a lamp, three chickens, and a guitar. MAC is confused but enthralled."
    hide jennica with dissolve
    hide teresa with dissolve
    hide rec with dissolve
    hide mac with dissolve
    "I can't help but look back at Daisy with the small rough-looking crew."
    "Her eyes fixated on the only person whose back is turned to me."
    "They're tall and well built with a wide brimmed hat, in dark leather, and long familiar black hair."
    show mac stream happy at stream_left_mac with dissolve
    macS "Are you coming Captain?"
    "I stare at the crew as they walk away."
    mS "Sure thing kid."
    hide mac with dissolve
    jump vig3_sc6

label vig3_sc6():
    hide akarplaza_stream
    show bbpub_stream at topleft onlayer background with dissolve
    "The days are shorter this time of year and when night falls we make it to the Burnt Bulb."
    "It took some time to get through Akar, MAC wanted to see everything he could."
    "As if it would disappear if he took his eyes off it."
    "The Burnt Bulb Pub feels like it's been stuck in time. 
    It's wooden paneling, the carnivorous plants that line its ceilings."
    "There's a warmth to this place, I feel like that young Outlaw scared out of my mind, clinging to Ama and hoping I won't get bulldozed at my first brawl."
    show rec stream happy at stream_right5 with dissolve
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    show mac stream neutral at stream_left5mac with dissolve
    macS "Cozy."
    "In the back, someone yells and is then quickly tossed through a window."
    "MAC's face drops and he clings to my leg."
    show mac stream shock at stream_left5mac
    macS "Aren't their children around outside?"
    pS "That's why he was tossed out the back window."
    enS "This is a respectable place after all."
    recS "Only the best for the Oakley."
    recS "Hopefully they're not booked up 'cause of the Fair."
    enS "Let's find out."
    hide rec with dissolve
    hide teresa with dissolve
    show mac stream neutral at stream_center with move
    show jennica stream neutral at stream_center with move
    "As we walk through the bar, I notice how may regulars have been lost to time.
    Akar is different now."
    menu:
        "How do you feel about how Akar has changed?"
        "Being invisible is what we need.":
            "There's a small comfort in not being immediately recognized."
            "It's better for MAC."
            pS "Y'alright Cap?"
            mS "Yeah let's just get through and find a spot."
            "The new crews are quite the sight."
            "The gear is impressive."
            "A little intimidating..."
            "We hug a wall and find any available table."
            macS "Woah..."
            "I move MAC away from staring too long  at a particularily burly Outlaw and smile nicely."
            "When we find the table, I gently push off a passed out patron."
            "Teresa and Rec come back to us with our first round." 
            "I buy us the next one."
        "Surely not everyone forgot us.":
            "I'm sure some more people remember who we are."
            ms "See anyone familiar?"
            "Jenn takes a moment to survey the space."
            pS "Think we might've missed the reunion."
            ms "Ha, looks like it."
            "We move through the bar and I scan for any familiar faces."
            "Or any face that seems friendly."
            "Apart from a waitress who waved at us or of courtesy, no one."
            "When we find our table, I gently push off a passed out patron lying on it."
            "Teresa and Rec come back to us with our first round." 
            "I buy us the next one."
        "Let's make sure they don't forget us.":
            "I don't care how long its been the Oakley is still legendary."
            "Maybe we should remind them who we are..."
            "We barrel through the crowd to find a table."
            mS "Make way for the Oakley everyone!"
            mS "C'mon let's move, let's move!"
            pS "Oh we're doin' this?"
            "I give Jenn a wink and she smiles."
            pS "You heard the Captain, move it or lose it!"
            "I bump into a particularily scary guy who decides to take a swing at me for my indescretion."
            "I make sure he meets the floor quickly." 
            mS "Pardon us."
            "I step over his curled up body."
            "When we find our table, I gently push off a passed out patron lying on it."
            "Teresa and Rec come back to us with our first round." 
            "I buy us the next one."
    "And then another."
    "And another."
    show jennica stream neutral at stream_left with move
    show mac stream neutral at stream_left5mac with move
    show rec stream drunk at stream_right5 with dissolve
    recS "So I said, \"You should've been more specific about the screw!\""
    show teresa stream happy at stream_right with dissolve
    show jennica stream neutral at stream_left with dissolve 
    "Raucous laughter pours out of us, barely audible in this crowded bar."
    enS "Makers, that's dumb."
    macS "Now I found that funny but can someone clarify the part about the screw?"
    enS "Well you see \"screw-\""
    show jennica stream shock at stream_left
    "Jennica covers what she thinks are MAC's ears."
    pS "Too young, too impressionable."
    show teresa stream neutral at stream_right
    enS "He's a courier bot, it's fine."
    show jennica stream angry at stream_left
    macS "That's not where my ears are."
    pS "C'mon a bot? Get out!"
    macS "That is not an incorrect statement."
    show teresa stream upset at stream_right
    enS "Why must you be so emotional about everything?"
    pS "And why ya gotta be a cold hearted b-"
    show mac stream shock at stream_center with move 
    show rec stream surprised
    $ reactTarget = "vig3_sc6_crewspat"
    show screen streamerCommentary
    recS "WOAH! How about I go and get us another round."
    show rec stream happy
    recS "C'mon buddy, I'll get you a treat."
    hide rec with dissolve
    hide mac with dissolve
    "MAC looks at me expectantly."
    mS "In eyesight, got it?"
    "MAC lets out an excited noise and heads to the bar with Rec."
    "The table is silent."
    mS "I owe you both an apology"
    "Jennica and Teresa perk their heads towards me."
    hide screen streamerCommentary
    show teresa stream neutral at stream_right
    show jennica stream neutral at stream_left
    mS "I'm not going to say that I regret what we did in Gibian V, that doesn't matter now."
    mS "But I can't have the two of you blowing up at each other over something I decided."
    mS "When it comes down to it, we need to look out for each other." 
    mS "You're the ones I can rely on, the only ones I trust and I need that to be the same between all of us."
    show jennica stream neutral at stream_left
    show teresa stream happy at stream_right
    "When the two of them begin to smile at each other I know that something I said stuck."
    enS "You know I was wondering when we'd get an inspiring heart to heart from you."
    pS "I'm thinkin' that cracks the top five."
    enS "Not as good as the one on Firma 12. How did that one go?" 
    enS "\"We're family, a crazy, wild, dysfunctional family-\""
    pS "\"But that's what makes us special!\" I'm tearing up thinking 'bout it."
    mS "Okay, okay, that's enough"
    "Jennica raises her glass."
    pS "We got your back Moze."
    "Teresa raises her glass."
    enS "Always."
    "I raise mine in response."
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
    "There's a chill that runs down my spine."
    ###Recount choice again###
    menu:
        "Do I investigate this stranger?"
        "Follow them":
            $ reactTarget = "vig3_sc6_stranger"
            show screen streamerCommentary
            "I follow the stranger out of the bar and every fiber in my being is yelling at me that this is a bad idea."
            hide bbpub_stream with dissolve
            show akarplaza_stream at topleft onlayer background with dissolve 
            "I struggle to navigate the dark winding streets of Akar." 
            "The chaos is picking up as the night continues." 
            "I almost lose the stranger as they tuck away behind an alley and I move to close in on them."
            "As I turn the corner I'm met with a knife to my throat."
            "So clearly not Ama's style."
            show stranger 1 stream at stream_center with dissolve
            "The stranger eyes are bright and blue. They're face pretty and heart-shaped face with a mole under her left eye."
            strngr1 "Why are you following me?"
            mS "I just-"
            "She presses the knife into my neck."
            strngr1 "You what? Thought I was some easy mark."
            "She's young in her voice and in her confidence."
            mS "No, I just thought you were someone else."
            "She doesn't let go of the knife."
            strngr1 "Well sorry to disappoint. But I don't take kindly to being followed."
            hide screen streamerCommentary
            "I should say something to get out of this." #Options: Hands up and walk away, flirt, wrestle the knife away.
            menu:
                "How do I get out of this?"
                "Flirt.":
                    mS "Oh, I'm far from disappointed." #flirt
                    "A small smile rises on her face."
                    strngr1 "Oh yeah?"
                    mS "You're a much more pleasant sight if I say so myself."
                    "She doesn't let go of the knife but moves in closer."
                    strngr1 "You're not an eyesore yourself."
                    mS "Ouch I'm hurt."
                    strngr1 "Not yet, but the night's young."
                    "When the knife falls we close the distance and tuck ourselves deeper in the alley, far away from eyesight."
                    hide stranger 1 stream with dissolve 
                    "I return to the Burnt Bulb a bit disheveled hoping that the small nick on my neck has started to scar over."
                    "I go to see Mac and Rec."
                    hide akarplaza_stream
                    show bbpub_stream at topleft onlayer background with dissolve
                "Hands up, walk away.":
                    mS "Look this got out of hand."
                    "I hold my hands up and start at her trying to relax the situation."
                    strngr1 "Ha, what can't follow through?"
                    mS "Nothing to follow through on."
                    hide stranger 1 stream with dissolve 
                    strngr1 "Pathetic."
                    "Her knife doesn't move but she nods her head to tell me to get lost."
                    "I don't take my eyes off her when I back away"
                    "I return to the Burnt Bulb disappointed."
                    "I go to see Mac and Rec."
                    hide akarplaza_stream
                    show bbpub_stream at topleft onlayer background with dissolve
                "Wrestle the knife away":
                    mS "I don't have time for this."
                    "I grab her wrist before she can cut me open and twist her arm down and away."
                    menu:
                        "Make it hurt?"
                        "Yes. Just like Ama taught me.": 
                            "She yells as something snaps."
                            strngr1 "Po dunk!"
                            "Sweat is pouring down her face."
                            "I slam a knee to her chest."
                        "No. I've made my point.": 
                            "I shove her against the wall and she falls over."
                            "The knife clatters away."
                    "It's over before it even starts."
                    mS "Need me to call someone for you?"
                    strngr1 "Go to hell."
                    mS "Trust me they know I'm coming."
                    hide stranger 1 stream with dissolve 
                    "On my way back to the Burnt Bulb I can feel eyes on me."
                    "I take careful steps."
                    "When I get to my destination I and wipe a bit of dust off my jacket before heading in."
                    "I go to see Mac and Rec."
                    hide akarplaza_stream
                    show bbpub_stream at topleft onlayer background with dissolve

        "Check in on MAC and Rec":
            "I can't follow paranoid hunches, I gotta stick to my crew."
            "Rec and MAC are chatting at the bar, I get the tail end of their conversation."
            show rec stream drunk at stream_right with dissolve
            show mac stream neutral at stream_left with dissolve
            recS "You know when you've lived here for so long you get used to it truly."
            $ reactTarget = "vig3_sc6_recbonding"
            show screen streamerCommentary
            macS "But it's so dangerous, are you not worried?"
            recS "Of course I worry, but no use in worrying all the time."
            menu: 
                "Say something."
                "They're right you know.":
                    mS "They're right, just because something is difficult doesn't mean you need to worry all the time."
                    mS "How you work through that is more important."
                    macS "I think I understand."
                    show rec stream happy at stream_center with dissolve
                    recS "You know Moze I do admire what you do, it's a tough life but it's yours."
                    "I smile."
                    mS "It has it's good moments."
                    macS "Like candy!" 
                    mS "Exactly. That's why we go through the worry."
                    recS "You know..."
                    recS "I was so scared when Allistar decided to join the Snakehawks."
                    recS "But I'm happy he had you with him."
                    recS "It made me worry less."
                    mS "Rec I should tell you-"
                "Rec should really consider moving.":
                    mS "Rec ever thought that moving would be the right call?"
                    recS "Oh that's rich coming from you."
                    mS "I'm just saying there's better places than this one."
                    mS "With less Hounds."
                    recS "I like my shop and my community, I don't regret planting roots here."
                    recS "Plus when Allistar was with the Snakehawks I always knew you'd be here after your missions."
                    recS "I'm happy I got to see him as much as I did."
                    "A pit forms in my stomach."
                    mS "I didn't mean to offend."
                    mS "You found a place that is yours."
                    recS "I'll be sure to fight for it."
                    mS "Rec I should tell you-"
                    hide rec stream happy with dissolve
                "Akar is beautiful if you look in the right places.":
                    mS "It may not look it but Akar is beautiful."
                    mS "Didn't you see all the colour and community here?"
                    mac "People were getting hurt."
                    mS "Sure, but that's not all the time and people et hurt everywhere."
                    recS "That doesn't mean you can't surround yourself with good people."
                    macS "Like what we have?"
                    mS "Yeah kid."
                    show rec stream happy
                    recS "So cute..."
                    "I feel my face get warm. Then an undeniable pit forming."
                    
                    show rec stream neutral
            "A part of the bar goes silent as a bald burly man stands to address the crowd."
            hide mac with dissolve
            hide rec with dissolve
            hide screen streamerCommentary
            show zan stream at stream_center with dissolve
            zan "Patrons! Who is brave enough to ride Karousel!"
            "Oh god not this game. What kind of idiot would even take that challenge-"
            pS "Right here!"
            "Jennica marches to the man who laughs."
            show jennica stream neutral at stream_left with dissolve
            zan "So small, already tipping over, I fear you may not survive haha!"
            "A small group of patrons at a table behind him laugh."
            pS "Then you have nothin' to worry about."
            zan "Apologies but I will not pick you up from the floor when you lose."
            pS "Please."
            "Teresa saddles up next to Jennica."
            show teresa stream happy at stream_right with dissolve
            enS "The lady said she'd like to ride the Karousel."
            zan "Two of you! I'll need a bigger mop!"
            "A woman from the table flanks him, she rivals him in size."
            enS "So does that mean you're ready to play?"
            zan "HAHA, I like you, moxie!"
            pS "Moxie's our middle name."
            zan "That is strange...but ZAN APPROVES!"
            "He lifts up two thumbs and points to himself then speaks to the woman in a language I do not understand."
            "She nods and picks up a large table to make the play area. Jennica and Zan speak for a moment before shaking hands."
    #This will be where we start after the stranger track#
    zan "The bet is done! Mr. Stein. Zan requests The Karousel please!"
    "Bet? What bet?"
    "A small man holds up the Karousel high over his head, I barely see him before it appears on the table and the door to the back room swings closed."
    hide jennica with dissolve
    hide teresa with dissolve
    hide zan with dissolve
    show mac neutral stream at stream_left_mac with dissolve
    show rec stream drunk at stream_right with dissolve 
    macS "Are they playing Brikarousel?"
    recS "Aren't you too young to know that game?"
    macS "I have a full database that allows me to know a myriad of games."
    show rec stream thinking
    recS "A full database..."
    "Rec's eyes move back on the gambling table, Jennica and Teresa are deep in conversation."
    recS "You know I never understood this game."
    macS "Well Brikarousel was invented by Brika Alphonse approximately 30 years ago when..."
    show rec stream drunk
    recS "I meant why people are so eager to play."
    macS "Oh."
    macS "Alcohol?"
    mS "You catch on quick."
    "I look over at the table as a pit in my stomach forms."
    mS "Bet? What did they bet?"
    show rec stream thinking
    recS "I didn't hear but I read lips a bit, a “sh” something?"
    mS "\"Sh\" something???"
    macS "Shirt, shoes, shilling..."
    "Ship?"
    "They wouldn't-"
    $ reactTarget = "vig3_sc6_shipbet1"
    show screen streamerCommentary
    hide rec with dissolve
    hide mac with dissolve
    "No that's stupid."
    recS "Shorts? Shawls..."
    macS "Squash!"
    "..."
    "Okay now that's stupid."
    "Teresa and Jennica bet the Ship."
    "Shit."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    show zan stream at stream_center with dissolve
    "A small man with dark hair and modified gray skin steps to the table."
    pS "Talkin' to us about bein' small and your guy is thinner than my jacket."
    zan "Ovid is strong of heart, muscles on the inside."
    enS "That tends to be where they go yes."
    ovid "Zan must we always play this game whenever we go out?"
    zan "..."
    zan "YES!"
    "The game starts off with a bang, the rules are simple, teams of two play hands to collect played cards from a pool." 
    "Some cards are worth points, the pair with the lower amount of points at the end of the round takes a shot from the Karousel."
    "The first team that withdraws or has a member drop loses."
    "...By round ten, it's not looking good."
    hide screen streamerCommentary
    zan "How is moxie?"
    pS "Stronger than my mama's back!"
    enS "I'm starting to feel mine in the back of my throat."
    "Teresa and Jennica look wrung out but Zan and Ovid are sturdy despite drinking their fill."
    hide jennica with dissolve
    hide teresa with dissolve
    hide zan with dissolve
    show mac neutral stream at stream_center_mac with dissolve
    show rec stream drunk at stream_right with dissolve
    macS "They're cheating."
    show rec stream surprised
    recS "How did you-"
    mS "Of course! We've been out of the game too long."
    macS "We must tell someone, this is improper."
    show rec stream drunk
    mS "MAC I'm going to lay this out for you. No one cares if something is improper here."
    macS "Then we should do something."
    mS "I'm already on it."
    macS "And I'll help."
    menu: 
        "Say something."
        "Abosultely not!":
            mS "You will sit down and say nothing and let me handle it."
            macS "But I-"
            mS "But nothing, I don't need a liability right now. Understand?"
        "It's better if I just do it.":
            mS "This is better as a solo mission."
            macS "But I-"
            mS "I know you want to help but some things work better with less people."               
    macS "But I'm part of this crew too!"
    "That was my voice."
    "Upset, scared of being left behind."
    mS "You are, and you'll have other chances to prove it. Just not right now."
    "When Jennica calls for a short recess I know that's my time to head over."
    hide rec with dissolve
    hide mac with dissolve
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    mS "I don't know if you've noticed..."
    pS "We're losing-"
    enS "They're cheating."
    enS "So are we just not as effectively."
    mS "Better think of something fast after what you just bet."
    pS "Ya Resa, I don't think hand signals are going to cut it here."
    "I swallow the knowledge that hand signals were the only thing they thought of after betting our ship."
    menu: 
        "There has to be signs for how they're doing this."
        "Check Ovid":
            "Ovid stares blankly across the room poking at something metal in his mouth."
            pS "Ovid's not drinking."
            enS "An evaporator..."
            pS "Was wondering how that little guy is still standing."
            "I look around the room for more signs."
    menu: 
        "There has to be more signs for how they're doing this."
        "Check the deck":
            pS "The deck isn't right. I know a standard set when I see one."
            mS "That makes sense, especially if they're regulars."
            enS "Truly? All for a stupid game?"
            "What else?"
    menu: 
        "There has to be more signs for how they're doing this."
        "Check the Karousel":
            "Teresa's eyes are fixed on the Karousel."
            mS "The Karousel?"
            enS "There's a delay before it settles. And one of their friends has been staring at his communicator all night."
            "I think that's all."
    "Ovid's tube, the deck, the Karousel. We have to deal with them."
    pS "We need to tip the table."
    enS "Can't do that while we play."
    mS "I got it covered, just stay standing until I do."
    "The game resumes and I step away."
    show zan stream at stream_center with dissolve
    zan "Now! Moxie!"
    "I scan my options."
    "If I start a fight I'm sure I can get someone slammed into the table." 
    "That should take care of some of the issues."
    "I look at the ceiling where the carnivorous plants lie waiting and salivating."
    "One of the ropes for their netting looks frayed and worn if I undo it then it's open season on that table. Maybe quits for the Karousel."
    "As I scan my options I can feel MAC's eyes on me."
    "He's really not gonna like this at all."
    hide zan with dissolve
    hide jennica with dissolve
    hide teresa with dissolve
    menu:
        "How do I help Jennica and Teresa?"
        "Start a bar fight.":
            "I see a young couple pinning each other on a pillar near the table." 
            "They're really in it."
            "Ah young love, so easy to break."
            "When they separate I go up to the young man and shove him."
            mS "How dare you! We spent five glorious nights together, you tell me you love me..." 
            mS "And after MONTHS of not hearing from you I find you here with a random woman!"
            "His jaw is on the floor."
            wifenpc "Random! I'm his wife!"
            husbnpc "What? huh? I don't-"
            mS "Oh typical, you don't what? Know me? Don't even remember proposing to me do you?"
            wifenpc "PROPOSE!!!!"
            wifenpc "So that's what you've been doing on your business trips huh?"
            husbnpc "No-what?!? I don't even know her!"
            "Before I can even add fuel to the fire."
            "The youg woman hits him with a one-two combo that almost lands her a spot on the Oakley." 
            "He fumbles onto Ovid and the table."
            "Cards fly everywhere and before I can process what happens Zan has the man in a chokehold."
            show zan stream at stream_center with dissolve
            zan "You interrupt the Karousel!"
            "It's hand fifteen, and half the bar is up in arms."
            "Friends of the man square up with Zan's crew."
            "It's only when tiny Mr. Stein waddles to the table and promises a free round that the room begrudgingly settles."
            "Ovid coughs loudly before putting something in his pocket."
            "with cards scattered all over the floor the deck is replaced."
            "The Karousel is untouched, the rounds continues."
            hide zan with dissolve
        "Cut the rope holding the carnivorous plants":
            "I take a look at the frayed rope and the netting that is so carefully holding back the plants."
            "How has no one changed the rope yet?"
            "It's too easy and so dangerous."
            "I move carefully to the hook with the rope."
            mS "Excuse me sorry just tryna get a decent view"
            husbnpc "Watch it man, c'mon we all want a good view."
            "I push my way to wall and lean just behind it."
            "The rounds continue."
            show zan stream at stream_center with dissolve
            zan "Another victory, another shot for you."
            show jennica stream angry at stream_left with dissolve
            pS "Fine meathead, you got it."
            show teresa stream neutral at stream_right with dissolve
            enS "Makers this is insanity."
            "Then I get an idea."
            mS "Drink! Drink! Drink! Drink!"
            "The bar is in an uproar people are going to grab their nearest cups."
            "They're slamming the floor, the room is shaking"
            "A roaring cheer, I cut the rope."
            "The scream that is let out is so high, I couldn't believe it came from Zan."
            zan "YEEEEEEOWWWWWWWW"
            zan "They're alive!!!"
            "He swatting at them like whack-a-moles. One plant's head pops like a grape."
            enS "Stein get these out of here."
            zan "Ah ah AHHHHHHHHHHH"
            "Ten patrons were injured from Zan's wild flailing, the attacking plants destroyed."
            "Stein with the help of his crew subdued the other plants and have begun to put up new netting."
            "Zan's eyes dart from the game to the ceiling."
            "Ovid coughs loudly before putting something in his pocket, The Karousel is replaced by an older model."
            "The round continues."
            hide zan with dissolve
            hide teresa with dissolve
            hide jennica with dissolve

    #maybe fade in and out to show passage of time again?#
    "Round 25 is rough. Even with some of the obstacles out of the way Teresa and Jennica are barely holding on." 
    "Ovid is finally looking like he's playing the game and Zan is rocking in his seat like a child."
    ovid "Please, call it quits?"
    show teresa stream neutral at stream_right with dissolve 
    enS "Not likely."
    show zan stream at stream_center with dissolve
    zan "Hehehe, I say I am impressed. And having the best of times!"
    show jennica stream neutral at stream_left with dissolve
    pS "Not after this you aren't."
    "When Zan and Ovid lose the round an opportunity presents itself." 
    "Zan will tip his chair back to take his drink."
    "One clean shot to the leg and he's on the ground."
    "But that's risky."
    "I could just leave it to the two of them to take it home, Ovid looks like he's on his last legs."
    "But if they actually bet the ship then I don't know how we're gonna get it back."
    ###Two choices and three endings. If the player doesn't shoot they may or may not win which will have two separate endings. If they do shoot they will automatically win, this is also the Ama choice###
    menu:
        "How do I finish this?"
        "Shoot Zan's Leg":
            $ outlaw += 1
            $ macViolence += 1
            $ macPessimism += 1
            "I can't leave it up to chance, the crowd is completely absorbed by this game."
            "Zan has a notable plate on his leg, a good shot should send him flying with minimal damage. Hopefully."
            "I take my position."
            "As I scan the bar for any eyes on me, I take in just how packed this place is. It's wall to wall."
            "Then I see them, a small group near the door, half watching the game."
            "Is that?"
            "No."
            "My vision is still betraying me and I don't have time to get a better look."
            zan "FOR MY LOYAL FANS!"
            "Zan does a messy cheers to Ovid, teeters his chair back to knock the shot into his mouth."
            "As I pull the trigger... Zan's eyes meet mine."
            "Damn."
            $ reactTarget = "vig3_sc6_shootingzan"
            play audio "lazer.wav" volume 5.0
            hide zan with Dissolve (0.1)
            "Zan falls hard, the pub is silent."
            show screen streamerCommentary
            pS "HELL YEAH!!!"
            show jennica stream neutral at stream_left
            show teresa stream happy at stream_right
            "The crowd erupts, Zan's crew is visibly miffed but the rest of the bar is patting Teresa and Jennica on the back."
            show zan stream at stream_center with dissolve
            "Zan gets up to accept defeat, Ovid has fully crawled under the table."
            "I look over again to the crew, but that table is empty."
            "The door swings closed."
            ovid "Thank the Makers it's over."
            zan "Good, good! NOW!" 
            zan "I must go and throw up. HAHA!"
            "The three exchange handshakes as Zan passes by me and stops."
            hide jennica stream 
            hide teresa stream
            zan "You are Captain, no?" 
            menu: 
                "Respond to Zan."
                "And what's it to you?":
                    mS "And what's it to you?"
                    zan "You have a good crew, good moxie."
                    mS "I'm aware."
                "The one and only!":
                    mS "The one and only!"
                    zan "You have a good crew, good moxie."
                    mS "We like to show out."   
            "Good shot, but messy."
            "Have more faith next time."
            "Before I can respond, he pats my shoulder and I almost buckle under the weight of the impact."
            hide screen streamerCommentary
            hide zan with dissolve
            "I move to greet my victors."
            mS "I can't believe we pulled that off. That was some risky business."
            pS "C'mon Cap, just harmless fun."
            "... what?"
            mS "Betting the ship is harmless to you?"
            enS "The ship? What do you take us for?"
            enS "Zan asked us to perform a show for the bar if we lost."
            mS "A show?"
            pS "Mighty embarassin' that've been."
            pS "Everyone knows Resa sounds likes a torn up gear when she sings."
            enS "Agreed."
            pS "But alls well, big guy told us he'd comp our room for the night."
            "...I'm truly losing it."
            mS "Alright, well congrats then. I'm turning in."
            hide teresa with dissolve
            hide jennica with dissolve
        "Trust the crew to win.":
            $ marshal += 1
            $ macHope += 1
            $ macPeace += 1
            #need a variable to determine if they win or not.
            $ reactTarget = "vig3_sc6_trustcrew"
            show screen streamerCommentary
            "There's a part of me that know I'll regret this but I don't go for my pistol."
            "These two are idiots but they're my idiots."
            "And I have to trust they'll pull through."
            "The game keep going."
            "So do the drinks."
            "26, 27, 28..."
            "...29..."
            "Then a loud crash."
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
                "Zan pushes the table away and goes to make sure Ovid is alright "
                hide zan with dissolve
                "I move to greet my victors."
                mS "I can't believe you pulled that off. That was some risky business."
                pS "C'mon Cap, just harmless fun."
                mS "Betting the ship is harmless to you?"
                enS "The ship? What do you take us for?" 
                enS "Zan asked us to perform a show for the bar if we lost."
                $ reactTarget = "vig3_sc6_shipbet2"
                show screen streamerCommentary
                mS "A show?"
                pS "Mighty embarassin' that've been, Everyone knows Resa sounds likes a torn up gear when she sings."
                enS "Agreed."
                pS "But alls well-"
                "...I'm truly losing it."
                "Just then Zan comes over to us and kneels."
                show zan at stream_center with dissolve
                zan "I must make good on promise."
                "Teresa and Jeneca each take a seat on one flexed arm."
                "Zan hoists them in the are and parades them around the bar."
                zan "MOXIE MOXIE MOXIE MOXIE!"
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
                "Zan pushes the table away and goes to hug Ovid who looks like his eyes are about to pop out."
                hide zan with dissolve
                "I move to help Jennica."
                enS "C'mon Jenn, you're good, you're alright."
                pS "Did... Did we win?"
                enS "Sorry sweerheart we didn't."
                mS "Makers, why did you bet the ship?"
                enS "The ship? What do you take us for?" 
                enS "Zan asked us to perform a show for the bar if we lost."
                $ reactTarget = "vig3_sc6_shipbet2"
                show screen streamerCommentary
                mS "A show?"
                pS "A show! Oh scrap, you sound horrible when you sing Resa."
                enS "Still better than you."
                pS "But we must press on! *hick*"
                "...I'm truly losing it."
                "Just then Zan comes over to us."
                show zan at stream_center with dissolve
                zan "You must make good on promise."
                "Teresa helps Jennica get up and they stand on the Karousel table."
                "Zan yells for music." #The melody is "C'est a ton tour"
                "Teresa and Jennica begin to sing"
                pS "Zan is the man! Zan has a plan! Zan's got the muscles to beat any man." 
                enS "Ovid's the best! Above all the rest! With muscles inside to pass any test."
                "When they look back I give them a nod like I'm ready to turn in."
                "They continue in broken harmony" 
                hide teresa with dissolve
                hide jennica with dissolve 
                hide zan with dissolve        
    hide screen streamerCommentary            
    "I head back to Rec and MAC."
    show rec stream drunk at stream_right with dissolve
    show mac stream neutral at stream_left_mac with dissolve
    mS "I'm taking the kid, we'll check in with you tomorrow at the shop, alright?"
    recS "Sure thing Cap."
    show rec stream thinking
    recS "Actually Moze wait."
    "They look serious."
    mS "What's going on?"
    recS "MAC isn't a normal bot is he?"
    "I take a moment and look down at MAC."
    "It's been long enough."
    mS "No... he's not."
    recS "BigCorp has been deploying agents everywhere."
    recS "They're looking for something {i}big.{/i}"
    recS "Lots of rumors about what that could be."
    "MAC looks away." 
    mS "So then you can imagine why we can't let them have him."
    "Rec looks down at MAC."
    show rec stream happy
    recS "He's a special kid."
    "Something flashes behind their eyes. I remember Allistar."
    recS "We'll keep looking for that part tomorrow."
    "MAC waves to Rec as they leave."
    recS "See ya buddy."
    "We turn in."
    hide rec with dissolve
    hide mac with dissolve
    jump vig3_sc7

label vig3_sc7():
    hide bbpub_stream 
    show akarplaza_stream at topleft onlayer background with dissolve
    "The next day is hot, the hangover in my brain is smashing at my skull like it's the bars of a prison."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    enS "All day searching, and nothing?"
    pS "Well there was that one guy."
    mS "He tried to sell a walking stick he carved when we asked for a range extender."
    pS "I thought it was quite lovely."
    "MAC is silent."
    mS "Alright kid?"
    show mac stream neutral at stream_center_mac with dissolve
    macS "Yes, I hope we can find a lead soon."
    menu:
        "Respond to MAC."
        "Cheer up bud!":
            mS "Cheer up kid, we'll find it!"
            "MAC looks unconvinced. And tired?"
        "We'll find it I promise.":
            mS "It'll just be a little longer but we'll find it."
            "MAC looks unconvinced. And tired?"
    ##Conversation with MAC?##
    hide mac with dissolve
    "Rec gave us some good starting points but after searching for hours we've notice most operations aren't running with their usual stock because of the Inventor's fair."
    mS "We might need to split up."
    enS "I agree we'll cover more ground."
    pS "Are we just looking to buy?"
    #player choice
    menu:
        "How do we want to approach getting the antenna?"
        "Whatever it takes.":
            mS "Do whatever it takes, we need that part and we'll take it if necessary."
            pS "All in then. Got it."
        "Don't cause any unnecessary drama.":
            ms "We need to do everything we can to get that part but we can't cause problems."
            enS "Go for option A, option B if necessary."
    enS "I'll head to the plaza, Jennica the outskirts, Moze you take MAC and do another sweep of the shops near Rec."
    mS "Perfect Resa, let's get started then. Now MAC-"
    "Fear surges through my body as I look between the three of us and MAC is nowhere to be found."
    $ reactTarget = "vig3_sc7_lostmac"
    show screen streamerCommentary
    mS "MAC!"
    hide teresa stream with move
    hide jennica stream with move
    "I know Teresa and Jennica are screaming for him but I can't hear them, I can't hear anything but my heart pounding in my chest."
    "Where is he?"
    "WHERE IS HE?"
    "Then I see him far in the distance, wheeling himself slowly to a group of people."
    "To a group of Hounds."
    "My feet move before my brain can register what is happening."
    "It happens so fast, MAC runs into the leader, his arms frantic."
    "They swarm him, my feet aren't moving fast enough."
    "I can't think of anything but how fast my legs should be moving." 
    "MOVE FASTER."
    "When they take him and drive away, I don't register how a cruiser almost hit me, I don't feel the pain of my knees when they hit the ground."
    "All I can hear is Ama's voice in my head, \"You'll have the chance to prove it, just not right now.\"" ##Consider changing this line##
    hide screen streamerCommentary
    hide jennica with dissolve
    hide teresa with dissolve
    jump vig3_sc8

label vig3_sc8():
    hide akarplaza_stream with dissolve
    show bg black at topleft onlayer background
    "I don't remember much after."
    "We knew we couldn't chase down the Hounds. There was nothing that could be done once MAC was out of sight."
    "It was Rec who gave us the suggestion to intercept them where they were. That meant in the belly of the beast, Reynar's Vineyard."
    "It was nothing short of the worst case scenario."
    hide bg black with dissolve
    show exteriorvineyard_stream at topleft onlayer background
    pS "You know I'm not a fancy sort of gal, but my butt looks fantastic in this."
    show jennica stream neutral at stream_left with dissolve
    "Jennica has not stopped looking at herself in every reflective surface since arriving here." 
    "Not surprised that the first thing she does out of the luxury cruiser is stare at herself in the window."
    pS "Sorry Jimmy, gotta make sure the girls are in order before I do some serious ass-kicking."
    "Jimmy is a friend of Rec's who owns a luxury cruiser company and thankfully owed them a favor."
    show teresa stream neutral at stream_right with dissolve
    enS "Can you give it a rest, there are people around."
    pS "I thought you'd want me to look presentable?"
    mS "You need to be serious about this."
    pS "Oh I'm very serious, just my face don't look it. Y'all should consider fixin' yours."
    "Rec moves thier jaw as if trying to manually relax it."
    "I relax my shoulders as an attendant walks over to us."
    vyattend "Good afternoon, my name Ryo and it is my pleasure to welcome you to the Vineyard." 
    vyattend "Are you perhaps here for the Inventor's Fair?"
    enS "Pleased to make your acquaintance Ryo. Please check the list for Vira Prismari and retinue."
    "They raise an eyebrow before checking a screen."
    vyattend "Prismari?"
    enS "That is correct." 
    "There's a long pause."
    reynar "Ryo I'll take it from here."
    "Our jaws nearly drop at the finely dressed man who approached us. Reynar..."
    show reynar stream neutral at stream_center with dissolve
    reynar "How wonderful, we were certain to receive another refusal gift this year."
    enS "Well we so desperately missed the inspiration of the Inventor's Fair."
    enS "I hope you are well to accommodate us?"
    reynar "I must say your posse is such a surprise it's so... pleasantly unexpected."
    "It's like watching a tennis match with a bomb for a ball."
    enS "You know we are so thankful your consideration every year, and so lovely to see our donations put to such good use."
    enS "You've truly spared no expense."
    reynar "Of course, we want to celebrate all those who contribute to the research and development of the Outposts."
    enS "The Prismari family is always proud to support this iconic hub of innovation."
    reynar "You've offered much more than support."
    reynar "We are pleased to have you back Miss Prismari."
    "Reynar nods to us and walks away cooly. Leaving to welcome in other guests."
    hide reynar stream with dissolve
    $ reactTarget = "vig3_sc8_teresabluff"
    show screen streamerCommentary
    pS "You're a bit scary when you're proper."
    show rec stream thinking at stream_center with dissolve
    mS "You sure what just happened back there was alright?"
    enS "If Reynar really wanted us out he would've done so already."
    pS "So why didn't he..."
    mS "Does he think your family will take care of it?"
    enS "Please. My family hasn't come to these since I was exiled. Doubtful they'll even know I was here."
    enS "We're in, that's what matters."
    mS "Got it."
    enS "And thank you Reccrin. Couldn't have done it without you getting us ready."
    show rec stream neutral
    recS "I've been here for years and never set foot in the Inventor's Fair. I'd give you my whole shop if ya needed."

    show inventorfairgallery_stream at topleft onlayer background with dissolve 
    "The Inventor's Fair is even more insane looking than I could've imagined. The fanfare in Akar is a kid's birthday party by comparison." 
    "Brimming with shine and luster. Inventors setting up sections with their project."
    "Finely dressed guests being served by his android wait staff." 
    hide screen streamerCommentary
    "Carefully plated exotic food and drink fill the silver trays that circulate the a gallery-style showroom."
    enS "Apparently the theme is Lost Renaissance, remembering a time long past..."
    pS "That why some of these statues don't have arms?"
    "It's excess at its highest degree, it's so much that I can't imagine us finding MAC in all of this."
    recS "Reynar likes to personally assess what the Hounds find so they're probably holding MAC somewhere close by."
    pS "Let's rough up some suits and find out where they've got him."
    "Teresa turns around and stops us in our tracks."
    enS "Okay lets make this crystal. We'll not be doing anything of the like."
    pS "Resa-"
    enS "Listen Jenn, I appreciate how ready you are to fight for MAC. But you don't understand the situation we're in." 
    pS "I ain't scared of the Hounds."
    enS "The reason Reynar is using the Hounds in the first place is because all of his actual security is here. Look around." 
    "I'm almost embarrassed by how long it took me to realize. I can feel dozens of eyes on us."
    "The androids here aren't just waiting, they're scanning, searching. A step too far out of line and that's it for us."
    pS "So now what?"
    enS "Schmooze, flirt, impress, find any way for someone to give you information but more importantly access."
    pS "I ain't much of a talker..."
    show rec stream happy
    recS "How about we do this together? I'd like to see the work maybe even chat up some of the researchers here."
    pS "I'd like that."
    enS "Perfect! Cap let's fan out and figure this out."
    mS "Got it, let's play up the part and be perfect guests for the Fair. More importantly stay in eyesight."
    enS "And Jenn..."
    pS "Hmm?"
    enS "Mind your manners please."
    pS "Course, milady."
    "Jenn tips an imaginary hat and walks away with Rec."
    hide jennica with dissolve
    hide rec with dissolve
    show teresa stream upset
    enS "We're doomed."
    mS "Yeah..."
    hide teresa with dissolve
    jump vig3_sc9

label vig3_sc9():
    show inventorfairgallery_stream at topleft onlayer background with dissolve
    hide exteriorvineyard_stream with dissolve
    invfairnpc1 "I told them raising Silver Badgers was a terrible idea! Now they have a torn up farm and no coats to show for it."
    "My eyes nearly roll out of my head at the forced laughter from the surrounding guests."
    "I hate schmoozing, the evening has droned on and absolutely no leads or sign of MAC anywhere."
    "I see Jenn taking an interested sip of her drink as Rec chats up some presenters near their inventions. One of the other guest follows my sight line." 
    "I think their name was Mills?"
    invfairnpc2 "I know it's such an eyesore, that arm should be scrapped honestly."
    mS "Don't you have modified teeth."
    invfairnpc2 "Of course but you could never tell!"
    invfairnpc2 "I swear they let anyone in the Fair nowadays."
    mS "Truly..."
    menu:
        "This guy's an snob"
        "Let it be.":
            "I can feel the anger boiling up to my throat."
            "It's so tempting just to trip these snobs into the drink table."
            invfairnpc2 "And that dress? What off the rack from Akar."
            invfairnpc1 "Not Akar! A half-way town for drunks and undesirables."
            invfairnpc2 "Sometimes makes you wish BigCorp took over."
            invfairnpc1 "All hail the Snakehawks."
            invfairnpc2 "And now the former leader is their personal dog."
            "I can't take this."
            mS "Excuse me for a moment."
        "Take him down a peg.":
            "Now I know I'm supposed to be on my best behavior, but I have limits. Just as Mills steps towards a drink tray I make sure to step ever so gentle on the fabric of their flared pants."
            "They tumble over knocking several drinks around and onto them."
            mS "Oh dear are you alright!"
            invfairnpc2 "MY SUIT! I knew I should've had these pants hemmed. Damn stylist!"
            "Mills walks away dripping on a few guests with them."
            mS "I guess some folks can't hold their drink."
            invfairnpc1 "There's one every year." #using invfairnpc1 because it's just labeled as "Inventor's fair guest." works for offscreen npc.
    "I move on, scanning the gallery, I see Teresa looking in her element gliding through various groups with a natural grace. Never lingering too long."
    showgirl "It's you!"
    show showgirl stream at stream_center with dissolve
    $ reactTarget = "vig3_sc9_daisyreturns"
    show screen streamerCommentary
    "A familiar batch of feathers block my view, Daisy stands in all her showgirl glory with a bit more refinement."
    mS "Oh, Daisy was it?"
    showgirl "You bet?"
    mS "50 Credits at Nova Casino."
    showgirl "What a terrible deal. That barely gets you a few good spins, not even a buy-in at a low ball table."
    mS "I guess the only big win anyone is getting is at the bar."
    "We both laugh, a genuine laugh."
    mS "I'm sorry for earlier, I've been on edge."
    showgirl "Don't sweat it, if you weren't going to shoot me I was. I hate that script."
    mS "Costume is great though."
    showgirl "Why you flatter me. It is one of my favorite parts."
    "Daisy sways in front of me to show me the movement of her feathers."
    mS "Fabulous. Truly."
    "She has such a sweet smile."
    showgirl "Well I should be off then."
    mS "Actually wait! Daisy. I have a question for you."
    showgirl "Oh?"
    mS "If someone would want to maybe go around and check out some of the off the floor pieces. Could she?"
    showgirl "Not without attracting some serious attention."
    showgirl "Unless they waited for a big presentation and had someone to help them through."
    mS "When's the next one scheduled?"
    showgirl "The Big Corp showcase should be happening in fifteen minutes, hear you'll get a killer view from the door near that vase over there."
    "She points to a large ornate vase at the side of the ballroom. There's an unmanned service door just behind it. I'm still trying to process what she just said."
    mS "Big Corp is here?"
    showgirl "Oh yeah, big reveal! Heard Reynar is hedging new investments and maybe some property in the Outposts, hard to expand without greasing some palms."
    mS "Noted. I'll make sure to check out that view."
    "Daisy nods and heads over to navigate the large crowd of guests. I rush to find the rest of my crew."
    hide showgirl with dissolve
    hide screen streamerCommentary
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    show rec stream neutral at stream_center with dissolve
    pS "Oh so we're really in it now."
    enS "Guess we didn't get much distance after all."
    recS "What happens if they catch you?"
    enS "Oh I assume chained to a factory for the rest of our natural lives."
    pS "I'd rather a bullet to the eyes."
    mS "We need to find MAC and get the hell out of here."
    show rec stream thinking
    recS "If we can trust your friend Daisy we might find whatever storeroom they put him in, hell maybe even your range extender on the way."
    mS "Makers willing. Okay, once the presentation starts then we'll head out."
    hide jennica with dissolve
    hide teresa with dissolve
    hide rec with dissolve
    "We go back to the floor. How many enforcers, are they all guests, maybe some waiting in the wings?"
    "Do they already have MAC and are just waiting for this presentation before heading off?"
    invfairannounce "And now a feature presentation from the Big Corp laboratories."
    "The music dies down an a platform rises from the center of the gallery. Spotlights alight on it and people halfheartedly turn to the center."
    "A finely dressed man walks up to the platform an attendant wheels in something covered by a blanket."
    bcrep "Ladies and Gentlemen, honorable guests of the Vineyard." 
    bcrep "We at BigCorp would like to thank Reynar for this opportunity to present a prototype for a new and exciting venture."
    "The crowd murmurs at the word prototype, I move closer to the corner of the room. Ready to make an escape."
    "Until the representative pulls off the sheet revealing their newest invention, a small purple robot with an unmistakable leaf over his head."
    show mac stream neutral at stream_center_mac with dissolve
    bcrep "Machine Automated Couriers or M.A.C is our revolutionary new bot that we are outfitting with fully adaptable AI technology."
    "His little eyes lock on mine."
    bcrep "As I said is just our prototype as we continue to look for new ways to truly develop our AI databases. But our scientists are hard at work to..."
    "This is a nightmare. A true honest to Maker nightmare."
    bcrep "Now a demonstration. Say hi M.A.C!"
    "There's a small pause."
    macS "Hi MAC..."
    "The room chuckles as the representative keeps talking. I look over at the crew who are frozen, unsure of how to proceed." 
    "Jennica begins to move up to me but stops and turns white as a ghost."
    amaS "Now ain't this a stroke of bad luck."
    hide mac with dissolve
    "I turn to the voice and am certain I've fully lost it." 
    "Because there she is, full ballgown staring at me with that same condescending look I've always known."
    show ama stream neutral at stream_center with Dissolve(2.0)
    $ reactTarget = "vig3_sc9_amasurprise"
    show screen streamerCommentary
    "But this time, it doesn't go away. Ama smiles."
    amaS "Hello Mozely."
    hide ama with dissolve
    jump vig3_sc10 

label vig3_sc10():
    show bg black at topleft onlayer background with dissolve
    hide inventorfairgallery_stream
    "I flinch as a shot rings outs, echoing in my ears."
    "My body is buzzing, heart pounding."
    "Ama takes the blaster away from me."
    # Ext. Akar - A Decade Ago 
    show ama stream neutral at stream_center with dissolve
    amaS "Kid, if you're gonna jump everytime someone shoots at you, they'll be playing target practice with your head."
    mS "I can't help it. I'm trying."
    amaS "You're scared."
    mS "I'm not scared. I'm a SnakeHawk!"
    amaS "Not after this you aren't."
    "What does she know? I am a SnakeHawk. A better one than that stupid Matticus at least."
    mS "Let me go again!"
    amaS "Please..."
    mS "Let me prove myself."
    amaS "All you've proven is that you're a liability."
    mS "Oh yeah like Jenn is any better."
    amaS "She can fire a blaster without flinching."
    "I feel tears swell up in my eyes."
    mS "Screw you! You don't know anything about me."
    amaS "We're done here."
    "Ama raises the blaster and points it at me. My body starts to freeze."
    "NO!"
    "I move out of the way just as the impact hits my shoulder, a hair's breadth away from my heart."
    "My arm is limp but there's no blood, she set it to stun."
    "Ama walks up to me, and turns the blaster, handle pointed at me."
    "The insignia of the Snakehawks branded on the handle."
    amaS "Again."
    "I get up and take the blaster. I grip the handle it like it's mine. Because it is." 
    "I point it at the target."
    "And fire."
    hide screen streamerCommentary
    hide ama with dissolve
    jump vig3_sc11

label vig3_sc11():
    show inventorfairgallery_stream at topleft onlayer background with dissolve
    hide bg black
    #Int. Inventor's Fair. 
    show ama stream neutral at stream_center with dissolve
    menu:
        "Ama stand in front of me steely gaze."
        "Of course you found us...": #Flirt
            mS "Of course you found us..."
            mS "I shouldn't have expected less from the great Deadeye."
            amaS "You flatter me."
            amaS "Gotta say getting into an event like this is impressive."
            amaS "You look...well."
        "Impossible":
            mS "Impossible."
            mS "How could you have possibly found us?"
            amaS "You think so little of me."
            amaS "Thought that stunt on Gibian V was going to keep me away?"
            amaS "How's Sallent doing?"
        "I see we're still playing the lapdog?":
            mS "Still playing the obedient lapdog I see?"
            mS "Money must be good."
            amaS "Even know you're still that arrogant little girl."
            amaS "How has playing the hero been? Finally found that purpose you've been missing?"
    "Her tone is playful but there's no mistaking that her rifle is folded behind her long jacket."
    "Big Corps presentation continues and I hope that the crew has taken this as a moment to leave."
    "It's up to Resa and Jenn, now."
    amaS "So tell me how is that little crew of yours, the Willow?"
    mS "The Oakley."
    amaS "Right, right, quaint."
    amaS "So let me cut to it, you give me what I want and I won't gut your crew and make you watch."
    "I look up at the platform."
    "I could laugh."
    "That smart little devil."
    mS "I don't know what you mean Ama, left something behind have you?"
    amaS "Oh we're playing dumb are we? The droid Mozely, give me the droid."
    menu: 
        "Ama doesn't have MAC, we can use this."
        "Why don't you just enjoy the party?": #Flirt
            mS "Ama please, it's a celebration, have a drink."
            mS "All this stress will give you wrinkles."
            "A smile forms on her face, anger mixed with something else."
            amaS "You little shit..."
            mS "Now, now, don't make a scene. You're better than that."
            $ reactTarget = "vig3_sc11_amabacksass"
        "I don't have the droid you're looking for.":
            mS "I don't have it."
            amaS "Are you playing dumb with me?"
            mS "I lost it, he's not with me."
            "Ama furrows her brow."
            amaS "This isn't the time to yank my chain."
            mS "Isn't that BigCorp's job?"
            $ reactTarget = "vig3_sc11_amabacksass"
        "But he's right there on the platform, no?":
            mS "Why are you asking me?"
            mS "It's right there isn't it?"
            "Ama turns to the platform then back at me, unimpressed."
            amaS "Don't quit your day job Moze."
            amaS "I want that droid and I want it now."
            $ reactTarget = "vig3_sc11_amabacksass"
    show screen streamerCommentary
    "Ama stalks towards me and I know what's coming."
    "I move to my blaster hidden in my clothes."#choice here?
    "I'm sorry Resa."
    show ama stream neutral at stream_right with move
    show reynar at stream_left with dissolve
    reynar "Ladies, I hope your evening is going well."
    amaS "Reynar."
    reynar "Hello Ama, a pleasure as always."
    reynar "And this must be young Moze. All grown up."
    "I relax my shoulders."
    mS "Reynar, thank you for having us this evening."
    reynar "If only you were invited..."
    hide screen streamerCommentary
    "A pause."
    "A waiter passes by with a full tray, Reynar grabs a bubbling drink without even looking."
    reynar "I sincerely hope, the two of your aren't about to do what I think you are."
    amaS "Respectfully this is Big Corp buisness."
    reynar "Is it now? Funny I didn't know that I ever gave them jurisdiction to conduct buisness in MY Vineyard."
    amaS "Consider it a favor, we're removing a known fugitive from the premises."
    reynar "Oh what a shame that you'll be leaving so soon."
    amaS "Such an incessant queen."
    menu: 
        "Get in the mix."
        "Bold coming from you.": 
            mS "Bold coming from you."
            amaS "Oh? You're speaking now?"
            mS "Hard to get a word in when you love hearing yourself talk."
            amaS "Haha little chick has grown up!"
            reynar "And with a considerable bite."
            mS "You don't know the half of it."
            "There is hunger in Ama's eyes."
        "Placeholder 2":
            "Placeholder text."
        "Placeholder 3":
            "Placeholder text."
    "I am thankful for Reynar's intervention but even he isn't known for hand outs."
    mS "Reynar, pardon my intrusion but I am here because your Hounds stole a piece of merchandise of mine."
    reynar "Did they now?"
    mS "A range extender, a small repair for my ship. I'd like it back."
    reynar "Well you can leave your information with Ryo and we'd be happy to oblige you after the festivities."
    "Ama chuckles under her breath."
    mS "I'd like to have this matter resolved as soon as possible."
    reynar "Of course! But first things first."
    "Which a snap of his fingers Ryo reemerges."
    reynar "Ryo please take our guests to the east balcony, they could use the privacy."
    "A nasty smile creeps on Ama's face."
    "I can feel the eyes around me."
    "The presentation is over and some attends are ushering the BigCrop rep away from the crowd."
    reynar "It was wonderful to see you both."
    "Reynar gives a forced hug and double cheek kiss to Ama. Then moves to me."
    "He offers the same gesture then whispers quietly."
    reynar "I do hope to see you later for the toast."
    "He slips something into my back pocket."
    "Ryo ushers us both in the direction of the east balcony."
    "Ama walks in front of me and I watch as her jacket hits something solid on her back."
    hide ama with dissolve
    hide reynar with dissolve
    jump vig3_sc12

label vig3_sc12():
    #Ext. Vineyard Balcony
    show exteriorvineyard_stream at topleft onlayer background with dissolve
    hide inventorfairgallery_stream
    "Overlooking the lush chimaeron trees, the east balcony was as ornate as it was private."
    "The noise of the Fair cuts as the large doors close on the balcony."
    "Clearly this space is meant for more quiet buisness."
    "In the distance I see Akar, lights gleaming like little stars."
    "It's so far away..."
    show ama stream neutral at stream_left with dissolve
    show bcrep stream neutral at stream_center with dissolve
    show mac stream neutral at stream_right_mac with dissolve
    bcrep "Absolute garbage!"
    "I hear the sound of metal on the ground, a small pained whine."
    "I press down my white hot anger."
    bcrep "What did you say to him? What did you do?"
    "He's talking to Ama, who arrogantly has he back to me."
    bcrep "I swear to the Makers if you screwed up again!"
    "The representative hasn't noticed me yet."
    "And soon had more pressing matters as he strained and struggled against Ama's grip on his throat."
    $ reactTarget = "vig3_sc12_amachoke"
    show screen streamerCommentary
    "I forgot how fast Ama was. How deadly."
    amaS "I suggest you watch that mouth of yours."
    bcrep "My...boss'...sign...your checks."
    amaS "Yes THEY do."
    "Her grip tightens."
    "I see MAC on the ground just passed them, still."
    "Then his eyes lock on mine, he perks up."
    "I put my finger to my lips."
    bcrep "P-l-ease..."
    "When Ama lets him go, he spills to the ground, tears in their eyes."
    hide screen streamerCommentary
    menu: 
        "Say something?"
        "Being a little rough are we?": #This is a choice. 
            mS "Being a bit too rough maybe?"
            amaS "Just handling business."
            mS "I can see that."
            amaS "Don't worry I'll get to you later..."
        "That was unnecessary":
            mS "A tad unnecessary."
            amaS "I'd suggest you let me handle business."
            amaS "But don't worry."
            amaS "I'll get to you soon."
        "Say nothing.":
            "I let the scene unfold."
            "The rep is desperately catching their breath."
            amaS "Enjoying the show?"
            "The words are trapped in my throat."
            amaS "Don't worry I haven't forgotten about you."
    bcrep "Who's this? One of Reynar's goons?"
    amaS "You academics are so up your own asses."
    "Their eyes widen as they stand to look at me."
    "They laugh in disbelief."
    bcrep "Incredible! Absolutely incredible!"
    bcrep "Do you have any idea how terrible this has been?"
    "He walks up to MAC."
    bcrep "But now that we have you, no more of this STUPID PIECE OF JUNK."
    "They're moving to kick MAC off the balcony."
    menu: 
        "How do you stop him?"
        "Fire your blaster.":
            "Absolutely not!"
            "I raise my blaster on instinct."
            mS "Hands off him!"
            "A shot rings out and my blaster flies out of my hand."
            amaS "Not likely Moze."
            "Ama stands with rifle in hand aimed at me."
            "The commotion is enough to stop the rep in his tracks."
        "Rush them down.":
            mS "No!"
            "I rush the rep ready to tackle him to the ground."
            "A shot rings out and the ground in front of kicks up with stone and dust."
            "I fall to the ground, my blaster flies out of my holster."
            amaS "Not likely Moze"
            "Ama stands with rifle in hand aimed at me."
            "The commotion is enough to stop the rep in his tracks."
        "You can't react fast enough.":
            "This is crazy."
            "All of this, we are so over our heads."
            "I can't will my body to move"
            bcrep "STUPID JUNK!"
            "Just as the rep attempts to land his kick, he's stopped by the sound of Ama's rifle."
            amaS "Hold it!"
            "The rep backs away."
            "The rifle turns to me."
            amaS "Blaster on the ground Mozely."
            "I wasn't even reaching for it. But I grab it from the holster in my suit jacket."
            "And toss it away from me."
    amaS "You always did play with your heart out Moze."
    "She looks to MAC."
    $ reactTarget = "vig3_sc12_amafindsout"
    show screen streamerCommentary
    amaS "That's it, isn't it."
    amaS "All that struggle. All that runnin'"
    amaS "Was it worth it?"
    "I looked at MAC and then Ama."
    "Before I even realize it, I start walking towards her."
    amaS "Woah now, stay right there."
    "I take another step."
    amaS "I'm warnin' ya Mozely."
    "She's hesitating."
    "Another step."
    hide screen streamerCommentary
    amaS "You're gonna make me shoot you?"
    "Until I'm close enough."
    "I pause."
    mS "Yeah."
    "I grab the gun as it fires inches from my face in the air."
    "I try to pry it from her hands but she's as strong as I remember."
    amaS "You little shit!"
    "I struggle against her strength as we pull the rifle back and forth."
    "BANG!"
    "Dust kicks up around us."
    "BANG!"
    "A chunk of the rail explodes out into the open air."
    macS "STOP IT!"
    "Ama and I hit a stalemate as we turn to MAC."
    "The rep is white as a ghost, back to the rails as if he'll throw himself off."
    "And there's MAC with my blaster in his hand."
    "Gripping the handle like it's his own."
    #Choices happen based on MAC's alignment.
    if macViolence >= macPeace and macPessimism >= macHope:
        "He fires the blaster in-between us, it hits the wall with a definitive smack."
        bcrep "Makers!" 
        "Ama just stares at MAC who is resolute in his stance."
        amaS "You gonna do something with that baby blaster?"
        amaS "If you're gonna shoot, you better shoot straight."
        macS "My programming ensures perfect accuracy. Shall I demonstrate?" 
        bcrep "Programming..."
        amaS "Well then, let's-"
        "The blaster rings out and before I can react Ama is on the ground clutching her side."
        amaS "Bastard!" 
        macS "I have been provoked and damaged, I will defend myself."
        macS "I will defend my Captain."
        "The rep is shaking and I almost forget the rifle in my hand."
        "MAC slowly rolls towards me passing Ama without even looking at her."
        amaS "You won't get out here you know."
        macS "Will you stop us. I can remove you if necessary."
        amaS "I-"
        macS "We should leave, yes?"
        $ reactTarget = "vig3_sc12_macalignment_violencepessimism"
        show screen streamerCommentary
        mS "You got it."
        "Without losing my sights on her we head inside."
    elif macViolence >= macPeace and macPessimism < macHope:
        "He fires the blaster in between us, it hits the wall with a definitive smack."
        bcrep "Makers!" 
        "Ama just stares at MAC who holds the gun steady but with noticeable apprehension."
        amaS "You gonna do something with that baby blaster?"
        amaS "If you're gonna shoot, you better shoot straight."
        macS "My programming ensures perfect accuracy when required." 
        bcrep "Programming..." 
        amaS "Well then, let's see it."
        macS "I know you don't want BigCorp to succeed anymore than we do."
        amaS "I don't know I'm being paid quite well."
        "Another fire from the blaster, right in front of Ama's face."
        macS "Then I'll shoot you if I must."
        amaS "You little bastard."
        "This is my chance."
        "With a proper shove I get Ama off balance and aim her rifle at her."
        mS "MAC let's go!" 
        macS "Yes Captain!"
        "MAC wheels towards me and stops at Ama."
        macS "Captain says you're one of the best."
        macS "My records show a long list of... accomplishments perpetrated by you."
        amaS "And what about it?"
        macS "... You're better than this."
        $ reactTarget = "vig3_sc12_macalignment_violenceoptimism"
        show screen streamerCommentary
        "Ama is speechless"
        "Without losing my sights on her we head inside."
    elif macViolence < macPeace and macPessimism >= macHope:
        "He fires the blaster in-between us, it hits the wall with a definitive smack."
        bcrep "Makers!" 
        "Ama just stares at MAC who is resolute in his stance."
        amaS "You gonna do something with that baby blaster?"
        amaS "If you're gonna shoot, you better shoot straight."
        macS "My programming... ensures perfect accuracy."
        bcrep "Programming..."
        "Ama flashes him her famous condescending smile."
        amaS "But did they program any nerve in you?"
        "MAC is struggling to keep the blaster straight" 
        "He's trying to do what he thinks is best..."
        macS "I can't..."
        "He begins to lower the gun."
        "I didn't think droids could feel defeat."
        amaS "Takes alot more than a good shot to be an outlaw." 
        "I can feel Ama loosen her grip."
        "This is my chance."
        "With a proper shove I get Ama off balance and aim her rifle at her."
        mS "Enough nerve for ya?"
        "MAC quickly rolls to me."
        mS "We're walking out of her."
        $ reactTarget = "vig3_sc12_macalignment_peacepessimism"
        show screen streamerCommentary
        "Without losing my sights on her we head inside."
    else:
        "He fires the blaster in-between us, it hits the wall with a definitive smack."
        bcrep "Makers!" 
        "Ama just stares at MAC who is resolute in his stance."
        amaS "You gonna do something with that baby blaster?"
        amaS "If you're gonna shoot, you better shoot straight."
        macS "My programming ensures perfect accuracy. But I won't need this."
        bcrep "Programming..."
        amaS "Mighty confident are we? Gonna take me on with hands?"
        macS "I will not do that."
        macS "You're going to let us go."
        amaS "Sorry but I'm not feeling very charitable at the moment."
        "There's a moment as the two stare at each other."
        macS "I know you still have love for Moze." 
        amaS "..."
        amaS "What did you say?"
        "MAC also takes me aback but I regain composure first."
        "With a proper shove I get Ama off balance and aim her rifle at her."
        macS "Moze, don't hurt her."
        macS "Let's just go."
        "MAC slowly rolls towards me."
        "As he passes Ama he looks at her and smiles."
        macS "Take care Ama."
        $ reactTarget = "vig3_sc12_macalignment_peaceoptimism"
        show screen streamerCommentary
        "Without losing my sights on her we head inside." 
    #elif macViolence < macPeace and macPessimism < macHope:
    # "MAC is a peaceful optimist."            
    "I remove the core from the rifle, put it in my pocket and toss the shell on the ground."
    "We break into a sprint down the hall."
    hide ama with dissolve
    hide bcrep with dissolve
    show mac stream neutral at stream_center_mac with move
    jump vig3_sc13

label vig3_sc13():
    "My blaster feels heavier as we run down the winding paths of the Vineyard." 
    "Tucked away tight to my side I'm resolute in making sure MAC doesn't touch it."
    "There's no time to talk about what happened."
    "Not that MAC looks too inclined to talk about it anyways." 
    macS "They should be right down here."
    "This whole area has been cleared. Why is there no one here?"
    "Loud bangs ring out in the distance. Fireworks? Maybe?"
    "Maybe mine wasn't the only secret meeting tonight."
    hide screen streamerCommentary
    macS "In here!"
    "MAC stops us at a door, I can hear muffled arguing beyond it."
    "It's locked and needs a card to open."
    macS "Let me!"
    "With an efficiency that I've only ever seen from Teresa. MAC undoes the scanner and brings his hand to it as the door swings open."
    "Two blasters meet me as the door swings open."
    show mac stream neutral at stream_right5mac with move
    show rec stream surprised at stream_left5 with dissolve
    show teresa stream fight at stream_right with dissolve
    show jennica stream fight at stream_left with dissolve
    mS "Well don't be too happy to see me!"
    enS "Captain!"
    pS "Thought ya dead, I won't lie."
    "MAC rushed past me to grab Teresa's legs. The door closes behind me as I walk in."
    show teresa stream happy
    show jennica stream neutral
    show rec stream happy
    enS "Good to see you buddy."
    pS "Where's Deadeye?"
    mS "Left her on the east balcony might be on our tail but didn't see where we went."
    pS "That gives us some time."
    enS "But we have MAC and that's important."
    recS "Not just MAC."
    "They hold up the range extender laying on the counter near them."
    mS "How?"
    pS "Long story truly, did you know Zan is here?"
    mS "At the Fair? For what?"
    recS "He's one of the featured designers! A big name is biomechanical engineering."
    pS "He's some good-lookin' work."
    show rec stream drunk
    recS "And some good-lookin' muscles."
    mS "..."
    recS "Forget I said that."
    show rec stream happy
    mS "Okay let's focus up. What's going on here."
    show teresa stream neutral
    show jennica stream neutral
    enS "Rec found a private comms room. We were hoping to at least catch our breath before we head out."
    pS "Can't go back through the party."
    recS "But there's still a shuttle system that can get us to Akar. Usually used by the workers and it should be a quick run here."
    enS "Ama will probably head there too."
    mS "If she's not already getting her ship off the ground to scan for us."
    "We need to act now."
    menu: 
        "Call in a favour to deal with Ama?":
            "Let's just hope he picks up."
            if vig2_outlawEpilogue == True:
                jump vig3outlawcomms
            else:
                jump vig3marshalcomms 
        "Mad dash to the shuttles.":
            "No time to lose lets make a break for it!"
            "..."
            show mac stream shock
            macS "APOLOGIES!"
            "This was the third security guard MAC had run over with reckless abandon."
            "Like a little purple battering ram MAC was clearing a path through just as Reynar's security came to intercept us."
            "When we set off we didn't imagine it would be this close to the fair."
            "Dodging through the side garden to the entrance shuttles I pray that Reynar isn't too upset with our escape plan."
            show jennica stream shock
            pS "Jeez this kid's goin' fast and furious."
            show teresa stream happy
            enS "He gets it from you!"
            show rec stream thinking
            recS "This architecture is incredible, the bio-tech is so seemlessly integrated into the material of the wall."
            mS "REC LOOK FORWARD!"
            show rec stream surprised
            "In their distracted state they mindless slam into a couple going hot and heavy."
            "No doubt using the garden to avoid any possible scandal..."
            show jennica stream neutral
            pS "Keep up y'all I'm the only one in heels and I'm leagues ahead!"
            enS "Stop showing off!"
            pS "How 'bout ya start showing up!"
            show rec stream happy
            recS "How about that terrarium!"
            mS "REC!"
            "With only minor casualties, we make it to the shuttles."
            jump vig3_sc14

label vig3outlawcomms():
    show matticus phone neutral at stream_center_mac with dissolve
    show jennica stream angry
    smatt "Well hello ladies! Need a hand from little ole me?"
    "Matticus smiles in that shit-eating grin that he loves."
    pS "This is a terrible idea"
    "I'm starting to agree."
    mS "We're not here for pleasantries"
    recS "I almost forgot what he was like."
    show rec stream neutral
    smatt "Is that little Reccrin?"
    smatt "Been a while kid."
    recS "You know I'm the older one right?"
    smatt "Hard to tell when Allistar was the one with the nerve."
    mS "Matticus!"
    smatt "What is it sweetheart?"
    mS "Ama found us in the Vineyard. We need to give her a hard time following us out of here."
    smatt "The Vineyard? It sounds like you did this to yourself lovey!"
    mS "I don't have to explain my reasons to you. Can you do it or not?"
    enS "This is a waste of time, Matt can't take on Reynar."
    smatt "Excuse you, must you think so little of me?"
    pS "Couldn't even hide us well 'nough. I say lets go Cap."
    recS "Reynar's system is too impressive anyways you wouldn't be much of a challenge."
    smatt "Okay okay since you did such a good job."
    smatt "I'll make sure Reynar's airspace will be especially hostile."
    mS "Fabulous."
    smatt "Aren't I?"
    smatt "Bye bye and try not to die. I'll be looking for you to repay the favour."
    hide matticus with dissolve
    "The comms go dead."
    macS "Skeeve."
    recS "The biggest."
    mS "Let's get out of here."
    "With relative ease we make it to the shuttles."
    show jennica stream neutral
    jump vig3_sc14

label vig3marshalcomms():
    show matticus phone neutral at stream_center_mac with dissolve
    show jennica stream angry
    smatt "Well hello ladies! To what do I owe the pleasure?"
    "Matticus smiles in that shit-eating grin that he loves."
    pS "Disrespectfully, we didn't call you."
    "This is bad."
    smatt "Oh no? Were you perchance hoping I was some young redheaded datacenter intern?"
    show rec stream neutral
    recS "Sounds like a nicer face to look at."
    smatt "Oh is that little Reccrin? The SnakeHawk dropout?"
    smatt "Still hiding in that little hovel in Akar?"
    smatt "Oh... Oh Moze you do love to live dangerously do you."
    mS "What kind of bullshit is this?"
    enS "Where's the kid?"
    smatt "Ever since your hack job with Sallent ship. I had to restablish the pecking order around here."
    smatt "So I had to make an example."
    "This rat bastard."
    mS "That's low even for you."
    enS "How do you sleep at night?"
    smatt "On a king bed after a nice big meal."
    "Jenn spits on the ground."
    smatt "I think we're done here. And Mozely."
    smatt "From the bottom of my heart."
    smatt "I hope Deadeye skins your crew alive while you watch."
    smatt "Bye bye now!"
    hide matticus with dissolve
    "The comms go dead."
    macS "Skeeve."
    recS "The biggest."
    mS "Let's get out of here."
    "Carefully we make it to the shuttles. Not sure what awaits us on the other side."
    show jennica stream neutral
    jump vig3_sc14

label vig3_sc14():
    "Just beyond the entrance the shuttles are empty."
    "Reynar hasn't toasted to the crowd and people wouldn't dare to leave before his address."
    show rec stream thinking
    recS "This one, it'll take us right to the plaza!"
    "With quick work MAC undoes the security protocol and gets us loaded in."
    hide mac with dissolve
    show ama stream neutral at stream_right5 with vpunch
    "Then I'm thrown against the wall and there's Ama, knife in hand at my throat."
    show rec stream surprised
    show teresa stream fight
    show jennica stream fight
    "Teresa and Jen are quick to act."
    enS "Let her go Ama!"
    pS "We'll drag your body out of here if necessary."
    amaS "Then you'll need to make room for two."
    "She presses harder against my throat."
    hide jennica with dissolve
    hide teresa with dissolve
    show ama stream neutral at stream_right with move
    show rec stream surprised at stream_left with move
    recS "Deadeye..."
    "Ama's eye move to Rec."
    amaS "Well well, if it isn't Reccrin."
    amaS "Right where we left him."
    show rec stream angry
    recS "Screw you, you took Allistar away to go galavanting in the Outposts."
    recS "I have nothing to say to you."
    "Ama looks around expectantly."
    "A realization creeps on her face."
    amaS "Mozely, where is Allistar? Last I checked I left him with you."
    show rec stream surprised
    "Rec's eyes fix to me, finally catching me in my lie."
    recS "What?"
    amaS "Oh you didn't know?"
    "Guilt stains all of our faces."
    recS "Is this true?"
    mS "It is..."
    show rec stream angry
    recS "Well!? Where is he!?"
    "I can't lie anymore."
    mS "He's dead Rec, I shot him."
    "Rec's eys widen, as they step back, horrified."
    recS "Why?"
    menu: 
        "Why did you shoot Allistar?"
        "I didn't want to it just happened.":
            $ reactTarget = "vig3_sc14_recfindsout_regret"
            mS "After he fixed MAC, we brought him to the ship."
            mS "He was trying to take MAC."
            mS "I was scared. Scared of this."
            mS "And I think he was too."
            "Tears are forming in Rec's eyes." 
            recS "So why?"
            mS "I just happened. Before I realized what I've done he was on the ground."
            mS "I'm so sorry Rec, it's my greatest failure."
            "There's a long moment where Rec just looks at us."
            "But they say nothing and turn to walk away."
            show screen streamerCommentary
            hide rec with dissolve
            "Teresa and Jennica don't turn to them, still fixed on Ama."
            "MAC clings to Teresa."
            amaS "How disappointing, he was a talented kid."
            "Ama looks to Teresa and Jennica."
            "I see Reynar's security detail bounding for us in the distance."
            "Ama takes the knife off my neck. And puts her hands in the air."
            amaS "Let's finish this later, shall we?"
            "We don't move as she backs away from us."
            "Then out of sight."
            hide ama with dissolve
            "We don't have time to process before we head for the shuttle."
            show mac stream neutral at stream_center_mac with dissolve
            macS "Moze?"
            mS "Yes MAC."
            macS "Will Rec be okay?"
            mS "I don't know."
            macS "Are you okay?"
            mS "I don't know."
            hide mac with dissolve
            hide jennica with dissolve
            hide teresa with dissolve
            jump vig3_epilogue

        "I did what I had to do.":
            $ reactTarget = "vig3_sc14_recfindsout_ihadto"
            mS "After he fixed MAC, we brought him to the ship."
            mS "He was trying to take MAC."
            mS "I found him trying to take an escape pod."
            mS "MAC is so important, too important."
            mS "I couldn't let him leave, I did what-"
            recS "Bullshit!"
            "Tears are pouring from Rec's eyes."
            recS "Know who else is important? MY LITTLE BROTHER!"
            "I see MAC clutch Jennica's leg"
            recS "You didn't have to do anything."
            recS "You screwed up and needed an easy way to be bailed out."
            "I see Reynar's security detail bounding for us in the distance."
            recS "Well I'm not going to stick around to bail you out of this."
            "They turn to walk away."
            show screen streamerCommentary
            hide rec with dissolve
            amaS "How disappointing, Allistar was a talented kid."
            "Ama looks to Teresa and Jennica."
            amaS "Let's finish this later, shall we?"
            "We don't move as she backs away from us."
            "Then out of sight."
            hide ama with dissolve
            "We don't have time to process before we head for the shuttle."
            hide mac with dissolve
            hide jennica with dissolve
            hide teresa with dissolve
            jump vig3_epilogue

        "I did it because he deserved it.":
            $ reactTarget = "vig3_sc14_recfindsout_noremorse"
            mS "After he fixed MAC, we brought him to the ship."
            mS "He was trying to take MAC."
            mS "We trusted him."
            mS "I saw him with MAC at the escape pods and I realized what he was trying to do."
            "The blade cuts into my neck as I turn to look Rec in the eyes."
            "I can hear Ama chuckle under her breath."
            mS "I killed Allistar, and that spineless traitor got exactly what he deserved!"
            "Teresa and Jennica almost lose their sights on Ama."
            "MAC stays there motionless."
            "Behind him is Rec. Face like they took a bullet to the gut."
            recS "You..."
            "Tears pouring down his face."
            "They look at me and Ama."
            recS "You two deserve each other."
            "Rec turns around and walks away from us."
            show screen streamerCommentary
            hide rec with dissolve
            "Ama leans in close."
            amaS "That was cold Mozely, even for me."
            "Ama takes the knife off my neck. And puts her hands in the air."
            amaS "Let's finish this later, shall we?"
            "We don't move as she backs away from us."
            "Then out of sight."
            hide ama with dissolve
            "We don't have time to process before we head for the shuttle."
            hide mac with dissolve
            hide jennica with dissolve
            hide teresa with dissolve
            jump vig3_epilogue

label vig3_epilogue():
    "As the shuttle zooms to Akar, the Vineyard is alight with fireworks."
    "The screens in the shuttle spring to life."
    "Reynar is there, glass in hand toasting it to the camera."
    "And I remember what he left in my pocket."
    hide screen streamerCommentary
    show shiphub_stream at topleft onlayer background with dissolve
    "Teresa outfits the Oakley best she can."
    "And with Reynar's gift we got access to fly the Oakley out through restricted sky."
    "Which gives us time."
    "At least..."
    "But the Oakley is silent."
    "For days it is buisness as usual, no one knowing how to tallk about the dark cloud over us."
    "Rec refuses to answer Jenn or Teresa's transmissions."
    "MAC has be silent, spending time alone."
    "Then the transmission comes through."
    show teresa stream neutral at stream_right with dissolve
    show jennica stream neutral at stream_left with dissolve
    show mac stream neutral at stream_center_mac with dissolve
    dflycontact "Captain Moze of the Oakley this is Dr. Coil of the Dragonflies."
    dflycontact "I hear you are in possession of Dr. Vanas' work."
    dflycontact "We are contacting you regarding the drop off point."
    dflycontact "We are stationed at a plant known as Polaris."
    dflycontact "Brevifolia sector coordinates 11 03 7"
    dflycontact "This is the last attempt, should this message be lost, then so is our hope."
    "The transmission ends."
    mS "Jenn?"
    pS "On it Cap."
    mS "Thank you, I'll be in my quarters."
    hide jennica with dissolve
    hide teresa with dissolve
    hide mac with dissolve
    show ship_hallway_stream at topleft onlayer background with dissolve
    "As I walk down the hall, I'm once again intercepted."
    show mac stream neutral at stream_center_mac with dissolve
    "It's MAC."
    "We stare at each other in silence."
    "I lower myself to his eye level."
    "He rolls towards me."
    "And hugs me."
    "The Oakley presses forward, and away from Akar."
    hide mac stream neutral with dissolve
    hide screen streamChat
    hide screen streamDetails
    scene bg black with dissolve
    jump vig3_macro_start

label vig3_macro_start():
    $ vignette3 = True
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
    $ menu = nvl_menu
    mod_nvl "Yoyoyo!"
    mod_nvl "Another great stream!"
    if viewershipHigh == True:
        mod_nvl "The viewership numbers were crazy."
        mod_nvl "I wouldn't be surprised if we already hit all the marks to make Affiliate!"
        menu:
            "•You think so??":
                player_nvl "You think I made it already?"
                mod_nvl "Maybe! It was a lot of people."
                mod_nvl "Check your analytics on Flinch and let me know."
                mod_nvl "I guess you still have to do one more stream technically, but that might be a formality at this point."
            "•I still have to do one more stream.":
                player_nvl "Maybe in terms of analytics, but I have to stream at least one more time next week to officially make it."
                mod_nvl "True. But even then, at least you know it's pretty much a formality."
    else:
        mod_nvl "Viewership wasn't the same as the previous stream. Maybe cause you went a little too Marshal in Episode 2."
        mod_nvl "But it was still good numbers. With a solid final stream, you should be all set for Affiliate!"
        menu:
            "•You think we'll make it?":
                player_nvl "Do you really think we'll make it to where we need to go?"
                mod_nvl "Oh yeah."
                mod_nvl "I mean, I've believed in you since I start modding for your stream."
                mod_nvl "Why stop now?"
                player_nvl "Thanks, Jessie."
                mod_nvl "Of course."
            "•I'm feeling confident.":
                player_nvl "I feel good about our chances too."
                player_nvl "I know the numbers dipped from when I streamed Episode 2, but I think the crew that's there is in it for the long haul."
                mod_nvl "You got a lot of friendly voices in the chat."
                mod_nvl "Not every streamer can say that."
    mod_nvl "Alright, I don't have a ton of time, but I wanted to say you did a great job dealing with the crash!"
    menu:
        "•I was so stressed out!":
            player_nvl "Oh my god that stressed me out so much!"
            player_nvl "I'm like shocked the chat didn't abandon me."
            mod_nvl "Just goes to show the kind of vibe you cultivated!"
        "•I felt weirdly calm.":
            player_nvl "It's weird, in the past that kind of stuff really rattled me."
            player_nvl "But this time I just felt really calm."
            mod_nvl "Interesting. Guess you're still getting better at this stuff!"
        "•It happens.":
            player_nvl "You stream enough times, you get used to technical difficulties. It happens."
            mod_nvl "I mean, still, you handled it like a pro!"
    mod_nvl "Ok, gotta run and grab some udon."
    mod_nvl "Have a good night! So excited for the last episode!"
    menu:
        "•Take care!":
            player_nvl "Thanks, Jessie! You take care!"
    jump vig3_macro_webNav

label vig3_macro_webNav():
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
    call screen webNavigation_vig3

label vig3_macro_viewerChat_1():
    $ menu = nvl_menu
    scene discordview with dissolve
    $ screenComplete = False
    $ loopdView = True
    $ menu = nvl_menu
    "This is a test for the viewerchat section."
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
    show screen viewershipButton_vig3
    call screen streamAnalytics_vig3
    hide screen streamAnalytics_vig3 with dissolve

label blueitVignette3_1():
    $ menu = adv_menu
    scene blueit_v2screen at truecenter with dissolve
    $ screenComplete = False
    $ blueitView = True
    $ blueitPages = [] #this line can be deleted eventually. It's here temporarily to make testing a bit easier.
    $ blueitPages.append(vig3_bThread1)
    #$ blueitPages.append(vig3_bThread2)
    #$ blueitPages.append(vig3_bThread3)
    #$ blueitPages.append(vig3_bThread4)
    "You go to check out the subblueit to see how people are reacting to Episode 3."
    jump blueitVignette3_2

label blueitVignette3_2():
    scene blueit_v2screen at truecenter
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
    "It's reassuring that Jessie feels good about the stream."
    "And he's right, there's just one more episode to go."
    "One way or another, this thing will come to an end."
    "You start absentmindedly scrolling through Loop'D and you see that Elliot is online."
    "It's been a while since you had a proper chat."
    scene discordview with dissolve
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
    bro_nvl "Of course [player]! Any time?"
    bro_nvl "I was actually just gonna shoot you a message asking the same thing lol"
    menu:
        "•What did Elliot want to check-in about?":
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
            player_nvl "That's great, El! Should take some of the pressure off the final."
            bro_nvl "Yeah, it's a relief for sure :)"
            player_nvl "...anything else to report on?"
            bro_nvl "Nothing too important really."
            player_nvl "suuuuure"
            bro_nvl ">:)"
        "•Who cares, I want boy news!":
            player_nvl "Grades shmades! What about the Brit Boy!"
            bro_nvl "Who?"
            player_nvl "YOU KNOW WHO, EL!"
            bro_nvl "lmao >:)"
    player_nvl "Spill it."
    bro_nvl "I asked Cedric out on a date."
    menu:
        "•What did he say?":
            player_nvl "El! That's amazing!"
            player_nvl "I'm so proud of you!"
            player_nvl "What did he say?"
        "•YESSSS!":
            player_nvl "YESSS!"
            player_nvl "WHOOOO!"
            player_nvl "So proud of you, El!"
            player_nvl "How did you do it? Was it like a big production like a prom thing? Were you like wearing a suit or something?"
            player_nvl "Wait, what did he say?"
    bro_nvl "lmao"
    bro_nvl "He said yes!"
    player_nvl "WHOOOOO!"
    menu:
        "•Best. Day. Ever.":
            player_nvl "Best. Day. Ever."
        "•I'm gonna cry.":
            player_nvl "Omg, I'm legit gonna cry."
    bro_nvl "It's not your crush haha"
    player_nvl "No, but like."
    bro_nvl "But thank you."
    player_nvl "You made the move"
    bro_nvl "I know."
    player_nvl "You put yourself out there"
    bro_nvl "Yeah."
    player_nvl "That's huge."
    bro_nvl "I know! I'm like giddy all over!"
    player_nvl "So how did it happen?"
    bro_nvl "Well, it wasn't a big production."
    bro_nvl "I took your advice from a couple weeks back and just kept making the effort to chat with him these past couple weeks."
    player_nvl "Uh huh."
    bro_nvl "It was tough, but I kept thinking about what you said."
    if vig1_overthink == True:
        bro_nvl "\"Don't overthink it.\""
    else:
        bro_nvl "Talking to someone you like is \"never not weird.\""
    bro_nvl "So I just tried to be myself and we started walking home from school together like almost every day."
    player_nvl "Cuuuuute"
    bro_nvl "And when we got to my block today...I don't know."
    bro_nvl "I just asked if he'd like to go on a date with me."
    bro_nvl "I didn't even realize I was doing it until I heard myself say the word \"date.\""
    player_nvl "And then?"
    bro_nvl "He said yes and kissed me on the cheek :)"
    player_nvl "I'm dying"
    bro_nvl "lol"
    player_nvl "No, legit, I couldn't write a better story for you two."
    player_nvl "You got plans for the date??"
    bro_nvl "Yeah, he's gonna take me to see a movie next Friday!"
    $ playerNVLNarration = "That's the same day as the release of the Oakley's final episode."
    show screen NVLnarration with dissolve
    pause
    menu:
        "•That's the same day as the last Oakley stream.":
            hide screen NVLnarration
            player_nvl "Funny, that's the same day as my last Oakley stream."
            bro_nvl "I know, I'm sorry I won't be able to make it!"
            bro_nvl "It's the only night Cedric's free!"
            player_nvl "nononono your date is way more important."
            player_nvl "We'll catch up on Oakley 2 when I get back for Thanksgiving!"
            bro_nvl "Yes!"
            player_nvl "And I'll be sending you the best vibes for a good date from a distant galaxy!"
            bro_nvl "I promise they will be received haha"
        "•You? In a movie theater?":
            hide screen NVLnarration
            player_nvl "Since when do you go see movies in theathers Mr. \"Classical Music is the Only Real Theatre.\""
            bro_nvl "Since my crush started giving me shit about my lack of pop culture knowledge."
            player_nvl "You know what, fair."
            player_nvl "I did try to get into MOBAs just to impress my crush a couple years back so I guess I can't talk."
            bro_nvl "Yeah, I remember that. Fun streams!"
            player_nvl "My kda was like 0.3."
            bro_nvl "I didn't say they were fun for you."
            player_nvl "Shut up."
            bro_nvl "Love you too <3"
    if vig3_brotherChat == 1:
        bro_nvl "Soooo yeah, that's my big news."
        bro_nvl "What's up with you? How's the stream going'?"
        jump vig3_macro_brother_stream
    else:
        jump vig3_macro_brother_end

label vig3_macro_brother_stream():
    $ vig3_brotherChat += 1
    menu:
        "•Stream is great!":
            player_nvl "The stream is great!"
            bro_nvl "Love hearing that!"
            if energy >= 5:
                bro_nvl "Just based on the VODs it looks like you're having a good time."
            else:
                bro_nvl "Glad you're not like beaten down by the push for Affiliate."
            if viewershipLow == True:
                bro_nvl "Though it seems like not too many people stuck around after that raid."
                player_nvl "Yeah, the chat isn't too crazy, but it's still bigger than I'm used to."
                menu:
                    "•It can get a little overwhelming.":
                        $ energy -= 1
                        player_nvl "Tbh it can feel a little overwhelming."
                    "•It's super fun!":
                        $ energy += 1
                        player_nvl "It's super fun! But I'm also still learning how to manage that chaos."
            else:
                bro_nvl "Plus it looks like people have stuck around after that raid a while back."
                player_nvl "Yeah the chat is popping off on a regular basis these days."
                menu:
                    "•It can get a little overwhelming.":
                        $ energy -= 1
                        player_nvl "Tbh it can feel a little overwhelming, but still fun."
                    "•It's super fun!":
                        $ energy += 1
                        player_nvl "It's super fun! But also like really chaotic."
            bro_nvl "For sure, so what are you enjoying the most?"
            menu:
                "•The game.":
                    player_nvl "The game, for sure!"
                    bro_nvl "Yeaaah, Oakley 2 does look sick."
                    bro_nvl "Bummed I'll have to wait till the holidays to get it for myself."
                    player_nvl "It's cool. I mean the art is so good."
                    bro_nvl "The soundtrack too. Heard that little futuristic baroque piece in Episode 3. Very nice."
                    if vibes == True:
                        player_nvl "Yeah and game has a great vibe in general. Very easy to stream, but still really engaging."
                    elif humour == True:
                        player_nvl "Plus it's just a funny game. Script has a lot of good one-liners."
                    elif story == True:
                        player_nvl "And the story builds on the themes from the first game so well."
                        player_nvl "The characters especially are really well done."
                    else:
                        player_nvl "And the story builds on the themes from the first game so well."
                        player_nvl "The characters especially are really well done."
                    bro_nvl "Yep, I was already bummed I couldn't play it at launch and keeping up with your playthrough is just increasing the fomo"
                    player_nvl "Lol, sorry"
                    bro_nvl "Ahh it's fine. This way I get to see you make all the mistakes and then do the better choices for me!"
                    player_nvl "Always so selfless"
                    bro_nvl "You know me :)"
                "•The chat.":
                    player_nvl "I'm having a lot of fun interacting with the chat."
                    if viewershipHigh == True:
                        player_nvl "Like I said, there are way more people around there now and it's really cool to be hanging out with everyone."
                        player_nvl "I get to hear more perpsectives on the game's moral choices. Wacky stories. Crazy jokes."
                    else:
                        player_nvl "It's not that many more people than I'm used to, but even so, there's a lot more going on there now."
                        player_nvl "I like hearing people's different perspectives on the game's moral choices and seeing their wacky jokes."
                    player_nvl "Plus it feels like the people in chat are really starting to vibe and be like friends."
                    player_nvl "It's cute!"
                    bro_nvl "Yeah, honestly half the fun of watching the VODs is seeing what goes on in your chat."
                    bro_nvl "And I'm really glad it's been a positive experience for you!"
                "•Being on camera.":
                    player_nvl "I think it's just being on camera."
                    player_nvl "When I'm not trying to get Affiliate, I stream a bit less regularly."
                    player_nvl "It's nice to just be in the habit of performing for people."
                    player_nvl "It can get tiring, don't get me wrong. But I have so much fun that it doesn't matter."
                    bro_nvl "I'm glad! I know you always feel a bit \"off\" if you go without streaming for a while."
                    bro_nvl "Definitely good to keep up the habit!"
        "•It's going well.":
            player_nvl "Yeah, it's going well."
            bro_nvl "Ooh, not the period."
            bro_nvl "What's up?"
            menu:
                "•Nothing.":
                    player_nvl "Nothing's up."
                    bro_nvl "You sure?"
                    menu:
                        "•Yes.":
                            player_nvl "Yeah, things are good."
                            player_nvl "They're just not great."
                            player_nvl "They're not shit. But they're not great."
                            if enthusiasm >= reluctance:
                                player_nvl "Trying to get Affiliate is a bit of a slog, but playing the game and hanging with chat has been really fulfilling."
                            if energy < 5:
                                player_nvl "I feel pretty tired, but not like exhausted."
                            if outlaw > marshal and enthusiasm >= reluctance:
                                player_nvl "And I'm having fun experimenting with the game's Outlaw choices."
                                player_nvl "But the episodies can get long too."
                            bro_nvl "Sounds like the life of someone who turned their passion into work."
                            player_nvl "Yeah, but that work isn't even paying me anything."
                            bro_nvl "But it's still rewarding to you. That's why you even bother to do it."
                            bro_nvl "I know you love games, and I know that all the streaming stuff makes playing them more complicated." 
                            bro_nvl "But you still love them and the community that comes from the stream."
                            bro_nvl "I just hope the good of that stuff always outweighs the bad. And if it starts to flip, then you can stop. No one is making you do this, y'know."
                            player_nvl "You're right. Thanks, El."
                            bro_nvl "Anytime."
                        "•Actually...":
                            player_nvl "Actually, yeah some things are bugging me."
                            bro_nvl "I knew it. Like what?"
                            menu:
                                "•The grind for Affiliate sucks.":
                                    player_nvl "The grind for Affiliate just sucks."
                                    player_nvl "Like I'm playing this game and it's bringing in more viewers on the regular."
                                    player_nvl "But jamming out smaller streams is just exhausting."
                                    if energy < 5:
                                        bro_nvl "Yeah, ngl, you look a bit tired in the streams sometimes."
                                        player_nvl "Well that's kinda embarrassing lol"
                                        bro_nvl "I mean, I don't think anyone else would notice."
                                        bro_nvl "But like, I can tell when you're running on low energy."
                                        bro_nvl "Sibling shit, y'know."                            
                                    else:
                                        bro_nvl "Really? On the VODs you look energized."
                                        player_nvl "That's good to hear."
                                        player_nvl "Sometimes I stream and I feel really good. Other times, it's rough."
                                    bro_nvl "Mom always says life has its ups and downs."
                                    bro_nvl "But I know you. And I know that you stream because it has way more highs than lows."
                                    bro_nvl "Otherwise you wouldn't bother."
                                    bro_nvl "Like just think about the people you've met from it that you wouldn't have otherwise."
                                    player_nvl "You're right. Thanks, El."
                                    bro_nvl "Anytime."
                                "•I feel pressure from the viewers.":
                                    player_nvl "Honestly, I feel pressure from the viewers."
                                    player_nvl "Especially since the raid."
                                    if viewershipHigh == True:
                                        player_nvl "It's kinda like people are expecting me to play Outlaw."
                                    else:
                                        player_nvl "Not a ton of people stuck around after Episode 2. So I'm wondering if I like should've changed my playstyle more."
                                    player_nvl "Idk, it feels a bit weird now."
                                    bro_nvl "You know, a wise person once said: \"just be yourself, and they'll see you for the warm, smart, and talented person you are."
                                    player_nvl "I think you're paraphrasing there."
                                    bro_nvl "A bit, yeah, but the point still stands."
                                    bro_nvl "You're gonna hit Affiliate because you're awesome and smart and talented."
                                    bro_nvl "If you feel pressure from the audience, I dunno, screw 'em. Just do you!"
                                    player_nvl "Thanks, El. You're really good at being encouraging."
                                    bro_nvl "I learned from the best :)"
                                "•I don't know.":
                                    player_nvl "Honestly, I don't know."
                                    bro_nvl "Come on, it has to be something."
                                    bro_nvl "Is it the game? Do you not like it?"
                                    menu:
                                        "•No, that's not it.":
                                            player_nvl "No, I really like the game."
                                        "•Maybe.":
                                            player_nvl "Maybe. It's been different than what I expected."
                                    bro_nvl "Was it something someone said in chat?"
                                    menu:
                                        "•I don't think so.":
                                            player_nvl "I don't think so. People have been really friendly, actually."
                                        "•No.":
                                            player_nvl "No, the people in chat have been really good."
                                    bro_nvl "Is it Kalena?"
                                    menu:
                                        "•Definitely not.":
                                            player_nvl "Definitely not, I haven't thought about her in months."
                                            bro_nvl "Ok, ok, just checking my bases."
                                    bro_nvl "Damn, I'm sorry. Wish there was something I could do to help."
                                    player_nvl "No I don't think this thing is like \"solvable.\""
                                    player_nvl "I'm just feeling a type of way right now."
                                    player_nvl "But you are helping, just talking like this."
                                    player_nvl "Thanks, El."
                                    bro_nvl "Anytime!"
                "•The grind for Affiliate sucks.":
                    player_nvl "The grind for Affiliate just sucks."
                    player_nvl "Like I'm playing this game and it's bringing in more viewers on the regular."
                    player_nvl "But jamming out smaller streams is just exhausting."
                    if energy < 5:
                        bro_nvl "Yeah, ngl, you look a bit tired in the streams sometimes."
                        player_nvl "Well that's kinda embarrassing lol"
                        bro_nvl "I mean, I don't think anyone else would notice."
                        bro_nvl "But like, I can tell when you're running on low energy."
                        bro_nvl "Sibling shit, y'know."                            
                    else:
                        bro_nvl "Really? On the VODs you look energized."
                        player_nvl "That's good to hear."
                        player_nvl "Sometimes I stream and I feel really good. Other times, it's rough."
                    bro_nvl "Mom always says life has its ups and downs."
                    bro_nvl "But I know you. And I know that you stream because it has way more highs than lows."
                    bro_nvl "Otherwise you wouldn't bother."
                    bro_nvl "Like just think about the people you've met from it that you wouldn't have otherwise."
                    player_nvl "You're right. Thanks, El."
                    bro_nvl "Anytime."
                "•Genuinely, things are just fine.":
                    player_nvl "No, genuinely, things are just good."
                    player_nvl "School is hectic, especially with the grind for Affiliate, but it's manageable."
                    player_nvl "I'm excited to come back home for Thanksgiving."
                    player_nvl "And the stream feels good."
                    player_nvl "Not like, incredible. But I like where I'm at."
                    player_nvl "That's kind of all I can ask for."
                    bro_nvl "You dating anyone?"
                    player_nvl "lmao well that came out of nowhere."
                    bro_nvl "I'm just saying it's been a while ok!"
                    player_nvl "I've been too busy recently. But I promise I will try to get back on the horse. For you."
                    bro_nvl "Good :)"
        "•It's getting pretty tough.":
            player_nvl "Honestly, it feels pretty rough out there."
            bro_nvl "Ah, I'm sorry to hear that."
            bro_nvl "What's up?"
            menu:
                "•The grind for Affiliate sucks.":
                    player_nvl "The grind for Affiliate just sucks."
                    player_nvl "Like I'm playing this game and it's bringing in more viewers on the regular."
                    player_nvl "But jamming out smaller streams is just exhausting."
                    if energy < 5:
                        bro_nvl "Yeah, ngl, you look a bit tired in the streams sometimes."
                        player_nvl "Well that's kinda embarrassing lol"
                        bro_nvl "I mean, I don't think anyone else would notice."
                        bro_nvl "But like, I can tell when you're running on low energy."
                        bro_nvl "Sibling shit, y'know."                            
                    else:
                        bro_nvl "Really? On the VODs you look energized."
                        player_nvl "That's good to hear."
                        player_nvl "Sometimes I stream and I feel really good. Other times, it's rough."
                    bro_nvl "Mom always says life has its ups and downs."
                    bro_nvl "But I know you. And I know that you stream because it has way more highs than lows."
                    bro_nvl "Otherwise you wouldn't bother."
                    bro_nvl "Like just think about the people you've met from it that you wouldn't have otherwise."
                    player_nvl "You're right. Thanks, El."
                    bro_nvl "Anytime."
                "•I feel pressure from the viewers.":
                    player_nvl "Honestly, I feel pressure from the viewers."
                    player_nvl "Especially since the raid."
                    if viewershipHigh == True:
                        player_nvl "It's kinda like people are expecting me to play Outlaw."
                    else:
                        player_nvl "Not a ton of people stuck around after Episode 2. So I'm wondering if I like should've changed my playstyle more."
                    player_nvl "Idk, it feels a bit weird now."
                    bro_nvl "You know, a wise person once said: \"just be yourself, and they'll see you for the warm, smart, and talented person you are."
                    player_nvl "I think you're paraphrasing there."
                    bro_nvl "A bit, yeah, but the point still stands."
                    bro_nvl "You're gonna hit Affiliate because you're awesome and smart and talented."
                    bro_nvl "If you feel pressure from the audience, I dunno, screw 'em. Just do you!"
                    player_nvl "Thanks, El. You're really good at being encouraging."
                    bro_nvl "I learned from the best :)"
                "•I don't know.":
                    player_nvl "Honestly, I don't know."
                    bro_nvl "Come on, it has to be something."
                    bro_nvl "Is it the game? Do you not like it?"
                    menu:
                        "•No, that's not it.":
                            player_nvl "No, I really like the game."
                        "•Maybe.":
                            player_nvl "Maybe. It's been different than what I expected."
                    bro_nvl "Was it something someone said in chat?"
                    menu:
                        "•I don't think so.":
                            player_nvl "I don't think so. People have been really friendly, actually."
                        "•No.":
                            player_nvl "No, the people in chat have been really good."
                    bro_nvl "Is it Kalena?"
                    menu:
                        "•Definitely not.":
                            player_nvl "Definitely not, I haven't thought about her in months."
                            bro_nvl "Ok, ok, just checking my bases."
                    bro_nvl "Damn, I'm sorry. Wish there was something I could do to help."
                    player_nvl "No I don't think this thing is like \"solvable.\""
                    player_nvl "You're helping right now, just talking like this."
                    player_nvl "Thanks, El."
                    bro_nvl "Anytime!"
    player_nvl "Oh and playing Oakley on stream is so different."
    player_nvl "Definitely not like back when it was just you and me."
    bro_nvl "Aahh good times."
    bro_nvl "Remember when I ripped the controller from you cause you threatened to insult Allistar?"
    player_nvl "I was teasing you a bit too much haha"
    bro_nvl "Now look at us."
    bro_nvl "Or you. Big bad outlaw >:)"
    menu:
        "•Yeah, sorry about Allistar.":
            player_nvl "Yeah, sorry about that"
            bro_nvl "lolwut"
            bro_nvl "Why are you apologizing?"
            player_nvl "For killing Allistar. I know he's your favorite character."
            bro_nvl "Oh, seriously? Don't worry about it"
            menu:
                "•But it wasn't even on purpose.":
                    player_nvl "But like, I didn't even do it on purpose."
                    bro_nvl "So what?"
                    bro_nvl "I mean yeah, if it were me, I probably would've stunned him. But it's your game."
                    bro_nvl "I know how many times you tried to play Outlaw Moze in Oakley 1."
                    bro_nvl "If a misclick actually got you to do it and see what that's all about, I'm happy for you!"
                "•Thanks for understanding.":
                    player_nvl "Thanks for understanding."
                    player_nvl "I figured you'd be disappointed you didn't get to see his story."
                    bro_nvl "Pfft that's your loss lol"
                    bro_nvl "I'm romancing the hell out of that hunk when I start my playthrough."
        "•I'm not that much of an Outlaw.":
            player_nvl "I'm not {i}that{/i} much of an outlaw."
            if marshal > outlaw + 5: #testing if I can check how much more one variable is greater than another
                bro_nvl "I know, I know, I've been watching the VODs."
                bro_nvl "Still gotta give you some guff for offing Allistar haha"
            elif marshal > outlaw:
                bro_nvl "Ehhhh"
                bro_nvl "Let's be real, you're on the borderline."
            else:
                bro_nvl "Srsly?"
                bro_nvl "I caught up on the VODs. I seen {i}everything{/i}."
            bro_nvl "But you do you. That's how you gotta stream, right?"
            if vig2_marshalEpilogue == True:
                bro_nvl "I will say, I am glad you didn't side with Matticus."
                bro_nvl "What a skeeve."
            else:
                bro_nvl "That Matticus alignment at the end of Episode 2 shocked me even more than the Allistar thing tbh"
            bro_nvl "I'm excited to check out Episode 3 when it goes up!"
        "•Outlaw life is good!":
            player_nvl "Like I said, Outlaw life is good!"
            if marshal > outlaw + 5: #testing if I can check how much more one variable is greater than another
                bro_nvl "Srsly? I was just talking about you offing Allistar"
                bro_nvl "I caught up on the VODs, I know you're back to goody two-shoes Moze haha"
            elif marshal > outlaw:
                bro_nvl "Ehhhh"
                bro_nvl "Let's be real, you're on the borderline."
            else:
                bro_nvl "Good, it looks like you're really into it on stream."
                bro_nvl "And I know how many times you tried to play Outlaw Moze in Oakley 1."
                bro_nvl "Glad you're getting the chance now."
    if vig3_brotherChat == 2:
        bro_nvl "Oooh maybe I should see if Cedric is down to play this game."
        player_nvl "Oh yeah, if he gets to take you to movies, you get to make him play games."
        bro_nvl "And test his moral compass at the same time >:)"
    else:
        bro_nvl "Can't wait till I get the chance to play this game."
        player_nvl "I'm excited to hear your thoughts when you get your hands on it!"
    if vig3_brotherChat == 1:
        player_nvl "That's enough about me though."
        player_nvl "What's up with you? Got any life updates?"
        jump vig3_macro_brother_stream
    else:
        jump vig3_macro_brother_end

label vig3_macro_brother_end():
    bro_nvl "Alright, I gotta go. High school never ends."
    player_nvl "Orchestra stuff?"
    bro_nvl "Nope, I gotta panic and figure out what I'm gonna wear on my date!"
    player_nvl "Lmao you have so much time."
    bro_nvl "I know. But I'm still nervous."
    player_nvl "It's gonna be a great time."
    player_nvl "Seriously, I'm so excited for you! Cedric's one lucky guy."
    bro_nvl "Thanks, [player]. I {i}really{/i} appreciate all your advice and just you listening to me when I freak out."
    player_nvl "Hey, I appreciate you listening when I need to talk about stream stuff."
    bro_nvl "Fair, haha"
    bro_nvl "Guess we have each other's backs."
    player_nvl "Always."
    bro_nvl "Love you, [player], have a good night!"
    player_nvl "Love you too, El! Take care!"
    hide discordview with dissolve
    scene bg black with dissolve
    "You close Loop'D and turn off your computer for the night."
    "The conversation with your brother eased some of the nerves you were feeling about finishing Oakley 2."
    "It was nice to chat with him."
    "And good to feel encouragement."
    "He's really growing up and into his own."
    "You spend the rest of your waking night thinking about how much your brother has grown until, eventually, you drift off to sleep."
    nvl clear
    pause 3.0
    jump vignette4Start














