# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image bg blank_bg = "GUI/main_menu_bg.png"
image bg school_morning = "Backgrounds/classroom_morning.jpg"
image bg school_afternoon = "Backgrounds/classroom_afternoon.jpg"
image bg school_evening = "Backgrounds/classroom_evening.jpg"
image bg principal_office = im.FactorScale("Backgrounds/uncle mugen school corridor afternoon.jpg", 0.33,0.33)
image bg school_corridor_morning = im.FactorScale("Backgrounds/school_corridor_background.jpg",0.33,0.33)
image bg home_morning = "Backgrounds/studio_with_office_morning.jpg"
image bg home_sunset = "Backgrounds/studio_with_office_sunset.jpg"
image bg home_night = "Backgrounds/studio_with_office_night.jpg"

image principal neutral = "Characters/Principal/tokudaya_neutral_suit.png"
image principal happy = "Characters/Principal/tokudaya_smile_suit.png"
image principal disappointed = "Characters/Principal/tokudaya_serious_suit.png"

image student_0 = ConditionSwitch(
    "classroom_obj.all_students[0].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_1 = ConditionSwitch(
    "classroom_obj.all_students[1].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_2 = ConditionSwitch(
    "classroom_obj.all_students[2].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_3 = ConditionSwitch(
    "classroom_obj.all_students[3].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_4 = ConditionSwitch(
    "classroom_obj.all_students[4].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_5 = ConditionSwitch(
    "classroom_obj.all_students[5].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_6 = ConditionSwitch(
    "classroom_obj.all_students[6].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_7 = ConditionSwitch(
    "classroom_obj.all_students[7].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_8 = ConditionSwitch(
    "classroom_obj.all_students[8].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_9 = ConditionSwitch(
    "classroom_obj.all_students[9].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_10 = ConditionSwitch(
    "classroom_obj.all_students[10].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_11 = ConditionSwitch(
    "classroom_obj.all_students[11].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_12 = ConditionSwitch(
    "classroom_obj.all_students[12].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_13 = ConditionSwitch(
    "classroom_obj.all_students[13].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")
image student_14 = ConditionSwitch(
    "classroom_obj.all_students[14].needs_met(player) == True", "GUI/passing_seat.png",
    "True", "GUI/failing_seat.png")

# Declare characters used by this game.
# define e = Character('Eileen', color="#c8ffc8")

define p = Character('You', color="#c8ffc8")
define prin = Character('Principal')
define narrator = Character('Narrator')

#Screen overlay for the current Day count
screen day_display:
    window id "window":
        vbox:
            spacing 10
            text ("Day %d" % day_count):
                xpos 0
                ypos -450

#Screen overlay for Class Seating chart to show current students progress
screen class_seating_chart:
    window id "class":
        grid 5 3:
            xpos 500
            ypos -400
            
            image ConditionSwitch("classroom_obj.all_students[0].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")
            image ConditionSwitch("classroom_obj.all_students[1].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")
            image ConditionSwitch("classroom_obj.all_students[2].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")
            image ConditionSwitch("classroom_obj.all_students[3].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")
            image ConditionSwitch("classroom_obj.all_students[4].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")

            image ConditionSwitch("classroom_obj.all_students[5].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")
            image ConditionSwitch("classroom_obj.all_students[6].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")
            image ConditionSwitch("classroom_obj.all_students[7].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")
            image ConditionSwitch("classroom_obj.all_students[8].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")
            image ConditionSwitch("classroom_obj.all_students[9].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")

            image ConditionSwitch("classroom_obj.all_students[10].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")
            image ConditionSwitch("classroom_obj.all_students[11].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")
            image ConditionSwitch("classroom_obj.all_students[12].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")
            image ConditionSwitch("classroom_obj.all_students[13].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")
            image ConditionSwitch("classroom_obj.all_students[14].needs_met(player) == True", "GUI/passing_seat.png","True", "GUI/failing_seat.png")


init python:

    #BEGIN Global Variables

    CLASS_SIZE = 15

    #Maximum Trait Values
    MAX_INTELLIGENCE = 100 #Corresponds with STUDENT_LEARNING
    MAX_CHARISMA = 100 #Corresponds with STUDENT_ATTENTION
    MAX_DEXTERITY = 100 #Can affect the increase rate of Player.intelligence and Player.charisma
    MAX_CONSTITUTION = 50 #

    # Ranges used for determining Student's trait values:
    # Note that SKILL_NEED = MAX_SKILL_VALUE - STUDENT_TRAIT
    # ex: if MAX_INTELLIGENCE = 50 and STUDENT_LEARNING = 10
    # then, INTELLIGENCE_NEED = 50 - 10 = 40
    # Which means that the player must have at least 40 Intelligence skill points or greater
    # for that student's intelligence need to be met
    MIN_STUDENT_ATTENTION = 10
    MAX_STUDENT_ATTENTION = 25
    MIN_STUDENT_LEARNING = 10
    MAX_STUDENT_LEARNING = 25

    #END Global Variables

    #BEGIN Classes

    # Player Class
    # Represents the variables and functions that affect the player's character
    class Player:
        def __init__(self, intelligence, charisma, dexterity, constitution):
            if intelligence <= MAX_INTELLIGENCE:
                self.intelligence = intelligence
            else:
                raise Exception("Intelligence value out of bounds")
            if charisma <= MAX_CHARISMA:
                self.charisma = charisma
            else:
                raise Exception("Charisma value out of bounds")
            if dexterity <= MAX_DEXTERITY:
                self.dexterity = dexterity
            else:
                raise Exception("Dexterity value out of bounds")
            if constitution <= MAX_CONSTITUTION:
                self.constitution = constitution
            else:
                raise Exception("Constitution value out of bounds")
            self.first_name = ""
            self.last_name = ""
            self.salutation = ""

        def small_skill_increment_value(self, max_skill_value):
            return max_skill_value*0.05

        def medium_skill_increment_value(self, max_skill_value):
            return max_skill_value*0.1

        def large_skill_increment_value(self, max_skill_value):
            return max_skill_value*0.15

        #Makes sure values are within bounds
        def skill_value_adjustment(self):
            if self.intelligence > MAX_INTELLIGENCE:
                self.intelligence = MAX_INTELLIGENCE
            if self.intelligence < 0:
                self.intelligence = 0
            if self.charisma > MAX_CHARISMA:
                self.charisma = MAX_CHARISMA
            if self.charisma < 0:
                self.charisma = 0
            if self.dexterity > MAX_DEXTERITY:
                self.dexterity = MAX_DEXTERITY
            if self.dexterity < 0:
                self.dexterity = 0
            if self.constitution > MAX_CONSTITUTION:
                self.constitution = MAX_CONSTITUTION
            if self.constitution < 0:
                self.constitution = 0

        def increment_skill(self, level, skill_name):
            if level == "small":
                if skill_name == "intelligence":
                    self.intelligence += self.small_skill_increment_value(MAX_INTELLIGENCE)
                if skill_name == "charisma":
                    self.charisma += self.small_skill_increment_value(MAX_CHARISMA)
                if skill_name == "dexterity":
                    self.dexterity += self.small_skill_increment_value(MAX_DEXTERITY)
                if skill_name == "constitution":
                    self.constitution += self.small_skill_increment_value(MAX_CONSTITUTION)
            if level == "medium":
                if skill_name == "intelligence":
                    self.intelligence += self.medium_skill_increment_value(MAX_INTELLIGENCE)
                if skill_name == "charisma":
                    self.charisma += self.medium_skill_increment_value(MAX_CHARISMA)
                if skill_name == "dexterity":
                    self.dexterity += self.medium_skill_increment_value(MAX_DEXTERITY)
                if skill_name == "constitution":
                    self.constitution += self.medium_skill_increment_value(MAX_CONSTITUTION)
            if level == "large":
                if skill_name == "intelligence":
                    self.intelligence += self.large_skill_increment_value(MAX_INTELLIGENCE)
                if skill_name == "charisma":
                    self.charisma += self.large_skill_increment_value(MAX_CHARISMA)
                if skill_name == "dexterity":
                    self.dexterity += self.large_skill_increment_value(MAX_DEXTERITY)
                if skill_name == "constitution":
                    self.constitution += self.large_skill_increment_value(MAX_CONSTITUTION)
            self.skill_value_adjustment()

        def decrement_skill(self, level, skill_name):
            if level == "small":
                if skill_name == "intelligence":
                    self.intelligence -= self.small_skill_increment_value(MAX_INTELLIGENCE)
                if skill_name == "charisma":
                    self.charisma -= self.small_skill_increment_value(MAX_CHARISMA)
                if skill_name == "dexterity":
                    self.dexterity == self.small_skill_increment_value(MAX_DEXTERITY)
                if skill_name == "constitution":
                    self.constitution -= self.small_skill_increment_value(MAX_CONSTITUTION)
            if level == "medium":
                if skill_name == "intelligence":
                    self.intelligence -= self.medium_skill_increment_value(MAX_INTELLIGENCE)
                if skill_name == "charisma":
                    self.charisma -= self.medium_skill_increment_value(MAX_CHARISMA)
                if skill_name == "dexterity":
                    self.dexterity -= self.medium_skill_increment_value(MAX_DEXTERITY)
                if skill_name == "constitution":
                    self.constitution -= self.medium_skill_increment_value(MAX_CONSTITUTION)
            if level == "large":
                if skill_name == "intelligence":
                    self.intelligence -= self.large_skill_increment_value(MAX_INTELLIGENCE)
                if skill_name == "charisma":
                    self.charisma -= self.large_skill_increment_value(MAX_CHARISMA)
                if skill_name == "dexterity":
                    self.dexterity -= self.large_skill_increment_value(MAX_DEXTERITY)
                if skill_name == "constitution":
                    self.constitution -= self.large_skill_increment_value(MAX_CONSTITUTION) 
            self.skill_value_adjustment() 


        def tired(self):
            if self.constitution <= 0.15*MAX_CONSTITUTION:
                return True
            else:
                return False

        def skills_boost(self):
            if self.dexterity >= 0.5*MAX_DEXTERITY and not self.tired:
                return True
            else:
                return False

    # Student Class
    # Represents one student in the classroom.
    class Student:
        def __init__(self):
            #randomization of traits occurs upon initialization
            self.learning = self.random_skill_value(MIN_STUDENT_LEARNING,MAX_STUDENT_LEARNING)
            self.attention = self.random_skill_value(MIN_STUDENT_ATTENTION,MAX_STUDENT_ATTENTION)

        def random_skill_value(self, minimum, maximum):
            return renpy.random.randint(minimum, maximum)

        def needs_met(self, teacher):
            if teacher.intelligence >= MAX_INTELLIGENCE - self.learning:
                if teacher.charisma >= MAX_CHARISMA - self.attention:
                    return True
                else:
                    return False
            else:
                return False

    # Classroom Class
    # Contains Student objects
    class Classroom:
        def __init__(self):
            self.all_students = [Student() for i in range(CLASS_SIZE)] #instatiates CLASS_SIZE many student objects
        def class_passes(self,teacher):
            for student in self.all_students:
                if not student.needs_met(teacher):
                    return False
            return True

    #END Classes


# The game starts here.

label splashscreen:
    scene black
    with Pause(1)

    show text "Ebtissam Wahman Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return


label start:

    python:
        classroom_obj = Classroom()
        player = Player(20,20,20,50)
        day_count = 0
        weekly_training = False
        weekly_exam = False
        last_day_of_school = False

        def teach_class_label():
            if player.skills_boost() == True:
                return "Teach New Material (+INT, ++CHA --CON)"
            return "Teach New Material (+INT, +CHA --CON)"
    scene bg blank_bg
    play music "music/Groddle-Forest-Theme_1291876879.mp3"

    #jump first_day #For testing only

    "Welcome to Grade School Teacher Simulator"
    scene bg home_morning
    narrator "With some money loaned to you by your parents, you have moved to a new city to live on your own after graduating from college."
    narrator "Today is your first day as a 7th grade English Literature teacher at ABC Middle School. It's the first job you've ever had."
    narrator "The job market is saturated and it has been very difficult for you to find a job. The principal of ABC Middle has hired you under one condition..."
    scene bg school_corridor_morning 
    show principal neutral
    prin "That every student in your class successfully passes the 7th grade math standards exam at the end of the semester."
    prin "If they don't, we will be forced to let you go."
    scene bg home_morning
    narrator "It's quite a challenge, but you are confident that you can do this."
    narrator "What is your first name?"
    $ first_name = renpy.input("First Name:")
    $ first_name = first_name.strip()
    $ player.first_name = first_name
    narrator "What is your last name?"
    $ last_name = renpy.input("Last Name:")
    $ last_name = last_name.strip()
    $ player.last_name = last_name
    narrator "What salutation would your like to go by?"

    menu:
        "Ms.":
            $ player.salutation = "Ms."
        "Mr.":
            $ player.salutation = "Mr."
        "Mrs.":
            $ player.salutation = "Mrs."
        "Dr.":
            $ player.salutation = "Dr."
        "Professor":
            $ player.salutation = "Professor"

    narrator "Nice to meet you [player.salutation] [player.last_name]. You're first day of school begins now."

    scene bg school_morning
    narrator "Would you like to know the game basics?"
    menu: 
        "Yes":
            jump game_basics
        "No":
            jump first_day

    label game_basics:
    "How to Play" "You are a 7th grade teacher. You have 4 skill traits: Intelligence, Charisma, Dexterity, and Constitution"
    "How to Play" "Intelligence (INT): The higher this skill, the more successful you are with teaching the students the material."
    "How to Play" "Charisma (CHA): The higher this skill, the better students behave and pay attention in class."
    "How to Play" "Dexterity (DEX): The higher this skill, the faster you can build your Intelligence and Charisma skills. You can increase this skill by performing after school activities such as training and grading papers."
    "How to Play" "Constitution (CON): Measures your stamina, if this gets too low, it takes longer to build skills."

#Scene: First Day of School
    label first_day:
    scene bg school_morning
      
    p "Hello class, I will be your English Literature teacher starting today. You can call me [player.salutation] [player.last_name]"

#Scene: School Hours Turn   
    label school_hours:
    scene bg school_morning
    show screen day_display
    
    $ day_count+= 1
    if day_count%5 == 1 : #On the first day of the week, we reset the once a week training and exam variables and set constitution to max
        $ weekly_training = False
        $ weekly_exam = False
        $ player.constitution = MAX_CONSTITUTION
        if day_count > 1 : 
            p "What a relaxing weekend! Time to start a new school week."
    if day_count == 60: #12 weeks * 5 = 60, therefore day 60 is the last day of school
        $ last_day_of_school = True
        p "Today is the last day of school, better make it count..."

    if player.constitution == 0:
        p "I don't have much energy..."

    p "Today we are going to..."
    menu:
        "Teach a New Lesson" if player.constitution > 0:
            p "Today we are going to learn something new!"

            if player.tired() == True:
                p "I'm not feeling that great"
                $ player.decrement_skill("medium", "constitution")
            else:
                $ player.increment_skill("small", "intelligence")
                if player.skills_boost() == True:
                    $ player.increment_skill("medium","charisma")
                    p "I'm feeling more sociable than usual."
                else:
                    $ player.increment_skill("small", "charisma")
                    p "Everything seems to be going well."
                $ player.decrement_skill("medium", "constitution")

        "Have an Exam" if weekly_exam == False and player.constitution > 0: 
            $ weekly_exam = True
            p "Today we are going to have an exam. Please take out your #2 Pencils!"
            "Class" "Aww man..."
            if player.tired() == True:
                p "I'm not feeling that great"
                $ player.decrement_skill("small", "constitution")
            else:
                if player.skills_boost() == True:
                    $ player.increment_skill("medium","intelligence")
                    p "I'm feeling more enlightened than usual."
                else:
                    $ player.increment_skill("small", "intelligence")
                    p "Everything seems to be going well."
                $ player.decrement_skill("small", "constitution")

        "Watch a Movie" :
            p "Today we are going to take a break and watch a movie."
            "Class" "Yaaaay!"

    if last_day_of_school == True:
        "The school day has ended. The principal calls you over to his office."
        jump last_day_results

#Scene: Daily Status Report
    label status_report:
    scene bg school_afternoon
    "The school day has ended."
    show screen class_seating_chart
    "Here are the current predictions for the students."
    


#Scene: After School Turn
    label after_school:

    hide screen class_seating_chart

    if player.tired() == True:
        p "I'm feeling really tired."

    p "I've got some time for myself. What should I do?"


    menu:
        "Lesson Plan" if player.tired() == False:
            scene bg home_night 
            p "Time to plan some lessons."
            $ player.increment_skill("small", "intelligence")
            $ player.decrement_skill("medium", "constitution")
            p "I've got some good material planned."

        "Attend Training" if weekly_training == False and player.tired() == False: 
            $ weekly_training = True
            p "I'll attend this week's educator training course."
            scene bg school_evening
            $ player.increment_skill("small","intelligence")
            $ player.increment_skill("medium", "dexterity")
            $ player.decrement_skill("large", "constitution")
            scene bg home_night
            p "Who knew there was so much about teaching that I didn't know!"

        "Rest" : 
            scene bg home_night
            p "Time for some good old rest and relaxation."

    if last_day_of_school == False:
        jump school_hours

#Scene: Last Day of the school semester. Game Results.

    label last_day_results:

    scene bg principal_office
    show principal neutral
    prin "Good afternoon [player.salutation] [player.last_name]. As you may know today is the last day of the class. The students will be taking the 7th grade math standards exam tomorrow. We will discuss the results next week, enjoy the break!"

    scene bg home_morning
    narrator "A few days pass..."
    narrator "The principal gives you phone call one morning and tells you to come to his office."

    scene bg principal_office
    show principal neutral
    prin "Good morning. Today is the big day, we received the results from the exam..."
    
    show screen class_seating_chart

    if classroom_obj.class_passes(player) == True:
        show principal happy
        prin "It lookes like everyone in you class has passed!"
    else:
        show principal disappointed
        prin "It looks like not everyone in your class has passed..."
        prin "If you recall our agreement, then you know that we will have to terminate your employment with us."

    #TODO: SHOW CREDITS

    return
