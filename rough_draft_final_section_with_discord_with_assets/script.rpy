
# characters

define m = Character(("Moze"))
define pilot = Character(("Jennica"), color="#e9791dff")
define engineer = Character(("Teresa"), color="#b40d0dff")
define mac = Character(("Mac"), color="#0bb6b6")
define anatar = Character(("Anatar"), color="#e4e009")
define merchant = Character(("Merchant"), color="#41b60b")
define ama = Character(("Ama"), color="#770bb6")
define mc = Character(("StreamerProtagonist"), color="#66CC00")
define mod = Character (("StreamMod"), color="#00FFCC")
define bro = Character (("Little Brother"), color="#FE67EB")



# rest of the vignette goes here

label start:
    scene council with dissolve
    show captain at truecenter with dissolve
    show engineer at right with dissolve
    show pilot at left with dissolve
    pilot "We've been in hyperspace for about an hour. And we got out before the cruisers were within range of us. We should be clear of any BC tracking devices."
    engineer "\"Should\" be. They shouldn't have been able to track us to Cromuu in the first place."
    m "Maybe that wyvern-class mercenary wasn't as random as we thought. They might have transmitted coordinates to BC before we dusted them."
    pilot "And from there, there are only a handful of habitable planets in the sector."
    engineer "They could have increased surveillance on each of them."
    m "Could have. Hard to know for certain. But we'll need to be more careful in the future, and find a way to navigate the interstellar pathways with more stealth."
    pilot "Any ideas?"
    m "Maybe. I need to think."
    "We're all quiet. No {i}bzzrts{/i}, no random facts about our past lives."
    "...no Mac."
    m "Does anyone know where Mac is?"
    "Ship Intercom" "Attention crew, escape pod procedure activated."
    m "Shit, what trouble is he getting into now."
    "I rush out of the council room."
    jump escapePodConfrontation

label escapePodConfrontation:
    scene hallway with dissolve
    show captain at left
    "I run down the halls of the ship and leap over the railing leading down to the escape pod bay."
    "As I near the pods, I hear Anatar's voice."
    anatar "Come on Mac, you can trust me. We can live a safe life. You don't have to be on the run all the time."
    mac "But Captain said to stay close to her."
    anatar "I know Mac. But Moze isn't always right. This place is dangerous."
    "I turn the corner."
    show mac at right with dissolve
    show mechanic at truecenter with dissolve
    "Mac is standing in the center of the hall. Anatar has one foot inside an open escape pod."
    "As I step into the light, Anatar sees me and reaches for Mac."
    "Discord ping"
    jump messagefrommod

label messagefrommod:
    scene bg hallwaydiscord with dissolve
    mod "Hey just wanted to let you know, you have 40 new viewers right now"
    mc "What?"
    mc "where did these people come from?"
    mod "Coronolius was in squeejieboy33's stream when it was ending. He suggested your stream when they were deciding on someone to raid."
    mc "Holy cow. This is the most viewers I've ever had! What should I do?"
    mod "I dunno man. Just thought you should know lol."
    "Wow what do I do?"
    "Better address them right?"
    mc "Wow squeejieboy33 sent all of you? This is crazy! Hope you guys enjoy the stream!"
    "I guess I should finish up this chapter"
    jump postmodmessage


label postmodmessage:
    scene hallway
    show captain at left
    show mac at right
    show mechanic at truecenter
    "I pull my blaster and point it at him, but by the time I do he has already grabbed Mac with his left arm and is holding him in the air in front of him."
    m "What are you doing, Anatar?"
    anatar "I'm getting {i}out{/i} of this crazy life, Moze."
    anatar "You saw what happened just now, right?"
    anatar "Ama said BC was going to hold me as an accomplice. What do you think that means they're going to do to Grand Junction?"
    anatar "That's beside the ruin we left of the spaceport. Or the people who got hurt in the crossfire."
    m "I know. None of that was right. But we didn't have a choice."
    anatar "We {i}always{/i} have a choice."
    m "If BC gets Mac, things are only going to get worse."
    anatar "Things are already worse!"
    anatar "They get worse everywhere we go!"
    anatar "No, everywhere {i}you{/i} go."
    anatar "I know you think Ama's code is selfish, but at least it's a code. At least she lives by rules."
    anatar "You, Moze, you just go anywhere you want, do anything you want, and try to justify it by saying, \"I didn't have a choice.\""
    anatar "Grow up and start living in this galaxy with the rest of us. You don't change anything for the better. You just bring pain and death."
    m "I've heard enough."

    menu:
        m "I've heard enough."
        "Fire (cruelty)":
            "I fire a bolt. It lands right between Anatar's eyes."
            "He slumps to the ground."
            "Mac hits the floor and crawls to the other end of the hall."
            "I go over to Anatar's body. It's limp and cold."
            "I activate my com."
            m "Teresa, Jennica, Anatar tried to activate an escape pod and take Mac away."
            pilot "He did what?"
            engineer "Why?"
            pilot "Are you okay?"
            m "I don't know. I could use some help with the body."
            engineer "Roger, I'll be right down."
            "I gently move toward Mac and crouch down in front of him."
            m "Hey, I'm sorry about that."
            mac "Is he...is he dead?"
            "I glance back at the body."
            m "Yes."
            mac "Why?"
            m "He threatened you. He made his choice."
            mac "But, did he have to die?"
            m "It's safer than the alternative."
            mac "So this ship is still safe?"
            "I reach out my hand toward Mac."
            m "I'll make sure it is."
            jump postdecision1
        "Stun (mercy)":
            "I mean to press the stun button, but my finger slips"
            mc "Wait no!"
            "I fire a bolt. It lands right between Anatar's eyes."
            "He slumps to the ground."
            "Mac hits the floor and crawls to the other end of the hall."
            "I go over to Anatar's body. It's limp and cold."
            "I activate my com."
            m "Teresa, Jennica, Anatar tried to activate an escape pod and take Mac away."
            pilot "He did what?"
            engineer "Why?"
            pilot "Are you okay?"
            m "I don't know. I could use some help with the body."
            engineer "Roger, I'll be right down."
            "I gently move toward Mac and crouch down in front of him."
            m "Hey, I'm sorry about that."
            mac "Is he...is he dead?"
            "I glance back at the body."
            m "Yes."
            mac "Why?"
            m "He threatened you. He made his choice."
            mac "But, did he have to die?"
            m "It's safer than the alternative."
            mac "So this ship is still safe?"
            "I reach out my hand toward Mac."
            m "I'll make sure it is."
            jump postdecision1

label postdecision1:
    scene bg mainmenu with dissolve
    "Damn, I didn't want to do that."
    "I wanted to hit the stun button."
    "These viewers seemed to really like it though. This is the craziest I've ever seen my chat."
    #show chat going crazy
    mc "Oh I guess that’s the end of this week's chapter."
    "This is as good a stopping point as any. I wonder if these people will be back next week."
    mc "I think I'm gonna call it for tonight guys. Thanks for tuning in this week! I'm gonna be live again next Friday to play the next chapter."
    "I should thank the new viewers too"
    mc "Thanks for everyone who came from the raid! I hope you guys will tune in again next week!"
    mc "Peace out everyone."
    #stream ends
    scene bg mainmenuwdiscord with dissolve
    mod "Hey bud crazy stream. I g2g Bradley wants to get some bibimbap"
    mc "Yeah insane! Enjoy I'll see you later."
    mod "ttyl"
    "Damn this is nuts, why did they want Anatar to die so bad?"
    "Discord ping"
    "Oh yeah! My brother said he wanted to talk after classes."
    scene bg mainmenuwdiscordbrowindow
    bro "Hey bro I just finished class, do you have a second?"
    mc "Sure! How have you been? How's school going? Everything you hoped for ;)?"
    bro "I'm alright, class has been kinda boring, it's most just orientation stuff."
    bro "Yknow like, \"here's where you eat, here's where you shower, don't do both at the same time\""
    mc "Hahahah classic"
    bro "Yeah like they say they really treat you like an adult in college."
    mc "Ah don't worry, soon enough you'll be thinking back on these moments like the good ol' days hahahaha"
    bro "Yeah I don't doubt it."
    bro "But yeah, I wanted to ask you for some advice if you've got a sec…"
    mc "Yeah sure! I'm honored <3"
    bro "<3"
    bro "Yeah so there's this guy on my floor, and he's really cute. I kinda have a bit of a crush on him :$"
    mc  ":3"
    bro ":/"
    mc "Sorry, continue?"
    bro "I kinda just wanted to get some advice on what I should do?"
    mc "…does he have a name?"
    bro "hahahah yeah, Tom. We chatted during the icebreaker last week. He's in biochem."
    mc "Cool! Have you guys talked much?"
    bro "Yeah! We really hit it off last week. I kinda want to ask him out but…"
    mc "…is he single?"
    bro "ahh yeah, Idk. I think so but I'm not sure."
    "He's adorable"
    mc "yeah I mean, that’s a somewhat important detail XD"
    bro "yeah for sure…"
    mc "well for now I'd say just keep talking to him. If he's with someone that info will come out sooner or later."
    bro "yeah that makes sense. Thanks bro!"
    mc "No problem! Don't worry  too much about it, if you both feel a connection then I'm sure the opportunity will present itself."
    bro "<3 You're the best :)"
    mc "Thanks! Let me know how it goes :)"
    bro "Gotta go! Talk later"
    mc "See ya!"
    jump endPrototype
    
label endPrototype:
    scene black with dissolve
    "Thank you for playing the first prototype of \"Stream Evil\"!"
    return