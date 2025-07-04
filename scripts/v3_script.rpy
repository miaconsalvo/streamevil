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
    mS "It's nice always being the first one up, if it's even morning?"
    "I check the clock on the wall, yep, morning."
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
        "Be firm":
            mS "You can't go in like that. Fix yourself, I'll see you there."
    "I wait until I can feel her shoulder relax and walk out and down the hall, alone."
    hide teresa with dissolve
    jump vig3_sc2

label vig3marshalstart(): 
    show shiphub_stream at topleft onlayer background with dissolve
    "The Oakley is quiet today, and this coffee feels like I'm trying to cure every sleepless night I've had for the past few days."
    mS "It's nice to always be first one up, if it's even morning?"
    "I check the clock on the wall, yep, morning."
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
    pS "Yes Captain!" #(multiple=2) #same as before, we could also define a new character as "teresa and jennica"
    enS "Yes, Captain!" #(multiple=2) #same as before, we could also define a new character as "teresa and jennica"
    hide jennica with dissolve
    hide teresa with dissolve
    "I turn to the door and go out into the hall. I'm stopped by a tiny purple metal leaf and an excited MAC"
    #hide cockpit_stream
    show ship_hallway_stream at topleft onlayer background with dissolve
    macS "Captain."
    show mac stream neutral at stream_center_mac with dissolve
    "I can't help but jump."
    mS "Jeez MAC, remind me to let you take point on stealth missions next time."
    macS "Might I make a suggestion?"
    mS "A suggestion?"
    macS "Yes I have ideas"
    mS "MAC respectfully, I don't have time for this-"
    macS "Which is precisely why I have a suggestion, see I was scanning BigCorp databases..."
    "I feel frustration twisting my face." ##Dialogue choice that links to MAC's reaction here.##
    menu:
        "MAC that's dangerous!":
            mS "MAC please tell me after all this work to keep us safe you're not poking in BigCorp's networks!"
        "MAC it's not safe":
            mS "MAC don't go poking into BigCorp networks. After all the work the keep you safe." #more gentle way of chiding MAC about being inconspicuous#
    "MAC's head lowers" ## this reaction can differ based on choices##
    macS "I just wanted to be helpful..."
    "I let out a heavy sigh."
    mS "MAC you are it's just- What's your suggestion?"
    macS "An initial search suggests a nearby planet known as Solara, specifically the city of Akar. It may be suitable for our needs." 
    macS "However I should caution you..."
    "For a moment, the Oakley falls away from my view."
    "The low hum of the ship replaced by a crowded bar, the starting lines of song that will bellow out to bustling streets."
    "An old crew of Outlaws, drunk off a job well done."
    macS "Now there seems to be a significant amount of criminal activity, the crime rate is actually quite abnormal-"
    "I pat MAC's head interrupting him."
    mS "Good job buddy, rest up. I'll see you in an hour."
    "With every step I can't help but feel my smile grow, knowing this will be the calmest hour that I've had in a very long time."
    hide mac with dissolve
    jump vig3_sc3

##START OF ACT 1###
label vig3_sc3():
    show akarstreet_stream at topleft onlayer background with dissolve
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
    show mac stream neutral at stream_left with move
    "I almost didn't see the guy as he pushes past Teresa, getting a bit too close for comfort..." ##HOUND LEADER (early forties)##
    show teresa stream angry at stream_right
    show jennica stream angry at stream_left
    enS "Hey! Care to watch yourself?"
    #show houndleader stream neutral at stream_center with dissolve
    houndleaderunknown "Aw, smile a bit sweetcheeks, it's a celebration!"
    show jennica stream fight at stream_left
    "Before anyone can respond, Jennica punches the man in the face. He falls down hard and she puts her boot on his throat, Teresa leans over grinning." 
    #hide houndleader with dissolve
    "I can feel MAC on my leg as he hides behind me."
    $ reactTarget = "vig3_sc3_firstfight"
    show screen streamerCommentary
    enS "How's this, sweetcheeks?"
    "I can hear footsteps rushing to us. He's not alone."
    menu:
        "Pull out your gun.":
            "I pull out my gun in the direction of the sound." 
            mS "Not likely boys."
        "Show them you're a Snakehawk":
            "I lift my arm and flash the Snakehawks tattoo on my left hand."
            mS "I really wouldn't do that."
    #show houndgoon stream neutral at stream_center with dissolve 
    "The two men back away and fall back, they're well built but not sharp enough for a fight like this."
    "I give the signal to Jennica as she lets their friend scramble up before heading out."
    #hide houndgoon with dissolve
    hide screen streamerCommentary
    "The city moves as normal, uninterested in what just happened."
    enS "It's good to be back."
    hide teresa with Dissolve(0.5)
    hide jennica with Dissolve(0.5)
    hide mac with Dissolve(0.5)
    jump vig3_sc4

label vig3_sc4():
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    show mac stream neutral at stream_center_mac with dissolve
    #hide akarstreet_stream
    #show akarstreet_stream at topleft onlayer background with dissolve   
    "We arrive at the storefront of Specs and Steele, a small body shop just off the side of the main road."
    macS "Is this the most suitable store for our needs?"
    mS "Definitely. Run by an old friend. Probably one of the only ones that won't shoot first before taking our credits."
    "MAC pauses for a moment, thinking through something."
    macS "You seem to be worried about a lot violence. Did you do something Captain?"
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
    macS "A delicacy from the Vineyard, Reynar's Vira Brandy, named after his partner has a shelf life of 5 years."
    pS "See? Just made it!"
    hide mac with dissolve
    "With MAC trailing us I scan some of the newer gear, even some weirder stuff, weird for Steele."
    "Someone comes out from the back room."
    show rec stream neutral at stream_center 
    ###RECCRIN (Late 20s) enters from the back room. They looks like an older version of their brother Allistar, long hair, tougher build.##
    recS "Well I'll be..."
    "We can't help our silence in this moment."
    show jennica stream neutral at stream_left
    show teresa stream happy at stream_right
    pS "REC!"
    "Jennica runs up to hug Rec, they embrace and Jenn lifts them off the ground."
    pS "It's wonderful to see you kid."
    enS "Looking good, Reccrin!"
    recS "Thanks but I'm not much of a kid anymore."
    mS "I'll say."
    "I walk over slower than I should and go for a hug. Pushing the guilt down as I do."
    mS "What happened to Steele?"
    recS "Old man passed two years back, so I took over."
    mS "I know he was up in years but to think."
    pS "What happened?"
    recS "Nothing, just age, the years caught up to him."
    enS "Oh all the things I can't believe the years were what got him."
    pS "I was really lookin' forward to sharin' that brandy."
    recS "Well you're in luck."
    pS "Hell yeah!"
    show mac stream neutral at stream_left with dissolve
    macS "Vira Brandy is first invention using edible chimaeron fruit. Which is quite odd."
    pS "And delicious!"
    "As Rec turns to get the brandy they pause to look down at MAC."
    recS "And who's this little guy?"
    macS "I'm MAC!"
    recS "I bet you are!"
    "Rec's eyes grow wide, it's the same look Allistar gave him when they first met."
    recS "And where did they pick you up?"
    macS "From a top secret research facility in BigCorp headquarters."
    "If I could die right now I would. Reccrin just stares at MAC blinking rapidly."
    recS "... What?"
    #mS (Multiple Response options about how to lie)
    menu:
        "Might be too dangerous to tell Rec everything right now."
        "Just a courier bot we picked up.":
            mS "Just a courier bot we found and outfitted figured we could use an extra hand and a morale boost..."
        "Top secret? Please.":
            mS "If by top secret you mean off a random shelf, then sure, keep it hush hush though."
        "Teresa did you program that?":
            mS "That's the last time I let you touch our gear Teresa."
    #^All of these feel mean....could use a rewrite#
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
    recS "Sorry yeah got carried away. What do you need? New parts?"
    enS "Definitely a range extender."
    pS "Honestly even the base parts could use an upgrade. If you have some to spare."
    mS "We needa get outfitted and going in the next few days."
    recS "Got it, lemme check the back, I might have something for you."
    #hide rec with dissolve
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
            mS "MAC I'll be honest, I'm not being fair. But we need their help and that's a conversation for after."
        "They'll know after we get the part":
            mS "Range extender first, hard talk later. We can't leave here without it."
        "I have no love for Allistar":
            mS "I'm not about to apologize for what I needed to do. They'll find out eventually."
    "Reccrin comes out after a brief moment with a long antennae and some internal parts for our Comms."
    show mac stream neutral at stream_left with move
    show rec stream neutral at stream_center with dissolve
    recS "Definitely an older model but she should work better than what you got. Need an install?"
    enS "I could use the hand."
    pS "Thanks Rec."
    mS "It's very appreciated."
    recS "No worries! Hey since y'all have been on the move, you wouldn't have happened by Al at all?" 
    recS "I haven't heard from him in while."
    "There's too long of a pause that I can't think of something fast enough. But thankfully I didn't have to as the shop door swings open."
    hide mac with dissolve
    hide jennica with dissolve
    #show houndleader at stream left with dissolve
    "A group of five enter the shop, dark uniforms with a dog patched on their right shoulder." 
    "These guys, they're ones who gave Resa a hard time." ##The Hound Leader##
    $ reactTarget = "vig3_sc4_houndraid"
    show screen streamerCommentary
    houndleader "Alright Reccrin, you know the drill! Mandatory sweep!"
    houndleader "Don't cause any-oh!"
    enS "You must be joking."
    houndleader "Sweetcheeks."
    enS "Bite me."
    houndleader "Maybe later, I'm on the clock now."
    hide teresa with dissolve
    mS "Didn't know Akar hired rent-a-cops."
    #show houndgoon at stream_right with dissolve
    "A smaller Hound one moves up next to leader, she's clearly the next toughest and with something to prove."
    houndgoon "I suggest you get yourself and your crew in order and stay out of the way."
    hide screen streamerCommentary
    "Rec looks at me with a forced smile."
    recS "Please Moze."
    recS "Hounds! We don't want any trouble, just do what you need to do."
    houndleader "That's what I like about you Rec, so reasonable."
    "We stand back as the group rummages through the store, knocking over shelves and taking random items." 
    "They're armed to the teeth and now I understand why Rec is so quick to comply."
    ###Describe the wreck this group is leaving and give the players two opportunities to intervene or continue to comply silently.###
    menu:
        "They trash the place"
        "That's enough!":
            mS "Alright that's enough!"
        "Let them continue":
            "They keep trashing it."
            "I cringe as each piece falls. Broken parts start to litter the floor."
            menu:
                "Do I intervene?"
                "That's enough!":
                    mS "Alright that's enough!"
                "Stay quiet.":
                    "They continue to trash the shop. More carnage. They're laughing to each other, tossing equipment like a hackey sac."
                    "I see one of them try to head to the back room."
    mS "Alright that's enough!"
    houndgoon "You'd be best to stay out of official business."
    "Another uniform chimes in."
    houndgoon "We're under order to collect contraband."
    mS "Contraband? That's rich, learned that from the little pamphlet they gave you?"
    houndgoon "Tryna be smart are we?"
    mS "Someone has to."
    houndgoon "Contraband is whatever we say it is."
    houndleader "We'll also be taking this."
    "The Hound's leader goes to pick up the antennae for the Coms that's sitting on Rec's store counter." 
    ###Streamer reaction: Of course he does###
    recS "This item is being sold to customers at the moment. I can assure you it's perfectly legitimate."
    houndleader "Are you admitting to selling contraband Reccrin? That's cause for reprimand."
    mS "That so called \"contraband\" is mine. And they said it's perfectly legit."
    "I slowly walk up to the counter moving to take the parts."
    mS "So I'd like it back now."
    "The uniforms turn to us and I know they're gearing up for a fight. They probably won't kill us, but I can't imagine how banged up we'll be or what happens if they find MAC." ###The player must decide between three actions, fight, let them have it, or Bribe - IF THEY HAVEN'T BRIBED REGI###.
    menu:
        "How do I deal with this?"
        "Fight them.":
            "I get into his face - let him pry my gear from my cold dead hands. He smiles and throws the first punch before I can react." 
            "It knocks the wind out of me and I hit the ground."
            "Then impact after impact to my stomach before I can catch my breath. He gets low, right to my ear."
            houndleader "You should've died with the rest of the Snakehawks."
            "He takes the antennae as I struggle to get up from the floor."
            houndleader "Pleasure doing business with you."
            "The Hounds leave us to pick ourselves up and walk out of the shop. MAC who has thankfully been hiding rolls forward."
            hide houndgoon with dissolve
            hide houndleader with dissolve
            show mac stream neutral at stream_left with dissolve
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            macS "Captain are you hurt?" 
            mS "Just my pride."
            "Teresa goes to pull me up."
            enS "I want to burn that man from the inside."
            pS "Maybe we can use him as our antennae instead."
            mS "Now that's a thought. Rec, you know those guys?"
        "Let them take the antenna.":
            "I take a step back, we can't afford a fight right now, it's too risky."
            houndleader "Pleasure doing business with you."
            "The Hounds turn to leave knocking some stuff around."
            "On the way out with the parts, the Leader hits me with a good punch while I'm off guard."
            hide houndgoon with dissolve
            hide houndleader with dissolve
            show mac stream neutral at stream_left with dissolve
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            macS "Captain are you hurt?" 
            mS "Just my pride."
            "Teresa goes to pull me up."
            "Sorry I didn't want to put you all in more danger."
            enS "You're good Captain."
            enS "Makers I'd like to blow that man up from the inside."
            pS "Maybe we can use him as our antennae instead."
            mS "Now that's a thought. Rec, you know those guys?"
        "Try and bribe them" if reginaldChoice == False: #This option shoudl still be here but different outcomes based on the variable.
            "I take out my communicator,"
            mS "Listen this doesn't need to be ugly, we'll pay the tarriff and get out of your hair."
            houndleader "Finally a sensible idea." #it doesnt work right? they need to take the antenna to force the crew to keep looking
            "We do the transfer and as it completes I'm hit dead on without warning."
            "He grabs the part and the Hounds move out."
            houndleader "Pleasure doing business with you."
            "The Hounds commit some extra carnage on the way out."
            hide houndgoon with dissolve
            hide houndleader with dissolve
            show mac stream neutral at stream_left with dissolve
            show jennica stream neutral at stream_left with dissolve
            show teresa stream neutral at stream_right with dissolve
            mS "Just my pride, and my wallet."
            "Teresa goes to pull me up."
            enS "I want to burn that man up from the inside."
            pS "Maybe we can use him as our antennae instead."
            mS "Now that's a thought. Rec, you know those guys?"
    "They pull out five glasses. And drop a bottle of brandy on the counter"
    "As they start to pour, they stop themselves at the fifth and grab an oil can and pour it in giving it to MAC."
    macS "Thank you!"
    recS "They're the Hounds. Reynar's new security detail."
    recS "Usually they're more of nuisance than anything. Shaking down shops and bars."
    recS "But with the Inventor's Fair they've gotten more excitable. Not surprised they'd come by here just terrible timing is all."
    pS "Sorry what's the Inventor's Fair? I forgot to ask."
    enS "Big conference. Lots of tech companies, scholars, and start-ups from all over. Schmoozing and rubbing shoulders, the like."
    pS "Sounds like a party."
    enS "One of the biggest."
    mS "We're steering clear. Rec anyone else you know who can get us the part we need?"
    recS "Not top of mind but I can show you around and we can probably find something."
    mS "Sounds like a plan."
    "Reccrin holds their glass up and swallows their drink in one gulp. We follow suit."
    amaS "Ah that's the stuff."
    "I stop the glass at my lips and nearly drop it. Whipping my head around I almost grab for my gun until I catch Jennica's eyes."
    pS "All right, Cap?"
    "I compose myself and try to calm down."
    mS "Ya, sorry."
    "When I swallow my drink, it goes down hard."
    hide jennica with dissolve
    hide teresa with dissolve
    hide rec with dissolve
    hide mac with dissolve
    jump vig3_sc5

#END OF ACT 1#

#START OF ACT 2#

label vig3_sc5():
    hide reccshop_stream
    show akarplaza_stream at topleft onlayer background with dissolve 
    "When Rec leads us to the plaza I'm almost startstruck with how it looks." ###REC takes the Oakley Crew to the Plaza. In front is Rec and MOZE with JENNICA and TERESA taking up the rear with MAC in between them.##
    "The space is abundant with life. The shops and bars on the outer ring of the roundabout shine with bright flashing lights and are bursting with patrons." 
    "Music and reverie pour out like sections of a cacophonous orchestra."
    "At the center is a park area that sits a large statue of a man sitting at a tree, staring at an apple in his hand." 
    "The statue has a massive hole blown out of it."
    show rec stream neutral at stream_center with dissolve
    show jennica stream neutral at stream_left with dissolve
    show teresa stream happy at stream_right with dissolve
    show mac stream neutral at stram_left with dissolve
    recS "Alright Oakley it's been a while but welcome to the Plaza!"
    macS "Wow...."
    pS "Surprised it's still standing."
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
    "BigCorp officers scattered attempting to suppress the riot."
    "With small fires everywhere Teresa hangs from the arm of a statue of a man in a lab coat, Jennica and I look on, blasters in hand."
    enS "We're gonna be *HICK* glorkin *HICK* LEGENDS HAHA!!!"
    pS "Pffffft! Glorkin?"
    mS "Resa hey hey Resa, ya gotta, gotta down from there."
    enS "Not until you say it."
    pS "A wild one for sure."
    mS "She's really set huh."
    pS "Please do the honors Captain."
    "An enforcer in the distance fires a shot at the statue and misses."
    mS "Okay okay, you're in!"
    enS "No, no, do the call, it's not real without it."
    mS "The call isn't real, get down from there."
    enS "I KNOW IT'S REAL!"
    "Another bullet narrowly misses Teresa"
    pS "Better do the call Cap."
    enS "SEE!!! THERE IS ONE!!"
    "These two are gonna be a problem."
    mS "CAW CAW HISS HISS"
    "We all laugh"
    enS "LEGENDS!! LONG LIVE THE OAKLEY!!!"
    "Teresa sticks something to the statue and leaps off."
    enS "Hehe catch me!"
    "I'm barely able to catch her in time."
    mS "I got ya!"
    "I carry Teresa in my arms, Jennica trailing quickly behind just as the bomb detonates and blows the statue sky high."
    show teresa stream happy at stream_right with dissolve
    mS "I'd bet money this place hasn't seen a bigger stunt than that."
    amaS "...You bet?"
    "I jump and turn to the direction of the voice, this time I make it to my gun."
    $ reactTarget = "vig3_sc5_amahallu"
    show screen streamerCommentary
    "When I come to I realize I've scared the young showgirl behind me near to death."
    show showgirl stream at stream_left with dissolve 
    mS "What?"
    "She stares wide eyed and is taken her off script."
    showgirl "Uh um, name's Daisy, do you bet?"
    mS "Do I bet if your name is Daisy?"
    showgirl "Well if you did you'd be a winner, and you can win bigger at NOVA CASINO!"
    showgirl "First 50 Credits are on us!"
    "She attempts to hand me a casino card, it's holographic with an animation of a supernova and 50 credits in big lettering."
    mS "Thanks but no thanks."
    showgirl "Well, have a nice day!"
    hide streamerCommentary
    "Daisy hurriedly leaves and heads to another group to perform the same spiel. I see her carefully get their attention this time."
    hide showgirl with dissolve
    show teresa stream shock
    show jennica stream shock at stream_left with dissolve
    show mac stream shock at stream_left with dissolve
    show rec stream neutral at stream_center with dissolve
    pS "Alright alright, what's this about?"
    enS "You've been anxious all day Captain."
    mS "I'm fine."
    recS "You just yelled at girl wearing feathers, I beg to differ."
    macS "We are concerned."
    mS "I'm tired is all."
    show teresa stream neutral at stream_left
    show jennica stream neutral at stream_right
    recS "You know most of the shops are closing for the day. Let's set you up somewhere for the night."
    recS "I think the Broken Bulb has a deal on pints."
    "We begin to move out. Jennica begins a story involving a lamp, three chickens, and a guitar. MAC is confused but enthralled."
    "I can't help but look back at Daisy with the small rough-looking crew. Her eyes fixate on the only person whose back is turned to me."
    "They're tall and well built with a wide brimmed hat, in all dark leather, and long black familiar hair."
    macS "Are you coming Captain?"
    mS "Sure thing kid."
    hide jennica with dissolve
    hide teresa with dissolve
    hide rec with dissolve
    hide mac with dissolve
    jump vig3_sc6

label vig3_sc6():
    hide akarplaza_stream
    show bbpub_stream at topleft onlayer background with dissolve
    "It took some time to get through Akar, MAC wanted to see everything he could."
    "As if it would disappear if he took his eyes off it."
    "The days are shorter this time of year and when night falls we make it to the Burnt Bulb."
    "The Burnt Bulb Pub feels like it's been stuck in time. 
    It's wooden paneling, the carnivorous plants that line its ceilings."
    "There's a warmth to this place, I feel like that young Outlaw scared out of my mind, clinging to Ama and hoping I won't get bulldozed at my first brawl."
    show rec stream neutral at stream_center with dissolve
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    show mac stream neutral at stram_left with dissolve
    macS "Cozy."
    "MAC's face drops as a someone yells and is then quickly tossed through a window. He clings to my leg."
    macS "Aren't their children around outside?"
    pS "That's why he was tossed out the back window."
    enS "This is a respectable place after all."
    recS "Only the best for the Oakley."
    recS "Hopefully they're not booked up 'cause of the Fair."
    enS "Let's find out."
    hide rec with dissolve
    mS "Thanks guys, we'll get a spot."
    show mac stream neutral at stream_center_mac with move
    "As we walk through the bar, I notice how may regulars have been lost to time.
    Akar is different now."
    menu:
        "It's been a while since the Oakley was in Akar."
        "Being invisible is what we need.":
            "There's a small comfort in not being immediately recognized."
            "It's better for MAC."
        "Surely not everyone forgot us.":
            "I'm sure some more people remember who we are."
            "May need to be careful from here on out."
        "They could never forget us.":
            "I don't care how long its been the Oakley is still legendary."
            "Maybe we should remind them who we are..."
    "I make sure we get our table, gently pushing off a passed out patron by themselves. I buy us a round."
    "And then another."
    "And another."
    show mac stream neutral at stream_left with move
    show rec stream neutral at stream_center with dissolve
    recS " So I said, \"You should've been more specific about the screw!\""
    show teresa stream happy at stream_right
    show jennica stream neutral at stream_left 
    "Raucous laughter pours out of us, barely audible in this crowded bar."
    enS "Makers, that's dumb."
    macS "Now I found that funny but can someone clarify the part about the screw?"
    enS "Well you see \"screw\"-"
    show jennica stream shock at stream_left
    "Jennica covers what she thinks are MAC's ears."
    pS "Too young, too impressionable."
    show teresa stream neutral at stream_right
    enS "He's a courier bot, it's fine."
    show jennica stream angry at stream_left
    macS "That's not where my ears are."
    pS "C'mon a bot? Get out!"
    macS "That is not an incorrect statement."
    show teresa stream angry at stream_right
    enS "Why must you be so emotional about everything?"
    pS "And why ya gotta be a cold hearted b-"
    recS "WOAH! How about I go and get us another round."
    recS "C'mon buddy, I'll get you a treat."
    hide rec with dissolve
    hide mac with dissolve
    "MAC looks at me expectantly."
    mS "In eyesight, got it?"
    "MAC lets out an excited noise and heads to the bar with Rec."
    "The table is silent."
    mS "I owe you both an apology"
    "Jennica and Teresa perk their heads towards me."
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
    mS "Okay okay, that's enough"
    "Jennica raises her glass."
    pS "We got your back Moze."
    "Teresa raises her glass."
    enS "Always."
    "I raise mine in response."
    mS "Long live the Oakley!"
    # maybe fade in and out, show the passage of time
    hide teresa with dissolve
    hide jennica with dissolve
    "As the night continues on, the Broken Bulb becomes more and more packed, the empty glasses on our table sit in tall stacks as a barkeep cleans them."
    "Teresa is in a corner watching in unwavering curiosity at the plants that line the ceiling, tossing bits of food up for them to catch."
    "Jennica is at a pool table, chatting away with some couple who stare at her in amazement."
    "Rec is telling MAC a story that has him fully engaged. But he keeps looking around the room nervously."

    #This would normally be a menu with multiple choices but for simplicity and time we'll only have MAC and Rec and the stranger

    "I should check in on MAC, see how he's holding up." 
    "Just as I get up I notice that wide brimmed hat again, long dark hair, she walks right past me and out the door."
    "There's a chill that runs down my spine."
    ###Recount choice again###
    menu:
        "Do I investigate this stranger?"
        "Follow them":
            "I follow the stranger out of the bar and every fiber in my being is yelling at me that this is a bad idea."
            hide bbpub_stream with dissolve
            show akarplaza_stream at topleft onlayer background with dissolve 
            "I struggle to navigate the dark winding streets the stranger tucks away behind an alley and I move to close in on them."
            "As I turn the corner I'm met with a knife to my throat. So clearly not Ama's style."
            show stranger 1 stream at stream_center with dissolve
            "The stranger eyes bright and blue with a heart-shaped face and a mole under her left eye."
            strngr1 "Why are you following me?"
            mS "I'm sorry I just-"
            "She presses the knife into my neck."
            strngr1 "You what? Thought I was some easy mark."
            "She's young in her voice and her confidence."
            mS "No, I just thought you were someone else."
            "She doesn't let go of the knife."
            strngr1 "Well sorry to disappoint. But I don't take kindly to being followed."
            "I should say something to get out of this." #Options: Hands up and walk away, flirt, wrestle the knife away.
            menu:
                "How do I get out of this?"
                "Flirt.":
                    mS "Oh, I'm far from disappointed." #flirt
                    "A small smile comes on her face."
                    strngr1 "Oh yeah?"
                    mS "You're a much more pleasant sight if I say so myself."
                    "She doesn't let go of the knife but moves in closer."
                    strngr1 "You're not an eyesore yourself."
                    mS "Ouch I'm hurt."
                    strngr1 "Not yet, but the night's young."
                    "When the knife falls we close the distance and tuck ourselves deeper in the alley, far away from eyesight."
                    hide stranger 1 stream with dissolve 
                    "I return to the Broken Bulb a bit disheveled hoping that the small nick on my neck has started to scar over."
                    "I go to see Mac and Rec."
                    hide akarplaza_stream
                    show bbpub_stream at topleft onlayer background with dissolve
                "Hands up, walk away.":
                    mS "Look this got out of hand."
                    "I hold my hands up and start at her trying to relax the situation."
                    strngr1 "Ha, what can't follow through?"
                    mS "Nothing to follow through on."
                    hide stranger 1 stream with dissolve 
                    strngr1 "Pathetic"
                    "Her knife doesn't move but she nods her head to tell me to get lost."
                    "I don't take my eyes off her when I back away"
                    "I return to the Broken Bulb disappointed."
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
                            "Knee to the chest."
                        "No. I've made my point.": 
                            "I shove her against the wall and she falls over."
                            "The knife clatters away."
                    "It's over before it even starts."
                    mS "Need me to call someone for you."
                    strngr1 "Go to hell."
                    mS "Trust me they know I'm coming."
                    hide stranger 1 stream with dissolve 
                    "I return to the Broken Bulb and wipe a bit of dust off my jacket before heading in."
                    "I go to see Mac and Rec"
                    hide akarplaza_stream
                    show bbpub_stream at topleft onlayer background with dissolve

        "Check in on MAC and Rec":
            "I can't follow paranoid hunches, I gotta stick to my crew."
            "Rec and MAC are chatting at the bar, I get the tail end of their conversation."
            recS "You know when you've lived here for so long you get used to it truly."
            macS "But it's so dangerous, are you not worried?"
            recS "Of course I worry, but no use in worrying all the time."
            menu: 
                "Say something."
                "They're right you know.":
                    mS "They're right, just because something is difficult doesn't mean you need to be consumed by it."
                    mS "People do plenty of things that make them worried, how you wrok through that is more important."
                    macS "I think I understand."
                    recS "Thanks Moze. You know I do admire what you do, it's a tough life but it's yours."
                    "I smile."
                    mS "It has it's good moments."
                    macS "Like candy!" 
                    mS "Exactly. That's why we go through the worry."
                "You should really consider moving":
                    mS "Rec every thought moving would be the right call?"
                    recS "Oh that's rich coming from you."
                    mS "I'm just saying there's better places than one riddled with Hounds."
                    macS "I didn't see much of a dog population here."
                    recS "I like my shop and my community, I don't regret planting roots here."
                    recS "I'm happy I didn't become a Snakehawk."
                    "A pit forms in my stomach."
                    mS "I'm happy your found a place that is yours."
                    recS "I'll be sure to fight for it."
                "Akar is beautiful if you look in the right places":
                    mS "It may not look it but Akar is beautiful."
                    mS "Sometimes the worrying makes sense if you have a community where you are."
                    macS "Like what we have?"
                    mS "Yeah kid."
                    recS "So cute..."
                    "I feel my face get warm."
                    mS "You always look for the beautiful parts it's the whole point."
            "A part of the bar goes silent as a bald burly man stands to address the crowd."
            show zan stream at stream_center with dissolve
            zan "Patrons! Who is brave enough to ride Karousel!"
            "Oh god not this game. What kind of idiot would even take that challenge-"
            pS "Right here!"
            "Jennica marches to the man who laughs."
            show jennica happy stream at stream_left with dissolve
            zan "So small, already tipping over, I fear you may not survive haha!"
            "A small group of patrons at a table behind him laugh."
            pS "Then you have nothin' to worry about."
            zan "Apologies but I will not pick you up from the floor when you lose."
            pS "Please."
            "Teresa saddles up next to Jennica."
            show teresa happy stream at stream_right with dissolve
            enS "The lady said she'd like to ride the karousel."
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
    show mac neutral stream at stream_center_mac with dissolve
    show rec neutral stream at stream_right with dissolve 
    macS "Are they playing Brikarousel?"
    recS "Aren't you too young to know that game?"
    macS "I have a full database that allows me to know a myriad of games."
    recS "A full database..."
    "Rec's eyes move back on the gambling table, Jennica and Teresa are deep in conversation."
    recS "You know I never understood this game."
    macS "Well Brikarousel was invented by Brika Alphonse approximately 30 years ago when..."
    recS "I meant why people are so eager to play."
    macS "Oh."
    macS "Alcohol?"
    mS "You catch on quick."
    "I look over at the table as a pit in my stomach forms."
    mS "Bet? What did they bet?"
    recS "I didn't hear but I read lips a bit, a “sh” something?"
    mS "\"Sh\" something???"
    macS "Shirt, shoes, shilling..."
    "Ship? They wouldn't-"
    hide rec with dissolve
    hide mac with dissolve
    "No that's stupid."
    "Then I remember who's playing the game." 
    "Shit."
    show jennica neutral stream at stream_left with dissolve
    show teresa neutral stream at stream_right with dissolve
    show zan stream at stream_center with dissolve
    "Though I would assume Zan (as he keeps reminding everyone) would pick the tough looking women as his partner, instead it's a small man with dark hair and modified gray skin."
    pS "Talkin' to us about bein' small and your guy is thinner than my jacket."
    zan "Ovid is strong of heart, muscles on the inside."
    enS "That tends to be where they go yes."
    ovid "Zan must we always play this game whenever we go out?"
    zan "OF COURSE! HAHA!"
    "The game starts off with a bang, the rules are simple, teams of two play hands to collect played cards from a pool." 
    "Some cards are worth points, the pair with the lower amount of points at the end of the round takes a shot from the karousel."
    "The first team that withdraws or has a member drop loses."
    "...By round ten, it's not looking good."
    zan "How is moxie?"
    pS "Stronger than my mama's back!"
    enS "I'm starting to feel mine in the back of my throat."
    "Teresa and Jennica look wrung out but Zan and Ovid are sturdy despite drinking their fill."
    hide jennica with dissolve
    hide teresa with dissolve
    hide zan with dissolve
    show mac neutral stream at stream_center_mac with dissolve
    show rec neutral stream at stream_right with dissolve
    macS "They're cheating."
    recS "How did you-"
    mS "Of course! We've been out of the game too long."
    macS "We must tell someone, this is improper."
    mS "MAC I'm going to lay this out for you. No one cares if something is improper here."
    macS "Then we should do something."
    mS "I'm already on it."
    macS "And I'll help."
    menu: 
        "Say something."
        "Abosultely not!":
            mS "You will sit down and say nothing and let me handle it."
            macS "But I-"
            mS "Understand?"
        "It's better if I just do it.":
            mS "This is better as a solo mission."
            macS "But I-"
            mS "It'll be fine don't worry."            
    macS "But I'm part of this crew too *Ama*!"
    "That was my voice. Upset, scared of being left behind."
    mS "You are, and you'll have other chances to prove it. Just not right now."
    "When Jennica calls for a short recess I know that's my time to head over."
    hide mac with dissolve
    show jennica neutral stream at stream_left with dissolve
    show teresa neutral stream at stream_right with dissolve
    mS "I don't know if you've noticed..."
    pS "We're losing-"
    enS "They're cheating."
    enS "So are we just not as effectively."
    mS "Better think of something fast after what you just bet."
    pS "Ya Resa, I don't think hand signals are going to cut it here."
    "I swallow the knowledge that hand signals were the only thing they thought of after betting our ship."
    "There has to be signs for how they're doing this."
    "Ovid stares blankly across the room poking at something metal in his mouth."
    pS "Ovid's not drinking."
    enS "An evaporator..."
    pS "Was wondering how that little guy is still standing."
    "I look around the room for more signs."
    pS "The deck isn't right. I know a standard set when I see one."
    mS "That makes sense, especially if they're regulars."
    "What else. Teresa's eyes are fixed on the Karousel."
    enS "The Karousel. There's a delay before it settles. And one of their friends has been staring at his communicator all night."
    "Ovid's tube, the deck, the karousel. We have to deal with them."
    pS "We need to tip the table."
    enS "Can't do that while we play."
    pS "I got it covered, just stay standing until I do."
    "The game resumes and I step away."
    show zan stream at stream_center with dissolve
    zan "Now! Moxie!"
    "I scan my options."
    "If I start a fight I'm sure I can get someone slammed into the table. That should take care of some of the issues."
    "I look at the ceiling where the carnivorous plants lie waiting and salivating."
    "One of the ropes for their netting looks frayed and worn if I undo it then it's open season on that table. Maybe quits for the Karousel."
    hide zan with dissolve
    hide jennica with dissolve
    hide teresa with dissolve
    menu:
        "How do I help Jennica and Teresa?"
        "Start a bar fight.":
            "I see a young couple pinning each other on a pillar near the table." 
            "When they separate I go up to the young man and shove him."
            mS "How dare you! We spent five glorious nights together, you tell me you love me and after months of not hearing from you I find you here with a random woman!"
            wifenpc "Random! I'm his wife!"
            husbnpc "What? huh? I don't-"
            mS "Oh typical, you don't what? Know me? Don't even remember proposing to me do you?"
            wifenpc "PROPOSE! So that's what you've been doing on your business trips huh?"
            husbnpc "No-what?!? I don't even know her!"
            "Before I can even add fuel to the fire. With a one-two combo that almost lands the young woman a spot on the Oakley, the man fumbles onto Ovid and the table."
            "Cards fly everywhere and before I can process what happens Zan has the man in a chokehold."
            show zan stream at stream_center with dissolve
            zan "Fool! You interrupt the Karousel!"
            "It's hand fifteen, and half the bar is up in arms, friends of the man square up with Zan's crew. It's only when tiny Mr. Stein waddles to the table and promises a free round that the room begrudgingly settles."
            "Ovid coughs loudly before putting something in his pocket, with cards scattered all over the floor the deck is replaced."
            "The Karousel is untouched, the rounds continues."
            hide zan with dissolve
        "Cut the rope holding the carnivorous plants":
            "I take a look at the frayed rope and the netting that is so carefully holding back the plants."
            "It's too easy and so dangerous, people might definitely get hurt."
            "I move carefully to the hook with the rope."
            mS "Excuse me sorry just tryna get a decent view"
            husbnpc "Watch it mna, c'mon we all want a good view."
            "I push my way to wall and lean just behind it."
            "The rounds are continue."
            zan "Another victory, another shot for you."
            pS "Fine meathead, you got it."
            enS "Makers this is insanity."
            "Then I get an idea."
            mS "Drink! Drink! Drink! Drink!"
            "The bar is in an uproar people are going to grab their nearest cups."
            "They're slamming the floor, the room is shaking"
            "A roaring cheer, I cut the rope."
            "It's hand fifteen, and the plants decend onto the crowd, it's madness."
            "One took a solid swipt at Jeneca and another a bite of Teresa's arm."
            enS "GET IT OFF!!!"
            "Ten patrons were injured, the attacking plants destroyed, two people carted off to the backroom until help arrived."
            "Stein with the help of his crew subdued the other plants, who sleep restfully over a new net with strung up."
            "Ovid coughs loudly before putting something in his pocket, The Karousel is replaced by a beat up version."
            "The round continues."

    #maybe fade in and out to show passage of time again?#
    
    "Round 25 is rough. Even with some of the obstacles out of the way Teresa and Jennica are barely holding on. Ovid is finally looking like he's playing the game and Zan is rocking in his seat like a child."
    ovid "Please, call it quits?"
    show teresa stream neutral at stream_right with dissolve 
    enS "Not likely."
    show zan stream at stream_center with dissolve
    zan "Hehehe, I say I am impressed. And having the best of times!"
    show jennica stream neutral at stream_left with dissolve
    pS "Not after this you aren't."
    "When Zan and Ovid lose the round an opportunity presents itself. Zan will tip his chair back, one clean shot to the leg and he's on the ground. But that's risky."
    "I could just leave it to the two of them to take it home, Ovid looks like he's on his last legs. But if they actually bet the ship then I don't know how we're gonna get it back."
    ###Two choices and three endings. If the player doesn't shoot they may or may not win which will have two separate endings. If they do shoot they will automatically win, this is also the Ama choice###
    menu:
        "How do I finish this?"
        "Shoot Zan's Leg":
            $ outlaw += 1
            $ macViolence += 1
            $ macPessimism += 1
            "I can't leave it up to chance, the crowd is completely absorbed by this game."
            "Zan has a notable plate on his leg, a good shot should send him flying with minimal damage. Hopefully" "I take my position."
            "As I scan the bar for any eyes on me, I take in just how packed this place is. It's wall to wall."
            "Then I see them, a small group near the door, half watching the game. Is that? No. My vision is still betraying me and I don't have time to get a better look."
            zan "FOR MY LOYAL FANS!"
            "Zan does a messy cheers to Ovid, teeters his chair back to knock the shot into his mouth."
            "As I pull the trigger Zan's eyes meet mine. Damn."
            play audio "lazer.wav" volume 5.0
            hide zan with Dissolve (0.1)
            "Zan falls hard, the pub is silent."
            show jennica stream neutral at stream_left
            show teresa stream happy at stream_right
            pS "HELL YEAH!!!"
            "The crowd erupts, Zan's crew is visibly miffed but the rest of the bar is patting Teresa and Jennica on the back."
            show zan stream at stream_center with dissolve
            "Zan gets up to accept defeat, Ovid has fully crawled under the table."
            "I look over again to the crew, but that table is empty."
            "The door swings closed."
            ovid "Thank the Makers it's over."
            zan "Good, good! NOW! I must go and throw up. HAHA!"
            "The three exchange handshakes as Zan passes by me and stops."
            zan "You are Captain, no?" 
            menu: 
                "Respond to Zan."
                "And what's it too you?":
                    mS "And what's it to you?"
                    zan "You have a good crew, good moxie."
                    mS "I'm aware."
                "The one and only!":
                    mS "The one and only!"
                    zan "You have a good crew, good moxie."
                    mS "We like to show out."   
            "Good shot, but messy. Have more faith next time."
            "Before I can respond, he pats my shoulder and I almost buckle under the weight of the impact."
            hide zan with dissolve
            "I move to greet my victors."
            mS "I can't believe you pulled that off. That was some risky business."
            pS "C'mon Cap, just harmless fun."
            mS "Betting the ship is harmless to you?"
            enS "The ship? What do you take us for? Zan asked us to perform a show for the bar if we lost."
            mS "A show?"
            pS "Mighty embarassin' that've been, Everyone knows Resa sounds likes a torn up gear when she sings."
            enS "Agreed."
            pS "But alls well, big guy told us he'd comp our room for the night."
            "I'm truly losing it."
            mS "Alright, well congrats then. I'm turning in."
            hide teresa with dissolve
            hide jennica with dissolve
        "Trust the crew to win.":
            $ marshal += 1
            $ macHope += 1
            $ macPeace += 1
            #need a variable to determine if they win or not.
            "There's a part of me that know I'll regret this but I don't go for my pistol."
            "These two are idiots but they're my idiots and I have to trust they'll pull through."
            "The hands keep going."
            "So do the drinks."
            "26, 27, 28..."
            "...29..."
            "Then a loud crash."
            mS "No way" 
            macS "Oh my..." 
            $ vig3_brika = renpy.random.randint(0, 1)
            if vig3_brika == 0:
                show jennica stream neutral at stream_left
                show teresa stream happy at stream_right
                "Ovid is under the table."
                mS "WE DID IT!"
                "The whole bar is roaring!"
                "Zan pushes the table away and goes to make sure Ovid is alright "
                "I move to greet my victors."
                mS "I can't believe you pulled that off. That was some risky business."
                pS "C'mon Cap, just harmless fun."
                mS "Betting the ship is harmless to you?"
                enS "The ship? What do you take us for? Zan asked us to perform a show for the bar if we lost."
                mS "A show?"
                pS "Mighty embarassin' that've been, Everyone knows Resa sounds likes a torn up gear when she sings."
                enS "Agreed."
                pS "But alls well-"
                "I'm truly losing it."
                "Just then Zan comes over to us and kneels."
                zan "I must make good on promise."
                "Teresa and Jeneca each take a seat on one flexed arm."
                "Zan hoists them in the are and parades them around the bar."
                zan "MOXIE MOXIE MOXIE MOXIE!"
                "When they look back I give them a nod like I'm ready to turn in."
                hide teresa with dissolve
                hide jennica with dissolve
            else:
                show jennica stream neutral at stream_left
                show teresa stream happy at stream_right
                "Jennica's under the table"
                mS "Oh no..."
                "The whole bar is roaring!"
                "Zan pushes the table away and goes to hug Ovid who looks like his eyes are about to pop out."
                "I move to help Jennica"
                enS "C'mon Jenn, you're good, you're alright."
                pS "Did... Did we win?"
                enS "Sorry sweerheart we didn't."
                mS "Makers, why did you bet the ship?"
                enS "The ship? What do you take us for? Zan asked us to perform a show for the bar if we lost."
                mS "A show?"
                pS "A show! Oh scrap, you sound horrible when you sing Resa."
                enS "Still better than you."
                pS "But we must press on! *hick*"
                "I'm truly losing it."
                "Just then Zan comes over to us."
                zan "You must make good on promise."
                "Teresa helps Jennica get up and they stand on the Karousel table."
                "Zan begins to clap on beat." #The melody is "C'est a ton tour"
                "Teresa and Jennica begin to sing"
                pS "Zan is the man! Zan has a plan! Zan's got the muscles to beat any man." 
                enS "Ovid's the best! Above all the rest! With muscles inside to pass any test."
                "When they look back I give them a nod like I'm ready to turn in."
                "They continue in broken harmony" 
                hide teresa with dissolve
                hide jennica with dissolve         
                
    "I head back to Rec and MAC."
    show rec stream neutral at stream_right with dissolve
    show mac stream neutral at stream_left_mac with dissolve
    mS "I'm taking the kid, we'll check in with you tomorrow at the shop, alright?"
    recS "Sure thing Cap."
    recS "Actually Moze wait."
    "They look serious."
    mS "What's going on?"
    recS "MAC isn't a normal bot is he?"
    "I'm in no position to lie here."
    mS "No... he's not."
    recS "BigCorp has been deploying agents everywhere."
    recS "They're looking for something big"
    recS "Lots of rumors about what that could be."
    "MAC is looking at us now." 
    mS "So then you can imagine why we can't let them have him."
    hide rec with dissolve
    "Rec looks down at MAC."
    recS "He's a special kid."
    recS "We'll keep looking for that part tomorrow."
    "MAC waves to Rec as they leave. We turn in."
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
            pS "Go for option A prepare for option B. Got it."
        "Don't cause any unnecessary drama.":
            mS "We need to do everything we can to get that part but we can't be afraid to cause problems."
            enS "Play it demure until we have to push."
    enS "I'll head to the plaza, Jennica the outskirts, Moze you take MAC and do another sweep of the shops near Rec."
    mS "Perfect Resa, let's get started then. Now MAC-"
    "Fear surges through my body as I look between the three of us and MAC is nowhere to be found."
    mS "MAC!"
    "I know Teresa and Jennica are screaming for him but I can't hear them, I can't hear anything but my heart pounding in my chest."
    "Where is he?"
    "WHERE IS HE?"
    "Then I see him far in the distance, wheeling himself slowly to a group of people."
    "To a group of Hounds."
    "My feet move before my brain can register what is happening."
    "It happens so fast, MAC runs into the leader, his arms frantic."
    "They swarm him, my feet aren't moving fast enough. I can't think of anything but how fast my legs should be moving." 
    "MOVE FASTER."
    "When they take him and drive away, I don't register how a cruiser almost hit me, I don't feel the pain of my knees when they hit the ground in defeat."
    "All I can hear is Ama's voice in my head, \"You'll have the chance to prove it, just not right now.\"" ##Consider changing this line##
    hide jennica with dissolve
    hide teresa with dissolve
    jump vig3_sc8

label vig3_sc8():
    hide akarplaza_stream
    show bg black at topleft onlayer background
    "We knew we couldn't chase down the Hounds. There was nothing that could be done once MAC was out of sight."
    "It was Rec who gave us the suggestion to intercept them where they were. That meant in the belly of the beast, Reynar's Vineyard."
    "It was nothing short of the worst case scenario."
    hide bg black
    show exteriorvineyard_stream at topleft onlayer background
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    pS "You know I'm not a fancy sort of gal, but my butt looks fantastic in this."
    "Jennica has not stopped looking at herself in every reflective surface since arriving here." 
    "Not surprised that the first thing she does out of the luxury cruiser is stare at herself in the window."
    pS "Sorry Jimmy, gotta make sure the girls are in order before I do some serious ass-kicking."
    "Jimmy is a friend of Rec's who owns a luxury cruiser company and thankfully owed them a favor."
    enS "Can you give it a rest there are people around."
    pS "I thought you'd want me to look presentable?"
    mS "You need to be serious about this."
    pS "Oh I'm very serious, just my face don't look it. Y'all should consider fixin' yours."
    "I relax my shoulders as an attendant walks over to us."
    show vineyardattendnpc stream at stream_center with dissolve
    vyattend "Good afternoon, my name Ryo and it is my pleasure to welcome you to the Vineyard." 
    vyattend "Are you perhaps here for the Inventor's Fair?"
    enS "Pleased to make your acquaintance Ryo. Please check the list for Vira Prismari and retinue."
    "They raise an eyebrow before checking a screen."
    vyattend "Prismari? How wonderful, we were certain to receive another refusal gift this year."
    enS "Well we so desperately missed the inspiration of the Inventor's Fair. I hope you are well to accommodate us?"
    vyattend "I must say your posse is such a surprise it's so... pleasantly unexpected."
    "It's like watching a tennis match with a bomb for a ball."
    enS "You know we are so thankful to Reynar for his consideration every year, and so lovely to see our donations put to such good use."
    enS "You've truly spared no expense."
    vyattend "Of course, we want to celebrate all those who contribute to research and development of the Outposts."
    enS "The Prismari family is always proud to support this iconic hub of innovation."
    vyattend "We are pleased to have you Miss Prismari, right this way."
    "The attendant makes a gesture to the main ballroom and leaves us to check in other guests."
    hide vineyardattendnpc with dissolve
    pS "You're a bit scary when you're proper."
    show rec stream neutral at stream_center with dissolve
    recS "Can you kill someone by being too nice?"
    enS "I'm sure someone has."
    mS "Your sister isn't going to be mad with you using her name?"
    enS "Please. My family hasn't come to these since I was exiled. Doubtful they'll even know I was here."
    mS "I appreciate you going through this so we can get in."
    enS "Couldn't have done it without Rec getting us ready."
    recS "I've been here for years and never set foot in the Inventor's Fair. I'd give you my whole shop if ya needed."
    recS "The Inventor's Fair is even more insane looking than I could've imagined. The fanfare in Akar is a kid's birthday party by comparison." 
    "Reynar and his Vineyard have spared no expense. His finely dressed guests being served by his android wait staff." 
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
    enS "We're doomed."
    mS "Yeah..."
    hide teresa with dissolve
    jump vig3_sc9

label vig3_sc9():
    hide exteriorvineyard_stream
    show inventorfairgallery_stream at topleft onlayer background
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
            invfairnpc2 "Sometimes makes you wish BigCorps took over."
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
            "From the crowd, I hear a voice murmuring"
            invfairnpc1 "There's one every year." #using invfairnpc1 because it's just labeled as "Inventor's fair guest." works for offscreen npc.
    "I move on, scanning the gallery, I see Teresa looking in her element gliding through various groups with a natural grace. Never lingering too long."
    showgirl "It's you!"
    show showgirl stream at stream_center with dissolve
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
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    show rec stream neutral at stream_center with dissolve
    pS "Oh so we're really in it now."
    enS "Guess we didn't get much distance after all."
    recS "What happens if they catch you?"
    enS "Oh I assume chained to a factory for the rest of our natural lives."
    pS "I'd rather a bullet to the eyes."
    mS "We need to find MAC and get the hell out of here."
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
    bcrep "Ladies and Gentlemen, honorable guests of the Vineyard. We at BigCorp would like to thank Reynar for this opportunity to present a prototype for a new and exciting venture."
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
    "The room chuckles as the representative keeps talking. I look over at the crew who are frozen, unsure of how to proceed. Jennica begins to move up to me but stops and turns white as a ghost."
    amaS "Now ain't this a stroke of bad luck."
    hide mac with dissolve
    "I turn to the voice and am certain I've fully lost it." 
    "Because there she is, full ballgown staring at me with that same condescending look I've always known."
    show ama stream neutral at stream_center with dissolve
    "But this time, it doesn't go away. Ama smiles."
    amaS "Hello Mozely." 
    jump vig3_sc10 

label vig3_sc10():
    hide inventorfairgallery_stream
    show bg black at topleft onlayer background with dissolve
    "I flinch as a shot rings outs, echoing in my ears."
    "My body is buzzing, heart pounding."
    "Ama takes the blaster away from me."
    # Ext. Akar - A Decade Ago 
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
    jump vig3_sc11

label vig3_sc11():
    show inventorfairgallery_stream at topleft onlayer background with dissolve
    hide bg black
    #Int. Inventor's Fair. 
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
        "I don't have the droid you're looking for.":
            mS "I don't have it."
            amaS "Are you playing dumb with me?"
            mS "I lost it, he's not with me."
            "Ama furrows her brow."
            amaS "This isn't the time to yank my chain."
            mS "Isn't that BigCorp's job?"
        "But he's right there on the platform, no?":
            mS "Why are you asking me?"
            mS "It's right there isn't it?"
            "Ama turns to the platform then back at me, unimpressed."
            amaS "Don't quit your day job Moze."
            amaS "I want that droid and I want it now."
    "Ama stalks towards me and I know what's coming."
    "I move to my blaster hidden in my clothes."#choice here?
    "I'm sorry Resa."
    reynar "Ladies, I hope your evening is going well."
    amaS "Reynar."
    reynar "Hello Ama, a pleasure as always."
    reynar "And this must be young Moze. All grown up."
    "I relax my shoulders."
    mS "Reynar, thank you for having us this evening."
    reynar "If only you were invited..."
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
    mS "A range extender, a small repair for my ship I'd like it back."
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
    bcrep "Absolute garbage!"
    "I hear the sound of metal on the ground, a small pained whine."
    "I press down my white hot anger."
    bcrep "What did you say to him? What did you do?"
    "He's talking to Ama, who arrogantly has he back to me."
    bcrep "I swear to the Makers if you screwed up again!"
    "The representative hasn't noticed me yet."
    "And soon had more pressing matters as he strained and struggled against Ama's grip on his throat."
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
    "They laugh in dsibelief."
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
            rep "STUPID JUNK!"
            "Just as the rep attempts to land his kick, he's stopped by the sound of Ama's rifle."
            amaS "Hold it!"
            "The rep backs away."
            "The rifle turns to me."
            amaS "Blaster on the ground Mozely."
            "I wasn't even reaching for it. But I grab it from the holster in my suit jacket."
            "And toss it away from me."
    amaS "You always did play with your heart out Moze."
    "She looks to MAC."
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
        repS "Makers!" 
        "Ama just stares at MAC who is resolute in his stance."
        amaS "You gonna do something with that baby blaster?"
        amaS "If you're gonna shoot, you better shoot straight."
        macS "My programming ensures perfect accuracy. Shall I demonstrate?" 
        repS "Programming..."
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
        mS "You got it."
        "Without losing my sights on her we head inside."
    elif macViolence >= macPeace and macPessimism < macHope:
        "He fires the blaster in between us, it hits the wall with a definitive smack."
        repS "Makers!" 
        "Ama just stares at MAC who holds the gun steady but with noticeable apprehension."
        amaS "You gonna do something with that baby blaster?"
        amaS "If you're gonna shoot, you better shoot straight."
        macS "My programming ensures perfect accuracy when required." 
        repS "Programming..." 
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
        "Ama is speechless"
        "Without losing my sights on her we head inside."
    elif macViolence < macPeace and macPessimism >= macHope:
        "He fires the blaster in-between us, it hits the wall with a definitive smack."
        repS "Makers!" 
        "Ama just stares at MAC who is resolute in his stance."
        amaS "You gonna do something with that baby blaster?"
        amaS "If you're gonna shoot, you better shoot straight."
        macS "My programming... ensures perfect accuracy."
        repS "Programming..."
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
        "Without losing my sights on her we head inside."
    else:
        "He fires the blaster in-between us, it hits the wall with a definitive smack."
        repS "Makers!" 
        "Ama just stares at MAC who is resolute in his stance."
        amaS "You gonna do something with that baby blaster?"
        amaS "If you're gonna shoot, you better shoot straight."
        macS "My programming ensures perfect accuracy. But I won't need this."
        repS "Programming..."
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
        "Without losing my sights on her we head inside." 
    #elif macViolence < macPeace and macPessimism < macHope:
    # "MAC is a peaceful optimist."            
    "I remove the core from the rifle, put it in my pocket and toss the shell on the ground."
    "We break into a sprint down the hall."
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
    macS "In here!"
    "MAC stops us at a door, I can hear muffled arguing beyond it."
    "It's locked and needs a card to open."
    macS "Let me!"
    "With an efficiency that I've only ever seen from Teresa. MAC undoes the scanner and brings his hand to it as the door swings open."
    "Two blasters meet me as the door swings open."
    mS "Well don't be too happy to see me!"
    enS "Captain!"
    pS "Thought ya dead, I won't lie."
    "MAC rushed past me to grab Teresa's legs. The door closes behind me as I walk in."
    enS "Good to see you buddy."
    pS "Where's Deadeye."
    mS "Left her on the east balcony might be on our tail but didn't see where we went."
    pS "That gives us sometime."
    enS "But we have MAC and that's important."
    recS "Not just MAC."
    "They hold up the range extender laying on the counter near them."
    mS "How?"
    pS "Long story truly, did you know Zan is here?"
    mS "At the Fair? For what?"
    recS "He's one of the featured designers! A big name is biomechanical engineering."
    pS "He's some good-lookin' work."
    recS "And some good-lookin' muscles."
    mS "..."
    recS "Forget I said that."
    mS "Okay let's focus up. What's going on here."
    enS "Rec found a private comms room. We were hoping to at least catch our breath before we head out."
    pS "Can't go back through the party."
    recS "But there's still a shuttle system that can get us to Akar.Usually used by the workers and it should be a quick run here."
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
            macS "APOLOGIES!"
            "This was the third security guard MAC had run over with reckless abandon."
            "Like a little purple battering ram MAC was clearing a path through just as Reynar's security came to intercept us."
            "When we set off we didn't imagine it would be this close to the fair."
            "Dodging through the side garden to the entrance shuttles I pray that Reynar isn't too upset with our escape plan."
            pS "Jeez this kid's goin' fast and furious."
            enS "He gets it from you!"
            recS "This architecture is incredible, the bio-tech is so seemlessly integrated into the material of the wall."
            mS "REC LOOK FORWARD!"
            "In their distracted state they mindless slam into a couple going hot and heavy."
            "No doubt using the garden to avoid any possible scandal,"
            pS "Keep up y'all I'm the only one in heels and I'm leagues ahead!"
            enS "Stop showing off!"
            pS "How 'bout ya start showing up!"
            recS "How about that terrarium!"
            mS "REC!"
            "With only minor casualties, we make it to the shuttles."
            jump vig3_sc14

label vig3outlawcomms():
    smatt "Well hello ladies! Need a hand from little ole me?"
    "Matticus smiles in that shit-eating grin that he loves."
    pS "This is a terrible idea"
    "I'm starting to agree."
    mS "We're not here for pleasantries"
    recS "I almost forgot what he was like."
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
    "The comms go dead."
    macS "Skeeve."
    recS "The biggest."
    mS "Let's get out of here."
    "With relative ease we make it to the shuttles."
    jump vig3_sc14

label vig3marshalcomms():
    smatt "Well hello ladies! To what do I owe the pleasure?"
    "Matticus smiles in that shit-eating grin that he loves."
    pS "Disrespectfully, we didn't call you."
    "This is bad."
    smatt "Oh no? Were you perchance hoping I was some young redheaded datacenter intern?"
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
    "The comms go dead."
    macS "Skeeve."
    recS "The biggest."
    mS "Let's get out of here."
    "Carefully we make it to the shuttles. Not sure what awaits us on the other side. "
    jump vig3_sc14

label vig3_sc14():
    "Just beyond the entrance the shuttles are empty."
    "Reynar hasn't toasted to the crowd and people wouldn't dare to leave before his address."
    recS "This one, it'll take us right to the plaza!"
    "With quick work MAC undoes the security protocol and gets us loaded in."
    "Then I'm thrown against the wall and there's Ama, knife in hand at my throat."
    "Teresa and Jen are quick to act."
    enS "Let her go Ama!"
    pS "We'll drag your body out of here if necessary."
    amaS "Then you'll need to make room for two."
    "She presses harder against my throat."
    recS "Deadeye..."
    "Ama's eye move to Rec."
    amaS "Well well, if it isn't Reccrin."
    amaS "Right where we left him."
    recS "Screw you, you took Allistar away to go galavanting in the Outposts."
    recS "I have nothing to say to you."
    "Ama looks around expectantly."
    "A realization creeps on her face."
    amaS "Mozely, where is Allistar? Last I checked I left him with you."
    "Rec's eyes fix to me, finally catching me in my lie."
    recS "What?"
    amaS "Oh you didn't know?"
    "Guilt stains all of our faces."
    recS "Is this true."
    mS "It is..."
    recS "Well! where is he?"
    "I can't lie anymore."
    mS "He's dead Rec, I shot him."
    "Rec's eys widen, as they step back, horrified."
    recS "Why?"
    menu: 
        "Why did you shoot Allistar?"
        "I didn't want to it just happened.":
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
            "Teresa and Jennica don't turn to them, still fixed on Ama."
            "MAC clings to Teresa."
            amaS "How disappointing, he was a talented kid."
            "Ama looks to Teresa and Jennica."
            "I see Reynar's security detail bounding for us in the distance."
            "Ama takes the knife off my neck. And puts her hands in the air."
            amaS "Let's finish this later, shall we?"
            "We don't move as she backs away from us."
            "Then out of sight."
            "We don't have time to process before we head for the shuttle."
            macS "Moze?"
            mS "Yes MAC."
            macS "Will Rec be okay?"
            mS "I don't know."
            macS "Are you okay?"
            mS "I don't know."
            jump vig3_epilogue

        "I did what I had to do.":
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
            amaS "How disappointing, Allistar was a talented kid."
            "Ama looks to Teresa and Jennica."
            amaS "Let's finish this later, shall we?"
            "We don't move as she backs away from us."
            "Then out of sight."
            "We don't have time to process before we head for the shuttle."
            jump vig3_epilogue

        "I did it because he deserved it.":
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
            "Ama leans in close."
            amaS "That was cold Mozely, even for me."
            "Ama takes the knife off my neck. And puts her hands in the air."
            amaS "Let's finish this later, shall we?"
            "We don't move as she backs away from us."
            "Then out of sight."
            "We don't have time to process before we head for the shuttle."
            jump vig3_epilogue

label vig3_epilogue():
    "As the shuttle zooms to Akar, the Vineyard is alight with fireworks."
    "The screens in the shuttle spring to life."
    "Reynar is there, glass in hand toasting it to the camera."
    "And I remember what he left in my pocket."
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
    show ship_hallway_stream at topleft onlayer background with dissolve
    "As I walk down the hall, I'm once again intercepted."
    "It's MAC."
    "We stare at each other in silence."
    "I lower myself to his eye level."
    "He rolls towards me."
    "And hugs me."
    "The Oakley presses forward to Akar."
    "This is the end of the current build"
    "Going back now."
















