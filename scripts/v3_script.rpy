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
    ps "But we need to be more united on things if we're gonna make it."
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
    #show cockpit_stream at topleft onlayer background with dissolve
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
    show jennica stream happy at stream_left
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
    #show akarstreet_stream at topleft onlayer background with dissolve
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
    show jennica stream happy at stream_left
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
            "I pull up my sleeve to real my Snakehawks tattoo"
            mS "I really wouldn't do that."
    #show houndgoon stream neutral at stream_center with dissolve 
    "The two men back away and fall back, they're well built but not sharp enough for a fight like this. I give the signal to Jennica as she lets their friend scramble up before heading out."
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
    #hide akarstreet_stream with dissolve
    #show reccshop_stream at topleft onlayer background with dissolve
    "We walk into Specs and Steele the inside is a chaotic mess of equipment and gear stacked wildly against the walls."
    "Thankfully there's enough space to move with it being empty."
    mS "Hey Steele! You in?"
    pS "Hope you still have that Vira Brandy!"
    enS "From four years ago?"
    pS "It ages well!"
    macS "A delicacy from the Vineyard, Reynar's Vira Brandy, named after his late partner has a shelf life of 5 years."
    pS "See? Barely made it!"
    hide mac with dissolve
    "With MAC trailing us I scan some of the newer gear, even some weirder stuff, weird for Steele."
    "Someone comes out from the back room."
    #show rec stream neutral at stream_center 
    ###RECCRIN (Late 20s) enters from the back room. They looks like an older version of their brother Allistar, long hair, tougher build.##
    recS "Well I'll be..."
    "We can't help our silence in this moment."
    show jennica stream happy at stream_left
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
    macS "Vira Brandy is first invention using edible chimereon fruit. Which is quite odd."
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
            mS "If by top secret you mean of a random shelf, then sure, keep it hush hush though."
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
    #show rec stream neutral at stream_center with dissolve
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
            "Every weird invention and new gadget clatters to the ground. Broken parts start to litter the floor."
            menu:
                "Do I intervene?"
                "That's enough!":
                    mS "Alright that's enough!"
                "Stay quiet.":
                    "They continue to trash the shop. More carnage. They're laughing to each other tossing equipment like a hackey sac."
                    "I see one of them try to head to the back room."
    mS "Alright that's enough!"
    houndgoon "You'd be best to stay out of official business."
    "Another gangster chimes in."
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
    "The Hounds turn to us and I know they're gearing up for a fight. They probably won't kill us, but I can't imagine how banged up we'll be or what happens if they find MAC." ###The player must decide between three actions, fight, let them have it, or Bribe - IF THEY HAVEN'T BRIBED REGI###.
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
            enS "I want to blow that man up from the inside."
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
            enS "I want to blow that man up from the inside."
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
    show jennica stream happy at stream_left with dissolve
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
    show pub_stream at topleft onlayer background with dissolve
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
    show jennica stream happy at stream_left 
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
    "MAC lets out an excited noise and heads  to the bar with Rec."
    "The table is silent."
    mS "I owe you both an apology"
    "Jennica and Teresa perk their heads towards me."
    show teresa stream neutral at stream_right
    show jennica stream neutral at stream_left
    mS "I'm not going to say that I regret what we did in Gibian V, that doesn't matter now."
    mS "But I can't have the two of you blowing up at each other over something I decided."
    mS "When it comes down to it, we need to look out for each other." 
    mS "You're the ones I can rely on, the only ones I trust and I need that to be the same between all of us."
    show jennica stream happy at stream_left
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
    "Rec is telling MAC a story that has him fully engaged."
    "Teresa is in a corner watching in unwavering curiosity at the plants that line the ceiling, tossing bits of food up for them to catch."
    "Jennica is at a pool table, chatting away with some couple who stare at her in amazement."
   
    #I would want to have the stranger choice be an interruption after picking a choice with the crew. Doing it like this for simplicity. 
    menu:
        "I should check in on one of them...."
        "Check in on Teresa":
            "Teresa and I haven't had some alone time in a while. "
        "Check in on Jennica":
            "Jennica and I should talk."
        "Check in on Mac and Rec":
            "This place is probably overwhelming, I should check-in."
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
                    hide akarplaza_stream
                    show bbpub_stream at topleft onlayer background with dissolve
                "Wrestle the knife away":
                    "Placeholder dialogue here."
                    "violence ensues."
                    hide stranger 1 stream with dissolve 
                    "I return to the Broken Bulb a bit disheveled."
                    hide akarplaza_stream
                    show bbpub_stream at topleft onlayer background with dissolve
        "Chat with Teresa":
        "Chat with Jennica":
        "Check in on MAC and Rec":
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
    zan "The bet is done! Mr. Stein. The Karousel please!"
    "Bet? What bet?"
    "A small man holds up the karousel high over his head, I barely see him before it appears on the table and the door to the back room swings closed."
    hide jennica with dissolve
    hide teresa with dissolve
    hide zan with dissolve
    show mac neutral stream at stream_center_mac with dissolve
    show rec neutral stream at stream_right with dissolve 
    macS "Are they playing Brikarousel?"
    recS "Aren't you too young to know that game?"
    macS "I have a full database that allows me to know a myriad of games."
    recS "Got me there... You know I never understood this game."
    macS "Well Brikarousel was invented by Brika Alphonse approximately 30 years ago when..."
    recS "I meant why people are so eager to play."
    macS "Alcohol?"
    recS "You're learning fast."
    "I look over at the table as a pit in my stomach forms."
    mS "Bet? What did they bet?"
    recS "I didn't hear but I read lips a bit, a “sh” something?"
    mS "\"Sh\" something."
    macS "Shirt, shoes, shilling Ship? They wouldn't-"
    hide rec with dissolve
    hide mac with dissolve
    "No that's stupid."
    "Then I remember who's playing the game." 
    "Shit."
    show jennica neutral stream at stream_left with dissolve
    show teresa neutral stream at stream_right with dissolve
    show zan stream at stream_center with dissolve
    "Contrary to my belief the tough woman next to Zan is not participating instead it's a small man with dark hair and modified gray skin."
    pS "Talkin' to us about bein' small and your guy is thinner than my jacket."
    zan "Ovid is strong of heart, muscles on the inside."
    enS "That tends to be where they go yes."
    ovid "Zan must we always play this game whenever we go out?"
    "The game starts off with a bang, the rules are simple, teams of two play hands to collect played cards from a pool." 
    "Some cards are worth points, the pair with the lower amount of points at the end of the round takes a shot from the karousel."
    "The first team that withdraws or has a member drop loses."
    "By round ten, it's not looking good."
    zan "How is moxie?"
    pS "Stronger than my momma's back!"
    enS "I'm starting to feel mine in the back of my throat."
    "Teresa and Jennica look wrung out but surprisingly Zan and Ovid are sturdy despite drinking their fill."
    hide jennica with dissolve
    hide teresa with dissolve
    hide zan with dissolve
    show mac neutral stream at stream_center_mac with dissolve
    show rec neutral stream at stream_right with dissolve
    macS "They're cheating."
    recS "How did you-"
    recS "Of course! We've been out of the game too long."
    macS "We must tell someone, this is improper."
    mS "MAC I'm going to lay this out for you plainly. No one cares if something is improper here."
    macS "Then we should do something."
    mS "I'm on it."
    macS "And I'll help."
    mS "You will sit down and say nothing and let me handle it."
    macS "But I-"
    mS "Understand?"
    macS "But I'm part of this crew too Ama!"
    "That was my voice. Upset, scared of being left behind."
    mS "You are, and you'll have other chances to prove it. Just not right now."
    "When Jennica calls for a short recess I know that's my time to head over. Players can't leave the table so I go to them."
    hide rec with dissolve
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
    mS "The deck isn't right. I know a standard set when I see one."
    pS "That makes sense, the feel was off."
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
            "I see a young couple pinning each other on a pillar near the table." #bar fight choice
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
            zan "Idiot! You interrupt the Karousel!"
            "It's hand fifteen, and half the bar is up in arms, friends of the man square up with Zan's crew. It's only when tiny Mr. Stein waddles to the table and promises a free round that the room begrudgingly settles."
            hide zan with dissolve
        "Shoot the rope holding the carnivorous plants":
            "Placeholder dialogue here."
            "Plants do some stuff, problem ensues."
    #maybe fade in and out to show passage of time again?#
    "Ovid coughs loudly before putting something in his pocket, with cards scattered all over the floor the deck is replaced."
    "The karousel is untouched, the rounds continue."
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
        "Shoot the chair":
            "I can't leave it up to chance, the crowd is completely absorbed by this game. I set my pistol to stun and take my position."
            "As I scan the bar for any eyes on me, I take in just how packed this place is. It's wall to wall."
            "Then I see them, a small group near the door, half watching the game. Is that - Ama's crew? No. My vision is still betraying me and I don't have time to get a better look."
            zan "FOR MY LOYAL FANS!"
            "Zan does a messy cheers to Ovid, teeters his chair back to knock the shot into his mouth."
            "As I pull the trigger Zan's eyes meet mine. Damn."
            play audio "lazer.wav" volume 5.0
            hide zan with Dissolve (0.1)
            "Zan falls hard, the pub is silent."
            show jennica stream happy at stream_left
            show teresa stream happy at stream_right
            pS "HELL YEAH!!!"
            "The crowd erupts, Zan's crew is visibly miffed but the rest of the bar is patting Teresa and Jennica on the back."
            show zan stream at stream_center with dissolve
            "Zan gets up to accept defeat, Ovid has fully crawled under the table."
            "I look over again to where I saw Ama's crew, no one is there."
            "The door has just swung closed."
            ovid "Thank the Makers it's over."
            zan "Good, good! NOW! I must go and throw up. HAHA!"
            "The three exchange handshakes as Zan passes by me and stops."
            zan "You are Captain, no? Good shot, well played, but messy. Have more faith next time."
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
            #need a variable to determine if they win or not. 
            "Placeholder dialogue."
            "We are victorious." #if the variable determines that they win.
            show jennica stream happy at stream_left
            show teresa stream happy at stream_right
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
            #if they lose, some dialogue here explaining that they didnt actually lose the ship.
            # "Jennica and Teresa make good on their end of the deal, begin singing."
    "Turning away from the two of them, I head back to Rec and MAC."
    show rec stream neutral at stream_right with dissolve
    show mac stream neutral at stream_left_mac with dissolve
    mS "I'm taking the kid, we'll check in with you tomorrow at the shop, alright?"
    recS "Got it!"
    recS "See ya later little buddy!"
    macS "Bye bye!"
    "Reccrin goes to say their goodbyes to the rest of the crew before heading out."
    hide rec with dissolve
    mS "Ready to turn in, kid?"
    "MAC looks at me almost offended."
    macS "Yes, Captain."
    "We head upstairs and turn in for the night."
    hide mac with dissolve
    jump vig3_sc7

label vig3_sc7():
    hide bbpub_stream 
    show akarplaza_stream at topleft onlayer background with dissolve
    "The next day is hot, the hangover in my brain is smashing at my skull like it's the bars of a prison."
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    enS "We spent all day searching, and nothing?"
    pS "Well there was that one guy."
    mS "He tried to sell a walking stick he carved when we asked for a range extender."
    pS "I thought it was quite lovely."
    "MAC is silent."
    mS "Alright kid?"
    show mac stream neutral at stream_center_mac with dissolve
    macS "Yes, I hope we can find a lead soon."
    menu:
        "Conversation with MAC placeholder."
        "Placeholder dialogue 1":
            "Dialogue placeholder."
        "Placeholder dialogue 2":
            "Dialogue placeholder"
    ##Conversation with MAC?##
    hide mac with dissolve
    "Rec gave us some good starting points but after searching for hours we've notice most operations aren't running with their usual stock because of the Inventor's fair."
    mS "We might need to split up."
    enS "I agree we'll cover more ground."
    pS "Are we just looking to buy?"
    #player choice
    menu:
        "How do we want to approach getting the antenna?"
        "Whatever it takes, maybe violence.":
            mS "Do whatever it takes, we need that part and we might have to take it if necessary."
            pS "Go for option A prepare for option B. Got it."
        "Placeholder choice 2":
            "Dialogue placeholder."
    enS "I'll sweep the plaza, Jennica the outskirts, Moze you take MAC and do another sweep of the shops near Rec."
    mS "Perfect Resa, let's get started then. Now MAC-"
    "Fear surges through my body as I look between the three of us and MAC is nowhere to be found."
    mS "MAC!"
    "I know Teresa and Jennica are screaming for him to but I can't hear them, I can't hear anything but the pounding of my heart in my skull."
    "Where is he?"
    "WHERE IS HE?"
    "Then I see him far in the distance, wheeling himself slowly to a group of people."
    "Hounds."
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
    show vineyardinventorfair_stream at topleft onlayer background
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    pS "You know I'm not a fancy sort of gal, but my butt looks fantastic in this."
    "Jennica has not stopped looking at herself in every reflective surface since arriving here." 
    "Not surprised that the first thing she does out of the luxury cruiser is stare at herself in the window."
    pS "Sorry Jimmy, gotta make sure the girls are in order before I do some serious ass-kicking."
    "Jimmy is a friend of Rec's who owns a luxury cruiser company and thankfully owed them a favor."
    enS "Can you give it a rest there are people around."
    pS "I thought you'd want me to look presentable?"
    mS "You need to be serious about."
    pS "Oh I'm very serious, just my face doesn't look bugged out. Y'all should consider fixing yours."
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
    vyattend "Very thoughtful, we are pleased to have you Miss Prismari, right this way."
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
    recS "The Inventor's is even more insane looking than I could've imagined. The fanfare in Akar is a kid's birthday party by comparison." 
    "Reynar and his Vineyard have spared no expense. His finely dressed guests being served by his android wait staff." 
    "Carefully plated exotic food and drink fill the silver trays that circulate the a gallery-style showroom."
    enS "Apparently the theme is Lost Renaissance, remembering a time long past..."
    pS "That why some of these statues don't have arms?"
    "It's excess at its highest degree, it's so much that I can't imagine us finding MAC in all of this."
    recS "Reynar likes to personally assess what the Hounds find so they're probably holding MAC somewhere close by."
    pS "Let's rough up some suits and find out where they've got him."
    "Teresa turns around and stops us in our tracks."
    enS "Okay lets get this clear. We're not going to do anything of the like."
    pS "Resa-"
    enS "Listen Jenn, I appreciate how readuy are to fight for MAC. But I don't think you understand what situation we're in." 
    pS "I ain't scared of the Hounds."
    enS "The reason Reynar is using the Hounds in the first place is because all of his actual security is here. Look around." 
    "I'm almost embarrassed by how long it took me to realize. Even now with us just talking I can feel dozens of eyes on us."
    "The androids here aren't just waiting, they're scanning, searching. A step too far out of line and that's it for us."
    pS "So now what?"
    enS "Schmooze, flirt, impress, find anyway for someone to give you information but more importantly access."
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
    hide vineyardinventorfair_stream
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
            "Placeholder dialogue."
            "Better let this go."
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
    "A familiar batch of feathers block my view, Daisy stands there very much a showgirl with a bit more refinement to her outfit."
    mS "Oh hello, Daisy was it?"
    showgirl "You bet?"
    mS "50 Credits at Nova Casino."
    showgirl "What a terrible deal. That barely gets you a few good spins, not even a buy-in at a low ball table."
    mS "I guess the only big win anyone is getting is at the bar."
    "We both laugh, a genuine laugh."
    mS "I'm sorry for earlier, I've been on edge."
    showgirl "Don't sweat it, if you weren't going to shoot me I was. I hate that script."
    mS "Costume is great though."
    showgirl "You think? Why you flatter me. It is one of my favorite parts."
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
    recS "What happens if they spot you?"
    enS "Oh I assume chained to a factory for the rest of our natural lives."
    pS "I'd rather a bullet to the eyes."
    mS "We need to find MAC and get the hell out of here."
    recS "If we can trust your friend Daisy we might find whatever storeroom they put him in, hell maybe even your range extender on the way."
    mS "Makers willing. Okay, once the presentation starts then we'll head out."
    hide jennica with dissolve
    hide teresa with dissolve
    hide rec with dissolve
    "We go back to our parts and my eyes dart around the room. How many enforcers, are they all guests, maybe some waiting in the wings?"
    "Do they already have MAC and are just waiting for this presentation before heading off?"
    invfairannounce "And now a feature presentation from the Big Corp laboratories."
    "The music dies down an a platform rises from the center of the gallery. Spotlights alight on it and people halfheartedly turn to the center."
    "A finely dressed man walks up to the platform an attendant wheels in something covered by a blanket."
    bcrep "Ladies and Gentlemen, honorable guests of the Vineyard. We at Big Corp would like to thank Reynar for this opportunity to present a prototype for a new and exciting venture."
    "The crowd murmurs at the word prototype, I move closer to the corner of the room. Ready to make an escape."
    "Until the representative pulls off the sheet revealing their newest invention, a small purple robot with an unmistakable leaf over his head."
    show mac stream neutral at stream_center_mac with dissolve
    bcrep "Machine Automated Couriers or M.A.C is our revolutionary new courier bot that we are outfitting with fully adaptable AI technology."
    "His little eyes lock on mine."
    bcrep "As I said is just our prototype as we continue to look for new ways to truly develop our AI databases. But our scientists are hard at work to..."
    "This is a nightmare. A true honest to Maker nightmare."
    bcrep "Say hi M.A.C!"
    macS "Hi MAC..."
    "The room chuckles as the representative keeps talking. I look over at the crew who are frozen, unsure of how to proceed. Jennica begins to move up to me but stops and turns white as a ghost."
    amaS "Now isn't this just a stroke of bad luck."
    hide mac with dissolve
    "I turn to the voice and am certain I've fully lost it." 
    "Because there she is, full ballgown staring at me with that same condescending look I've always known."
    show ama stream neutral at stream_center with dissolve
    "But this time, it doesn't go away. Ama smiles."
    mS "Deadeye?"
    amaS "Hello Mozely." 
    "This is the end of the current build"
    "Going back now."










