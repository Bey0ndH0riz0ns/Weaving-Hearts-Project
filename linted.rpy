##############################
  ##  ##  ##  ##  ##  ####
  ##  ##  ##  ##  ##  ##  ##
  ##  ##  ##  ######  ####
  ##  ##  ##  ##  ##  ##
    ##  ##    ##  ##  ##
##############################

### Persistants
default persistent.sakura = 1

### Predefined
init:
    image d-sak-i c:
        ConditionSwitch(
        "persistent.sakura == 0", Image("images/d-sak-i 0.png"),
        "persistent.sakura != 0", Image("images/d-sak-i 1.png")
        )

init: ### Screen Locations
    ##   x only   ## These only effect left/right position, not up/down
    transform lx:#Just off screen left
        xanchor 1.0 xpos 0.0
    transform lw:#Just on screen against left wall
        xalign 0.0
    transform l7:
        xcenter -0.2
    transform l6:
        xcenter -0.1
    transform l5:##Split across left wall
        xcenter 0.0
    transform l4:
        xcenter 0.1
    transform l3:
        xcenter 0.2
    transform l2:
        xcenter 0.3
    transform l1:
        xcenter 0.4
    transform c0:#Centered
        xcenter 0.5
    transform r1:
        xcenter 0.6
    transform r2:
        xcenter 0.7
    transform r3:
        xcenter 0.8
    transform r4:
        xcenter 0.9
    transform r5:#Split across right wall
        xcenter 1.0
    transform r6:
        xcenter 1.1
    transform r7:
        xcenter 1.2
    transform rw:#Just on screen against right wall
        xalign 1.0
    transform rx:#Just off screen right
        xcenter 1.0
    transform xl:#Exit Left
        xcenter -2.0
    transform xr:#Exit Right
        xcenter 3.0
        ##   Other   ##
    transform ax:#centered 1 screen height above - For tripple height BGs
        ypos -.5 yanchor 0.5
        #ypos 0.0
    transform cx:#Aligned against ceiling
        ypos 0.0
    transform fx:#Aligned against floor
        ypos 1.0
    transform bx:#centered 1 screen height below - For tripple height BGs
        ypos 1.5 yanchor 0.5
        #ypos 1.0
    transform cc:# Cerner screen - For Mini-CG / Chibi
        ycenter 0.5
        xcenter 0.5
    transform ftr:# Faces sprites toward the right
        xzoom -1.0
init: ### Sprite Animation
    transform bounce:# makes the sprite jump
        linear 0.1 yoffset -80
        pause 0.1
        linear 0.1 yoffset 0
    transform nod:# makes the sprite bow/nod
        linear 0.2 yoffset 80
        pause 0.4
        linear 0.2 yoffset 0
    transform shake:# makes the sprite shake left/right
        linear 0.1 xoffset 40
        linear 0.1 xoffset -40
        linear 0.1 xoffset 40
        linear 0.1 xoffset -40
        linear 0.1 xoffset 40
        linear 0.1 xoffset -40

init: ### Character Shorthands
    #main
    define mc   = Character("MC"             ,color="#267f00")  # A #
    define gei  = Character("Geisha"         ,color="#eb448f")  # B
    define geiq = Character("???"            ,color="#eb448f")  # B
    define krn  = Character("Kirin"          ,color="#eb448f")  # B
    define har  = Character("Haruka"         ,color="#e53935")  # C #
    define hars = Character("Yamane Sensei"  ,color="#e53935")  # C #
    define krr  = Character("Kaori"          ,color="#8859ff")  # D
    define krr  = Character("Kirara"         ,color="#200857")  # E #
    define sca  = Character("Scarlet"        ,color="#900000")  # F
    define sco  = Character("Scotlyn"        ,color="#000000")  # G #
    #Side
    define bra  = Character("Brandon"        ,color="#0094ff")  # A #
    define braq = Character("???"            ,color="#0094ff")  # A #
    define bri  = Character("Brianne"        ,color="#000000")  # B
    define fum  = Character("Fumika"         ,color="#ffd700")  # C #
    define nek  = Character("Nekome"         ,color="#8afdff")  # D
    define nyk  = Character("Nyeko"          ,color="#8afdff")  # D
    define nekq = Character("???"            ,color="#8afdff")  # D
    define sho  = Character("Shoko"          ,color="#000000")  # E #
    define rin  = Character("Rin"            ,color="#08080f")  # F
    define tog  = Character("Toge"           ,color="#007f0e")  # G #
    define nad  = Character("Nadeshiko"      ,color="#a4b0e6")  # H
    #NRC
    define ats  = Character("Atsuko"         ,color="#000000")  # A #
    define kan  = Character("Kanou"          ,color="#000000")  # B
    define sjk  = Character("Malcolm"        ,color="#000000")  # C #
    define sjks = Character("Sinclair Sensei",color="#000000")  # C #
    define sor  = Character("Sora"           ,color="#000000")  # D
    define tam  = Character("Tamashii"       ,color="#000000")  # E #
    define yur  = Character("Yuri"           ,color="#00887a")  # F
    define yurs = Character("Karakada Sensei",color="#00887a")  # F
    #WW
    define alf  = Character("Alfred"         ,color="#000000")  # A #
    define asm  = Character("Asmund"         ,color="#000000")  # B
    define dad  = Character("Dad"            ,color="#000000")  # C #
    define may  = Character("Mayor"          ,color="#000000")  # D
    define sam  = Character("Sams"           ,color="#000000")  # E #
    #???
    define mar  = Character("Mari"           ,color="#000000")  # F
    define oto  = Character("Otto"           ,color="#000000")  # G #

## Misc

#
#image shortname = Movie(play="filename.ogv", pos=(0, 0), anchor=(0, 0))
#    e "For example, we might want to have text that is {b}bold{/b}, {i}italic{/i}, {s}struckthrough{/s}, or {u}underlined{/u}."


init: ### Character Sprites
    layeredimage a-hikari1:
            always:
                Image("a-hikari1_base.png")
            group o auto:
                attribute nude:
                    pos (155, 240)
                    zoom 0.3
                    ConditionSwitch("persistent.sakura == 0", Image("images/d-sakura-p 0.png"),"persistent.sakura != 0", Image("images/d-sakura-p 1.png"))
                attribute nude:
                    pos (155, 400)
                    zoom 0.3
                    ConditionSwitch("persistent.sakura == 0", Image("images/d-sakura-p 0.png"),"persistent.sakura != 0", Image("images/d-sakura-p 1.png"))
            group e auto:
                attribute neut default
    layeredimage a-hikari2:
            always:
                Image("a-hikari2_base.png")
            group o auto:
                attribute nude:
                    pos (155, 240)
                    zoom 0.3
                    ConditionSwitch("persistent.sakura == 0", Image("images/d-sakura-p 0.png"),"persistent.sakura != 0", Image("images/d-sakura-p 1.png"))
                attribute nude:
                    pos (155, 400)
                    zoom 0.3
                    ConditionSwitch("persistent.sakura == 0", Image("images/d-sakura-p 0.png"),"persistent.sakura != 0", Image("images/d-sakura-p 1.png"))
            group e auto:
                attribute neut default
    layeredimage a-sayaka1:
            always:
                Image("a-sayaka1_base.png")
            group o auto:
                attribute nude:
                    pos (140, 240)
                    zoom 0.3
                    ConditionSwitch("persistent.sakura == 0", Image("images/d-sakura-p 0.png"),"persistent.sakura != 0", Image("images/d-sakura-p 1.png"))
                attribute nude:
                    pos (170, 400)
                    zoom 0.3
                    ConditionSwitch("persistent.sakura == 0", Image("images/d-sakura-p 0.png"),"persistent.sakura != 0", Image("images/d-sakura-p 1.png"))
            group e auto:
                attribute neut default
    layeredimage a-sayaka2:
            always:
                Image("a-sayaka2_base.png")
            group o auto:
                attribute nude:
                    pos (140, 240)
                    zoom 0.3
                    ConditionSwitch("persistent.sakura == 0", Image("images/d-sakura-p 0.png"),"persistent.sakura != 0", Image("images/d-sakura-p 1.png"))
                attribute nude:
                    pos (170, 400)
                    zoom 0.3
                    ConditionSwitch("persistent.sakura == 0", Image("images/d-sakura-p 0.png"),"persistent.sakura != 0", Image("images/d-sakura-p 1.png"))
            group e auto:
                attribute neut default
    layeredimage a-yuzuki1:
            always:
                Image("a-yuzuki1_base.png")
            group o auto:
                attribute nude:
                    pos (160, 210)
                    zoom 0.35
                    ConditionSwitch("persistent.sakura == 0", Image("images/d-sakura-p 0.png"),"persistent.sakura != 0", Image("images/d-sakura-p 1.png"))
                attribute nude:
                    pos (180, 420)
                    zoom 0.3
                    ConditionSwitch("persistent.sakura == 0", Image("images/d-sakura-p 0.png"),"persistent.sakura != 0", Image("images/d-sakura-p 1.png"))
            group e auto:
                attribute neut default
    layeredimage a-yuzuki2:
            always:
                Image("a-yuzuki2_base.png")
            group o auto:
                attribute nude:
                    pos (160, 210)
                    zoom 0.35
                    ConditionSwitch("persistent.sakura == 0", Image("images/d-sakura-p 0.png"),"persistent.sakura != 0", Image("images/d-sakura-p 1.png"))
                attribute nude:
                    pos (180, 420)
                    zoom 0.3
                    ConditionSwitch("persistent.sakura == 0", Image("images/d-sakura-p 0.png"),"persistent.sakura != 0", Image("images/d-sakura-p 1.png"))
            group e auto:
                attribute neut default
    layeredimage a-nana:
        always:
            Image("a-nana_base.png")
        group o auto:
            attribute znak:
                zoom 0.3
                ConditionSwitch("persistent.sakura != 0", Image("images/d-sakura-p 1.png",pos=(420-(3*30), 900-(3*30)))   ,   "persistent.sakura == 0", Image("images/d-sakura-p 0.png"))
            attribute znak:
                zoom 0.3
                ConditionSwitch("persistent.sakura != 0", Image("images/d-sakura-p 1.png",pos=(590-(3*30), 900-(3*30)))   ,   "persistent.sakura == 0", Image("images/d-sakura-p 0.png"))
            attribute znak:
                zoom 0.3
                ConditionSwitch("persistent.sakura != 0", Image("images/d-sakura-p 1.png",pos=(550-(3*30), 1450-(3*30)))   ,   "persistent.sakura == 0", Image("images/d-sakura-p 0.png"))
        group e auto:
            attribute hap1 default
        attribute p_hold:
            Image("a-nana_p_hold.png")
    layeredimage a-roka:
        always:
            Image("a-roka_base.png")
        group o auto:
            attribute 1znak:
                "a-roka_o_1znak.png"
            attribute 1znak:
                zoom 0.3
                ConditionSwitch("persistent.sakura != 0", Image("images/d-sakura-p 1.png",pos=(500-(3*30), 800-(3*30)))   ,   "persistent.sakura == 0", Image("images/d-sakura-p 0.png"))
            attribute 1znak:
                zoom 0.3
                ConditionSwitch("persistent.sakura != 0", Image("images/d-sakura-p 1.png",pos=(660-(3*30), 800-(3*30)))   ,   "persistent.sakura == 0", Image("images/d-sakura-p 0.png"))
            attribute 1znak:
                zoom 0.3
                ConditionSwitch("persistent.sakura != 0", Image("images/d-sakura-p 1.png",pos=(550-(3*30), 1350-(3*30)))   ,   "persistent.sakura == 0", Image("images/d-sakura-p 0.png"))
            attribute 2znak:
                "a-roka_o_2znak.png"
            attribute 2znak:
                zoom 0.3
                ConditionSwitch("persistent.sakura != 0", Image("images/d-sakura-p 1.png",pos=(500-(3*30), 800-(3*30)))   ,   "persistent.sakura == 0", Image("images/d-sakura-p 0.png"))
            attribute 2znak:
                zoom 0.3
                ConditionSwitch("persistent.sakura != 0", Image("images/d-sakura-p 1.png",pos=(660-(3*30), 800-(3*30)))   ,   "persistent.sakura == 0", Image("images/d-sakura-p 0.png"))
            attribute 2znak:
                zoom 0.3
                ConditionSwitch("persistent.sakura != 0", Image("images/d-sakura-p 1.png",pos=(550-(3*30), 1350-(3*30)))   ,   "persistent.sakura == 0", Image("images/d-sakura-p 0.png"))
        group e auto:
            attribute hap1 default
    ########################    ########################    ########################
    layeredimage x-sakura_check_template_step_1:
        always:
            Image("a-roka_base.png")    #Naked sprite you want to censor
        always:
            Image("xdbg-grid.png")       #Grid with increments every 100px
        always:
            zoom 0.3                     #~Distance-Between-Nips/300 to 1 Decimal Place
            pos(500-(3*30), 800-(3*30)) #left-nip (xpos+15zoom, ypos25zoom)
            Image("xdbg-sakura.png") #Sakura with 100px grid scaled with sprite
        always:
            zoom 0.3                        # #zoom same as above
            pos(660-(3*30), 800-(3*30))    # #vagoo (xpos-300zoom, ypos-300zoom)
            Image("xdbg-sakura.png")
        always:
            zoom 0.3                        # #zoom same as above
            pos(550-(3*30), 1350-(3*30))    # #vagoo (xpos-300zoom, ypos-300zoom)
            Image("xdbg-sakura.png")
    layeredimage x-sakura_check_template_step_2:
        always:
            Image("a-roka_base.png")    #Naked sprite you want to censor
        group o auto:
            attribute 1znak:
                "a-roka_o_1znak.png" # If applicable
            attribute 1znak:#copy from above
                zoom 0.3
                ConditionSwitch("persistent.sakura != 0", Image("images/d-sakura-p 1.png",pos=(500-(3*30), 800-(3*30)))   ,   "persistent.sakura == 0", Image("images/d-sakura-p 0.png"))
            attribute 1znak:#copy from above
                zoom 0.3
                ConditionSwitch("persistent.sakura != 0", Image("images/d-sakura-p 1.png",pos=(660-(3*30), 800-(3*30)))   ,   "persistent.sakura == 0", Image("images/d-sakura-p 0.png"))
            attribute 1znak:#copy from above
                zoom 0.3
                ConditionSwitch("persistent.sakura != 0", Image("images/d-sakura-p 1.png",pos=(550-(3*30), 1350-(3*30)))   ,   "persistent.sakura == 0", Image("images/d-sakura-p 0.png"))
label spritecheck:
    scene b-blackscreen with dissolve
    "Sprite checker"
    window hide
    show x-sakura_check_template_step_1:
        l3
        cx
        zoom 0.5
    pause
    show x-sakura_check_template_step_2 1znak:
        c0
        cx
        zoom 0.5
    pause
    show a-roka 1znak:
        r3
        cx
        zoom 0.5
    pause
    window auto
    scene b-blackscreen with dissolve
    jump devmen

#show a-roka2 casu  #will show roka with outfit "casual"
#show a-roka2 work  #will change outfit to "work"
#show a-roka2 -work #will remove outfit work but WILL NOT correctly show a nude srite
#show a-roka2 nude  #will change outfit to "nude" correctly

label start: ### Start Of Game
    $ txtbox = 00
    "Welcome to the WIP Weaving hearts VN"
    show ax-roka1_o_1zpan:
        cx
        l4
        zoom 1.0
    show ax-roka2_o_1zpan:
        cx
        l1
        zoom 0.75
    show ax-roka3_o_1zpan:
        cx
        r2
        zoom 0.5
    show ax-roka4_o_1zpan:
        cx
        r4
        zoom 0.25
    "\nSprites at 100\%, 75\%, 50\%, and 25\% size"
    window hide
    #scene tstgry
    #"..."
    #$ txtbox = 22
    #"This uses the first frame style."
    #$ txtbox = 30
    #"This uses the second frame style."
    #define a = Character("Test Character 1", color="#200857", who_outlines=[ (1, "#ffffff") ], what_outlines=[ (1, "#ffffff") ])
    #define b = Character("Test Character 2", color="#08080f", who_outlines=[ (1, "#ffffff") ], what_outlines=[ (1, "#ffffff") ])
    #a "This is Kirara's colour"
    #b "And this is Rin's colour"
    ### Dev Scene Select
label devmen: ### Dev Menu
    image ScSeTx = Text(_("Dev Scene select"), size=120)
    show ScSeTx with dissolve:
        c0
        ypos 0.0
    menu:
        "Dev Sprite Checker":
            hide ScSeTx with dissolve
            jump spritecheck
        "Prologue Intro":
            hide ScSeTx with dissolve
            jump prologue_intro
        "Prologue Concert Q&A":
            hide ScSeTx with dissolve
            jump prologue_qna
        "Prologue Concert End":
            hide ScSeTx with dissolve
            jump prologue_concert_end
        "Wholesome Library Scene":
            hide ScSeTx with dissolve
            jump wholesome_library
        "Sakura Mode Explanation":
            hide ScSeTx with dissolve
            jump experimental
        "Sakura Mode Demo":
            hide ScSeTx with dissolve
            jump demo_h_start
        "End":
            hide ScSeTx with dissolve
            jump end_of_wip
label scene_bookends: ## Copy when making new scene
    "{i}scene_bookend start{/i}"
    scene b-blackscreen with dissolve
    $ txtbox = 00
    "{i}scene_bookend end{/i}"
    scene b-blackscreen with dissolve
    pause 1 # "
label prologue_intro:
    "{i}Prologue, Scene 1*{/i}"
    scene b-blackscreen with dissolve
    $ txtbox = 12
    "{i}Before the Concert{/i}"
    #[mc is seated on a bench in the city’s largest park, gazing into the darkening sky]
    "(Some kind of profound monologue regarding his current view of the world, idfk)"
    mc  "(I was so lost in thought that I hadn’t noticed how long I had been sitting here, waiting.)"
    #[A can of chilled soda appears as the text is read]
    mc  "(It was only when I had felt the touch of an ice cold object pressed against the nape of my neck that I realized I had been daydreaming)"
    #[Silhouette of Brandon’s sprite appears, as screen shakes to signify mc jolting up]
    mc  "?!"
    braq "Oh, hey, you are awake."
    #[Pulling out his phone to see the time was now 6:34 PM]
    mc  "Yeah, I am. You’re cutting it close. What took you so long?" #[Slightly annoyed tone]
    #[Brandon’s silhouette fully becomes the character’s sprite]
    bra "Missed the damn train because I had to make a stop. Got us some drinks and snacks, see?" #[Lifts up a convenience store bag full of items]
    "(The person that had just risen me from my stupor was my close friend, Brandon Marsh. We’ve known each other since we were kids, but we didn’t really grow up together.)"
    "(I only ever saw him when I would visit my grandparents here in the city, since his house was just down the road. You could probably tell from his mannerisms and appearance, but he’s not from Japan.)"
    "(He tells me that when he was 2 years old, his parents were so fascinated by the country that they moved here, though that wasn’t without some issues.)"
    "(Because of this, he was raised by both the Japanese school system and the American mannerisms that his parents carried over from their last residence. The first time I met him, I was 5 years old, and we've become good friends since.)"
    #[Standing up from the bench]
    mc  "I guess that saves us some money, then. C’mon, the show starts at 7, and we still have to get through the line at security"
    bra "Shit, you’re right. Yeah, let’s hurry"
    #[mc and Brandon begin walking further through the park to the concert venue, which is a stage set up near the center of the grass]
    bra "So what made you a fan of this Scarlett girl? I didn’t think you were the type to follow anything idol related."
    mc  "Well, sometime before I moved here, I was scrolling through a bunch of channels. One of them was this broadcast showcasing a bunch of up-and-coming artists. Most of them didn’t really stand out to me. Felt like they were all part of this blur"
    #[Looking to the side at mc]
    bra "But she did, huh?"
    mc  "Yeah… I don’t know what it was about her."
    #[mc begins to look up to the sky, in which the sun had already set]
    mc  "She just felt so vibrant, you know? Singing those songs all while dancing with a smile. It all just felt… cool, I guess. I don’t know, she just feels right to me, like she just knew how to pique my fancy"
    #[Camera cuts back to scene]
    bra "And that’s why you wanted to go to the first concert available, to see your new favorite idol live?"
    mc  "Yeah, you caught me" #[Mockingly defeated tone]
    bra "I thought that was the case. Because I thought you’d wanna see more of Scarlett tonight…"
    #[Brandon pulls out 2 tickets from his hoodie pockets, and hands one to mc]
    bra "...I got us these"
    mc  "No way!"
    mc  "Are those the deluxe tickets that sold out weeks ago?!"
    bra "Sure are"
    mc  "Don’t these cost quite a bit? I’ll pay you back later, when I can"
    #[Waving his hand in front of him dismissively]
    bra "Nah, don’t sweat it. Just think of this as a welcome gift from me."
    mc  "Oh, well, thanks dude. This is actually a really nice thing of you to do for once"
    bra "Like I’m ever not nice" #[Sarcastically]
    mc  "Well, it’s a good thing you told me now, because there’s a second line for special ticket holders to go right through"
    #[mc points at a shorter, much faster line into the venue with a sign that reads "deluxe patrons only"]
    bra "I knew I made the right call to make that stop"
    mc  "What was that?" #[Quizzically]
    bra "Nothing, let’s head in"
    "(The wait had just barely reached the 5 minute mark when we got cleared to enter. It was now 6:50, ten minutes until showtime. And the other line looked like it wouldn’t be fully cleared until after the show had already started.)"
    mc "(Thanks again Brandon)"
    #[Scene transitions to the concert]
    "(The crowd was unlike anything I had seen before. At least a thousand or two strangers crammed into this small section of the park. There was no ceiling, so you could look up and see the night sky.)"
    "(The stage spotlights were currently aimed at the crowd as one of the sole sources of light for the crowd to see and navigate with. But thanks to our nearly late arrival, Brandon and I were stuck near the rear middle, a good 15 rows away from the stage.)"
    "(But I could thankfully still see the stage clearly, the sea of heads indicative of just how popular Scarlett must be. Before long, the voice of a hypeman roars through the speakers.)"
    "Hypeman" "Alright, you precious little Roses. You’ve been waiting long enough. Give some cheer to your darling senpai, Scarlett!"
    #[The crowd begins counting down with the hypeman]
    "Hypeman" "In 5{w=0.2}.{w=0.2}.{w=0.2}.{w=0.4} 4{w=0.2}.{w=0.2}.{w=0.2}.{w=0.4} 3{w=0.2}.{w=0.2}.{w=0.2}.{w=0.4} 2{w=0.2}.{w=0.2}.{w=0.2}.{w=0.4} 1{w=0.2}.{w=0.2}.{w=0.2}.{w=0.4}"
    #"(When the countdown had reached zero, all the lights in the area had shut off. In this period of pitch black respite, a wave of glow sticks from raving fans had emerged, dimly illuminating the restless and excited crowd.)"
    #"(When the stage lighting had reactivated, there stood Scarlett, who opened up her performance with her iconic line)"
    sca "Heeeeyyyy, everyone~"
    #[Sounds of the roaring crowd following this opening line]
    sca "How are my lovely little Roses doing on this fine evening? I hope you’re prepared to get pumped up, because the show starts now!"
    "(The instrumental of her latest single began to play, as the crowd cheered Scarlett on.)"
    "(The vibrant flashing lights, in conjunction with Scarlett’s stellar singing and captivating rhythmic dances, had created a vivid image that could never be achieved by just viewing a televised broadcast.)"
    "(This was here. This was now. This was Scarlett’s magic spell in action. I stood there in awe, unable to even cheer myself with just how incredible this spectacle was.)"
    "(At least an hour had gone by with this routine keeping my attention in this tunnel visioned daydream. Before I realized, the performance had come to an end and I was left wanting for more.)"
    "(The sounds of encore raging throughout the park awoke me, along with an announcement from Scarlett herself)"
    sca "This isn’t the end yet, Roses. You dedicated fans already know that just after this, there will be a meet and greet Q&A panel, where you can request any question of your darling senpai, at the adjacent tent. See you there, lovelies."
    #[Scarlett then walks towards the backstage, vanishing behind the curtains]
    mc  "(Seemingly reading my mind, I felt Brandon tap my shoulder, speaking to me.)"
    bra "That’s us, get your ticket ready"
    mc  "Yeah, I have it here. We should head over"
    #[mc and Brandon begin to walk over to the exit and towards the neighboring tent]
    "{i}Scene End{/i}"
    scene b-blackscreen with dissolve
    pause 1 # "
label prologue_qna:
    "{i}Prologue, Scene 3*{/i}"
    scene b-blackscreen with dissolve
    $ txtbox = 12
    "{i}After? the Concert{/i}"
    #[Connor and Brandon exit the concert tent and begin walking towards the end of the line full of deluxe ticket holders, waiting to enter the tent where the Q&A panel would be held]
    bra "So what’d you think? Worth the price of the tickets?"
    mc  "Yeah, definitely. I’ll be going to the next concert if I find the time. You wanna tag along?"
    bra "Sure, I’m down with that."
    #[Brandon notices that he has to use the restroom]
    bra "Hey, go ahead and get in line without me. Gotta use the restroom real quick."
    mc  "Oh, alright. Get back here quick, though. I don’t wanna be in this line alone for too long."
    #[Brandon begins heading away from the line, while Connor moves towards it]
    #[Connor gazes at how long the line has formed]
    mc  "No wonder those tickets sold ou-"
    #[Geisha’s silhouette appears, screen shakes]
    geiq "He…GYA-!"
    mc  "(Since I was distracted by my own thoughts, I didn’t notice that I was about to crash into someone else. I heard her cry out slightly before we were both sent to the ground from our collision)"
    #[Scene switches to image of Connor helping Geisha back on her feet]
    mc  "Hey, you ok? I wasn’t looking ahead."
    geiq "Sorry! My bad, shoulda been, like, watching where I was going…"
    mc  "(Oh god, not this trend…)"
    mc  "That’s good. Here, lemme help you up."
    #[Scene changes to previous backdrop, but Geisha’s sprite is fully visible now]
    geiq "Yeah, thanks. Sorry, if I'm, like, making you late somewhere."
    mc  "No, it’s fine. I’m just about to get in the line here."
    geiq "You’re here for the panel? Like, no way! How did you even manage to buy the tickets? They sold out in, like, 30 seconds."
    mc  "Oh, that was thanks to my friend. I don't know where he got them, but we came here together."
    geiq "Tsk… fuckin’ lucky…"
    mc  "What, did you not manage to get them?"
    geiq "No… just barely had enough to, like, get the basic one…"
    mc  "Well, that’s too bad, I gue-"
    #[Nekome’s sprite rushes into the scene, out of breath]
    nekq "Kiriiiin~! Wait up~!"
    mc  "(Kirin…?)"
    krn "Oh hii~, Nyeko-chan. What’s up?"
    nyk "Why’d you run off like that?"
    #[Pouty-like]
    krn "I just felt like getting out of here, ya know?"
    nyk "But Kirin, Atsuko managed to, like, upgrade our tickets. I wanted to tell you, but you, like, ran off and stuff."
    #[Excitedly]
    krn "She did? Like, how??"
    nyk "I don't know, but she told me to come get you and bring you back."
    krn "Like, where is she then?!"
    nyk "She should be near the front now, so we should like-"
    #[Geisha’s sprite rushes off (with a sound like they use in cartoons, you know the kind)]
    nyk "Heyy~! Don’t do that~"
    #[Nekome turns to Connor, giving him a quick silent glance, before her sprites also rushes off, but slower than Geisha]
    mc  "(Wonder what her deal is. Still, glad that girl’s problem got solved.)"
    #[Connor begins walking to the end of the line, and starts waiting his turn. Brandon soon returns]
    bra "Yo, I miss anything?"
    mc  "Nah, you’re fine. Just ran into this group of gals. Nothing really happened though."
    bra "Ok, then. Let’s get in there."
    mc  "(Kirin, huh? I think I know that name. I’ll have to check if it really was them…)"
    #[The scene transitions into the tent]
    mc  "(Brandon and I take our seats. I can’t get a good look to see where that Kirin girl and her friends are, but that’s fine.)"
    #[Scarlett’s sprite appears]
    mc  "(The panel began, but the questions were lackluster for the most part, usually just about Scarlett’s sizes, her address… things she would never even want to answer. It continued like this until a reporter stood up and posed a rather odd question that received an even more outstanding answer.)"
    "Reporter" "Rumor has it that you’re still in highschool, Ms. Scarlett, but you’re set to graduate this year. Is this a claim that you can confirm, and what would it mean for your career going forward?"
    #[Scarlett’s sprite takes on somewhat of a strained smile]
    sca "Oh, wow~! You must know your stuff, huh…?"
    #[Sprite returns to normal]
    sca "Well, I’ll have you know that I definitely have big plans coming up by the end of the year. Because, and you heard this here first, my little roses, I’m planning on taking on the idol industry in Japan by storm, and rising to the top!"
    #[The crowd cheers]
    sca "And not only that, when I’m done with Japan, I’m going after the world itself! I hope you’ll be there to support your darling Senpai."
    #[Scarlett’s sprite puts on a cute face]
    sca "Won’t you?"
    #[Crowd cheers even louder than before]
    mc  "(She’s really planning on doing all that? Well, damn, I’ll be on that wild ride too.)"
    mc  "(...but wait, what about the first part? She didn’t outright deny it. It’s more like she… tried to avoid it. Whatever the case, I’ll try my best to show her my support.)"
    #[Scene fades to black]
    mc  "(The panel continued on with nothing else special happening. After a series of answered questions, Scarlett thanked everyone for coming, and she retired backstage while the crowd dispersed towards the exit. After we left the venue, Brandon and I walked back to the train station. On the train, I told Brandon what I thought of her avoiding the question, and he replied that it’s just her business and she doesn’t have to tell anybody. After we got off the train, we walked down to our houses, said our good nights, and turned in for some sleep.)"
    "{i}Scene End{/i}"
    scene b-blackscreen with dissolve
    pause 1 # "
label prologue_concert_end:
    "{i}Prologue, Scene 2*{/i}"
    ##concert scene at night.
    scene b-stage n1
    $ txtbox = 22
    "{i}b-stage n1.png - Stage BG night{/i}"
    #scarlett excited
    show cm-concertzoom 1 at cc with dissolve
    "{i}cm-concertzoom 1.png - Agreed mini-CG showing a closeup of scarlet on stage{/i}"
    sca "I hope everyone has had as much fun as I have!"
    "Crowd" "YEAH!!!!"
    show cm-concertzoom 2
    sca "The meet and greet starts in half an hour, so make sure to stick around!"
    show cm-concertzoom 1
    sca "It's going to be awhile before my next concert, so I'd like to make this count! See you all in a few!"
    hide cm-concertzoom with dissolve
    ##crowd in background, at crowd level
    ##brandon appears mid-screen
    #brandon smug
    show a-bra smug:
        ftr
        l3
        bx
        ease 1.0 fx
    show a-mc smile:
        r3
        bx
        ease 1.0 fx
    bra "Wow, what a first date, didn’t think it’d be so glamorous."
    bra "I kinda had a feeling you were excited to see me again, but damn, didn’t think you’d go this far."
    mc  "Says the one who made us snacks, don’t act like you’re not into it."
    #bradon smiling
    show a-bra smile
    bra "Into baking sweets and watching you fangirl? Absolutely."
    bra "But I will say, Scarlett is pretty sweet."
    mc  "Isn’t she? I knew you’d get it."
    #brandon slight frown
    show a-bra frown
    bra "Oh cool, you’re doing that selective hearing thing again.."
    show a-mc:
        linear 0.2 ftr
        pause 0.2
        linear 0.5 xr
    mc  "LET’S GO MEET SCARLETT!"
    ##mc fades from screen
    bra "{cps=*0.1}Aaaand{/cps} he’s gone."
    show a-bra:
        linear 4.0 xr
    show b-blackscreen with dissolve
    ##same crowd scene just after transition
    ##scarlett enters mid-screen
    #scarlett happy
    show a-bra neutral at l4
    show a-mc awkward at l2
    show a-sca smile at r3
    show a-mc:
        ease 1.0 l1
    hide b-blackscreen with dissolve
    pause 0.5
    sca "Hi, it’s nice to meet you! As you know, I’m Scarlett! Always awesome to see a new fan!"
    mc  "…"
    mc  "(DAMMIT! NOW THAT I’M HERE, WHAT DO I SAY!)"
    mc  "(OH MY GOD, SHE'S ACTUALLY IN FRONT OF ME!)"
    show a-bra frown
    "Not Brandon" "(You can take five guys, but not this?)"
    mc  "(How the hell does he always do that?)"
    #scarlett nervous smile
    show a-sca awkward
    sca "{cps=*0.1}Soooo,{/cps} {w=1.0} {cps=*0.5}what’s your name?{/cps}"
    python:
        mcn = renpy.input(_("What {i}is{/i} my name?"))
        mcn = mcn.strip() or "MC"
    #brandon enters left side
    show a-bra smile:
        ease 1.0 l3
    bra "Hey, I’m Brandon and this is [mcn], sorry he’s weird."
    bra "Great show by the way."
    #scarlett excited
    show a-sca laugh:
        bounce
    sca "Thank you! I’m glad you liked it! I always try to put on a good show!"
    #brandon angry
    show a-bra angy
    "..."
    #brandon shakes MC
    #scarlett shocked
    show a-bra:
        linear 0.2 l2
        shake
    pause 0.2
    show a-mc gya:
        shake
    show a-sca scared:
        linear 0.2 r4
    pause 1.0
    bra "You were so excited, say something, idiot!"
    show a-sca awkward
    show a-mc awkward:
        ease 0.5 c0
    mc  "Right! I-I’m a huge fan, I just wanted to say I’ve been a fan for a long time and your music has helped me a lot!"
    mc  "I was hoping you could sign this."
    #scarlet hops twice
    show a-sca laugh:
        bounce
        bounce
    #scarlet happy
    pause 1.0
    show a-sca laugh
    sca "Absolutely!"
    #brandon smug
    show a-bra smug
    show a-mc smile:
        ease 1.0 r1
    show a-sca:
        ease 0.5 r3
        pause 0.5
        ease 0.3 yoffset 20
    bra "Hey, you did it! My boys all grown up!"
    mc  "You’re really asking to get put on your ass."
    bra "If you're offering."
    #brandon smile
    show a-bra smile
    show a-sca:
        ease 0.3 fx
        pause 0.3
        ease 0.3 yoffset 0
    sca "Here you go! Hope to see you at my next concert!"
    show a-mc:
        ease 0.5 c0
    mc  "I’ll be there!"
    show a-sca:
        nod
    show a-mc:
        nod
    #sacrlett fades from screen
    #brandon fades from screen
    pause 0.8
    show a-sca:
        linear 0.5 alpha 0.0
    show a-bra:
        linear 0.5 alpha 0.0
    mc  "(I love this town.)"
    scene b-blackscreen with dissolve
    pause 1 # "
    "{i}Scene End{/i}"
    #this is a test line from Able98Able98
    #This is another test line from able98able98
label wholesome_library:
    "{i}Wholesome Library Scene start{/i}"
    scene b-cl-library d
    $ txtbox = 22
    "{i}With assets shamelessly stolen from Cafe Stella's BG{/i}"
    window hide
    show bx-lib-yuzu desk-look
    show bx-lib-toge tble-read:
        ypos 2.0
    show bx-lib-neko desk-b
    show b-blackscreen
    pause 1.0
    hide b-blackscreen with dissolve
    pause
    show bx-lib-neko shlf with dissolve
    show bx-lib-yuzu desk-read with dissolve
    pause # Toge comes in the room
    show bx-lib-yuzu desk-surp
    pause 0.15
    show bx-lib-yuzu desk-neu with dissolve
    pause 0.6
    show bx-lib-yuzu desk-look with dissolve
    show bx-lib-toge with dissolve:
        ypos 0.0
    pause 1.5
    show bx-lib-yuzu desk-read with dissolve
    pause # Neko sits down
    show bx-lib-neko tble-read with dissolve
    pause
    show bx-lib-yuzu desk-look with dissolve
    pause # Toge gets up
    show bx-lib-yuzu desk-look-surp
    pause 0.15
    show bx-lib-yuzu desk-read with dissolve
    pause 0.15
    show bx-lib-toge shlf with dissolve
    pause # Toge sits down
    show bx-lib-toge tble-read with dissolve
    show bx-lib-yuzu desk-look with dissolve
    pause 0.2
    show bx-lib-yuzu desk-read with dissolve
    pause # Neko gets up
    show bx-lib-neko shlf with dissolve
    pause # Neko sits down
    show bx-lib-neko tble-read with dissolve
    pause # Yuzu wonders what's up
    show bx-lib-yuzu desk-conf with dissolve
    pause 0.5
    show bx-lib-cc-angy 1-i    with dissolve
    pause
    show bx-lib-cc-angy 1-ii   with dissolve
    pause
    show bx-lib-cc-angy 1-iii  with dissolve
    pause
    show bx-lib-cc-angy 1-iv   with dissolve
    pause # Yuzu awkward
    hide bx-lib-cc-angy        with dissolve
    image bx-lib-yuzu desk-awk:
        "bx-lib-yuzu desk-awk-i"
        pause 0.1
        "bx-lib-yuzu desk-awk-ii"
        pause 0.1
        "bx-lib-yuzu desk-awk-iii"
        pause 0.1
        "bx-lib-yuzu desk-awk-iv"
        pause 0.1
        repeat
    show bx-lib-yuzu desk-awk with dissolve
    pause # Toge leaves
    show bx-lib-yuzu desk-look-surp
    pause 0.15
    hide bx-lib-toge with dissolve
    pause 0.15
    show bx-lib-yuzu desk-neu with dissolve
    pause 1.0
    show bx-lib-yuzu desk-read with dissolve
    pause
    show bx-lib-neko desk with dissolve
    pause 0.5
    show bx-lib-yuzu desk-look-conf with dissolve
    pause
    window auto
    show bx-lib-yuzu desk-look with dissolve
    show bx-lib-neko desk-conf with dissolve
    pause
    nek "There was someone else here?"
    "{i}Wholesome Library Scene end{/i}"
    pause 1 # "
label experimental:
    scene b-blackscreen with dissolve
    $ txtbox = 00
    "{i}Start of Experimental section{/i}"
    show d-sak-i x:
        alpha 0.5
        xalign 1.0
        yalign 0.0
    "This game has a patent pending Sakura setting for H scenes to make them SFYT and ease editing"
    image d-sakura-p1 c:
        ConditionSwitch(
        "persistent.sakura == 0", Image("images/d-sakura-p 0.png"),
        "persistent.sakura == 1", Image("images/d-sakura-p 1.png"),
        "persistent.sakura == 2", Image("images/d-sakura-p 1.png")
        )
    show d-sakura-p1 1 with dissolve:
        alpha 0.5
        yoffset -30
    show d-sak-i 1 with dissolve:
        linear 0.6 alpha 1.0
    "A petal will appear in the corner during H-Scenes"
    show d-sak-i 3 with dissolve
    "The specific petal shows what mode is selected"
    "Sakura has 3 modes:"
    show d-sak-i 0:
        linear 0.2 alpha 0.5
        linear 0.2 alpha 1.0
    "Sakura has 3 modes:{fast}
    \n - NONE: H-Scenes will play uninpeeded"
    show d-sak-i 1:
        linear 0.2 alpha 0.5
        linear 0.2 alpha 1.0
    "Sakura has 3 modes:
    \n - NONE: H-Scenes will play uninpeeded{fast}
    \n - ZOOM: H-Scenes will be kept SFYT"
    show d-sak-i 2:
        linear 0.2 alpha 0.5
        linear 0.2 alpha 1.0
    "Sakura has 3 modes:
    \n - NONE: H-Scenes will play uninpeeded
    \n - ZOOM: H-Scenes will be kept SFYT{fast}
    \n - SKIP: H-Scenes will be skipped"
    show d-sak-i 3 with dissolve:
        linear 0.3 alpha 0.5
    "Sakura can be changed in the preference menu at any time though it might not update immediately"
    show d-sak-i c:
        linear 0.2 alpha 1.0
        linear 0.2 alpha 0.5
        linear 0.2 alpha 1.0
        linear 0.2 alpha 0.5
    if persistent.sakura == 0:
        "Sakura is curreltly set to NONE."
    elif persistent.sakura == 1:
        "Sakura is curreltly set to ZOOM."
    elif persistent.sakura == 2:
        "Sakura is curreltly set to SKIP."
    else:
        "Sakura is currently not set"
    "Now for an example"
    scene b-blackscreen with dissolve
label demo_h_start:
    scene b-blackscreen with dissolve
    $ txtbox = 30
    "{i}Demo H-scene{/i}"
    define roka = Character("Roka"  ,color="#e07070")
    define nana = Character("Nanao" ,color="#b06060")
    show a-roka 1casu hap1 with dissolve:
        l2
        cx
        zoom 0.75
    show a-nana 1work hap1 with dissolve:
        r2
        cx
        zoom 0.75
    roka "I really enjoyed this evening dear."
    nana "Awww sweetie, Me too."
    nana "It's nice to do someting special from time to time."
    show a-roka 2casu haps
    roka "Y-yeah."
    show a-nana hap1:
        ease 0.8 c0
    show a-roka 1casu hap0 with dissolve
    show a-roka:
        ease 0.5 l1
    nana "Awww, come here."
    "..."
    show a-nana:
        ease 0.8 r1
    nana "It's about time we turn in for the night."
    show a-roka awk1  with dissolve
    roka "Um..."
    show a-nana awk2 with dissolve
    nana "Yes dear?"
    show a-roka:
        ease 0.4 xoffset -20
        ease 0.4 xoffset  20
        ease 0.5 xoffset -20
        ease 0.6 xoffset  20
        ease 0.4 xoffset   0
    roka "...Hey so this might be weird but I kinda wanted to try something..."
    nana "What, you want to try being the big spoon?"
    show a-roka surp with dissolve
    roka "No...{w=0.1} Not that."
    show a-roka 1casu awk1 with dissolve
    roka "...{w=0.3} I mean maybe annother tine but I actually meant something else."
    show a-nana hap1 with dissolve
    nana "Oh? Go on."
    roka "When a girl and annother girl love each other very much...{w}\n{i}{b}Sex?{/b}{/i}"
    show a-nana awk2 with dissolve
    nana "Huh."
    show a-roka surp with dissolve
    roka "I-I mean only if you're ok with it."
    show a-roka awk0 with dissolve
    nana "I mean I'm not...{w=0.3} opposed...{w=0.3} exactly..."
    nana "I thought you say you were happy without?"
    show a-roka awk1 with dissolve
    roka "I am.{w=0.3} I...{w=0.3} I guess I just got curious?"
    nana "Well I can't say I've never considered it."
    show a-nana hap1 with dissolve
    nana "Sure, I guess we can try that."
    show a-roka 2casu surp with dissolve
    roka "really."
    show a-roka hap2:
        bounce
        cx
    roka "Thanks Honey!"
    scene b-blackscreen with dissolve
    show a-roka 1casu awk1 with dissolve:
        r2
        ftr
        zoom 0.75
    show a-nana 1work hap1 with dissolve:
        l1
        ftr
        zoom 0.75
    show d-sak-i 3 with dissolve:
        alpha 0.5
        xalign 1.0
        yalign 0.0
    "..."
    roka "Soooo....{w=0.3} how does this work?"
    show a-nana awk2 with dissolve
    nana "You're the one who asked yet you don't know how sex works?"
    show a-roka awk0 with dissolve
    roka "I know how sex {i}normally{/i} works but... {w}how does it work between women?"
label demo_h_spice:  ### Return point for repeating scene
    $ txtbox = 30
    show a-roka awk0 with dissolve:
        r2
        zoom  0.75
    show a-nana hap1 with dissolve:
        l1
        zoom  0.75
    show d-sak-i 3 with dissolve:
        alpha 0.5
        xalign 1.0
        yalign 0.0
    nana "Geez, you're hopeless."
    nana "I'll google it."
    show a-roka 2casu awk1 with dissolve
    "..."
    show a-nana awk2 with dissolve
    nana "Ewww, I'm vetiong that one."
    "..."
    show a-nana hap1 with dissolve
    nana "Hmmm... This could work."
    show a-nana znak hap1 with dissolve
    show d-sak-i c
    show a-roka 1casu awk0:
        bounce
    roka "Kyah!"
    show a-nana awk2 with dissolve
    nana "Did you just..."
    show a-roka 2casu awk1 with dissolve
    "..."
    nana "We share a bed.{w=0.3} You see me naked every day."
    show a-roka:
        ease 0.4 xoffset -20
        ease 0.4 xoffset  20
        ease 0.5 xoffset -20
        ease 0.6 xoffset  20
        ease 0.4 xoffset   0
    roka "Owowowow..."
    show a-nana hap1 with dissolve
    nana "What am I going to do with you..."
    nana "W-well, other than this."
label demo_h_glomp: ###### GLOMP #######
    show a-nana:
        parallel:
            linear 0.3 r2
            ease 0.3 xoffset 400
        parallel:
            ease 0.3 yoffset -400
            ease 0.9 yoffset 1600
        parallel:
            pause 0.3
            rotate_pad False
            rotate 0
            ease 0.6 rotate 60
    show a-roka surp:
        pause 0.15
        parallel:
            ease 0.4 xoffset 500
        parallel:
            ease 0.15 yoffset -100
            pause 0.05
            ease 0.6 yoffset 1600
        parallel:
            pause 0.15
            rotate_pad False
            rotate 0
            ease 0.6 rotate 60
    roka "Kyah!"
    if persistent.sakura == 2: ## Skip Check
        scene b-blackscreen with dissolve
        jump demo_h_after
    image cxdemoh 1:
        ConditionSwitch(
        "persistent.sakura == 0", Image("images/cx-demoh 1h.png"),
        "persistent.sakura == 1", Image("images/cx-demoh 1z.png")
        )
    image cxdemoh 2:
        ConditionSwitch(
        "persistent.sakura == 0", Image("images/cx-demoh 2h.png"),
        "persistent.sakura == 1", Image("images/cx-demoh 1z.png")
        )
    $ txtbox = 30
    roka "AARGH!! F***!"
    nana "S***! Are you ok?!"
    roka "Y-yeah...{w=0.3} I just jammed my arm into my chest."
    nana "let me have a look."
    if persistent.sakura == 2: ## Skip Check
        scene b-blackscreen with dissolve
        jump demo_h_after
    scene cxdemoh 1 with dissolve
    roka "I'm fine I swear!"
    roka "It prolly won't even bruise."
    nana "hmmm..."
    roka "W-what?"
    nana "*Poke*{w=0.2} *Poke*{w=0.2}\n Boobs."
    roka "Kiyaah!"
    nana "You're awfully jumpy today."
    nana "Are you {i}sure{/i} you're up for...{w=0.2} {i}{b}sex?{/b}{/i}"
    roka "y-{w=0.3} n-no..."
    nana "*Sigh*"
    nana "Sweetie you're always like this."
    roka "I thought I'd be fine."
    nana "Here."
    scene cxdemoh 2 with dissolve
    roka "Kyah!"
    nana "There, how's that?"
    nana "Not too much for you is it dear?"
    roka "Y-yeah...{w=0.2} This much is ok."
    "..."
    "......"
label demo_h_after:
    roka "I love you Honey."
    nana "Awww Sweetie. I love you too."
    scene b-blackscreen with dissolve
    #$ txtbox = 64
    show a-roka 2znak awk1:
        c0
        xoffset -49
        yoffset 104
        zoom  0.75
        alpha 0.0
    show a-nana p_hold znak awk2:
        r1
        yoffset 100
        zoom  0.7
        alpha 0.0
    show d-sak-i c with dissolve:
        alpha 0.5
        xalign 1.0
        yalign 0.0
    show a-roka with dissolve:
        alpha 1.0
    show a-nana with dissolve:
        alpha 1.0
    nana "Soooo{w=0.2}, what did we learn"
    show a-roka awk0 with dissolve
    roka "S-sex is a big jump up from ear cleaning?"
    show a-nana hap1 with dissolve
    nana "{i}I dunno, ear cleaning's pretty intimate{/i}"
    show a-roka awk1 with dissolve
    roka "S-still..."
    show a-nana awk2 with dissolve
    "..."
    nana "Hey, lets actually go to bed now."
    show a-roka awk1 with dissolve
    roka "Y-yeah."
    show a-roka hap2 with dissolve
    roka "Can I be little spoon?"
    show a-nana hap1 with dissolve
    nana "Of course dear."
    show a-roka hap0 with dissolve
    roka "I love you"
    nana "I love you too"
    scene b-blackscreen with dissolve
    "{i}Demo H-scene End{/i}"
    menu:
        "Repeat scene with diferent setting?"
        "Yes":
            "Remember to change the setting for a diferent result"
            scene b-blackscreen with dissolve
            jump demo_h_spice
        "No":
            "Ok, that's the end of the Sakura mode demo"
    "{i}End of Experimental section{/i}"
    scene b-blackscreen with dissolve
    pause 1 # "
label end_of_wip:
    "{i}This is the end of the WIP game{/i}"
    "{i}The VN will now return to the main menu{/i}"
    scene b-blackscreen with dissolve
    pause 1 # "
    return
label cut: ######   ######   ######   ######   ######   ######
    scene b-blackscreen with dissolve
    $ txtbox = 23
    "{i}Allong comes an H scene{/i}"
    show d-sak-i c:
        alpha 0.5
        xalign 1.0
        yalign 0.0
    show a-sca laugh at c0 with dissolve
    image nips = Solid("#900000", xysize=(400, 200))
    image naps = Text(_("Nip Naps"), size=80)
    define sdem  = Character("Heroine",color="#804040")
    show nips:
        c0
        ypos 0.65
        alpha 0.0
    show naps:
        c0
        ypos 0.65
        alpha 0.0
    show d-sakura-p c:
        c0
        zoom -0.5
        alpha 0.0
    show nips:
        alpha 1.0
    show naps:
        alpha 1.0
    ""
    show a-sca scared with dissolve
    pause 0.5
    show a-sca awkward with dissolve
    return
##############################
  ##  ##  ##  ##  ##  ####
  ##  ##  ##  ##  ##  ##  ##
  ##  ##  ##  ######  ####
  ##  ##  ##  ##  ##  ##
    ##  ##    ##  ##  ##
##############################