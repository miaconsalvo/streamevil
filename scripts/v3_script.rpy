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
    mS "It's nice to be first one up, actually is it even morning?"
    "I check the clock on the wall, yep, morning."
    "\"I've got lots more work where that came from.\" Arrogant rat. I should've gone back and blown his fortress to ash."
    "I take an uninterested sip of my drink wrapping both hands around the glass."
    "I can't believe I'm letting this get to me. Hell I've done worse, we've done worse. This probably wouldn't even crack the top five."
    "But we're supposed to do better." 
    "That's the point of all of this isn't it?"
    "I find myself staring off into the distance." 
    "With my back to the door I don't see Teresa come in."
    show teresa stream neutral at stream_right with dissolve
    "She's in her usual clothes, her shirt is uncharacteristically wrinkled and half tucked, a button undone at the bottom."
    enS "Early start Captain?"
    mS "You know me, first one up, last one down."
    enS "That's a recipe for sleep deprivation I fear."
    "She pulls up a chair next to me grabs the warm metal pitcher from the table and fills a glass of her own."
    mS "And aren't you just the picture of a good night's sleep."
    enS "Hardly..."
    mS "Fighting with Jennica didn't tire either of you out?"
    enS "I can't speak for her, she's been camping in the cockpit since yesterday."
    mS "Luckily there isn't a bathroom in there."
    "She lets out a forced chuckle and the room goes quiet and cold for moment."
    enS "There's uh, no news on Sallent."
    "I straighten myself as best as I can."
    enS "You know, that MAC is remarkable, the database access he has, even for a BigCorp bot. I could easily get you a news bulletin from the Central Planets if you wanted."
    mS "A talented little guy for sure."
    enS "But Sallent. Nothing. Not even a distress signal. Not a single report since we left Gibian V."
    mS "Hard to ask people to risk Gray Fever for a check-in. Hell, who knows if anyone is working Comms there anymore."
    "There's a long pause."
    enS "I don't...this isn't proper to say."
    enS "I wondering if you - if we - made the right choice."
    "She's looking away from me now, she never had a problem speaking plainly before."
    enS "We did what we did to keep safe and what we're doing requires... tough choices. Such is the nature of our mission."
    mS "Resa..."
    enS "We can't always expect to feel good about what we do. It's a difficult call to make."
    mS "Please."
    enS "SHE WON'T EVEN LOOK AT ME MOZE!"
    "She slams the table and her glass spills on the ground with a clang spilling. Her breath is strained as she calms herself."
    "I set my cup down gently."
    enS "We weren't the best people before we started this, and I know you and Jennica have more history than even I know about." 
    enS "But at least we dealt with things together."
    "I don't respond. Teresa needs this."
    enS "But ever since we took that- took MAC, it's been one awful choice after another. Barely escaping every time..."
    "Teresa lets out a defeated sigh. Before I can respond Jennica's voice echoes through the speaker."
    pS "Captain! Comms comin' in, fuzzy but - I reckon it's the Dragonflies."
    "Teresa shoots up, I place hand on her shoulder."
    mS "Take ten seconds."
    "I wait until I can feel her shoulder relax and walk out and down the hall, alone."
    hide teresa with dissolve
    jump vig3_sc2

label vig3marshalstart(): 
    show shiphub_stream at topleft onlayer background with dissolve
    "The Oakley is quiet today, and this coffee feels like I'm trying to cure every sleepless night I've had for the past few days."
    mS "It's nice to be first one up, if it's even morning?"
    "I check the clock on the wall, yep, morning."
    "\"Don't worry. You'll get yours.\""
    "Annoying rat. He's lucky I didn't turn back and blow his fortress to ash."
    "I take an uninterested sip of my drink wrapping both hands around the glass."
    "I'm letting this get to me. When have I ever taken one of Sav's threats seriously?" 
    "I'm sure he wants to see *her* even less than me."
    "We're trying to be better, but what's the point if we're all arrested, if they take MAC away."
    "I find myself staring off staring off into the distance." 
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
    pS "No, but I'm the only one that can outrun Ama. We got lucky but - no offense to our saving grace - I don't like not knowing how much distance we might or might not have."
    "There's a long pause."
    pS "Every little blip on the scanner make me jump, Captain. That's until I find out it's some stoved-up space junk floatin' in from a click over."
    "She looks away from me to find the words."
    pS "I wonder...if we made the right choice. As wrong as it sounds."
    mS "Jenn..."
    pS "You're right, those people needed that aid but we gotta be okay with the tough choices ya know, be more logical, make the hard call."
    mS "Please."
    "Jennica goes quiet."
    pS "She can barely look at me Moze..."
    "Jennica smacks the glass away from her, it falls to the ground with a clang. She takes a quiet moment to calm herself." 
    "I set my cup down gently."
    pS "We're doing better, and that's all fine and good. And hell I'll stand by what I said."
    ps "But we need to be more united on things if we're gonna make it."
    "I don't respond."
    pS "I like the kid. But we've been over our heads from the start..." 
    pS "She's gonna find us, and I'm sure BigCorp isn't hung up on whether or not we're brought back in one piece."
    "Jennica lets out a defeated sigh. Teresa's voice echoes through the speaker before I can answer."
    enS "Captain! There's a transmission for us - I'm certain it's the Dragonflies."
    "Jennica shoots up, I place a hand on her shoulder."
    mS "Take ten seconds."
    "When Jennica's shoulder relaxes I walk out and down the hall, alone."
    hide jennica with dissolve
    jump vig3_sc2

label vig3_sc2():
    #show cockpit_stream at topleft onlayer background with dissolve
    "The Cockpit is a mess, Jennica has made quick work at putting some of her effects in here. MAC's been sitting patiently in the corner, he's been spending more time here than usual."
    "Teresa works to get the message on the screen while Jennica hangs back next to him."
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
    mS "We should be used to a tight schedule by now."
    "We take a moment to think."
    macS "Dad..."
    "All eyes turn to MAC, Jennica's expression softens and I watch Teresa's face rises with curiosity then fall." 
    "MAC sits innocently in his chair, eyes looking off to the expanse of open space searching for the answer to a question he doesn't know how to ask."
    mS "What's going on bud?"
    macS "I- do not know."
    pS "Well that's a first." #(multiple=2) #might break the dialogue box positions
    enS "That's remarkable." #(multiple=2) #might break the dialogue box positions
    "The two exchange a quick look before turning away, remembering that they're still fighting. I turn the focus away from MAC."
    mS "Let's consider our options, come up with a plan to get our Comms back in working order. Meet at the Bridge in an hour to debrief."
    pS "Yes Captain!" #(multiple=2) #same as before, we could also define a new character as "teresa and jennica"
    enS "Yes, Captain!" #(multiple=2) #same as before, we could also define a new character as "teresa and jennica"
    "I turn to the door and go out into the hall. I'm stopped by a tiny purple metal leaf."
    #hide cockpit_stream
    show ship_hallway_stream at topleft onlayer background with dissolve
    macS "Captain."
    show mac stream neutral at stream_center_mac with dissolve
    "I can't help but jump."
    mS "Jeez MAC, don't sneak up on me like that!"
    macS "Might I make a suggestion?"
    mS "Only if it's after a stiff drink."
    macS "Pardon me but, it's the morning..."
    mS "MAC respectfully, I don't have time for this-"
    macS "Which is precisely why I have a suggestion, see I was scanning BigCorp databases..."
    "I feel the anger twisting my face." ##Dialogue choice thatlinks to MAC's reaction here.##
    mS "MAC please tell me after all this work to keep us safe you're not poking in BigCorp's networks!"
    "MAC rolls back" ## this reaction can differ based on choices##
    macS "I just wanted to be helpful..."
    "I let out a heavy sigh."
    mS "MAC you are it's just- What's your suggestion?"
    macS "An initial search suggests a nearby planet known as Solara, specifically the city of Akar. It may be suitable for *both* of your needs." 
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
###Scene 3###
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
    mS "Yeah stick close bud, don't go running off around here."
    pS "Moze why'd ya bring us here? Fancy gettin' caught by Ama?"
    enS "It's risky even by your standards."
    mS "You both know that this is where we'll get quality upgrades for what we need."
    mS "And I figured it'd be nice to take a break while we're at it."
    pS "I think you're too nostalgic."
    enS "And eager to get arrested."
    mS "Well a BigCorp prison probably has better food than some of the places we've seen."
    macS "There doesn't seem to be many enforcers operating here. Curious."
    mS "Yeah they tried that once, didn't go so hot."
    enS "But doesn't mean there aren't some off duty grunts here."
    mS "Resa look, the Inventor's Fair is in town." 
    mS "Most of the security will be looking at the Vineyard- not here." 
    mS "Let's see if we can find some old friends, grab what we need, and maybe a drink or two..."
    pS "And a softer bed."
    enS "...A proper hot meal."
    macS "I require none of those things."
    "A small kid walks past with his parents carrying a giant cotton candy dessert. It looks like a planet being orbited by small chocolate moons." ###The candy could change based on alignment###
    macS "But I require that."
    "As MAC start to wheel towards the treat Jennica thankfully picks him up."
    pS "Alright buddy we'll see what we can do."
    show mac stream neutral at stream_left with move
    "I almost didn't see the guy as he pushes past Teresa, getting a bit too close for comfort..." ##HOUND LEADER (early forties)##
    enS "Hey! Care to watch yourself?"
    #show houndleader stream neutral at stream_center with dissolve
    houndleaderunknown "Aw, smile a bit sweetcheeks, it's a celebration!"
    "Before anyone can respond, Jennica punches the man in the face. He falls down hard she puts her boot on his throat, Teresa leans over grinning." 
    #hide houndleader with dissolve
    "I can feel MAC on my leg as he hides behind me."
    enS "How's this, sweetcheeks?"
    "I can hear footsteps rushing to us. He's not alone. I pull my gun in the direction of the sound."
    #show houndgoon stream neutral at stream_center with dissolve 
    "The two 'tough' guys back away."
    mS "Not likely boys."
    "The two men fall back, well built but not sharp enough for a fight like this. I give the signal to Jennica as she lets their friend scramble up before heading out."
    #hide houndgoon with dissolve
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
    hide mac with dissolve
    "With MAC trailing us I scan some of the newer gear, even some weirder stuff, weird for Steele."
    "Someone comes out from the back room."
    #show rec stream neutral at stream_center 
    ###RECCRIN (Late 20s) enters from the back room. They looks like an older version of their brother Allistar, long hair, tougher build.##
    recS "Well I'll be..."
    "We can't help our silence in this moment."
    pS "REC!"
    "Jennica runs up to hug Rec, they embrace and Jen lifts them off the ground. Teresa goes to join in."
    enS "It's wonderful to see you kid."
    recS "Not much of a kid anymore."
    mS "I'll say."
    "I walk over slower than I should and go for a hug."
    mS "What happened to Steele?"
    recS "Old man passed two years back, so I took over."
    mS "I know he was up in years but to think."
    pS "What happened?"
    recS "Nothing, just age, the years caught up to him."
    enS "A shame. Good man."
    pS "I was really lookin' forward to sharin' that brandy."
    recS "Well you're in luck."
    pS "Hell yeah!"
    show mac stream neutral at stream_left with dissolve
    macS "It's still the afternoon..."
    "As Rec turns to get the brandy they pause to look down to see MAC."
    recS "And who's this little guy?"
    macS "I'm MAC!"
    recS "I bet you are!"
    "Rec's eyes grow wide, it's the same look Allistar gave him when they first met."
    recS "And where did they pick you up from?"
    macS "From a top secret research facility in BigCorp headquarters."
    "If I could die right now I would. Reccrin just starts at MAC blinking rapidly."
    recS "... What?"
    #mS (Multiple Response options about how to lie)
    mS "Just a courier bot we found and outfitted figured we could use an extra hand and a morale boost..."
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
    mS "Definitely a range extender."
    enS "Honestly even the base parts could use an upgrade. If you have some to spare."
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
    mS "MAC I'll be honest, I'm not being fair. But we need their help and that's a conversation for after."
    "Reccrin comes out after a brief moment with a long antennae and some internal parts for our Comms."
    show mac stream neutral at stream_left with move
    #show rec stream neutral at stream_center with dissolve
    recS "Definitely an older model but she should still work fine. Need an install?"
    enS "I could use the hand."
    pS "Thanks Rec."
    mS "It's very appreciated."
    recS "No worries! Hey since y'all have been on the move, you wouldn't have happened by Al at all?" 
    recS "I haven't heard from him in while."
    "There's too long of a pause that I can't think of something fast enough to end. But thankfully I didn't have to as the shop door swings open."
    hide mac with dissolve
    hide jennica with dissolve
    #show houndleader at stream left with dissolve
    "A group of five enter the shop, dark uniforms with a wolf patched on their right shoulder." 
    "I know some of these guys, they're ones who gave Resa a hard time." ##The Hound Leader##
    houndleader "Alright Reccrin, you know the drill! Mandatory sweep!"
    houndleader "Don't cause any-oh!"
    enS "You must be joking."
    houndleader "Sweetcheeks."
    enS "Bite me."
    houndleader "Maybe later, I'm on the clock now."
    hide teresa with dissolve
    mS "Didn't know Akar hired rent-a-cops."
    #show houndgoon at stream_right with dissolve
    "A smaller one moves up next to the big guy, she's the next toughest and looks like she has something to prove."
    houndgoon "I suggest you get yourself and your crew in order and stay out of the way."
    "Rec looks at me with a forced smile."
    recS "Please Moze."
    recS "Hounds! We don't want any trouble, just do what you need to do."
    houndleader "That's what I like about you Rec, so reasonable."
    "We stand back as the group rummages through the store, knocking over shelves and taking random items." 
    "They're armed to the teeth and now I understand why Rec is so quick to comply."
    ###Describe the wreck this group is leaving and give the players two opportunities to intervene or continue to comply silently.###
    mS "Alright that's enough!"
    houndgoon "You'd be best to stay out of official business."
    "Another gangster chimes in."
    houndgoon "We're under order to collect contraband."
    mS "Contraband? And what classifies as contraband?"
    houndgoon "Whatever we say."
    houndleader "We'll also be taking this."
    "The Hound's leader goes to pick up the antennae for the Coms that's sitting on Rec's store counter." 
    ###Streamer reaction: Of course he does###
    recS "This is item is being sold to customers at the moment. I can assure you it's perfectly legitimate."
    houndleader "Are you admitting to selling contraband Reccrin? That's cause for reprimand."
    mS "That so called \"contraband\" is mine. And they said it's perfectly legit."
    "I slowly walk up to the counter moving to get into his face."
    mS "So I'd like it back now."
    "The Hounds turn to us and I know they're gearing up for a fight. They probably won't kill us, but I can't imagine how banged up we'll be or what happens if they find MAC." ###The player must decide between three actions, fight, let them have it, or Bribe - IF THEY HAVEN'T BRIBED REGI###.
    "(Fight) I get into his face - let him pry my gear from my cold dead hands. He smiles and throws the first punch before I can react." 
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

label vig3_sc5():
    hide reccshop_stream
    show akarplaza_stream at topleft onlayer background with dissolve 
    "When Rec leads us to the plaza I'm almost startstruck with how it looks." ###REC takes the Oakley Crew to the Plaza. In front is Rec and MOZE with JENNICA and TERESA taking up the rear with MAC in between them.##
    "The space is abundant with life. The shops and bars on the outer ring of the roundabout shine with bright flashing lights and are bursting with patrons." 
    "Music and reverie pour out like sections of a cacophonous orchestra."
    "At the center is a park area that sits a large statue of a man sitting at a tree, staring at an apple in his hand." 
    "The tree has a massive hole blown out of it."
    show rec stream neutral at stream_center with dissolve
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
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
    enS "LEGENDS!! LONG LIVE THE OAKLEY!!!"
    "Teresa sticks something to the statue and leaps off."
    enS "Hehe catch me!"
    "I'm barely able to catch her in time."
    mS "I got ya!"
    "I carry Teresa in my arms as Jennica trails quickly behind just as the bomb detonates and blows the statue sky high."
    enS "It was an insane idea."
    mS "I'd bet money this place hasn't seen a bigger stunt than that."
    amaS "...You bet?"
    "I jump and turn to the direction of the voice, this time I make it to my gun."
    "When I come to I realize I've scared the young showgirl behind me near to death."
    mS "What?"
    "She stares wide eyed and is taken her off script."
    showgirl "Uh um, name's Daisy, do you bet?"
    mS "Do I bet if your name is Daisy?"
    showgirl "Well if you did you'd be a winner, and you can win bigger at NOVA CASINO!"
    showgirl "First 50 Credits are on us!"
    "She attempts to hand me a casino card, it's holographic with an animation of a supernova and 50 credits in big lettering."
    mS "Thanks but no thanks."
    showgirl "Well, have a nice day!"
    "Daisy hurriedly leaves adn heads to another group to perform the same spiel. I see her carefully get their attention this time."
    pS "Alright alright, what's this about?"
    macS "You've been anxious all day Captain."
    mS "I'm fine."
    enS "You just yelled at girl wearing feathers, I beg to differ."
    mS "I'm tired is all."
    recS "You know most of the shops are closing for the day. Let's set you up somewhere for the night."
    recS "I think the Broken Bulb has a deal on pints."
    "We begin to move out. Jennica begins a story involving a lamp, three chickens, and a guitar. MAC is confused but enthralled."
    "I can't help but look back at Daisy with the small rough-looking crew. Her eyes fixate on the only person whose back is turned to me."
    "They're tall and well built with a wide brimmed hat, in all dark leather, and long black familiar hair."
    macS "Are you coming Captain?"
    mS "Sure thing kid."




