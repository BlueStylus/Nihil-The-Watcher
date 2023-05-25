label prePlay:
    $ pause_unlocked = True
    $ noprofile_true = True
    $ ctcOn = True
    window show
    "This story is a work of fiction."
    "Any resemblance to actual events, locations or people is entirely coincidental."
    "This visual novel is roughly a 5 minute game meant to be enjoyed over 30 minutes."
    "To meet this goal, we have taken many steps to encourage the player to progress slowly."
    "For example, some features common to visual novels, such as skipping dialogue, have been disabled for the first playthrough."
    "A golden ring indicator will appear in the bottom right to let you know when you should advance dialogue."
    "Please allow our animations and transitions to fully finish playing to increase your immersion."
    "To learn more about how to progress the story as intended, please consult the Help section in the pause menu."
    "Thank you for bearing with us, and without further ado, please enjoy our demo of Nihil."
    $ _history_list.clear()
    window hide Dissolve(3.0)
    return

################################################################################

label theWatcher:
    $ back_button = True
    $ history_button = True
    $ auto_mode_button = True
    if persistent.completed:
        $ fastforward_button = True
        $ newNote = True
    if played_through:
        $ fastforward_button = True
        $ newNote = True

    $ phone_menu_button_turnedOn = True
    $ load_button_turnedOn = True
    $ save_load_button_turnedOn = True
    $ mapUnlocked = True
    $ library_show = False
    $ noprofile_true = False
    $ ctcOn = False

    centered "2018."
    #$ narrator.pop_history() #removes previous dialogue from the history logs

    scene bg campground-day with slower_dis
    play music "music/in-the-forest-ambient.mp3" fadein 10.0
    $ right_menu_turnedOn = True
    $ right_menu = True
    $ quick_menu = True
    $ pause_unlocked = True
    $ noprofile_true = True
    $ ctcOn = True
    $ renpy.block_rollback()
    window show
    "Pale sunlight illuminates a clearing in the forest."
    "A designated camping area, maintained by the provincial government – though it's lush with vegetation..."
    "...it's clearly demarcated for people to start fires in some places, comes with benches, and even some grills."
    "Nobody is around. Not many people camp around this time of the year."
    "The only sounds around are the wind, the occasional wave from the distant lake, and some feral wildlife."
    play sound "sfx/car stopping.mp3"
    "A car cuts through the wilderness in silence, smoothly gliding over the beaten path."
    "After some time, it slowly turns to the side, running over some grass, before coming to a stop upon the camping area."
    play sound "sfx/car door open.mp3"
    "The car turns off, and from the driver seat door emerges a lion, before taking a deep breath and stretching."

    $ noprofile_true = False
    show screen profile(jo0) with dis
    show screen profile(jo1)
    jo "We're here."
    play sound "sfx/car door.mp3"
    show screen profile(jo0)
    "The passenger side door opens, and out walks a deer. He stretches as well."
    show ja 0 with dis
    ja "Mm... Nice and chilly, huh... "
    show screen profile(jo2)
    jo "No amount of 'the temperatures rise around this time of the year' will ever save us from the fact that this is still Canada."
    show screen profile(jo1)
    jo "It's still warmer than our little town – I guess you're used to the city, huh. At least we brought tents and plenty of blankets and firewood to make a fire with."
    jo "You made sure to bundle up well, right?"
    show screen profile(jo0)
    "The deer looks down at the jacket he's wearing."
    show ja 2
    ja "Yeah."

    play sound "sfx/car door.mp3"
    show ja 0 at three with move
    "The other doors of the car open and out walk a salamander, a bear and a fox."
    show b 0 at five with dis
    show m 0 at seven with dis
    show t 0 at nine behind m with dis
    "They all stretch out, enjoying the fact that they can move now, while the salamander rubs his hands together."
    show b 4
    b "Brrr... I really don't think my people were meant to live in this area of the world... "
    show screen profile(jo1)
    jo "Do you want a blanket, Brett?"
    show screen profile(jo0)
    show b 5
    b "Nah, don't worry man, I'll be fine! Just gonna take some time for me to get used to it, is all... "
    jo "Mm."
    "The lion nods."
    show screen profile(jo3)
    jo "Just sit somewhere while I unpack, then."
    play sound "sfx/car door close.mp3"

    show screen profile(jo4) with dis
    scene bg trunk with dis
    play sound "sfx/car trunk.mp3"
    "He closes the door of his car and walks to the back, opening the trunk and examining its contents."
    "Plenty of food to grill, plenty of firewood to burn, some coal, some fuel and alcohol."
    "Tents, blankets, sleeping bags."
    "Good preparation."
    show t 1 at nine with dis
    show screen profile(jo0)
    t "Um, what do I help with?"
    "Joshua looks at him before pointing at the containers with their food."
    show screen profile(jo5)
    jo "Take these to the grill. You can handle the weight."
    show t 2
    t "Alright!"
    show screen profile(jo0)
    play sound "sfx/footsteps on gravel away.mp3"
    hide t with dis
    "Tyler reaches into the back and starts taking containers out, dutifully carrying them one by one."

    show screen profile(jo1)
    jo "James."
    show screen profile(jo0)
    "The deer turns to face him."
    show ja 5 with dis
    ja "Yeah?"
    show screen profile(jo1)
    jo "Could you help me with a thing? We need to set up the tents now, while there's sunlight out."
    show screen profile(jo0)
    show ja 1
    ja "Oh, sure. Lemme just... "
    hide ja with dis
    play sound "sfx/moving items.mp3"
    "He reaches into the trunk and pulls out their tents – three of them. They're sleeping in pairs, and one person is sleeping alone."
    "They haven't decided on the order of the pairs yet."
    show screen profile(jo1)
    jo "Alright. Where are we making the fire?"
    show screen profile(jo0)
    show ja 5 with dis
    ja "Right... there, no?"
    "James points to a circle of stones in the middle of the clearing, that has some ash inside."
    show screen profile(jo6)
    show ja 0
    jo "Well, that's convenient. Unfortunate it wasn't completely cleaned out, but what can you do."

    show screen profile(jo4) with dis
    scene bg campground-day with dis
    play sound "sfx/footsteps on leaves towards.mp3"
    "Joshua carries the tents to the area and sets them out around the fireplace, starting to pitch them one by one."
    "James walks up to him and stands by him as he works in silence, tapping his foot against the ground."
    show ja 6 with dis
    show screen profile(jo7)
    ja "Didn't you need help?"
    "Joshua looks up at him for a few seconds."
    show screen profile(jo8)
    jo "... huh?"
    show ja 7
    show screen profile(jo9) with dis
    "He eventually facepalms."
    jo "Right."
    show screen profile(jo10) with dis
    "He nods at the unmade tent opposite of his own."
    jo "If you could get to working on that one, please."
    show ja 2
    ja "You got it!"

    play sound "sfx/moving items.mp3"
    show ja 15 with dis
    show screen profile(jo4) with dis
    "James starts to work. He isn't as skilled at it as Joshua, but he does his best."
    "While he's still finishing the setting up of his tent, Joshua has finished the other two."
    show screen profile(jo1)
    jo "No, wait. You aren't supposed to twist this like that. You... "
    show ja 5 with dis
    "Joshua kneels by him and grabs his hands. Gently, he shows him the motion he has to follow."
    jo "Into this hole. Alright?"
    show ja 15 with dis
    "James nods slowly, paying attention."
    ja "Mmhmm... "
    show screen profile(jo3)
    jo "Alright, lemme see you do it, then."
    ja "I'll try."
    show screen profile(jo4)
    "Joshua lets go. After that, setting the tent up goes a lot more smoothly."
    show ja 2 with dis
    ja "Oh, there we go."
    show screen profile(jo11)
    jo "Well done."
    show ja 3
    ja "Thanks, Josh!"
    show screen profile(jo12)
    "Joshua smiles, patting James on the shoulder and getting up. The deer finishes anchoring the tent to the soil."
    play sound "sfx/footsteps on leaves away.mp3"
    "Joshua just gives him a thumbs-up over his shoulder as he walks back to the car."

    $ timeofDay = "Afternoon"
    show screen profile(jo0)
    scene bg trunk with dis
    show m 3 at eight with dis
    "By the car, Michael is checking his phone."
    m "Tch."
    show screen profile(jo1)
    jo "What is it?"
    "Joshua goes back to the trunk."
    m "Shitty fucking phone coverage here."
    show screen profile(jo6)
    jo "Which is to be expected, no? Given that we're in the middle of the forest and all."
    m "Well, yeah, of course. Doesn't make it any less sucky."
    show m 0 with dis
    "He clicks his tongue then shakes his head, pocketing his phone again."
    show screen profile(jo2)
    jo "Right. I understand."
    show m 4 with dis
    show screen profile(jo0)
    m "Besides, my parents might try to... "
    "That idea gives Joshua pause."
    show screen profile(jo13)
    jo "... right. Your parents."
    m "Yeah?"
    show m 5
    "Michael crosses his arms and looks at him. The lion nods slowly."
    show screen profile(jo14)
    jo "I understand your concern now."
    show screen profile(jo15) with dis
    jo "I hadn't considered that, sorry."
    show screen profile(jo16)
    show m 2 with dis
    m "It's whatever, man."
    show m 0 at three with move

    "Michael comes to the trunk as well."
    show screen profile(jo8) with dis
    jo "Oh, right. You remember I gave you money to buy something to drink for all of us? What did you get?"
    show m 1
    show screen profile(jo0)
    m "Oh, here."
    hide m with dis
    play sound "sfx/moving items.mp3"
    "Michael reaches into the trunk, almost jumping into the car, and moves the sleeping bags around."
    "He smirks."
    m "Padded 'em out with all this shit so they wouldn't get damaged, hehe."
    show m 6 with dis
    "As he finishes moving things around, he retrieves... several packs of canned beer."
    "Joshua blinks a few times."
    show screen profile(jo6)
    jo "Beer."
    show screen profile(jo7)
    show m 1 with dis
    m "Yeah. It's the shit people drink while grilling meat, isn't it? And this is my favorite brand."
    m "They started releasing their crap in cans recently – makes it easier and safer to lug around, yeah?"
    play sound "sfx/can set down.mp3"
    "He starts setting the packs on the ground. There's more of them than Joshua expected."
    play sound "sfx/can set down.mp3"
    show screen profile(jo8)
    jo "I see. You got a lot of them."
    m "Beer's cheap, man. And between the five of us we'll burn through this quickly."
    show m 0
    play sound "sfx/can set down.mp3"
    show screen profile(jo4)
    "Joshua can't help wondering how much of that 'us' really just means Michael."
    play sound "sfx/can set down.mp3"
    "He nods slowly."
    play sound "sfx/can set down.mp3"
    show screen profile(jo2)
    jo "That makes sense. So all the money I gave you for drinks went into this beer, then?"
    play sound "sfx/can set down.mp3"
    show m 2
    m "Yeah. It's what you gave it to me for."
    stop music fadeout 2.0
    "He finishes setting the beers on the ground and looks back up at Joshua."
    show m 7 with dis
    m "There a fucking problem with that?"
    "Joshua blinks. He crosses his arms, looking down at the beer."
    show screen profile(jo17) with dis
    jo "... no. I was just expecting something stronger. But we'll manage."
    show screen profile(jo5) with dis
    jo "This is probably better – more liquid into our bodies. Just thinking... "

    "Joshua looks to the camp and Michael's gaze follows."
    "Tyler is leaning against the stone grill, James is sitting inside a tent fiddling with a speaker, and Brett is finally getting used to the temperature while helping James."
    m "Thinking what?"
    show screen profile(jo1)
    jo "I don't think James really drinks beer. Is all."
    show m 9 with dis
    "Michael lets out a small grunt."
    m "It's always something about that fucking dude with you, isn't it? All the problems with—"
    show screen profile(jo14)
    jo "Michael."
    show screen profile(jo13)
    "Joshua closes his eyes, his tone suddenly stern."
    show m 10 with dis
    "Michael stops speaking, suddenly feeling like he's getting lectured, incapable of saying anything back."
    "Joshua opens his eyes again, casting a resolute glance at him."
    show screen profile(jo18)
    jo "Don't start. Not today, please."
    show screen profile(jo15) with dis
    "He sighs, pressing a couple of fingers against his temple. Michael looks at him solemnly."
    jo "... It isn't often that we all get to be together around this time of the year."
    show screen profile(jo18) with dis
    jo "James is usually away due to school, but he has no homework this week, so he decided to go on this two-day trip with us instead."
    jo "Nobody else has any real obligations either. So just... let's enjoy this."
    show screen profile(jo19)
    jo "Please."
    show m 4 with dis
    "Michael squeezes himself, letting out a deep breath."
    m "... alright."
    show screen profile(jo4)
    jo "Thank you."

    play music "music/in-the-forest-ambient.mp3" fadein 3.0
    play sound "sfx/moving items.mp3"
    show screen profile(jo0) with dis
    "Joshua turns back to the car, taking out sleeping bags."
    show screen profile(jo5)
    jo "Only question in my mind right now is how much we'll have to piss with all that beer."
    show m 0 with dis
    m "Heh."
    "Michael uncrosses his arms, lifting up the beers. He looks around."
    show m 1
    m "That's what all the trees around us are for, and we all have dicks."
    show m 2
    m "... We all have dicks, right?"
    show screen profile(jo6)
    jo "I wouldn't know. I haven't fucked everyone in the group or anything, and it's not a question you can casually pose to a person."
    "He takes a deep breath."
    show screen profile(jo2)
    jo "Even if you don't, I think you can just squat and it-"
    show screen profile(jo15) with dis
    jo "Why am I thinking about this?"
    show m 6 with dis
    "Michael chuckles."
    m "Hot thoughts about hot piss, huh?"
    show screen profile(jo9)
    "Joshua lightly shakes his head."
    jo "I'm just glad I brought a kettle and some things to brew a hot beverage if we get cold, or tomorrow morning, before we reach somewhere to get breakfast."
    show m 8 with dis
    m "Talking about piss got you thinking about hot drinks?"
    show screen profile(jo3) with dis
    jo "Fuck you."
    play sound "sfx/footsteps on gravel away.mp3"

    $ noprofile_true = True
    $ timeofDay = "Evening"
    hide screen profile with dis
    scene bg campground-sunset with dis
    "Joshua walks off while Michael chuckles to himself."
    "He carries the sleeping bags to the tents, putting two inside each tent – except for the odd last one out, which only gets one."
    "They all finish getting their supplies out."
    "A small, bluetooth speaker is set on a bench, connected to a phone, and they're all listening to music."
    stop music fadeout 4.0
    "It promises to be a good day, even as it starts to darken."

    scene bg black with dis
    ". . . "

    $ timeofDay = "Night"
    scene bg campground-night with dis
    play music "music/uplifting-dreams with campfire.mp3" fadein 3.0
    "Night falls, and they all sit around the fire, exchanging stories and drinking."
    "The smell of grilled, seasoned meat still fills the air, even though it's been an hour or two since they all ate."
    "Between them, a cozy, crackling fire that they occasionally toss more wood into, that keeps them warm."
    "Above them, a full moon."
    show b 1 at three with dis
    show t 7 at six with dis
    show m 14 at nine with dis
    "Michael chuckles, brandishing a half-full can of beer. He sits next to the salamander and the bear, who he pokes with his elbow."
    m "So, what was the deal with that shit again, Ty?"
    "Tyler holds a can of beer as well, taking sips out of it every now and then."
    show t 6
    t "Um... Well, the series never left Japan."
    m "Yeah?"
    t "Yeah, like... this isn't like the very old series that never left Japan because the companies were so small they couldn't afford to localize at all."
    t "This is a big company publishing this series of games, and, um, they conducted all the market research... "
    show m 8 with dis
    show t 1 with dis
    m "Oh, we're whipping out the academia terms? Alright... "
    #"The fox chuckles, leaning back."
    show m 13 with dis
    m "Keep going, Ty."
    show b 3 with dis
    "Brett smiles at the bear, sitting to the other side of him, drinking as well."
    t "Yeah, and... they just found that it wouldn't sell well at all? So much that localizing the game wouldn't be worth the effort at all."
    show t 8 with dis
    "He yawns."
    show t 9
    t "Which... sucks a bit."
    "The salamander tilts his head towards Tyler."
    show b 2
    b "Well, you can still read it, can't you, Ty? Since you speak Japanese and all."
    show t 6 with dis
    t "Well, yeah. I'm good enough at it that I understand the whole game, and I can weather the importing costs, but... "
    show m 15 with dis
    m "Mm?"
    t "It just sucks a bit, you know? Thinking that some people are just never going to play the stuff, because it's not available here... "
    play sound "sfx/can set down.mp3"
    show t 0 with dis
    "He finishes his beer, gingerly setting the can to a side."
    "Michael fetches another can and tosses it at him. He tries to catch it in mid-air and fails, the metal harmlessly bouncing off his belly."
    show t 1
    t "Ah... "
    show b 8
    b "Aren't there like... translation patches and stuff?"
    show t 5 with dis
    "Tyler's face lights up."
    t "Yeah! And, um... I may have helped with a few, extraofficially."
    t "I can't advertise being involved with that stuff too much, if I want to keep receiving free stuff from companies... but... "
    show b 9
    b "Mmhmm?"
    play sound "sfx/can drop.mp3"
    "Brett finishes his beer and tosses his can ahead, to a small pile in front of him."
    show b 1 with dis
    "Michael tosses him a can as well, and he actually manages to catch it."
    show t 4
    t "It's just not the same. It takes more effort to do, so not many people do it."
    t "You still don't have as much reach as you could by having the game officially translated... "
    play sound "sfx/can open.mp3"
    "Tyler opens his next can, taking sips out of it. He's gotten used to the flavor."
    show t 6 with dis
    t "I mean... it's better than just not having any kind of translation... but it could be better."
    show m 16
    m "Hey, everything could be better, man."
    "He lightly pokes Tyler's side with his finger, and Tyler giggles a little in response."
    show t 9 with dis
    t "... heh. Are you sure we're still talking about my games?"
    play sound "sfx/crush can.mp3"
    show m 17
    show t 1
    "Michael finishes his can, dropping it to the ground and crushing it with his foot."
    show m 13 with dis
    "The sound makes Tyler flinch slightly. The fox flops down next to the other two, looking up at the sky."
    show m 18 with dis
    m "Look at us."
    show t 4 with dis
    t "Hm?"
    show m 19 with dis
    m "We're really out in the middle of fuckin' nowhere, sitting around a campfire, and we're talking about weird Japanese videogames, huh?"
    m "Some well-adjusted adults we are, heh... "
    "He chuckles to himself."
    show t 3 with dis
    t "Oh... "
    t "Sorry, I started talking about it... "
    show b 9 with dis
    "Tyler rubs his arm. Brett pats him on the shoulder."
    b "No, no, it's alright."
    "Michael cranes his head towards the bear."
    show m 16 with dis
    m "Not sayin' anything bad about you. It's just funny to me, man. Chill out... "
    "He chuckles, trying to get up but tripping."
    show m 8 with dis
    m "Ah, shit. Probs not takin' any more beers, huh."
    show t 6 with dis
    "Tyler looks at the pile of crushed cans in front of Michael."
    show t 7
    t "Yeah, probably for the best... just sit for a bit."
    show m 14 with dis
    m "Feels good, man."
    show b 1 with dis
    b "I bet it does... "
    "The bear lightly pats Michael's shoulder. He keeps drinking his beer, holding the can with both hands, smiling."

    "Michael was right when he said all five of them would work through the beers without any problems."
    "They were almost out, and the cans around them were testament to how good they were at drinking:"
    "Michael's pile of crushed cans, Tyler's nearly organized arrangement of them, and Brett's discarded, piled up cans."
    "Joshua was also right, in that Michael was going to drink the most."
    "He easily had the most cans to his name, even if they occupied less space due to being crushed. He was drinking a lot lately."
    "Still... it's not like he was alone in that."

    scene bg bonfire with dis
    $ noprofile_true = False
    $ profileblush = True
    show screen profile(jo4)
    show ja 13 at eight with dis
    "A few feet from them, opposite from the three, were Joshua and James, sitting against each other, drinking, while looking at the fire."
    "They had a rough arrangement of cans around them, discarded wherever they fell."
    "They were too concentrated in their conversation... or what little remained of it at that moment."
    play sound "sfx/can drop roll.mp3"
    "Joshua finishes a can of beer and lets it drop to the side, with it rolling away from him before settling next to a few others."
    show screen profile(jo2)
    jo "School is treating you nicely, right?"
    show ja 8 with dis
    "His accent was slipping a bit. James takes some time to reply, holding his can intensely, blurry gaze looking at the fire."
    ja "Mmhmm... "
    show screen profile(jo4) with dis
    jo "That's good. That's good... "
    "Not that Joshua was any better, if the deep red flush on his cheeks was any indication."
    play sound "sfx/can open.mp3"
    "He grabs another can from the pack and opens it, downing half the contents with little effort."
    show screen profile(jo3) with dis
    jo "It's good that it's treating you nicely."
    ja "You just... you just get used to the workload after some time. You were right when you told me that."
    show screen profile(jo8) with dis
    jo "Did I tell you that, James?"
    show ja 9 with dis
    ja "You did. Back when I first got to New Blackden, back before I knew what I wanted to do with my life."
    show screen profile(jo4) with dis
    jo "I see, I see..."

    scene bg black with dis
    "He closes his eyes and thinks. He can't remember doing that... but there is a lot he doesn't remember at that moment."
    show screen profile(jo0) with dis
    show bg bonfire
    show ja 10 at eight
    with dis
    ja "Yeah... you helped a lot. Thank you."
    show screen profile(jo12) with dis
    jo "It's okay."
    "A small pause."
    show ja 11 with dis
    ja "What would you do if it wasn't like that?"
    show screen profile(jo4) with dis
    jo "... mm?"
    play sound "sfx/can drop.mp3"
    "The lion finishes the rest of his can, letting it roll to a side like the others."
    show ja 12 with dis
    ja "If... if school wasn't treating me nicely. What would you do?"
    show screen profile(jo17) with dis
    "Joshua takes a deep breath, looking at the fire."
    jo "I don't know, James. But I wouldn't like it."
    show ja 13 with dis
    ja "Mm... you wouldn't like it?"
    show screen profile(jo2) with dis
    jo "No. If you were having a bad time, I wouldn't like it much at all."
    show screen profile(jo4) with dis
    show ja 28 with dis
    "James tilts his can to the side, checking out the contents, looking down."
    ja "Would you... "
    show screen profile(jo0) with dis
    jo "Yeah?"
    ja "Would you take me away from it all?"
    show screen profile(jo1) with dis
    jo "What do you mean?"
    show ja 11 with dis
    ja "If I... if studying didn't work out. What if I dropped out?"
    show screen profile(jo2) with dis
    jo "You're not dropping out, James. You're doing great at it."
    show ja 12 with dis
    ja "But what if...?"
    show screen profile(jo13) with dis
    jo "..."
    show screen profile(jo18) with dis
    jo "I don't... I don't know what you want me to tell you here."
    show screen profile(jo20) with dis
    show ja 24 with dis
    ja "..."
    "A long pause. James adopts a solemn expression."
    ja "Would you take me away from it all? Like..."
    show ja 25 with dis
    ja "I don't know. Would you... rescue me from it all?"
    ja "If I didn't want to think or feel, if the weight of the world bearing down on me proved to be too much... would you take me away from it all?"
    stop music fadeout 3.0
    ja "Would you spread your wings and bring me refuge, Josh?"
    "There is no response."

    play music "music/night-forest-campfire.mp3" fadein 5.0
    show screen profile(jo19) with dis
    show ja 27 with dis
    "Joshua gingerly grabs the can from James' hands. James lets go without much resistance."
    "Their fingertips brush against each other."
    show ja 32 with dis
    jo "You've had enough to drink, James. You've always been a lightweight."
    "Joshua has had enough to drink as well. The world was blurry, and he could hardly think. He could only feel."
    "He looks at the wet edge of the can he took from James, at the droplet of beer dripping down its side... "
    "...and he brings it to his lips, downing the contents with no effort."
    play sound "sfx/can drop roll.mp3"
    "He lets that can flop down to his side as well."
    "James takes a deep breath as the can is downed."
    show ja 27 with dis
    ja "Maybe. Maybe I have."
    "They remain quiet for a few seconds."
    show screen profile(jo2) with dis
    jo "...I would."
    show ja 26 with dis
    ja "Mm...?"
    "Joshua leans back, looking wistfully at the flame."
    show screen profile(jo17) with dis
    jo "I would spread my wings and bring you refuge as long as it took, until the storm passed."
    jo "I would go through hell to bring a smile to your face. I would keep you safe, even if you want me to take you away from everything."
    jo "Even knowing that... that I shouldn't."
    show bg black with dis
    show ja 26 at six with move
    show screen profile(jo19) with dis
    "He closes his eyes."
    jo "As I always have done. As I do. As I shall always do."
    show ja 27 with dis
    "James remains quiet, weighing the words in his mind."
    show ja 13 with dis
    ja "As it has always been, as it currently is, as it shall always be."
    ja "I knew you would say that."
    show screen profile(jo4) with dis
    jo "Did you?"
    ja "I did."
    ja "..."
    show ja 14 with dis
    ja "...But I liked hearing it anyways."
    show screen profile(jo21) with dis
    "Joshua breathes softly."
    jo "I'm glad. I'm glad... "
    show bg bonfire with dis
    show ja 13 with dis
    show screen profile(jo12) with dis
    "He opens his eyes after a few moments, as he feels James leaning against his shoulder."
    "He looks at the man next to him – his eyes are closed, but from the red of his cheeks, it's clear he's drunk."
    "At least, what little red he can catch through his blurry eyesight, being drunk himself."
    show screen profile(jo20) with dis
    "Joshua feels the deer's body lightly shiver, a vibration sending ripples into his fur."
    show ja 12 with dis
    ja "... "
    show screen profile(jo8) with dis
    jo "Is something wrong?"
    show ja 11 with dis
    ja "... no."
    show screen profile(jo7) with dis
    "His voice is soft."
    show ja 27 with dis
    ja "I'm just a bit cold, is all."
    show screen profile(jo0) with dis
    jo "Oh... "
    show screen profile(jo5) with dis
    "The lion's eyes perk up."
    jo "I could bring you a blanket. Hang on—"
    show screen profile(jo7) with dis
    show ja 16 with dis
    "But even as he starts getting up, he's made to stop as James grabs his hand and pushes it against the ground."
    ja "No. No. Don't get up."
    show screen profile(jo20) with dis
    "Joshua sits back down, leaning against James' weight."
    show screen profile(jo18) with dis
    jo "Why?"
    "James takes a deep breath."
    show ja 12 with dis
    show screen profile(jo8) with dis
    ja "You're warm. And... and you're all the warmth I need right now."
    jo "... "
    "His heart skips a beat as he hears that."
    show ja 17 with dis
    "James looks up at him, finally opening his eyes."
    "Even though his gaze is ever so slightly unfocused, it's still piercing into his eyes."
    show ja 18 with dis
    ja "Did you hear me?"
    "He isn't sure what to say. James' breath... reeks of alcohol."
    "But the way his hand is being pressed down, and being looked at like that... "
    "James pushes more of his weight against him."
    show ja 19 with dis
    ja "I said... you're... "
    ja "You're all the warmth I need right now. You're... a crackling, blazing hearth. Warmth. Light."
    ja "A way home."
    show ja 17 with dis
    show screen profile(jo7) with dis
    jo "... "

    show bg black with slow_dis
    stop music fadeout 4.0
    "Then and there, it's like the world goes silent for both of them."
    "There's no moon, no fire, no forest around them – just each other."
    "They are so intoxicated that they cannot properly perceive the rest of the world anyways, but it's more than that."
    "Joshua slowly turns his numb hand, and James holds it. They interlace their fingers. Joshua's breath catches in his throat."
    "James' gaze... remains resolute. He wants something."
    show ja 19 with dis
    ja "Josh."
    "His voice is barely above a whisper."
    jo "... mm... mmhmm?"
    "The deer turns his body towards Joshua more fully, his eyes never leaving the lion's."
    show ja 20 with dis
    ja "Please... give me more warmth. The night is so cold."
    show screen profile(jo8) with dis
    "He grabs Joshua's other hand."
    ja "Be... my home."
    show ja 21 with dis
    "Their eyelids drop, and their lips part lightly."
    ja "Come... and be my... "
    hide ja with slow_dis
    hide screen profile with dis
    $ noprofile_true = True

    play music "music/uplifting-dreams with campfire.mp3" fadein 3.0
    scene bg campground-night with slow_dis
    show b 1 at three with dis
    show t 7 at six with dis
    show m 8 at nine with dis
    ". . . "
    "Michael laughs at Brett's story. He went back on his word and kept drinking."
    show m 15 with dis
    "He's enjoying the two's company when he suddenly detects movement outside his field of vision. He turns to it, trying to focus on it... "
    show m 10 with dis
    "... his eyes go wide."
    m "... wait."
    "He paws at Tyler's side, trying to get his attention."
    show m 11 with dis
    m "Wait. Wait. Guys."
    "Tyler is just lightly moving his head to the music."
    show t 4 with dis
    t "Mm?"
    stop music fadeout 3.0
    show t 10 with dis
    show b 6 with dis
    "He opens his eyes... and lets out a gasp as he notices what Michael is looking at."
    t "Oh... "
    "Brett looks as well, left speechless by what's happening."
    b "Huh?"

    scene cg campfire-kiss with slower_dis
    $ persistent.kissPic = True
    "Mere feet away from them, and without them realizing, James and Joshua are kissing."
    "They're slow, deliberate movements, as their numb lips brush against each other, but they're kissing."
    "Gentle... almost loving movements."
    "Their eyes are closed, and their lips don't leave each other alone, only occasionally giving glimpses of their locking tongues."
    "Despite the music playing in the background, it feels completely silent."
    "Joshua lets go of James' hand and brings it to his cheek, gently caressing him."
    "James seems to lean more of his weight into Joshua's calm body."
    "He throws his arms around the lion's thicker neck, bringing him closer."
    "Michael shakes his head."
    $ noprofile_true = False
    $ profileblush = False
    show screen profile(m0) with dis
    m "Wait. Fuck. No. They're so fucked up."
    "He concentrates on them... their faces are completely red. They are fully inebriated."
    show screen profile(b0) with dis
    b "Shit, dude... should we take them apart from each other?"
    show screen profile(m0) with dis
    m "I... I don't know, man! They look like they're way into it!"
    "Joshua's hand goes to James' chest, pushing him back, making him lay on the ground."
    show screen profile(t0) with dis
    "Tyler can only gasp."

    $ noprofile_true = True
    hide screen profile with dis
    scene cg campfire-passion with slow_dis
    show screen hm
    $ persistent.passionPic = True
    "Breathing heavily, Joshua moves above the deer's body."
    "Even like this, he looks up at him like he wants more. He surrounds the bigger lion's wide body with his hands and tries to pull him in closer."
    "Laying like that, Joshua notices the moon reflects off James' eyes – with that, under the moonlight, and bathed in the light of the fire to his side – he looks incredible."
    "He goes in for another kiss."
    jo "Mmph... "
    "As their lips part, James speaks."
    ja "Give me... warmth... "
    "Joshua's hand goes to the bottom of James' jacket."
    "He slips it under his shirt, slowly bringing it up – across his belly, across his chest."
    "James lets out a small moan."
    jo "Like that?"
    ja "Like... that... "
    "They keep kissing each other, as Joshua presses his weight down on the deer."
    "The other three can only stare on, slack-jawed, as the display of desire continues."
    "But... "

    hide screen hm
    hide screen hmm
    scene bg bonfire with slow_dis
    play music "music/night-forest-ambient.mp3" fadein 5.0
    show ja 22 with dis
    $ noprofile_true = False
    $ profileblush = True
    show screen profile(jo13) with dis
    "Joshua breaks the kiss, looking down at him."
    "He takes a deep breath... and shakes his head, getting up."
    jo "No. No... "
    ja "Wait... "
    "James tries to grab Joshua's hands, but it's a futile effort."
    show screen profile(jo14) with dis
    jo "You're... too drunk."
    "Not that he's any better."
    jo "You're too drunk. You don't actually want this. It's not right."
    show screen profile(jo13) with dis
    scene bg black with dis
    "He staggers away, as James paws futilely in his direction, begging him to come back. He lets out a small noise of pleading that only Joshua can hear."
    $ profileblush = False
    show screen profile(jo22)
    ja "Josh... "
    jo "No. This can't... happen like this."
    show screen profile(jo23)
    "He brings a hand to his head."
    jo "... this is... really happening, right...?"
    "He takes a few deep breaths, supporting himself with his hands on his knees, to try and clear his head."
    "The whimpering behind him dies out."

    show screen profile(jo24) with dis
    scene bg bonfire with dis
    "He eventually turns around... James fell asleep."
    $ profileblush = True
    show screen profile(jo20)
    "He approaches the limp body and slowly shakes his head."
    show screen profile(jo21) with dis
    jo "See... you were too fucked up."
    jo "Were you... asleep?"
    ja "... "
    "He bends down, gingerly picking up James' unconscious body."
    play sound "sfx/footsteps on leaves towards.mp3"
    "He carries him to one of the tents with two sleeping bags in it."

    #$ noprofile_true = True
    $ profileblush = False
    show screen profile(blank) with slow_dis
    scene bg campground-night with slow_dis
    show screen profile(m0) with dis
    #show b 6 at three with dis
    #show t 10 at six with dis
    #show m 11 at nine with dis
    "Michael's eyes go wide."
    m "... no. He wouldn't."
    $ noprofile_true = True
    hide screen profile with dis
    "It seems like Brett and Tyler get the same idea, as all three get up at the same time, staring intently at the intoxicated lion."
    play sound "sfx/moving items.mp3"
    "Joshua opens the tent, crawls inside on his knees, and sets James down on one of the sleeping bags."
    "He pulls his jacket down, so it covers his belly... and then he leaves the tent."
    play sound "sfx/footsteps on leaves away.mp3"
    show jo 1 with slow_dis
    jo "Go... sleep."
    hide jo with dis
    "Michael relaxes slightly."
    "Joshua goes to the opposite tent, staggering as he walks and knocking a few cans to the side as he goes, and opens it, crawling inside on all fours."
    play sound "sfx/moving items.mp3"
    "He grunts as he moves. He comes to one of the sleeping bags and collapses on top of it."
    "He takes his glasses off and folds them up, setting them to a side... and seemingly falls unconscious."
    jo "Mh... "
    ". . . "

    show b 7 at three with dis
    show t 11 at six with dis
    show m 12 at nine with dis
    "They all breathe a sigh of relief. Tyler is the first to speak up, keeping his voice down to not disturb the two asleep."
    t "Well... that's over."
    "Michael flops back down to the ground."
    m "Ugh. How'd he get so fucked up on beer?"
    b "Hey, man... "
    "Brett sits down once more."
    b "Not like you're any better... "
    show m 4 with dis
    m "Shut up."
    "They sit in silence for a few moments."
    show t 12 with dis
    "Tyler twiddles his thumbs."
    t "... maybe we should all go to sleep... it's late anyways."
    show b 4 with dis
    b "Yeah. Yeah... "
    hide b with dis
    hide t with dis
    hide m with dis
    play sound "sfx/moving items.mp3"
    "They pick up part of the mess. They turn off the wireless speaker nobody's paid attention to in some time."
    play sound "sfx/footsteps on leaves away.mp3"
    "Finally, they separate and go to their own tents."
    "Brett and Tyler sleep in the same tent. Michael crawls into the tent that Joshua put James in."
    "Joshua sleeps alone that night."
    stop music fadeout 4.0
    scene bg black with slower_dis

    ". . . "

    $ dayofWeek = "SATURDAY"
    $ date = "June 16"
    $ timeofDay = "Morning"
    scene bg campground-day with dis
    play music "music/morning-light-ambient.mp3" fadein 5.0
    #$ noprofile_true = False
    #show screen profile(jo4) with dis
    "The next morning, after they've already picked their things up and put everything away, Joshua finishes brewing some coffee for everyone."
    play sound "sfx/pour coffee.mp3"
    "He pours everyone a cup – downing part of it with milk for everyone besides himself."
    "He leans against the lit grill, downing his cup of black coffee, looking around."
    jo "This is just to hold us over until we reach a restaurant or diner and can buy breakfast, alright?"
    "Everyone nods, tiredly. Joshua seems to have more energy than everyone else."
    play sound "sfx/footsteps on gravel away.mp3"
    "Particularly James, who seems to only be half alive – he is obviously battling a horrible hangover."
    play sound "sfx/car door.mp3"
    "He grimaces as he finishes his cup of coffee, trying not to move too much, wrapping himself in a blanket before climbing inside the car, in the passenger's side."
    "Joshua rinses out the kettle and the cups once everyone's done with some water, and puts everything away."
    play sound "sfx/car door.mp3"
    "Everyone gets inside the car. Joshua turns the heating on and they drive off."
    play sound "sfx/car leaving.mp3"

    scene bg road with dis
    "They drive in silence for a few moments, only the sound of the radio to keep them company."
    $ noprofile_true = False
    show screen profile(m1) with dis
    "Joshua begins to speak softly, so as to not bother the group's hangover."
    play sound "sfx/driving.mp3"
    show jo 0 at four with dis
    jo "So."
    jo "James."
    show ja 29 at nine with dis
    ja "Yeah?"
    jo "Do you remember anything that happened last night?"
    "... "
    show screen profile(m2) with dis
    "Michael's eyes go wide, and he looks at the pair from the back seat."
    "James takes a deep breath, rubbing his temples. He shakes his head."
    ja "No... I don't remember much."
    ja "Why, what happened?"
    show screen profile(m3) with dis
    "Michael opens his mouth... but he isn't sure what to say or do."
    "Joshua takes a few seconds to respond, as he's turning a curve."
    show jo 2 with dis
    jo "Not much. You just drank a lot and passed out. I didn't know you had it in you to drink that much."
    show ja 30
    "James grimaces."
    ja "I don't think I do, honestly... "
    show jo 3 with dis
    jo "Heh. I guess you were just that fucked up last night, huh... "
    show jo 1 with dis
    "The driver looks at Michael through the rearview mirror. They look at each other."
    show screen profile(m1) with dis
    "Joshua slowly shakes his head."
    show screen profile(m4) with dis
    show jo 3 with dis
    jo "Don't worry. Once we get somewhere with food, I'm getting you some aspirin and plenty of water. Just sleep until we get there."
    "Michael leans back on his chair. Joshua seems to remember what happened... "
    show ja 31 with dis
    "James takes another deep breath, closing his eyes."
    ja "Alright... I'll try."
    jo "Mm."
    $ noprofile_true = True
    hide screen profile with dis

    scene bg black with slow_dis
    stop sound fadeout 3.0
    "... "
    "James gives Joshua a sidelong glance."
    "He keeps looking for a good few moments."
    "Either Joshua doesn't notice, or he is trying not to bring any attention to it."
    "After a bit, he sighs, looking out the window."
    "Maybe he remembers too."
    "Maybe he wishes it had gone further."

    #$ persistent.notesNumber += 1
    play music "music/the-sound-of-light-8863.mp3"
    $ right_menu_turnedOn = False
    $ right_menu = False
    $ quick_menu = False
    $ pause_unlocked = False
    $ noprofile_true = False
    $ ctcOn = True
    with dis
    window hide

    $ credits_speed = 15 #scrolling speed in seconds
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend with dis
    show cred at Move((0.5, 2.1), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    #change the 5 to a different number to make sure the credits scroll correctly
    with Pause(credits_speed + 1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks with dis

    if not persistent.completed:
        centered "Something has changed. Check your phone next time."
    $ played_through = True
    $ persistent.completed = True

    return
