#This script contains the list of comments and chats that can appear in the stream

init python:
    class ChatEntry():
        #This function defines a new class of objects called ChatEntry.
        #ChatEntry objects have four potential attributes that can be defined.
        def __init__(self, click, prompt, tag, colour = "", target = "", ): #"click" has to go earlier because of the kind of argument it is.
            #self identifies the object as itself, allowing the object to reference its own attributes
            self.click = click #click is a boolean that determines if a comment is clickable or not. True is clickable, False is not.
            self.prompt = prompt #prompt is the string that will appear when the chat is shown
            self.tag = tag #tag is a numeric identifier that will allow us to "batch" comments together.
                            #Then we can do things like remove every object in the comments list with a tag == 2.
            self.colour = colour #added an attribute that will allow us to change the color of the text that appears.
                                #this probably won't be necessary, but wanted to play around with some possibilities.
                                #called it "colour" because "color" is often used by Renpy to refer to specific things and handle already determined attributes.
            self.target = target #target indicates a label that a clickable object will call.

#defining useful functions
default yadj = ui.adjustment()

init python:

    def AddChatter(message):
        global chatter_list
        global yadj

        chatter_list.append(message)
        renpy.pause(0.01) #bc reasons
        yadj.change(float('inf'))
        #yadj.value = float('inf') #- Getting this to work would be ideal
        #but it's still behaving weird, so stick with yadj.change for now

        if commentPing == True:
            renpy.sound.play("audio/ReceiveText.ogg")
        else:
            pass #Is there a "Pass" syntax?
        return

    def AddRandomChatter():

        global comment_list
        global chatter_list

        renpy.random.shuffle(comments_list) #This shuffles the comments_list so they appear in a random order
        chatter_list.append(comments_list[0]) 
        comments_list.remove(comments_list[0])
        return

label TurnSound():
    #$ commentPing = ! commentPing #There's a one liner for this but I don't know the syntax
    #so we do it unwieldy
    if commentPing == False:
        $ commentPing = True
        $ textContent = "Sound is On"
    elif commentPing == True:
        $ commentPing = False
        $ textContent = "Sound is Off"
    return

    
default chatter_list = [ ] #This is the list that displays on the Stream UI
default comments_list = [ ] #This list contains the objects that will be shuffled and chosen from to add to "chats"
#Objects will be taken from this list and added to "chats_list"

#Example Chat Entries:
default comment1 = ChatEntry( False, "{b}Squeejieboy33:{/b} Hope everyone's week is going well!", 1, "#000000ff" )
default comment2 = ChatEntry( False, "{b}topOmornin:{/b} Really dig the art style of this game", 2, "#000000ff", "comment2Choice")
default comment3 = ChatEntry( True, "{b}xKSamuraiKx:{/b} Hey [player], how's your week been?" , 1, "#000000ff", "comment3Choice")
default comment4 = ChatEntry( False, "{b}J4MIR0QU4I:{/b} Glad to see you still streaming this game!", 1, "#000000ff", )

#Comments in Scene 1
default vig2_sc1_comment1 = ChatEntry( False, "{b}Coriolis:{/b} I just got the live notification!", 2, "#000000")
default vig2_sc1_comment2 = ChatEntry( True, "{b}Coriolis:{/b} It's just after dinner for you right? How did that test go?", 2, "#000000", "vig2_sc1_testquestion")
default vig2_sc1_comment3 = ChatEntry( False, "{b}Squeejieboy33:{/b} ehh back again! the ending last time was nuts", 2, "#000000")
default vig2_sc1_comment4 = ChatEntry( False, "{b}kitcat:{/b} hey everyone!! ah im pumped for this one!", 2, "#000000")
default vig2_sc1_comment5 = ChatEntry( False, "{b}_lostinmetr0:{/b} does anyone know if this is the whole crew?", 2, "#000000")
default vig2_sc1_comment6 = ChatEntry( False, "{b}AFKangel:{/b} dunno. havent played yet.", 2, "#000000")
default vig2_sc1_comment7 = ChatEntry( False, "{b}kitcat:{/b} from where im at, yup that's it!", 2, "#000000")
default vig2_sc1_comment8 = ChatEntry( False, "{b}turb0g00se:{/b} matticus alignment might give some interesting options", 2, "#000000")
default vig2_sc1_comment9 = ChatEntry( False, "{b}_lostinmetr0:{/b} yeah it would give them a lot more access to the underground.", 2, "#000000")
default vig2_sc1_comment10 = ChatEntry( False, "{b}Coriolis:{/b} if [player] can convince him! like in the {i}Treck Down{/i} stream with the underworlder chief.", 2, "#000000")
default vig2_sc1_comment11 = ChatEntry( False, "{b}turb0g00se:{/b} true true", 2, "#000000")
default vig2_sc1_comment12 = ChatEntry( False, "{b}PickledDragons:{/b} yeah and definitely would lead to some shenanigans", 2, "#000000")
default vig2_sc1_comment13 = ChatEntry( True, "{b}shnzi:{/b} new to stream! did you like matticus in the first game?", 2, "#000000", "vig2_sc1_matticusopinion")
default vig2_sc1_comment14 = ChatEntry( False, "{b}kitcat:{/b} ouh yeah! let my lil guy MAC out to see the world!", 2, "#000000")

#Comments in Scene 1 Chat Responses
default vig2_sc1_coriolis_comment1 = ChatEntry( False, "{b}Coriolis:{/b} of course! I'm glad it went well!", 2, "#000000")
default vig2_sc1_coriolis_comment2 = ChatEntry( False, "{b}Coriolis:{/b} Oh I'm sorry to hear that, I hope your grade comes back ok!", 2, "#000000")
default vig2_sc1_kitcat_comment1 = ChatEntry( False, "{b}kitcat:{/b} Hot take alert haha", 2, "#000000")
default vig2_sc1_kitcat_comment2 = ChatEntry( False, "{b}kitcat:{/b} wow someone with a genuine hot take on this game, heck yea!", 2, "#000000")

#Comments in Scene 2
default vig2_sc2_comment1 = ChatEntry( False, "{b}_lostinmetr0:{/b} I too am a hater of customs. just an airport hater in general.", 2, "#000000")
default vig2_sc2_comment2 = ChatEntry( False, "{b}turb0g00se:{/b} fr", 2, "#000000")
default vig2_sc2_comment3 = ChatEntry( False, "{b}AFKangel:{/b} teresa OP", 2, "#000000")
default vig2_sc2_comment4 = ChatEntry( False, "{b}PickledDragons:{/b} ugh wait is this whole chapter just a stealth thing?", 2, "#000000")
default vig2_sc2_comment5 = ChatEntry( False, "{b}kitcat:{/b} Stealth Mission. Gaming Trope. Typically boring but allows for good character moments.", 2, "#000000")
default vig2_sc2_comment6 = ChatEntry( False, "{b}shnzi:{/b} LOL", 2, "#000000")
default vig2_sc2_comment7 = ChatEntry( False, "{b}PickledDragons:{/b} ok no teresa has my vote, quick and easy getaway", 2, "#000000")

#Comments in Scene 2 - Marshall Choice
default vig2_sc2_mar_comment1 = ChatEntry( False, "{b}Coriolis:{/b} yeah safe bet for sure", 2, "#000000")
default vig2_sc2_mar_comment2 = ChatEntry( False, "{b}kitcat:{/b} these aren't the outlaws you're looking for", 2, "#000000")
default vig2_sc2_mar_comment3 = ChatEntry( True, "{b}J4MIR0QU4I:{/b} meh after last time does this even make sense for the crew?", 2, "#000000", "vig2_sc2_mar_consistency")
default vig2_sc2_mar_J4MresponseMAR = ChatEntry( False, "{b}J4MIR0QU4I:{/b} booooooo", 2, "#000000")
default vig2_sc2_mar_J4MresponseOUT = ChatEntry( False, "{b}J4MIR0QU4I:{/b} hell yeah, this is why I'm here!", 2, "#000000")
default vig2_sc2_mar_comment4 = ChatEntry( False, "{b}_lostinmetr0:{/b} wdym", 2, "#000000")
default vig2_sc2_mar_comment5 = ChatEntry( False, "{b}Coriolis:{/b} last stream took a darker turn", 2, "#000000")
default vig2_sc2_mar_comment6 = ChatEntry( False, "{b}_lostinmetr0:{/b} ohh okok", 2, "#000000")
default vig2_sc2_mar_comment7 = ChatEntry( False, "{b}shnzi:{/b} me too I picked bribe", 2, "#000000")
default vig2_sc2_mar_comment8 = ChatEntry( False, "{b}turb0g00se:{/b} smart man, I also hate my job", 2, "#000000")
default vig2_sc2_mar_comment9 = ChatEntry( False, "{b}AFKangel:{/b} for sure he took the money and ran", 2, "#000000")
default vig2_sc2_mar_comment10 = ChatEntry( False, "{b}bacon8r_6:{/b} perfect ad time, no idea what's going on now", 2, "#000000")

#Comments in Scene 2 - Outlaw Choice
default vig2_sc2_out_comment1 = ChatEntry( False, "{b}PickledDragons:{/b} ah yes exactly, better have your fate in your own hands", 2, "#000000")
default vig2_sc2_out_comment2 = ChatEntry( False, "{b}Coriolis:{/b} cant help but agree", 2, "#000000")
default vig2_sc2_out_comment3 = ChatEntry( False, "{b}AFKangel:{/b} lmao teresa always makes it fun", 2, "#000000")
default vig2_sc2_out_comment4 = ChatEntry( False, "{b}turb0g00se:{/b} YES literally whas the worst that can happen", 2, "#000000")
default vig2_sc2_out_comment5 = ChatEntry( True, "{b}shnzi:{/b} hey [player], are you romancing teresa?", 2, "#000000", "vig2_sc2_out_romance")
default vig2_sc2_out_comment6 = ChatEntry( False, "{b}kitcat:{/b} it's hard to, unless you make some whack choices", 2, "#000000")
default vig2_sc2_out_comment7 = ChatEntry( False, "{b}bacon8r_6:{/b} don't understand why more people don't pick what an actual outlaw crew would do", 2, "#000000")
default vig2_sc2_out_comment8 = ChatEntry( False, "{b}PickledDragons:{/b} even Jennica's having fun - crew bonding at max capacity", 2, "#000000")
default vig2_sc2_out_comment9 = ChatEntry( False, "{b}R4dioRobbie:{/b} RUBES", 2, "#000000")
default vig2_sc2_out_comment10 = ChatEntry( False, "{b}Coriolis:{/b} that was actually so cute - go team!", 2, "#000000")
default vig2_sc2_out_comment11 = ChatEntry( False, "{b}AFKangel:{/b} easy peasy", 2, "#000000")

#comments for Romance Decision
default vig2_sc2_romance_ama1 = ChatEntry (False, "{b}PickledDragons:{/b} Yessss! OMG I want the Ama drama so bad!", 0, "#000000ff")
default vig2_sc2_romance_ama2 = ChatEntry (False, "{b}kitcat:{/b} Turn the big bad with love? Dig it!", 0, "#000000ff")
default vig2_sc2_romance_pilot1 = ChatEntry(False, "{b}Coriolis:{/b} Jennica ftw!", 0, "#000000ff")
default vig2_sc2_romance_engineer1 = ChatEntry(False, "{b}KitKat:{/b} Crazy engineer ftw!", 0, "#000000ff")

#Comments in Scene 3
default vig2_sc3_comment1 = ChatEntry( False, "{b}Coriolis:{/b} yeah classic bad guy gates", 2, "#000000")
default vig2_sc3_comment2 = ChatEntry( False, "{b}shnzi:{/b} character = bad is the same as character = has giant castle made of gold in generally poor area", 2, "#000000")
default vig2_sc3_comment3 = ChatEntry( False, "{b}kitcat:{/b} brat", 2, "#000000")
default vig2_sc3_comment4 = ChatEntry( False, "{b}AFKangel:{/b}: :P", 2, "#000000")

#Comments in Scene 3 - Lore
default vig2_sc3_lore_comment1 = ChatEntry( False, "{b}turb0g00se:{/b} when are we going to find out what happened at tiber iii?", 2, "#000000")
default vig2_sc3_lore_comment2 = ChatEntry( False, "{b}_lostinmetr0:{/b} the running gag must run", 2, "#000000") 

#Comments in Scene 3 - Threaten
default vig2_sc3_threat_comment1 = ChatEntry( False, "{b}R4dioRobbie:{/b} literally just doing his job", 2, "#000000")
default vig2_sc3_threat_comment2 = ChatEntry( False, "{b}_lostinmetr0:{/b} bruh so are we, just let us through", 2, "#000000")
default vig2_sc3_threat_comment3 = ChatEntry( False, "{b}J4MIR0QU4I:{/b} exaaaaactly^^", 2, "#000000")

#Comments in Scene 4
default vig2_sc4_comment1 = ChatEntry( True, "{b}Coriolis:{/b} is there a gameplan here?", 2, "#000000", "vig2_sc4_gameplan")
default vig2_sc4_comment2 = ChatEntry( False, "{b}kitcat:{/b} aaaahhh, no! I don't want Matticus knowing about the lil guy!", 2, "#000000")
default vig2_sc4_comment3 = ChatEntry( False, "{b}PickledDragons:{/b} better the devil you know, especially when Deadeye's involved", 2, "#000000")
default vig2_sc4_comment4 = ChatEntry( False, "{b}shnzi:{/b} smart to ally with Matticus, but not a popular choice", 2, "#000000")
default vig2_sc4_comment5 = ChatEntry( False, "{b}AFKangel:{/b} can't start a villain arc without a little villainty", 2, "#000000")
default vig2_sc4_comment6 = ChatEntry( False, "{b}PickledDragons:{/b} agreed and literally no one plays like that, makes it feel like these guys weren't even outlaws to begin with", 2, "#000000")
default vig2_sc4_comment7 = ChatEntry( False, "{b}Coriolis:{/b} yeah but they're \"doing better\"", 2, "#000000")
default vig2_sc4_comment8 = ChatEntry( False, "{b}turb0g00se:{/b} true, but literally everyone plays like matticus was never their ally", 2, "#000000")
default vig2_sc4_comment9 = ChatEntry( False, "{b}R4dioRobbie:{/b} yeah agreed, ngl that's how I did the chapter", 2, "#000000")
default vig2_sc4_comment10 = ChatEntry( False, "{b}shnzi:{/b} same", 2, "#000000")

#Comments in Scene 4 - response to Matticus question
default vig2_sc4_against_comment1 = ChatEntry( False, "{b}shnzi:{/b} yeah I can't stand the guy", 2, "#000000")
default vig2_sc4_against_comment2 = ChatEntry( False, "{b}kitcat:{/b} literally have no idea what he gives you because i never side with THE skeevy slum lord", 2, "#000000")
default vig2_sc4_ally_comment1 = ChatEntry( False, "{b}PickledDragons:{/b} Exactly!! why wouldn't you use your contact", 2, "#000000")
default vig2_sc4_ally_comment2 = ChatEntry( False, "{b}bacon8r_6:{/b} ugh so glad someone is doing this, I heard you get much cooler plot points by allying matticus", 2, "#000000")
default vig2_sc4_ally_comment3 = ChatEntry( False, "{b}_lostinmetr0:{/b} he gives me the ick", 2, "#000000")
default vig2_sc4_ally_comment4 = ChatEntry( False, "{b}turb0g00se:{/b} yea but for the plot bro", 2, "#000000")

#Comments in Scene 5
default vig2_sc5_comment1 = ChatEntry( False, "{b}_lostinmetr0:{/b} okay finally the action starts", 2, "#000000")
default vig2_sc5_comment2 = ChatEntry( False, "{b}kitcat:{/b} coudlnt bring myself to lie to the little guy", 2, "#000000")
default vig2_sc5_comment3 = ChatEntry( False, "{b}J4MIR0QU4I:{/b} it's best if he just stays their ally though", 2, "#000000")
default vig2_sc5_comment4 = ChatEntry( False, "{b}kitcat:{/b} yeah but bad/good is not a thing to teach the baby", 2, "#000000")
default vig2_sc5_comment5 = ChatEntry( False, "{b}shnzi:{/b} me neither, we all agree there", 2, "#000000")
default vig2_sc5_comment6 = ChatEntry( False, "{b}turb0g00se:{/b} reginald's a mood", 2, "#000000")

#Comments in Scene 6 - Marshall Infiltration
default vig2_sc6_mar_comment1 = ChatEntry( False, "{b}Coriolis:{/b} sir stealth is back! You got really good at it in the last game", 2, "#000000")
default vig2_sc6_mar_comment2 = ChatEntry( False, "{b}shnzi:{/b} boo okay im out this is the route I did, I know how it ends", 2, "#000000")
default vig2_sc6_mar_comment3 = ChatEntry( False, "{b}PickledDragons:{/b} quick, quiet, quite the typical choice my guy", 2, "#000000")
default vig2_sc6_mar_comment4 = ChatEntry( False, "{b}turb0g00se:{/b} even reginald thinks so! my man is a voice of the people", 2, "#000000")
default vig2_sc6_mar_choice1_stun_comment1 = ChatEntry( False, "{b}R4dioRobbie:{/b} I did that too!", 2, "#000000")
default vig2_sc6_mar_choice1_bluff_comment1 = ChatEntry( False, "{b}_lostinmetr0:{/b} me too I just trust every new face that walks into my secret base >.<", 2, "#000000")
default vig2_sc6_mar_choice2_stun_comment1 = ChatEntry( False, "{b}kitcat:{/b} not stunned with the choice though", 2, "#000000")
default vig2_sc6_mar_choice2_stun_comment2 = ChatEntry( False, "{b}AFKangel:{/b} we all picked that one didn't we? :')", 2, "#000000")
default vig2_sc6_mar_choice2_stun_comment3 = ChatEntry( False, "{b}J4MIR0QU4I:{/b} we are united in our lameness <3", 2, "#000000")
default vig2_sc6_mar_choice2_dist_comment1 = ChatEntry( False, "{b}_lostinmetr0:{/b} the tried and true distract and run", 2, "#000000")
default vig2_sc6_mar_choice2_dist_comment2 = ChatEntry( False, "{b}Coriolis:{/b} a [player] classic", 2, "#000000")

#Comments in Scene 6 - Outlaw Assault
default vig2_sc6_out_comment1 = ChatEntry( False, "{b}PickledDragons:{/b} YES! Outlaws being outlaws!", 2, "#000000")
default vig2_sc6_out_comment2 = ChatEntry( False, "{b}shnzi:{/b} no clue whats gonna happen", 2, "#000000")
default vig2_sc6_out_comment3 = ChatEntry( False, "{b}xxxP0tat0Pr0phetxxx:{/b} is this the stream with the evil mc? just joined!", 2, "#000000")
default vig2_sc6_out_comment4 = ChatEntry( False, "{b}Coriolis:{/b} not evil! just...okay a little evil today", 2, "#000000")
default vig2_sc6_out_comment5 = ChatEntry( False, "{b}kitcat:{/b} oh poor MAC", 2, "#000000")
default vig2_sc6_out_comment6 = ChatEntry( False, "{b}_lostinmetr0:{/b} he's so sweet, this really shows his trust", 2, "#000000")
default vig2_sc6_out_comment7 = ChatEntry( False, "{b}AFKangel:{/b} shoot! get him! more will come!", 2, "#000000")
default vig2_sc6_out_comment8 = ChatEntry( False, "{b}R4dioRobbie:{/b} dude this isn't a quick time event.", 2, "#000000")
default vig2_sc6_out_comment9 = ChatEntry( False, "{b}AFKangel:{/b} right I just got caught up - it's so exciting", 2, "#000000")
default vig2_sc6_out_comment10 = ChatEntry( False, "{b}shnzi:{/b} Totally agree, this is way crazier than the stealth run!", 2, "#000000")
default vig2_sc6_out_shoot_comment1 = ChatEntry( False, "{b}_lostinmetr0:{/b} ah! you got him! keep going!", 2, "#000000")
default vig2_sc6_out_shoot_comment2 = ChatEntry( False, "{b}xxxP0tat0Pr0phetxxx:{/b} the horror!", 2, "#000000")
default vig2_sc6_out_shoot_comment3 = ChatEntry( False, "{b}R4dioRobbie:{/b} LOL", 2, "#000000")
default vig2_sc6_out_shoot_comment4 = ChatEntry( False, "{b}turb0g00se:{/b} who's the real deadeye here amirite", 2, "#000000")
default vig2_sc6_out_suppress_comment1 = ChatEntry( False, "{b}PickledDragons:{/b} bruh you already killed 2 guys", 2, "#000000")
default vig2_sc6_out_suppress_comment2 = ChatEntry( False, "{b}xxxP0tat0Pr0phetxxx:{/b} fr", 2, "#000000")
default vig2_sc6_out_comment11 = ChatEntry( False, "{b}AFKangel:{/b} I told you more would come!", 2, "#000000")
default vig2_sc6_out_comment12 = ChatEntry( False, "{b}kitcat:{/b} THE GRENADE", 2, "#000000")
default vig2_sc6_out_comment13 = ChatEntry( False, "{b}Coriolis:{/b} oh hell now I'm all caught up in it - get down lmao!!", 2, "#000000")
default vig2_sc6_out_comment14 = ChatEntry( False, "{b}turb0g00se:{/b} who needs the quick and quiet route haha", 2, "#000000")
default vig2_sc6_out_comment15 = ChatEntry( False, "{b}_lostinmetr0:{/b} what a mess!", 2, "#000000")
default vig2_sc6_out_comment16 = ChatEntry( False, "{b}PickledDragons:{/b} well you got us this far...time to execute", 2, "#000000")
default vig2_sc6_out_comment17 = ChatEntry( False, "{b}Coriolis:{/b} bro so casually drops a \"time to execute\"", 2, "#000000")
default vig2_sc6_out_comment18 = ChatEntry( False, "{b}PickledDragons:{/b} lol well the situation calls for it!", 2, "#000000")
default vig2_sc6_out_execute_comment1 = ChatEntry( False, "{b}xxxP0tat0Pr0phetxxx:{/b} yeah!", 2, "#000000")
default vig2_sc6_out_execute_comment2 = ChatEntry( False, "{b}bacon8r_6:{/b} YA", 2, "#000000")
default vig2_sc6_out_execute_comment3 = ChatEntry( False, "{b}Coriolis:{/b} OMG", 2, "#000000")
default vig2_sc6_out_execute_comment4 = ChatEntry( False, "{b}_lostinmetr0:{/b} I cant watch!", 2, "#000000")
default vig2_sc6_out_execute_comment5 = ChatEntry( False, "{b}shnzi:{/b} girl WHAT", 2, "#000000")
default vig2_sc6_out_execute_comment6 = ChatEntry( False, "{b}PickledDragons:{/b} WOW", 2, "#000000")
default vig2_sc6_out_execute_comment7 = ChatEntry( False, "{b}R4dioRobbie:{/b} rip that guy", 2, "#000000")
default vig2_sc6_out_execute_comment8 = ChatEntry( False, "{b}turb0g00se:{/b} COLD", 2, "#000000")
default vig2_sc6_out_execute_comment9 = ChatEntry( False, "{b}AFKangel:{/b} !!!!!!!!!", 2, "#000000")
default vig2_sc6_out_execute_comment10 = ChatEntry( False, "{b}shnzi:{/b} NOT THE \"I HAVE KIDS\" CARD", 2, "#000000")
default vig2_sc6_out_execute_comment11 = ChatEntry( False, "{b}xxxP0tat0Pr0phetxxx:{/b} no regrets", 2, "#000000")
default vig2_sc6_out_execute_comment12 = ChatEntry( False, "{b}R4dioRobbie:{/b} don't you mean \"no rugrats\" because now the kids don't have a father", 2, "#000000")
default vig2_sc6_out_execute_comment13 = ChatEntry( False, "{b}turb0g00se:{/b} BRO HAHA WHAT", 2, "#000000")
default vig2_sc6_out_execute_comment14 = ChatEntry( False, "{b}kitcat:{/b} dead man tells no tales...and is no longer a father", 2, "#000000")
default vig2_sc6_out_execute_comment15 = ChatEntry( False, "{b}_lostinmetr0:{/b} LOL we're all awful, aren't we?", 2, "#000000")
default vig2_sc6_out_spare_comment1 = ChatEntry( False, "{b}PickledDragons:{/b} lobs grenades and kills 99\% of the staff but the last guy? Nah he's good", 2, "#000000")
default vig2_sc6_out_spare_comment2 = ChatEntry( False, "{b}xxxP0tat0Pr0phetxxx:{/b} omg cmon", 2, "#000000")
default vig2_sc6_out_spare_comment3 = ChatEntry( False, "{b}turb0g00se:{/b} REGGIEEEEEE", 2, "#000000")
default vig2_sc6_out_spare_comment4 = ChatEntry( False, "{b}bacon8r_6{/b} HES SO REAL FOR THAT", 2, "#000000")
default vig2_sc6_out_spare_comment5 = ChatEntry( False, "{b}kitcat:{/b} \"he didn't need to die\" okay neither did the minimum 4 other people we just blasted", 2, "#000000")
default vig2_sc6_out_spare_comment6 = ChatEntry( False, "{b}shnzi:{/b} \"we\"? none of us killed anyone if we played this chapter befr", 2, "#000000")
default vig2_sc6_out_spare_comment7 = ChatEntry( False, "{b}_lostinmetr0:{/b} hey hey - we're all a team now: a chat united in destruction", 2, "#000000")

#Comments for Scene 7
default vig2_sc7_comment1 = ChatEntry( False, "{b}AFKangel:{/b} omg no not the aid shipment", 2, "#000000")
default vig2_sc7_comment2 = ChatEntry( False, "{b}turb0g00se:{/b} poor community needing aid vs one robot", 2, "#000000")
default vig2_sc7_comment3 = ChatEntry( False, "{b}_lostinmetr0:{/b} LOL omg true", 2, "#000000")
default vig2_sc7_comment4 = ChatEntry( False, "{b}PickledDragons:{/b} again reginald making sense", 2, "#000000")
default vig2_sc7_comment5 = ChatEntry( False, "{b}bacon8r_6:{/b} mc getting called OUT", 2, "#000000")
default vig2_sc7_comment6 = ChatEntry( False, "{b}Coriolis:{/b} poor MAC cant compute", 2, "#000000")
default vig2_sc7_comment7 = ChatEntry( False, "{b}kitcat:{/b} he's just a lil guy doing his best!", 2, "#000000")

#Comments for Scene 7 - Marshall
default vig2_sc7_mar_comment1 = ChatEntry( False, "{b}J4MIR0QU4I:{/b} makes sense", 2, "#000000")
default vig2_sc7_mar_comment2 = ChatEntry( False, "{b}_lostinmetr0:{/b} but how are we gonna make it out now?", 2, "#000000")
default vig2_sc7_mar_comment3 = ChatEntry( False, "{b}turb0g00se:{/b} reginald about to earn his paycheck", 2, "#000000")
default vig2_sc7_mar_stun_comment1 = ChatEntry( False, "{b}bacon8r_6:{/b} rip", 2, "#000000")
default vig2_sc7_mar_bribe_comment1 = ChatEntry( False, "{b}Coriolis:{/b} clever!", 2, "#000000")
default vig2_sc7_mar_bribe_comment2 = ChatEntry( False, "{b}kitcat:{/b} yeah I stunned him!", 2, "#000000")
default vig2_sc7_mar_comment4 = ChatEntry( False, "{b}AFKangel:{/b} OH COME ON", 2, "#000000")
default vig2_sc7_mar_comment5 = ChatEntry( False, "{b}PickledDragons:{/b} CLASSIC paragon game cop out making the good choice have NO consequences", 2, "#000000")
default vig2_sc7_mar_comment6 = ChatEntry( False, "{b}R4dioRobbie:{/b} totally agree", 2, "#000000")
default vig2_sc7_mar_comment7 = ChatEntry( False, "{b}Coriolis:{/b} I gotta agree too - was hoping the good choice would at least be interesting consequence-wise", 2, "#000000")
default vig2_sc7_mar_comment8 = ChatEntry( False, "{b}turb0g00se:{/b} lets be honest, we all knew this was coming.", 2, "#000000")
default vig2_sc7_mar_comment9 = ChatEntry( False, "{b}_lostinmetr0:{/b} this team really relies on lucking into helpful people lol", 2, "#000000")

#Comments for Scene 7 - Outlaw
default vig2_sc7_out_comment1 = ChatEntry( True, "{b}R4dioRobbie:{/b} WEVE COME THIS FAR", 2, "#000000", "vig2_sc7_toofar")
default vig2_sc7_out_comment2_shnzi = ChatEntry( False, "{b}shnzi:{/b} literally the most black and white decision of the game", 2, "#000000")
default vig2_sc7_out_comment2_AFK = ChatEntry( False, "{b}AFKangel:{/b} literally the most black and white decision of the game", 2, "#000000")
default vig2_sc7_out_comment3 = ChatEntry( False, "{b}kitcat:{/b} and we have shown our blackened heart >:)", 2, "#000000")
default vig2_sc7_out_comment4 = ChatEntry( False, "{b}bacon8r_6:{/b} F", 2, "#000000")
default vig2_sc7_out_comment5 = ChatEntry( False, "{b}turb0g00se:{/b} my condolences but...we doing the bad guy thing", 2, "#000000")
default vig2_sc7_out_comment6 = ChatEntry( False, "{b}_lostinmetr0:{/b} I think youre literally the first person that was like \" nah f those sick people\"", 2, "#000000")
default vig2_sc7_out_comment7 = ChatEntry( False, "{b}xxxP0tat0Pr0phetxxx:{/b} LOL you might be right", 2, "#000000")
default vig2_sc7_out_comment8 = ChatEntry( False, "{b}PickledDragons:{/b} dude this is awesome", 2, "#000000")
default vig2_sc7_out_comment9 = ChatEntry( False, "{b}Coriolis:{/b} awesome?", 2, "#000000")
default vig2_sc7_out_comment10 = ChatEntry( False, "{b}PickledDragons:{/b} nonono not that we killed a bunch of sick people", 2, "#000000")
default vig2_sc7_out_comment11 = ChatEntry( False, "{b}Coriolis:{/b} good LOL", 2, "#000000")
default vig2_sc7_out_comment12 = ChatEntry( False, "{b}PickledDragons:{/b} I'm just having fun that we're picking things a lot of people don't", 2, "#000000")
default vig2_sc7_out_comment13 = ChatEntry( False, "{b}turb0g00se:{/b} same!!", 2, "#000000")
default vig2_sc7_out_comment14 = ChatEntry( False, "{b}Coriolis:{/b} yeah [player]'s fun to watch", 2, "#000000")
default vig2_sc7_out_comment15 = ChatEntry( False, "{b}J4MIR0QU4I:{/b} yes!", 2, "#000000")
default vig2_sc7_out_comment16 = ChatEntry( False, "{b}R4dioRobbie:{/b} LIVE STREAM backwards iS EVIL (maerts) >:)", 2, "#000000")
default vig2_sc7_out_comment17 = ChatEntry( False, "{b}turb0g00se:{/b} that's so corny", 2, "#000000")
default vig2_sc7_out_comment18 = ChatEntry( False, "{b}_lostinmetr0:{/b} no rugrats for real now", 2, "#000000")
default vig2_sc7_out_comment19_shnzi = ChatEntry( False, "{b}shnzi:{/b} omg true rip", 2, "#000000")
default vig2_sc7_out_comment19_bacon = ChatEntry( False, "{b}bacon8r_6:{/b} omg true rip", 2, "#000000")
default vig2_sc7_out_comment20 = ChatEntry( False, "{b}_lostinmetr0:{/b} my adrenaline is so high right now", 2, "#000000")
default vig2_sc7_out_comment21 = ChatEntry( False, "{b}kitcat:{/b} SAME", 2, "#000000")
default vig2_sc7_out_comment22 = ChatEntry( False, "{b}xxxP0tat0Pr0phetxxx:{/b} last man standing, you know what to do", 2, "#000000")
default vig2_sc7_out_comment23 = ChatEntry( False, "{b}AFKangel:{/b} GUYS WE CANT", 2, "#000000")
default vig2_sc7_out_comment24 = ChatEntry( False, "{b}turb0g00se:{/b} our last shred of dignity", 2, "#000000")
default vig2_sc7_out_coerce_comment1 = ChatEntry( False, "{b}_lostinmetr0:{/b} yeah honestly we've done enough damage to these humanitarians", 2, "#000000")
default vig2_sc7_out_coerce_comment2 = ChatEntry( False, "{b}R4dioRobbie:{/b} mmm maybe", 2, "#000000")
default vig2_sc7_out_coerce_comment3 = ChatEntry( False, "{b}AFKangel:{/b} LOL MAYBE?", 2, "#000000")
default vig2_sc7_out_coerce_comment4 = ChatEntry( False, "{b}R4dioRobbie:{/b} I'm getting in the outlaw spirit!", 2, "#000000")
default vig2_sc7_out_execute_comment1 = ChatEntry( False, "{b}bacon8r_6:{/b} NO SURVIVORS", 2, "#000000")
default vig2_sc7_out_execute_comment2 = ChatEntry( False, "{b}J4MIR0QU4I:{/b} humanitarians? Not on our watch", 2, "#000000")
default vig2_sc7_out_execute_comment3 = ChatEntry( False, "{b}_lostinmetr0:{/b} we stand for justice...sort of", 2, "#000000")
default vig2_sc7_out_execute_comment4 = ChatEntry( True, "{b}PickledDragons:{/b} Chat, time to RIP for our humanitarians", 2, "#000000", "vig2_sc7_rips")
default vig2_sc7_out_comment25 = ChatEntry( False, "{b}bacon8r_6:{/b} And there she blows", 2, "#000000")
default vig2_sc7_out_comment26 = ChatEntry( False, "{b}J4MIR0QU4I:{/b} LOL omg I feel so bad for laughing", 2, "#000000")
default vig2_sc7_out_comment27 = ChatEntry( False, "{b}R4dioRobbie:{/b} cmon Jennica, we're all on board", 2, "#000000")
default vig2_sc7_out_comment28 = ChatEntry( False, "{b}turb0g00se:{/b} yeah go team \"dgaf like reginald\"", 2, "#000000")

#Comments for Marshall Epilogue
default vig2_epilogue_mar_comment1 = ChatEntry( False, "{b}turb0g00se:{/b} for all that tension it ended in a low key dull place", 2, "#000000")
default vig2_epilogue_mar_comment2 = ChatEntry( False, "{b}Coriolis:{/b} yea the storytelling got a bit dicey at the end there", 2, "#000000")
default vig2_epilogue_mar_comment3 = ChatEntry( False, "{b}_lostinmetr0:{/b} at least we stayed true to ourselves though", 2, "#000000")
default vig2_epilogue_mar_comment4 = ChatEntry( False, "{b}kitcat:{/b}anti-hero vibes, but more \"hero\" than \"anti\"", 2, "#000000")
default vig2_epilogue_mar_comment5 = ChatEntry( False, "{b}AFKangel:{/b} oh matticus big mad", 2, "#000000")
default vig2_epilogue_mar_comment6 = ChatEntry( False, "{b}R4dioRobbie:{/b} at least those sick people aren't the big sad now", 2, "#000000")
default vig2_epilogue_mar_comment7 = ChatEntry( False, "{b}turb0g00se:{/b} LOL", 2, "#000000") 
default vig2_epilogue_mar_comment8 = ChatEntry( False, "{b}J4MIR0QU4I:{/b} way more chill than last time", 2, "#000000")
default vig2_epilogue_mar_comment9 = ChatEntry( False, "{b}Coriolis:{/b} okay guys! Chat next week!", 2, "#000000")
default vig2_epilogue_mar_comment10 = ChatEntry( False, "{b}AFKangel:{/b} yeah sure!", 2, "#000000")
default vig2_epilogue_mar_comment11 = ChatEntry( False, "{b}_lostinmetr0:{/b} have a great week everyone!", 2, "#000000")
default vig2_epilogue_mar_comment12 = ChatEntry( False, "{b}kitcat:{/b} catch ya on the flip side!", 2, "#000000")

#Comments for Outlaw Epilogue
default vig2_epilogue_out_comment1 = ChatEntry( False, "{b}AFKangel:{/b} what a wild ride", 2, "#000000")
default vig2_epilogue_out_comment2 = ChatEntry( False, "{b}_lostinmetr0:{/b} we'll make matticus indirectly aid in saving the universe", 2, "#000000")
default vig2_epilogue_out_comment3 = ChatEntry( False, "{b}kitcat:{/b} matticus loves Mac too im convinced", 2, "#000000")
default vig2_epilogue_out_comment4 = ChatEntry( False, "{b}J4MIR0QU4I:{/b} how can he not?", 2, "#000000")
default vig2_epilogue_out_comment5 = ChatEntry( False, "{b}PickledDragons:{/b} I feel exhausted that was such a roller coaster", 2, "#000000")
default vig2_epilogue_out_comment6 = ChatEntry( True, "{b}Coriolis:{/b} you're telling me! Not how we typically do things at all...right cap?", 2, "#000000", "vig2_epilogue_outlaw")
default vig2_epilogue_out_comment7 = ChatEntry( False, "{b}_lostinmetr0:{/b} but I had so much fun honestly", 2, "#000000")
default vig2_epilogue_out_comment8 = ChatEntry( False, "{b}xxxP0tat0Pr0phetxxx:{/b} yeah this chat is the best yall are too funny", 2, "#000000")
default vig2_epilogue_out_comment9 = ChatEntry( False, "{b}turb0g00se:{/b} I hope next week is even more crazy", 2, "#000000")
default vig2_epilogue_out_comment10 = ChatEntry( False, "{b}bacon8r_6:{/b} hard to top murdering a bunch of humanitarians AND annihilating a planet of poor people overrun with plague", 2, "#000000")
default vig2_epilogue_out_comment11 = ChatEntry( False, "{b}shnzi:{/b} bro when you say it like that I sorta feel bad", 2, "#000000")
default vig2_epilogue_out_comment12 = ChatEntry( False, "{b}R4dioRobbie:{/b} no rugrats!", 2, "#000000")
default vig2_epilogue_out_comment13 = ChatEntry( False, "{b}turb0g00se:{/b} LOL", 2, "#000000")
default vig2_epilogue_out_comment14 = ChatEntry( False, "{b}shnzi:{/b} yeah true time to channel my inner outlaw and out of sight out of mind it", 2, "#000000")
default vig2_epilogue_out_comment15 = ChatEntry( False, "{b}PickledDragons:{/b} plus we get to see where this matticus allyship goes", 2, "#000000")
default vig2_epilogue_out_comment16 = ChatEntry( False, "{b}AFKangel:{/b} even if it goes nowhere, at least we tried?", 2, "#000000")
default vig2_epilogue_out_comment17 = ChatEntry( False, "{b}kitcat:{/b} agreed!", 2, "#000000")
default vig2_epilogue_out_comment18 = ChatEntry( False, "{b}Coriolis:{/b} for everyone wanting to see the next stream - we meet at this time every first Friday of the month when the new episode drops", 2, "#000000")
default vig2_epilogue_out_comment19 = ChatEntry( False, "{b}_lostinmetr0:{/b} oh thanks! I'm gonna send the link to a couple buddies", 2, "#000000")
default vig2_epilogue_out_comment20 = ChatEntry( False, "{b}bacon8r_6:{/b} same!", 2, "#000000")
default vig2_epilogue_out_comment21 = ChatEntry( False, "{b}shnzi:{/b} oh my gosh yeah literally had my heart racing", 2, "#000000")
default vig2_epilogue_out_comment22 = ChatEntry( False, "{b}AFKangel:{/b} we should start a reddit thread or something", 2, "#000000")
default vig2_epilogue_out_comment23 = ChatEntry( False, "{b}turb0g00se:{/b} that's a good idea!", 2, "#000000")
default vig2_epilogue_out_comment24 = ChatEntry( False, "{b}PickledDragons:{/b} totally! we can post our anti-humanitarian agenda there", 2, "#000000")
default vig2_epilogue_out_comment25 = ChatEntry( False, "{b}turb0g00se:{/b} LOL >:)", 2, "#000000")
default vig2_epilogue_out_comment26 = ChatEntry( False, "{b}shnzi:{/b} have a great week everyone!", 2, "#000000")
default vig2_epilogue_out_comment27 = ChatEntry( False, "{b}_lostinmetr0:{/b} see you soon!", 2, "#000000")

#Comments for Outlaw Epilogue RIPs
default vig2_epilogue_out_rips1 = ChatEntry( False, "{b}turb0g00se:{/b} RIP", 2, "#000000")
default vig2_epilogue_out_rips2 = ChatEntry( False, "{b}AFKangel:{/b} rip", 2, "#000000")
default vig2_epilogue_out_rips3 = ChatEntry( False, "{b}shnzi:{/b} ripperoo", 2, "#000000")
default vig2_epilogue_out_rips4 = ChatEntry( False, "{b}xxxP0tat0Pr0phetxxx:{/b} Fs", 2, "#000000")
default vig2_epilogue_out_rips5 = ChatEntry( False, "{b}bacon8r_6:{/b} rest", 2, "#000000")
default vig2_epilogue_out_rips6 = ChatEntry( False, "{b}_lostinmetr0:{/b} ripperoni", 2, "#000000")
default vig2_epilogue_out_rips7 = ChatEntry( False, "{b}J4MIR0QU4I:{/b} R I P", 2, "#000000")




###################### OLD COMMENTS FROM PROTOTYPING########################


#comments for decision 2
default pdLovesChaos = ChatEntry (False, "{b}PickledDragons:{/b} chaos chaos chaos chaos", 0, "#000000ff")
default kkMac = ChatEntry (False, "{b}KitKat:{/b} Oh no Mac!", 0, "#000000ff")
#comments for outlaw decision 2
default pdOutlawD2 = ChatEntry (False, "{b}PickledDragons:{/b} CHAOS CHAOS CHAOS", 0, "#000000ff")
default csOutlawD2 = ChatEntry(True, "{b}Coriolis:{/b} bahahaha just like my DnD group's stealth rols", 0, "#000000ff", "CoriolisTalksDnDOutlaw")

#comments for marshal decision 2
default csMarshalD2 = ChatEntry(True, "{b}Coriolis:{/b} Jennica the top-tier support character of the DnD party", 0, "#000000ff", "CoriolisTalksDnDMarshal")
default kkMarshalD2 = ChatEntry(False, "{b}KitKat:{/b} Awww I wanted to see what Teresa had up her sleeve", 0, "#000000ff" )

#comments for CoriolisDnD talk
default csDnDvg2 = ChatEntry (False, "{b}Coriolis:{/b} nooooo hit her up again, make it happen!", 0, "#000000ff")
default csDnD2vg2 = ChatEntry (False, "{b}Coriolis:{/b} same! I go cleric a lot of the time, though I typically spec it to be effective in combat too", 0, "#000000ff" )
default kkDnDvg2 = ChatEntry (True, "{b}KitKat:{/b} What class do you think [player] would run?", 0, "#000000ff", "DnDClassTalk")
default kkDnDvg2play = ChatEntry (True, "{b}KitKat:{/b} What class do you think [player] runs?", 0, "#000000ff", "DnDClassTalkplay")
default pdDnDvg2 = ChatEntry (False, "{b}PickledDragons:{/b} I'm seeing Paladin for some reason personally", 0, "#000000ff")
default pdDnD2vg2 = ChatEntry (False, "{b}PickledDragons:{/b} Called it!", 0, "#000000ff")


