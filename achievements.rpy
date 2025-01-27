define myconfig.INGAME_POPUP_WITH_STEAM = True

define myconfig.ACHIEVEMENT_HIDE_TIME = 1.0


define myconfig.SHOW_ACHIEVEMENT_POPUPS = True

define myconfig.ACHIEVEMENT_SOUND = None 

define myconfig.ACHIEVEMENT_CHANNEL = "audio"



init python:
    achievement.steam_position = None


image locked_achievement = Text("?")









screen achievement_popup(a, tag, num):

    zorder 190

   
    default achievement_yoffset = num*170

    frame:
        style_prefix 'achieve_popup'
        at achievement_popout()
        yoffset achievement_yoffset
        has hbox
        add a.unlocked_image:
            fit "contain" ysize 95 align (0.5, 0.5)
        vbox:
            text a.name
            text a.description size 25

    
    timer 5.0 action [Hide("achievement_popup"),
            Show('finish_animating_achievement', num=num, _tag=tag+"1")]

style achieve_popup_frame:
    is confirm_frame
    align (0.0, 0.0)
style achieve_popup_hbox:
    spacing 10
style achieve_popup_vbox:
    spacing 2



transform achievement_popout():
    on show:
        xpos 0.0 xanchor 1.0
        easein_back 1.0 xpos 0.0 xanchor 0.0
    on hide, replaced:
        easeout_back myconfig.ACHIEVEMENT_HIDE_TIME xpos 0.0 xanchor 1.0


screen achievement_gallery():
    tag menu

    add VBox(Transform("#292835", ysize=110), "#21212db2") # Background

   
    textbutton _("Return") action Return() align (1.0, 1.0)
    viewport:
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        xalign 0.5 yalign 0.5
        xsize int(config.screen_width*0.6) ysize int(config.screen_height*0.7)
        xfill False yfill False
        has vbox
        spacing 20



        for a in Achievement.all_achievements:
            button:
                style_prefix 'achievement'
                if config.developer:
                    action a.Toggle()
                has hbox
                if a.idle_img:
                    fixed:
                        align (0.5, 0.5)
                        xysize (155, 155)
                        add a.idle_img fit "scale-down" ysize 155 align (0.5, 0.5)
                else:
                    null width -10
                vbox:
                    label a.name
                    text a.description
                    if a.has():
                        text a.timestamp size 22
                    elif a.stat_max:
                        fixed:
                            fit_first True
                            bar value a.stat_progress range a.stat_max:
                                style 'achievement_bar'
                            text "[a.stat_progress]/[a.stat_max]":
                                style_suffix "progress_text"


        null height 100


    label __("Достижения: ") + "{earned}/{total}".format(
            earned=Achievement.num_earned(), total=Achievement.num_total()):
        text_size 52 xalign 0.5 text_color "#f93c3e" top_padding 15



style achievement_button:
    size_group 'achievement'
    xmaximum 750
style achievement_label:
    padding (2, 2)
style achievement_label_text:
    size 40 color "#ff8335"
style achievement_hbox:
    spacing 10
style achievement_vbox:
    spacing 2
style achievement_bar:
    xmaximum 600
