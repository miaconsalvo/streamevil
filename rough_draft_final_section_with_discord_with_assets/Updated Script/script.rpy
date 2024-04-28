
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
    menu:

        "Pitch the stream to the newer viewers":
            mc "I think I'm gonna call it for tonight guys. If you're new here, I stream PLACEHOLDERGAME every Friday!"
            mc "We're gonna play the next chapter as soon as it's out."
            mc "I mostly just play games like this, or sometimes with friends."
            mc "We're all about good vibes! Drop in if you're curious!"
            "I should probably thank the new viewers too"
            mc "Thanks everyone who came fromt he raid! I hope you guys will tune in again next week!"
            jump poststreamdec
        "Sign off normally":
            mc "I think I'm gonna call it for tonight guys. Thanks for tuning in this week! I'm gonna be live again next Friday to play the next chapter."
            mc "Peace out everyone."
            jump poststreamdec

label poststreamdec:
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
    mc "Sure! How have you been? How's school going?" 
    mc "Everything you hoped for ;)?"
    bro "I'm alright, class has been kinda boring, it's most just orientation stuff."
    bro "Yknow like, \"here's where you eat, here's where you shower, don't do both at the same time\""
    mc "Hahahah classic"
    bro "Yeah like they say they really treat you like an adult in college."
    bro "To be honest I'm kinda unimpressed. They really have been drilling this \"Be careful with booze\" message into us."
    bro "Like some people like to get wasted, whats the big deal?"
    menu:

        "Yeah agreed":
            mc "Yeah for sure. I remember first semester Jeff and I would show up to every Friday morning lecture hungover with sunglasses."
            mc "Good times lol."
            bro "lol I don't know about that."
            bro "Didn't he like flunk out?"
            mc "Yeah. He hit frosh super hard and then kinda never stopped."
            bro "Damn sounds hardcore."
            bro "I didn't realize you were such a party animal. ;)"
            mc "I'm not! I just had a crazy first year."
            bro "sure sure :)"
            jump brodec1


        "Be careful with that stuff":
            mc "Yeah I know what you mean, but there's a lot of people who have a really tough time with that stuff."
            mc "You remember my first year roommate Jeff? He hit frosh super hard and then kinda never stopped."
            mc "He basically flunked out second year."
            bro "You know I'm not like that right?"
            mc "Yeah for sure. Just be careful with that stuff. Make sure you don't get sucked into doing things you don't want to."
            bro "You're definitiely right about that!"
            bro "There was this guy at the orientation the other day bragging about doing lines and going to a rave."
            bro "Yuck."
            mc "Hahaha yeah exactly."
            jump brodec1


    label brodec1:
        mc "Just be mindful of why you're there and what you want to get out of it."
        bro "Yeah you're right."
        bro "But yeah, I wanted to ask you for some advice if you've got a sec…"
        mc "I'm honored!"
        bro "<3"
        bro "Yeah so there's this guy on my floor, and he's really cute. I kinda have a bit of a crush on him :$"
        mc  ":3"
        bro ":/"
        mc "Sorry, continue?"
        bro "I kinda just wanted to get some advice on what I should do?"
    menu:
        "Let things continue naturally!":
            mc "…does he have a name?"
            bro "hahahah yeah, Tom. We chatted during the icebreaker last week. He's in biochem."
            mc "Cool! Have you guys talked much?"
            mc "…is he single?"
            bro "ahh yeah, Idk. I think so but I'm not sure."
            mc "Yeah I mean that's kinda an important detail XD"
            bro "I KNOW!!"
            bro "Aaahg why can't we all wear nametags with relationships statuses!"
            mc "I know what you mean. But don't worry!"
            mc "Just keep spending time together! I'm sure if he's with someone it'll come out naturally soner or later."
            bro "Yeah that makese sense."
            mc "Don't worry too much about it, if you both feel a connection then I'm sure the opportunity will present itself."
            jump brodec2
    
        "Seize the day!":
            mc "I mean does he know you have a crush?"
            bro "I'm not sure…"
            mc "Well I mean, you can't expect him to be a mindreader no?"
            mc "Seize the day! Ask him out!"
            bro "What? We only talked that one time during the icebreaker."
            mc "That's how these things start out! It's all part of the process of getting to know someone."
            mc "If you both feel a connection I'm sure he'll say yes!"
            mc "And if he says no…"
            mc "Well that's part of life too hahaha"
            bro "ooof fair enough."
            bro "It would be nice to know though…"
            bro "Maybe you're right."
            mc "I'm telling you, life's too short."
            jump brodec2

    label brodec2:
        bro "<3 You're the best :)"
        mc "Thanks! Let me know how it goes :)"
        bro "Gotta go! Talk later"
        mc "See ya!"
        jump endPrototype
    
label endPrototype:
    scene black with dissolve
    "Thank you for playing the first prototype of \"Stream Evil\"!"
    return