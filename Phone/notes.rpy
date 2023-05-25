##The notes app on the phone has its own .rpy file because of the number of notes
##Jackie will be taking throughout the story. each note is its own screen.

################################################################################

#Example note. This shows all the syntax necessary to make a new note.

screen findme:

    tag note #only one screen tagged note can be shown at a time
    zorder 83 #put above the notes app
    modal True #cannot click out of screen

    add "phoneMenu/notes bg.png" xpos 1486 ypos 131

    viewport:
        area (1486, 144, 365, 599)
        scrollbars "vertical"
        draggable True
        mousewheel True

        vbox:
            #Put all the text in the note in here. New paragraph = new text ""
            text "Hm. Show me where was it again? ...Behind you? I don't think you received my message."

    imagebutton:
        idle "phoneMenu/home button invis.png" #this image is transparent
        hover "phoneMenu/home button invis.png" #this image is transparent
        xpos 1639 #this is the exact x-value. don't touch!!
        ypos 751 #this is the exact y-value. don't touch!!
        action Hide('findme')

################################################################################
