################################################################################

label help1:
    scene bg black
    $ pause_mtt = False
    $ back_button = False
    $ history_button = False
    $ fastforward_button = False
    $ auto_mode_button = False
    $ pause_unlocked = True
    $ noprofile_true = True
    $ ctcOn = True
    show screen quick_menu
    $ pause_mtt = True
    "You have clicked on the tutorial for the quick menu. Click pause and main menu at any time to leave the tutorial."
    #"I'll appear when game mechanics that might be confusing are unlocked throughout the visual novel. You can recognize me with my green text and my ultra-positive atti-dude, dude!"
    #"Before I get into my helpfully helpful help, {color=#c72b20}do you want my help?{/color} You can choose to turn me off, if you want."
    #$ narrator.pop_history() #removes previous dialogue from the history logs

    #menu:
        #"Before I get into my helpfully helpful help, {color=#c72b20}do you want my help?{/color} You can choose to turn me off, if you want.{fast}"
        #"Yes":
            #$ narrator.add_history(kind="adv", who=narrator.name, what="Yes") #adds this choice to the history logs
            #"Cool! I'll start by explaining the basic controls, then major gameplay mechanics. Don't worry, it's not that complicated!"
        #"No":
            #$ narrator.add_history(kind="adv", who=narrator.name, what="No") #adds this choice to the history logs
            #$ gameHelperOn = False
            #$ back_button = True
            #$ fastforward_button = True
            #$ history_button = True
            #$ auto_mode_button = True
            #"Ok, that's fine! I won't disrupt your experience now, or for the rest of the game."
            #"If you ever get confused about how to play the game, you can always find me in the \"Help\" section on the main menu."
            #"Enjoy Visual Novel About Gay Romance and Mystery (title pending)! Buh-bye!"
            #scene black with Dissolve(1.0)
            #return

    "This visual novel is roughly a 5 minute game meant to be enjoyed over 30 minutes."
    "To meet this goal, we have taken many steps to encourage the player to progress slowly."
    "The quick menu was created to give players an easy way to access our features for maximum immersion."
    "First, to continue to the next dialogue in a conversation, click anywhere on the screen."
    "A golden ring indicator will appear in the bottom right to let you know when you should advance dialogue."
    "Next, allow me to explain the buttons below the text. There are four clickable icons."
    if renpy.in_rollback():
        $ quick_menu_modal = False
        "Right now the buttons are deactivated so that I may explain what they do. I'll start from the left and work my way right."
        $ back_button = True
        "Excellent. Unlike most visual novels, using the scrollwheel on your mouse to replay dialogue is disabled in this game. Let's move onto the next button."
        jump help2
    "Right now the buttons are deactivated so that I may explain what they do. I'll start from the left and work my way right."
    $ quick_menu = True
    $ back_button = True
    if renpy.in_rollback():
        $ quick_menu_modal = False
        "Right now the buttons are deactivated so that I may explain what they do. I'll start from the left and work my way right."
        $ back_button = True
        "Excellent. Unlike most visual novels, using the scrollwheel on your mouse to replay dialogue is disabled in this game. Let's move onto the next button."
        jump help2
    "This is the replay button. Clicking it will allow you to go to the previous frame of dialogue. Try it out now."
    $ narrator.pop_history()
    $ quick_menu_modal = True
    show screen quick_menu
    "This is the replay button. Clicking it will allow you to go to the previous frame of dialogue. Try it out now.{fast}"
    jump help2

label help2:
    $ back_button = True
    $ history_button = True
    "Next is the history button. It allows you to look at the past history of the dialogue. Click it now to see it."
    "(To be honest, I can't tell whether or not you actually opened the history. I hope you did so you know what it looks like.)"
    "You can open the dialogue history at any point of the visual novel. If you ever missed what someone said, it'll be in there up to a certain point."
    jump help3

label help3:
    $ quick_menu_modal = False
    "Next is the fast-forward button, which turns on fast-forward mode. If your latest save is far back from where you actually stopped playing, this mode can help you skip to where you actually stopped."
    "Click the fast-forward button again to turn fast-forward mode off and resume normal progression."
    "This button is deactivated by default but can be turned on in Options at any time. Turning it on will also activate the control key, which can be held down to skip."
    "Fast-forward will always automatically stop at a question asking for your response (also called a menu). Otherwise, it'll skip over all dialogue and narration."
    $ fastforward_button = True
    "Go ahead and skip the following speech and get to the next menu. This is a demonstration on how the fast-forward feature works."
    $ _skipping = True
    if fasted:
        $ quick_menu_modal = False
        show screen quick_menu
    else:
        $ quick_menu_modal = True
        show screen quick_menu
    "Sorry, you can't click to continue past this point. Please go back and press the fast-forward button{fast}"
    show screen skip_indicator
    "A thick soupy darkness surrounded him, and deformed hands, aged and tormented, reached up from it, grabbing and pulling.{fast}{w=0.1}"
    $ narrator.pop_history()
    "Voices called in falsetto screams and guttural moans, begging for release and salvation.{fast}{w=0.1}"
    $ narrator.pop_history()
    "The awful cacophony of destruction had subsided, leaving an eerie sound vacuum which amplified the cries of the tormented souls. A chilly wind blew.{fast}{w=0.1}"
    $ narrator.pop_history()
    "The contorted limbs and distorted heads with their unhinged jaws, stitched up eyes and melting flesh, were of human and beastly forms, their only fellowship being in their writhing and their agony.{fast}{w=0.1}"
    $ narrator.pop_history()
    "Again and again they desperately reached up, flinching and twitching in rage and wretchedness.{fast}{w=0.1}"
    $ narrator.pop_history()
    "Plumes of toxic odors, acidic and pungent to the very back of the throat, wafted up in ever greater dispersions.{fast}{w=0.1}"
    $ narrator.pop_history()
    "There seemed to be a lawlessness to the senses so that what could be seen could also be felt, what could be heard could be tasted and what could be smelt could be seen.{fast}{w=0.1}"
    $ narrator.pop_history()
    "As such, the sulphuric stench contained an anaemic glow which rose up into what had, until very recently, been air, giving everything a dull, rotting appearance.{fast}{w=0.1}"
    $ narrator.pop_history()
    "It seeped into every crevice and orifice. Screaming was one’s only release, yet it only served to exacerbate the suffering.{fast}{w=0.1}"
    $ narrator.pop_history()
    "Other than Frank, Bitchiro was the last semblance of life to remain.{fast}{w=0.1}"
    $ narrator.pop_history()
    "Chest-deep in damnation, he held fast to Frank’s ankle but the soulless hands were on him and around him, pulling at him, wrenching his garments and gouging their gnarled digits deep into his flesh.{fast}{w=0.1}"
    $ narrator.pop_history()
    "That was from Filthy Frank's book, {i}Francis of the Filth{/i}. One of my favorite books, I must say!{fast}{w=0.1}"
    $ narrator.pop_history()
    $ quick_menu_modal = False
    show screen quick_menu
    "Anyways, here comes the menu.{fast}{w=0.1}"
    $ renpy.block_rollback()
    $ narrator.pop_history()

    menu:
        "{color=#c72b20}Did the fast-forward button work?{/color}{fast}"
        "Yes":
            $ narrator.add_history(kind="adv", who=narrator.name, what="Yes") #adds this choice to the history logs
            "By the way, sometimes menus have many choices, and sometimes they only have one. How interesting!"
            jump help4

label help4:
    $ _skipping = False
    "The last button of this tutorial is the automatic mode button. Turning it on makes the story automatically continue without needing you to click!"
    "You may turn auto mode on whenever you want, and all you'll have to do is sit back, read, and relax."
    "Like fast-forward mode, auto mode stops at menus. However, it'll continue to be on if you don't press the button again."
    $ auto_mode_button = True
    "The button is activated now, and it'll be available whenever you need it in the visual novel."
    "That completes the quick menu tutorial. Please enjoy reading Nihil: The Watcher!"
    #"From now on, there will be an option to skip the tutorials I bring in case you find me annoying (which, by the way, how rude)."
    #"See you soon! And enjoy Visual Novel About Gay Romance and Mystery (title pending)! Buh-bye!"
    #$ beginningTutorial = False
    return

    #this goes into the tutorial about saving
    #"Anyways, before you jump into the story, I have to explain how saving works."
    #"Most visual novels let you save whenever you want. They even have autosave features. How modern!"
    #"This visual novel is a bit different though. You have to save manually at certain points every day."
    #"Well, you don't {i}have{/i} to save."

label help5:
    scene bg black
    $ pause_mtt = False
    $ phone_menu_button_turnedOn = False
    $ load_button_turnedOn = False
    $ save_load_button_turnedOn = False
    $ pause_unlocked = True
    $ noprofile_true = True
    $ ctcOn = True
    show screen right_menu
    $ pause_mtt = True
    "You have clicked on the tutorial for the right menu. Click pause and main menu at any time to leave the tutorial."
    "This visual novel is roughly a 5 minute game meant to be enjoyed over 30 minutes."
    "To meet this goal, we have taken many steps to encourage the player to progress slowly."
    "The right menu was created to give players a stylize menu for key visual novel features."
    "The right menu has the Library, Bookmark, Phone, and Hide Box buttons."
    "While they may sound confusing, they're actually just our versions of the Load, Save, and... well, Phone buttons."
    "To learn more about the phone menu, there is a separate tutorial in the Help menu about it."

    "The first button is the Hide Box button. It is in the top right corner of the dialogue box."
    "Click it to hide all UI elements so you can see the full character sprites, scene, or background behind it."
    "Click on the Show Box button in the bottom right corner to make the dialogue box and pause button appear again."
    "You may also use the middle click button if you are using a mouse to quickly hide and show the dialogue box."

    $ load_button_turnedOn = True
    "The second button is the Library button. Use this button to access your save files."
    "The library organizes three types of saves using the page numbers at the bottom."
    "The letter A on the left stands for autosaves. These are created using the engine every few minutes."
    "If you forgot to save before an important choice (not that there are any in this game), use the autosave to go back."
    "The letter Q stands for quick saves. Quick saving has been turned off in this game. Apologies!"
    "The numbers 1 through 9 are for manual saves. You can create manual saves..."

    $ save_load_button_turnedOn = True
    "...using the Bookmark button. It has been activated now."
    "(The uh... the gimmick here is that each save is a bookmark in the novel and you save a library of bookmarks. Okay it doesn't really make sense here but it'll make more sense in the full game.)"
    "You may also use the right click button if you are using a mouse to quickly access the save list."
    "We recommend saving in a new slot each time rather than saving over an existing slot."
    "But since this game is rather short, it's not required to save often to enjoy the story."

    $ phone_menu_button_turnedOn = False
    "Finally, there's the Phone button. There is a separate tutorial for how to use each app."
    "For now, it is important to know that you may still click anywhere to advance the story even when the phone is open."
    "Most of the functionality of the phone is limited to easter eggs and secrets in this game."
    "To open and close the phone, you may click the Phone button."
    "To close the phone, you may also click the power button at the top of the phone."
    "That completes the right menu tutorial. Please enjoy reading Nihil: The Watcher!"
    return

label help6:
    scene bg black
    $ pause_mtt = False
    $ phone_menu_button_turnedOn = False
    $ load_button_turnedOn = False
    $ save_load_button_turnedOn = False
    $ pause_unlocked = True
    $ noprofile_true = True
    $ ctcOn = True
    show screen right_menu
    $ pause_mtt = True
    "You have clicked on the tutorial for the phone menu. Click pause and main menu at any time to leave the tutorial."
    "This visual novel is roughly a 5 minute game meant to be enjoyed over 30 minutes."
    "To meet this goal, we have taken many steps to encourage the player to progress slowly."
    "The phone menu was created to give players a fun way to access features that would play a part in the story."
    "But since this game is rather short, the phone does not play that big of a part in the story."
    "However, as you can probably tell from the colors, the phone in this case belongs to Joshua."

    $ phone_menu_button_turnedOn = True
    "The Phone button has now been activated."
    "To open and close the phone, you may click the Phone button."
    "To close the phone, you may also click the power button at the top of the phone."

    "The phone presents some helpful information regarding the setting."
    "The day and date are displayed in the top left, and will change when a day has passed or click the home button."
    "However, when you have an app open, the home button will instead return you to the phone's home screen rather than turn it off."
    "The time in the top right corner will also change as you advance time by progressing the story."

    "The phone currently has 5 apps. I will explain each one in order from top to bottom, left to right."
    #map, contacts, gallery, messages, notes, translate which is not implemented yet
    "The red app is the map app. Use it to get a good look at where you currently are in the world."
    "In the finished game, the map will be used to go from one place to another easily. For now, it's only use is to find a certain secret."
    "The cyan app is the contacts app. Use this app to take a look at some information about the characters."
    "If you are wondering why their birthdays are mispelled, it is because we actually have not decided on their birthdays yet."
    "Consider them placeholders for now."
    "The purple app is the gallery app. Use this app to look at full size scenes once they are unlocked."
    "You may unlock images by seeing them while playing through the game, or by receiving them in text messages (not implemented in demo)."
    "You may also access the gallery from the main menu after you have played through the game at least once."
    "In the final version of the game, you will be able to access the Gallery from the main menu as soon as you have unlocked at least one scene."
    "The green app is the messages app. Use this app to look through some of the text threads between Joshua and his friends."
    "You will be able to send and receive messages in the final game, but for now you may only look through previous texts."
    "The messages are also used for a certain secret."
    "The final yellow app is the notes app, where you will be able to find helpful notes that the protagonist writes down throughout the story."
    "In the final game, you will be allowed and encouraged to take your own notes for puzzle solving, but it is not implemented in the demo."

    "That completes the phone menu tutorial. Please enjoy reading Nihil: The Watcher!"
    return
