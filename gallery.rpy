init python:
    g = Gallery()
    g.transition = dissolve 
screen gallery:
    python:
        g.locked_button_s = "images/s_locked.jpg"
        g.button("s1") #...регистрируем кнопку для первого спрайта. 
        if s.info == 1: #....Создаем условие, если переменная с первым спрайтов имеет значение 1, тогда...
            g.image("images/strateg.jpg") #...тогда по клику на кнопке - переход к изображению...



        g.button("f1") 
        if f.info == 1: 
            g.image("images/fighter.jpg") 

        g.button("p1") 
        if p.info == 1: 
            g.image("images/psyho.jpg") 

    tag menu 


    add "images/black.png"

    textbutton _("Return") action Return() align (1.0, 1.0)


    

    add g.make_button("s1", "images/s_info.jpg", locked="images/s_locked.jpg", xalign=0.1, yalign=0.5)
#Добавляем кнопку "s1"
#указываем изображение, которое будет превьюшкой для данного спрайта
# если же карточка ещё не была открыта, для этого случая указываем изображение, где она закрыта
#Далее, указываем координаты с плавающей точкой для данной кнопки-превью.
#То же проделываем и для остальных превью.

    add g.make_button("f1", "images/f_info.jpg", locked="images/f_locked.jpg", xalign=0.5, yalign=0.5)
    add g.make_button("p1", "images/p_info.jpg", locked="images/p_locked.jpg", xalign=0.9, yalign=0.5)
    


