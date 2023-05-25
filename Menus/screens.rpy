################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"
    zorder 2

    if not hide_say:
        window:
            id "window"

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what" color narratorColor

            if noprofile_true:
                add "gui/textbox/noprofile.png" yalign 1.0


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    #if not renpy.variant("small"):
        #add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    zorder 10

    side "bl":
        vbox:
            for i in items:
                textbutton i.caption action i.action text_align 0.0 xalign 0.0


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xpos 235
    ypos 770
    yalign 1.0

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    xalign 0.0


## CTC screen ##################################################################

screen ctc(arg=None):

    zorder 100

    if ctcOn:
        hbox:
            xalign 0.82
            yalign 0.97

            add "gui/textbox/continue.png" at ctcblink


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100
    modal quick_menu_modal

    if quick_menu_modal:
        key 'dismiss' action NullAction()

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.175
            yalign 0.98
            spacing 9

            if back_button:
                imagebutton: #back button
                    idle "gui/textbox/back.png"
                    hover "gui/textbox/back interact.png"
                    hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Replay", size=25, font="fonts/GARAIT.TTF", color="#ffffff"))]
                    unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
                    action [Rollback(), SetField(mtt, 'redraw', True), mtt.Action(Text("")), Hide('phoneMenu')]
            else:
                imagebutton: #locked back button
                    idle "gui/textbox/back locked.png"
                    hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Unavailable", size=25, font="fonts/GARAIT.TTF", color="#b8b8b8"))]

            if history_button:
                imagebutton: #history button
                    idle "gui/textbox/history.png"
                    hover "gui/textbox/history interact.png"
                    hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("History", size=25, font="fonts/GARAIT.TTF", color="#ffffff"))]
                    unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
                    action [ShowMenu('history'), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            else:
                imagebutton: #locked history button
                    idle "gui/textbox/history locked.png"
                    hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Unavailable", size=25, font="fonts/GARAIT.TTF", color="#b8b8b8"))]

            if fastforward_button:
                imagebutton: #fast forward button
                    idle "gui/textbox/skip.png"
                    hover "gui/textbox/skip interact.png"
                    hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Fast Forward", size=25, font="fonts/GARAIT.TTF", color="#ffffff"))]
                    unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
                    action [Skip(), SetField(mtt, 'redraw', True), mtt.Action(Text(""))] alternate [Skip(fast=True, confirm=True), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            else:
                imagebutton: #locked fast forward button
                    idle "gui/textbox/skip locked.png"
                    hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Unavailable", size=25, font="fonts/GARAIT.TTF", color="#b8b8b8"))]

            if auto_mode_button:
                imagebutton: #auto mode button
                    idle "gui/textbox/auto.png"
                    hover "gui/textbox/auto interact.png"
                    hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Auto Mode", size=25, font="fonts/GARAIT.TTF", color="#ffffff"))]
                    unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
                    action [Preference("auto-forward", "toggle"), ToggleVariable("autoOn"), ToggleVariable("ctcOn"), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            else:
                imagebutton: #locked auto mode button
                    idle "gui/textbox/auto locked.png"
                    hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Unavailable", size=25, font="fonts/GARAIT.TTF", color="#b8b8b8"))]

            #textbutton _("Save") action ShowMenu('save')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            #textbutton _("Prefs") action ShowMenu('preferences')

        if autoOn:
            if preferences.auto-forward:
                hbox:
                    xalign 0.8
                    yalign 0.98
                    text "Auto Mode is On." size 20

# Menu on the bottom right corner for phone, inventory, and menu

screen right_menu():

    zorder 99
    modal right_menu_modal

    if right_menu:

        #add "gui/textbox/textbox line.png" yalign 1.0

        vbox:
            xalign 1.00
            yalign 0.766

            imagebutton:
                idle "gui/textbox/hide textbox.png"
                hover "gui/textbox/hide textbox interact.png"
                action [SetVariable("hide_say", True), SetVariable("quick_menu", False), SetVariable("right_menu", False), SetVariable("profileshow", False), SetVariable("ctcOn", False), Hide("phoneMenu", transition=dissolve), Show("show_textbox", transition=dissolve)]

        vbox:
            xalign 0.99
            yalign 0.975

            spacing 10

            #if inventory_button_turnedOn:
                #imagebutton:
                    #idle "gui/textbox/right menu inventory idle.png"
                    #hover "gui/textbox/right menu inventory hover.png"
                    #action ToggleScreen("inventory_screen", transition = None)
            #else:
                #imagebutton:
                    #idle "gui/textbox/right menu inventory locked.png"

            if load_button_turnedOn:
                imagebutton:
                    idle "gui/textbox/right menu load idle.png"
                    hover "gui/textbox/right menu load hover.png"
                    action ShowMenu("load")

            if save_button_turnedOn:
                imagebutton:
                    idle "gui/textbox/right menu save idle.png"
                    hover "gui/textbox/right menu save hover.png"
                    action ShowMenu("save")

            if phone_menu_button_turnedOn:
                imagebutton:
                    idle "gui/textbox/right menu phone idle.png"
                    hover "gui/textbox/right menu phone hover.png"
                    action ToggleScreen("phoneMenu", transition = None)
            else:
                imagebutton:
                    idle "gui/textbox/right menu phone locked.png"

        add mtt

screen show_textbox:

    modal True

    vbox:
        xalign 1.00
        yalign 1.00

        imagebutton:
            idle "gui/textbox/show textbox.png"
            hover "gui/textbox/show textbox interact.png"
            action [SetVariable("hide_say", False), SetVariable("quick_menu", True), SetVariable("right_menu", True), SetVariable("profileshow", True), SetVariable("ctcOn", True), Hide("show_textbox", transition=dissolve)]

screen pause_button:

    zorder 1

    if pause_unlocked:
        imagebutton:
            idle "gui/pause_idle.png"
            hover "gui/pause_interact.png"
            action [ShowMenu("preferences"), SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
            xalign 0
            yalign 0
            hovered [SetField(mtt, 'redraw', True), mtt.Action(Text("Pause", size=25))]
            unhovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))]
    #else:
        #imagebutton:
            #idle "gui/pause_locked.png"
            #xalign 0.01
            #yalign 0.01

    if pause_mtt:
        add mtt


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.

init python:
    config.overlay_screens.append("quick_menu")
    config.overlay_screens.append("right_menu")
    config.overlay_screens.append("pause_button")

default quick_menu = False
#these are false for the tutorial
default back_button = False
default history_button = False
default fastforward_button = False
default fasted = False
default auto_mode_button = False
default quick_menu_modal = False

default right_menu = False
default right_menu_modal = False
default right_menu_turnedOn = False
default phone_menu_button_turnedOn = False
default inventory_button_turnedOn = False
default save_load_button_turnedOn = False
default save_button_turnedOn = True
default load_button_turnedOn = True
default save_button = False
default load_button = False

#have the pause button availabe at all times
default pause_unlocked = False
default pause_mtt = True

style quick_button is default
style quick_button_text is button_text

style right_button is default
style right_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

style right_button:
    properties gui.button_properties("right_button")

style right_button_text:
    properties gui.button_text_properties("right_button")

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Read") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Bookmark") action ShowMenu("save")

        textbutton _("Library") action ShowMenu("load")

        textbutton _("Options") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") or renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    #frame:
        #pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen. Just kidding!
    ## use navigation
    vbox:

        xpos 300
        yalign 0.8

        spacing gui.navigation_spacing

        textbutton _("Read") action Start()

        #textbutton _("History") action ShowMenu("history")

        textbutton _("Library") action ShowMenu("load")

        #textbutton _("Save") action ShowMenu("save")

        if persistent.completed:
            textbutton _("Gallery") action ShowMenu("galleryMenu")

        textbutton _("Options") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        textbutton _("About") action ShowMenu("about")

        # original> if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

    if gui.show_name:

        vbox:
            yalign 0.05
            text "[config.name!t]":
                style "main_menu_title"
                size 50
                #font "fonts/Metropolis/Metropolis-Bold.otf" the upside down V doesn't exist

            text "Honest Spirits of the Forest v1.0": #"Demo Version [config.version]":
                style "main_menu_version"
                size 25
                color "#FFFFFF"
                #font "fonts/Pangolin-Regular.ttf"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

screen calendarLoad:
    text "here it would be"


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Honest Spirits of the Forest v1.0\n") #_("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Bookmark"))


screen load():

    tag menu

    use file_slots(_("Library"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Options"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                #vbox:
                    #style_prefix "radio"
                    #label _("Rollback Side")
                    #textbutton _("Disable") action Preference("rollback side", "disable")
                    #textbutton _("Left") action Preference("rollback side", "left")
                    #textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action [Preference("skip", "toggle"), ToggleVariable("fastforward_button")]
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

                textbutton _("Game Mechanics") action SetScreenVariable("device", "gameMechanics")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help
            elif device == "gameMechanics":
                use gameMechanics_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    #hbox:
        #label _("Arrow Keys")
        #text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    #hbox:
        #label _("Ctrl")
        #text _("Skips dialogue while held down.")

    #hbox:
        #label _("Tab")
        #text _("Toggles dialogue skipping.")

    #hbox:
        #label _("Page Up")
        #text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    #hbox:
        #label _("Mouse Wheel Up\nClick Rollback Side")
        #text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


screen gameMechanics_help:
    hbox:
        label _("Quick Menu")
        textbutton _("Tutorial") hovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))] action [Start('help1')]

    hbox:
        label _("Right Menu")
        textbutton _("Tutorial") hovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))] action [Start('help5')]

    hbox:
        label _("Phone")
        textbutton _("Tutorial") hovered [SetField(mtt, 'redraw', True), mtt.Action(Text(""))] action [Start('help6')]


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0


## hmm #########################################################################

screen hm:
    zorder 0
    imagemap:
        idle "CGs/cg campfire-passion.png"
        hover "CGs/cg campfire-passion.png"
        ground "CGs/cg campfire-passion.png"
        if hm1 == True:
            if hm2 == True:
                hotspot (36, 114, 52, 92) action Jump('hmmm')
        else:
            hotspot (36, 114, 52, 92) action [Show("hmm", transition=Dissolve(3.0)), SetVariable('hm3', True)]


screen hmm:
    zorder 0
    add "CGs/cg campfire-hm.png"

image hmshadow = "Sprites/hm.png"

label hmmm:
    $ back_button = False
    $ history_button = False
    $ fastforward_button = False
    $ auto_mode_button = False
    $ pause_unlocked = True
    $ noprofile_true = True

    $ phone_menu_button_turnedOn = False
    $ load_button_turnedOn = False
    $ save_load_button_turnedOn = False

    hide screen profile
    hide screen phoneMenu
    hide screen map
    hide screen hm

    show bg hmm1
    show hmshadow with slow_dis
    $ _history = False
    hm "So you found me."
    hm "..."
    hm "...hm."
    hm "You've decided to confront me headon, yes?"
    hm "I commend your bravery. The last was not so... fortunate, shall we say?"
    hm "Well then, I will reward your initiative."
    hm "There are three of them. Three vessels that he will use and destroy."
    hm "When he regains his full power, their lives will be in danger."
    hm "The chance that you can save them without my help is... honestly, low."
    hm "But I can assist you in saving one. Choose, and it shall be done."
    hm "..."
    hm "You must choose, do you not feel the evil rising?"
    hm "You only put off the inevitable."
    hm "..."
    hm "Make the choice."
    hm "Make it."
    hm "Choose."
    hm "Hurry."
    hm "Make a choice or be consumed by darkness."
    hm "..."
    hm "Do not face the void."
    "I don't want to."
    hm "..."
    hm "...So that's what you choose. I feel your resolve."
    hm "It's a shame it will go to waste."
    play music "music/droning sound.mp3"
    show bg hmm2
    hm "You will forget.{nw}"
    hm "{cps=80}You will forget because you are a coward.{nw}"
    show bg hmm3
    hm "{cps=80}You are refused power because you refuse to make a choice.{nw}"
    hm "{cps=80}You are useless.{nw}"
    hm "{cps=160}You will be purged of the ability to choose and cast into the pit, where the gnashing maws and sharpened claws of the void will rend your body asunder and consume you whole.{nw}"
    show bg hmm4
    hm "{cps=80}You are but another entry point now.{nw}"
    hm "{cps=80}No matter.{nw}"
    hm "{cps=80}Another, better, more empty vessel shall arrive within two years’ time, and the cycle will begin.{nw}"
    show bg hmm5
    hm "{cps=160}Pleasure, cowardice, catharsis and melancholy will swirl into the nihil’s maw, and they will all be in the eye of the maelstrom, condemned to pain, death, choice, and repetition.{nw}"
    hm "{cps=80}The salamander shall suffer the pain of denial.{nw}"
    hm "{cps=80}The bear shall suffer the pain of solitude and loss of direction.{nw}"
    show bg hmm6
    hm "{cps=80}The fox shall suffer the pain of revenge and torture.{nw}"
    hm "{cps=80}The lion shall bear all their burdens until his will shatters, and he shall be made to bear the heaviest cross.{nw}"
    hm "{cps=80}And the new man shall be none the wiser.{nw}"
    show bg grey
    stop music
    hm ". . . "
    hm "Nihil will return again."
    $ noprofile_true = False
    $ right_menu = False
    $ quick_menu = False
    $ pause_unlocked = False
    $ right_menu_turnedOn = False
    window hide
    show bg black
    python:
        if os.name == 'nt':
            import os

            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                player = os.environ.get(name)
        elif os.name == 'posix':
            import os

            for user in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                player = os.environ.get('USER')
    centered "{size=40}{font=fonts/Youmurdererbb-pwoK.otf}{color=#7d0000}And you better be prepared for it, [player].{/color}{/font}{/size}"
    $ renpy.quit()

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    on "show" action SetVariable('fasted', True)

    zorder 100
    style_prefix "skip"

    frame:

        xalign 0
        yalign 0.06

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
