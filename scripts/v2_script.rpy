label vignette2Start():
    #We want to reset these before the start of the vignette
    $ vignette1 = False
    $ vignette2 = True
    $ vignette3 = False
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
    $ flinchView = False
    $ flinch_viewcountCheck = False
    $ flinch_topfanCheck = False
    $ flinch_audienceCheck = False
    $ blueitView = False
    $ loopdView = False
    $ screenComplete = False
    $ macroChoice = False
    $ viewershipHigh = True
    $ viewershipMed = False
    $ viewershipLow = False
    #We now use the "scene" function to show the streamview
    #This makes it constantly viewable without being affected by transitions between labels
    #show streamview
    "It's been one week since you last streamed {i}Oakley 2{/i}."
    "Episode 2 just dropped so it's time to get back into it."
    scene streamview with dissolve
    show screen streamDetails
    show screen streamChat
    "You begin the stream and then boot up the game."
    $ reactTarget = "vig2_sc1_openingstream"
    show screen streamerCommentary
    "You load the save file you were previously playing, and are ready to go."
    jump vig2Start

###SCENE 1###
label vig2Start(): 
    show ship_hallway_stream at topleft onlayer background with dissolve
    #scene ship_hallway_stream at topleft with dissolve -- These two lines of code were the previous way of displaying backgrounds
    #show streamview at center onlayer master -- now we just need the line of code above them since streamview is always visible
    #BUT we need to hide these backgrounds whenever the scene transitions
    #$ macroNarration = False
    $ narrator = alt_narrator
    #$ chatter_list.append(vig2_sc1_comment1) - Old way of writing the addition of stream comments (IGNORE)
    $ viewCount += 3
    play audio "shipAlarmShort.wav"
    "The \"Approaching Planet\" alarm jolts me out of bed."
    hide screen streamerCommentary
    $ AddChatter(vig2_sc1_comment1)
    pause 1.0
    $ AddChatter(vig2_sc1_comment2)
    shipcom "Alert! Approaching Planet Gibian V. All hands on deck."
    mS "Ugh..."
    "I'd be annoyed if I was actually sleeping."
    "I haven't been able to get any real sleep since Allistar forced my hand."
    "What did he think I was gonna do? Just let him go?"
    $ vig2_sc1_comment2.click = False
    $ reactTarget = "vig2_sc1_mentionallistar"
    show screen streamerCommentary
    play audio "shipAlarmShort.wav"
    shipcom "Alert! Approaching planet Gibian V. All hands on deck."
    "Right. Maybe it's a blessing that I don't have so much time to reflect."
    $ viewCheck1 = viewCount
    $ AddChatter(vig2_sc1_comment3)
    hide screen streamerCommentary
    "Better get down there."

    jump Vig2BridgeScene

label Vig2BridgeScene():
    show shiphub_stream at topleft onlayer background with dissolve
    hide ship_hallway_stream
    show jennica stream neutral at stream_left with Dissolve(0.5)
    show teresa stream neutral at stream_right with Dissolve(0.5)
    show mac stream neutral at stream_center_mac with Dissolve(0.5)
    #repeat for additional characters
    play music "soundtrack/vig1scratchtrack.wav" volume 0.7 loop fadein 1.0
    "As I step onto the bridge, Jennica, Teresa and Mac are discussing the visualization on the ship's computer."
    $ AddChatter(vig2_sc1_comment4)
    enS "Oh swell, Gibian V, another backwater frontier planet."
    "A backwater with a certain old associate running it."
    $ viewCount += 3
    mS "We ready to land?"
    $ AddChatter(vig2_sc1_comment5)
    show jennica stream crossed at stream_left
    pS "Can I reiterate again that this is a bad idea?"
    show teresa stream upset
    "Teresa rolls her eyes."
    $ AddChatter(vig2_sc1_comment6)
    enS "Must we go through this again?"
    $ AddChatter(vig2_sc1_comment7)
    pS "Look, I know we need to cover our trail from Ama."
    enS "An astute observation—"
    $ AddChatter(vig2_sc1_comment8)
    pS "But is Matticus really the one we want to do it? Guy was a damn skeeve when we last knew him."
    play audio "macPing.wav" volume 1.5
    macS "Skeeve. Noun. An immoral or repulsive person."
    pS "Got that right."
    enS "Fancy telling us what other options we have? Shall we go down the list of who else is ready and willing to help us?"
    $ AddChatter(vig2_sc1_comment9)
    show jennica stream angry
    pS "Look here, I just think—"
    show teresa stream neutral
    enS "Pardon me Jen, why don't I pull a \"forger with a heart of gold and access to BigCorp databases\" out of my purse and we'll be set!"
    pS "Doesn't mean we should trust Matticus, some wannabe godfather of a one-horse po-dunk planet!"
    play audio "macPing.wav" volume 1.5
    macS "Po-dunk, adjective, slang word amongst inhabitants of Kohle, denoting of a less than adequate status."
    $ AddChatter(vig2_sc1_comment10)
    "Jennica's not wrong. Matticus was always particularly unscrupulous, even amongst the Snakehawks."
    "But Teresa's also got a point, we aren't exactly spoiled for choice."
    $ AddChatter(vig2_sc1_comment11)
    enS "I say better the devil we know."
    menu: #minorchoice1
        enS "I say better the devil we know."
        "We don't have a choice.":
            show teresa stream happy at stream_right      
            mS "I understand the concern. But we don't really have another option."
            mS "We don't have to trust him, I certainly don't."
            mS "But we can't afford to be picky with our contacts."
        "We can trust his selfishness.":
            show teresa stream happy at stream_right      
            mS "We don't need to trust him, per se..."
            mS "We just need to trust his greed and selfishness."
            mS "Have you ever known Matticus to turn down something that benefits him?"
    "A look of begrudging acceptance flashes across Jennica's face."
    $ reactTarget = "vig2_sc1_matticusjennicaopinion"
    show screen streamerCommentary
    macS "Po-dunk..."
    mS "..."
    $ AddChatter(vig2_sc1_comment12)
    pS "Ok. So what's the plan?"
    hide screen streamerCommentary
    "Teresa inputs a set of coordinates into the ship computer."
    show teresa stream neutral at stream_right
    show jennica stream neutral at stream_left
    $ AddChatter(vig2_sc1_comment13)
    $ viewCount += 1
    "The visualization zooms in on the capital of Gibian V, Montserrat."
    "A map of the city appears on the computer, along with images of the spaceport, customs depot, and Matticus's compound."
    enS "One benefit of Gibian V being such a middle-of-nowhere planet is that finding Matticus will be easy."
    enS "He's became the magistrate and BigCorp security rep for this sector, has been for several years."
    pS "Never really been one for subtle life."
    "The visualization zooms in on images of Matticus's compound."
    "It's enormous, by far the largest building in town, complete with ostentatious fences emblazoned with his initials."
    enS "Case in point."
    pS "Charming."
    macS "Who is this \"Skeeve?\""
    enS "Savlian Matticus. Formerly of the Snakehawks and quite proficient in tampering with databases and security protocols."
    pS "He certainly landed on his feet since we disbanded. I'd thought he'd break a knee on the way down."
    enS "Remarkably successful for a magistrate of a tiny frontier planet."
    macS "He is abusing his authority and stealing from people?"
    $ vig2_sc1_comment13.click = False
    menu: #minorchoice2
        macS "He is abusing his authority and stealing from people?"
        "Yeah he's a scumbag.":
            $ macHope += 1
            mS "Yeah. He always did have a... {i}flexible{/i} moral compass."
            pS "So flexible it's like water. Fills any container."
            mS "I wouldn't be surprised if this isn't even his main palace."
            pS "Bet he's gotta a ranch or somethin' on the other side of the planet."
            enS "You think someone who has the money to spend on a ranch would buy one on Gibian V?"
            "Jennica looks puzzled for a moment."
            pS "Fair 'nough."
        "At least we know him.":
            $ macPessimism += 1
            mS "He's a skeeve, but he's our skeeve."
            mS "He's just trying to survive."
            pS "Mighty successful surviving he's doing."
            mS "Probably part of the deal. He needs to flaunt his wealth or his underlings might get ideas."
            enS "True. If they see weakness they might try to usurp him. I'm sure it wouldn't take much."
            pS "Of course. He's stealing and profiting so nobly."
            "Jennica rolls her eyes."
    pS "Alright, now what's the deal with the customs depot?"
    enS "Typical for a small planet. Standard issue scanners from half a decade ago."
    enS "Shouldn't be too much of a problem to fool them."
    mS "What about Ama? Think she might have eyes there?"
    enS "On Gibian V?"
    mS "Point taken. What about MAC? Do you think they might be on the lookout for him?"
    mS "They did put out an APB."
    enS "I doubt it. Takes a while for those bulletins to make it out here."
    enS "If they even do."
    play audio "macHappy.wav" volume 1.5
    show mac stream happy at stream_center_mac
    macS "Po-dunk!"
    enS "Precisely."
    pS "All the same, we needa take him along."
    show mac stream neutral at stream_center_mac
    pS "Can't risk 'em finding him here in a surprise scan of the ship while we're gone."
    $ AddChatter(vig2_sc1_comment14)
    mS "That'll have to be good enough. Are we all good to go?"
    "Teresa nods. Jennica looks vexed, but eventually nods as well." 
    mS "Let's get moving."
    pS "Aye aye."
    "Jennica begins the ship's descent to the spaceport."
    #Now that we've defined the streamview as the background, we have to manually hide characters before we transition between labels
    #If we don't want them to immediately be on screen in the next scene.
    #There are useful aspects of this - see the transition into the Marshal or Outlaw routes out of the Customs Depot for example
    $ viewCheck2 += viewCount
    stop music fadeout 4.0
    hide mac with Dissolve(0.5)
    hide teresa with Dissolve(0.5)
    hide jennica with Dissolve(0.5)
    hide shiphub_stream with dissolve

    jump GibianVCustomsDepot

###SCENE 2###
label GibianVCustomsDepot(): 
    show vig2_depot_stream at topleft onlayer background with Dissolve(2.0)
    play music "soundtrack/gibianV.wav" volume 0.8 loop fadein 2.0
    play backAudio "bgcrowd.wav" volume 0.4 loop fadein 0.5
    "The tiny barebones customs depot seems like it's on the verge of bursting."
    "There are barely a dozen agents staffing the whole building."
    "New arrivals pile in hurriedly, while departures crowd at the checkpoint leading to the spaceport."
    $ reactTarget = "vig2_sc2_landingongibian"
    show screen streamerCommentary
    show teresa stream neutral at stream_right with dissolve
    "Teresa sighs as we arrive at the main depot."
    enS "I hate customs."
    $ AddChatter(vig2_sc2_comment1)
    "Teresa's eyes dart around the depot facilities."
    show jennica stream neutral at stream_left with dissolve
    hide screen streamerCommentary
    pS "Well getting a permit to fly our ship 'round here would attract a lot more attention."
    pS "And would require an inspection of all cargo."
    $ reactTarget = "vig2_sc2_whywedidntfly"
    show screen streamerCommentary ###I would cut this one. It feels like too many right in a row
    "Jennica gestures to the small crate holding MAC."
    $ viewCount += 2
    pS "Which is a nonstarter."
    hide screen streamerCommentary
    "Teresa rolls her eyes as we get in the line marked \"New Arrivals.\""
    $ AddChatter(vig2_sc2_comment2)
    show teresa stream shock at stream_right
    "Those same eyes grow wide and panicked."
    enS "Shit! We have a problem."
    mS "I knew this was too easy. What is it?"
    $ reactTarget = "vig2_sc2_firstproblem"
    show screen streamerCommentary
    "Teresa gestures toward a customs official, scanning cargo crates."
    enS "That's a BigCorp scanner. I imagine it'll be able to detect their stolen property."
    show jennica stream crossed
    pS "So APB's do make it out here..."
    show teresa stream neutral
    enS "Something to say, Brown?"
    mS "We don't have the time!"
    show jennica stream neutral
    mS "We need a plan to get through without them finding MAC."
    hide screen streamerCommentary
    enS "Agreed."
    play audio "bagSearch.wav" volume 5.0
    "Teresa pulls out a metal sphere with numerous access ports."
    enS "I could whip up a diversion with this if you buy me a little time."
    $ AddChatter(vig2_sc2_comment3)
    show jennica stream shock at stream_left
    pS "One of {i}your{/i} diversions? Here?"
    #"Jennica appears irritated by this idea." - Cut this, unnecessary
    pS "With all these people? It's gonna cause a panic!"
    $ AddChatter(vig2_sc2_comment4)
    enS "Care to enlighten us with a better plan?"
    show jennica stream neutral at stream_left
    pS "Yeah. We may be overthinking this."
    $ AddChatter(vig2_sc2_comment5)
    pS "These customs guys ain't exactly flush with cash, especially since they're working for good ol' Matticus."
    $ AddChatter(vig2_sc2_comment6)
    pS "A little grease in the right palm'll do the trick."
    "Teresa scoffs."
    enS "Sure, unless one of them happens to have ambitions of a promotion?"
    enS "An employee-of-the-month type will report us to BigCorp in a heartbeat!"
    $ AddChatter(vig2_sc2_comment7)
    pS "As opposed to causing a stampede?"
    pS "Whole bunch of injured innocent bystanders aint't exactly clandestine."
    "The crew looks to me."
    enS "It's your call captain. What say you?"
    "Jennica has a point. There's a ton of innocent people here, it's very likely someone will get hurt if we cause a panic."
    "Teresa's point is just as valid, if one of these officials reports us to BigCorp then we might be looking at the inside of a jail cell quick."
    "MAC is quiet, but I can feel him toss delicately around in the crate."
    $ viewCheck3 += viewCount
    menu: #decision2
        "Should Teresa prepare a distraction or will you look for an official to bribe?"
        "Have Teresa prep the distraction.":
            $ customsStampede = True
            $ outlaw += 2
            $ pdEngagement += 2
            $ kcEngagement += 1
            $ engineerApproval += 1
            $ macViolence += 2
            #$ customsDistraction = True
            jump GibianVCustomsOutlaw
        "Follow Jennica and bribe a guard.":
            $ customsStampede = False
            $ macPeace += 2
            $ marshal += 2
            $ pdEngagement -= 1
            $ csEngagement += 1
            $ kcEngagement -= 1
            $ pilotApproval += 1
            #$ customsDistraction = False
            jump GibianVCustomsMarshal

label GibianVCustomsMarshal():
    #show teresa stream neutral at stream_right with dissolve
    #show jennica stream neutral at stream_left with dissolve
    #Now that we're not changing scenes between labels, we also don't need to show characters at the beginning of every label
    $ reactTarget = "vig2_sc2_customsdecision"
    "Jennica's right. A diversion could hurt a lot of people."
    "And it could definitely attract the wrong attention."
    $ AddChatter(vig2_sc2_mar_comment1)
    mS "We can't cause a panic here. We're going with Jennica's plan."
    show screen streamerCommentary
    "Teresa reluctantly puts away her device."
    $ AddChatter(vig2_sc2_mar_comment2)
    enS "Fine. I just hope we don't regret this."
    pS "Good. Let's find an agent who looks like they could use a break."
    mS "Right, let's do a quick scout."
    $ AddChatter(vig2_sc2_mar_comment3)
    hide screen streamerCommentary
    "There's a few different agents spread across the depot."
    "Most look pretty... ordinary."
    "Teresa gestures towards a younger looking agent with glasses."
    "His uniform is spotless, perfectly tucked and pleated with meticulous precision."
    enS "That one looks pretty eager, definitely not him." 
    $ vig2_sc2_mar_comment3.click = False
    "Jennica zeroes in on an agent at the \"Hazardous Luggage\" counter, subtly gesturing to me to look at him."
    "His uniform is wrinkled, shirt half tucked in a rushed panic."
    "The man looks deflated, with dark bags under his eyes."
    $ AddChatter(vig2_sc2_mar_comment4)
    "He looks like he may collapse at any moment."
    pS "That's our mark."
    mS "Good find. He looks like the dictionary page for \"disheartened.\""
    $ AddChatter(vig2_sc2_mar_comment5)
    "Jennica chuckles."
    hide jennica with Dissolve(0.4)
    "Teresa nods to us. Let's do this."
    hide teresa with Dissolve(0.4)
    show customs agent at stream_center with Dissolve(0.6)
    menu: #minorchoice3
        "Smile and look him in the eyes.":
            "As I approach the customs officer, his eyes perk up."
            $ AddChatter(vig2_sc2_mar_comment6)
            agent1 "Hello Ma'am. How might I assist you today?"
            $ AddChatter(vig2_sc2_mar_comment7)
            menu: #minorchoice3a
                agent1 "Hello Ma'am. How might I assist you today?"
                "You're such a hard worker!":
                    mS "You strike me as a hard worker sir." 
                    agent1 "Excuse me?"
                    "He seems a little confused."
                    mS "It seems like this whole place is propped up by you eh?"
                    "His eyes relax as he begins to get what I'm saying."
                    agent1 "You don't know the half of it." 
                    agent1 "I've been working back to back shifts this whole week!" 
                    mS "Really!? That doesn't sit right with me."
                    mS "Not one bit."
                "You look overworked.":
                    mS "Man, they really have you guys stretched thin eh?"
                    agent1 "Excuse me?"
                    "He's a little confused."
                    mS "You guys are so understaffed, this is ridiculous!"
                    mS "How can they expect you to work like this!?"
                    "He seems to be getting what I'm saying"
                    agent1 "Yeah it's bogus."
                    agent1 "Night shift quit on us so now I'm stuck picking up the slack."
                    mS "Yeah that {b}is{/b} bogus."
                    mS "A guy like you deserves a bonus."
        "Ring the bell.":
            "I ring the bell on his desk."
            play audio "ding.wav" volume 8.0
            "He's instantly jolted out of his stupor, looking bewildered."
            "In his panic, I notice a wedding band on his ring finger."
            agent1 "{i}Gaah!{/i}"
            mS "Sorry bout that!"
            "His face begins to relax."
            $ AddChatter(vig2_sc2_mar_comment6)
            agent1 "No it's my fault. How can I assist you today?"
            $ AddChatter(vig2_sc2_mar_comment7)
            menu: #minorchoice3b
                agent1 "No it's my fault. How can I assist you today?"
                "How long has this shift been?":
                    mS "Man, you look exhausted."
                    agent1 "Excuse me?"
                    "He's a little confused. And annoyed."
                    mS "How many hours have they got you working this shift?"
                    agent1 "Ugh. Like 16?"
                    agent1 "Nightshift quit the other day, I have to pick up his hours until we can find someone new."
                    mS "No overtime I assume?"
                    agent1 "Overtime? Never heard of her."
                    mS "Really!? That doesn't sit right with me."
                    "His eyes relax as he finally understands what I'm saying"
                "You got kids?":
                    mS "You got kids?"
                    agent1 "Excuse me?"
                    "He's confused, and a little annoyed."
                    mS "Sorry I just noticed your ring."
                    agent1 "Oh. Sorry, yeah got a daughter. She's 4."
                    "He pulls out a picture and shows me."
                    mS "Cute!"
                    "He smiles."
                    agent1 "Yeah, she's my world."
                    mS "She deserves nice things eh?"
                    "He's still a little confused."
                    mS "Especially from such a hard working dad!"
                    "His eyes relax as he finally clues in."
    "A smirk begins to spread across his face."
    agent1 "I do appreciate that."
    mS "I wouldn't be able to sleep if I didn't make it right."
    "I extend my hand to shake his, slipping him a 100 credit note."
    mS "If you're feeling keen, mind helping my friends and I get through? We're in a hurry."
    "He quickly slips it into his pocket before looking around the depot at his fellow employees."
    $ AddChatter(vig2_sc2_mar_comment8)
    agent1 "Wait by the breakroom for me."
    "I see his eyes are pointing at the staff breakroom on the other side of the depot."
    agent1 "Five minutes."
    "All of a sudden, he raises his voice to be easily audible by nearby bystanders and co-workers."
    agent1 "I'm terribly sorry but I can't help you Ma'am, you need to enter customs regularly."
    "He motions for me to move on."
    hide customs agent with dissolve
    show jennica stream neutral at stream_left with Dissolve(0.5)
    show teresa stream neutral at stream_right with Dissolve(0.5)
    "I signal the direction of the breakroom to Teresa and Jennica as I begin strolling towards it."
    "Teresa looks worried."
    "A minute passes."
    $ AddChatter(vig2_sc2_mar_comment9)
    "And another."
    "Three minutes." 
    enS "You sure he's not ratting us out?"
    "Teresa's head whips around to face Jennica."
    enS "I swear, if I have to break us out of the Gibian V penitentiary..."
    "A muffled voice perks up from the crate."
    play audio "macPing.wav" volume 2.0
    macS "Penitentiary. Noun. A place for imprisoning crim—"
    enS "SHUSH!"
    "The door creaks ajar."
    show customs agent at stream_center with Dissolve(0.2)
    "The customs official peeks his head through the door."
    agent1 "Quick. Stay close."
    "We don't need to be told twice."
    $ AddChatter(vig2_sc2_mar_comment10)
    "The agent whisks us from room to room, out from one backdoor to another."
    stop backAudio fadeout 15.0
    "Soon we're outside, next to the trash dump for the depot."
    pause 1.0
    "We're out."
    agent1 "Right so..."
    agent1 "Y'all strike me as the types to not need reminding that we never met."
    #show jennica stream happy at stream_left
    pS "Sorry who're you again? Can't seem to recall."
    "The agent wordlessly tips his hat before disappearing through the door."
    hide customs agent with Dissolve (0.4)
    show teresa stream think at stream_right
    pS "Simple as it gets! Right sweetheart?"
    enS "Yes. Almost too much so..."
    #stop music fadeout 2.0
    $ viewCheck4 += viewCount
    hide teresa with Dissolve(0.5)
    hide jennica with Dissolve(0.5)

    jump matticusDoor

label GibianVCustomsOutlaw():
    $ AddChatter(vig2_sc2_out_comment1)
    show teresa stream happy at stream_right
    show jennica stream crossed at stream_left
    "Teresa's right. We can't afford a goody-two-shoes ratting us out."
    "We can't trust the officials here. We'll have to get through our own way."
    mS "Bribing's too risky. We're going with Teresa's plan."
    $ reactTarget = "vig2_sc2_customsdecision"
    show screen streamerCommentary
    "Jennica sighs."
    pS "Alright, but let's make it quick. I don't want too many people to get hurt."
    enS "Hurt? Please! This will be by far the most exciting thing to happen here in years!"
    mS "Maybe let's keep the excitement to a minimum?"
    hide screen streamerCommentary
    $ AddChatter(vig2_sc2_out_comment2)
    show jennica stream neutral at stream_left
    "Teresa rolls her eyes at me."
    show teresa stream neutral at stream_right
    enS "I kid, of course. Anyhow..."
    "Teresa begins surveying the depot."
    $ AddChatter(vig2_sc2_out_comment3)
    enS "Right. So, Jennica will slip this device into the customs declaration box."
    enS "Once she is clear, I will activate it."
    enS "Then we make a break for the exit as soon as the second phase begins."
    mS "What's the second phase?"
    $ AddChatter(vig2_sc2_out_comment4)
    enS "I'm glad you ask! It is the {i}conflagrant{/i} phase."
    "A muffled voice perks up from the crate."
    play audio "macPing.wav" volume 1.5
    macS "Conflagrant. Adjective. Burning or bl-."
    enS "SHUSH!"
    $ AddChatter(vig2_sc2_out_comment5)
    show jennica stream shock at stream_left
    pS "Conflagrant? You lost your damn mind!?"
    mS "We're trying {i}not{/i} to attract attention Teresa."
    enS "Fires happen in these depots all the time! It's par for the course."
    enS "They'll blame it on some farmer's cigar catching on some fertilizer or something of the sort."
    show jennica stream neutral at stream_left
    mS "Just keep it under control."
    show teresa stream happy at stream_right
    "Teresa smirks slyly."
    enS "Of course, Captain, I always do."
    "Teresa pulls several parts from her bag and begins plugging them into her device."
    $ vig2_sc2_out_comment5.click = False
    show teresa stream neutral at stream_right
    #$ AddChatter(vig2_sc2_out_comment6)
    enS "Now, just a liiiiittle tweak to the capacitors, and that should do the trick!"
    enS "There!"
    $ AddChatter(vig2_sc2_out_comment7)
    show jennica stream shock
    "A spark flies off of the device as Teresa hands it to Jennica."
    pS "Sure this is safe? Looks like it's gonna turn my face into ash."
    show teresa stream happy
    enS "As safe as one of your daring escape maneuvers at the very least."
    show jennica stream neutral
    "Jennica chuckles."
    pS "Fair 'nough."
    $ AddChatter(vig2_sc2_out_comment8)
    mS "We ready?"
    show teresa stream neutral
    #show jennica stream neutral at stream_left
    "Jennica and Teresa nod to me."
    "Teresa and I head towards the customs declarations line."
    "Jennica carefully walks by the customs declaration box and slips the device inside."
    "As soon as Jennica begins making her way back to us, Teresa presses a button on her wrist computer."
    enS "Let's show these rubes a good time."
    # music should get more exciting here?
    "A thin plume of white smoke begins to emanate from the box."
    "As the smoke grows thicker, security officials approach the box to investigate."
    $ AddChatter(vig2_sc2_out_comment9)
    "A commotion begins to spread across the depot as more and more of the crowd notices the smoke."
    $ renpy.music.set_volume(5.0, 2.0, "backAudio")
    enS "Get ready."
    "Once the security guards close in on the box, Teresa activates the device again."
    "A powerful blaze erupts from the box."
    "Black smoke begins to billow into the depot as the fire alarm starts blaring."
    pS "Time to haul ass."
    mS "You read my mind."
    $ renpy.music.set_volume(10.0, 1.0, "backAudio")
    "The crowd explodes into a panic. Hordes of bodies rush towards the exit."
    "It's easy enough to slip through the crowd unnoticed."
    $ AddChatter(vig2_sc2_out_comment10)
    "Whatever security was covering the exit is long gone by the time we reach the doors."
    "The doors burst open as the crowd pours out of the depot."
    $ AddChatter(vig2_sc2_out_comment11)
    mS "Let's get off the main street!"
    "Teresa and Jennica nod as I point towards a small alleyway."
    stop backAudio fadeout 3.0
    "We're out and on our way to Matticus's compound."
    $ viewCheck4 += viewCount
    #Rstop music fadeout 2.0
    hide teresa with Dissolve(0.5)
    hide jennica with Dissolve(0.5)
    jump matticusDoor

###SCENE 3###
label matticusDoor():
    show vig2_compound_stream at topleft onlayer background with dissolve
    hide vig2_depot_stream
    #play music "soundtrack/theme.wav" fadein 1.0
    $ reactTarget = "vig2_sc3_aftercustoms"
    show screen streamerCommentary
    "It's only a few blocks to Matticus's compound."
    "Not like we could miss it though."
    show jennica stream shock at stream_left with dissolve
    "Jennica's eyes widen as we first see the gates."
    hide screen streamerCommentary
    pS "Holy smokes!"
    "The gates dwarf the rest of the block."
    "They're taller than the whole building across the street, and shining with gaudy golden accents and initials."
    $ AddChatter(vig2_sc3_comment1)
    show teresa stream neutral at stream_right with dissolve
    enS "Understated. How classy."
    mS "Yeah I need a second to just appreciate the elegance of it all."
    show jennica stream angry at stream_left
    pS "Can we get this over with?"
    $ AddChatter(vig2_sc3_comment2)
    "Jennica motions to the intercom."
    pS "I'd like to be done dealing with with this slum-king as soon as possible."
    "A muffled voice pipes up from the crate."
    play audio "macAffirmative.wav" volume 1.5
    macS "Po-dunk king!"
    show jennica stream neutral
    "Jennica hides her laughter."
    enS "Quiet!"
    "I press on the intercom button outside the gate."
    play audio "callRing.wav" volume 2.0
    "A dial tone begins to play"
    show jennica stream neutral at stream_left
    mattdoorbell "Name and ID?"
    mS "We're old friends of Sav."
    $ AddChatter(vig2_sc3_comment3)
    mattdoorbell "Sure. And my wife loves me more than anything."
    mS "What?"
    mattdoorbell "Oh sorry, I thought we were practicing how to believe our own delusions."
    mattdoorbell "The boss doesn't see \"friends.\" He doesn't have 'em."
    $ AddChatter(vig2_sc3_comment4)
    mS "Real old. Before his coronation."
    mattdoorbell "Snakehawks?"
    mS "I don't like to brag."
    mattdoorbell "Thought there weren't any left after your last job."
    mS "Yeah me too. Can we come in?"
    mattdoorbell "I need a little more proof than that."
    menu:
        mattdoorbell "I need a little more proof than that."
        "Bring up an old debt.": #Lore
            $ macPeace += 1
            $ marshal += 1
            mS "Remind him that he owes me his whole ass for saving him on Tiber III."
            mattdoorbell "Alright give me a sec."
            "The line goes quiet."
            $ AddChatter(vig2_sc3_lore_comment1)
            $ pilotApproval -= 1
            pS "Not sure if {i}that{/i} was the best story to bring up Cap."
            mS "I mean, there's no way he forgot about it."
            pS "That's the point..."
            "The intercom lights up again."
            $ AddChatter(vig2_sc3_lore_comment2)
            mattdoorbell "You're good. But not here."
            mattdoorbell "The boss has to be careful who he's seen with."
            mattdoorbell "He'll meet you in the warehouse down the road. Here's the coordinates."
        "Threaten the doorman.": #Threaten
            $ macViolence += 1
            $ outlaw += 1
            $ pdEngagement += 1
            mS "Listen buddy. Just let us in."
            mS "Do you wanna explain to him that you pissed off his old merc crew?"
            mattdoorbell "No, I just—"
            "He's flustered."
            $ AddChatter(vig2_sc3_threat_comment1)
            mS "Tell him Moze is going to do to this gate what he did to that bar on Forsteuk if you don't let her in."
            mattdoorbell "Fine. Have it your way."
            "The line goes quiet."
            $ AddChatter(vig2_sc3_threat_comment2)
            $ engineerApproval -= 1
            enS "As much as it amuses me to see you coerce some mook..."
            enS "Was that really the best course of action?"
            mS "He's a big boy. He'll be fine."
            $ AddChatter(vig2_sc3_threat_comment3)
            mattdoorbell "You're good. But not here."
            mattdoorbell "The boss has to be careful who he's seen with."
            mattdoorbell "He'll meet you in the warehouse down the road. Here's the coordinates."
    stop music fadeout 2.0
    hide teresa with Dissolve(0.5)
    hide jennica with Dissolve(0.5)
    jump meetingMatticus

###SCENE4###
label meetingMatticus():
    show warehouse_stream at topleft onlayer background with dissolve
    hide vig2_compound_stream
    $ AddChatter(vig2_sc4_comment1)
    $ viewCheck5 += viewCount
    "The dingy warehouse has a hint of stale air."
    "Just as I think to look how long we've been waiting, the doors swing open."
    play music "soundtrack/matticus.wav"
    show matticus stream at stream_center with dissolve
    smatt "As I live and breathe!"
    "Matticus waddles through the doors into view, flanked on either side by henchmen."
    $ vig2_sc4_comment1.click = False
    $ reactTarget = "vig2_sc4_meetingmatticus"
    show screen streamerCommentary
    "He approaches me smiling, revealing rows of yellowed teeth."
    smatt "I thought my doorman was lying! But here you are."
    "Matticus pulls out a cigar and lights it."
    mS "Yeah. Here we are."
    smatt "What a delightful surprise. And you brought Jenn too."
    show jennica stream angry at stream_left with dissolve
    "Jennica silently nods, trying to redirect the smoke away from her face."
    smatt "Quite a reunion!"
    hide screen streamerCommentary
    menu: #minorchoice4
        smatt "Quite a reunion!"
        "Great to see you.":
            mS "Yeah. Always great to see old friends."
            mS "Right, Jenn?"
            "Jennica looks annoyed."
            pS "Yeah. 'Been too long, Sav."
            "Matticus smirks knowingly."
            smatt "Oh, Jenn. You don't have to lie."
        "Reunion implies a lot.":
            mS "Reunion implies that we were united at one point."
            smatt "Ice cold as always Moze!"
            smatt "Y'know, I miss this banter. I've missed you ladies."
            pS "Really?"
            "Matticus smirks and looks at Jennica."
            smatt "No."
    "Matticus takes a long drag on his cigar before looking at me expectantly. The fake smile fades from his face."
    hide jennica with dissolve
    show matticus stream at stream_left with move
    smatt "... So? I assume you didn't come all this way to reminisce about the good ol' days."
    mS "No. We need a favor."
    smatt "Do you now?"
    mS "BigCorp is looking for us. We want to make that difficult."
    smatt "I see. I wonder if it has to do with the break-in to their top secret facility a few weeks back."
    "The smoke wafts out of Matticus's grin like fog."
    mS "It might."
    mS "And they hired our old boss to hunt us."
    "Matticus stops smirking."
    smatt "Oh."
    smatt "She doesn't come cheap."
    smatt "You really kicked the hornet's nest, eh?"
    "A voice perks up from the crate."
    play audio "macPing.wav" volume 3.0
    macS "Kick the hornet's nest. Idiom. Provoking a situation whi—"
    show reginald stream bigmad at stream_right with Dissolve (0.2)
    goon "What the hell!?"
    "Matticus's guards spring into action and draw their weapons."
    show mac stream shock at stream_center_mac with Dissolve(0.5)
    play audio "macSad.wav" volume 1.5
    "MAC sheepishly opens the crate lid and pokes his head out."
    hide reginald with Dissolve (0.5)
    smatt "Who's this?"
    menu: #minorchoice5
        smatt "Who's this?"
        "What we stole from BigCorp.": 
            #$ macHonesty += 1
            $ pilotApproval -= 1
            $ engineerApproval -= 1
            hide mac with dissolve
            mS "He's what was in that facility."
            show matticus stream at stream_center with move
            "Matticus approaches MAC, looking him over."
            smatt "Neat. So how much you figure it's worth?"
            smatt "BigCorps's burning money to get it back, must be something important."
        "Mind your own business.":
            #$ macHonesty -= 1
            hide mac with dissolve
            mS "None of your business."
            show matticus stream at stream_center with move
            "Matticus looks back at me, one eyebrow raised."
            smatt "Oh really?"
            smatt "Looks like a courier bot..."
            "Matticus looks back at MAC."
            smatt "But they don't talk like {i}that{/i}."
            smatt "What're a couple of outlaws doing with something like this?"
    $ AddChatter(vig2_sc4_comment2)
    mS "We're just looking to get him to the Dragonflies."
    "Matticus's eyes widen. His voice takes on a singsong quality."
    smatt "Moze! You've gone soft!"
    smatt "I never figured you for a tenderhearted philanthropist!"
    $ AddChatter(vig2_sc4_comment3)
    show jennica stream angry at stream_left with Dissolve(0.5)
    "Jennica rolls her eyes."
    "I hear MAC quietly chime in."
    show mac stream neutral at stream_right_mac with Dissolve(0.5)
    play audio "macAlarmed.wav" volume 2.0
    macS "\"Skeeve\" detected."
    mS "Not now, MAC."
    smatt "Oh and it's got jokes too! Fun."
    hide mac with dissolve
    show teresa stream neutral at stream_right with Dissolve(0.5)
    enS "We don't have all day. Will you help us or not?"
    "His face twists into a grin again."
    smatt "I might. First I need you to do something for me."
    mS "I'm listening."
    $ AddChatter(vig2_sc4_comment4)
    smatt "It's a simple job. Right in your wheelhouse."
    smatt "There's an off-world shipment coming in later today. It's going to have an abrupt reunion with gravity."
    smatt "I was gonna hire mercs, but you'll save me a few bucks."
    pS "What's in the shipment?"
    "Matticus continues to smirk as he takes another long drag off his cigar."
    smatt "It's not important."
    $ AddChatter(vig2_sc4_comment5)
    pS "I don't care for that answer one bit."
    smatt "You'll have to learn to like it, or you'll find out what Deadeye's got planned for you."
    enS "That's a reasonable point, Captain."
    menu: #minorchoice6
        "Matticus isn't telling us something."
        "Why are you so cagey?":
            mS "What aren't you telling us?"
            "Matticus smirks at me."
            smatt "Any number of things, really."
            mS "Don't play dumb. Why are you being so sketchy about what's in the shipment?"
            "A twinge of anger passes through Matticus's face for a moment."
            smatt "Since when do you care?"
            smatt "Awful late in the game to start thinking about details like that."
            "Matticus's anger subsides, his smug facade is back up."
            smatt "Besides. Where else are you gonna go?"
            smatt "You're not out here because you've got options."
            "I turn to Jennica."
            mS "He's not wrong."
        "Trying to screw us over?":
            mS "Seems suspicious, Sav. What are you trying to pull here?"
            "Matticus smirks at me."
            smatt "Moze! After all our time together..."
            mS "After all our time together I know you well enough to know when you're hiding something."
            smatt "So what if I am?" 
            smatt "Look, if I really wanted to turn you in, don't you think I'd have done it by now?"
            pS "You might yet."
            "Matticus chuckles."
            smatt "You think I want the inspectors poking around my operation?"
            smatt "Besides. Where else are you gonna go?"
            smatt "You're not out here because you've got options."
            "I turn to Jennica."
            mS "He's not wrong."
    mS "What alternatives do we have, Jenn?"
    "Jennica reluctantly agrees."
    $ reactTarget = "vig2_sc4_plancheckin"
    show screen streamerCommentary
    $ AddChatter(vig2_sc4_comment6)
    mS "And if we do this?"
    smatt "I'll feed false reports into the BigCorp security database."
    smatt "Deadeye'll be looking for you in every corner of the galaxy, except for where you actually are."
    smatt "And you bleeding hearts will be free to save the universe."
    enS "Not an unreasonable agreement."
    show jennica stream crossed
    pS "I don't buy it. Seems fishy."
    smatt "Oh Jenn. I'm wounded. After all we've been through?"
    $ AddChatter(vig2_sc4_comment7)
    smatt "You still don't trust me?"
    show jennica stream angry
    pS "You surprised?"
    smatt "I don't get surprised honey."
    pS "Seemed surprised at the door."
    "Matticus smirks at Jennica."
    $ AddChatter(vig2_sc4_comment8)
    smatt "Oh? Did I?"
    play audio "macGrumble.wav" volume 1.0
    "MAC anxiously looks around."
    hide screen streamerCommentary
    smatt "Don't waste my time. Do we have a deal?"
    "Matticus looks at me impatiently."
    menu: #minorchoice7
        "Matticus looks at me impatiently."
        "Deal.":
            "Guess we don't have much choice."
            mS "On your honour as a Snakehawk?"
            "Matticus chuckles to himself."
            smatt "How nostalgic."
            smatt "On my honour."
        "Wait this still seems suspicious.":
            "This still seems fishy."
            mS "Wait. This all seems too good to be true."
            smatt "Things aren't always what they seem Moze."
            smatt "Besides, I'm done with this haggling. Do you want to work together or not?"
            menu: #minorchoice7a
                smatt "Besides, I'm done with this haggling. Do you want to work together or not?"
                "Fine. Deal.":
                    "Guess we don't have much choice."
                    mS "On your honour as a Snakehawk?"
                    "Matticus chuckles to himself."
                    smatt "How nostalgic."
                    smatt "On my honour."
                "Keep asking questions.":
                    $ macHope -= 1
                    mS "I can't help but feel like you're manipulating us."
                    smatt "Feelings lie Moze."
                    "Matticus rolls his eyes."
                    smatt "I don't have time for this. Take the deal or get lost."
                    enS "Captain we really can't afford to get caught."
                    "Guess we don't have much choice."
    mS "Alright. Deal."
    smatt "Good. My pointman Reginald will brief and supervise."
    show matticus stream at stream_right5 with move
    show reginald stream neutral at stream_left5 with dissolve
    "One of the henchmen nods to us."
    $ AddChatter(vig2_sc4_comment9)
    smatt "I'll see you ladies later. It's been lovely catching up."
    menu: #minorchoice8
        smatt "I'll see you ladies later. It's been lovely catching up."
        "Bye.":
            mS "Later, Sav."
            $ engineerApproval += 1
        "Piss off.":
            $ pdEngagement += 1
            $ pilotApproval += 1
            $ engineerApproval -=1
            mS "Get bent you ugly warthog."
            #show jennica stream happy at stream_left
            "Jennica chuckles."
            enS "Mature."
    "Matticus waves as he leaves the warehouse."
    hide matticus stream with dissolve
    show reginald stream neutral at stream_center with move
    "Reginald turns to us."
    goon "Alright. So first we need to get the tracking coordinates for this ship."
    "MAC pipes up from his crate."
    show mac stream shock at stream_right5 with dissolve
    play audio "macAlarmed.wav" volume 2.0
    macS "Another \"skeeve?\""
    show reginald stream mad at stream_center
    "Reginald rolls his eyes."
    show mac stream neutral
    goon "They're stored at a communications array on the outskirts of the city."
    $ AddChatter(vig2_sc4_comment10)
    mS "Matticus doesn't have the target's location?"
    pS "Yeah why is this our job? I thought the \"king\" would have mooks to do this."
    goon "His guys can't be seen doing this."
    pS "Reassuring."
    goon "We don't have time for this. Let's get to the shuttle."
    mS "Agreed."
    play backAudio "jetEngines.wav" volume 1.0 fadein 2.0
    hide reginald with Dissolve(0.5)
    hide jennica with Dissolve(0.5)
    hide teresa with Dissolve(0.5)
    hide mac with Dissolve(0.5)
    #stop music fadeout 2.0 - want to keep the matticus music going thru next scene
    jump approachingBase

###SCENE 5###
label approachingBase():
    show vig2_targetbase_stream at topleft onlayer background with dissolve
    hide warehouse_stream
    show jennica stream neutral at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve
    stop backAudio fadeout 5.0
    $ renpy.music.set_volume(0.7, 1)
    #play music "soundtrack/gibianV.wav" fadein 2.0
    "The shuttle lands on the ground near the base."
    "Hardly a base, more of an outpost with a big antenna."
    pS "Forgot how cramped these cheapo shuttles are."
    enS "Fitting for a cheapo planet like this."
    mS "Pipe down you two. Focus up."
    "Jennica and Teresa nod to me."
    show mac stream neutral at stream_center_mac with Dissolve(0.5)
    "The brief silence is broken by MAC."
    play audio "macPing.wav" volume 1.5
    macS "What is a \"cheapo planet?\" My database has no\"cheapo\" category."
    "Jennica laughs."
    pS "Similar to po-dunk."
    "A kind of realization flashes across MAC's eyes, like he's connecting the two."
    enS "What about that?"
    "Teresa gestures towards MAC."
    enS "Perhaps we just leave it here?"
    mS "We're gonna have to bring him along. It's not ideal, but if he gets taken from the shuttle then all of this is pointless."
    enS "True. However, it is equally pointless if it gets damaged beyond repair."
    enS "And we \"lost\" the last mechanic we knew who could help out with that."
    mS "I'll protect him. It's my responsibility."
    mS "MAC, you're going to stick to me like glue, got it?"
    macS "Like an adhesive? I don't want to damage your clothes."
    show teresa stream upset
    "Jennica chuckles under her breath."
    $ AddChatter(vig2_sc5_comment1)
    mS "No, MAC, you need to stay close to me. It's dangerous in there and I need to protect you."
    macS "This is a dangerous place? Are these bad people like Matticus?"
    menu:
        macS "This is a dangerous place? Are these bad people like Matticus?"
        "They're bad people.":
            $ macPessimism += 1
            $ pdEngagement -= 1
            $ AddChatter(vig2_sc5_comment2)
            mS "Yes. They're bad people."
            $ AddChatter(vig2_sc5_comment3)
            macS "I understand. I will stay close to Captain."
            show teresa stream neutral
            $ reactTarget = "vig2_sc5_macquestion"
            show screen streamerCommentary
            $ AddChatter(vig2_sc5_comment4)
            mS "Good. Let's move."
            hide mac with dissolve
        "Maybe.":
            #$ macHonesty += 1
            mS "I don't know. But they will try to hurt us."
            $ AddChatter(vig2_sc5_comment2)
            macS "Why do we need to work with bad people?"
            mS "We don't have the time to discuss it right now."
            $ AddChatter(vig2_sc5_comment5)
            mS "You just need to stay close to me."
            macS "I understand. I will stay close to Captain."
            show teresa stream neutral
            $ reactTarget = "vig2_sc5_macquestion"
            show screen streamerCommentary
            mS "Good. Let's move."
            hide mac with dissolve
        #Should NPC approval adjustments happen here?
    show reginald stream neutral at stream_center with Dissolve(0.5)
    pS "So, you got a plan?"
    goon "Plan? This is your operation. We just gotta get to the main datacentre computer."
    hide screen streamerCommentary
    enS "Do you even know where it is?"
    goon "Yeah. In there somewhere. This is Gibian V. There are maybe three or four rooms in there."
    goon "How much traffic do you think comes through here?"
    pS "Maybe we can get in and out before drawing attention?"
    show reginald stream mad at stream_center
    goon "Seems pointless, but I don't give a shit. It's your job."
    enS "You're not coming with us?"
    goon "You think I get paid enough to get shot at? As if."
    "Reginald lights a cigarette and walks off."
    hide reginald with dissolve
    #$ chatter_list.append(vig2_sc5_comment6)
    $ AddChatter(vig2_sc5_comment6)
    show teresa stream think
    enS "I'm inclined to agree with him. We don't know how much firepower they'll have in there."
    enS "I say we go in heavy and take them out expeditiously. Minimize the hazards to ourselves and the cargo."
    show jennica stream crossed
    pS "The fewer people who know we were here the better. And an explosion'll tip a few folks off"
    enS "On Gibian V? I doubt this news makes it off-world."
    show teresa stream neutral
    show jennica stream neutral
    pS "What's your call Cap?"
    menu:
        pS "What's your call Cap?"
        "A full offensive is more tactically sound.":
            $ gunsBlazing = True
            $ outlaw += 3
            $ pdEngagement += 3
            $ kcEngagement += 2
            $ csEngagement -= 1
            $ engineerApproval += 2
            $ macViolence += 3
            "We don't know what kind of security we're walking into."
            $ AddChatter(vig2_sc6_out_comment1)
            "Getting caught off guard is a risk we can't afford to take."
            mS "I agree with Teresa. We can't know what's waiting for us inside."
            show teresa stream happy at stream_right
            mS "We'll get in and out quick and dirty."
            $ AddChatter(vig2_sc6_out_comment2)
            pS "Alright Cap."
            enS "I'll whip up a door breaching charge."
            show teresa stream neutral at stream_right
            mS "I'll take point, you two cover me when I go in."
            $ viewCount += 1
            $ AddChatter(vig2_sc6_out_comment3)
            "Teresa and Jennica nod in agreement."
            show reginald stream neutral at stream_center with dissolve
            "I wave over Reginald."
            goon "So what are we doing?"
            mS "Going in the front door guns blazing."
            show reginald stream impressed at stream_center
            goon "Legends. This should be entertaining."
            $ viewCheck6 += viewCount
            "Teresa signals to me that she's ready."
            mS "Alright let's get to it."
            stop music fadeout 6.0
            hide teresa with Dissolve(0.5)
            hide jennica with Dissolve(0.5)
            hide reginald with Dissolve(0.5)
            jump commsBase_OUT1
        "Better to be as quiet as possible.":
            $ marshal += 2
            $ gunsBlazing = False
            $ csEngagement += 2
            $ pdEngagement -= 2
            $ kcEngagement -= 1
            $ pilotApproval += 2
            $ macPeace += 2
            $ AddChatter(vig2_sc6_mar_comment1)
            "Quick and quiet would be safer."
            mS "Jennica's right, lets try to avoid attention."
            #show jennica stream happy at stream_left
            enS "Very well. I'll get to work disabling the alarm."
            $ AddChatter(vig2_sc6_mar_comment2)
            $ shnzi = False
            $ viewCount -= 1
            pS "The fire escape on the left'll be our way in."
            mS "Good. Remember, quick and quiet."
            "Jennica and Teresa nod in agreement."
            $ AddChatter(vig2_sc6_mar_comment3)
            "I wave Reginald over."
            show reginald stream neutral at stream_center with dissolve
            mS "We're going in quiet."
            "Reginald chuckles."
            $ AddChatter(vig2_sc6_mar_comment4)
            $ viewCheck6 += viewCount
            show reginald stream surprised at stream_center
            goon "Really? I didn't think ex-Snakehawks would be so demure."
            goon "Whatever. I'll follow behind you."
            stop music fadeout 3.0
            hide jennica with Dissolve(0.5)
            hide reginald with Dissolve(0.5)
            jump commsBase_MAR1

####SCENE 6####
label commsBase_MAR1():
    show vig2_compound_hall_stream at topleft onlayer background with dissolve
    play music "soundtrack/stealthmode.wav" volume 1.8 fadein 1.0
    show teresa stream neutral at stream_right with Dissolve (0.3)
    "As we approach the base, Teresa signals to stay quiet."
    "After climbing up the fire escape, Teresa takes out a device and affixes it to the door."
    play audio "unlock.wav" volume 2.5
    "The devices begins to beep and its lights flicker on and off."
    "Teresa mutters under her breath."
    enS "Child's play."
    "The door unlocks and pops ajar."
    hide teresa with dissolve
    show vig2_compound_hall_stream at topleft onlayer background with dissolve
    hide vig2_targetbase_stream
    "We're inside. The base seems even smaller on the inside and lightly guarded."
    "Its just a few stairs down from the upper level to the ground floor."
    "The stairs lead to a hallway."
    show guard1 stream at stream_center with Dissolve(0.2)
    "We turn the corner and run face-first into a lone guard on patrol."
    "He jumps up, startled, and begins raising his hand..."
    "My instincts take over."
    menu:
        "My instincts take over."
        "Stun him":
            $ kcEngagement -= 1
            $ engineerApproval += 1
            "I instantly flick my blaster to stun before shooting him in the chest."
            $ AddChatter(vig2_sc6_mar_choice1_stun_comment1)
            "He can barely react as the stunning blast ripples through his body, incapacitating him."
            play audio "lazer.wav" volume 1.0
            "As he slumps to the ground, his eyes stare back at me with... confusion?"
            "He seems completely dumbfounded as to why we're here."
            hide guard1 stream with dissolve
            show reginald stream bigmad at stream_center with Dissolve(0.5)
            goon "Keep moving!"
            mS "I know!"
            "I can't afford to hesitate."
            hide reginald with dissolve
            jump commsBase_MAR2
        "Bluff.":
            $ pdEngagement += 1
            $ csEngagement += 1
            $ kcEngagement += 1
            $ pilotApproval += 1
            $ macPeace += 1
            mS "Hey! How's it going?"
            "His hand raises into a wave as he greets us"
            hsguard1 "Hey! Sorry I don't think we've met."
            mS "Yeah, we're the new security recruits. Just getting familiarized now for our shift tomorrow."
            hsguard1 "We have money for new recruits?"
            mS "Yeah I was shocked too. I'll see you around?"
            hsguard1 "Sure."
            hide guard1 stream with dissolve
            "He continues along his patrol, oblivious."
            $ AddChatter(vig2_sc6_mar_choice1_bluff_comment1)
            show jennica stream neutral at stream_left with Dissolve(0.5)
            pS "This seems too easy."
            mS "Tell me about it."
            hide jennica with dissolve
            jump commsBase_MAR2

label commsBase_MAR2():
    "At the end of the hall, we arrive at a door."
    "Cracking the door ajar, I'm able to get a look at what's on the other side."
    "There is a typical security desk manned by three guards."
    "They don't have much in the way of firepower, just their sidearms."
    "And they aren't so focused either. Shouldn't be too hard to get past them."
    "We could probably bust in and stun them all without an issue."
    "But that might get a little hairy."
    "A fake radio call would probably get them all to leave too."
    "They might come back though."
    $ viewCheck7 += viewCount
    menu:
        "Knock them out.":
            $ macViolence += 1
            "We can't risk them coming back and finding us."
            $ AddChatter(vig2_sc6_mar_choice2_stun_comment1)
            "We need to neutralize these guys."
            "I signal to Jennica and Teresa that we're going to stun them."
            show jennica stream fight at stream_left with Dissolve(0.3)
            show teresa stream fight at stream_right with Dissolve(0.3)
            "I'll take the one on the right, Jennica will get the middle one, and Teresa the left."
            "Jennica and Teresa take position behind me."
            "Once everyone's ready, I kick the door open."
            $ AddChatter(vig2_sc6_mar_choice2_stun_comment2)
            "It's over in a flash, the guards barely have time to react."
            play audio "lazerFire.wav" volume 1.0
            "Like clockwork, they all fall to the ground."
            show jennica stream neutral at stream_left
            show teresa stream upset at stream_right
            pS "This all feels way too easy."
            enS "Why is that a bad thing?"
            $ AddChatter(vig2_sc6_mar_choice2_stun_comment3)
            $ reactTarget = "vig2_sc6_mar_reflect"
            show screen streamerCommentary
            enS "I rather like it when things are easy."
            show reginald stream neutral at stream_center with Dissolve(0.3)
            "Reginald signals us to follow him."
            goon "The main datacentre is through this door here."
            "Reginald opens the door."
            hide screen streamerCommentary
            hide teresa with Dissolve(0.5)
            hide jennica with Dissolve(0.5)
            hide reginald with Dissolve(0.5)
            jump commsBase_DataCenter
        "Go with a diversion.":
            $ macPeace += 1
            $ csEngagement += 1
            $ kcEngagement -= 1
            $ pdEngagement -= 1
            "We can get through without firing a shot."
            "Quick and quiet."
            "I signal to Teresa to prepare a fake radio diversion."
            show teresa stream think at stream_right with dissolve
            "She nods, and begins inputting code into her computer."
            $ AddChatter(vig2_sc6_mar_choice2_dist_comment1)
            play audio "shipalarmshort.wav" volume 0.4
            "In an instant, all three of the guards' radios begin blaring with a distress call."
            "A sense of urgency hits them as they begin running out of the room to the source of the call."
            "Once they're out, I wave over Reginald."
            show teresa stream neutral at stream_right
            show reginald stream mad at stream_center with dissolve
            show jennica stream neutral at stream_left with dissolve
            goon "Wow so much work for what?"
            pS "This all feels way too easy."
            $ reactTarget = "vig2_sc6_mar_reflect"
            show screen streamerCommentary
            $ AddChatter(vig2_sc6_mar_choice2_dist_comment2)
            show teresa stream upset at stream_right
            enS "Why is that a bad thing?"
            enS "I rather like it when things are easy."
            "Reginald signals us to follow him."
            goon "The main datacentre is through this door here."
            "Reginald opens the door."
            hide screen streamerCommentary
            hide teresa with Dissolve(0.5)
            hide jennica with Dissolve(0.5)
            hide reginald with Dissolve(0.5)
            jump commsBase_DataCenter

label commsBase_OUT1():
    #show vig2_compound_hall_stream at topleft onlayer background with dissolve
    hide vig2_targetbase_stream with dissolve
    show teresa stream fight at stream_right with Dissolve(0.5)
    show jennica stream fight at stream_left with Dissolve(0.5)
    "Teresa begins placing the charge on the front door."
    "We line up on either side of the entrance."
    play audio "macGrumble.wav"
    show mac stream neutral at stream_center_mac with Dissolve(0.5)
    "I notice MAC looks a little worried."
    menu:
        "I notice MAC looks a little worried."
        "It's going to be ok.":
            $ macHope += 1
            mS "Don't worry MAC, everything's gonna be ok."
            mS "Just stay close to me."
        "It's going to be chaotic.":
            $ macPessimism += 1
            mS "Things are going to get hectic in there, MAC."
            mS "Just stay close to me."
    play audio "macAffirmative.wav"
    macS "Affirmative. Sticking to Captain."
    $ AddChatter(vig2_sc6_out_comment5)
    hide mac with Dissolve(0.5)
    "I give the signal to Teresa."
    hide jennica
    hide teresa
    play music "soundtrack/saveTheGalaxy.wav" volume 1.2
    show vig2_compound_hall_stream at topleft onlayer background with vpunch
    "With a deafening bang, the door is obliterated into countless pieces."
    "An instant later I'm running through the smoke."
    play backAudio "lazerFire.wav" volume 2.0
    play audio "macSpin.wav" volume 0.5
    "MAC's motor whirs behind me."
    "I make a dive for a piece of rubble as shots fly around me."
    $ AddChatter(vig2_sc6_out_comment6)
    "I peek out from cover."
    $ AddChatter(vig2_sc6_out_comment7)
    "Two of the guards are dead already from the explosion."
    $ AddChatter(vig2_sc6_out_comment8)
    "Two more are shooting at us from the other side of the room."
    $ AddChatter(vig2_sc6_out_comment9)
    "I think I have a good shot on one of them."
    menu:
        "I think I have a good shot on one of them."
        "Shoot to kill.":
            $ pdEngagement += 1
            $ csEngagement -= 1
            "I take a deep breath and fire my blaster."
            play audio "lazer.wav" volume 1.0
            "The guard's head snaps back before he slumps over."
            $ AddChatter(vig2_sc6_out_shoot_comment1)
            $ AddChatter(vig2_sc6_out_shoot_comment2)
            $ AddChatter(vig2_sc6_out_shoot_comment3)
            "I hear shots ringing out from behind me."
            play audio "lazerFire.wav" volume 0.5
            $ AddChatter(vig2_sc6_out_shoot_comment4)
            pS "Nice shooting!"
            show jennica stream fight at stream_left with Dissolve(0.2)
            "Jennica dives into cover next to me."
        "Suppressing fire.":
            $ kcEngagement += 1
            "Too risky."
            $ AddChatter(vig2_sc6_out_suppress_comment1)
            "I fire a few more shots from cover."
            play audio "lazerFire.wav" volume 1.0
            $ AddChatter(vig2_sc6_out_suppress_comment2)
            "Shots ring out from behind me, hitting one of the guards."
            play audio "lazerFire.wav" volume 0.5
            pS "Thanks for the cover!"
            show jennica stream fight at stream_left with Dissolve(0.2)
            "Jennica dives into cover next to me."
    mS "There's only one left!"
    mS "Teresa has him pinned down."
    pS "I'll get'em!"
    "Jennica leaps out of cover and begins running towards the guard."
    "Three more guards emerge from the door, guns drawn."
    pS "Shit! We got company!"
    $ AddChatter(vig2_sc6_out_comment11)
    hide jennica with Dissolve(0.5)
    "Jennica takes cover behind another piece of rubble."
    play audio "lazerFire.wav" volume 0.5
    "I hear shots whizzing over my head as the guards fire at us."
    "I pull out a grenade and lob it at the guards."
    $ AddChatter(vig2_sc6_out_comment12)
    hsguard1 "GRENADE! GET DOWN!"
    #explosion sound here?
    "Two of the guards are able to dive out of the way in time."
    $ AddChatter(vig2_sc6_out_comment13)
    "The grenade detonates with an unnerving concussive thump."
    "I peek out of cover and spot one of the guards running."
    play audio "lazer.wav" volume 1.0
    "Jennica fires her blaster, hitting the fleeing guard."
    $ AddChatter(vig2_sc6_out_comment14)
    play audio "lazerFire.wav" volume 0.5
    "Teresa continues shooting."
    "Only one guard is left."
    stop backAudio fadeout 1.0
    $ renpy.music.set_volume(0.4, 1.0)
    $ AddChatter(vig2_sc6_out_comment15)
    show guard1 stream at stream_center with Dissolve(0.4)
    hsguard1 "I surrender!"
    mS "Stand up and put your hands where I can see them!"
    "The guard complies."
    hsguard1 "Please, Miss, just let me go, I promise I'll never breathe a word of this to anyone."
    "He's terrified, as if this is the first time anyone's shot at him."
    $ AddChatter(vig2_sc6_out_comment16)
    pause 0.5
    $ AddChatter(vig2_sc6_out_comment17)
    pause 0.5
    $ AddChatter(vig2_sc6_out_comment18)
    $ viewCheck7 += viewCount
    menu:
        "He's terrified, as if this is the first time anyone's shot at him."
        "This isn't his fault.":
            $ macPeace += 1
            $ macHope += 1
            $ baseGuardKilled = False
            $ marshal += 2
            $ pilotApproval += 2
            $ pdEngagement -= 1
            $ kcEngagement += 1
            $ csEngagement += 1
            $ AddChatter(vig2_sc6_out_spare_comment1)
            "This guy was just doing his job."
            mS "Alright."
            $ AddChatter(vig2_sc6_out_spare_comment2)
            hsguard1 "Thank you miss! I—"
            play audio "lazer.wav" volume 5.0
            hide guard1 stream with Dissolve (0.1)
            "A shot rings out and the guard falls over, lifelessly."
            show reginald stream neutral at stream_center with dissolve
            "Reginald stands over the corpse."
            $ AddChatter(vig2_sc6_out_spare_comment3)
            goon "Come on. We're almost done."
            $ AddChatter(vig2_sc6_out_spare_comment4)
            show jennica stream shock at stream_left with Dissolve(0.2)
            pS "What the hell!?"
            show jennica stream angry at stream_left
            mS "He didn't need to die!"
            show reginald stream mad at stream_center
            $ AddChatter(vig2_sc6_out_spare_comment5)
            show teresa stream neutral at stream_right with Dissolve(0.2)
            enS "Better him than us I suppose."
            show jennica stream crossed at stream_left
            $ AddChatter(vig2_sc6_out_spare_comment6)
            "Jennica scowls at Teresa."
            goon "We haven't got all day!"
            $ reactTarget = "vig2_sc6_out_reflect"
            show screen streamerCommentary
            $ AddChatter(vig2_sc6_out_spare_comment7)
            "Reginald approaches and opens the door to the datacentre."
        "I can't risk survivors.":
            $ macViolence += 1
            $ macPessimism += 2
            $ baseGuardKilled = True
            $ outlaw += 2
            $ engineerApproval += 1
            $ pdEngagement += 1
            $ csEngagement -= 1
            "The less witnesses the better."
            $ AddChatter(vig2_sc6_out_execute_comment1)
            $ AddChatter(vig2_sc6_out_execute_comment2)
            "I raise my blaster."
            $ AddChatter(vig2_sc6_out_execute_comment3)
            hsguard1 "Miss, I have kids."
            $ AddChatter(vig2_sc6_out_execute_comment4)
            play audio "lazer.wav" volume 5.0
            hide guard1 stream with Dissolve(0.1)
            "His body slumps to the ground lifelessly."
            $ AddChatter(vig2_sc6_out_execute_comment5)
            $ AddChatter(vig2_sc6_out_execute_comment6)
            $ AddChatter(vig2_sc6_out_execute_comment7)
            show jennica stream shock at stream_left with Dissolve(0.2)
            pS "Damn, Cap. That was cold."
            $ AddChatter(vig2_sc6_out_execute_comment8)
            $ AddChatter(vig2_sc6_out_execute_comment9)
            $ AddChatter(vig2_sc6_out_execute_comment10)
            show teresa stream neutral at stream_right with Dissolve(0.2)
            enS "Better safe than sorry."
            show jennica stream angry at stream_left
            $ AddChatter(vig2_sc6_out_execute_comment11)
            show reginald stream neutral at stream_center with Dissolve(0.2)
            "Reginald emerges through the door."
            $ AddChatter(vig2_sc6_out_execute_comment12)
            $ AddChatter(vig2_sc6_out_execute_comment13)
            pS "Nice of you to join us."
            show reginald stream mad
            "Reginald rolls his eyes at Jennica."
            $ reactTarget = "vig2_sc6_out_reflect"
            show screen streamerCommentary
            $ AddChatter(vig2_sc6_out_execute_comment14)
            goon "Come on. We're almost done."
            $ AddChatter(vig2_sc6_out_execute_comment15)
    hide teresa with Dissolve(0.5)
    hide jennica with Dissolve(0.5)
    hide reginald with Dissolve(0.5)
    jump commsBase_DataCenter

###SCENE 7###
label commsBase_DataCenter():
    #Placeholder
    show vig2_datacenter_stream at topleft onlayer background with dissolve
    hide vig2_compound_hall_stream
    "The datacentre is underwhelming."
    "At the center of the small room is a computer workstation with numerous monitors displaying a variety of shipments and other logistic info."
    hide screen streamerCommentary
    show data agent scared at stream_left5 with dissolve
    "Sitting at the workstation is a scrawny technician in glasses, terrified."
    stop music fadeout 3.0
    worker "What are you doing here!?"
    show reginald stream neutral at stream_right5 with Dissolve(0.2)
    play audio "chairRush.wav" volume 4.0
    "Before we have a chance to say anything, Reginald is in his face."
    show reginald stream bigmad at stream_right5
    goon "Shut it! What's the next shipment's tracking coordinates!?"
    worker "The aid shipm—"
    "Reginald shoves his gun into the technician's face."
    goon "{i}Now!{/i}"
    show jennica stream angry at stream_left with Dissolve(0.4)
    pS "What'd he say?"
    worker "Why do you want the tracking coordinates of an aid shipment?"
    $ AddChatter(vig2_sc7_comment1)
    pS "Yeah, Reginald, why {i}do{/i} we want the tracking coordinates of an aid shipment?"
    play music "soundtrack/decisionTime.wav" volume 1.2
    show reginald stream mad at stream_right5
    "Reginald sighs exasperatedly."
    goon "I don't get paid enough for this."
    goon "The shipment's going to a town called Sallent."
    goon "They haven't paid their protection money this month."
    $ AddChatter(vig2_sc7_comment2)
    goon "The boss wants to send a \"message\" to them and any other would-be heroes who don't think they need protection."
    $ AddChatter(vig2_sc7_comment3)
    show jennica stream shock at stream_left
    pS "I knew this was too damn easy!"
    hide data
    play audio "macAlarmed.wav"
    show mac stream neutral at stream_center_mac with dissolve
    macS "They were not \"skeeves?\""
    pS "They were rent-a-cops!"
    hide mac with Dissolve(0.1)
    show teresa stream shock at stream_right with Dissolve(0.2)
    enS "Well they were still cops."
    goon "Look. This is the mission. Don't act like you've never done worse."
    goon "I've heard stories of what you all did."
    "Reginald turns to look me in the eyes."
    goon "Especially {i}you{/i}."
    $ reactTarget = "vig2_sc7_bigreveal"
    show screen streamerCommentary
    mS "So what happens if the town doesn't get that aid?"
    show data agent scared at stream_left5
    worker "Sallent? There's an outbreak of Gray fever there. They need that medicine!"
    goon "People from a town you've never heard of until now {i}might{/i} die."
    goon "You really care that much about them?"
    $ AddChatter(vig2_sc7_comment4)
    show teresa stream think at stream_right with Dissolve(0.4)
    show jennica stream crossed at stream_left with Dissolve(0.4)
    enS "As much as I loathe to admit it, I agree."
    enS "We came here to cover our trail."
    $ AddChatter(vig2_sc7_comment5)
    show teresa stream neutral at stream_right
    enS "If we renege on the deal now, we'll be no closer to doing that, and we'll have made an enemy of Matticus."
    enS "All the people we save here won't matter if we get caught!"
    show jennica stream angry at stream_left
    pS "They're people!"
    pS "Being born {i}here{/i} doesn't make 'em disposable!"
    pS "We really going through with this, Cap?"
    hide screen streamerCommentary
    $ AddChatter(vig2_sc7_comment6)
    show mac stream neutral at stream_center_mac with Dissolve (0.5)
    "MAC is almost completely quiet. They've been looking at me the entire time." 
    $ AddChatter(vig2_sc7_comment7)
    $ viewCheck8 += viewCount
    menu:
        "MAC is almost completely quiet. They've been looking at me the entire time." 
        "This has gone too far.":
            $ marshal += 5
            $ csEngagement += 3
            $ pdEngagement -= 3
            $ kcEngagement += 1
            $ pilotApproval += 3
            $ engineerApproval -= 1
            $ macHope += 3
            $ macPeace += 1
            "This is just plain wrong."
            "We have to be better."
            "Or at least we have to try to be."
            jump commsBase_DataCenter_MAR
        "We don't have a choice.":
            $ macViolence += 3
            $ macPessimism += 1
            $ outlaw += 5
            $ csEngagement -= 3
            $ pdEngagement +=3
            $ kcEngagement += 1
            $ engineerApproval += 2
            $ pilotApproval -= 2
            #This way, either choice produces the same difference in micro-game NPC Approval
            #BUT if we want to do things where like only certain dialogues trigger if Approval with
            #someone is high enough, the difference in individual scales can matter
            "We've come this far."
            $ AddChatter(vig2_sc7_out_comment1)
            "We have to do this."
            mS "We don't have a choice anymore."
            jump commsBase_DataCenter_OUT

label commsBase_DataCenter_MAR():
    mS "We can't do this."
    pS "Cap?"
    $ AddChatter(vig2_sc7_mar_comment1)
    mS "We've come this far because we wanted to try and make this galaxy better."
    mS "How can we honestly say that if we follow through with this?"
    enS "Yes, but what does that matter if we get caught and BigCorp takes their robot back?"
    pS "We'll have tried."
    $ AddChatter(vig2_sc7_mar_comment2)
    enS "I don't like this any more than you two, but what's the alternative?"
    enS "If we don't cover our tracks, Deadeye will be on our asses in no time! We need Matticus's access to the security database."
    pS "We can find someone else with access!"
    enS "Yes access to secure databases is easy to find and widespread! How could I forget!?"
    enS "That's what \"secure\" means right!?"
    hide mac with dissolve
    "The technician perks up. He begins gingerly raising his hand before he's interrupted by Reginald."
    show reginald stream bigmad at stream_right5 with Dissolve(0.3)
    goon "Oh you have got to be kidding me."
    "Reginald points his blaster at me."
    $ reactTarget = "vig2_sc8_mar_reacttoregi"
    show screen streamerCommentary
    goon "How did the most infamous outlaw merc group in the outposts become soft as baby shit?"
    $ AddChatter(vig2_sc7_mar_comment3)
    goon "You really think I'm gonna let you just bail on this deal?"
    "I notice Jennica reaching for her blaster."
    hide screen streamerCommentary
    menu:
        "I notice Jennica reaching for her blaster."
        "Signal Jennica to stun him.":
            $ reginaldChoice = True
            $ outlaw += 1
            $ pilotApproval += 1
            $ engineerApproval += 1
            $ macViolence += 1
            "I look over to Jennica and give her the signal."
            show jennica stream fight at stream_left
            play audio "lazer.wav" volume 5.0
            "Reginald is struck by the stun bolt. His body seizes up and shakes before he falls to the floor, incapacitated."
            hide reginald with Dissolve(0.2)
            show jennica stream neutral at stream_left
            show teresa stream shock at stream_right
            pS "Wish I coulda done that hours ago."
            $ AddChatter(vig2_sc7_mar_stun_comment1)
            "I can see the burning hatred in his eyes, as if to say, \"This isn't over!\""
            $ reactTarget = "vig2_sc8_mar_reacttoregistun"
            show screen streamerCommentary
            show mac stream happy at stream_center_mac with Dissolve(0.2)
            #We could use a conditional here based on Mac's violence trait to alter his respone to Reggie getting tagged.
            macS "Take that \"skeeve!\""
            show teresa stream neutral at stream_right
            enS "I suppose the die is cast then."
            enS "So where are we to find someone to help cover our tracks now?"
            pS "Beats me."
            hide screen streamerCommentary
            hide mac with Dissolve(0.2)
        "Bribe Reginald.":
            $ reginaldChoice = False
            $ marshal += 1
            $ macPeace += 1
            "I signal to Jennica to wait."
            mS "How much do you really like working for Sav?"
            goon "Like?"
            mS "You strike me as someone with flexible attitudes towards allegiance, not a true believer."
            show reginald stream surprised at stream_right5
            "Reginald begins to lower his blaster."
            goon "Go on."
            mS "What would it cost for you to get off world? I take it you have ambitions bigger than Gibian V?"
            "Reginald's brow furrows."
            goon "A couple grand I guess?"
            show jennica stream shock
            pS "A couple grand!?"
            $ AddChatter(vig2_sc7_mar_bribe_comment1)
            goon "I need to make it off world in one piece. Money don't spend if I'm dead."
            mS "We can afford that."
            play audio "bagSearch.wav" volume 1.0
            "I reach into my pocket and grab 2000 credits."
            show reginald stream impressed at stream_right5
            goon "Pleasure doing business."
            $ AddChatter(vig2_sc7_mar_bribe_comment2)
            "Reginald looks us over one more time before turning around and briskly leaving."
            $ reactTarget = "vig2_sc8_mar_reacttoregibribe"
            show screen streamerCommentary
            hide reginald with dissolve
            show jennica stream angry at stream_left
            pS "{i}Can{/i} we afford that?"
            mS "I hope so."
            show teresa stream upset at stream_right
            enS "We have bigger problems. Where are we to find someone to help us cover our tracks now?"
            show jennica stream neutral at stream_left
            "I notice MAC watching Reginald run away, lost in thought."
            hide screen streamerCommentary
    show data agent neutral at stream_center with move
    worker "I uh... Couldn't help but overhear your predicament..."
    show teresa stream think at stream_right
    enS "Eavesdropping are we?" 
    worker "You're holding me uh... hostage."
    mS "Yeah. Sorry about that. You were saying?"
    "The technician shifts around uneasily."
    worker "I might be able to help you."
    show teresa stream neutral at stream_right
    enS "Oh?"
    worker "I have some access to the BigCorp security database. Not as much as Matticus obviously, but I can get in and spread a few reports."
    pS "Well butter my biscuit!"
    mS "How do you have access? Sounds awfully convenient."
    worker "The Intergalactic Humanitarian Society has observer access to the database, to stay informed about pirates and solar storm sightings."
    $ AddChatter(vig2_sc7_mar_comment4)
    worker "Once I'm in, I just need to spoof the ID to make it look like I'm an ordinary security grunt."
    enS "Where did you learn how to do all of this?"
    "The technician continues to shift uneasily."
    worker "I... might use the Society's remote shipments to smuggle cargo."
    worker "The tariffs are insane! Matticus isn't exactly a free trade advocate."
    $ viewCheck9 += viewCount
    "This feels too good to be true."
    $ AddChatter(vig2_sc7_mar_comment5)
    mS "Why are you helping us?"
    if gunsBlazing == False:
        worker "You care enough about strangers from a small town to make an enemy out of Matticus."
        worker "You're obviously good people. And you risked your neck to spare all of my colleagues here."
        worker "I saw on the security cameras."
        "The technician smiles at me."
        $ AddChatter(vig2_sc7_mar_comment6)
    else:
        worker "What choice do I have!?"
        worker "You killed everyone here! I saw on the security cameras."
        "The technician sighs."
        worker "But you're better than Matticus. At least you refused to let all those people die of grey fever."
        $ AddChatter(vig2_sc7_mar_comment7)
        worker "Better the lesser evil."
    mS "Fair enough. So what do you need to do this?"
    $ AddChatter(vig2_sc7_mar_comment8)
    worker "I can do it right here. I just need your ship's registration code, planet of origin and operating name."
    enS "How can we know you're not going to betray us?"
    worker "You can't. You're going to have to trust me."
    show teresa stream think at stream_right
    enS "Worrisome."
    worker "Maybe, but you don't really have a choice."
    mS "He's not wrong. We burned the bridge with Matticus, this is our only option."
    pS "Can't look a gift horse in the mouth. For better or worse."
    "Teresa sighs in resignation."
    show teresa stream neutral at stream_right
    enS "Very well."
    worker "So we have a deal?"
    "I reach out and shake his hand."
    mS "Deal. Don't screw us."
    "The technician nods. He begins typing a series of commands into the computer."
    worker "Alright it should be set up. It'll begin sending in the reports once you're off world."
    mS "Great. Needless to say, we were never here."
    $ AddChatter(vig2_sc7_mar_comment9)
    "The technician smiles and winks at me."
    worker "I don't know who you're talking about. I wasn't even working that night!"
    stop music fadeout 8.0
    hide data with Dissolve(0.5)
    hide teresa with Dissolve(0.5)
    hide jennica with Dissolve(0.5)
    jump vig2epilogue_MAR

label commsBase_DataCenter_OUT():
    show jennica stream shock at stream_left
    pS "And let all those people die!?"
    enS "Thousands more will die as well if they get MAC."
    if shnzi == True:
        $ AddChatter(vig2_sc7_out_comment2_shnzi)
    else:
        $ AddChatter(vig2_sc7_out_comment2_AFK)
    mS "I don't like this any more than you do, Jen, but we're out of options."
    show jennica stream angry at stream_left
    pS "Damnit, Cap."
    $ AddChatter(vig2_sc7_out_comment3)
    $ AddChatter(vig2_sc7_out_comment4)
    $ vig2_sc7_out_comment1.click = False
    enS "If you have a better way to cover our trail do share. Please."
    "There's a long moment before Jennica answers." 
    pS "I thought we were tryin' to be better than this..."
    "Teresa turns away from her"
    $ AddChatter(vig2_sc7_out_comment5)
    mS "We can't do better if we're in jail, and considering how close we got last time..."
    mS "I can't lose you guys. You're all I've got."
    $ AddChatter(vig2_sc7_out_comment6)
    hide jennica with dissolve
    hide teresa with dissolve
    hide mac with dissolve
    show reginald stream neutral at stream_right5
    goon "Are we done with this yet?"
    goon "I ain't got all day."
    $ AddChatter(vig2_sc7_out_comment7)
    mS "Yeah. Lets get the tracking code and get out of here."
    $ AddChatter(vig2_sc7_out_comment8)
    goon "Good."
    $ AddChatter(vig2_sc7_out_comment9)
    "Reginald turns to the technician."
    $ AddChatter(vig2_sc7_out_comment10)
    show data agent scared at stream_left5
    show reginald stream mad at stream_right
    goon "I'm not going to ask nicely again. The tracking code, now."
    $ AddChatter(vig2_sc7_out_comment11)
    "The technician looks terrified as he clicks through the various menus on the computer."
    worker "44s-73f-94c-21o."
    show reginald stream impressed at stream_right5
    $ AddChatter(vig2_sc7_out_comment12)
    $ AddChatter(vig2_sc7_out_comment13)
    worker "You realise these people have nothing right?"
    $ AddChatter(vig2_sc7_out_comment14)
    $ AddChatter(vig2_sc7_out_comment15)
    show reginald at stream_left with move
    "Reginald walks past the technician as he logs the code into his agenda."
    goon "I don't get paid to realise things."
    $ AddChatter(vig2_sc7_out_comment16)
    $ AddChatter(vig2_sc7_out_comment17)
    $ AddChatter(vig2_sc7_out_comment18)
    show teresa stream neutral at stream_right
    enS "What do we do with him?"
    "Teresa gesture to the technician."
    if shnzi == True:
        $ AddChatter(vig2_sc7_out_comment19_shnzi)
    else:
        $ AddChatter(vig2_sc7_out_comment19_bacon)
    goon "I'll leave that to you. Meet me back at the shuttle."
    $ AddChatter(vig2_sc7_out_comment20)
    $ AddChatter(vig2_sc7_out_comment21)
    "Reginald walks out of the room."
    $ AddChatter(vig2_sc7_out_comment22)
    $ AddChatter(vig2_sc7_out_comment23)
    $ AddChatter(vig2_sc7_out_comment24)
    hide reginald with dissolve
    show jennica stream neutral at stream_left
    $ viewCheck9 += viewCount
    menu:
        "Reginald walks out of the room."
        "Convince him not to say anything.":
            $ technicianChoice = False
            $ macViolence += 1
            $ marshal += 1
            $ pdEngagement += 1
            $ csEngagement += 1
            $ kcEngagement += 1
            $ pilotApproval += 1
            $ engineerApproval += 1
            "We don't need to hurt him. Just need to make him think we will."
            mS "Look, it's in your best interest that you forget everything that happened here."
            $ AddChatter(vig2_sc7_out_coerce_comment1)
            worker "What?"
            mS "Spreading word of this around is just gonna make things more difficult."
            mS "For us..."
            $ AddChatter(vig2_sc7_out_coerce_comment2)
            "I pull out my blaster and slowly drag the muzzle across his chest."
            mS "And for you. We really don't want to have to come back and deal with you."
            $ AddChatter(vig2_sc7_out_coerce_comment3)
            mS "You don't want that either."
            "The technician is shaking, paralyzed with fear."
            $ AddChatter(vig2_sc7_out_coerce_comment4)
            mS "Do we understand each other?"
            worker "Yes! I won't breathe a word of this to anyone else!"
            mS "Glad to hear it. Let's move."
            hide data with dissolve
            show mac stream neutral at stream_center_mac with Dissolve(0.5)
            "MAC stares at the terrified technician."
            pS "Damn, Cap, that was dark."
            enS "If it works it works."
            hide teresa with dissolve
            hide jennica with dissolve
            mS "Come, MAC."
            "MAC begins to follow."
            hide mac with Dissolve(1.5)
        "Kill him.":
            $ technicianChoice = True
            $ macViolence += 2
            $ macPessimism += 1
            $ outlaw += 2
            $ pdEngagement += 2
            $ csEngagement -= 1
            $ kcEngagement -= 1
            $ pilotApproval -= 1
            $ engineerApproval += 1
            $ AddChatter(vig2_sc7_out_execute_comment1)
            "Only one way to make sure this never leaves the building."
            $ AddChatter(vig2_sc7_out_execute_comment2)
            "I raise my blaster up to the technician's face."
            $ AddChatter(vig2_sc7_out_execute_comment3)
            worker "Wait! You don't have to do—"
            play audio "lazer.wav" volume 5.0
            hide data with Dissolve(0.1)
            "The shot rings out. The technician's body slumps to the floor, lifeless."
            show jennica stream shock at stream_left
            show mac stream shock at stream_center_mac with Dissolve(1.0)
            pS "Damn, Cap. Reckon we killed enough today."
            pS "He really needed to die too?"
            $ AddChatter(vig2_sc7_out_execute_comment4)
            enS "Perhaps. But now we can be certain he won't expose us."
            play audio "macSad.wav" volume 1.0
            show mac stream neutral
            macS "Dead..."
            show jennica stream angry at stream_left
            mS "Enough blabbing. Lets go."
            hide teresa with dissolve
            hide jennica with dissolve
            "MAC continues to stare at the technician's corpse."
            mS "Come, MAC."
            $ vig2_sc7_out_execute_comment4.click = False
            "MAC begins to follow."
            hide mac with Dissolve(2.0)
    show vig2_targetbase_stream at topleft onlayer background with dissolve
    hide vig2_datacenter_stream
    show reginald stream neutral at stream_center with Dissolve(0.5)
    show teresa stream neutral at stream_right with dissolve
    show jennica stream angry at stream_left with dissolve
    "Reginald is waiting by the shuttle for us."
    $ reactTarget = "vig2_sc8_out_postchoice"
    show screen streamerCommentary
    goon "All sorted?"
    mS "Yeah. So how are we doing this?"
    goon "We need to make sure the shot can't be traced back to us."
    goon "We'll make the interception, and then ditch this shuttle in the desert."
    enS "How are we getting out of the desert?"
    goon "The boss has a crew waiting for us out there. They'll take care of the disposal."
    pS "And the firepower?"
    goon "This shuttle has a BigCorp missile loaded on it. When they try and trace it, it'll just lead back to their own factories."
    mS "Sounds simple enough."
    goon "Swell."
    hide screen streamerCommentary
    hide jennica with Dissolve(0.5)
    hide teresa with Dissolve(0.5)
    hide reginald with Dissolve(0.5)
    jump shuttleDestruction

label shuttleDestruction():
    show bg black topleft onlayer background with dissolve
    hide vig2_targetbase_stream 
    show vig2_orbit_stream at topleft onlayer background with Dissolve(0.7)
    show reginald stream neutral at stream_center with dissolve
    show jennica stream crossed at stream_left with dissolve
    show teresa stream neutral at stream_right with dissolve       
    "Once we're in low orbit, it's only a matter of time before the shuttle shows up."
    goon "You're sure we're in the right spot?"
    pS "Think I can't read a damn tracking code?"
    show reginald stream mad at stream_center
    goon "I think you don't want to."
    "Jennica scoffs."
    enS "My scanner says it's incoming."
    "Out of the corner of my eye, I see a small light approaching us."
    "An unmanned aid ship comes into view. It's small, barely larger than the shuttle."
    goon "That's it."
    $ AddChatter(vig2_sc7_out_comment25)
    mS "Alright, Jen."
    pS "Sure about this, Cap?"
    mS "Yeah. Hit it."
    $ AddChatter(vig2_sc7_out_comment26)
    "Jennica pulls the trigger."
    "A rush of momentum shakes the shuttle as the missile flies out from under it."
    $ reactTarget = "vig2_sc8_out_reflect"
    show screen streamerCommentary
    "The missile races across the sky before colliding with the ship, obliterating it."
    "Pieces of debris scatter from the site of impact."
    "Jennica sighs."
    $ AddChatter(vig2_sc7_out_comment27)
    pS "Hope this is worth it."
    hide screen streamerCommentary
    $ AddChatter(vig2_sc7_out_comment28)
    hide teresa with Dissolve(0.5)
    hide jennica with Dissolve(0.5)
    hide reginald with Dissolve(0.5)
    jump vig2epilogue_OUT

label vig2epilogue_MAR():
    play music "soundtrack/vig1scratchtrack.wav" volume 1.2
    show shiphub_stream at topleft onlayer background with dissolve
    hide vig2_datacenter_stream
    show teresa stream happy at stream_right with dissolve
    show jennica stream neutral at stream_left with dissolve  
    enS "Thank goodness that's over. If I never see Gibian V again it'll be too soon."
    $ reactTarget = "vig2_sc9_mar_end"
    show screen streamerCommentary
    $ AddChatter(vig2_epilogue_mar_comment1)
    pS "Couldn't agree more! Although it felt good sticking it to Matticus like that."
    pS "Wish I coulda seen his face..."
    $ AddChatter(vig2_epilogue_mar_comment2)
    "The meeting is interrupted by a ship intercom alert."
    play audio "callRing.wav" volume 1.5
    shipcom "Incoming call from Magistrate Savlian Matticus."
    mS "Be careful what you wish for."
    mS "Accept."
    hide screen streamerCommentary
    show matticus phone neutral at stream_center_mac with Dissolve(0.5)
    "Matticus appears on the ship computer. He's incensed."
    $ AddChatter(vig2_epilogue_mar_comment3)
    $ AddChatter(vig2_epilogue_mar_comment4)
    smatt "You idiots! You don't know how much you just screwed me."
    mS "Sorry Sav I'm picking up some bullshit on this line, what was that?"
    smatt "I should've known you didn't have the stomach for real work."
    $ AddChatter(vig2_epilogue_mar_comment5)
    mS "Real work like blowing up medicine for some bumpkins?"
    smatt "Since when do you care about anyone but yourself Moze!?"
    smatt "You've done worse. This wouldn't have even cracked your top ten!"
    mS "Is that it?"
    $ AddChatter(vig2_epilogue_mar_comment6)
    "I hear Jennica snicker behind me."
    smatt "Don't worry. You'll get yours. You think I got to where I am by letting people screw me over?"
    mS "Lose this channel Teresa."
    $ AddChatter(vig2_epilogue_mar_comment7)
    enS "With pleasure."
    play audio "cutCall.wav" volume 1.5
    hide matticus with dissolve
    $ viewCheck10 += viewCount
    "The screen powers off."
    pS "Maybe we shouldnta added insult to injury?"
    $ AddChatter(vig2_epilogue_mar_comment8)
    mS "Maybe. But didn't that feel good?"
    "Jennica smiles and chuckles warmly."
    pS "Like fresh underwear after a shower."
    mS "Alright, do you two have anything else to report?"
    enS "All systems are functional, Captain."
    pS "Steady as she goes, Cap."
    mS "Good. I'll be in my quarters."
    hide teresa with Dissolve(0.5)
    hide jennica with Dissolve(0.5)
    "I move to leave the briefing room when I feel a tug on my sleeve."
    show mac stream neutral at stream_center_mac with Dissolve(0.5)
    macS "May I ask a question?"
    mS "Of course MAC."
    macS "I'm confused about our mission? Why do we need to hide if we are good people?"
    menu:
        macS "I'm confused about our mission? Why do we need to hide if we are good people?"
        "The people in power are bad.":
            $ macHope += 2
            $ marshal += 1
            $ pdEngagement -= 1
            $ csEngagement += 1
            mS "Sometimes the people in power are bad, and to do good we need to hide from them."
            macS "But we broke the law many times. How can we be doing good by breaking the law?"
            mS "Laws aren't always good. Sometimes they're put in place by bad people."
            macS "But how do you know if a law is bad?"
            mS "That's up to you to decide. That's why we're outlaws. There's no one-size-fits-all rule."
            mS "The universe is just more complicated than that."
            macS "I see. The universe is confusing."
            mS "Agreed."
        "The universe is bad and we can't trust anyone.":
            $ macPessimism += 2
            $ outlaw += 1
            $ pdEngagement += 1
            $ kcEngagement += 1
            mS "The universe is a dangerous place. We can never know who's looking to stab us in the back."
            mS "Better to hide than risk that I'd say."
            macS "But we broke the law many times. How can we be good if we make the universe more dangerous?"
            mS "The universe was dangerous before us and it'll be the same after we're gone. Following the rules won't change that."
            mS "To change bad things, sometimes we have to do dangerous things."
            macS "I see. The universe is confusing."
            mS "Agreed."
    $ narrator = reg_narrator
    #$ macroNarration = True
    $ macroChoice = True
    $ AddChatter(vig2_epilogue_mar_comment9)
    hide mac with dissolve
    hide shiphub_stream with dissolve
    player "Wow..."
    player "Guess that's the end of the chapter, seems like a good spot to end."
    player "Alright everyone, thank you all for coming out! See ya next time!"
    "You quit out of the game and watch as the people in the chat discuss the stream."            
    $ AddChatter(vig2_epilogue_mar_comment10)
    pause 0.5
    $ AddChatter(vig2_epilogue_mar_comment11)
    pause 0.5
    $ AddChatter(vig2_epilogue_mar_comment12)
    pause 0.5
    $ vig2_marshalEpilogue = True
    $ vig2_outlawEpilogue = False
    "As the chat winds down, you take off your headset, and sign off of Flinch."
    hide screen streamChat
    hide screen streamDetails
    scene black with dissolve
    jump vig2_macro_start

label vig2epilogue_OUT():
    play music "soundtrack/vig1scratchtrack.wav" volume 1.2
    show shiphub_stream at topleft onlayer background with dissolve
    hide vig2_orbit_stream
    show teresa stream neutral at stream_right with dissolve
    show jennica stream neutral at stream_left with dissolve 
    $ AddChatter(vig2_epilogue_out_comment1)
    "The ship computer powers on."
    play audio "callRing.wav" volume 1.5
    shipcom "Incoming call from Magistrate Savlian Matticus."
    mS "Accept."
    $ AddChatter(vig2_epilogue_out_comment2)
    show matticus phone neutral at stream_center_mac with dissolve
    show jennica stream crossed
    "Matticus appears on the ship computer."
    smatt "Oh Moze. Its been so wonderful working with you again."
    smatt "We have to catch up some time!"
    "Jennica is visibly annoyed."
    mS "And your end of the deal?"
    $ AddChatter(vig2_epilogue_out_comment3)
    smatt "It's already done! As far as anyone else knows, the Oakley's doing a grand tour of the Mauritz nebula."
    $ AddChatter(vig2_epilogue_out_comment4)
    pS "Make damn sure he's not lying, Teresa."
    show teresa stream think
    "Teresa nods and begins typing on her computer."
    $ AddChatter(vig2_epilogue_out_comment5)
    smatt "Oh, Jenn. You're a real ice queen."
    smatt "So cold."
    "Matticus mimes himself shivering."
    $ AddChatter(vig2_epilogue_out_comment6)
    enS "It's true. Our logged coordinates are on the other side of the galaxy right now."
    smatt "See? I would never deceive you guys. We old Snakehawks need to look out for each other."
    "Jennica rolls her eyes."
    smatt "Alright, now that our business has concluded, I'm going to have a drink."
    smatt "Let me know when you're done playing hero with the robot, Moze. I've got lots more work where that came from."
    $ AddChatter(vig2_epilogue_out_comment7)
    mS "Goodbye, Sav."
    smatt "Think about it."
    $ AddChatter(vig2_epilogue_out_comment8)
    "Matticus winks before the screen powers off."
    $ reactTarget = "vig2_sc9_out_end"
    show screen streamerCommentary
    play audio "cutCall.wav" volume 1.5
    hide matticus with dissolve
    $ viewCheck10 += viewCount
    show teresa stream neutral
    enS "Well at least we have some breathing room."
    $ AddChatter(vig2_epilogue_out_comment9)
    enS "Deadeye won't trouble us for the foreseeable future."
    show jennica stream neutral
    pS "I suppose. I doubt the Ama we ran with'll chase red herrings for long though."
    $ AddChatter(vig2_epilogue_out_comment10)
    mS "Agreed. We ought to keep an eye out."
    $ vig2_epilogue_out_comment6.click = False
    hide screen streamerCommentary
    mS "Anything else to report?"
    enS "All systems are functional, Captain."
    pS "Steady as she goes, Cap."
    $ AddChatter(vig2_epilogue_out_comment11)
    mS "Good. I'll be in my quarters."
    hide jennica stream neutral with dissolve
    hide teresa with dissolve
    "I move to leave the briefing room when I feel a tug on my sleeve."
    if baseGuardKilled == True:
        $ AddChatter(vig2_epilogue_out_comment12)
        $ AddChatter(vig2_epilogue_out_comment13)
    show mac stream neutral at stream_center_mac with Dissolve(0.5)
    macS "May I ask a question?"
    mS "Of course, MAC."
    play audio "macGrumble.wav" volume 1.5
    macS "I don't know how to feel about our mission. Why did we need to help the skeeve Matticus?"
    $ AddChatter(vig2_epilogue_out_comment14)
    menu:
        macS "I don't know how to feel about our mission. Why did we need to help the skeeve Matticus?"
        "Doing bad things now can let us do good things later.":
            $ macHope += 2
            $ outlaw += 2
            $ pdEngagement += 2
            $ csEngagement -= 2
            $ kcEngagement += 1
            mS "Sometimes we have to do bad things so that we can do better things later."
            macS "But we hurt innocent people. Doesn't that make us skeeves?"
            $ AddChatter(vig2_epilogue_out_comment15)
            mS "It's more complicated than that. Sometimes skeeves do good things, and sometimes non-skeeves do bad things."
            mS "There's no one-size-fits-all rule."
            $ AddChatter(vig2_epilogue_out_comment16)
            mS "If we didn't help Matticus, we might've gotten caught. And then a lot more innocent people would be hurt."
            macS "I see. The universe is confusing."
            $ AddChatter(vig2_epilogue_out_comment17)
            mS "Agreed."
        "The universe is bad and we can't trust anyone.":
            $ macPessimism += 1
            $ outlaw += 1
            $ pdEngagement += 2
            $ csEngagement += 1
            $ kcEngagement += 1
            mS "The universe is a dangerous place. We can never know who's looking to stab us in the back."
            mS "Better to hide than risk that I'd say."
            $ AddChatter(vig2_epilogue_out_comment15)
            macS "But we broke the law many times. How can we be good if we make the universe more dangerous?"
            mS "The universe was dangerous before us and it'll be the same after we're gone. Following the rules won't change that."
            $ AddChatter(vig2_epilogue_out_comment16)
            mS "To change bad things, sometimes we have to do dangerous things."
            macS "I see. The universe is confusing."
            $ AddChatter(vig2_epilogue_out_comment17)
            mS "Agreed."
    $ narrator = reg_narrator
    #$ macroNarration = True
    $ macroChoice = True
    $ AddChatter(vig2_epilogue_out_comment18)
    hide mac with dissolve
    hide shiphub_stream with dissolve
    player "Wow..."
    player "Guess that's the end of the chapter, seems like a good spot to end."
    $ AddChatter(vig2_epilogue_out_comment19)
    player "Alright everyone, thank you all for coming out! See ya next time!"
    "You quit out of the game and watch as the people in the chat discuss the stream."
    pause 0.5
    $ AddChatter(vig2_epilogue_out_comment20)
    pause 0.5
    $ AddChatter(vig2_epilogue_out_comment21)
    pause 0.5
    $ AddChatter(vig2_epilogue_out_comment22)
    pause 0.5
    $ AddChatter(vig2_epilogue_out_comment23)
    pause 0.5
    $ AddChatter(vig2_epilogue_out_comment24)
    pause 0.5
    $ AddChatter(vig2_epilogue_out_comment25)
    pause 0.5
    $ AddChatter(vig2_epilogue_out_comment26)
    pause 0.5
    $ AddChatter(vig2_epilogue_out_comment27)
    $ vig2_outlawEpilogue = True
    $ vig2_marshalEpilogue = False
    stop music fadeout 6.0
    "As the chat winds down, you take off your headset, and sign off of Flinch."
    hide screen streamChat
    hide screen streamDetails
    scene black with dissolve
    jump vig2_macro_start


#### MACRO GAME #######
label vig2_macro_start():
    $ vignette2 = True
    if csEngagement > pdEngagement and csEngagement > kcEngagement:
        $ topfan = "Coriolis"
    elif kcEngagement > pdEngagement and kcEngagement >= csEngagement:
        $ topfan = "kitcat"
    elif pdEngagement >= kcEngagement and pdEngagement >= csEngagement:
        $ topfan = "pickledDragons"
    else:
        $ topfan = "Coriolis"
    play music "soundtrack/postStreamGroove.wav" volume 0.8 loop fadein 2.0
    $ narrator = reg_narrator
    #$ macroNarration = True
    $ macroChoice = True
    "You lean back in your chair and let your body relax now that you're no longer on camera."
    $ renpy.sound.play("audio/ReceiveText.ogg")
    "Then you get a Loop'd notification."
    scene streamview with dissolve
    "It's from Jessie."
    "You should see what they have to say, and check on Flinch and Blueit."
    $ screenComplete = True
    call screen webNavigation_vig2
    jump vig2_macro_modStart

label vig2_macro_modStart():
    scene discordview with dissolve
    $ screenComplete = False
    $ loopdView = True
    $ menu = nvl_menu
    mod_nvl "Hey, great stream again, so glad you decided to keep going with the game!"
    mod_nvl "How're you holding up?"
    if vig2_outlawEpilogue == True:
        mod_nvl "The chat got really excited by diving into the Outlaw stuff"
        if outlaw >= marshal:
            mod_nvl "And you seemed pretty into it too!"
        else:
            mod_nvl "You seemed a bit on the fence tho"
        jump vig2_macro_mod_outlaw1
    else:
        mod_nvl "Seemed like you had to manage the chat a bit this time around"
        if outlaw >= marshal:
            mod_nvl "They were pretty hype about the Outlaw choices even though you went Marshal at the end"
        else:
            mod_nvl "It was cool to see you stick to your guns tho"
        jump vig2_macro_mod_marshal1

###Labels for the Outlaw playthrough###
label vig2_macro_mod_outlaw1():
    menu:
        "•The stream is fun!":
            $ enthusiasm += 1
            player_nvl "Yeah, the stream feels really good!"
            jump vig2_macro_mod_outlaw2_enthusiastic
        "•Not feeling great.":
            $ reluctance += 1
            player_nvl "Honestly, I'm not feelin so great about it"
            jump vig2_macro_mod_outlaw2_reluctant
        "•Kind of mixed.":
            player_nvl "I'm ok? Idk, it's complicated"
            jump vig2_macro_mod_outlaw2_reluctant

label vig2_macro_mod_outlaw2_enthusiastic():
    mod_nvl "Amazing!"
    mod_nvl "How does it feel being the bad guy this time ;)"
    menu:
        "•It's fun!":
            $ enthusiasm += 2
            player_nvl "Surprisingly really fun!"
            jump vig2_macro_mod_outlaw3_enthusiastic
        "•Hard but enjoyable.":
            $ enthusiasm += 1
            player_nvl "It's a little tough cause it's not my usual style, but it's cool!"
            jump vig2_macro_mod_outlaw3_enthusiastic
        "•Odd...":
            $ reluctance += 1
            player_nvl "That part's feelin kinda weird, I'm thinking of switching things up honestly"
            jump vig2_macro_mod_outlaw3_reluctant

label vig2_macro_mod_outlaw2_reluctant():
    mod_nvl "Oh? What's up? Talk to me"
    menu:
        "•The choices are starting to weigh on me.":
            player_nvl "I feel really good about the response from the stream, but the choices are starting to weigh on me a bit"
            jump vig2_macro_mod_outlaw3_reluctant
        "•It's exhausting.":
            $ energy -= 1
            player_nvl "It's really cool that I get to see more of the story, but it's real tiring to play"
            jump vig2_macro_mod_outlaw3_reluctant

label vig2_macro_mod_outlaw3_enthusiastic():
    mod_nvl "Great to hear!"
    mod_nvl "I thought I saw a sly smile when you chose to ally with Savlian haha"
    menu:
        "•That got the chat going.":
            $ curiosity = False
            player_nvl "Omg the chant went WILD at that part!"
            player_nvl "So fun!"
            jump vig2_macro_mod_outlawEnd
        "•It was a cool side of the story.":
            $ curiosity = True
            player_nvl "The different story paths are crazy!"
            player_nvl "I never realized how different they could feel"
            jump vig2_macro_mod_outlawEnd
        "•I was so stressed at that part.":
            $ reluctance += 1
            player_nvl "Really?"
            player_nvl "Honestly, I was so stressed out making that choice"
            mod_nvl "Huh, I couldn't tell"
            mod_nvl "Way to play it off!"
            jump vig2_macro_mod_outlawEnd

label vig2_macro_mod_outlaw3_reluctant():
    mod_nvl "For sure, that makes sense"
    mod_nvl "I could kind of tell you weren't really into doing Savlian's dirty work"
    menu:
        "•It was what the stream wanted.":
            $ curiosity = False
            player_nvl "That obvious?"
            player_nvl "Yeah, I guess I went that route cause it seemed like what the stream wanted"
            jump vig2_macro_mod_outlaw4_reluctant
        "•I was trying to role play.":
            $ curiosity = False
            player_nvl "Tbh, I had to disassociate from that one a bit"
            player_nvl "I thought of Moze as 'Outlaw Moze'"
            player_nvl "So I wasn't really doing what like I would do in that position"
            menu:
                "•It was cool.":
                    player_nvl "It was cool actually"
                    jump vig2_macro_mod_outlaw4_reluctant
                "•It felt a little weird.":
                    player_nvl "Kind of a weird 'out of body' sensation"
                    jump vig2_macro_mod_outlaw4_reluctant
        "•I liked seeing another side of the story":
            $ curiosity = True
            player_nvl "It didn't feel great"
            player_nvl "But it was interesting to see a different spin on the story"
            player_nvl "Never really seen that side of Moze before"
            jump vig2_macro_mod_outlaw4_reluctant
        "•That didn't really bother me.":
            $ enthusiasm += 1
            player_nvl "Really?"
            player_nvl "That felt fine actually"
            jump vig2_macro_mod_outlaw4_reluctant

label vig2_macro_mod_outlaw4_reluctant():
    mod_nvl "So you thinking of changing it up?"
    menu:
        "•Yeah, Marshal feels more right.":
            $ reluctance += 2
            player_nvl "Yeah I am"
            player_nvl "Marshal just feels more fun for me"
            jump vig2_macro_mod_outlawEnd
        "•Maybe.":
            $ reluctance += 1
            player_nvl "It's not a big deal, really"
            player_nvl "But it does take a lot out of me. So maybe I'll pivot"
            jump vig2_macro_mod_outlawEnd
        "•No, this is a good path to Affiliate.":
            $ enthusiasm += 1
            player_nvl "No, I think this is still the best way to get Affiliate"
            player_nvl "It's keeping me going tbh"
            jump vig2_macro_mod_outlawEnd

label vig2_macro_mod_outlawEnd():
    mod_nvl "Well you have this momentum now, and the audience does seem to like when you play Outlaw"
    mod_nvl "But it's your stream y'know"
    mod_nvl "If you're feeling good, then keep it going!"
    mod_nvl "If not then don't"
    mod_nvl "I got your back, whatever you choose!"
    menu:
        "•Thanks.":
            player_nvl "Thanks, I appreciate it"
    mod_nvl "Np."
    mod_nvl "Gotta run, gonna go grab some pho with a friend, chat later ya?"
    player_nvl "For sure, enjoy!"
    #$ blueitPages = [] #this line can be deleted eventually. It's here temporarily to make testing a bit easier.
    #$ blueitPages.append(vig2_bThread1)
    #$ blueitPages.append(vig2_bThread2)
    #$ blueitPages.append(vig2_bThread3)
    #$ blueitPages.append(vig2_bThread4)
    $ screenComplete = True
    call screen webNavigation_vig2
    scene bg black with dissolve
    #jump blueitVignette2_1


###Labels for Marshal playthrough###
label vig2_macro_mod_marshal1():
    menu:
        "•Stream felt good.":
            $ reluctance += 1
            player_nvl "Yeah it was a bit hectic"
            player_nvl "But I really like where the stream is at!"
            jump vig2_macro_mod_marshal2_reluctant
        "•A bit confused.":
            $ enthusiasm += 1
            player_nvl "Honestly, I feel kinda confused"
            jump vig2_macro_mod_marshal2_enthusiastic
        "•Complicated.":
            player_nvl "I'm ok?"
            player_nvl "Idk, it's complicated"
            jump vig2_macro_mod_marshal2_enthusiastic

label vig2_macro_mod_marshal2_reluctant():
    mod_nvl "Hell yeah!"
    mod_nvl "Going back to Marshal felt like the right call then?"
    menu:
        "•Definitely, it felt good.":
            $ reluctance += 2
            player_nvl "Definitely, it just feels more right to me"
            jump vig2_macro_mod_marshal3_reluctant
        "•Pretty much, chat seemed nicer.":
            $ reluctance += 1
            player_nvl "Yeah, I think the vibes in chat are better for it"
            jump vig2_macro_mod_marshal3_reluctant
        "•I'm not so sure, actually.":
            $ enthusiasm += 1
            player_nvl "Actually, I'm not so sure" 
            player_nvl "I kinda miss the excitement of the Outlaw style"
            jump vig2_macro_mod_marshal3_enthusiastic

label vig2_macro_mod_marshal2_enthusiastic():
    mod_nvl "Oh? What's up? Talk to me."
    menu:
        "•Stream doesn't seem as entertained.":
            player_nvl "It's like..."
            player_nvl "I definitely prefer player Marshal. But I feel like that's not what the stream wants to see"
            jump vig2_macro_mod_marshal3_enthusiastic
        "•The story felt predictable":
            player_nvl "I don't know"
            player_nvl "The story felt a little predictable. Like I'd seen it before"
            jump vig2_macro_mod_marshal3_enthusiastic

label vig2_macro_mod_marshal3_enthusiastic():
    mod_nvl "No that makes sense"
    mod_nvl "You did seem to take longer than usual to ally with that humanitarian group"
    menu:
        "•I second-guessed myself a bit.":
            player_nvl "That obvious?"
            player_nvl "I guess I kind of second-guessed myself there"
            jump vig2_macro_mod_marshal4_enthusiastic
        "•Had to check in with chat.":
            $ curiosity = False
            player_nvl "Yea, I needed some time to take stock of the chat"
            jump vig2_macro_mod_marshal4_enthusiastic
        "•I was considering the Outlaw choice.":
            $ curiosity = True
            player_nvl "I was open to going Outlaw, but I liked the arguments for Marshal better"
            jump vig2_macro_mod_marshal4_enthusiastic
        "•I didn't notice.":
            player_nvl "Really? That felt fine actually"
            jump vig2_macro_mod_marshal4_enthusiastic

label vig2_macro_mod_marshal3_reluctant():
    mod_nvl "Great to hear!"
    mod_nvl "You seemed pretty stoked to betray Matticus"
    menu:
        "•I felt good energy from chat with that.":
            $ curiosity = False
            player_nvl "Honestly, that was mostly talking through the choice with chat"
            jump vig2_macro_mod_marshalEnd
        "•Definitely, I wonder about the Outlaw choice.":
            $ curiosity = True
            player_nvl "100\% the right move"
            player_nvl "I do wonder what would've happened if I went Outlaw there tho"
            jump vig2_macro_mod_marshalEnd
        "•I was kind of stressed.":
            player_nvl "Really?"
            player_nvl "Honestly, I was so stressed out making that choice"
            mod_nvl "Huh, I couldn't tell"
            mod_nvl "Way to play it off!"
            jump vig2_macro_mod_marshalEnd

label vig2_macro_mod_marshal4_enthusiastic():
    mod_nvl "So you thinking of changing it up?"
    menu:
        "•Yeah, Outlaw's good for viewers.":
            $ enthusiasm += 1
            player_nvl "Yeah, it kinda feels like I should try Outlaw again"
            player_nvl "May be the best shot to get Affiliate?"
            jump vig2_macro_mod_marshalEnd
        "•Maybe.":
            $ reluctance += 1
            player_nvl "Maybe?"
            player_nvl "I'm still not sure"
            jump vig2_macro_mod_marshalEnd
        "•No, Marshal feels right.":
            $ reluctance += 2
            player_nvl "No. Even if Outlaw gets more views, this still feels right to me"
            jump vig2_macro_mod_marshalEnd

label vig2_macro_mod_marshalEnd():
    mod_nvl "Well the audience does seem to like when you play Outlaw, but there's still some Marshal fans out there too"
    mod_nvl "It's your stream tho"
    mod_nvl "If you're feeling good, then keep it going!"
    mod_nvl "If not then change it up!"
    mod_nvl "I got your back, whatever you choose"            
    menu:
        "•Thanks.":
            player_nvl "Thanks, I appreciate it"
    mod_nvl "Np"
    mod_nvl "Gotta run, gonna go grab some fried rice with a friend"
    mod_nvl "Chat later, ya?"
    player_nvl "For sure, enjoy!"
    $ screenComplete = True
    call screen webNavigation_vig2
    scene bg black with dissolve
    #jump blueitVignette2_1

###label for blueit
label blueitVignette2_1:
    $ menu = adv_menu
    scene blueit_v2screen at truecenter with dissolve
    $ screenComplete = False
    $ blueitView = True
    $ blueitPages = [] #this line can be deleted eventually. It's here temporarily to make testing a bit easier.
    $ blueitPages.append(vig2_bThread1)
    $ blueitPages.append(vig2_bThread2)
    $ blueitPages.append(vig2_bThread3)
    $ blueitPages.append(vig2_bThread4)
    "You go to check out the subblueit to see how people are reacting to Episode 2."
    jump blueitVignette2_2
    
label blueitVignette2_2():
    scene blueit_v2screen at truecenter
    show screen webNavigation_vig2
    if blueitChoiceCheck == True:
        $ screenComplete = True
    else:
        pass
    call screen blueit
    return
    jump vig2_macro_viewerChat_1

label FlinchAnalytics_vig2():
    $ menu = adv_menu
    $ screenComplete = False
    $ flinchView = True
    "You should probably check out Flinch's analytics page."
    $ flinchCheck = 0
    show screen webNavigation_vig2
    scene flinch_v2screen with dissolve
    #The six lines below this allow us to change who the topfan is
    #if csEngagement >= kcEngagement and csEngagement >= pdEngagement:
    #    $ topfan = "Coriolis"
    #elif kcEngagement > csEngagement and kcEngagement > pdEngagement:
    #    $ topfan = "kitcat"
    #else:
    #    $ topfan = "pickledDragons"
    #For this particular vignette though, we want it to be Coriolis
    $ followerGoal = 2
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
    show screen viewershipButton_vig2
    call screen streamAnalytics_vig2
    hide screen streamAnalytics_vig2 with dissolve

label vig2_macro_viewerChat_1():
    nvl clear
    $ menu = nvl_menu
    hide screen viewershipButton_vig2
    scene bg black
    $ renpy.sound.play("audio/ReceiveText.ogg")
    "You're about to move away from your computer when you hear another notification."
    scene discordview with dissolve
    if csEngagement > pdEngagement and csEngagement > kcEngagement:
        "It's Coriolis?"
        cs_nvl "Hey [username], that was such a cool stream!"
        if gunsBlazing == True:
            cs_nvl "It was fun to see you go out of your comfort zone and be a bit chaotic"
            cs_nvl "Honestly, I wasn't expecting to have as much fun with it as I did haha"
            cs_nvl "Anyway, thanks for the stream!"
            $ playerNVLNarration = "Coriolis is so nice. Should I respond?"
            show screen NVLnarration
            menu:
                "•You haven't seen anything yet.":
                    hide screen NVLnarration
                    $ enthusiasm += 1
                    player_nvl "Well get ready for more chaos!"
                    player_nvl "Outlaws on the loose!"
                "•Thank you.":
                    hide screen NVLnarration
                    $ csEngagement += 1
                    player_nvl "Thanks, Coriolis"
                    player_nvl "It means a lot to have you in the chat!"
                    cs_nvl "Aww, thanks [username]!"
                "•Don't respond.":
                    hide screen NVLnarration
                    $ csEngagement -= 2
                    "Nah, don't really want to encourage a parasocial relationship."
        else:
            cs_nvl "I liked that stealth run on the base"
            cs_nvl "It felt really tense"
            if vig2_outlawEpilogue == True:
                cs_nvl "I was surprised by siding with Matticus at the end, though"
                cs_nvl "But I get it, tough to weigh the safety of MAC and the wider galaxy in that moment"
            else:
                cs_nvl "And I was stoked to see you side against the 'skeeve' Matticus haha"
            cs_nvl "Anyway, thanks for the stream!"
            $ playerNVLNarration = "Coriolis is so nice. Should I respond?"
            show screen NVLnarration
            menu:
                "•It was tough balancing both Outlaw and Marshal." if vig2_outlawEpilogue == True:
                    hide screen NVLnarration
                    $ reluctance += 1
                    player_nvl "Yeah, it was tough balancing the two styles"
                    player_nvl "Moze being both an Outlaw thief and a captain with Morals is interesting"
                    cs_nvl "Totally"
                    cs_nvl "Glad I don't have to be in that position haha"
                "•Good to go back to basics." if vig2_outlawEpilogue == False:
                    hide screen NVLnarration
                    $ reluctance += 1
                    player_nvl "Yeah, I wanted to go back to basics"
                    player_nvl "Get into some outlaw thievery vibes"
                    cs_nvl "It was fun to see those vibes back!"
                "•I'm glad you're liking it.":
                    hide screen NVLnarration
                    $ csEngagement += 1
                    player_nvl "Thanks, Coriolis"
                    player_nvl "It means a lot to have you in the chat!"
                    cs_nvl "Aww, thanks [player]!"
                "•Don't respond.":
                    hide screen NVLnarration
                    $ csEngagement -= 2
                    "Nah, don't really want to encourage a parasocial relationship."
        jump vig2_macro_bro1


    elif kcEngagement > pdEngagement and kcEngagement >= csEngagement:
        "It's kitcat?"
        kc_nvl "[username], hi! How's it goin!"
        kc_nvl "Sry to message randomly, hope it's not weird"
        kc_nvl "But I have to ask about your romance path"
        kc_nvl "I wanna read the tea leaves of your soul!"
        kc_nvl "jk, sort of, anyway"
        if romanceAma == True:
            kc_nvl "Ama. Great pick! Honestly, I didn't even think about that"
            kc_nvl "Do you think it's an actual path the devs made?"
            kc_nvl "Or are you just fanshipping this vibe hard?"
            $ playerNVLNarration = "Woah, kitcat's a little intense. Should I respond?"
            show screen NVLnarration
            menu:
                "•I think it'll be a choice.":
                    hide screen NVLnarration
                    $ kcEngagement += 1
                    player_nvl "No I think they'll give you that option"
                    player_nvl "I mean, the drama is right there"
                    player_nvl "And I get more of a family vibe from the other crew members"
                    kc_nvl "icic"
                    kc_nvl "Great catch there! They should hire you to write on the next game!"
                "•Just a fan theory tbh.":
                    hide screen NVLnarration
                    $ kcEngagement += 1
                    player_nvl "It's just a fan ship"
                    player_nvl "Ama's probably not in the game enough for that to make sense"
                    kc_nvl "Yeah, you're probably right"
                    kc_nvl "It's a great idea though, they should hire you to write on the next one!"
                "•Don't respond.":
                    hide screen NVLnarration
                    $ kcEngagement -=3
                    "Nah, don't really want to encourage a parasocial relationship."
        elif romanceTeresa == True:
            kc_nvl "Ok, so Teresa, I'm into this"
            kc_nvl "I feel like Jennica's the dev-intended romance"
            kc_nvl "And I just think the tension with Teresa is more interesting, no?"
            $ playerNVLNarration = "Woah, kitcat's a little intense. Should I respond?"
            show screen NVLnarration           
            menu:
                '•Totally agree.':
                    hide screen NVLnarration
                    $ kcEngagement += 2
                    player_nvl "100\% agree"
                    player_nvl "Jennica's sweet, but I think the connection with Teresa feels more real"
                    player_nvl "Probably because there's more tension there"
                    kc_nvl "Exactly!"
                    kc_nvl "I knew you'd get it"
                "•IDK, seemed fun.":
                    hide screen NVLnarration
                    $ kcEngagement += 1
                    player_nvl "I dunno, I didn't think about it too much"
                    player_nvl "Guess I just feel it more with Teresa?"
                    kc_nvl "Ah ic, more just an intuition thing"
                    kc_nvl "I can respect that"
                "•Don't respond.":
                    hide screen NVLnarration
                    $ kcEngagement -=5
                    "Nah, don't really want to encourage a parasocial relationship."
        elif romanceJennica == True:
            kc_nvl "Ok, so, Jennica. What's the deal with that?"
            kc_nvl "Like, I see people fawning over her online and..."
            kc_nvl "idk, she just feels like the dev canon romance to me, which just seems kinda uninteresting"
            $ playerNVLNarration = "Woah, kitcat's a little intense. Should I respond?"
            show screen NVLnarration
            menu:
                '•Yes, but that\'s what makes it good.':
                    hide screen NVLnarration
                    $ kcEngagement += 2
                    player_nvl "That's kind of the thing though"
                    player_nvl "I don't really buy a romance path with Teresa"
                    player_nvl "Even though it's more \'on rails\' I guess, the Jennica romance just feels more real"
                    player_nvl "There's more there because the devs spent more time on it"
                    kc_nvl "mmmm true. It does feel like Teresa doesn\'t always get a lot of shine"
                    kc_nvl "I'm into the maximize content view. Makes sense!"
                "•IDK, seemed fun.":
                    hide screen NVLnarration
                    player_nvl "I dunno, I didn't think about it too much"
                    player_nvl "Guess I just feel it more with Jennica?"
                    kc_nvl "Ah ic, more just an intuition thing"
                    kc_nvl "I can respect that"
                "•Don\'t respond.":
                    hide screen NVLnarration
                    $ kcEngagement -=5
                    "Nah, don't really want to encourage a parasocial relationship."
        else:
            kc_nvl "Who are you thinking of romancing? You didn't say during stream"
            kc_nvl "I feel like Jennica is canon, but Teresa's compelling too"
            $ playerNVLNarration = "Woah, kitcat's a little intense. Should I respond?"
            show screen NVLnarration
            menu:
                "•I'm thinking Jennica.":
                    hide screen NVLnarration
                    player_nvl "Jennica's sweet, I'm leaning her at the moment!"
                    $ romanceJennica = True
                    $ romanceTeresa = False
                    $ romanceAma = False
                    kc_nvl "Sure sure"
                    kc_nvl "Can't go wrong with the dev-authored path"
                "•Probably Teresa.":
                    hide screen NVLnarration
                    $ kcEngagement += 2
                    player_nvl "Teresa for sure. She's got an edge I appreciate"
                    kc_nvl "Yes!"
                    kc_nvl "I'm also into the crazy engineer!"
                "•Ama all day, for sure.":
                    hide screen NVLnarration
                    $ kcEngagement += 3
                    player_nvl "Actually, I'm holding out that there will be an Ama romance path"
                    $ romanceAma = True
                    $ romanceTeresa = False
                    $ romanceJennica = False
                    kc_nvl "Oh WOW I hadn't even thought that they would do that"
                    kc_nvl "Gotta go scour some forums for thoughts on that ship!"
                "•Don\'t respond.":
                    hide screen NVLnarration
                    $ kcEngagement -=5
                    "Nah, don't really want to encourage a parasocial relationship."
        jump vig2_macro_bro1


    elif pdEngagement >= kcEngagement and pdEngagement >= csEngagement:
        "It's PickledDragons?"
        pd_nvl "Hey [username], hope this isn't weird. Just wanted to share some thoughts on the stream"
        if gunsBlazing == True and vig2_outlawEpilogue == True:
            pd_nvl "I appreciate how you leaned into the edginess of these characters"
            pd_nvl "And I hope it's not weird what I'm typing into chat"
            pd_nvl "I just feel like...these are supposed to be outlaws"
            pd_nvl "If they only ever make \"good guy\" type decisions, they kind of become less interesting characters"
            pd_nvl "Like, to believe that Moze is going to grow as a character, we have to see some of that internal tension"
            pd_nvl "I've been on the fence with this game, but you're making me think about picking it up!"
            $ playerNVLNarration = "Interesting thoughts from PickledDragons. Should I respond?"
            show screen NVLnarration
            menu:
                "•100\% agree, these are complex characters.":
                    hide screen NVLnarration
                    $ pdEngagement += 2
                    player_nvl "Completely agree, I think the Outlaw path shows the character nuances more"
                    player_nvl "I was all Marshal before this, but it's been a really compelling experience"
                    pd_nvl "Well, glad I caught when you made the switch!"
                    pd_nvl "Looking forward to the next stream!"
                "•That's more thought than I put in tbh.":
                    hide screen NVLnarration
                    $ pdEngagement += 1
                    player_nvl "Honestly, that's more thought than I put in haha"
                    player_nvl "I'm kinda just going by feel"
                    pd_nvl "For sure, nothing wrong with flying by the seat of your pants!"
                "•Don't respond.":
                    hide screen NVLnarration
                    $ pdEngagement -= 1
                    "Nah, don't really want to encourage a parasocial relationship."
        elif gunsBlazing == True and vig2_outlawEpilogue == False:
            pd_nvl "I appreciate how you're playing around with the edginess of these characters"
            pd_nvl "I just feel like...these are supposed to be outlaws"
            pd_nvl "If they only ever make \"good guy\" type decisions, they kind of become less interesting characters"
            pd_nvl "I like the blend you're going with here. Curious if you'll keep it up?"
            $ playerNVLNarration = "Interesting thoughts from PickledDragons. Should I respond?"
            show screen NVLnarration
            menu:
                "•I'm digging the outlaw vibe.":
                    hide screen NVLnarration
                    $ pdEngagement += 2
                    $ promisedPDOutlaw = True
                    player_nvl "Completely agree, I think the Outlaw path shows the character nuances more"
                    player_nvl "I was all Marshal before this, but it's been a really compelling experience"
                    pd_nvl "Well, glad I caught when you made the switch!"
                "•Most decisions are spontaneous.":
                    hide screen NVLnarration
                    player_nvl "Honestly, that's more thought than I put in haha"
                    player_nvl "I'm kinda just going by feel"
                    player_nvl "So maybe it's still a blend, maybe it changes"
                    player_nvl "Gotta see what the Galaxy throws at us!"
                    pd_nvl "For sure, nothing wrong with flying by the seat of your pants!"
                "•Don't respond.":
                    hide screen NVLnarration
                    $ pdEngagement -= 1
                    "Nah, don't really want to encourage a parasocial relationship."
        elif gunsBlazing == False and vig2_outlawEpilogue == True:
            pd_nvl "I was really surprised by the choice you made at the end, shooting down the aid ship"
            pd_nvl "Quite the pivot from the quiet infiltration, but very interesting!"
            pd_nvl "I just feel like...these are supposed to be outlaws"
            pd_nvl "If they only ever make \"good guy\" type decisions, they kind of become less interesting characters"
            pd_nvl "Just curious how you see it?"
            $ playerNVLNarration = "Interesting thoughts from PickledDragons. Should I respond?"
            show screen NVLnarration
            menu:
                "•It's all complicated.":
                    hide screen NVLnarration
                    $ pdEngagement += 4
                    player_nvl "I think it's hard to say one way or the other"
                    player_nvl "I was all Marshal before this, but it's been really compelling to do some outlaw stuff"
                    player_nvl "Sometimes it makes sense for the characters to go that route. Sometimes it doesn't"
                    player_nvl "That's what makes the game interesting imo"
                    pd_nvl "100\% agree"
                    pd_nvl "I typically go all outlaw in games"
                    pd_nvl "But maybe the characters will feel more compelling if I sprinkle some marshal in there too"
                    pd_nvl "Thx for the quick chat!"
                "•Most decisions are spontaneous.":
                    hide screen NVLnarration
                    player_nvl "Honestly, that's more thought than I put in haha"
                    player_nvl "I'm kinda just going by feel"
                    player_nvl "The blend is cool, but it depends on how I'm feeling each day"
                    player_nvl "Gotta see what the Galaxy throws at us!"
                    pd_nvl "For sure, nothing wrong with flying by the seat of your pants!"
                "•Don't respond.":
                    hide screen NVLnarration
                    $ pdEngagement -= 1
                    "Nah, don't really want to encourage a parasocial relationship."
        else:
            pd_nvl "I really like your stream"
            pd_nvl "The energy in chat is great, you're fun to watch"
            pd_nvl "Even though you go Marshal most of the time, I'm still having a good time"
            pd_nvl "Ordinarily I go all for the Outlaw routes"
            pd_nvl "So I just wanted to say kudos for making Marshal so entertaining!"
            $ playerNVLNarration = "Some thoughtful messages from PickledDragons. Should I respond?"
            show screen NVLnarration
            menu:
                "•I feel good with Marshal.":
                    hide screen NVLnarration
                    player_nvl "Thanks!"
                    player_nvl "Marshal's for sure my comfort zone. Been playing with outlaw stuff"
                    player_nvl "but I think the stream is better when I'm on the Marshal path"
                    pd_nvl "Makes sense. Even though it's jut a game"
                    pd_nvl "Thx for the quick chat!"
                "•I could see myself switching it up.":
                    hide screen NVLnarration
                    $ pdEngagement += 2
                    $ promisedPDOutlaw = True
                    player_nvl "Thanks!"
                    player_nvl "I'm glad you dig it. tbh, I'm kinda considering sprinkling more outlaw choices in"
                    pd_nvl "Hell yeah, I think you'd enjoy that!"
                    pd_nvl "Just play around with that edge a little bit more. Why not?"
                    pd_nvl "It's just a game after all"
                "•Don't respond.":
                    hide screen NVLnarration
                    $ pdEngagement -= 1
                    "Nah, don't really want to encourage a parasocial relationship."
        jump vig2_macro_bro1
    
    else:
        "It's Coriolis?"
        cs_nvl "Hey [username], that was such a cool stream!"
        if gunsBlazing == True:
            cs_nvl "It was fun to see you go out of your comfort zone and be a bit chaotic"
            cs_nvl "Honestly, I wasn't expecting to have as much fun with it as I did haha"
            cs_nvl "Anyway, thanks for the stream!"
            $ playerNVLNarration = "Coriolis is so nice. Should I respond?"
            show screen NVLnarration
            menu:
                "•You haven't seen anything yet.":
                    hide screen NVLnarration
                    $ enthusiasm += 1
                    player_nvl "Well get ready for more chaos!"
                    player_nvl "Outlaws on the loose!"
                "•Thank you.":
                    hide screen NVLnarration
                    $ csEngagement += 1
                    player_nvl "Thanks, Coriolis"
                    player_nvl "It means a lot to have you in the chat!"
                    cs_nvl "Aww, thanks [username]!"
                "•Don't respond.":
                    hide screen NVLnarration
                    $ csEngagement -= 3
                    "Nah, don't really want to encourage a parasocial relationship."
        else:
            cs_nvl "I liked that stealth run on the base"
            cs_nvl "It felt really tense"
            if vig2_outlawEpilogue == True:
                cs_nvl "I was surprised by siding with Matticus at the end, though"
                cs_nvl "But I get it, tough to weigh the safety of MAC and the wider galaxy in that moment"
            else:
                cs_nvl "And I was stoked to see you side against the 'skeeve' Matticus haha"
            cs_nvl "Anyway, thanks for the stream!"
            $ playerNVLNarration = "Coriolis is so nice. Should I respond?"
            show screen NVLnarration
            menu:
                "•It was tough balancing both Outlaw and Marshal." if vig2_outlawEpilogue == True:
                    hide screen NVLnarration
                    $ reluctance += 1
                    player_nvl "Yeah, it was tough balancing the two styles"
                    player_nvl "Moze being both an Outlaw thief and a captain with Morals is interesting"
                    cs_nvl "Totally"
                    cs_nvl "Glad I don't have to be in that position haha"
                "•Good to go back to basics." if vig2_outlawEpilogue == False:
                    hide screen NVLnarration
                    $ reluctance += 1
                    player_nvl "Yeah, I wanted to go back to basics"
                    player_nvl "Get into some outlaw thievery vibes"
                    cs_nvl "It was fun to see those vibes back!"
                "•I'm glad you're liking it.":
                    hide screen NVLnarration
                    $ csEngagement += 1
                    player_nvl "Thanks, Coriolis"
                    player_nvl "It means a lot to have you in the chat!"
                    cs_nvl "Aww, thanks [player]!"
                "•Don't respond.":
                    hide screen NVLnarration
                    $ csEngagement -= 3
                    "Nah, don't really want to encourage a parasocial relationship."
        jump vig2_macro_bro1

label vig2_macro_bro1():
    nvl clear
    hide discordview with dissolve
    scene black with dissolve
    "You weren't expecting that. But it was kind of nice for them to reach out."
    "But now it's time to walk away from your computer."
    "You shut down the computer and start winding down for the evening."
    "You have a quick dinner and then finish up homework for class the next day."
    "As you brush your teeth, you see a notification on your phone that you missed while winding down."
    scene discordview with dissolve
    "It's from Elliot, a couple hours ago."
    bro_nvl "Hey [player], just wanted to let you know I caught the first stream VOD for Oakley 2"
    bro_nvl "Crazy stuff! I really like the direction they're taking Moze's character"
    bro_nvl "and OMG MAC"
    bro_nvl "SO CUTE!"
    bro_nvl "I love him. Would die for him. we stan 1000\%"
    bro_nvl "Also..."
    bro_nvl "Not you going \"bad guy\" Moze this time around?"
    bro_nvl "You've changed. Like a couple years at college and now you're a big bad Outlaw, crazyyyy"
    bro_nvl "Jkjk, hope you're having fun, excited to follow the stream!"
    $ playerNVLNarration = "Based on the time change, Elliot's probably already asleep." #check if this messes with the NVL sequence
    show screen NVLnarration
    pause
    $ playerNVLNarration = "But you decide to shoot him a message anyway."
    menu:
        "•Thanks!":
            hide screen NVLnarration
            player_nvl "Thanks El, really appreciate you checking it out!"
        "•Outlaw life is good!" if vig2_outlawEpilogue == True:
            hide screen NVLnarration
            $ enthusiasm += 2
            player_nvl "Felt like time for a change of pace"
            player_nvl "Outlaw life is pretty sweet!"
        "•Outlaw life is interesting." if customsStampede == True and gunsBlazing == False and vig2_outlawEpilogue == False:
            hide screen NVLnarration
            $ enthusiasm += 1
            player_nvl "It's a change of pace for sure"
            player_nvl "Still trying to see how it feels, but it's interesting"
        "•Outlaw life is good." if customsStampede == True and gunsBlazing == True and vig2_outlawEpilogue == False:
            hide screen NVLnarration
            $ enthusiasm += 1
            player_nvl "It's a change of pace"
            player_nvl "Been checking out how it feels to walk on the wild side!"
        "•Outlaw life is good." if customsStampede == False and gunsBlazing == True and vig2_outlawEpilogue == False:
            hide screen NVLnarration
            $ enthusiasm += 1
            player_nvl "It's a change of pace"
            player_nvl "Just kinda trying it out, seeing how the wild side feels"
        "•That was an accident.":
            hide screen NVLnarration
            player_nvl "That was an accident lol"
            player_nvl "I had to play it off on stream :'("
            menu:
                "•The chat's been a lot of fun.":
                    $ enthusiasm += 1
                    player_nvl "But it's been real fun to play around with chat"
                    player_nvl "Lotta bits in the chat, you'll see next episode!"
                "•The characters are really cool.":
                    $ enthusiasm += 1
                    player_nvl "But the character dynamics are really interesting this route"
                    player_nvl "It's a compelling spin on Moze!"
                "•Debating going back to Marshal, miss playing with you.":
                    $ reluctance += 2
                    player_nvl "I'm debating going back to Marshal style."
                    player_nvl "Game doesnt feel as rewarding as when we were playing together"
                "•Debating going back to Marshal, will see how story develops.":
                    $ reluctance += 1
                    player_nvl "Could go back to Marshal, idk"
                    player_nvl "Will have to see how the story goes"
    player_nvl "Hope things with Cedric are going good! Love you <3"
    "You send the texts and then finish getting ready for bed."
    jump vig2_macro_sleep

label vig2_macro_sleep():
    scene black with dissolve
    $ menu = adv_menu
    "It's been a long day and you feel the tension dissipate from your muscles as you get into bed."
    "You lay your head on the pillow."
    if reluctance > enthusiasm and outlaw > marshal:
        "It's been a long day and the stream took a lot out of you."
        "Your mind is foggy, a cloud of robots, outlaws, and spaceships."
        "What do you think about as you drift to sleep?"
    if reluctance > enthusiasm and marshal >= outlaw:
        "There's still some leftover adrenaline from the stream."
        "Your mind leaps through a series of images, robots, outlaws, and spaceships."
        "What do you think about as you drift to sleep?"
    if enthusiasm > reluctance and outlaw > marshal:
        "There's still some leftover adrenaline from the stream."
        "Your mind leaps through a series of images, robots, outlaws, and spaceships."
        "What do you think about as you drift to sleep?"
    if enthusiasm > reluctance and marshal > outlaw:
        "It's been a long day and the stream took a lot out of you."
        "Your mind is foggy, a cloud of robots, outlaws, and spaceships."
        "What do you think about as you drift to sleep?"
    menu:
        "What do you think about as you drift to sleep?"
        "Think about your conversations with chat.":
            "So many people watch you play a game."
            "It's fun...right?"
            menu:
                "Yeah!":
                    $ energy += 1
                    "Yeah, it is fun!"
                "Yes.":
                    "It is."
                "Sometimes.":
                    "It is. Most of the time."
                "Not always.":
                    $ energy -= 1
                    "A lot of the time it just feels draining."
        "Think about how tired you are.":
            "Sleep is going to feel so good"
            $ energy += 1
        "Think about getting to Affiliate.":
            "It's not going to be easy, but you know you can do this."
            "In your mind you picture it: a glossier stream set up, clear-sounding microphones, and 100+ viewers in chat."
    
    "As you start to drift to sleep, you can't stop your mind from wandering back to the last episode of {i}Oakley 2: Settle the Score{/i}."
    if outlaw > marshal:
        "You picture the comms base and the characters inside and feel..."
        menu:
            "Regret.":
                $ reluctance += 1
                "Even though it's just a game, you feel like you made the wrong choice."
            "Regret?":
                "A mixture of both regret and excitement."
                "Even though it's just a game, you feel confused."
            "Confidence.":
                $ enthusiasm += 1
                "You had to do what you had to do."
                "You know this."
            "A desire to replay the game.":
                $ energy += 1
                "You imagine how the end game scenario would have played out if you chose differently, and you feel excitement."
                "You can always play the game again, after all."
            "Nothing.":
                "You don't feel anything in particular."
            "Pressure from chat.":
                $ reluctance += 1
                "You remember the comments from chat, like small weights on a scale."
    else:
        "You picture MAC and feel..."
        menu:
                "Regret.":
                    $ enthusiasm += 1
                    "Even though it's just a game, you feel like you made the wrong choice."
                    "What if MAC is more in danger now?"
                "Regret?":
                    "A mixture of both regret and excitement."
                    "Even though it's just a game, you feel confused."
                "A desire to replay the game.":
                    $ energy += 1
                    "You imagine how the end game scenario would have played out if you chose differently, and you feel excitement."
                    "You can always play the game again, after all."
                "Confidence.":
                    $ reluctance += 1
                    "There was no other choice. You couldn't ally with Matticus."
                "Nothing.":
                    "You don't really feel anything in particular."
                "Pressure from chat.":
                    $ reluctance += 1
                    "You remember the comments from Chat, like small weights on a scale."
                "Even more tired.":
                    "Just thinking about the game makes your eyelids feel heavier."
        jump vig2_macro_end

label vig2_macro_end():
    "As your eyes finally start to become heavy, you hear a slight buzz from the nightstand."
    "A Loop'd notification. From Elliot."
    "You don't unlock the phone, because you can read the message from the lock screen."
    bro "Love you too!"
    stop music fadeout 4.0
    pause 2.0
    jump vignette3Start

#label endPlaytest():
    #pause 2.0
    #scene game_main_menu with dissolve
    #"Thank you for participating in this playtest of Stream Evil!"
    #"Our team is very grateful for your time and would love to hear your feedback!"
    #"If you're doing a remote test, please go to this {a=https://docs.google.com/forms/d/e/1FAIpQLScDUvazO6ajENISfpBgtitvIo3aI8ffpTi_Hvs7qu15Dec9Dw/viewform}google form{/a} and fill out a quick survey."
    #"If you're conducting an in-person test, please save your game in an empty slot, then notify your facilitator that you have finished the playtest.\n(Press ESC and select \"Save\" from the menu, then click on an empty square)"
    #"Once again, thank you very much for your time!"
    #"We hope you have a wonderful day!\n-Beck, Josh, Jules, Justin, and Mia"

    #scene bg black with dissolve
    #call screen playtestRecord

    #$ renpy.full_restart()
    #return
