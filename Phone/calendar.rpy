default calendarDateNotSelected = True
default calendarDay1Version1Selected = False
default calendarDay2Version1Selected = False
default calendarDay1Version2Selected = False
default calendarDay2Version2Selected = False

screen calendarLoad:
    tag menu

    use game_menu(_("Calendar"), scroll="viewport"):

        text "Thank you for playing the demo! Click a date and time to relive a moment in Jackie's two-day journey. \n"

        hbox:

            spacing 100

            imagemap:
                idle "phoneMenu/calendarIdle.png"
                hover "phoneMenu/calendarSelect.png"
                ground "phoneMenu/calendarIdle.png"

                hotspot (467, 310, 80, 78):
                    action [SetVariable("calendarDateNotSelected", False), SetVariable("calendarDay1Version1Selected", True), \
                    SetVariable("calendarDay2Version1Selected", False), SetVariable("calendarDay1Version2Selected", False), SetVariable("calendarDay2Version2Selected", False)]

                hotspot (559, 310, 81, 79):
                    action [SetVariable("calendarDateNotSelected", False), SetVariable("calendarDay2Version1Selected", True), \
                    SetVariable("calendarDay1Version1Selected", False), SetVariable("calendarDay1Version2Selected", False), SetVariable("calendarDay2Version2Selected", False)]

            if calendarDateNotSelected:
                imagemap:
                    idle "phoneMenu/calendarTimes.png"

                    hotspot (0,0,0,0):
                        action NullAction()

            if calendarDay1Version1Selected:

                imagemap:
                    idle "phoneMenu/day1Version1Idle.png"
                    hover "phoneMenu/day1Version1Select.png"
                    ground "phoneMenu/day1Version1Idle.png"

                    hotspot (218, 38, 102, 21):
                        action [SetVariable("calendarDay1Version1Selected", False), SetVariable("calendarDay1Version2Selected", True)]

                    hotspot (88, 124, 284, 41): #morning
                        action [Call('day1_morning'), With(Dissolve(1.0))]

                    hotspot (88, 257, 284, 43): #noon
                        action [Call('day1_noon'), With(Dissolve(1.0))]

                    hotspot (88, 394, 285, 40): #evening
                        action [Call('day1_evening1'), With(Dissolve(1.0))]

                    hotspot (88, 527, 284, 41): #night
                        action [Call('day1_evening2'), With(Dissolve(1.0))]

            if calendarDay2Version1Selected:
                imagemap:
                    idle "phoneMenu/day2Version1Idle.png"
                    hover "phoneMenu/day2Version1Select.png"
                    ground "phoneMenu/day2Version1Idle.png"

                hotspot (218, 38, 102, 21):
                    action [SetVariable("calendarDay2Version1Selected", False), SetVariable("calendarDay2Version2Selected", True)]

                hotspot (87, 79, 285, 40): #morning
                    action [Call('day2_morning'), With(Dissolve(1.0))]

                hotspot (87, 212, 285, 43): #noon
                    action NullAction() #doesn't exist yet

                hotspot (87, 347, 288, 42): #afternoon
                    action NullAction() #doesn't exist yet

                hotspot (87, 483, 287, 39): #evening
                    action NullAction() #doesn't exist yet

                hotspot (88, 570, 284, 43): #night
                    action NullAction() #doesn't exist yet

            if calendarDay1Version2Selected:
                imagemap:
                    idle "phoneMenu/day1Version2Idle.png"
                    hover "phoneMenu/day1Version2Select.png"
                    ground "phoneMenu/day1Version2Idle.png"

                    hotspot (98, 38, 100, 19):
                        action [SetVariable("calendarDay1Version1Selected", True), SetVariable("calendarDay1Version2Selected", False)]

                    hotspot (86, 303, 286, 42): #afternoon
                        action NullAction() #doesn't exist yet

                    hotspot (87, 394, 285, 40): #evening
                        action NullAction() #doesn't exist yet

                    hotspot (88, 572, 285, 40): #night
                        action NullAction() #doesn't exist yet

            if calendarDay2Version2Selected:
                imagemap:
                    idle "phoneMenu/day2Version2Idle.png"
                    hover "phoneMenu/day2Version2Select.png"
                    ground "phoneMenu/day2Version2Idle.png"

                hotspot (98, 38, 100, 19):
                    action [SetVariable("calendarDay2Version1Selected", True), SetVariable("calendarDay2Version2Selected", False)]

                hotspot (87, 80, 285, 40): #morning
                    action NullAction() #doesn't exist yet

                hotspot (86, 169, 286, 42): #noon
                    action NullAction() #doesn't exist yet

                hotspot (85, 303, 288, 44): #afternoon
                    action NullAction() #doesn't exist yet

                hotspot (88, 393, 286, 41): #evening
                    action NullAction() #doesn't exist yet
