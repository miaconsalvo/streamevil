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
    "The Oakley is quiet today, and this coffee feels like I'm trying to cure every sleepless night I've had for the past few days."
    mS "It's nice to be first one up, actually is it even morning?"
    "I check the clock on the wall, yep, morning."
    "\"I've got lots more work where that came from.\" Arrogant rat. I should've gone back and blown his fortress to ash."
    "I take an uninterested sip of my drink wrapping both hands around the glass."
    "I can't believe I'm letting this get to me. Hell I've done worse, we've done worse. This probably wouldn't even crack the top five."
    "But we're supposed to do better." 
    "That's the point of all of this isn't it?"
    "I find myself staring off staring off into the distance." 
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
    "I wait until I can feel her shoulder relax and walks out and down the hall, alone."

label vig3marshalstart(): 

INT. OAKLEY SPACE SHIP (MARSHALL)
The Oakley is quiet today, and this coffee feels like I’m trying to cure every sleepless night I’ve had for the past few days.
MOZE (V.O.)
It’s nice to be first one up, if it’s even morning?
I check the clock on the wall, yep, morning.
MOZE (V.O.)
"Don't worry. You'll get yours.”
Annoying rat. He’s lucky I didn’t turn back and blow his fortress to
ash.
I take an uninterested sip of my drink wrapping both hands
around the glass.
MOZE
I’m letting this get to me. When
have I ever taken one of Sav’s
threats seriously. I’m sure he
wants to see *her* even less than
me.
(Pause)
We’re trying to be better, but
what’s the point if we’re all
arrested, if they take MAC away.
I find myself staring off staring off into the distance. With
my back to the door I don’t see Jennica (Early 30s) come in.
She’s wearing her usual clothes but her eyes dark from
exhaustion.
JENNICA
Up early?
MOZE
Surprisingly so are you.
4.
5.
JENNICA
Can’t be early if ya ain’t sleep.
MOZE
Nothing quite like the comfort of
my pilot being sleep deprived.
JENNICA
Thank the Makers she flies herself
well enough.
She pulls up a chair next to me, grabs the warm metal pitcher
from the table and fills a glass of her own. She takes out a
small flask. I hold my cup out she pours a bit inside mine
and her own, we cheers in the air.
MOZE
Fighting with Teresa didn’t tire
either of your out I suppose?
JENNICA
Don’t know ‘bout her, I’ve been
camping in the cockpit so I don’t
find out.
MOZE
Luckily there isn’t a bathroom in
there.
JENNICA
Takes a brave woman to go relieve
herself in times like these.
Jennica’s joke ends in a forced chuckle. and the room goes
quiet and cold for moment.
JENNICA (CONT'D)
I’m not just staying in the cockpit
to avoid Resa...
Moze straightens herself.
JENNICA (CONT'D)
I keep dreaming about getting a hit
on the scanners, and I don’t make
it to the helm in time.
MOZE
You’re not the only who can operate
the Oakley.
5.
6.
JENNICA
No, but I’m the only one that can
outrun Ama. We got lucky- but no
offense to our saving grace I don’t
like not knowing how much distance
we might or might not have.
There’s a long pause.
JENNICA (CONT'D)
Every little blip on the scanner
make me jump, Captain. That’s until
I find out it’s some stoved-up
space junk floatin’ in from a click
over.
Jennica looks away from Moze for a moment to find the words.
JENNICA (CONT'D)
I wonder...if we made the right
choice. As wrong as it sounds.
MOZE
Jen...
JENNICA
You’re right, those people needed
that aid but we gotta be okay with
the tough choices ya know, be more
logical, make the hard call.
MOZE
Please.
Jennica goes quite.
JENNICA
She can barely look at me Moze...
Jennica smacks the glass away from her, it falls to the
ground with a clang. She takes a quiet moment to calm
herself. I set my cup down gently.
JENNICA (CONT'D)
We’re doing better, and that’s all
fine and good. And hell I’ll stand
by what I said. But we need to be
more united on things if we’re
gonna make it.
I don’t respond.
6.
7.
JENNICA (CONT'D)
I like the kid. But we’ve been over
our heads from the start... She’s
gonna find us, and I’m sure BigCorp
isn’t hung up on whether or not
we’re brought back in one piece.
Jennica lets out a defeated sigh. Teresa’s voice echoes
through the speaker before I can answer.
TERESA (O.S.)
Captain! There’s a transmission for
us - I’m certain it’s the
Dragonflies.
Jennica shoots up, I place a hand on her shoulder.
MOZE
Take ten seconds.
When Jennica’s shoulder relaxes I walk out and down the hall,
alone.

