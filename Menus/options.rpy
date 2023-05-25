## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.

## Mouse Tooltip ###############################################################

# this class allows a tooltip to follow a mouse. Made by jsfehler and GimmiRuski
# on Github: https://github.com/jsfehler/renpy-mouse-tooltip/

init -1 python:

    class MouseTooltip(Tooltip, renpy.Displayable):
        """A Tooltip whose x/y position follows the mouse's."""
        action = Action

        def __init__(self, default, padding=None, *args, **kwargs):
            super(renpy.Displayable, self).__init__(*args, **kwargs)

            self.default = default
            self.value = default

            self.padding = padding or {}
            self.pad_x = padding.get('x', 0)
            self.pad_y = padding.get('y', 0)

            self.x = 0
            self.y = 0

            self._redraw = False

        @property
        def redraw(self):
            return self._redraw

        @redraw.setter
        def redraw(self, new_value):
            self._redraw = new_value
            renpy.redraw(self, 0)

        def render(self, width, height, st, at):
            # Only Text() displayables have a size method
            try:
                w, h = self.value.size()

            except AttributeError:
                child_render = renpy.render(self.value, width, height, st, at)
                w, h = child_render.get_size()

            render = renpy.Render(w, h)
            render.place(self.value, x=self.x + self.pad_x, y=self.y + self.pad_y)
            return render

        def event(self, ev, x, y, st):
            self.x = x
            self.y = y

            if self.redraw:
                renpy.redraw(self, 0)

            # Pass the event to our child
            return self.value.event(ev, x, y, st)


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Nihil: The Watcher")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "0.1"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
Nihil: The Watcher is written by {a=https://archiveofourown.org/users/algol_ardhanari/}algol_ardhanari{/a},
drawn and programmed by {a=https://twitter.com/BlueStylusArt}BlueStylus{/a}, and inspired by
{a=https://echoproject.itch.io/}The Echo Project{/a}.
To read more Nihil, check out the full story on {a=https://archiveofourown.org/series/2153550}Archive of our Own{/a}.
To support the development of a full visual novel, visit our {a=https://www.patreon.com/nihilstory}Patreon{/a}!

Music used: In the forest-Les Free Music, Morning light-Les Free Music, Uplifting Dreams-Les Free Music, Summer night in the forest-Mixkit, The sound of light-Tomomi Kato.

Join our {a=https://discord.gg/nihilthestory}Discord server{/a}! Thank you for playing. <3
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "NihilWatcher"
define config.default_fullscreen = True

##itch.io info for renpy to export

define build.itch_project = "BlueStylus/NihilWatcher"

## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "music/the-sound-of-light-8863.mp3"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Used when entering the game menu from the game.
define config.enter_transition = dissolve

## Used when exiting the game menu to the game.
define config.exit_transition = None

## Used between screens of the game menu.
define config.intra_transition = dissolve

## Used when entering the game menu from the main menu.
define config.main_game_transition = dissolve

## Used when returning to the main menu from the game.
define config.game_main_transition = dissolve

## Used when entering the main menu from the splashscreen.
define config.end_splash_transition = dissolve

## Used when entering the main menu after the game has ended.
define config.end_game_transition = dissolve

## Used when a game is loaded.
define config.after_load_transition = dissolve

## Used when the window is shown.
define config.window_show_transition = dissolve

## Used when the window is hidden.
define config.window_hide_transition = dissolve

## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.5)
define config.window_hide_transition = Dissolve(.5)

define config.skip_delay = 100


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 45


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Disable rollback using the scrollwheel:

define config.rollback_enabled = True

## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "Watcher-1583640595"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Cursor ######################################################################
##
## The cursor used in-game.

define config.mouse = {"default":[ ("gui/cursor.png", 0, 0) ] }


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
