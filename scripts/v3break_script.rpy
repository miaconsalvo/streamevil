label vig3_break():
    $ narrator = reg_narrator
    show bg black at topleft onlayer background with pixellate
    hide inventorsfairgallery_stream
    "What was that?"
    "What just happened?"
    player "Did the game just...crash?"
    $ AddChatter (vig3break_crash_comment1)
    pause 0.5
    $ AddChatter (vig3break_crash_comment2)
    pause 0.5 
    $ AddChatter (vig3break_crash_comment3)
    pause 0.5 
    $ AddChatter (vig3break_crash_comment4)
    pause 1 
    $ AddChatter (vig3break_crash_comment5)
    pause 0.5 
    $ AddChatter (vig3break_crash_comment6)
    pause 0.5
    $ AddChatter (vig3break_crash_comment7)
    pause 0.5 
    $ AddChatter (vig3break_crash_comment8)
    player "It looks like there's a problem with the game files."
    player "Must've been something wrong when I updated."
    $ AddChatter (vig3break_crash_comment9)
    pause 0.5
    $ AddChatter (vig3break_crash_comment10)
    "You'll need to kill time while it gets fixed."
    menu:
        "Let's call a short break for now."
        "Make a joke.":
            player "Well everyone I guess that's our game!"
            player "Who cares if it's just the most insane cliffhanger."
            player "Been a great run!"
            $ AddChatter (vig3break_brb_comment1)
            pause 0.5 
            $ AddChatter (vig3break_brb_comment2)
            pause 0.5 
            $ AddChatter (vig3break_brb_comment3)
            player "I kid, I kid."
            player "Let's get some water and stretch those legs so we can lock in!"
            $ AddChatter (vig3break_brb_comment4)
            player "See ya in a bit!"
            $ AddChatter (vig3break_brb_comment8)
        "Be all professional-like.":
            player "I'm sorry guys it looks like it'll take some time to fix."
            player "Especially sorry that it happened after such a wild cliffhanger."
            $ AddChatter (vig3break_brb_comment5)
            player "So let's get some water, stretch our legs."
            player "and then we can chat while we wait!"
            $ AddChatter (vig3break_brb_comment5add)
            player "Be right back!"
            $ AddChatter (vig3break_brb_comment8)
        "Fumble a bit.":
            player "Well that happened ..."
            player "..."
            player "Oh wow that's gonna take a while."
            $ AddChatter (vig3break_brb_comment6)
            player "I'm gonna grab some water and stretch my legs"
            player "Be right back!"
            player "Hopefully it'll be all fixed by then."
            $ AddChatter (vig3break_brb_comment7)
            $ AddChatter (vig3break_brb_comment8)
    #show bg black with dissolve
    "Leaving the stream for a bit can always feel really nice."
    "The hallway is much cooler than your room, which has undoubtly been storing your body heat."
    "Your roomate is gone for the night, so at least you know you aren't disturbing them."
    "You pass through the quiet of your apartment."
    "Grab some water and stand in the kitchen for a moment."
    menu: 
        "Streaming is..."
        "Tiring.":
            $ energy -= 1
            "Even if it's only for a few hours, streaming can really take a toll."
            "It's hard to be so *on* all the time."
            "The chat's energy can help a bit."
            "But still."
        "Exciting.":
            $ energy += 1
            "New game, new audience, everything is so exciting."
            "There's something really fun about the way people respond to you and what you do."
            "That energy exchange keeps things fresh for sure."
        "Surprising.":
            "How did you get here?"
            "Feels like yesterday no one was watching and know you can feel a community building."
            "It's surprising."
            "But extremely rewarding."
    "You take a moment"
    "Breathe"
    "The chat is waiting."
    "You should probably go back."
    "You sit back in your chair, set your water bottle off the the side."
    #hide bg black with dissolve
    player "Alright, I'm back." 
    "It doesn't look like a lot of progress has gone by."
    player "How're we doin everyone?"
    $ AddChatter (vig3break_brb_comment9)
    pause 0.5
    $ AddChatter (vig3break_brb_comment10)
    pause 0.5
    "You take a short drink of water and wait for the responses to come."
    $ AddChatter (vig3break_brb_comment11)
    pause 0.5 
    $ AddChatter (vig3break_brb_comment12)
    player "We'll be back soon, no worries."
    "Let's get the chat hyped about what comes next."
    player "But can we talk about Ama for a second!"

    menu: 
        "Let's talk about Ama"
        "Y'all I think we can take her.":
            $ AddChatter (vig3break_ama_take_comment1)
            pause 0.5
            $ AddChatter (vig3break_ama_take_comment2)
            pause 0.5
            $ AddChatter (vig3break_ama_take_comment3)
            pause 1
            $ AddChatter (vig3break_ama_take_comment4)
            pause 0.5
            $ AddChatter (vig3break_ama_take_comment5)
            pause 0.5
            $ AddChatter (vig3break_ama_take_comment6)
            pause 1
            $ AddChatter (vig3break_ama_take_comment7)
            player "Hmmm"
            player "Who knows how much we can do, truly."
            player "Reynar has the whole Vineyard locked down tight."
            $ AddChatter (vig3break_ama_take_comment8)
            pause 0.5
            $ AddChatter (vig3break_ama_take_comment9)
            pause 0.5
            $ AddChatter (vig3break_ama_take_comment10)
            pause 1
            $ AddChatter (vig3break_ama_take_comment11)
            pause 0.5
            $ AddChatter (vig3break_ama_take_comment12)
            pause 0.5
            $ AddChatter (vig3break_ama_take_comment13)
            "The world is feeling so much bigger!"
            "With a bigger cast."
            "Speaking of the cast..."

        "She is just *chef's kiss*":
            $ AddChatter (vig3break_ama_kiss_comment1)
            pause 0.5
            $ AddChatter (vig3break_ama_kiss_comment2)
            pause 1
            $ AddChatter (vig3break_ama_kiss_comment3)
            pause 0.5
            $ AddChatter (vig3break_ama_kiss_comment4)
            pause 1
            $ AddChatter (vig3break_ama_kiss_comment5)
            pause 0.5
            $ AddChatter (vig3break_ama_kiss_comment6)
            player "She's definitely a fan favourite."
            player "Outlaws are charming."
            $ AddChatter (vig3break_ama_kiss_comment7)
            pause 0.5
            $ AddChatter (vig3break_ama_kiss_comment8)
            pause 0.5
            $ AddChatter (vig3break_ama_kiss_comment9)
            pause 0.5
            $ AddChatter (vig3break_ama_kiss_comment10)
            pause 0.5
            $ AddChatter (vig3break_ama_kiss_comment11)
            player "Gotta make sure we keep the family safe!" 
            player "Speaking of family..."

        "So how dead do you think we are?":
            $ AddChatter (vig3break_ama_dead_comment1)
            pause 0.5
            $ AddChatter (vig3break_ama_dead_comment2)
            pause 0.5
            $ AddChatter (vig3break_ama_dead_comment3)
            pause 1
            $ AddChatter (vig3break_ama_dead_comment4)
            pause 1
            $ AddChatter (vig3break_ama_dead_comment5)
            pause 0.5
            $ AddChatter (vig3break_ama_dead_comment6)
            pause 0.5
            $ AddChatter (vig3break_ama_dead_comment7)
            player "That relationship has always been rocky."
            player "Even a bit ambiguous at times."
            player "She's been hunting us so long, who knows."
            $ AddChatter (vig3break_ama_dead_comment8)
            pause 0.5
            $ AddChatter (vig3break_ama_dead_comment9)
            pause 0.5
            $ AddChatter (vig3break_ama_dead_comment10)
            pause 0.5
            $ AddChatter (vig3break_ama_dead_comment11)
            pause 0.5
            $ AddChatter (vig3break_ama_dead_comment12)

    player "We gotta talk about Rec."
    player "It's amazing we get to see them again."
    $ AddChatter (vig3break_rec_comment1)
    pause 0.5 
    $ AddChatter (vig3break_rec_comment2)
    pause 0.5 
    $ AddChatter (vig3break_rec_comment3)
    player "There's definitely a lot to unpack."

    menu: 
        "How does meeting Rec feel without Allistar"
        "Not having Allistar adds some good tension.":
            player "I really like how tense the story is."
            $ AddChatter (vig3break_rec_tense_comment1)
            pause 0.5 
            $ AddChatter (vig3break_rec_tense_comment2)
            pause 0.5 
            $ AddChatter (vig3break_rec_tense_comment3)
            pause 0.5
            $ AddChatter (vig3break_rec_tense_comment4)
            pause 1 
            $ AddChatter (vig3break_rec_tense_comment5)
            pause 0.5 
            $ AddChatter (vig3break_rec_tense_comment6)
            pause 0.5         
            $ AddChatter (vig3break_rec_tense_comment7)
            player "Hey we did what we had to right?"
            player "It's a hard choice but I think the game is interesting this way."
            $ AddChatter (vig3break_rec_tense_comment8)
            pause 0.5 
            $ AddChatter (vig3break_rec_tense_comment9)
            pause 0.5 
            $ AddChatter (vig3break_rec_tense_comment10)
            pause 1
            $ AddChatter (vig3break_rec_tense_comment11)
            pause 0.5 
            $ AddChatter (vig3break_rec_tense_comment12)
            pause 0.5 
            $ AddChatter (vig3break_rec_tense_comment13)
            player "We'll let it play out."
            player "I'm sure there's plenty more surprises waiting for us."
        "I wish I could've seen their reunion.":
            player "I wish I saw that reunion."
            $ AddChatter (vig3break_rec_reunion_comment1)
            pause 0.5 
            $ AddChatter (vig3break_rec_reunion_comment2)
            pause 0.5 
            $ AddChatter (vig3break_rec_reunion_comment3)
            pause 0.5
            $ AddChatter (vig3break_rec_reunion_comment4)
            pause 0.5 
            $ AddChatter (vig3break_rec_reunion_comment5)
            pause 0.5 
            $ AddChatter (vig3break_rec_reunion_comment6)
            player "I can always play again I guess."
            player "But this playthrough is cool!"
            $ AddChatter (vig3break_rec_reunion_comment7)
            pause 0.5 
            $ AddChatter (vig3break_rec_reunion_comment8)
            pause 0.5 
            $ AddChatter (vig3break_rec_reunion_comment9)
            pause 0.5
            $ AddChatter (vig3break_rec_reunion_comment10)
            pause 0.5 
            $ AddChatter (vig3break_rec_reunion_comment11)
            pause 0.5 
            $ AddChatter (vig3break_rec_reunion_comment12)
            player "We're definitely not out of the woods yet!"
            player "There's a whole chapter to play through."

    "You hear the unmistakable sound of a MYST notification."
    "The fix is done."
    $ AddChatter (vig3break_end_comment1)
    pause 0.5 
    $ AddChatter (vig3break_end_comment2)
    pause 0.5 
    $ AddChatter (vig3break_end_comment3)
    pause 0.5
    $ AddChatter (vig3break_end_comment4)
    player "Let's settle some scores everyone!"
    pause 0.5 
    $ AddChatter (vig3break_end_comment5)
    pause 0.5 
    $ AddChatter (vig3break_end_comment6)
    pause 0.5 
    $ AddChatter (vig3break_end_comment7)
    pause 0.5 
    $ AddChatter (vig3break_end_comment8)
    pause 0.5 
    $ AddChatter (vig3break_end_comment9)
    pause 0.5 
    $ AddChatter (vig3break_end_comment10)
    "You boot up the game again."
    "Open on your recovered save."
    "And pick up right where you left off."
    $ vig3break_ama_dead_comment11.click = False
    $ vig3break_rec_tense_comment4.click = False
    $ vig3break_rec_tense_comment10.click = False
    $ vig3break_rec_reunion_comment3.click = False
    $ vig3break_rec_reunion_comment9.click = False
    $ vig3break_end_comment5.click = False
    hide screen streamerCommentary
    $ macroChoice = False
    if macroChoice == False:
        $ narrator = alt_narrator
    else:
        $ narrator = reg_narrator
    jump vig3_sc10           
