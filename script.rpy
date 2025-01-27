# Определение персонажей игры. 
define b = Character('Баскетболист', color="#7b2ba3", image='b') 
define p = Character('Психопат', color="#7b0000", image='p') 
define f = Character('Борец', color="#305d27", image='f')
define s = Character('Стратег', color="#3430d5", image='s')
define bro = Character("Брат", color ="#575757")
define girl = Character("Девушка", color ="#603b58", image='girl')
define l = Character("Лайла", color ="#603b58", image='girl')
define sec = Character("Охранник", color ="#649a84", image='sec')
define voice = Character("Голос", color ="#649a84", image='sec')
define zombie = Character("Зомби", color ="#ffffff")

define fastdissolve = Dissolve(.1)
define slowdissolve = Dissolve(2.0)
define deathfade = Fade(0.2, 0.5, 0.3,color="#a70000")
define deadly = Fade()


#ДОСТИЖЕНИЯ

define finale = Achievement(
    name=_("Вы прошли игру."),
    id="hidden_achievement0",
    description=_("Молодцы!"),
    unlocked_image=Transform("images/прогресс.jpg"),
    hidden=True, 
)




define sweapon = Achievement(
    name=_("Получено оружие!"),
    id="hidden_achievement1",
    description=_("Вы получили нож."),
    unlocked_image=Transform("images/ножик.jpeg"),
    hidden=True, 
)
define sindzi = Achievement(
    name=_("Синдзи moment:"),
    id="hidden_achievement2",
    description=_("У вашего брата депрессия."),
    unlocked_image=Transform("images/синдзимомент.jpg"),
    hidden=True, 
)

define shurt = Achievement(
    name=_("Вас ранили!"),
    id="hidden_achievement3",
    description=_("Нога будет заживать долго."),
    unlocked_image=Transform("images/leg.jpg"),
    hidden=True, 
)

define srevenge = Achievement(
    name=_("Око за око:"),
    id="hidden_achievement4",
    description=_("Вы отомстили за брата."),
    unlocked_image=Transform("images/месть.jpg"),
    hidden=True, 
)

define sbitch = Achievement(
    name=_("Вы - мразь!"),
    id="hidden_achievement5",
    description=_("Вы убежали, но логически оправдали свои действия."),
    unlocked_image=Transform("images/мразь.jpg"),
    hidden=True, 
)

define food = Achievement(
    name=_("Главное что мы поели"),
    id="hidden_achievement6",
    description=_("Вы обеспечили себя провизией."),
    unlocked_image=Transform("images/поели.jpg"),
    hidden=True, 
)

define mraz = Achievement(
    name=_("Угрызения совести"),
    id="hidden_achievement7",
    description=_("Вы оставили брата умирать."),
    unlocked_image=Transform("images/mraz.jpeg"),
    hidden=True, 
)

define door = Achievement(
    name=_("OPEN THE DOOR!!!"),
    id="hidden_achievement8",
    unlocked_image=Transform("images/door.jpg"),
    hidden=True, 
)
define fuck = Achievement(
    name=_("Спасибо, дура"),
    id="hidden_achievement9",
    description=_("Вы отвлекли на себя зомби, зато девушка спаслась."),
    unlocked_image=Transform("images/fuck.jpg"),
    hidden=True, 
)
define pohui = Achievement(
    name=_("А мне пофик"),
    id="hidden_achievement10",
    description=_("Вам все равно на судьбу девушки."),
    unlocked_image=Transform("images/pohui.jpg"),
    hidden=True, 
)
define dogovor = Achievement(
    name=_("Я пришел договориться"),
    id="hidden_achievement11",
    description=_("Попробуйте убедить охранника вам поверить."),
    unlocked_image=Transform("images/dogovor.jpg"),
    hidden=True, 
)
define crazy = Achievement(
    name=_("Mental breakdown"),
    id="hidden_achievement12",
    description=_("Вы убили человека!"),
    unlocked_image=Transform("images/crazy.jpg"),
    hidden=True, 
)
define shurttummy = Achievement(
    name=_("Вас ранили!"),
    id="hidden_achievement13",
    description=_("Так вам и надо."),
    unlocked_image=Transform("images/sculp.png"),
    hidden=True, 
)
define who = Achievement(
    name=_("Кто вы?"),
    id="hidden_achievement15",
    description=_("Сами разбирайтесь"),
    unlocked_image=Transform("images/кто.jpg"),
    hidden=True, 
)

define honey = Achievement(
    name=_("Охранник:"),
    id="hidden_achievement16",
    description=_(" "),
    unlocked_image=Transform("images/буся.jpg"),
    hidden=True, 
)

define cool = Achievement(
    name=_("Это мой гриб, я его ем!"),
    id="hidden_achievement17",
    description=_("Это не ваш гриб."),
    unlocked_image=Transform("images/гриб.jpg"),
    hidden=True, 
)

define holiday = Achievement(
    name=_("Каникулы кончились..."),
    id="hidden_achievement18",
    description=_("Эхххх"),
    unlocked_image=Transform("images/каникулы.jpg"),
    hidden=True, 
)

define pupupu = Achievement(
    name=_("А всё, а надо было раньше"),
    id="hidden_achievement19",
    description=_("Накрыло парня"),
    unlocked_image=Transform("images/айсберг.jpg"),
    hidden=True, 
)

define kitty = Achievement(
    name=_("Вы без кота."),
    id="hidden_achievement20",
    description=_("ВЫ ПОНИМАЕТЕ?"),
    unlocked_image=Transform("images/кит.jpg"),
    hidden=True, 
)
define fweapon = Achievement(
    name=_("Получено оружие!"),
    id="hidden_achievement21",
    description=_("Вы нашли биту."),
    unlocked_image=Transform("images/bita.jpg"),
    hidden=True, 
)


define pweapon = Achievement(
    name=_("Получено оружие!"),
    id="hidden_achievement22",
    description=_("Вы получили катаны."),
    unlocked_image=Transform("images/катаны.png"),
    hidden=True, 
)


define phurt = Achievement(
    name=_("Вас ранили!"),
    id="hidden_achievement24",
    description=_("Нога будет заживать долго."),
    unlocked_image=Transform("images/leg.jpg"),
    hidden=True, 
)

define prevenge = Achievement(
    name=_("Око за око:"),
    id="hidden_achievement25",
    description=_("Вы отомстили за брата."),
    unlocked_image=Transform("images/месть.jpg"),
    hidden=True, 
)

define pbitch = Achievement(
    name=_("Вы - мразь!"),
    id="hidden_achievement26",
    description=_("Вы ушли, использовав брата как приманку."),
    unlocked_image=Transform("images/Добавления/disney.jpg"),
    hidden=True, 
)



define pmraz = Achievement(
    name=_("Такого амбала не спрятать!"),
    id="hidden_achievement28",
    description=_("Необдуманный ход стоил вам жизни."),
    unlocked_image=Transform("images/Добавления/ebaluga.jpg"),
    hidden=True, 
)


define seduct = Achievement(
    name=_("Вы втерлись в доверие!"),
    id="hidden_achievement30",
    description=_("Теперь девушка вам верит."),
    unlocked_image=Transform("images/Добавления/seduct.jpg"),
    hidden=True, 
)
define ppohui = Achievement(
    name=_("А мне пофик"),
    id="hidden_achievement31",
    description=_("Вам все равно на судьбу девушки."),
    unlocked_image=Transform("images/Добавления/Бан.jpg"),
    hidden=True, 
)
define hod = Achievement(
    name=_("#Манипулятор #Кукловод"),
    id="hidden_achievement32",
    description=_("Хитрый ход)"),
    unlocked_image=Transform("images/Добавления/hod.jpg"),
    hidden=True, 
)
define pcraz = Achievement(
    name=_("Taste of blood"),
    id="hidden_achievement33",
    description=_("Вы почуствавали свою власть над людскими жизьнями!"),
    unlocked_image=Transform("images/Добавления/texas.jpg"),
    hidden=True, 
)
define phurttummy = Achievement(
    name=_("Вас ранили!"),
    id="hidden_achievement34",
    description=_("Можно было и поговорить..."),
    unlocked_image=Transform("images/Добавления/sigma.jpg"),
    hidden=True, 
)













init:
    #ЗДОРОВЬЕ (повреждения)
    $ shealth = 0   
    $ phealth = 0
    $ fheakth = 0

    $ skill = 0



    #СОВЕСТЬ 
    $ fmental = 0
    $ smental = 0
    $ pmental = 0

    #Взял еду?
    $ ffood = 0
    $ sfood = 0
    $ pfood = 0

    $ s.info = 0
    $ f.info = 0
    $ p.info = 0


    # Психопат

    $ pcrazy=0
    $ palone=0
    $ pmanip=0
    $ pkill=0
    $ pslaughter=0
    




label splashscreen:
    scene hots with dissolve
    pause 2.0
    scene black with dissolve
    pause 1.0
    show text 'Команда "HOTS" представляет'
    pause 2.0
    show text '"Сдохни или умри"'
    pause 2 
    scene black with dissolve
    pause 1.0
    return




init -2:
    image vid = Movie(play = "images/vid.mpg", size = (1920,1080))

label main_menu:
    scene vid 
    jump main_menu_screen




# Игра начинается здесь:
label start:


    scene black


    centered 'Нажмите и сделайте свой первый выбор.'
    
    $ result = renpy.imagemap("квадраты 1.png", "квадраты 2.png", [
    (352, 390, 664, 697, "blue1"),
    (804, 383, 1113, 691, "red1"),
    (1261, 391, 1568, 696, "green1"),
    ], focus="imagemap")
   
    if result == "blue1":
        jump blue
    elif result == "red1":
        jump red 
    elif result == "green1":
        jump green

    

    label blue:
        $ s.info = 1

        scene black 
        show s with dissolve
        "Вы выбрали Cтратега."
        hide s
        show s power at truecenter with dissolve
        'Ваш персонаж обладает уникальной способностью - "Анализ Будущего".' 
        "Этот навык дает возможность быстро проанализировать ситуацию и сделать правильный выбор."
        hide s power
        "Больше о персонаже Вы можете узнать в галерее." #дополнить место где карточка 
        "Помните, что прохождение игры напрямую зависит от выбранного Вами персонажа."
        "Делайте выборы, исходя из его характеристик и оружия."
        "Наслаждайтесь игрой..."
        "{i}...И пусть удача всегда будет с Вами!{\i}"
        "P.S. Не забывайте сохраняться :)"

        stop music fadeout 2.0
        play music "audio/normal.mp3" fadein 1
        scene гостиная with slowdissolve
        "На улице уже стемнело. В этот поздний час в комнате царила тишина, нарушаемая лишь редким шорохом страниц."
        "Слабый свет настольной лампы создавал ощущение покоя."
        "Девушка внезапно решила прервать тишину, отложив книгу в сторону."
        show s at left with fastdissolve
        s "Напомни, когда там пицца приедет?"
        bro "..."
        s e "Прием?"
        bro "..."
        s an "415 БАЗА ОТВЕТЬТЕ!!!"
        show bro surprised at right with fastdissolve 
        bro"А??!"
        show bro shock 
        "Парень соизволил поднять взгляд и вопросительно посмотрел на сестру."
        s e"Сколько можно торчать в телефоне?"
        show bro angry
        show s
        s "Ты прямо типичный представитель зомбированного поколения."
        s "Унылый тинэйджер, который дальше своего телефона ничего не видит - это про тебя."
        show bro sm
        bro "Ты такая милая сегодня."
        "Очевидный сарказм в его голосе не поспособствовал разрешению ситуации."
        s an "А ты отвечай, когда тебе вопрос задают, и—"  
        play sound "audio/knocking.mp3"
        show s
        show bro norm
        "Их спор прервал стук в дверь."
        show bro sm2
        show s sm
        bro "А вот и пицца!"
        scene гостиная with fastdissolve
        "В срочном порядке брат с сестрой поспешили к входной двери."

        scene дверь with dissolve 
        "Младший брат взялся за дверную ручку.."
        "...Лучше бы он этого не делал."
        play sound "audio/skrip.mp3"
        scene дверь открыта  with slowdissolve
        "Открыв дверь, он увидел вовсе не курьера."
        show bro shock at right with fastdissolve 
        "На лице брата сперва появился шок."
        stop music fadeout 2.0
        show bro horrified
        "Затем его захватил непередаваемый ужас."
        play sound "audio/scream.mp3"
        bro "АААААААА!!!!!"
        play sound "audio/hand.mp3"
        scene дверь рука 
        "В полумраке резко возникла чья-то рука."
        play music "audio/tiktok.mp3" fadein 1
        "Парень едва успел отступить. Еще секунда - и полусгнившие пальцы сжались бы на его шее."
        show s at left with fastdissolve
        s "..."
        s an "Какого хре—"
        "Не успела она закончить мысль, как из дверного проема показалось...нечто."
        scene дверь открыта with fade
        window hide
        play sound "audio/zombie.mp3"
        show зомби 1 with fastdissolve
        pause 2.0
        window show
        "Нечеловеческий крик был оглушительным."
        "Существо, появившееся в коридоре, заставило сердце девушки пропустить удар."
        "Никогда она не видела ничего подобного."
        hide зомби 1
        show bro horrified 
        "Вдруг, младший брат резко потянул ее за руку."
        bro "БЕЖИМ!"
        scene black with fastdissolve
        "Едва не вывернув запястье девушки, брат помчался к ближайшей двери, ведущей в подвал."
        "Влетев туда, чудом не свалившись с лестницы, они одновременно захлопнули дверь."
        "Стратег задвинула щеколду, несмотря на нещадно дрожащие руки."
        "Быстрые шаги монстра раздались совсем рядом. Времени на раздумья не было."
        "На одном дыхании миновав лестничный пролет, брат с сестрой ошалело посмотрели друг на друга."
        scene подвал with fade
        show s hor at left with fastdissolve
        s "Это что...зомби..?"
        "Последнее слово она произнесла неверящим полушепотом."
        show bro cry at right with fastdissolve
        bro "...Никак по другому..эту тварь.....не назвать.."
        s "..."
        show bro dead
        bro "Какого хрена вообще?!"
        scene подвал with fade
        show синдзи at truecenter with dissolve
        play sound "audio/уведа.mp3"
        $ sindzi.grant()

        "Упав на стул и согнувшись в три погибели, парень завыл."
        hide синдзи with dissolve
        "Он был на грани истерики."
        "Но сейчас было не до нее."
        '"Тварь" была уже близко.'
        "Зомби от людей разделяла лишь запертая на ненадежную щеколду дверь."
    
        scene black 
        show s power at truecenter with fade #Анализ будущего

        scene подвал with fade
        show s an with fastdissolve
        s "(Рано или поздно оно прорвется.)"
        s "(Атас. Мы в подвале, убежать не получится.)"
        s "(Спрятаться негде, да и вряд-ли это сработает против зомби.)"
        s "(Драться с ним не хочется, но делать больше нечего.)"
        s "(Нужно найти средства самозащиты.)"
        show s 
        s "Слушай, надо поискать, чем можно защититься."
        bro "..."
        s e "Соберись, сейчас нет на это времени!"
        bro "..."
        s an "Если ты сейчас же не возмешь себя в руки, мы тут подохнем."
        "Брат не сдвинулся с места."
        show s
        s "(От него сейчас нет толку. Психика не выдерживает.)"
        scene подвал with fastdissolve
        "Не тратя больше времени, Стратег ринулась к настенной полке."
        "В доме они оружия не держали, но все-таки ее глаз кое-что зацепило."
        window hide
        scene black with fade
        show нож at truecenter with dissolve
        pause 2.0
        hide нож with dissolve
        window show
        "За неимением лучшей альтернативы, девушка взяла нож."
        play sound "audio/уведа.mp3"
        $ sweapon.grant()
        #ачивка, звуковой сигнал
        scene подвал with fade
        "С момента встречи с зомби прошло менее минуты."
        "Дверь вышибло."
        "Сестра и брат испуганно подняли головы."
        "Зомби на огромной скорости падал вниз по лестнице - логичное следствие интенсивного проникновения в подвал."
        "Оживший мертвец приземлился в нескольких метрах от брата."
        "Обычный человек после подобных финтов свернул бы шею. Но перед ними был не человек."
        "Зомби накинулся на парня."
        "Тот даже пискнуть не успел."
        show s w hor with fastdissolve
        s "..."
        s w cry "Брат..!"
        scene подвал with deathfade
        "На его животе появлялись рваные раны."
        "Душераздирающие вопли заполнили помещение."
        "Пока зомби вгрызался в плоть ее брата, Стратег лихорадочно искала пути отступления."
        "На ее глазах монстр убивал члена ее семьи."
        show s w cry with fastdissolve
        s "(Я следующая.)"
        s "..."
        s "(Я не могу умереть вот так!)"
        scene black 
        show s power at truecenter with fade #Анализ будущего

        scene подвал with fade
        show s w hor with fastdissolve
        s w hor "(Нужно подумать, как выбраться из этой ситуации.)"
        s w hor "(Я могла бы попробовать обогнуть зомби и сбежать, пока он занят братом..)"
        s w an "(Ему уже не помочь.)"
        scene bro death with dissolve
        window hide
        pause 2.0
        window show
        "Юноша уже не кричал."
        "Редкие всхипы указывали на то, что конец близок."
        "Сознание покидало его."
        "Так он и умрет. На холодном полу. С выпотрошенным животом."
        "Не так парень представлял сегодняшний вечер..."
        scene подвал with fade
        show s w hor with fastdissolve
        s w hor "..."
        s w hor "........."
        s w hor "(Брат, может мне стоит убить зомби?)"
        s w cry "(То, что он сделал с тобой - ужасно. Не могу же я оставить тебя..?)"
        s w hor "(Или могу?)"
        window hide
        hide s with fade
        window hide
        menu:
            "Убить зомби":
                jump kill_s_1
            
            "Обездвижить зомби":
                jump stop_s
            
            "Убежать":
                jump run_away_s_1

            "Попробовть спрятаться":
                jump hide_s
        window show

        label kill_s_1:
            scene подвал with fade
            show зомби 1 
            zombie "Кхаааа!!!"
            "Зомби самозабвенно отрывал куски плоти от едва живого юноши."
            "Непохоже, что он торопился: парень еще дышал, оставаясь на краю сознания."
            "Более того, мерзкий нелюдь в своем безудержном порыве даже не заметил девушку."

            "Стратег крепче ухватила нож и подкралась к спине мертвеца."
            hide зомби 1
            show s with fastdissolve
            s w an "КОНЕЦ ТЕБЕ, ТВАРЬ!"
            "Размашистым ударом она хотела вонзить нож в голову зомби."
            "Интуитивно понимала, что это его слабое место."
            'Но в решающий момент "тварь" внезапно обернулась. Нож резанул по шее.'
            play sound "audio/рык.mp3"
            zombie "АААРГХ!"
            "Зомби взревел. Некоторые связки были повреждены, и макушка на одну четверть перестала быть частью его тела."
            "Со свисающей головой, он, начиная заваливаться на бок, все же смог поранить девушку."
            show s w hor with deathfade
            s w hor "АЙ!"
            "Острая боль прошила все тело."
            play sound "audio/уведа.mp3"
            $ shurt.grant()
            "Крючковатые когти порезали икроножную мышцу."
            $ skill +=1 #убила зомби
            "Сквозь проступившие слезы Стратег посмотрела вниз."
            "Взгляд сначала прошелся по раненой ноге, затем скользнул по полудохлому зомби, чтобы в конце-концов остановиться на брате."
            "Он был мертв."
            s w cry "..."
            stop music fadeout 2.0
            scene black with fade
            play music "audio/killbill.mp3"
            "Гнев притупил боль. Волна ярости обожгла нутро."
            "Девушка остервенело наносила удары зомби."
            "Выброс адреналина, глубокая ненависть, боль от потери брата - все это вылилось в непрекращающиеся удары."
            "Черная кровь, которой было поразительно много для трупа, разлеталась во все стороны."
            "Даже когда хрипы зомбака стихли, сестра продолжала месть за брата."
            window hide
            pause(2.0)
            scene подвал with fade
            window show
            stop music fadeout 2.0
            play music "audio/normal2.mp3"
            play sound "audio/уведа.mp3"
            $ srevenge.grant()
            "{i}Какое-то время спустя{\i}"
            show s w bl with fastdissolve
            s "Пора отсюда выбираться."
            "В последний раз взглянув на брата, она, похрамывая, направилась наверх."

            
            jump saved_s_1


        label stop_s:
            scene подвал with fade
            show зомби 1 
            zombie "Кхаааа!!!"
            "Зомби самозабвенно отрывал куски плоти от едва живого юноши."
            "Непохоже, что он торопился: парень еще дышал, оставаясь на краю сознания."
            "Более того, мерзкий нелюдь в своем безудержном порыве даже не заметил девушку."

            "Смотреть, как мучается юноша было невыносимо."
            "Она должна что-то сделать."
            hide зомби 1
            show s w hor with fastdissolve
            s "(Я должна как-то ему помочь.)"
            s w an "(Что я смогу сделать зомби с кухонным ножом?..)"
            s w hor "(В физической силе я проигрываю.)"
            s "(Может, убить я его не смогу, но, могу попробовать обездвижить.)"
            s w an "(Достаточно будет перерезать сухожилия...)"
            scene black with fade
            "Дрожь в руках усилилась."
            "Но желание жить превосходило страх."
            "Девушка старалась как можно тише подкрасться к живому мертвецу."
            "То ли она была недостаточно осторожна, то ли он почувствовал ее страх..."
            "Зомби резко обернулся и атаковал."
            "Девушка умерла мгновенно."

            

            jump dead_end



        label run_away_s_1:
            scene подвал with fade
            show зомби 1 
            zombie "Кхаааа!!!"
            "Зомби самозабвенно отрывал куски плоти от едва живого юноши."
            "Непохоже, что он торопился: парень еще дышал, оставаясь на краю сознания."
            "Более того, мерзкий нелюдь в своем безудержном порыве даже не заметил девушку."

            "Это был шанс."
            hide зомби 1
            show s w with fastdissolve
            s "(Извини меня.)"
            s "(Я не смогу тебя спасти, поэтому мне нет смысла здесь оставаться.)"
            s "(Я тоже хочу жить.)"
            scene black with fade
            "Мысленно объяснившись с братом, Стратег в последний раз посмотрела на него."
            "Болезненный стон, совсем тихий. Жизнь покидала его."
            "Боясь встретиться с ним глазами, девушка поспешно отвернулась."
            "Зомбак по-прежнему не обращал на нее внимания, продолжая мучать юношу."
            "Делал он это нарочно или нет - не ее дело."
            "Ее дело - спастись самой."
            "Аккуратно и тихо девушка пробралась к лестничному пролету."
            "По ступеням она поднималась не останавливаясь."

            play sound "audio/уведа.mp3"
            $ sbitch.grant()


            jump saved_s_1


        label hide_s:
            scene подвал with fade
            show зомби 1 
            zombie "Кхаааа!!!"
            "Зомби самозабвенно отрывал куски плоти от едва живого юноши."
            "Непохоже, что он торопился: парень еще дышал, оставаясь на краю сознания."
            "Более того, мерзкий нелюдь в своем безудержном порыве даже не заметил девушку."

            "Но это не значит, что он не заметит ее позже."

            hide зомби 1
            show s w hor with fastdissolve
            s "(Боже...)"
            s w cry "(Как же страшно!)"
            "Истошные вопли брата становились все тише. Теперь только болезненные всхлипы эхом проносились по сырому подвалу."
            s w cry "..."
            s "(Я не хочу так страдать.)"
            scene black with fade
            "Ноги отказывались ее слушаться."
            "Она не грезила о побеге - ноги ее не держат."
            "И мысли о схватке с зомби отмела сразу. Чем ей поможет жалкий кухонный нож?"
            "Значит - надо спрятаться. Затаиться."
            "Девушка еще раз просканировала комнату."
            "..."
            "Ничего."
            "Ей негде спрятаться."
            "..."
            "....."
            "........."
            "Через какое-то время зомби заметил ее."
            "В подвале стало на один хладный труп больше."

            jump dead_end









        label saved_s_1:
            if skill == 1:
                jump after_1_bl
        
            else:
                jump after_1
        return

        

        label after_1_bl:
            scene дверь открыта with fade
            show s w bl with fastdissolve
            s w bl "(Времени на рефлексию нет.)"
            s w bl an "(Надо поскорее уходить отсюда.)"
            s w bl an "(В любой момент могут появиться еще зомби.)"
            show s w bl e
            play sound "audio/желудок.mp3"
            "В животе заурчало."
            s w bl an "(Пора бы отсюда сваливать, но, может, я успею взять немного еды?)"
            s w bl hor "(...Хотя другие зомби могут ворваться в любой момент..)"
            hide s with fade
            window hide
            menu:
                "Взять еды":
                    jump bl_with_food
                
                "Побыстрее уйти":
                    jump bl_no_food
            window show

        label bl_with_food:
            $ sfood += 1
            scene кухня with fade
            "Лунный свет пробивался через окно."
            "Была уже глубокая ночь."
            show s w bl with fastdissolve
            s "(Возьму только самое необходимое.)"
            hide s with fastdissolve
            "Быстро скидав в сумку какие-то консервы, снэки и бутылку воды, Стратег поспешила к выходу."
            play sound "audio/уведа.mp3"
            $ food.grant()
            "..."
            "А куда пойдем?"
            window hide


            menu:
                "Выйти через парадную дверь":
                    jump bl_front_door
                
                "Выйти через заднюю дверь":
                    jump bl_back_door
            window show


        label bl_no_food:
            $ sfood = 0
            show s w bl an with fastdissolve
            s "(Организму придется потерпеть.)"
            s w bl "(Эти твари могут нагрянуть в любой момент.)"
            s w bl "(Выйти через эту дверь или пойти через черный ход..?)"
            hide s with fastdissolve

            window hide


            menu:
                "Выйти через парадную дверь":
                    jump bl_front_door
                
                "Выйти через заднюю дверь":
                    jump bl_back_door
            window show



        label bl_front_door:
            scene дверь открыта with fade
            show s w bl with fastdissolve
            "Похрамывая, она уже почти добралась до двери."
            show s w bl hor
            "Как вдруг..."
            scene дверь открыта
            play sound "audio/zombie.mp3"
            show зомби мэн with deathfade
            zombie "ХАГГХААГХ!!!!!"
            scene black with fade
            "Зомби быстро расправился с девушкой."
            jump dead_end
            


        label bl_back_door:
            scene черный ход with fade
            show s w bl with fastdissolve
            s "Дома теперь небезопасно."
            s w bl an "Нужно найти надежное место."
            scene black with fade
            "Стратег покинула дом. Больше она сюда не вернется."
            jump bl_street
            

            












        label after_1:
            stop music fadeout 2.0
            scene дверь открыта with fade
            play music "audio/normal2.mp3"
            show s w with fastdissolve
            s w "(Времени на рефлексию нет.)"
            s w an "(Надо поскорее уходить отсюда.)"
            s w an "(В любой момент могут появиться еще зомби.)"
            show s w e
            play sound "audio/желудок.mp3"
            "В животе заурчало."
            s w an "(Пора бы отсюда сваливать, но, может, я успею взять немного еды?)"
            s w hor "(...Хотя другие зомби могут ворваться в любой момент..)"
            hide s with fade
            window hide
            menu:
                "Взять еды":
                    jump with_food
                
                "Побыстрее уйти":
                    jump no_food
            window show

        label with_food:
            $ sfood += 1
            scene кухня with fade
            "Лунный свет пробивался через окно."
            "Была уже глубокая ночь."
            show s w with fastdissolve
            s "(Возьму только самое необхожимое.)"
            hide s with fastdissolve
            "Быстро скидав в сумку какие-то консервы, снэки и бутылку воды, Стратег поспешила к выходу."
            play sound "audio/уведа.mp3"
            $ food.grant()
            "..."
            "А куда пойдем?"
            window hide


            menu:
                "Выйти через парадную дверь":
                    jump front_door
                
                "Выйти через заднюю дверь":
                    jump back_door
            window show



        label front_door:
            scene дверь открыта with fade
            show s w with fastdissolve
            "Она уже почти добралась до двери."
            show s w hor
            "Как вдруг..."
            scene дверь открыта
            play sound "audio/zombie.mp3"
            show зомби мэн with deathfade
            zombie "ХАГГХААГХ!!!!!"
            scene black with fade
            "Зомби быстро расправился с девушкой."
            jump dead_end
            


        label back_door:
            scene черный ход with fade
            show s w with fastdissolve
            s "Здесь небезопасно."
            s w an "Нужно найти надежное место."
            scene black with fade
            "Стратег покинула дом. Больше она сюда не вернется."
            jump street
            

            






        label no_food:
            show s w an with fastdissolve
            s "(Организму придется потерпеть.)"
            s w "(Эти твари могут нагрянуть в любой момент.)"
            s w "(Выйти через эту дверь или пойти через черный ход..?)"
            hide s with fastdissolve

            window hide


            menu:
                "Выйти через парадную дверь":
                    jump front_door
                
                "Выйти через заднюю дверь":
                    jump back_door
            window show



        label street:
            stop music fadeout 2.0
            scene street with fade
            play music "audio/piano.mp3"
            show s w with fastdissolve
            s w "(Так, я на улице.)"
            s w an "(Зомби поблизости не видать.)"
            s w "(Куда теперь идти интересно...)"
            show s w e
            play sound "audio/shout.mp3"
            "Вдруг послышался истошный крик."
            "Стратег повернулась к источнику шума."
            "Из-за угла доносились отчаянные женские вопли."
            s w hor "(Боже, что такое?!)"
            scene street with fastdissolve
            "Девушка тихонько двинулась дальше."
            scene tree with fade
            "За углом показалась аллея."
            "На одном из деревьев девушка спасалась от зомби. Она вскорабкалась на дерево, а зомби нетерпелось ее достать."
            show girl with fastdissolve
            girl cry "На помощь!!!"
            girl cry "Пожалуйста...помогите мне!....Кто-нибудь..?!"
            hide girl
            show zombie
            play sound "audio/рык.mp3"
            zombie "ХАААРГХ!"
            hide zombie
            show girl shock 
            girl shock "..."
            scene black 
            show s power at truecenter with fade #Анализ будущего

            scene tree with fade
            show s w with fastdissolve
            s w hor "(Помочь ей?)"
            s w hor "(Она умрет, если я ничего не сделаю.)"
            s w "(Логично было бы проигнорировать их. Спасаться самой.)"
            s w hor "(Но...Совесть взывает помочь девушке.)"
            s w "(Хотя, какая к черту совесть? Брату то я не помогла...)"
            play sound "audio/уведа.mp3"
            $ mraz.grant()
            s w "(Возможно, это шанс? На искупление..?)"



            hide s with fastdissolve

            window hide


            menu:
                "Отвлечь зомби":
                    jump distract
                
                "Убить зомби":
                    jump slaughter
                "Пройти мимо":
                    jump mimo
            window show


        
        label distract:
            if sfood == 1:
                jump distract_suc
            else:
                jump distract_fail
        return



        label distract_suc:                    
            scene tree with fade
            show s w 
            s w "(Можно попытаться отвлечь зомби... Но как?)"
            s w "(В прошлый раз тот почти не обратил на меня внимания.)"
            s w an "(Кажется, я взяла консервы из дома.)"
            s w sm "(Кину их подальше, авось он заинтересуется.)"
            s w an "..."
            s w an "(Я сейчас сильно рискую. Могу и умереть.)"
            s w ":("
            s w sm"(Ладно, я уже решила! ТОЛЬКО ВПЕРЕД!!!)"
            hide s with fastdissolve
            "Не давая себе шанса передумать, Стратег стремительно открыла консерву и с размаху бросила."
            play sound "audio/conserva.mp3"
            "Баночка с громким лязгом упала на приличном расстоянии от дерева."
            "....."
            scene tree1 with fade
            "Успех! Зомбак рванул на звук, оставляя девушку в покое."
            show girl with fastdissolve
            girl shock "А?"
            hide girl
            "Устремив взгляд в сторону, откуда прилетела банка, девушка увидела свою спасительницу."
            show s w
            s w hor "{i}БЕГИ СЮДА!{\i}"
            hide s 
            show girl sm2
            girl shock "!"
            hide girl
            "Девушка поспешила слезть с дерева и побежала к блондинке."

            scene street with fade

            show s w with fastdissolve
            s w "Ты в порядке?"
            hide s w 
            show girl with fastdissolve
            girl "...Да."
            girl sm "Спасибо тебе. Я думала, это конец."
            girl sm "Меня зовут Лайла."
            l "..."
            show girl
            l "У тебя есть план? Что нам теперь делать?"
            hide girl
            show s w with fastdissolve
            s w "Нужно найти укрытие. И побыстрее."
            s w e "Ты знаешь какое-нибудь безопасное место неподалеку?"
            s w an "Такое, чтоб зомби не прорвались."
            hide s
            show girl
            l "Если так подумать... Дальше по улице есть банк."
            l sm "Двери там надежные, с приличным замком."
            hide girl
            show s w 
            s w sm "Точно! Там и охрана должна быть."
            s w "Остается надеяться, что зомби нет внутри."

            scene black with fade

            "Девушки поспешили в сторону банка. На их счастье, зомби они не встретили." 
            "Когда они подошли к зданию, то обнаружили, что дверь заперта."
            "..."
            l "Блин, закрыто."
            s "Это же банк. Там должен быть охранник на смене, правильно?"
            "Девушки начали долбиться в дверь."
            play sound "audio/уведа.mp3"
            $ door.grant()
            "..."
            "Тишина."
            "Затем они обнаружили кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            l "Пожалуйста, помогите нам!"
            voice "..."
            voice "Что у вас случилось?"
            s "Нет времени объяснять! Сначала впустите нас."
            l "Мне кажется, они уже близко!!!"
            voice "Девушки, спокойно. Объясните, что случилось."
            l "ОТКРОЙТЕ ДВЕРЬ!"
            "Послышался усталый вздох. Затем прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."
            
            jump s_bank_with_girl



        label distract_fail:
            scene tree with fade
            show s w 
            s w "(Можно попытаться отвлечь зомби... Но как?)"
            s w "(В прошлый раз тот почти не обратил на меня внимания.)"
            s w "(Так...Ну вот камень лежит.)"
            s w sm "(Брошу его, может зомби с девушки на него переключится.)"
            s w an "..."
            s w an "(Я сейчас сильно рискую. Могу и умереть.)"
            s w ":("
            s w sm"(Ладно, я уже решила! ТОЛЬКО ВПЕРЕД!!!)"
            hide s with fastdissolve
            "Не давая себе шанса передумать, Стратег со всей силы бросила камень."
            play sound "audio/rock.mp3"
            "Камень упал на приличном расстоянии от дерева."
            "....."
            "Зомби он, по-видимому, не заинтересовал."
            show s w with fastdissolve
            s w an "Черт!"
            hide s
            "Девушка с дерева увидела Стратега."
            show girl shock with fastdissolve
            girl shock "ЭЭЭЙ!!! ПОМОГИ МНЕ!!!"
            girl cry "Ну что ты стоишь там?! Сделай что-нибудь! Пожалуйста.."
            hide girl 
            show s w 
            s w an "(Заткнись, дура! Он меня сейчас заметит!)"
            hide s
            "Стоило ей об этом подумать, как зомби обернулся."
            "Видя в Стратеге более легкую добычу, мертвец бросился в ее сторону."
            "Девушка на дереве, в свою очередь, поспешила слезть и рванула в противоположном направлении."
            scene black with fade
            s "БЛ#@$!!!!!"
            "Она бежала быстро, но зомби был быстрее."
            "Знала бы Стратег, чем ей обернется ее альтруизм - ни за что не помогла бы той девушке."
            "Но вот она - тщетно бежит от своей смерти."
            s "(Зато хоть та истеричка выжила...)"
            play sound "audio/уведа.mp3"
            $ fuck.grant()
            "В конце-концов, зомби все-таки добрался до блондинки."







            jump dead_end







        label slaughter:
            scene tree with fade
            show s w with fastdissolve
            s w hor"(Не могу я оставить ее так!)"
            s w an "(Да, брата я бросила! А ее не брошу!!)"
            s w an "(Я буду совсем бессовестной, если опять пройду мимо.)"
            s w an "(Просто убью зомби, и дело с концом.)"
            s w "(Должен же этот нож хоть какую-то пользу принести.)"
            scene tree with fastdissolve
            "Стретег покрепче ухватила оружие и вышла из-за укрытия."
            "Она тихо подкрадывалась к мертвецу. Точный удар в голову - вот и все."
            "До несчастного дерева осталось 10 метров."
            show girl shock with fastdissolve
            girl cry "Помоги..."
            hide girl
            show s w e
            s w an "(Молчи! Он заметит!)"
            s w an "БЛ#@$!"
            scene black with fade
            "Мысли материальны."
            "Зомби молниеносно обернулся и атаковал Стратега."
            "Та даже не успела нож поднять."

            jump dead_end




        label mimo:
            scene tree with fade 
            show s w with fastdissolve
            s w sm"(Ну какое н@хуй искупление?)"
            s w e "(Я даже брата оставила умирать - зачем мне рисковать жизнью из-за какой то чуни?)"
            s w e "(Про совесть и стыд уже нечего думать - на дворе зомби апокалипсис.)"
            s w "(Что в прошлый раз, что сейчас.. Я логически оправдываю свои действия. Такой я человек.)"
            play sound "audio/уведа.mp3"
            $ pohui.grant()
            "Стратег равнодушно отвернулась."
            scene street with fade
            show s w with fastdissolve
            s w "(Надо решить, что делать дальше.)"
            s w "(Приоритетная задача - найти укрытие.)"
            s w an "(Пока мне везло, и зомби на улице почти не было.)"
            s w an "(Но это не значит, что я в безопасности.)"
            s w "(Не хочу повторить судьбу той девушки на дереве.)"
            s w "(...Итак. Куда идти?)"
            s w "(Нужно безопасное место недалеко отсюда.)"
            s w an "(Чтоб ни один чертов зомби не проник внутрь.)"
            s w "(Желательно, с запасами еды и воды.)"
            s w "..."
            s w "(Думай, думай, думай..)"
            s w sm "О!"
            s w sm "(Тут же есть банк совсем рядом! С надежной металлической дверью.)"
            s w "(Туда и пойду. Все равно не вижу вариантов получше.)"
            scene black with fade
            "Девушка довольно быстро прибежала к зданию банка."
            "Дернула за ручку. Заперто."
            s "(Бл$! Конечно заперто, ночь на дворе.)"
            s "(Хотя, это же банк. Там должен быть охранник на смене.)"
            "Девушка начала долбиться в дверь."
            play sound "audio/уведа.mp3"
            $ door.grant()
            "..."
            "Тишина."
            "Затем она обнаружила кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            s "Пожалуйста, помогите!"
            voice "..."
            voice "Что у вас случилось?"
            s "Нет времени объяснять! Сначала впустите меня!"
            voice "Девушка, спокойно. Объясните, что случилось."
            s "ПРОСТО ОТКРОЙТЕ ДВЕРЬ!"
            "Послышался усталый вздох. Затем прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."
            
            jump s_bank















        label bl_street:
            stop music fadeout 2.0
            scene street with fade
            play music "audio/piano.mp3"
            show s w bl with fastdissolve
            s w bl"(Так, я на улице.)"
            s w bl an "(Зомби поблизости не видать.)"
            s w bl"(Куда теперь идти, интересно...)"
            show s w e bl
            play sound "audio/shout.mp3"
            "Вдруг, послышался истошный крик."
            "Стратег повернулась к источнику шума."
            "Из-за угла доносились отчаянные женские вопли."
            s w bl hor "(Боже, что такое?!)"
            scene street with fastdissolve
            "Девушка тихонько двинулась дальше."
            scene tree with fade
            "За углом показалась аллея."
            "На одном из деревьев девушка спасалась от зомби. Она вскорабкалась на дерево, а зомби нетерпелось ее достать."
            show girl with fastdissolve
            girl cry "На помощь!!!"
            girl cry "Пожалуйста...помогите мне!....Кто-нибудь..?!"
            hide girl
            show zombie
            play sound "audio/рык.mp3"
            zombie "ХАААРГХ!"
            hide zombie
            show girl shock 
            girl shock "..."
            scene black 
            show s power at truecenter with fade #Анализ будущего

            scene tree with fade
            show s w bl with fastdissolve
            s w bl hor "(Помочь ей?)"
            s w bl hor "(Она умрет, если я ничего не сделаю.)"
            s w bl "(Логично было бы проигнорировать их. Спасаться самой.)"
            s w bl hor "(Но...Совесть взывает помочь девушке.)"


            hide s with fastdissolve

            window hide


            menu:
                "Отвлечь зомби":
                    jump bl_distract
                
                "Убить зомби":
                    jump bl_slaughter
                "Пройти мимо":
                    jump bl_mimo
            window show


        
        label bl_distract:
            if sfood == 1:
                jump bl_distract_suc
            else:
                jump bl_distract_fail



        label bl_distract_suc:                    
            scene tree with fade
            show s w bl
            s w bl"(Можно попытаться отвлечь зомби... Но как?)"
            s w bl"(В прошлый раз тот почти не обратил на меня внимания.)"
            s w bl an "(Кажется, я взяла консервы из дома.)"
            s w bl sm "(Кину их подальше, авось он заинтересуется.)"
            s w bl an "..."
            s w bl an "(Я сейчас сильно рискую. Могу и умереть.)"
            s w bl":("
            s w bl sm"(Ладно, я уже решила! ТОЛЬКО ВПЕРЕД!!!)"
            hide s with fastdissolve
            "Не давая себе шанса передумать, Стратег стремительно открыла консерву и с размаху бросила."
            play sound "audio/conserva.mp3"
            "Баночка с громким лязгом упала на приличном расстоянии от дерева."
            "....."
            scene tree1 with fade
            "Успех! Зомбак рванул на звук, оставляя девушку в покое."
            show girl with fastdissolve
            girl shock "А?"
            hide girl
            "Устремив взгляд в сторону, откуда прилетела банка, девушка увидела свою спасительницу."
            show s w bl
            s w bl hor "{i}БЕГИ СЮДА!{\i}"
            hide s 
            show girl sm2
            girl shock "!"
            hide girl
            "Девушка поспешила слезть с дерева и побежала к блондинке."

            scene street with fade

            show s w bl with fastdissolve
            s w bl "Ты в порядке?"
            hide s w 
            show girl with fastdissolve
            girl "...Да."
            girl sm "Спасибо тебе. Я думала, это конец."
            girl sm "Меня зовут Лайла."
            l "..."
            show girl
            l "У тебя есть план? Что нам теперь делать?"
            hide girl
            show s w bl with fastdissolve
            s w bl "Нужно найти укрытие. И побыстрее."
            s w bl e "Ты знаешь какое-нибудь безопасное место неподалеку?"
            s w bl an "Такое, чтоб зомби не прорвались."
            hide s
            show girl
            l "Если так подумать... Дальше по улице есть банк."
            l sm "Двери там надежные, с приличным замком."
            hide girl
            show s w bl
            s w bl sm "Точно! Там и охрана должна быть."
            s w bl "Остается надеяться, что зомби нет внутри."

            scene black with fade

            "Девушки направились в сторону банка."
            "Стратег сильно хромала на одну ногу, так что двигались они непозволительно медленно."
            "На их счастье, зомби им не встретились." 
            "Когда они подошли к зданию, то обнаружили, что дверь заперта."
            "..."
            l "Блин, закрыто."
            s "Это же банк. Там должен быть охранник на смене, правильно?"
            "Девушки начали долбиться в дверь."
            play sound "audio/уведа.mp3"
            $ door.grant()
            "..."
            "Тишина."
            "Затем они обнаружили кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            l "Пожалуйста, помогите нам!"
            voice "..."
            voice "Что у вас случилось?"
            s "Нет времени объяснять! Сначала впустите нас."
            l "Мне кажется, они уже близко!!!"
            voice "Девушки, спокойно. Объясните, что случилось."
            l "ОТКРОЙТЕ ДВЕРЬ!"
            "Послышался усталый вздох. Затем прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."
            
            jump s_bl_bank_with_girl





        label bl_distract_fail:
            scene tree with fade
            show s w bl
            s w bl"(Можно попытаться отвлечь зомби... Но как?)"
            s w bl"(В прошлый раз тот почти не обратил на меня внимания.)"
            s w bl"(Так...Ну вот камень лежит.)"
            s w bl sm "(Брошу его, может зомби с девушки на него переключится.)"
            s w bl an "..."
            s w bl an "(Я сейчас сильно рискую. Могу и умереть.)"
            s w bl ":("
            s w bl sm"(Ладно, я уже решила! ТОЛЬКО ВПЕРЕД!!!)"
            hide s with fastdissolve
            "Не давая себе шанса передумать, Стратег со всей силы бросила камень."
            play sound "audio/rock.mp3"
            "Камень упал на приличном расстоянии от дерева."
            "....."
            "Зомби он, по-видимому, не заинтересовал."
            show s w bl with fastdissolve
            s w bl an "Черт!"
            hide s
            "Девушка с дерева увидела Стратега."
            show girl shock with fastdissolve
            girl shock "ЭЭЭЙ!!! ПОМОГИ МНЕ!!!"
            girl cry "Ну что ты стоишь там?! Сделай что-нибудь! Пожалуйста.."
            hide girl 
            show s w bl
            s w bl an "(Заткнись, дура! Он меня сейчас заметит!)"
            hide s
            "Стоило ей об этом подумать, как зомби обернулся."
            "Видя в Стратеге более легкую добычу, мертвец бросился в ее сторону."
            "Девушка на дереве, в свою очередь, поспешила слезть и рванула в противоположном направлении."
            scene black with fade
            s "БЛ#@$!!!!!"
            "Она бежала быстро, но зомби был быстрее."
            "Знала бы Стратег, чем ей обернется ее альтруизм - ни за что не помогла бы той девушке."
            "Но вот она - тщетно бежит от своей смерти."
            s "(Зато хоть та истеричка выжила...)"
            play sound "audio/уведа.mp3"
            $ fuck.grant()
            "В конце-концов, зомби все-таки добрался до блондинки."







            jump dead_end





        label bl_slaughter:
            scene tree with fade
            show s w bl with fastdissolve
            s w bl hor"(Не могу я оставить ее так!)"
            s w bl an "(Кем я буду после этого?)"
            s w bl "(Все-таки, я уже убила одного зомби.)"
            s w bl sm "(И в этот раз все получится!)"
            scene tree with fastdissolve
            "Стретег покрепче ухватила оружие и вышла из-за укрытия."
            "Она тихо подкрадывалась к мертвецу. Точный удар в голову - вот и все."
            "До несчастного дерева осталось 10 метров."
            show girl shock with fastdissolve
            girl cry "Помоги..."
            hide girl
            show s w bl e
            s w bl an "(Молчи! Он заметит!)"
            s w bl an "БЛ#@$!"
            scene black with fade
            "Мысли материальны."
            "Зомби молниеносно обернулся и атаковал Стратега."
            "Та даже не успела нож поднять."

            jump dead_end




        label bl_mimo:
            scene tree with fade 
            show s w bl with fastdissolve
            s w bl hor "(Прости! Я не могу тебе помочь...)"
            s w bl hor "(Не могу просто взять и грохнуть этого зомби! Это не плевое дело.)"
            s w bl hor "(Да, одного зомби я убила.)"
            s w bl "(Но то был выброс адреналина. Они сильные, быстрые. А я ранена. Больше такой фокус не пройдет.)"
            hide s
            "Стратег стыдливо отвернулась."

            scene street with fade
            show s w bl with fastdissolve
            s w bl "(Надо решить, что делать дальше.)"
            s w bl "(Приоритетная задача - найти укрытие.)"
            s w bl an "(Пока мне везло, и зомби на улице почти не было.)"
            s w bl an "(Но это не значит, что я в безопасности.)"
            s w bl hor "(Не хочу повторить судьбу той девушки на дереве.)"
            s w bl"(...Итак. Куда идти?)"
            s w bl"(Нужно безопасное место недалеко отсюда.)"
            s w bl an "(Чтоб ни один чертов зомби не проник внутрь.)"
            s w bl "(Желательно, с запасами еды и воды.)"
            s w bl "..."
            s w bl "(Думай, думай, думай..)"
            s w bl sm "О!"
            s w bl sm "(Тут же есть банк совсем рядом! С надежной металлической дверью.)"
            s w bl "(Туда и пойду. Все равно не вижу вариантов получше.)"
            scene black with fade
            "Девушка поковыляла к зданию банка."
            "Нога кровоточила, холодный пот прошиб все тело."
            "Спустя вечность, она добралась до цели."
            "Дернула за ручку. Заперто."
            s "(Бл$! Конечно заперто, ночь на дворе.)"
            s "(Хотя, это же банк. Там должен быть охранник на смене.)"
            "Девушка начала долбиться в дверь."
            play sound "audio/уведа.mp3"
            $ door.grant()
            "..."
            "Тишина."
            "Затем она обнаружила кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            s "Пожалуйста, помогите!"
            voice "..."
            voice "Что у вас случилось?"
            s "Нет времени объяснять! Сначала впустите меня!"
            voice "Девушка, спокойно. Объясните, что случилось."
            s "ПРОСТО ОТКРОЙТЕ ДВЕРЬ!"
            "Послышался усталый вздох. Затем прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."
            
            jump s_bl_bank











        label s_bank_with_girl:
            scene bank with fade
            "Первое, что девушки увидели - пронзительный взгляд охранника."
            show sec mad with fastdissolve
            sec mad "..."
            hide sec mad
            show s w with fastdissolve
            s w "..."
            hide s w
            show girl shock with fastdissolve
            l shock "..."
            l shock "Понимаете, мы-"
            hide girl
            show sec mad
            sec mad "..."
            hide sec mad
            show girl shock
            l shock "Мы..мы...эмм-м, да. Мы п-попали в сложную ситуацию. Эти..зомби, они-"
            "Девушка нервничала. Под тяжелым взором охранника ей было сложно сформулировать свои мысли."
            hide girl
            show sec
            sec"..."
            sec sm "Что?"
            sec sm "Вы думаете, это очень смешно?"
            sec "Врываться в государственное учреждение и нести бред в мою ночную смену - это такие шуточки у вас?"
            "Взгляд мужчины стал еще мрачнее."
            sec mad "Барышня, что это у Вас в руке делает нож?"
            hide sec
            show s w 
            s w e "Для самообороны, очевидно."
            hide s 
            show girl
            l an "Нет, послушайте, зом-"
            hide girl 
            show sec 
            sec "Довольно. На выход."
            hide sec
            show s w 
            s w an "Дайте хоть объяснить. Все очень серьезно."
            s w e "Вы что, не знаете, что происходит снаружи?"
            hide s 
            show sec 
            sec "Я знаю вот что: вам пора."
            sec mad "Нечего мне тут про каких-то зомби затирать. Посмеялись и хватит."
            hide sec
            show girl
            l an "..."
            hide girl
            show s w 
            s w an "..."
            hide s
            "Девушки ошарашенно уставились на него. Этот мужик про апокалипсис, оказывается, ни сном, ни духом. А теперь еще и выгоняет их?!"
            "Думает, они тут шутки шутят!"
            "Волна злости окатила Стратега."
            "Стоит тут, видите ли, весь такой из себя важный."
            show s w 
            s w an "(Да он нас даже не слушает! Козел.)"
            s w an "Мы же вам говорим - там людей убивают."
            hide s
            show girl
            l shock "Я сама чуть к прабабке не отправилась..."
            hide girl
            show s w
            s w an "Нам нужно забаррикадироваться и разработать план действий."
            s w "Угроза реальная, мы должны-"
            hide s
            show sec 
            sec "Вы сами себя вообще слышите? Решили мое терпение испытать, а?"
            hide sec
            s "{i}Я его убью сейчас нахрен.{\i}"
            l "{i}Тише ты, он же услышит!{\i}"
            s "(Ну и что с ним делать?)"

            window hide


            menu:
                "Попробовать договориться":
                    jump negotiation
                "Свалить отсюда":
                    jump get_out
                "Пришить ублюдка":
                    jump kill_the_bastard

            window show


        label negotiation:
            $smental = 5 # за брата не мстила, но дружит с Лайлой и охранником
            show s w with fastdissolve
            s w "Мы никуда не уйдем. Вы должны нас выслушать."
            play sound "audio/уведа.mp3"
            $ dogovor.grant()
            s w an "Поговорим как взрослые люди."
            hide s
            show sec 
            sec sm "Как взрослые люди? Взрослые люди, по идее, не порят чушь про сай-фай покойников."
            hide sec
            show girl
            l an "Д-да мы не врем! Пройдитесь по улице - сами убедитесь."
            hide girl
            show sec 
            sec "Мне нельзя покидать пост. У вас доказательства-то есть?"
            hide sec
            show girl
            l an "Доказательства?! Да как-то не было на это времени, меня, как-бы, чуть монстр не сожрал!"
            hide girl
            show s w 
            s w "Лайла, спокойно."
            s w sm "Уважаемый, зайдите в интернет. Я уверена, в новостях уже есть вся информация."
            hide s
            show sec 
            "Очередной усталый вздох. Он разве что глаза не закатил."
            "..."
            "Мужчина достал телефон и несколько минут изучал ленту новостей."
            "По тому, как его глаза расширились, девушки поняли - в новостях подтвердились их слова."
            sec "..."
            sec mad "В это сложно поверить."
            hide sec
            show s w 
            s w an "Такова реальность. Мир уже не тот, каким был вчера."
            hide s 
            show sec mad
            sec mad "Ладно. Хорошо. Видимо, вы правы. Наступил конец света."
            sec mad "Прелестно."
            sec mad "..."
            sec "Ну и что вы предлагаете?"
            hide sec
            show s w 
            s w "Как я уже сказала, нам нужно себя обезопасить. Крепко запереть дверь и заблокировать окна."
            s w "Побудем здесь какое-то время. В безопасности. А потом, может, нас спасут спецслужбы."
            s w hor"(По крайней мере, я на это надеюсь.)"
            hide s
            show girl 
            l "Звучит как толковый план."
            l sm "У меня вот нет желания снова выходить наружу. Уже хватило впечатлений."
            l sm "Останемся здесь и подождем, пока государство обо всем позаботиться."
            hide girl 
            show sec 
            sec "(Сомнительно...)"
            sec "И долго мы тут торчать будем? Еда и вода не бесконечные. Из того, что есть в комнате отдыха, хватит на, дай Бог, 5 дней."
            hide sec
            show s w 
            s w an "Значит будем экономить. Нам нужно подумать, что делать в нынешней ситуации. Как противостоять зомби."
            s w "Нужно больше информации о них. Когда закончится провизия, попробуем сделать вылазку."
            s w "Но об этом позже."
            scene black with fade
            "С господином охранником, все-же, удалось договориться."
            "Трое людей приступили к укреплению их пристанища."
            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show s w with fastdissolve
            s w e "(Как же я устала...)"
            hide s with fastdissolve
            "Ее новые знакомые готовились ко сну."
            "Сегодняшняя ночь всем знатно потрепала нервы."
            s "(Может, стоит...)"


            window hide


            menu:
                "Поговорить перед сном":
                    jump talk_both
                "Лечь спать":
                    jump sleep_both


            window show




        label talk_both:
            show s w with fastdissolve
            s w "Ну и что вы об этом думаете..?"
            hide s 
            show girl
            l "О чем?"
            hide girl 
            show s w
            s w "О конце света."
            s w "Как это вообще произошло?"
            hide s
            show sec 
            sec sm "Да хрен его знает. Что толку об этом думать? Может, узнаем из новостей."
            hide sec
            show s w
            s w "Хм."
            hide s
            "На какое-то время комната погрузилась в тишину."
            "Каждый думал о чем-то своем."
            "..."
            show girl 
            l "Вы волнуетесь за близких?"
            l sm "Я вот только о них и думаю."
            hide girl
            "От ее слов засосало под ложечкой."
            "Стратег не хотела думать об этом. Не хотела вспоминать, как поступила с НИМ."
            show sec 
            sec sm "Мой спиногрыз, слава Богу, живой. Созванивался с ним."
            hide sec 
            show girl 
            l sm "Так у Вас есть сын..."
            hide girl
            show sec 
            sec "Ага. Тоже, говорит, забаррикадировался и сидит дома."
            sec sm "А у Вас что с семьей?"
            hide sec 
            show girl 
            l sm "Родители и младшая сестра. Они сейчас на отдыхе в другой стране."
            l sm2 "Наверное, попивают мохито и в ус не дуют."
            l sm "Не могу с ними связаться, к сожалению. Но, сердцем чувствую, что у них все хорошо."
            hide girl
            show sec 
            sec sm "Правильный настрой!"
            hide sec 
            "Разговор лился своим чередом."
            "Несмотря на усталость, все чувствовали нужду поболтать."
            "Хотели хоть как-то отвлечься от происходящего кошмара."
            scene black with slowdissolve
            "..."
            "В конце-концов, сон все-таки сморил их небольшую компанию."
            "Засыпали они с надеждой на будущее."
            "Светлое будущее, где не будет никаких зомби."



            jump end 



        label sleep_both:
            show s w with fastdissolve
            s w sm "(Ну, и мне пора баиньки.)"
            s w "(Не хочу думать обо всей этой херне с зомби.)"
            s w sm "(Я выжила - и это главное. Я крутая.)"
            hide s
            "Мозг отключался."
            scene black with slowdissolve
            "Всех сморил блаженный сон."
            "Больше не было стресса, не было гнетущего напряжения."
            "Этой бесконечной ночи пришел конец."
            "Завтра они проснуться. Продолжиться борьба за выживание."
            "Но это все завтра. А пока - безмятежная нега."
            jump end 





            






        label get_out:
            "Терпение Стратега лопнуло."
            "Она не могла больше здесь оставаться."
            show s w 
            s w an "З@ебал ты меня, дядя."
            s w an "Узколобый баран, ты даже не пытаешься нас услышать."
            s w an "Тебе проще верить в то, что все хорошо."
            s w an "Что снаружи не ходят гребаные зомби. Что они не мочат людей."
            hide s
            show sec 
            sec mad "..."
            hide sec
            show s w 
            s w an "Лайла, пошли отсюда. Найдем другое место."
            hide s
            show girl
            l shock "Эмм.."
            l cry "К-куда же мы пойдем? Может, стоит попробовать договориться?"
            hide girl
            show s w
            s w e "Ну, пока мы сюда шли, зомби нам не встречались. Мы вполне можем найти другое место."
            "Стратег злобно зыркнула на охранника."
            s w an "Здесь мы вряд-ли добъемся понимания."
            hide s
            show girl 
            l cry "Но.."
            hide girl
            "Стратег закатила глаза."
            s "(Заколебали. Все.)"
            scene black with fade
            "Не дожидаясь девушки, Стратег развернулась и пошла к выходу."
            "Злость на тупого охранника. Злость на ситуацию, в которой она оказалась. Злость на себя."
            "Эти чувства переполняли ее, выводили из себя."
            "Когда Стратег вышла из здания, она решила пойти в ближайший магазин."
            "Можно будет не переживать из-за запасов еды. Она сможет осесть там."
            "С осторожностью Стратег пошла дальше по улице."
            "Как вдруг..."
            "Из-за угла резко появился зомби!"
            "Он не стал церемониться и откусил у девушки часть затылка."
            "Вот ее песенка и спета."

            jump dead_end 


        label kill_the_bastard:
            show s w with fastdissolve
            s w an "(Она думает, я не всерьез.)"
            s w an "(Но я правда это сделаю. Он довел меня до ручки.)"
            s w "(Избавлюсь от него. Тогда мы с ней без проблем здесь останемся. И на один голодный рот меньше.)"
            s w "(Я на все готова ради выживания. Он - помеха. Надо устранить.)"
            hide s
            show sec 
            sec "Ну так вы собираетесь уходить? Или мне применить силу?"
            hide sec
            show girl 
            l shock "Но..."
            hide girl
            show s w 
            s w sm "Мы уходим. Счастливо оставаться!"
            s w an"(Черта с два ты меня прогонишь.)"
            scene black with fade
            'Пока охранник провожал их до двери, Стратег "случайно" задела бедром пачку документов на столе.'
            "Листки спланировали на пол."
            s "Ой..."
            sec "Аккуратней с документами!"
            "С тяжелым вздохом мужчина наклонился, собирая разбросанные бумаги."
            "Девушка того и ждала."
            "Она замахнулась и со всей силы загнала нож в спину мужчине."
            sec "АААААА!!!!СУКАА-АААА!!!!"
            l "ААААА???!!!!!!!!!!! ТЫ ЧТО?!!!"
            "Мужчина орал от боли. Лайла орала от ужаса."
            "Охранник резко согнул ногу и ударил блондинку в живот."
            scene black with deathfade
            play sound "audio/уведа.mp3"
            $ shurttummy.grant()
            "Для человека, которого пырнули, сила удара была недюжинная."
            "Стратег согнулась пополам и закашлялась."
            "По ощущениям, ей сломали пару ребер."
            $ shealth += 1 #ранена
            "..."
            "С этим ударом последние силы покинули мужчину."
            "Он обмяк и перестал дышать."

            play sound "audio/уведа.mp3"
            $ crazy.grant()
            "..."

            "Когда Стратег немного пришла в себя, она заметила на себе потерянный взгляд Лайлы."
            $ sslaughter +=1  #- убила мужика
            s "Теперь все-КХа-кхаа-..хорошо. Мы..мы сможем здесь остаться. Не волнуйся."
            l "..."
            s "Ты же понимаешь, что я должна была это сделать? Или он - или мы."
            l "....."
            s "Лайла."
            l "...? Что?"
            s "Я сделала это для нашей безопасности. Не бойся меня."
            l ".....Я понимаю. Ты права."
            s "Ты правда понимаешь?"
            l "Да."
            s "Хорошо."

            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show s w with fastdissolve
            s w  "(Как же я устала...)"
            s w an "(Блин, как ребра ломит. Я сегодня точно не засну.)"
            s w "(Мдя, прописал он мне знатно...)"
            s w "..."
            s w hor "(Вот уж не думала, что способна на такое...)"
            s w hor '(Я..Я поступила правильно. В этом "дивном новом мире" по другому не выживешь.)'
            s w "......"
            hide s
            "Тем временем, ее новая знакомая готовилась ко сну."
            "Это была трудная ночь. Им обеим нужно было отдохнуть."
            show s w with fastdissolve
            s "(Может, стоит...)"
            hide s



            window hide


            menu:
                "Поговорить с Лайлой":
                    jump talk_layla
                "Лечь спать":
                    jump sleep_layla
                "Убить ее":
                    jump kill_layla

            window show
        


        

        label talk_layla:
            show s w with fastdissolve
            s w an"(Нужно с ней поговорить. Она с тех пор и словечком не обмолвилась.)"
            s w sm "Лайла?"
            s w sm "Лайла, милая, ты спишь?"
            l "......"
            s w an "(Уже заснула? Или притворяется?)"
            s w ':('
            s w sm "А я вот поболтать хотела, знаешь..."
            s w "Обо всей этой чертовщине в мире."
            s w "Почему...Как это произошло.."
            s w "Как теперь будет выглядеть наш мир?"
            s w sm "Существует ли еще мораль..."
            l "......"
            s w an "..."
            s w "(Видимо, реально спит.)"
            s w "(Да и мне пора.)"
            hide s
            "Стратег пыталась заснуть, но разные навязчивые мысли мешали."
            "Она вслушивалась в дыхание девушки: оно было ровное, глубокое."
            "Стратег сосредоточилась на этом звуке. Сон накатывал медленно, но неизбежно."
            scene black with slowdissolve
            "Она и не заметила, в какой момент заснула."
            "А вот пробуждение было ярким."
            scene restroom
            show girl with deathfade
            l an "..."
            hide girl
            "Лайла, этот божий одуванчик...Она пырнула девушку."
            "Ударила ножом в спину! Ее ножом!!!"
            show s 
            s hor "Лайла..."
            s cry "................."
            s cry "(Все-таки, она не поняла меня.)"

            jump dead_end


        label sleep_layla:
            show s w with fastdissolve
            s w "(Не буду ее отвлекать. Надо все переварить.)"
            s w "(Тоже попробую поспать. Во сне боли не чувствуешь.)"
            hide s
            "Она пыталась заснуть, но разные навязчивые мысли мешали."
            "Стратег вслушивалась в дыхание девушки рядом: оно было ровное, глубокое."
            "Сосредоточилась на этом звуке. Сон накатывал медленно, но неизбежно."
            scene black with slowdissolve
            "Она и не заметила, в какой момент заснула."
            "А вот пробуждение было ярким."
            scene restroom
            show girl with deathfade
            l an "..."
            hide girl
            "Лайла, этот божий одуванчик...Она пырнула девушку."
            "Ударила ножом в спину! Ее ножом!!!"
            show s 
            s hor "Лайла..."
            s cry "................."
            s cry "(Все-таки, она не поняла меня.)"

            jump dead_end

        label kill_layla:
            $ smental = 10 #ебанутая, всех убила
            show s w with fastdissolve
            s w "(Так не пойдет.)"
            s w an "(Она мне и слова не сказала после той ситуации.)"
            s w an "(Больше мне не доверяет...Если вообще доверяла.)"
            s w e "(Она так меня и грохнуть может...)"
            s w "(Буду действовать на опережение.)"
            s w "(Ничего личного. Холодный расчет.)"
            hide s
            "С этими невеселыми мыслями, Стратег закрыла глаза."
            scene black with slowdissolve
            s "(Нужно сделать вид, что сплю.)"
            s "(Она, якобы, уже заснула.)"
            s "(Скорее всего, тоже притворяется.)"
            "Немного погодя, Стратег решила действовать."
            scene restroom
            show girl with deathfade
            l shock "..."
            hide girl 
            show s w 
            s w "Прости, Лайла. Может, ты поймешь меня."
            hide s
            show girl
            l shock "С-сучка.."
            l cry "Убила меня!"
            hide girl
            scene black with fade
            "Это были ее последние слова."
            "Теперь Стратег осталась совсем одна."
            jump end







        


            

            



        label s_bank:
            scene bank with fade
            "Первое, что девушка увидела - пронзительный взгляд охранника."
            show sec mad with fastdissolve
            sec mad "..."
            hide sec mad
            show s w with fastdissolve
            s w an "..."
            s w "Мне нужна помощь."
            hide s
            show sec
            sec "Какая помощь?"
            hide sec
            show s w 
            s w "Укрытие. От зомби."
            "Девушка не ходила вокруг, да около. Сказала, как есть."
            hide s
            show sec
            sec "..."
            sec sm "Что?"
            sec sm "Вы думаете, это очень смешно?"
            sec "Врываться в государственное учреждение и нести бред в мою ночную смену - это такие шуточки у Вас?"
            "Взгляд мужчины стал еще мрачнее."
            sec mad "Барышня, а что это у Вас в руке делает нож?"
            hide sec
            show s w 
            s w e "Для самообороны, очевидно."
            s w e "..."
            s w "Вернемся к теме. Зом-"
            hide s
            show sec 
            sec "Довольно. На выход."
            hide sec
            show s w 
            s w an "Дайте хоть объяснить. Все очень серьезно."
            s w e "Вы что, не знаете, что происходит снаружи?"
            hide s 
            show sec 
            sec "Я знаю вот что: Вам пора."
            sec mad "Нечего мне тут про каких-то зомби затирать. Посмеялись и хватит."
            hide sec
            show s w 
            s w an "..."
            hide s
            show sec
            "Девушка ошарашенно посмотрела на него. Этот мужик про апокалипсис, оказывается, ни сном, ни духом. А теперь еще и выгоняет ее?!"
            "Думает, она тут шутки шутят!"
            "Волна злости окатила Стратега."
            "Стоит тут, видите ли, весь такой из себя важный."
            hide sec
            show s w 
            s w an "(Да он меня даже не слушает! Козел.)"
            s w an "Я же вам говорю - там людей убивают."
            s w hor "Моего брата загрызли. Девушка на улице..."
            s w hor"....."
            s w an "Нам нужно забаррикадироваться и разработать план действий."
            s w "Угроза реальная, мы должны-"
            hide s
            show sec 
            sec "Вы сами себя вообще слышите? Решили мое терпение испытать, а?"
            show sec mad
            s "(Я его убью сейчас нахрен!)"
            s "(Ну и что с ним делать?)"
            hide sec

            window hide


            menu:
                "Попробовать договориться":
                    jump negotiation_alone
                "Свалить отсюда":
                    jump get_out_alone
                "Пришить ублюдка":
                    jump kill_the_bastard_alone

            window show


        label negotiation_alone:
            show s w with fastdissolve
            s w "Я никуда не уйду. Вы должны меня выслушать."
            play sound "audio/уведа.mp3"
            $ dogovor.grant()
            s w an "Поговорим как взрослые люди."
            hide s
            show sec 
            sec sm "Как взрослые люди? Взрослые люди, по идее, не порят чушь про сай-фай покойников."
            hide sec
            show s w 
            s w "Я не вру! Пройдитесь по улице - сами убедитесь."
            hide s w 
            show sec 
            sec "Мне нельзя покидать пост. У Вас доказательства-то есть?"
            hide sec
            show s w
            s w an "Доказательства?! Да как-то не до них было.."
            s w "(Так, спокойно. Можно договориться.)"
            s w sm "Уважаемый, зайдите в интернет. Я уверена, в новостях уже есть вся информация."
            hide s
            show sec
            "Очередной усталый вздох. Он разве что глаза не закатил."
            "..."
            "Мужчина достал телефон и несколько минут изучал ленту новостей."
            "По тому, как его глаза расширились, девушка поняла - в новостях подтвердились ее слова."
            sec "..."
            sec mad "В это сложно поверить."
            hide sec
            show s w 
            s w an "Такова реальность. Мир уже не тот, каким был вчера."
            hide s 
            show sec mad
            sec mad "Ладно. Хорошо. Видимо, Вы правы. Наступил конец света."
            sec mad "Прелестно."
            sec mad "..."
            sec "Ну и что Вы предлагаете?"
            hide sec
            show s w 
            s w "Как я уже сказала, нам нужно себя обезопасить. Крепко запереть дверь и заблокировать окна."
            s w "Побудем здесь какое-то время. В безопасности. А потом, может, нас спасут спецслужбы."
            s w hor"(По крайней мере, я на это надеюсь.)"
            hide s
            show sec 
            sec "(Сомневаюсь...)"
            sec "И долго мы тут торчать будем? Еда и вода не бесконечные. Из того, что есть в комнате отдыха, хватит на, дай Бог, 5 дней."
            hide sec
            show s w 
            s w an "Значит будем экономить. Нам нужно подумать, что делать в нынешней ситуации. Как противостоять зомби."
            s w "Нужно больше информации о них. Когда закончится провизия, попробуем сделать вылазку."
            s w "Но об этом позже."
            scene black with fade
            "С господином охранником, все-же, удалось договориться."
            "Двое людей приступили к укреплению их пристанища."
            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show s w with fastdissolve
            s w e "(Как же я устала...)"
            show s w 
            "Ее новый знакомый готовился ко сну."
            "Сегодняшняя ночь знатно потрепала им нервы."
            s w "(Может, стоит...)"
            hide s w
            $ smental = 15 #пассивный наблюдатель, за брата не отомстила, девушку не спасла. с охранником только потому, что ей удобно.


            window hide


            menu:
                "Поговорить перед сном":
                    jump talk_sec
                "Лечь спать":
                    jump sleep_sec
                


            window show




        label talk_sec:
            show s w with fastdissolve
            s w "Ну и что Вы об этом думаете..?"
            hide s 
            show sec
            sec "Об апокалипсисе?"
            hide sec
            show s w
            s w "Да, о нем."
            s w "Как это вообще произошло?"
            hide s
            show sec 
            sec sm "Да хрен его знает. Что толку об этом думать? Может, узнаем из новостей."
            hide sec
            show s w
            s w "Хм."
            hide s
            "На какое-то время комната погрузилась в тишину."
            "Каждый думал о чем-то своем."
            "..."
            "Разговор все не клеился. Стратег не успела проникнуться нежными чувствами к охраннику."
            "Она с ним объединилась по одной лишь причине - безопасность."
            "Он, впрочем, тоже не был в восторге от их почти вынужденного дуэта."
            "Лучше бы она вообще не заводила разговор."
            "........."
            "Усталость брала свое - глазки уже слипались."
            scene black with slowdissolve
            "И в конце-концов, сон все-таки сморил их."
            "Стратег заснула глубоким сном без сновидений. Все ей было безразлично, никакие тревоги этого мира не трогали ее."
            "Ее холодное сердце было глухо к трагедиям, с которыми она столкнулась."
            "К чему приведет присущая ей меркантильность? Так ли полезен холодный расчет?"
            "Стратег об этом не думала. И не будет думать."
            "Сейчас она просто спит."




            jump end 



        label sleep_sec:
            show s w with fastdissolve
            s w sm "(Ну, и мне пора баиньки.)"
            s w "(Не хочу думать обо всей этой херне с зомби.)"
            s w sm "(Я выжила - и это главное. Я крутая.)"
            hide s
            "Мозг отключался."
            scene black with slowdissolve
            "Ее сморил долгожданный сон."
            "Больше не было брата. Не было той девушки с аллеи."
            "Их больше нет. Стратег не видела сам момент смерти. Зачем ей смотреть?"
            "Ну умерли, и умерли. Думать об этом - себе дороже."
            "Нельзя даже мысли допускать."
            "Вот она и не думала. Спала безмятежным сном."
            "Ей всегда будет все равно."
            jump end 





            






        label get_out_alone:
            "Терпение Стратега лопнуло."
            "Она не могла больше здесь оставаться."
            show s w 
            s w an "З@ебал ты меня, дядя."
            s w an "Узколобый баран, ты даже не пытаешься меня услышать."
            s w an "Тебе проще верить в то, что все хорошо."
            s w an "Что снаружи не ходят гребаные зомби. Что они не мочат людей."
            hide s
            show sec 
            sec mad "..."
            hide sec
            "Девушке это все осточертело."
            "Показав средний палец на прощание, она грациозной походкой пошла к выходу."
            scene black with fade
            "Злость на тупого охранника. Злость на ситуацию, в которой она оказалась. Злость на себя."
            "Эти чувства переполняли ее, выводили из себя."
            "Когда Стратег вышла из здания, она решила пойти в ближайший магазин."
            "Можно будет не переживать из-за запасов еды. Она сможет осесть там."
            "С осторожностью Стратег пошла дальше по улице."
            "Как вдруг..."
            "Из-за угла резко появился зомби!"
            "Он не стал церемониться и откусил у девушки часть затылка."
            "Вот ее песенка и спета."

            jump dead_end 


        label kill_the_bastard_alone:
            $ smental = 20 #  не спасла брата и девушку, убила охранника.
            show s w with fastdissolve
            s w an "(Да я его внатуре прикончу.)"
            s w an "(Довел меня до ручки.)"
            s w "(Избавлюсь от него. Тогда без проблем здесь осяду. И на один голодный рот меньше.)"
            s w "(Я на все готова ради выживания. Он - помеха. Надо устранить.)"
            hide s
            show sec 
            sec "Ну так Вы собираетесь уходить? Или мне применить силу?"
            hide sec
            show s w 
            s w sm "Я ухожу. Счастливо оставаться!"
            s w an"(Черта с два ты меня прогонишь.)"
            scene black with fade
            'Пока охранник провожал ее до двери, Стратег "случайно" задела бедром пачку документов на столе.'
            "Листки спланировали на пол."
            s "Ой..."
            sec "Аккуратней с документами!"
            "С тяжелым вздохом мужчина наклонился, собирая разбросанные бумаги."
            "Девушка того и ждала."
            "Она замахнулась и со всей силы загнала нож в мужскую спину."
            sec "АААААА!!!!СУКАА-АААА!!!!"
            "Мужчина заорал от боли."
            "Вдруг он резко согнул ногу и ударил блондинку в живот."
            scene black with deathfade
            play sound "audio/уведа.mp3"
            $ shurttummy.grant()
            "Для человека, которого пырнули, сила удара была недюжинная."
            "Стратег согнулась пополам и закашлялась."
            "По ощущениям, ей сломали пару ребер."
            $ shealth += 1 #ранена
            "..."
            "С этим ударом последние силы покинули мужчину."
            "Он обмяк и перестал дышать."

            play sound "audio/уведа.mp3"
            $ crazy.grant()
            "........"



            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show s w with fastdissolve
            s w  "(Как же я устала...)"
            s w an "(Блин, как ребра ломит. Я сегодня точно не засну.)"
            s w "(Мдя, прописал он мне знатно...)"
            s w "..."
            s w e "(Вот уж не думала, что способна на убийство человека...)"
            s w '(Хотя, того требовали обстоятельства.)'
            s w sm "Ай ну и похрен!"
            s w "(Итак, чем бы мне заняться?)"
            hide s



            window hide


            menu:
                "Порефлексировать":
                    jump reflection
                "Попробовать заснуть":
                    jump sleep_alone

            window show



        label reflection:
            show s w 
            s w e "(Итак...)"
            s w "(Как бы описать сегодняшний день...?)"
            s w sm '(Пожалуй, слово "п$здец" - самое подходящее.)'
            s w e "(Сначала брата живьем сожрали.)"
            s w "(Я, конечно, благоразумно оттуда ретировалась. И правильно сделала.)"
            s w "(Потом о нем поплачу.)"
            s w sm "(Потом эта дура на дереве. Орала она страшно.)"
            s w sm "(Ну и вишенка на торте - я убила мужика.)"
            s w an "(Мда, лоу-кик у него был мощный.)"
            s w sm "(Вот только где он, а где я?)"
            s w "(Лежит там, взгляд стеклянный.)"
            s w sm "(А я здесь! Весь банк в моем единоличном распоряжении.)"
            s w "(Даже не жалко этого охранника.)"
            s w "(Мне вообще никого не жалко.)"
            s w sm ":)"
            scene black with slowdissolve
            "С этими мыслями Стратег и заснула. С милой улыбкой."
            "Наверное, гордилась тем, что выжила."
            "Только она. А другие умерли."
            "Девушка смогла адаптироваться."
            "Мир изменился, и Стратег с ним."
            "Она этим утром, и она сейчас - два разных человека."
            "Только отбросив человечность, она смогла всех пережить."
            "Без сожалений."


            jump end 



        label sleep_alone:
            show s w 
            s w sm "(Перво-наперво, надо поспать!)"
            s w an "(Да, болит живот. Ну и ладно!)"
            s w an "(Потерплю, а как проснусь - все заживет.)"
            scene black with slowdissolve
            "Девушка поудобнее расположилась и начала считать овец."
            "Ей было все равно на труп охранника у входа."
            "Было пофиг на ту девушку с аллеи."
            "Про брата она даже не вспомнила."
            "Что-то в ней безвозвратно умерло."
            "Хочешь жить - умей вертеться. Так девушка и делала."
            "Заснула она в оглушающей тишине. Совсем одна."
            

            jump end 









        label s_bl_bank_with_girl:
            scene bank with fade
            "Первое, что девушки увидели - пронзительный взгляд охранника."
            show sec mad with fastdissolve
            sec mad "..."
            hide sec mad
            show s w bl with fastdissolve
            s w bl "..."
            hide s w
            show girl shock with fastdissolve
            l shock "..."
            l shock "Понимаете, мы-"
            hide girl
            show sec mad
            sec mad "..."
            hide sec mad
            show girl shock
            l shock "Мы..мы...эмм-м, да. Мы п-попали в сложную ситуацию. Эти..зомби, они-"
            "Девушка нервничала. Под тяжелым взором охранника ей было сложно сформулировать свои мысли."
            hide girl
            show sec
            sec"..."
            sec sm "Что?"
            sec sm "Вы думаете, это очень смешно?"
            sec "Врываться в государственное учреждение и нести бред в мою ночную смену - это такие шуточки у вас?"
            "Взгляд мужчины стал еще мрачнее."
            sec mad "Барышня, что это у Вас в руке делает нож?"
            hide sec
            show s w bl
            s w bl e "Для самообороны, очевидно."
            hide s 
            show girl
            l an "Нет, послушайте, зом-"
            hide girl 
            show sec 
            sec "Довольно. На выход."
            hide sec
            show s w bl 
            s w bl an "Дайте хоть объяснить. Все очень серьезно."
            s w bl e "Вы что, не знаете, что происходит снаружи?"
            hide s 
            show sec 
            sec "Я знаю вот что: вам пора."
            sec mad "Нечего мне тут про каких-то зомби затирать. Посмеялись и хватит."
            hide sec
            show girl
            l an "..."
            hide girl
            show s w bl 
            s w bl an "..."
            hide s
            "Девушки ошарашенно уставились на него. Этот мужик про апокалипсис, оказывается, ни сном, ни духом. А теперь еще и выгоняет их?!"
            "Думает, они тут шутки шутят!"
            "Волна злости окатила Стратега."
            "Стоит тут, видите ли, весь такой из себя важный."
            show s w bl 
            s w bl an "(Да он нас даже не слушает! Козел.)"
            s w bl an "Мы же вам говорим - там людей убивают."
            hide s
            show girl
            l shock "Я сама чуть к прабабке не отправилась..."
            hide girl
            show s w bl
            s w bl an "Нам нужно забаррикадироваться и разработать план действий."
            s w bl"Угроза реальная, мы должны-"
            hide s
            show sec 
            sec "Вы сами себя вообще слышите? Решили мое терпение испытать, а?"
            hide sec
            s "{i}Я его убью сейчас нахрен.{\i}"
            l "{i}Тише ты, он же услышит!{\i}"
            s "(Ну и что с ним делать?)"

            window hide


            menu:
                "Попробовать договориться":
                    jump blnegotiation
                "Свалить отсюда":
                    jump blget_out
                "Пришить ублюдка":
                    jump blkill_the_bastard

            window show


        label blnegotiation:
            $smental = 40 # отомстила за брата, дружит с Лайлой и охранником
            show s w bl with fastdissolve
            s w bl "Мы никуда не уйдем. Вы должны нас выслушать."
            play sound "audio/уведа.mp3"
            $ dogovor.grant()
            s w bl an "Поговорим как взрослые люди."
            hide s
            show sec 
            sec sm "Как взрослые люди? Взрослые люди, по идее, не порят чушь про сай-фай покойников."
            hide sec
            show girl
            l an "Д-да мы не врем! Пройдитесь по улице - сами убедитесь."
            hide girl
            show sec 
            sec "Мне нельзя покидать пост. У вас доказательства-то есть?"
            hide sec
            show girl
            l an "Доказательства?! Да как-то не было на это времени, меня, как-бы, чуть монстр не сожрал!"
            hide girl
            show s w bl 
            s w bl"Лайла, спокойно."
            s w bl sm "Уважаемый, зайдите в интернет. Я уверена, в новостях уже есть вся информация."
            hide s
            show sec 
            "Очередной усталый вздох. Он разве что глаза не закатил."
            "..."
            "Мужчина достал телефон и несколько минут изучал ленту новостей."
            "По тому, как его глаза расширились, девушки поняли - в новостях подтвердились их слова."
            sec "..."
            sec mad "В это сложно поверить."
            hide sec
            show s w bl
            s w bl an "Такова реальность. Мир уже не тот, каким был вчера."
            hide s 
            show sec mad
            sec mad "Ладно. Хорошо. Видимо, вы правы. Наступил конец света."
            sec mad "Прелестно."
            sec mad "..."
            sec "Ну и что вы предлагаете?"
            hide sec
            show s w bl
            s w bl "Как я уже сказала, нам нужно себя обезопасить. Крепко запереть дверь и заблокировать окна."
            s w bl "Побудем здесь какое-то время. В безопасности. А потом, может, нас спасут спецслужбы."
            s w bl hor"(По крайней мере, я на это надеюсь.)"
            hide s
            show girl 
            l "Звучит как толковый план."
            l sm "У меня вот нет желания снова выходить наружу. Уже хватило впечатлений."
            l sm "Останемся здесь и подождем, пока государство обо всем позаботиться."
            hide girl 
            show sec 
            sec "(Сомнительно...)"
            sec "И долго мы тут торчать будем? Еда и вода не бесконечные. Из того, что есть в комнате отдыха, хватит на, дай Бог, 5 дней."
            hide sec
            show s w bl
            s w bl an "Значит будем экономить. Нам нужно подумать, что делать в нынешней ситуации. Как противостоять зомби."
            s w bl "Нужно больше информации о них. Когда закончится провизия, попробуем сделать вылазку."
            s w bl "Но об этом позже."
            scene black with fade
            "С господином охранником, все-же, удалось договориться."
            "Трое людей приступили к укреплению их пристанища."
            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show s w bl with fastdissolve
            s w bl e "(Как же я устала...)"
            hide s with fastdissolve
            "Ее новые знакомые готовились ко сну."
            "Сегодняшняя ночь всем знатно потрепала нервы."
            s "(Может, стоит...)"


            window hide


            menu:
                "Поговорить перед сном":
                    jump bltalk_both
                "Лечь спать":
                    jump blsleep_both


            window show




        label bltalk_both:
            show s w bl with fastdissolve
            s w bl "Ну и что вы об этом думаете..?"
            hide s 
            show girl
            l "О чем?"
            hide girl 
            show s w bl
            s w bl "О конце света."
            s w bl "Как это вообще произошло?"
            hide s
            show sec 
            sec sm "Да хрен его знает. Что толку об этом думать? Может, узнаем из новостей."
            hide sec
            show s w bl
            s w bl "Хм."
            hide s
            "На какое-то время комната погрузилась в тишину."
            "Каждый думал о чем-то своем."
            "..."
            show girl 
            l "Вы волнуетесь за близких?"
            l sm "Я вот только о них и думаю."
            hide girl
            show sec 
            sec sm "Мой спиногрыз, слава Богу, живой. Созванивался с ним."
            hide sec 
            show girl 
            l sm "Так у Вас есть сын..."
            hide girl
            show sec 
            sec "Ага. Тоже, говорит, забаррикадировался и сидит дома."
            sec sm "А у Вас что с семьей?"
            hide sec 
            show girl 
            l sm "Родители и младшая сестра. Они сейчас на отдыхе в другой стране."
            l sm2 "Наверное, попивают мохито и в ус не дуют."
            l sm "Не могу с ними связаться, к сожалению. Но, сердцем чувствую, что у них все хорошо."
            hide girl
            show sec 
            sec sm "Правильный настрой!"
            hide sec 
            "Разговор лился своим чередом."
            "Несмотря на усталость, все чувствовали нужду поболтать."
            "Хотели хоть как-то отвлечься от происходящего кошмара."
            scene black with slowdissolve
            "..."
            "В конце-концов, сон все-таки сморил их небольшую компанию."
            "Засыпали они с надеждой на будущее."
            "Светлое будущее, где не будет никаких зомби."



            jump end 



        label blsleep_both:
            show s w bl with fastdissolve
            s w bl sm "(Ну, и мне пора баиньки.)"
            s w bl "(Не хочу думать обо всей этой херне с зомби.)"
            s w bl sm "(Я выжила - и это главное. Я крутая.)"
            hide s
            "Мозг отключался."
            scene black with slowdissolve
            "Всех сморил блаженный сон."
            "Больше не было стресса, не было гнетущего напряжения."
            "Этой бесконечной ночи пришел конец."
            "Завтра они проснуться. Продолжиться борьба за выживание."
            "Но это все завтра. А пока - безмятежная нега."
            jump end 





            






        label blget_out:
            "Терпение Стратега лопнуло."
            "Она не могла больше здесь оставаться."
            show s w bl 
            s w bl an "З@ебал ты меня, дядя."
            s w bl an "Узколобый баран, ты даже не пытаешься нас услышать."
            s w bl an "Тебе проще верить в то, что все хорошо."
            s w bl an "Что снаружи не ходят гребаные зомби. Что они не мочат людей."
            hide s
            show sec 
            sec mad "..."
            hide sec
            show s w bl
            s w bl an "Лайла, пошли отсюда. Найдем другое место."
            hide s
            show girl
            l shock "Эмм.."
            l cry "К-куда же мы пойдем? Может, стоит попробовать договориться?"
            hide girl
            show s w bl 
            s w bl e "Ну, пока мы сюда шли, зомби нам не встречались. Мы вполне можем найти другое место."
            "Стратег злобно зыркнула на охранника."
            s w bl an "Здесь мы вряд-ли добъемся понимания."
            hide s
            show girl 
            l cry "Но.."
            hide girl
            "Стратег закатила глаза."
            s "(Заколебали. Все.)"
            scene black with fade
            "Не дожидаясь девушки, Стратег развернулась и пошла к выходу."
            "Злость на тупого охранника. Злость на ситуацию, в которой она оказалась. Злость на себя."
            "Эти чувства переполняли ее, выводили из себя."
            "Когда Стратег вышла из здания, она решила пойти в ближайший магазин."
            "Можно будет не переживать из-за запасов еды. Она сможет осесть там."
            "С осторожностью Стратег пошла дальше по улице."
            "Как вдруг..."
            "Из-за угла резко появился зомби!"
            "Он не стал церемониться и откусил у девушки часть затылка."
            "Вот ее песенка и спета."

            jump dead_end 


        label blkill_the_bastard:
            show s w bl with fastdissolve
            s w bl an "(Она думает, я не всерьез.)"
            s w bl an "(Но я правда это сделаю. Он довел меня до ручки.)"
            s w bl "(Избавлюсь от него. Тогда мы с ней без проблем здесь останемся. И на один голодный рот меньше.)"
            s w bl "(Я на все готова ради выживания. Он - помеха. Надо устранить.)"
            hide s
            show sec 
            sec "Ну так вы собираетесь уходить? Или мне применить силу?"
            hide sec
            show girl 
            l shock "Но..."
            hide girl
            show s w bl 
            s w bl sm "Мы уходим. Счастливо оставаться!"
            s w bl an"(Черта с два ты меня прогонишь.)"
            scene black with fade
            'Пока охранник провожал их до двери, Стратег "случайно" задела бедром пачку документов на столе.'
            "Листки спланировали на пол."
            s "Ой..."
            sec "Аккуратней с документами!"
            "С тяжелым вздохом мужчина наклонился, собирая разбросанные бумаги."
            "Девушка того и ждала."
            "Она замахнулась и со всей силы загнала нож в спину мужчине."
            sec "АААААА!!!!СУКАА-АААА!!!!"
            l "ААААА???!!!!!!!!!!! ТЫ ЧТО?!!!"
            "Мужчина орал от боли. Лайла орала от ужаса."
            "Охранник резко согнул ногу и ударил блондинку."
            scene black with deathfade
            play sound "audio/уведа.mp3"
            $ shurttummy.grant()
            "Для человека, которого пырнули, сила удара была недюжинная."
            "Этот удар забрал его последние силы. Мужчина обмяк и больше не двигался."
            "Стратег же согнулась пополам и закашлялась."
            "Она и так была ранена. Еще одну травму она не переживет."
            "Обессиленная, она упала. Потеряла сознание."
            "Больше она не очнется."
            jump dead_end








        label s_bl_bank:
            scene bank with fade
            "Первое, что девушка увидела - пронзительный взгляд охранника."
            show sec mad with fastdissolve
            sec mad "..."
            hide sec mad
            show s w bl with fastdissolve
            s w bl an "..."
            s w bl "Мне нужна помощь."
            hide s
            show sec
            sec sm "Да, я понял по Вашему внешнему виду."
            hide sec
            "Стратег пропустила комментарий мимо ушей."
            show s w bl
            s w bl "Нужно укрытие. От зомби."
            "Девушка не ходила вокруг, да около. Сказала, как есть."
            hide s
            show sec
            sec "..."
            sec sm "Что?"
            sec sm "Вы думаете, это очень смешно?"
            sec "Врываться в государственное учреждение и нести бред в мою ночную смену - это такие шуточки у Вас?"
            "Взгляд мужчины стал еще мрачнее."
            sec mad "Барышня, а что это у Вас в руке делает нож?"
            hide sec
            show s w bl
            s w bl e "Для самообороны, очевидно."
            s w bl e "..."
            s w bl "Вернемся к теме. Зом-"
            hide s
            show sec 
            sec "Довольно. На выход."
            hide sec
            show s w bl
            s w bl an "Дайте хоть объяснить. Все очень серьезно."
            s w bl e "Вы что, не знаете, что происходит снаружи?"
            hide s 
            show sec 
            sec "Я знаю вот что: Вам пора."
            sec mad "Нечего мне тут про каких-то зомби затирать. Посмеялись и хватит."
            hide sec
            show s w bl
            s w bl an "..."
            hide s
            show sec
            "Девушка ошарашенно посмотрела на него. Этот мужик про апокалипсис, оказывается, ни сном, ни духом. А теперь еще и выгоняет ее?!"
            "Думает, она тут шутки шутят!"
            "Волна злости окатила Стратега."
            "Стоит тут, видите ли, весь такой из себя важный."
            hide sec
            show s w bl
            s w bl an "(Да он меня даже не слушает! Козел.)"
            s w bl an "Я же вам говорю - там людей убивают."
            s w bl hor "Моего брата загрызли. Девушка на улице..."
            s w bl hor"....."
            s w bl an "Нам нужно забаррикадироваться и разработать план действий."
            s w bl "Угроза реальная, мы должны-"
            hide s
            show sec 
            sec "Вы сами себя вообще слышите? Решили мое терпение испытать, а?"
            show sec mad
            s "(Я его убью сейчас нахрен!)"
            s "(Ну и что с ним делать?)"
            hide sec

            window hide


            menu:
                "Попробовать договориться":
                    jump blnegotiation_alone
                "Свалить отсюда":
                    jump blget_out_alone
                "Пришить ублюдка":
                    jump blkill_the_bastard_alone

            window show


        label blnegotiation_alone:
            show s w bl with fastdissolve
            s w bl "Я никуда не уйду. Вы должны меня выслушать."
            play sound "audio/уведа.mp3"
            $ dogovor.grant()
            s w bl an "Поговорим как взрослые люди."
            hide s
            show sec 
            sec sm "Как взрослые люди? Взрослые люди, по идее, не порят чушь про сай-фай покойников."
            hide sec
            show s w bl 
            s w bl "Я не вру! Пройдитесь по улице - сами убедитесь."
            hide s w 
            show sec 
            sec "Мне нельзя покидать пост. У Вас доказательства-то есть?"
            hide sec
            show s w bl 
            s w bl an "Доказательства?! Да как-то не до них было.."
            s w bl "(Так, спокойно. Можно договориться.)"
            s w bl sm "Уважаемый, зайдите в интернет. Я уверена, в новостях уже есть вся информация."
            hide s
            show sec
            "Очередной усталый вздох. Он разве что глаза не закатил."
            "..."
            "Мужчина достал телефон и несколько минут изучал ленту новостей."
            "По тому, как его глаза расширились, девушка поняла - в новостях подтвердились ее слова."
            sec "..."
            sec mad "В это сложно поверить."
            hide sec
            show s w bl 
            s w bl an "Такова реальность. Мир уже не тот, каким был вчера."
            hide s 
            show sec mad
            sec mad "Ладно. Хорошо. Видимо, Вы правы. Наступил конец света."
            sec mad "Прелестно."
            sec mad "..."
            sec "Ну и что Вы предлагаете?"
            hide sec
            show s w bl
            s w bl "Как я уже сказала, нам нужно себя обезопасить. Крепко запереть дверь и заблокировать окна."
            s w bl "Побудем здесь какое-то время. В безопасности. А потом, может, нас спасут спецслужбы."
            s w bl hor"(По крайней мере, я на это надеюсь.)"
            hide s
            show sec 
            sec "(Сомневаюсь...)"
            sec "И долго мы тут торчать будем? Еда и вода не бесконечные. Из того, что есть в комнате отдыха, хватит на, дай Бог, 5 дней."
            hide sec
            show s w bl 
            s w bl an "Значит будем экономить. Нам нужно подумать, что делать в нынешней ситуации. Как противостоять зомби."
            s w bl "Нужно больше информации о них. Когда закончится провизия, попробуем сделать вылазку."
            s w bl "Но об этом позже."
            scene black with fade
            "С господином охранником, все-же, удалось договориться."
            "Двое людей приступили к укреплению их пристанища."
            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show s w bl with fastdissolve
            s w bl e "(Как же я устала...)"
            s w bl an "(Еще одежда вся в этой черной крови. Фу!)"
            show s w bl 
            "Ее новый знакомый готовился ко сну."
            "Сегодняшняя ночь знатно потрепала им нервы."
            s w bl "(Может, стоит...)"
            hide s w
            $ smental = 25  #отомстила за брата, девушку не спасла. с охранником только потому, что ей удобно. травма, чувство вины.

            window hide


            menu:
                "Поговорить перед сном":
                    jump bltalk_sec
                "Лечь спать":
                    jump blsleep_sec
                


            window show




        label bltalk_sec:
            show s w bl with fastdissolve
            s w bl "Ну и что Вы об этом думаете..?"
            hide s 
            show sec
            sec "Об апокалипсисе?"
            hide sec
            show s w bl
            s w bl "Да, о нем."
            s w bl "Как это вообще произошло?"
            hide s
            show sec 
            sec sm "Да хрен его знает. Что толку об этом думать? Может, узнаем из новостей."
            hide sec
            show s w bl
            s w bl "Хм."
            hide s
            "На какое-то время комната погрузилась в тишину."
            "Каждый думал о чем-то своем."
            "..."
            "Разговор все не клеился. Стратег не успела проникнуться нежными чувствами к охраннику."
            "Она с ним объединилась по одной лишь причине - безопасность."
            "Он, впрочем, тоже не был в восторге от их почти вынужденного дуэта."
            "Лучше бы она вообще не заводила разговор."
            "........."
            "Усталость брала свое - глазки уже слипались."
            scene black with slowdissolve
            "И в конце-концов, они заснули."
            "Стратега мучал беспокойный сон. Воспоминания о покойном брате заполонили ее сознание."
            "Тупая боль сжала сердце."
            "Смерть брата была трагической. Стратег еще не скоро оправится от этой травмы."
            "Впереди ее ждало еще много потерь и лишений."
            "Начался зомби апокалипсис. Новая эра, где люди мрут как мухи."
            "Ее ждет тяжелый путь. Но она будет жить."
            "Чувство вины будет преследовать ее до гробовой доски."





            jump end 



        label blsleep_sec:
            show s w bl with fastdissolve
            s w bl sm "(Ну, и мне пора баиньки.)"
            s w bl "(Не хочу думать обо всей этой херне с зомби.)"
            s w bl sm "(Я выжила - и это главное. Я крутая.)"
            hide s
            "Мозг отключался."
            scene black with slowdissolve
            "Ее сморил беспокойный сон."
            "Снился брат. Девушка с аллеи, которую она не спасла."
            "Их больше нет. До самой смерти Стратег будет помнить, что не спасла их."
            "Была безучастным наблюдателем. Выбрала не рисковать жизнью. Позволила им бесславно умереть."
            "Таковы последствия ее выборов. Она жива, но какой ценой?"
            "Ее психика уже не будет прежней."
            jump end 





            






        label blget_out_alone:
            "Терпение Стратега лопнуло."
            "Она не могла больше здесь оставаться."
            show s w bl
            s w bl an "З@ебал ты меня, дядя."
            s w bl an "Узколобый баран, ты даже не пытаешься меня услышать."
            s w bl an "Тебе проще верить в то, что все хорошо."
            s w bl an "Что снаружи не ходят гребаные зомби. Что они не мочат людей."
            hide s
            show sec 
            sec mad "..."
            hide sec
            "Девушке это все осточертело."
            "Показав средний палец на прощание, она грациозной походкой пошла к выходу."
            scene black with fade
            "Злость на тупого охранника. Злость на ситуацию, в которой она оказалась. Злость на себя."
            "Эти чувства переполняли ее, выводили из себя."
            "Когда Стратег вышла из здания, она решила пойти в ближайший магазин."
            "Можно будет не переживать из-за запасов еды. Она сможет осесть там."
            "С осторожностью Стратег пошла дальше по улице."
            "Как вдруг..."
            "Из-за угла резко появился зомби!"
            "Он не стал церемониться и откусил у девушки часть затылка."
            "Вот ее песенка и спета."

            jump dead_end 


        label blkill_the_bastard_alone:
            show s w bl with fastdissolve
            s w bl an "(Да я его внатуре прикончу.)"
            s w bl an "(Довел меня до ручки.)"
            s w bl "(Избавлюсь от него. Тогда без проблем здесь осяду. И на один голодный рот меньше.)"
            s w bl "(Я на все готова ради выживания. Он - помеха. Надо устранить.)"
            hide s
            show sec 
            sec "Ну так Вы собираетесь уходить? Или мне применить силу?"
            hide sec
            show s w bl
            s w bl sm "Я ухожу. Счастливо оставаться!"
            s w bl an"(Черта с два ты меня прогонишь.)"
            scene black with fade
            'Пока охранник провожал ее до двери, Стратег "случайно" задела бедром пачку документов на столе.'
            "Листки спланировали на пол."
            s "Ой..."
            sec "Аккуратней с документами!"
            "С тяжелым вздохом мужчина наклонился, собирая разбросанные бумаги."
            "Девушка того и ждала."
            "Она замахнулась и со всей силы загнала нож в мужскую спину."
            sec "АААААА!!!!СУКАА-АААА!!!!"
            "Мужчина заорал от боли."
            "Вдруг он резко согнул ногу и ударил блондинку."
            scene black with deathfade
            play sound "audio/уведа.mp3"
            $ shurttummy.grant()
            "Для человека, которого пырнули, сила удара была недюжинная."
            "Этот удар забрал его последние силы. Мужчина обмяк и больше не двигался."
            "Стратег же согнулась пополам и закашлялась."
            "Она и так была ранена. Еще одну травму она не переживет."
            "Обессиленная, она упала. Потеряла сознание."
            "Больше она не очнется."
            jump dead_end




















                


       

    




        







        




        









































    label dead_end:
        play music "audio/смерть.mp3"
        window hide
        scene dead end with fade
        pause(2.0)
    
        
        
    return
        



    label red:
        $ p.info = 1

        scene black 
        show p with dissolve
        "Вы выбрали Психопата."
        hide p
        show p power at truecenter with dissolve
        'Ваш персонаж обладает уникальной способностью - "Безумие".' 
        "В пылу безумства у Вас включается режим 'имбы', но потеря контроля может стоить Вам жизни."
        hide p power
        "Больше о персонаже Вы можете узнать в галерее." #дополнить место где карточка 
        "Помните, что прохождение игры напрямую зависит от выбранного Вами персонажа."
        "Делайте выборы, исходя из его характеристик и оружия."
        "Наслаждайтесь игрой..."
        "{i}...И пусть удача всегда будет с Вами!{\i}"
        "P.S. Не забывайте сохраняться :)"
        stop music fadeout 2.0
        play music "audio/normal.mp3" fadein 1
        scene гостиная with slowdissolve
        "На улице уже стемнело. В этот поздний час в комнате царила тишина, нарушаемая лишь редким шорохом страниц."
        "Слабый свет настольной лампы создавал ощущение покоя."
        "Парень внезапно решил прервать тишину, отложив книгу в сторону."
        show p at right with fastdissolve
        p norm "Курьер опаздывает уже на 4 минуты."
        show bro surprised at left with fastdissolve
        bro "..."
        p e "Что?"
        bro"Твоя пунктуальность меня пугает, ты точно ненормальный."
        "Старший кинул равнодушный взгляд в сторону брата."
        p norm"Поаккуратнее со словами."
        show bro angry
        show p
        p "Успокойся, ты выглядишь смешно, когда злишься или что это на твоём лице?"
        show bro sm
        bro "Иди на хер)"
        "Обстановка в комнате накалялась с каждой секундой."  
        play sound "audio/knocking.mp3"
        show p norm
        show bro norm
        "Их спор прервал стук в дверь."
        show bro sm2
        show p norm
        bro "Ураааа еда!"
        scene гостиная with fastdissolve
        "В срочном порядке брат поспешил к входной двери."

        scene дверь with dissolve 
        "Младший брат взялся за дверную ручку.."
        "...Лучше бы он этого не делал."
        play sound "audio/skrip.mp3"
        scene дверь открыта  with slowdissolve
        "Открыв дверь, он увидел вовсе не курьера."
        show bro shock at left with fastdissolve 
        "На лице брата сперва появился шок."
        stop music fadeout 2.0
        show bro horrified
        "Затем его захватил непередаваемый ужас."
        play sound "audio/scream.mp3"
        bro "АААААААА!!!!!"
        play sound "audio/hand.mp3"
        scene дверь рука 
        "В полумраке резко возникла чья-то рука."
        play music "audio/tiktok.mp3" fadein 1
        "Парень едва успел отступить. Еще секунда - и полусгнившие пальцы сжались бы на его шее."
        show p an at right with fastdissolve
        p an "..."
        p an "Какого хре—"
        "Не успел он закончить мысль, как из дверного проема показалось...нечто."
        scene дверь открыта with fade
        window hide
        play sound "audio/zombie.mp3"
        show зомби 1 with fastdissolve
        pause 2.0
        window show
        "Нечеловеческий крик был оглушительным."
        "Существо, появившееся в коридоре, заставило содрогнуться все тело."
        "Никогда он не видел ничего подобного."
        hide зомби 1
        show bro horrified
        "Он уже собирлся уносить ноги, как вдруг заметил, что его брат стоит как приклеенный."
        hide bro
        show p an
        p "ТЫ ЧЁ ВТАЛ ПРИДУРОШНЫЙ, БЕЖИМ!!!!"
        scene black with fastdissolve
        "Едва не вывернув запястье брату, парень помчался к ближайшей двери, ведущей в подвал."
        "Влетев туда, чудом не свалившись с лестницы, они одновременно захлопнули дверь."
        play sound "audio/Добавления/komod.mp3"
        "Парень павалил комод одним движением руки, тем самым забарикодировав дверь."
        "Быстрые шаги монстра раздались совсем рядом. Времени на раздумья не было."
        scene подвал with fade
        show bro horrified at left with fastdissolve
        bro "Это что...зомби..?"
        "Последнее слово он произнес неверящим полушепотом."
        show p at right with fastdissolve
        p "Ха...ну хоть что-то веселое за эти выходные"
        bro "..."
        show bro dead
        bro "Какого хрена вообще?!"
        scene подвал with fade
        show синдзи at truecenter with dissolve
        play sound "audio/уведа.mp3"
        $ sindzi.grant()
        "Упав на стул и согнувшись в три погибели, парень завыл."
        hide синдзи with dissolve
        "Он был на грани истерики."
        "Но сейчас было не до нее."
        '"Тварь" была уже близко.'
        "Зомби от людей разделял лишь камод с рухлядью."
    
        scene black 
        show p power at truecenter with fade #Имба

        scene подвал with fade
        show p an with fastdissolve
        p "(Я размазжу голову этой твари.)"
        p "(Или своему брату, если он не прикратит истерить.)"
        p "(Свернуть голову голыми руками так себе затея.)"
        p "(Нужно отыскть что-нибудь, чем можно обороняться.)"
        show p 
        p "Сделай что-нибудь полезное успокойся и поищи чем будешь защищаться."
        bro "..."
        p e "Если тебя сожрут пеняй  на себя."
        "Брат не сдвинулся с места."
        show p
        scene подвал with fastdissolve
        "Не тратя больше времени, Психопат ринулся к настенной полке."
        "В доме они оружия не держали, но на стене висели коллекционные катаны."
        window hide
        scene black with fade
        show катаны at truecenter with dissolve
        pause 2.0
        hide катаны with dissolve
        window show
        "За неимением лучшей альтернативы, парень снял их со стены. К его удивлению, они были довольно хорошо заточенны."
        play sound "audio/уведа.mp3"
        $ pweapon.grant()
        scene подвал with fade
        "С момента встречи с зомби прошло менее минуты."
        "Комод не выдержал и дверь распахнулась."
        "Зомби на огромной скорости падал вниз по лестнице - логичное следствие интенсивного проникновения в подвал."
        "Оживший мертвец приземлился в нескольких метрах от брата."
        "Обычный человек после подобных финтов свернул бы шею. Но перед ними был не человек."
        "Зомби накинулся на брата."
        "Тот даже пискнуть не успел."
        show p w hor with fastdissolve
        p "Кха-ха"
        p w cr "Иди сюда ублюдок!"
        scene подвал with deathfade
        "Старший потянулся за оружием, но было позно. Зомби уже расправлялся с братом."
        play sound "audio/Добавления/scream.mp3"
        "На его животе появлялись рваные раны."
        "Душераздирающие вопли заполнили помещение."

        hide p with fade
        window hide
        menu:
            "Убить зомби":
                jump kill_p_1
            
            "Убежать":
                jump run_away_p_1

            "Попробовть спрятаться":
                jump hide_p
        window show

        label kill_p_1:
            scene подвал with fade
            show зомби 1 
            zombie "Кхаааа!!!"
            "Зомби самозабвенно отрывал куски плоти от едва живого юноши."
            "Непохоже, что он торопился: парень еще дышал, оставаясь на краю сознания."
            "Более того, мерзкий нелюдь в своем безудержном порыве даже не заметил парня."
            hide зомби 1
            show p with fastdissolve
            p w an "НУ ЖЕ, ИДИ СЮДА!"
            play sound "audio/рык.mp3"
            zombie "АААРГХ!"
            "Одним перекрестным движением он разрубил тварь на попалам."
            "Две отдельные части чего-то, что раньше было человеком, продолжали биться в конвульсиях."

            scene black 
            show p power at truecenter with fade #Имба
            play music "audio/Добавления/chop.mp3"
            "Он продолжал наносить удары, превращая зомби во что-то кашеподобное. "
            show p w bl cr with deathfade
            "Чуство превосходства затмевало разум, а лицо медлено резала безумная улыбка. "
            stop music fadeout 2.0

            play music "audio/tiktok.mp3" fadein 1 

            play sound "audio/уведа.mp3"
            $ pcraz.grant()
            $ pcrazy+=1
            $ pkill+=1
            "Спустя время Психопат пришел в себя. Опусив взгляд на пол, он увидел бездыханное тело своего брата."
            scene подвал with fade
            scene bro death with dissolve
            window hide
            pause 2.0
            window show
            "Юноша уже не кричал."
            scene подвал with fade
            show p w norm with fastdissolve
            stop music fadeout 2.0
            scene black with fade
            window hide
            pause(2.0)
            scene подвал with fade
            window show
            stop music fadeout 2.0
            play music "audio/normal2.mp3"
            play sound "audio/уведа.mp3"
            $ prevenge.grant()
            "{i}Какое-то время спустя{\i}"
            show p w bl with fastdissolve
            p "Сам виноват, нужно было меньше истерить и найти оружие, сейчас каждый сам за себя."
            "В последний раз взглянув на брата, он, направился к выходу из подвала."

            
            jump saved_p_1



        label run_away_p_1:
            scene подвал with fade
            show зомби 1 
            zombie "Кхаааа!!!"
            "Зомби самозабвенно отрывал куски плоти от едва живого юноши."
            "Непохоже, что он торопился: парень еще дышал, оставаясь на краю сознания."
            "Более того, мерзкий нелюдь в своем безудержном порыве даже не заметил парня."

            "Это был шанс."
            hide зомби 1
            show p w with fastdissolve
            p "(Как бы прискорбно не было, нужно уносить ноги.)"
            p "(А братец мне в этом поможет.)"
            p "(Побудет приманкой, так хоть какая-то польза от него.)"
            scene black with fade
            "Психопат в последний раз взглянул в глаза брата."
            "Болезненный стон, совсем тихий. Жизнь покидала его."
            scene bro death with dissolve
            "Глаза брата судорожно вглядывались в глаза Психопата."
            "Но ничего не отозвалось в душе, отвернувшись, он вышел за дверь."
            scene подвал with fade
            show p w bl with fastdissolve
            "Какое ему дело до мертвых..."
            play sound "audio/уведа.mp3"
            $ pbitch.grant()
            "...ну почти мертвых."
            $ palone+=1

            jump saved_p_1


        label hide_p:
            scene подвал with fade
            show зомби 1 
            zombie "Кхаааа!!!"
            "Зомби самозабвенно отрывал куски плоти от едва живого юноши."
            "Непохоже, что он торопился: парень еще дышал, оставаясь на краю сознания."
            "Более того, мерзкий нелюдь в своем безудержном порыве даже не заметил парня."

            "Но это не значит, что он не заметит его позже."

            hide зомби 1
            show p w hor with fastdissolve
            p "(Боже...)"
            p w hor  "(Как же страшно!)"
            "Истошные вопли брата становились все тише. Теперь только болезненные всхлипы эхом проносились по сырому подвалу."
            p w hor "..."
            p "(Я не хочу так страдать.)"
            scene black with fade
            "Ноги отказывались его слушаться."
            "Он не грезил о побеге - ноги его не держат."
            "Значит - надо спрятаться. Затаиться."
            "Парень еще раз просканировал комнату."
            "..."
            "Ничего."
            "Ему негде спрятаться."
            "..."
            "....."
            "........."
            "Через какое-то время зомби заметил его."
            play sound "audio/уведа.mp3"
            $ pmraz.grant()
            "В подвале стало на один хладный труп больше."

            jump dead_end





        label saved_p_1:
            if pkill == 1:
                jump after_1_bl_p
        
            else:
                jump after_1_p
        return









        label after_1_bl_p:
            scene дверь открыта with fade
            show p w bl with fastdissolve
            p w bl norm "(Впервые я почуствовал себя в своей тарелке.)"
            p w bl "(Ха-ха убивать проще чем я думал.)"
            p w bl norm "(Нужно убираться из дома, пока не появились ему подобные.)"
            show p w bl e
            play sound "audio/желудок.mp3"
            "В животе заурчало."
            p w bl norm "(Может, я успею взять немного еды?)"
            p w bl norm "(...Хотя другие зомби могут ворваться в любой момент..)"
            hide p with fade
            window hide
            menu:
                "Взять еды":
                    jump bl_with_food_p
                
                "Побыстрее уйти":
                    jump bl_no_food_p
            window show

        label bl_with_food_p:
            $ pfood += 1
            scene кухня with fade
            "Лунный свет пробивался через окно."
            "Была уже глубокая ночь."
            show p w bl norm with fastdissolve
            p "(Возьму только самое необходимое.)"
            hide p with fastdissolve
            "Быстро скидав в сумку какие-то консервы, снэки и бутылку воды, Психопат поспешил к выходу."
            play sound "audio/уведа.mp3"
            $ food.grant()
            "..."
            "А куда пойдем?"
            window hide


            menu:
                "Выйти через парадную дверь":
                    jump bl_front_door_p
                
                "Выйти через заднюю дверь":
                    jump bl_back_door_p
            window show


        label bl_no_food_p:
            show p w bl e with fastdissolve
            p "(Организму придется потерпеть.)"
            p w bl e "(Эти твари могут нагрянуть в любой момент.)"
            p w bl e "(Выйти через эту дверь или пойти через черный ход..?)"
            hide p with fastdissolve

            window hide


            menu:
                "Выйти через парадную дверь":
                    jump bl_front_door_p
                
                "Выйти через заднюю дверь":
                    jump bl_back_door_p
            window show



        label bl_front_door_p:
            scene дверь открыта with fade
            show p w bl with fastdissolve
            "Стараясь не издавать лишнего шума, он уже почти добрался до двери."
            show p w bl hor
            "Как вдруг..."
            scene дверь открыта
            play sound "audio/zombie.mp3"
            show зомби мэн with deathfade
            zombie "ХАГГХААГХ!!!!!"
            scene black with fade
            "Зомби быстро расправился с парнем."
            jump dead_end
            


        label bl_back_door_p:
            scene черный ход with fade
            show p w bl norm with fastdissolve
            p "Дома теперь небезопасно."
            p w bl e "Нужно найти надежное место."
            scene black with fade
            "Психопат покинул дом, не чуствуя никакой досады на этот счёт."
            jump bl_street_p
            

            
        label after_1_p:
            scene дверь открыта with fade
            show p w with fastdissolve
            p w norm "(Теперь мир изменился, выживают сильнейшие.)"
            p w "(Хм больше никаких моральных норм. Интересно куда это приведет человечство, если от него что-то останется конечно.)"
            p w norm "(Нужно убираться из дома, пока не появились ему подобные.)"
            show p w e
            play sound "audio/желудок.mp3"
            "В животе заурчало."
            p w norm "(Может, я успею взять немного еды?)"
            p w norm "(...Хотя другие зомби могут ворваться в любой момент..)"
            hide p with fade
            window hide
            menu:
                "Взять еды":
                    jump with_food_p
                
                "Побыстрее уйти":
                    jump no_food_p
            window show

        label with_food_p:
            $ pfood += 1
            scene кухня with fade
            "Лунный свет пробивался через окно."
            "Была уже глубокая ночь."
            show p w norm with fastdissolve
            p "(Возьму только самое необходимое.)"
            hide p with fastdissolve
            "Быстро скидав в сумку какие-то консервы, снэки и бутылку воды, Психопат поспешил к выходу."
            play sound "audio/уведа.mp3"
            $ food.grant()
            "..."
            "А куда пойдем?"
            window hide


            menu:
                "Выйти через парадную дверь":
                    jump front_door_p
                
                "Выйти через заднюю дверь":
                    jump back_door_p
            window show


        label no_food_p:
            show p w e with fastdissolve
            p "(Организму придется потерпеть.)"
            p w e "(Эти твари могут нагрянуть в любой момент.)"
            p w e "(Выйти через эту дверь или пойти через черный ход..?)"
            hide p with fastdissolve

            window hide


            menu:
                "Выйти через парадную дверь":
                    jump front_door_p
                
                "Выйти через заднюю дверь":
                    jump back_door_p
            window show



        label front_door_p:
            scene дверь открыта with fade
            show p w with fastdissolve
            "Стараясь не издавать лишнего шума, он уже почти добрался до двери."
            show p w hor
            "Как вдруг..."
            scene дверь открыта
            play sound "audio/zombie.mp3"
            show зомби мэн with deathfade
            zombie "ХАГГХААГХ!!!!!"
            scene black with fade
            "Зомби быстро расправился с парнем."
            jump dead_end
            


        label back_door_p:
            scene черный ход with fade
            show p w norm with fastdissolve
            p "Дома теперь небезопасно."
            p w e "Нужно найти надежное место."
            scene black with fade
            "Психопат покинул дом, не чуствуя никакой досады на этот счёт."
            jump street_p

        
        label street_p:
            stop music fadeout 2.0
            scene street with fade
            play music "audio/piano.mp3"
            show p w with fastdissolve
            p w "(Хмм на улице тихо.)"
            p w e "(Зомби поблизости не видать.)"
            p w "(Стоять на месте тоже не вариант.)"
            show p w norm
            play sound "audio/shout.mp3"
            "Вдруг послышался истошный крик."
            "Психопат повернулся к источнику шума."
            "Из-за угла доносились отчаянные женские вопли."
            p w cr "(Не мои проблемы, но итерес берет свое.)"
            scene street with fastdissolve
            "Парень решил поближе подобраться к источнику звука."
            scene tree with fade
            "За углом показалась аллея."
            "На одном из деревьев девушка спасалась от зомби. Она вскорабкалась на дерево, а зомби нетерпелось ее достать."
            show girl with fastdissolve
            girl cry "На помощь!!!"
            girl cry "Пожалуйста...помогите мне!....Кто-нибудь..?!"
            hide girl
            show zombie
            play sound "audio/рык.mp3"
            zombie "ХАААРГХ!"
            hide zombie
            show girl shock 
            girl shock "..."
            scene black 


            scene tree with fade
            show p w with fastdissolve
            p w hor "(Помочь ей?)"
            p w e "(Можно потом шантажировать ее спасением.)"
            p w cr"(Или использовать при удобном случае как приманку.)"
            p w norm "(Хотя нужна ли эта лишняя возьня?)"

            



            hide p with fastdissolve

            window hide


            menu:
                "Отвлечь зомби":
                    jump distract_p
                
                "Убить зомби":
                    jump slaughter_p

                "Пройти мимо":
                    jump mimo_p
            window show


        
        label distract_p:
            if pfood == 1:
                jump distract_suc_p
            else:
                jump distract_fail_p




        label distract_suc_p:                    
            scene tree with fade
            show p w norm
            p w "(Ладно, она может пригодиться, попробую отвлечь зомби... Но как?)"
            p w "(В прошлый раз тот почти не обратил на меня внимания.)"
            p w e "(Кажется, я взял консервы из дома.)"
            p w norm "(Кину их подальше, авось он заинтересуется.)"
            p w an "..."
            p w an "(В целом, если что-то пойдет не так, я убью их обоих.)"
            hide p with fastdissolve
            "Одним движением Психопат открыл консерву и с размаху бросил."
            play sound "audio/conserva.mp3"
            "Баночка с громким лязгом упала на приличном расстоянии от дерева."
            "....."
            scene tree1 with fade
            "Успех! Зомбак рванул на звук, оставляя девушку в покое."
            show girl with fastdissolve
            girl shock "А?"
            hide girl
            "Устремив взгляд в сторону, откуда прилетела банка, девушка увидела своего спасителя."
            show p w
            p w an "{i}Так и будешь стоять, пока он снова не возьмется за тебя?{\i}"
            hide p 
            show girl sm2
            girl shock "!"
            hide girl
            "Девушка поспешила слезть с дерева и побежала к парню."
            $ pmental+=1

            scene street with fade

            show p w with fastdissolve
            p w e "Успел укусить?"
            hide p w e
            show girl with fastdissolve
            girl "НЕТ...честно."
            girl sm "Спасибо тебе. Я думала, это конец."
            girl sm "Меня зовут Лайла."
            girl "..."
            show girl
            l "У тебя есть план? Что нам теперь делать?"
            hide girl
            show p w with fastdissolve
            p w "Можем, конечно, погулять под лунной и стать чьим-то ужином или найти укрытие."
            p w e "Что выберешь?"
            hide p
            show girl an
            l "Сарказм сейчас вовсе не к месту."
            l "И вообще у меня есть идея!"
            hide girl
            show p w 
            p w cr "Весь во внимании."
            hide p
            show girl an
            l"Банк. Там охрана и надежные двери. Остается надеяться, что зомби нет внутри."

            scene black with fade

            "Молодые люди поспешили в сторону банка. На их счастье, зомби они не встретили." 
            "Когда они подошли к зданию, то обнаружили, что дверь заперта."
            "..."
            l "Черт!"
            p "Скорее всего охраник решил вздремнуть, ну или он уже стал одной из этих тварей. "
            "Лейла, если бы могла, точно пропилила бы дырку в собеседнике своим взглядом."
            l "Тогда он бы не стал закрываться, нужно привлечь его внимание."
            "Девушка начала долбиться в дверь."
            play sound "audio/уведа.mp3"
            $ door.grant()
            "..."
            "Тишина."
            "Затем они обнаружили кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            l "Пожалуйста, помогите нам!"
            voice "..."
            voice "Что у вас случилось?"
            p "Нет времени объяснять! Сначала впустите нас."
            l "Мне кажется, они уже близко!!!"
            voice "Опять наркоши что-ли. Объясните, что случилось."
            l "ОТКРОЙТЕ ДВЕРЬ!"
            "Послышался усталый вздох. Затем прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."
            $ pmanip+=1

            
            jump bank_with_girl_p



        label distract_fail_p:
            scene tree with fade
            show p w 
            p w "(Ладно, она может пригодиться, попробую отвлечь зомби... Но как?)"
            p w "(В прошлый раз тот почти не обратил на меня внимания.)"
            p w "(Так...Ну вот камень лежит.)"
            p w e "(Брошу его, может зомби с девушки на него переключится.)"
            p w an "..."
            p w an "(Я сейчас сильно рискую.)"
            p w e"(Хотя мне плевать, глвное, чтобы на меня не кинулся)"
            hide p with fastdissolve
            "Парень со всей силы бросил камень."
            play sound "audio/rock.mp3"
            "Камень упал на приличном расстоянии от дерева."
            "....."
            "Зомби он, по-видимому, не заинтересовал."
            show p w norm with fastdissolve
            p w an "Черт!"
            hide p
            "Девушка с дерева увидела парня."
            show girl shock with fastdissolve
            girl shock "ЭЭЭЙ!!! ПОМОГИ МНЕ!!!"
            girl cry "Ну что ты стоишь там?! Сделай что-нибудь! Пожалуйста.."
            hide girl 
            show p w an
            p w an "(Чтож поговорка : не делай добра - не получишь зла, оказалась как никогда верной. )"
            hide p
            "Теперь зомби интересовал Психопат."
            "Видя в парне более легкую добычу, мертвец бросился в его сторону."
            "Девушка на дереве, в свою очередь, поспешила слезть и рванула в противоположном направлении."
            scene black with fade
            play sound "audio/Добавления/levi.mp3"
            p "БЛ#@$!!!!!"
            "Он отпрянул назад, чтобы выйграть время и достать оружие."
            "Идиотка, лучше бы не помогал."
            show p power at truecenter with fade
            "Я убью этого зомби и эту истиричку, если она не подохнет сама до этого врмени!"
            play music "audio/killbill.mp3"
            "Психопат делает шаг в сторону, уклоняясь от атаки, и наносит быстрый горизонтальный удар катаной, разрубая зомби по плечу. Но тот продолжает двигаться."
            play sound "audio/Добавления/ранение.mp3"
            "Зомби резко бросается вперед и царапает парня по ноге своими когтями. Психопат падает на одно колено, чувствуя резкую боль."
            play sound "audio/Добавления/ярость.mp3"
            "Собрав всю свою ярость, парень поднимается и делает вертикальный удар катаной, разрубая зомби пополам. Его враг падает замертво."
            play sound "audio/уведа.mp3"
            $ phurt.grant()
            scene black with fade
            stop music fadeout 2.0

            play music "audio/напряг2.mp3" fadein 1 
            "Единственное, что приходит в голову это банк. Там прочные двери и охрана, а значит шанс выжить больше." 
            "Когда он подошел к зданию, то обнаружил, что дверь заперта."
            p "(Это же банк. Там должен быть охранник на смене.)"
            "Парень со всей дури постучал в дверь."
            play sound "audio/уведа.mp3"
            $ door.grant()
            "..."
            "Тишина."
            "Затем он обнаружил кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            p "Откройте дверь!"
            voice "..."
            voice "Что у вас случилось?"
            p "Нет времени объяснять! Сначала впустите меня!"
            voice "Парень, спокойно. Объясни, что случилось."
            p "ПРОСТО ОТКРОЙТЕ ДВЕРЬ!"
            "Послышался усталый вздох. Затем прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."

            $ phealth+=1
            $ pcrazy+=1
            $ pmental+=1
            jump bank_alone_p




            

        label slaughter_p:
            scene tree with fade
            show p w with fastdissolve
            p w "(Ладно, она может пригодиться, нужно достать ее с дерева.)"
            p w "(Осталось просто прикончить тварь и готово.)"
            p w an "..."
            p w an "(В целом, если что-то пойдет не так, я убью их обоих.)"
            scene tree with fastdissolve
            show p power at truecenter with fade
            show p w cr with fastdissolve
            "Легким движением достав катаны, Психопат ринулся навстречу зомби с безумной улыбкой на лице."
            play sound "audio/Добавления/ранение.mp3"
            "Он тихо подкрадывался к мертвецу. Одним взмахом парень лишил врага головы."
            hide p
            show girl shock with fastdissolve
            girl cry "Боже..."
            hide girl

            show p w with fastdissolve
            p w e "Успел укусить?"
            hide p w e
            show girl with fastdissolve
            girl "НЕТ...честно."
            girl sm "Спасибо тебе. Я думала, это конец."
            girl sm "Меня зовут Лайла."
            girl "..."
            l "У тебя есть план? Что нам теперь делать?"
            hide girl
            show p w with fastdissolve
            p w "Можем, конечно, погулять под лунной и стать чьим-то ужином или найти укрытие."
            p w e "Что выберешь?"
            hide p
            show girl an
            l "Сарказм сейчас вовсе не к месту."
            l "И вообще у меня есть идея!"
            hide girl
            show p w 
            p w cr "Весь во внимании."
            hide p
            show girl an
            l"Банк. Там охрана и надежные двери. Остается надеяться, что зомби нет внутри."

            scene black with fade

            "Молодые люди поспешили в сторону банка. На их счастье, зомби они не встретили." 
            "Когда они подошли к зданию, то обнаружили, что дверь заперта."
            "..."
            l "Черт!"
            p "Скорее всего охраник решил вздремнуть, ну или он уже стал одной из этих тварей. "
            "Лейла, если бы могла, точно пропилила бы дырку в собеседнике своим взглядом."
            l "Тогда он бы не стал закрываться, нужно привлечь его внимание."
            "Девушка начала долбиться в дверь."
            play sound "audio/уведа.mp3"
            $ door.grant()
            "..."
            "Тишина."
            "Затем они обнаружили кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            l "Пожалуйста, помогите нам!"
            voice "..."
            voice "Что у вас случилось?"
            p "Нет времени объяснять! Сначала впустите нас."
            l "Мне кажется, они уже близко!!!"
            voice "Опять наркоши что-ли. Объясните, что случилось."
            l "ОТКРОЙТЕ ДВЕРЬ!"
            "Послышался усталый вздох. Затем прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."
            $ pmanip+=1
            $ pcrazy+=1
            $ pmental+=1

                
            jump bank_with_girl_p





        label mimo_p:
            scene tree with fade 
            show p w with fastdissolve
            p w cr"(Хм...так все равно, что даже немного стыдно.)"
            p w "(Я брата то не сильно спасал, а тут вообще незнакомка.)"
            p w e "(Что в прошлый раз, что сейчас.. Мне прсто плевать на других, мне неизвестно чуство сострадания. Такой я человек.)"
            play sound "audio/уведа.mp3"
            $ ppohui.grant()
            "Психопат развернулся и пошел в противоположном направлении от парка."
            scene street with fade
            show p w with fastdissolve
            p w norm"(Надо решить, что делать дальше.)"
            p w e"(Приоритетная задача - найти укрытие.)"
            p w e "(Рядом есть банк, есть смысл попытаться, там как никак прочнее двери, чем в любом из домов.)"
            
            scene black with fade
            "Дернул за ручку. Заперто."
            p "(Это же банк. Там должен быть охранник на смене.)"
            "Парень со всей дури постучал в дверь."
            play sound "audio/уведа.mp3"
            $ door.grant()
            "..."
            "Тишина."
            "Затем он обнаружил кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            p "Откройте дверь!"
            voice "..."
            voice "Что у вас случилось?"
            p "Нет времени объяснять! Сначала впустите меня!"
            voice "Парень, спокойно. Объясни, что случилось."
            p "ПРОСТО ОТКРОЙТЕ ДВЕРЬ!"
            "Послышался усталый вздох. Затем прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."
            $ palone+=1
            
            jump bank_alone_p





        label bl_street_p:
            stop music fadeout 2.0
            scene street with fade
            play music "audio/piano.mp3"
            show p w bl with fastdissolve
            p w bl "(Хмм на улице тихо.)"
            p w bl e "(Зомби поблизости не видать.)"
            p w bl "(Стоять на месте тоже не вариант.)"
            show p w bl norm
            play sound "audio/shout.mp3"
            "Вдруг послышался истошный крик."
            "Психопат повернулся к источнику шума."
            "Из-за угла доносились отчаянные женские вопли."
            p w bl cr "(Не мои проблемы, но итерес берет свое.)"
            scene street with fastdissolve
            "Парень решил поближе подобраться к источнику звука."
            scene tree with fade
            "За углом показалась аллея."
            "На одном из деревьев девушка спасалась от зомби. Она вскорабкалась на дерево, а зомби нетерпелось ее достать."
            show girl with fastdissolve
            girl cry "На помощь!!!"
            girl cry "Пожалуйста...помогите мне!....Кто-нибудь..?!"
            hide girl
            show zombie
            play sound "audio/рык.mp3"
            zombie "ХАААРГХ!"
            hide zombie
            show girl shock 
            girl shock "..."
            scene black 


            scene tree with fade
            show p w bl with fastdissolve
            p w bl hor "(Помочь ей?)"
            p w bl e "(Можно потом шантажировать ее спасением.)"
            p w bl cr"(Или использовать при удобном случае как приманку.)"
            p w bl norm "(Хотя нужна ли эта лишняя возьня?)"

            



            hide p with fastdissolve

            window hide


            menu:
                "Отвлечь зомби":
                    jump distract_p_bl
                
                "Убить зомби":
                    jump slaughter_p_bl

                "Пройти мимо":
                    jump mimo_p_bl
            window show


        
        label distract_p_bl:
            if sfood == 1:
                jump distract_suc_p_bl
            else:
                jump distract_fail_p_bl
        return



        label distract_suc_p_bl:                    
            scene tree with fade
            show p w bl norm
            p w bl "(Ладно, она может пригодиться, попробую отвлечь зомби... Но как?)"
            p w bl"(В прошлый раз тот почти не обратил на меня внимания.)"
            p w bl e "(Кажется, я взял консервы из дома.)"
            p w bl norm "(Кину их подальше, авось он заинтересуется.)"
            p w bl an "..."
            p w bl an "(В целом, если что-то пойдет не так, я убью их обоих.)"
            hide p with fastdissolve
            "Одним движением Психопат открыл консерву и с размаху бросил."
            play sound "audio/conserva.mp3"
            "Баночка с громким лязгом упала на приличном расстоянии от дерева."
            "....."
            scene tree1 with fade
            "Успех! Зомбак рванул на звук, оставляя девушку в покое."
            show girl with fastdissolve
            girl shock "А?"
            hide girl
            "Устремив взгляд в сторону, откуда прилетела банка, девушка увидела своего спасителя."
            show p w
            p w bl an "{i}Так и будешь стоять, пока он снова не возьмется за тебя?{\i}"
            hide p 
            show girl sm2
            girl shock "!"
            hide girl
            "Девушка поспешила слезть с дерева и побежала к парню."
            $ pmental+=1

            scene street with fade

            show p w bl with fastdissolve
            p w bl e "Успел укусить?"
            hide p w bl e
            show girl with fastdissolve
            girl "НЕТ...честно."
            girl sm "Спасибо тебе. Я думала, это конец."
            girl sm "Меня зовут Лайла."
            girl "..."
            show girl
            l "У тебя есть план? Что нам теперь делать?"
            hide girl
            show p w bl with fastdissolve
            p w bl "Можем, конечно, погулять под лунной и стать чьим-то ужином или найти укрытие."
            p w bl e "Что выберешь?"
            hide p
            show girl an
            l "Сарказм сейчас вовсе не к месту."
            l "И вообще у меня есть идея!"
            hide girl
            show p w bl 
            p w bl cr "Весь во внимании."
            hide p
            show girl an
            l"Банк. Там охрана и надежные двери. Остается надеяться, что зомби нет внутри."

            scene black with fade

            "Молодые люди поспешили в сторону банка. На их счастье, зомби они не встретили." 
            "Когда они подошли к зданию, то обнаружили, что дверь заперта."
            "..."
            l "Черт!"
            p "Скорее всего охраник решил вздремнуть, ну или он уже стал одной из этих тварей. "
            "Лейла, если бы могла, точно пропилила бы дырку в собеседнике своим взглядом."
            l "Тогда он бы не стал закрываться, нужно привлечь его внимание."
            "Девушка начала долбиться в дверь."
            play sound "audio/уведа.mp3"
            $ door.grant()
            "..."
            "Тишина."
            "Затем они обнаружили кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            l "Пожалуйста, помогите нам!"
            voice "..."
            voice "Что у вас случилось?"
            p "Нет времени объяснять! Сначала впустите нас."
            l "Мне кажется, они уже близко!!!"
            voice "Опять наркоши что-ли. Объясните, что случилось."
            l "ОТКРОЙТЕ ДВЕРЬ!"
            "Послышался усталый вздох. Затем прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."
            $ pmanip+=1

            
            jump bl_bank_with_girl_p



        label distract_fail_p_bl:
            scene tree with fade
            show p w bl
            p w bl "(Ладно, она может пригодиться, попробую отвлечь зомби... Но как?)"
            p w bl "(В прошлый раз тот почти не обратил на меня внимания.)"
            p w bl "(Так...Ну вот камень лежит.)"
            p w bl e "(Брошу его, может зомби с девушки на него переключится.)"
            p w bl an "..."
            p w bl an "(Я сейчас сильно рискую.)"
            p w bl e"(Хотя мне плевать, глвное, чтобы на меня не кинулся)"
            hide p with fastdissolve
            "Парень со всей силы бросил камень."
            play sound "audio/rock.mp3"
            "Камень упал на приличном расстоянии от дерева."
            "....."
            "Зомби он, по-видимому, не заинтересовал."
            show p w norm with fastdissolve
            p w bl an "Черт!"
            hide p
            "Девушка с дерева увидела парня."
            show girl shock with fastdissolve
            girl shock "ЭЭЭЙ!!! ПОМОГИ МНЕ!!!"
            girl cry "Ну что ты стоишь там?! Сделай что-нибудь! Пожалуйста.."
            hide girl 
            show p w bl an
            p w bl an "(Чтож поговорка : не делай добра - не получишь зла, оказалась как никогда верной. )"
            hide p
            "Теперь зомби интересовал Психопат."
            "Видя в парне более легкую добычу, мертвец бросился в его сторону."
            "Девушка на дереве, в свою очередь, поспешила слезть и рванула в противоположном направлении."
            scene black with fade
            play sound "audio/Добавления/levi.mp3"
            p "БЛ#@$!!!!!"
            "Он отпрянул назад, чтобы выйграть время и достать оружие."
            "Идиотка, лучше бы не помогал."
            show p power at truecenter with fade
            "Я убью этого зомби и эту истиричку, если она не подохнет сама до этого врмени!"
            play music "audio/killbill.mp3"
            "Психопат делает шаг в сторону, уклоняясь от атаки, и наносит быстрый горизонтальный удар катаной, разрубая зомби по плечу. Но тот продолжает двигаться."
            play sound "audio/Добавления/ранение.mp3"
            "Зомби резко бросается вперед и царапает парня по ноге своими когтями. Психопат падает на одно колено, чувствуя резкую боль."
            play sound "audio/Добавления/ярость.mp3"
            "Собрав всю свою ярость, парень поднимается и делает вертикальный удар катаной, разрубая зомби пополам. Его враг падает замертво."
            play sound "audio/уведа.mp3"
            $ phurt.grant()
            scene black with fade
            stop music fadeout 2.0

            play music "audio/напряг2.mp3" fadein 1 
            "Единственное, что приходит в голову это банк. Там прочные двери и охрана, а значит шанс выжить больше." 
            "Когда он подошел к зданию, то обнаружил, что дверь заперта."
            p "(Это же банк. Там должен быть охранник на смене.)"
            "Парень со всей дури постучал в дверь."
            play sound "audio/уведа.mp3"
            $ door.grant()
            "..."
            "Тишина."
            "Затем он обнаружил кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            p "Откройте дверь!"
            voice "..."
            voice "Что у вас случилось?"
            p "Нет времени объяснять! Сначала впустите меня!"
            voice "Парень, спокойно. Объясни, что случилось."
            p "ПРОСТО ОТКРОЙТЕ ДВЕРЬ!"
            "Послышался усталый вздох. Затем прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."

            $ phealth+=1
            $ pcrazy+=1
            $ pmental+=1
            jump bl_bank_alone_p




            

        label slaughter_p_bl:
            scene tree with fade
            show p w bl with fastdissolve
            p w bl "(Ладно, она может пригодиться, нужно достать ее с дерева.)"
            p w bl "(Осталось просто прикончить тварь и готово.)"
            p w bl an "..."
            p w bl an "(В целом, если что-то пойдет не так, я убью их обоих.)"
            scene tree with fastdissolve
            show p power at truecenter with fade
            show p w bl cr with fastdissolve
            "Легким движением достав катаны, Психопат ринулся навстречу зомби с безумной улыбкой на лице."
            play sound "audio/Добавления/ранение.mp3"
            "Он тихо подкрадывался к мертвецу. Одним взмахом парень лишил врага головы."
            hide p
            show girl shock with fastdissolve
            girl cry "Боже..."
            hide girl

            show p w bl with fastdissolve
            p w bl e "Успел укусить?"
            hide p w bl e
            show girl with fastdissolve
            girl "НЕТ...честно."
            girl sm "Спасибо тебе. Я думала, это конец."
            girl sm "Меня зовут Лайла."
            girl "..."
            show girl
            l "У тебя есть план? Что нам теперь делать?"
            hide girl
            show p w with fastdissolve
            p w bl "Можем, конечно, погулять под лунной и стать чьим-то ужином или найти укрытие."
            p w bl e "Что выберешь?"
            hide p
            show girl an
            l "Сарказм сейчас вовсе не к месту."
            l "И вообще у меня есть идея!"
            hide girl
            show p w 
            p w bl cr "Весь во внимании."
            hide p
            show girl an
            l"Банк. Там охрана и надежные двери. Остается надеяться, что зомби нет внутри."

            scene black with fade

            "Молодые люди поспешили в сторону банка. На их счастье, зомби они не встретили." 
            "Когда они подошли к зданию, то обнаружили, что дверь заперта."
            "..."
            l "Черт!"
            p "Скорее всего охраник решил вздремнуть, ну или он уже стал одной из этих тварей. "
            "Лейла, если бы могла, точно пропилила бы дырку в собеседнике своим взглядом."
            l "Тогда он бы не стал закрываться, нужно привлечь его внимание."
            "Девушка начала долбиться в дверь."
            play sound "audio/уведа.mp3"
            $ door.grant()
            "..."
            "Тишина."
            "Затем они обнаружили кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            l "Пожалуйста, помогите нам!"
            voice "..."
            voice "Что у вас случилось?"
            p "Нет времени объяснять! Сначала впустите нас."
            l "Мне кажется, они уже близко!!!"
            voice "Опять наркоши что-ли. Объясните, что случилось."
            l "ОТКРОЙТЕ ДВЕРЬ!"
            "Послышался усталый вздох. Затем прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."
            $ pmanip+=1
            $ pcrazy+=1
            $ pmental+=1

                
            jump bl_bank_with_girl_p





        label mimo_p_bl:
            scene tree with fade 
            show p w bl with fastdissolve
            p w bl cr"(Хм...так все равно, что даже немного стыдно.)"
            p w bl "(Я брата то не сильно спасал, а тут вообще незнакомка.)"
            p w bl e "(Что в прошлый раз, что сейчас.. Мне прсто плевать на других, мне неизвестно чуство сострадания. Такой я человек.)"
            play sound "audio/уведа.mp3"
            $ ppohui.grant()
            "Психопат развернулся и пошел в противоположном направлении от парка."
            scene street with fade
            show p w with fastdissolve
            p w bl norm"(Надо решить, что делать дальше.)"
            p w bl e"(Приоритетная задача - найти укрытие.)"
            p w bl e "(Рядом есть банк, есть смысл попытаться, там как никак прочнее двери, чем в любом из домов.)"
            
            scene black with fade
            "Дернул за ручку. Заперто."
            p "(Это же банк. Там должен быть охранник на смене.)"
            "Парень со всей дури постучал в дверь."
            play sound "audio/уведа.mp3"
            $ door.grant()
            "..."
            "Тишина."
            "Затем он обнаружил кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            p "Откройте дверь!"
            voice "..."
            voice "Что у вас случилось?"
            p "Нет времени объяснять! Сначала впустите меня!"
            voice "Парень, спокойно. Объясни, что случилось."
            p "ПРОСТО ОТКРОЙТЕ ДВЕРЬ!"
            "Послышался усталый вздох. Затем прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."
            $ palone+=1
            
            jump bl_bank_alone_p





        label bank_with_girl_p:
            scene bank with fade
            "Стоило им зайти внутрь, как тут же они попали под пронзительный взгляд охранника."
            show sec mad with fastdissolve
            sec mad "..."
            hide sec mad
            show p w with fastdissolve
            p w "..."
            hide p w
            show girl shock with fastdissolve
            l shock "..."
            l shock "Понимаете, мы-"
            hide girl
            show sec mad
            sec mad "..."
            hide sec mad
            show girl shock
            l shock "Мы..мы...эмм-м, да. Мы п-попали в сложную ситуацию. Эти..зомби, они-"
            "Девушка нервничала. Под тяжелым взором охранника ей было сложно сформулировать свои мысли."
            hide girl
            show sec
            sec"..."
            sec sm "Что?"
            sec sm "Вы думаете, это очень смешно?"
            sec "Врываться в государственное учреждение и нести бред в мою ночную смену - это такие шуточки у вас?"
            "Взгляд мужчины стал еще мрачнее."
            sec mad "Эй парень, ты вообще откуда сбежал с мечами за спиной?"
            hide sec
            show p w 
            p w cr "Давай на тебе их и обробуем)"
            hide p 
            show girl
            l an "Нет, послушайте, зом-"
            hide girl 
            show sec 
            sec "Он мне еще и угрожать удумал."
            sec "БЫСТРО НА ВЫХОД!"
            hide sec
            show p w an
            p w an "Если вы соизволите посмотреть запись камер наружного наблюдения, сами все поймете."
            p w e "Насколько мне известно это ваша прямая обязанность,а вы в потолок плюете на рабочем месте."
            hide p 
            show sec 
            sec "Моя прямая обязанность - выгонять всяких торчков, как Вы например."
            sec mad "Нечего мне тут про каких-то зомби затирать. Посмеялись и хватит."
            hide sec
            show girl
            l an "..."
            hide girl
            show p w 
            p w cr "Раз такой смелый, сходи сам погляди..."
            p w cr "Если никого не будет, мы просто уйдем, чего тебе стоит..."
            hide p
            show girl
            l shock "Что ты творишь, они ж..."
            hide girl
            show p w 
            p w cr "Давай, тебе же нечего там боятся, мы же все придумали..."
            hide p
            show sec 
            play sound "audio/уведа.mp3"
            $ hod.grant()
            sec "Закрой свой рот, с чего мне верить в ваш бред, мне запрещенно покидать пост!!!"
            hide sec
            show p w
            p w bl "Ха-ха смотри как разозлился, ну же давай, спать тоже запрещенно на рабочем месте."
            l "{i}Господи...{\i}"
            p w bl norm "(Нужно дествовать.)"

            window hide


            menu:
                "Вытащить охраника на улицу":
                    jump negotiation_p
                "Свалить отсюда":
                    jump get_out_p
                "Пришить ублюдка":
                    jump kill_the_bastard_p

            window show


        label negotiation_p:
            $ pmanip+=1
            show p w an with fastdissolve
            p "Где твоя решительность или мне проводить тебя за ручку?!"
            p w an "Пойдем, проведу тебе экскурсию в новый мир!"
            "Психопат начал стемительно сокращать расстояние между ними."
            "Девушка поняла, что это не к добру, а потому отошла в угол, желая испариться в воздухе."
            hide p
            show sec mad
            sec "Иди сюда клоун, я научу тебя манерам."
            hide sec
            play sound "audio/Добавления/fight.mp3"
            show girl cry
            l "Прекратите, выйдете на улицу и будете мертвы через минуту!!!."
            hide girl
            play sound "audio/Добавления/opd.mp3"
            "Психопат оказался сильнее, он буквально выпихнул охраника на улицу."
            show sec mad
            scene street3 with fade
            "Вся злость испарилась в секунду, когда нечто вышло из-за дерева. "
            window hide
            play sound "audio/zombie.mp3"
            show зомби 1 with fastdissolve
            pause 2.0
            window show
            sec "ТВОЮ МАТЬ..."
            scene bank with fade
            hide sec
            show p w cr
            p w cr "Кха-ха-ха-ха это лицо стоило того."
            hide p
            show sec mad 
            sec "Да ты отбитый на голову, смешно ему..."
            hide sec
            "Очередной усталый вздох. Охранник осел на пол и вперил свой взгляд в пол."
            "..."
            sec "..."
            sec mad "В это сложно поверить."
            hide sec
            show p w 
            p w "Такова реальность. Мир уже не тот, каким был вчера."
            hide p 
            show sec mad
            sec mad "Ладно. Хорошо. Видимо, вы правы. Наступил конец света."
            sec mad "Прелестно."
            sec mad "..."
            sec "Ну и что вы предлагаете?"
            hide sec
            show p w 
            p w "Запереть двери и найти еще оружие."
            p w "Побудем здесь какое-то время. В безопасности. А потом, нужно думать как найти провизию."
            hide p
            show girl 
            l "Звучит как толковый план."
            l sm "Останемся здесь на какое-то время."
            hide girl 
            show sec 
            sec "(Сомнительно...)"
            sec "И долго мы тут торчать будем? Еда и вода не бесконечные. Из того, что есть в комнате отдыха, хватит на, дай Бог, 5 дней."
            hide sec
            show p w 
            p w an "Значит кто-то без пайка ха..."
            scene black with fade
            "С господином охранником, все-же, удалось договориться."
            "Трое людей приступили к укреплению их пристанища."
            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show p w with fastdissolve
            p w e "(Чуствую себя неважно...)"
            hide p with fastdissolve
            "Его новые знакомые готовились ко сну."
            "Сегодняшняя ночь всем знатно потрепала нервы."
            jump raspr


        label get_out_p:
            "Терпение Психопата лопнуло."
            "Еще секунда и он прикончит этого охранника."
            show p w 
            p w an "З@ебал ты меня, дядя."
            p w an "Тебе проще верить в то, что все хорошо, ну тогда увидимся на том свете, когда поймешь, что уже поздно."
            hide p
            show sec 
            sec mad "..."
            hide sec
            show p w 
            p w an "Лайла, пошли отсюда. Найдем другое место."
            hide p
            show girl
            l shock "Эмм.."
            l cry "К-куда же мы пойдем? Может, стоит попробовать договориться?"
            hide girl
            show p w
            p w e "Ну, так сама попробуй, а я посмотрю)"
            "Девушка поплелась к выходу."
            p w an "Здесь мы вряд-ли добъемся понимания."
            hide p
            show girl 
            l cry "Но.."
            hide girl
            "Психопат закатил глаза"
            scene black with fade
            "Психопат слишком самоуверенно зашагал по улице."
            "Повернувшись на девушку, которая застыла в дверях, он заметил на ее лице гримасу ужаса."
            "Как вдруг..."
            "Из-за угла резко появился зомби!"
            play sound "audio/Добавления/ранение.mp3"
            "Он не стал церемониться и откусил у парня часть затылка."
            "Вот его песенка и спета."

            jump dead_end 


        label kill_the_bastard_p:
            show p w with fastdissolve
            p w an "(Он - лишь помеха, которую нужно устранить.)"
            hide p
            show sec 
            sec "Ну так вы собираетесь уходить? Или мне применить силу?"
            hide sec
            show girl 
            l shock "Но..."
            hide girl
            show p w 
            p w cr "Пожалуй ты уйдешь сегодня первым..."
            show p power at truecenter with fade
            scene black with fade
            "Он резким движением рассек брюхо мужчине."
            play sound "audio/Добавления/scream.mp3"
            sec "АААААА!!!!СУКАА-АААА!!!!"
            l "ААААА???!!!!!!!!!!! ТЫ ЧТО?!!!"
            "Мужчина орал от боли. Лайла орала от ужаса."
            "Охранник резко достал нож и нанес удар в бедро Психопату."
            scene black with deathfade
            play sound "audio/уведа.mp3"
            $ phurttummy.grant()
            "Для человека, у которого органы на пол пути вниз, сила удара была неожиданная."
            "Психопат схавтился за ногу."
            "По ощущениям, в артерию он не попал, а значит шанс выжить значительно повышается."
            $ shealth += 1 #ранен
            "..."
            "С этим ударом последние силы покинули мужчину."
            "Он обмяк и перестал дышать."

            play sound "audio/уведа.mp3"
            $ crazy.grant()
            "..."

            "Когда Психопат пришл в себя, он заметил на себе потерянный взгляд Лайлы."
            $ pslaughter +=1  #- убила мужика
            $ pcrazy+=1
            p "Теперь все-КХа-кхаа-..хорошо. Мы..мы сможем здесь остаться. Не волнуйся."
            l "..."
            p "Ты же понимаешь, что я должен был это сделать? Или он - или мы."
            l "....."
            p "Лайла."
            l "...? Что?"
            p "Я сделал это для нашей безопасности. Не бойся меня."
            l ".....Я понимаю. Ты прав."
            p "Ты правда понимаешь?"
            l "Да."
            p "Хорошо."

            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show p w with fastdissolve
            p w e "(Чуствую себя неважно...)"
            hide p with fastdissolve
            "Его новая знакомая готовилась ко сну."
            "Сегодняшняя ночь всем знатно потрепала нервы."
            p "А может..."
            



            window hide


            menu:
                "Поговорить с Лайлой":
                    jump talk_layla_p
                "Лечь спать":
                    jump sleep_layla_p
                "Убить ее":
                    jump kill_layla_p

            window show
        


        

        label talk_layla_p:
            show p w with fastdissolve
            p w norm"(Нужно с ней поговорить. Она с тех пор и словечком не обмолвилась.)"
            p w "Лайла?"
            hide p
            show girl
            l "...Да?"
            hide girl
            show p w
            p w "Знаешь, я не хочу, чтобы между нами была недосказанность."
            p w '(Нужно надавить на жалость и попробовать заставить сочуствовать мне.)'
            p w '(Или же отвлечь внимание, если не сработает придётся расправится и с ней.)'
            p w cr '(Ха ей лучше играть по моим правилам.)'
            "Психопат нежно коснулся ее предплечья и заглянул в глаза, под ладонью он почуствовал мелкую дрожь."
            p w "Тебе не меня стоит бояться."
            p w norm "Хотя я тебя полностью понимаю, на моих глазах эти твари убили моего младшего братика."
            p w norm "Я до последнего боролся, но не смог его защитить, понимаешь не смог... я никогда себе не прощу."
            hide p
            show girl cry
            "Девушка опустила плечи и на глазах проступили слезы. "
            hide girl
            show p w cr
            p w cr '(Серьезно? Пару слов и она уже преданее собаки.)'
            p w norm "Когда я встретил тебя, я понял, что это мой шанс...я обязан был защитить твою жизнь."
            p w norm "Чего бы это не стоило."
            hide p
            show girl cry
            play sound "audio/уведа.mp3"
            $ seduct.grant()
            l "Я тебя испугалась, но ты прав...наверное, если бы он нас выгнал, мы бы погибли."
            p w cr "Ну вот и все прияснили, а теперь можно ложится спать."
            scene black with slowdissolve
            $ pmanip+=1

            jump raspr


        label sleep_layla_p:
            show p w with fastdissolve
            p w "(Не буду ее отвлекать. Надо все переварить.)"
            p w "(Тоже попробую поспать.)"
            hide p
            "Он пытался заснуть, но разные навязчивые мысли мешали."
            "Психопат вслушивался в дыхание девушки рядом: оно было ровное, глубокое."
            "В скором времени он провалился в царство Морфея."
            scene black with slowdissolve
            "Вот только не надолго."
            "Пробуждение было ярким."
            scene restroom
            show girl with deathfade
            l an "..."
            hide girl
            play music "audio/piano.mp3"
            "Лайла, этот божий одуванчик...Она пырнула Психопата."
            "Ударила ножом охраника в спину!"
            show p 
            p hor "Лайла..."
            p hor "................."
            p cr "(Нужно было убить эту суку еще в начале.)"

            jump dead_end

        label kill_layla_p:
            show p w with fastdissolve
            play music "audio/Добавления/chop.mp3"
            show p power at truecenter with fade
            p w cr "(Зачем мне лишние проблемы.)"
            p w cr "Ну что Лейла, давай прощаться хах..."
            hide p
            show girl with deathfade
            l shock "Что ты задумал..."
            play sound "audio/Добавления/крик.mp3"
            scene black with fade
            "Она замолчала навсегда."
            $ pcrazy+=1
            jump raspr


        















        label bank_alone_p:
            scene bank with fade
            "Стоило ему зайти внутрь, как тут же он попал под пронзительный взгляд охранника."
            show sec mad with fastdissolve
            sec mad "..."
            hide sec mad
            show p w with fastdissolve
            p w "..."
            hide p w
            sec mad "..."
            hide sec mad
            show p w with fastdissolve
            p w "Если я вам скажу, что по улицам города бегают мертвецы...да, пожалуй, не годится в аргументы"
            hide p w
            show sec
            sec"..."
            sec sm "Что?"
            sec sm "Вы думаете, это очень смешно?"
            sec "Врываться в государственное учреждение и нести бред в мою ночную смену - это такие шуточки у вас?"
            "Взгляд мужчины стал еще мрачнее."
            sec mad "Парень, ты вообще откуда сбежал с мечами за спиной?"
            hide sec
            show p w 
            p w cr "Давай на тебе их и обробуем)"
            hide p 
            show sec 
            sec "Он мне еще и угрожать удумал."
            sec "БЫСТРО НА ВЫХОД!"
            hide sec
            show p w an
            p w an "Если вы соизволите посмотреть запись камер наружного наблюдения, сами все поймете."
            p w e "Насколько мне известно это ваша прямая обязанность,а вы в потолок плюете на рабочем месте."
            hide p 
            show sec 
            sec "Моя прямая обязанность - выгонять всяких торчков, как Вы например."
            sec mad "Нечего мне тут про каких-то зомби затирать. Посмеялись и хватит."
            hide sec
            show p w 
            p w cr "Раз такой смелый, сходи сам погляди..."
            p w cr "Если никого не будет, я просто уйду, чего тебе стоит..."
            hide p
            show p w 
            p w cr "Давай, тебе же нечего там боятся, я же несу бред..."
            hide p
            show sec 
            play sound "audio/уведа.mp3"
            $ hod.grant()
            sec "Закрой свой рот, с чего мне верить в твой бред, мне запрещенно покидать пост!!!"
            hide sec
            show p w
            p w "Ха-ха смотри как разозлился, ну же давай, спать тоже запрещенно на рабочем месте."
            p w norm "(Нужно дествовать.)"

            window hide


            menu:
                "Вытащить охраника на улицу":
                    jump negotiation_a_p
                "Свалить отсюда":
                    jump get_out_a_p
                "Пришить ублюдка":
                    jump kill_the_bastard_a_p

            window show


        label negotiation_a_p:
            $ pmanip+=1
            show p w an with fastdissolve
            p "Где твоя решительность или мне проводить тебя за ручку?!"
            p w an "Пойдем, проведу тебе экскурсию в новый мир!"
            "Психопат начал стемительно сокращать расстояние между ними."
            hide p
            show sec mad
            sec "Иди сюда клоун, я научу тебя манерам."
            hide sec
            play sound "audio/Добавления/fight.mp3"
            play sound "audio/Добавления/opd.mp3"
            "Психопат оказался сильнее, он буквально выпихнул охраника на улицу."
            show sec mad
            scene street3 with fade
            "Вся злость испарилась в секунду, когда нечто вышло из-за дерева. "
            window hide
            play sound "audio/zombie.mp3"
            show зомби 1 with fastdissolve
            pause 2.0
            window show
            sec "ТВОЮ МАТЬ..."
            scene bank with fade
            hide sec
            show p w cr
            p w cr "Кха-ха-ха-ха это лицо стоило того."
            hide p
            show sec mad 
            sec "Да ты отбитый на голову, смешно ему..."
            "Очередной усталый вздох. Охранник осел на пол и вперил свой взгляд в пол."
            "..."
            sec "..."
            sec mad "В это сложно поверить."
            hide sec
            show p w 
            p w "Такова реальность. Мир уже не тот, каким был вчера."
            hide p 
            show sec mad
            sec mad "Ладно. Хорошо. Видимо, ты прав. Наступил конец света."
            sec mad "Прелестно."
            sec mad "..."
            sec "Ну и что ты предлагаешь?"
            hide sec
            show p w 
            p w "Запереть двери и найти еще оружие."
            p w "Побудем здесь какое-то время. В безопасности. А потом, нужно думать как найти провизию."
            hide p
            show sec 
            sec "(Сомнительно...)"
            sec "И долго мы тут торчать будем? Еда и вода не бесконечные. Из того, что есть в комнате отдыха, хватит на, дай Бог, 5 дней."
            hide sec
            show p w 
            p w an "Значит кто-то без пайка ха..."
            scene black with fade
            "С господином охранником, все-же, удалось договориться."
            "Двое людей приступили к укреплению их пристанища."
            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show p w with fastdissolve
            p w e "(Чуствую себя неважно...)"
            hide p with fastdissolve
            "Его новый знакомый готовился ко сну."
            "Сегодняшняя ночь знатно потрепала нервы."
            jump raspr


        label get_out_a_p:
            "Терпение Психопата лопнуло."
            "Еще секунда и он прикончит этого охранника."
            show p w 
            p w an "З@ебал ты меня, дядя."
            p w an "Тебе проще верить в то, что все хорошо, ну тогда увидимся на том свете, когда поймешь, что уже поздно."
            hide p
            show sec 
            sec mad "..."
            hide sec
            scene black with fade
            "Психопат слишком самоуверенно зашагал по улице."
            "Повернувшись на охранника, который застыл в дверях, он заметил на его лице гримасу ужаса."
            "Как вдруг..."
            "Из-за угла резко появился зомби!"
            play sound "audio/Добавления/ранение.mp3"
            "Он не стал церемониться и откусил у парня часть затылка."
            "Вот его песенка и спета."

            jump dead_end 


        label kill_the_bastard_a_p:
            show p w with fastdissolve
            p w an "(Он - лишь помеха, которую нужно устранить.)"
            hide p
            show sec 
            sec "Ну так вы собираетесь уходить? Или мне применить силу?"
            hide sec
            show p w 
            p w cr "Пожалуй ты уйдешь сегодня первым..."
            show p power at truecenter with fade
            scene black with fade
            "Он резким движением рассек брюхо мужчине."
            play sound "audio/Добавления/scream.mp3"
            sec "АААААА!!!!СУКАА-АААА!!!!"
            "Мужчина орал от боли."
            "Охранник резко достал нож и нанес удар в бедро Психопату."
            scene black with deathfade
            play sound "audio/уведа.mp3"
            $ phurttummy.grant()
            "Для человека, у которого органы на пол пути вниз, сила удара была неожиданная."
            "Психопат схавтился за ногу."
            "По ощущениям, в артерию он не попал, а значит шанс выжить значительно повышается."
            $ shealth += 1 #ранен
            "..."
            "С этим ударом последние силы покинули мужчину."
            "Он обмяк и перестал дышать."

            play sound "audio/уведа.mp3"
            $ crazy.grant()
            "..."
            $ pslaughter +=1  #- убила мужика
            $ pcrazy+=1
            p "Теперь все-КХа-кхаа-..хорошо. Можно сказать отвоевал это место ха-ха-кха"

            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show p w with fastdissolve
            p w e "(Чуствую себя неважно...)"
            hide p with fastdissolve
            "Он стал готовится ко сну."
            "Сегодняшняя ночь знатно потрепала нервы."
            jump raspr
           
        





        label bl_bank_with_girl_p:
            scene bank with fade
            "Стоило им зайти внутрь, как тут же они попали под пронзительный взгляд охранника."
            show sec mad with fastdissolve
            sec mad "..."
            hide sec mad
            show p w bl with fastdissolve
            p w bl "..."
            hide p w bl
            show girl shock with fastdissolve
            l shock "..."
            l shock "Понимаете, мы-"
            hide girl
            show sec mad
            sec mad "..."
            hide sec mad
            show girl shock
            l shock "Мы..мы...эмм-м, да. Мы п-попали в сложную ситуацию. Эти..зомби, они-"
            "Девушка нервничала. Под тяжелым взором охранника ей было сложно сформулировать свои мысли."
            hide girl
            show sec
            sec"..."
            sec sm "Что?"
            sec sm "Вы думаете, это очень смешно?"
            sec "Врываться в государственное учреждение и нести бред в мою ночную смену - это такие шуточки у вас?"
            "Взгляд мужчины стал еще мрачнее."
            sec mad "Эй парень, ты вообще откуда сбежал с мечами за спиной?"
            hide sec
            show p w bl
            p w bl cr "Давай на тебе их и обробуем)"
            hide p  
            show girl
            l an "Нет, послушайте, зом-"
            hide girl 
            show sec 
            sec "Он мне еще и угрожать удумал."
            sec "БЫСТРО НА ВЫХОД!"
            hide sec
            show p w bl an
            p w an "Если вы соизволите посмотреть запись камер наружного наблюдения, сами все поймете."
            p w e "Насколько мне известно это ваша прямая обязанность,а вы в потолок плюете на рабочем месте."
            hide p 
            show sec 
            sec "Моя прямая обязанность - выгонять всяких торчков, как Вы например."
            sec mad "Нечего мне тут про каких-то зомби затирать. Посмеялись и хватит."
            hide sec
            show girl
            l an "..."
            hide girl
            show p w bl
            p w bl cr "Раз такой смелый, сходи сам погляди..."
            p w bl cr "Если никого не будет, мы просто уйдем, чего тебе стоит..."
            hide p
            show girl
            l shock "Что ты творишь, они ж..."
            hide girl
            show p w bl
            p w bl cr "Давай, тебе же нечего там боятся, мы же все придумали..."
            hide p
            show sec 
            play sound "audio/уведа.mp3"
            $ hod.grant()
            sec "Закрой свой рот, с чего мне верить в ваш бред, мне запрещенно покидать пост!!!"
            hide sec
            show p w
            p w bl "Ха-ха смотри как разозлился, ну же давай, спать тоже запрещенно на рабочем месте."
            l "{i}Господи...{\i}"
            p w bl norm "(Нужно дествовать.)"

            window hide


            menu:
                "Вытащить охраника на улицу":
                    jump bl_negotiation_p
                "Свалить отсюда":
                    jump bl_get_out_p
                "Пришить ублюдка":
                    jump bl_kill_the_bastard_p

            window show


        label bl_negotiation_p:
            $ pmanip+=1
            show p w bl an with fastdissolve
            p "Где твоя решительность или мне проводить тебя за ручку?!"
            p w bl an "Пойдем, проведу тебе экскурсию в новый мир!"
            "Психопат начал стемительно сокращать расстояние между ними."
            "Девушка поняла, что это не к добру, а потому отошла в угол, желая испариться в воздухе."
            hide p
            show sec mad
            sec "Иди сюда клоун, я научу тебя манерам."
            hide sec
            play sound "audio/Добавления/fight.mp3"
            show girl cry
            l "Прекратите, выйдете на улицу и будете мертвы через минуту!!!."
            hide girl
            play sound "audio/Добавления/opd.mp3"
            "Психопат оказался сильнее, он буквально выпихнул охраника на улицу."
            show sec mad
            scene street3 with fade
            "Вся злость испарилась в секунду, когда нечто вышло из-за дерева. "
            window hide
            play sound "audio/zombie.mp3"
            show зомби 1 with fastdissolve
            pause 2.0
            window show
            sec "ТВОЮ МАТЬ..."
            scene bank with fade
            hide sec
            show p w bl cr
            p w cr "Кха-ха-ха-ха это лицо стоило того."
            hide p
            show sec mad 
            sec "Да ты отбитый на голову, смешно ему..."
            hide sec
            "Очередной усталый вздох. Охранник осел на пол и вперил свой взгляд в пол."
            "..."
            sec "..."
            sec mad "В это сложно поверить."
            hide sec
            show p w bl 
            p w bl  "Такова реальность. Мир уже не тот, каким был вчера."
            hide p 
            show sec mad
            sec mad "Ладно. Хорошо. Видимо, вы правы. Наступил конец света."
            sec mad "Прелестно."
            sec mad "..."
            sec "Ну и что вы предлагаете?"
            hide sec
            show p w bl 
            p w bl "Запереть двери и найти еще оружие."
            p w bl "Побудем здесь какое-то время. В безопасности. А потом, нужно думать как найти провизию."
            hide p
            show girl 
            l "Звучит как толковый план."
            l "Останемся здесь на какое-то время."
            hide girl 
            show sec 
            sec "(Сомнительно...)"
            sec "И долго мы тут торчать будем? Еда и вода не бесконечные. Из того, что есть в комнате отдыха, хватит на, дай Бог, 5 дней."
            hide sec
            show p w bl
            p w bl an "Значит кто-то без пайка ха..."
            scene black with fade
            "С господином охранником, все-же, удалось договориться."
            "Трое людей приступили к укреплению их пристанища."
            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show p w with fastdissolve
            p w bl e "(Чуствую себя неважно...)"
            hide p with fastdissolve
            "Его новые знакомые готовились ко сну."
            "Сегодняшняя ночь всем знатно потрепала нервы."
            jump raspr


        label bl_get_out_p:
            "Терпение Психопата лопнуло."
            "Еще секунда и он прикончит этого охранника."
            show p w bl 
            p w bl an "З@ебал ты меня, дядя."
            p w bl an "Тебе проще верить в то, что все хорошо, ну тогда увидимся на том свете, когда поймешь, что уже поздно."
            hide p
            show sec 
            sec mad "..."
            hide sec
            show p w bl  
            p w bl an "Лайла, пошли отсюда. Найдем другое место."
            hide p
            show girl
            l shock "Эмм.."
            l cry "К-куда же мы пойдем? Может, стоит попробовать договориться?"
            hide girl
            show p w bl
            p w bl e "Ну, так сама попробуй, а я посмотрю)"
            "Девушка поплелась к выходу."
            p w bl an "Здесь мы вряд-ли добъемся понимания."
            hide p
            show girl 
            l cry "Но.."
            hide girl
            "Психопат закатил глаза"
            scene black with fade
            "Психопат слишком самоуверенно зашагал по улице."
            "Повернувшись на девушку, которая застыла в дверях, он заметил на ее лице гримасу ужаса."
            "Как вдруг..."
            "Из-за угла резко появился зомби!"
            play sound "audio/Добавления/ранение.mp3"
            "Он не стал церемониться и откусил у парня часть затылка."
            "Вот его песенка и спета."

            jump dead_end 


        label bl_kill_the_bastard_p:
            show p w bl with fastdissolve
            p w bl an "(Он - лишь помеха, которую нужно устранить.)"
            hide p
            show sec 
            sec "Ну так вы собираетесь уходить? Или мне применить силу?"
            hide sec
            show girl 
            l shock "Но..."
            hide girl
            show p w bl 
            p w  bl cr "Пожалуй ты уйдешь сегодня первым..."
            show p power at truecenter with fade
            scene black with fade
            "Он резким движением рассек брюхо мужчине."
            play sound "audio/Добавления/scream.mp3"
            sec "АААААА!!!!СУКАА-АААА!!!!"
            l "ААААА???!!!!!!!!!!! ТЫ ЧТО?!!!"
            "Мужчина орал от боли. Лайла орала от ужаса."
            "Охранник резко достал нож и нанес удар в бедро Психопату."
            scene black with deathfade
            play sound "audio/уведа.mp3"
            $ phurttummy.grant()
            "Для человека, у которого органы на пол пути вниз, сила удара была неожиданная."
            "Психопат схавтился за ногу."
            "По ощущениям, в артерию он не попал, а значит шанс выжить значительно повышается."
            $ shealth += 1 #ранен
            "..."
            "С этим ударом последние силы покинули мужчину."
            "Он обмяк и перестал дышать."

            play sound "audio/уведа.mp3"
            $ crazy.grant()
            "..."

            "Когда Психопат пришел в себя, он заметил на себе потерянный взгляд Лайлы."
            $ pslaughter +=1  #- убила мужика
            $ pcrazy+=1
            p "Теперь все-КХа-кхаа-..хорошо. Мы..мы сможем здесь остаться. Не волнуйся."
            l "..."
            p "Ты же понимаешь, что я должен был это сделать? Или он - или мы."
            l "....."
            p "Лайла."
            l "...? Что?"
            p "Я сделал это для нашей безопасности. Не бойся меня."
            l ".....Я понимаю. Ты прав."
            p "Ты правда понимаешь?"
            l "Да."
            p "Хорошо."

            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show p w with fastdissolve
            p w bl e "(Чуствую себя неважно...)"
            hide p with fastdissolve
            "Его новая знакомая готовилась ко сну."
            "Сегодняшняя ночь всем знатно потрепала нервы."
            p "А может..."
            



            window hide


            menu:
                "Поговорить с Лайлой":
                    jump bl_talk_layla_p
                "Лечь спать":
                    jump bl_sleep_layla_p
                "Убить ее":
                    jump bl_kill_layla_p

            window show
        


        

        label bl_talk_layla_p:
            show p w bl with fastdissolve
            p w bl norm"(Нужно с ней поговорить. Она с тех пор и словечком не обмолвилась.)"
            p w bl "Лайла?"
            hide p
            show girl
            l "...Да?"
            hide girl
            show p w bl 
            p w bl "Знаешь я не хочу, чтобы между нами была недосказанность."
            p w bl '(Нужно надавить на жалость и попробовать заставить сочуствовать мне.)'
            p w bl  '(Или же отвлечь внимание, если не сработает придётся расправится и с ней.)'
            p w bl cr '(Ха ей лучше играть по моим правилам.)'
            "Психопат нежно коснулся ее предплечья и заглянул в глаза, под ладонью он почуствовал мелкую дрожь."
            p w bl "Тебе не меня стоит бояться."
            p w bl norm "Хотя я тебя полностью понимаю, на моих глазах эти твари убили моего младшего братика."
            p w bl norm "Я до последнего боролся, но не смог его защитить, понимаешь не смог... я никогда себе не прощу."
            hide p
            show girl cry
            "Девушка опустила плечи и на глазах проступили слезы. "
            hide girl
            show p w bl cr
            p w bl cr '(Серьезно? Пару слов и она уже преданее собаки.)'
            p w bl norm "Когда я встретил тебя, я понял, что это мой шанс...я обязан был защитить твою жизнь."
            p w bl norm "Чего бы это не стоило."
            hide p
            show girl cry
            play sound "audio/уведа.mp3"
            $ seduct.grant()
            l "Я тебя испугалась, но ты прав...наверное, если бы он нас выгнал, мы бы погибли."
            p w bl cr "Ну вот и все прияснили, а теперь можно ложится спать."
            scene black with slowdissolve
            $ pmanip+=1

            jump raspr


        label bl_sleep_layla_p:
            show p w bl with fastdissolve
            p w bl "(Не буду ее отвлекать. Надо все переварить.)"
            p w bl "(Тоже попробую поспать.)"
            hide p
            "Она пыталась заснуть, но разные навязчивые мысли мешали."
            "Стратег вслушивалась в дыхание девушки рядом: оно было ровное, глубокое."
            "В скором времени он провалился в царство Морфея."
            scene black with slowdissolve
            "Вот только не надолго."
            "Пробуждение было ярким."
            scene restroom
            show girl with deathfade
            l an "..."
            hide girl
            play music "audio/piano.mp3"
            "Лайла, этот божий одуванчик...Она пырнула Психопата."
            "Ударила ножом охраника в спину!"
            show p 
            p w bl hor "Лайла..."
            p w bl hor "................."
            p w bl cr "(Нужно было убить эту суку еще в начале.)"

            jump dead_end

        label bl_kill_layla_p:
            show p w bl with fastdissolve
            play music "audio/Добавления/chop.mp3"
            show p power at truecenter with fade
            p w bl cr "(Зачем мне лишние проблемы.)"
            p w bl cr "Ну что Лейла, давай прощаться хах..."
            show girl with deathfade
            l shock "Что ты задумал..."
            play sound "audio/Добавления/крик.mp3"
            scene black with fade
            "Она замолчала навсегда."
            $ pcrazy+=1
            jump raspr


        








        label bl_bank_alone_p:
            scene bank with fade
            "Стоило ему зайти внутрь, как тут же он попал под пронзительный взгляд охранника."
            show sec mad with fastdissolve
            sec mad "..."
            hide sec mad
            show p w bl with fastdissolve
            p w bl"..."
            hide p w bl
            sec mad "..."
            hide sec mad
            show p w bl with fastdissolve
            p w bl"Если я вам скажу, что по улицам города бегают мертвецы...да, пожалуй, не годится в аргументы"
            hide p w bl
            show sec
            sec"..."
            sec sm "Что?"
            sec sm "Вы думаете, это очень смешно?"
            sec "Врываться в государственное учреждение и нести бред в мою ночную смену - это такие шуточки у вас?"
            "Взгляд мужчины стал еще мрачнее."
            sec mad "Парень, ты вообще откуда сбежал с мечами за спиной?"
            hide sec
            show p w bl
            p w bl cr "Давай на тебе их и обробуем)"
            hide p 
            show sec 
            sec "Он мне еще и угрожать удумал."
            sec "БЫСТРО НА ВЫХОД!"
            hide sec
            show p w bl an
            p w bl an "Если вы соизволите посмотреть запись камер наружного наблюдения, сами все поймете."
            p w bl e "Насколько мне известно это ваша прямая обязанность,а вы в потолок плюете на рабочем месте."
            hide p 
            show sec 
            sec "Моя прямая обязанность - выгонять всяких торчков, как Вы например."
            sec mad "Нечего мне тут про каких-то зомби затирать. Посмеялись и хватит."
            hide sec
            show p w bl 
            p w bl cr "Раз такой смелый, сходи сам погляди..."
            p w bl cr "Если никого не будет, я просто уйду, чего тебе стоит..."
            hide p
            show p w bl 
            p w bl cr "Давай, тебе же нечего там боятся, я же несу бред..."
            hide p
            show sec 
            play sound "audio/уведа.mp3"
            $ hod.grant()
            sec "Закрой свой рот, с чего мне верить в твой бред, мне запрещенно покидать пост!!!"
            hide sec
            show p w bl
            p w bl "Ха-ха смотри как разозлился, ну же давай, спать тоже запрещенно на рабочем месте."
            p w bl norm"(Нужно дествовать.)"

            window hide


            menu:
                "Вытащить охраника на улицу":
                    jump bl_negotiation_a_p
                "Свалить отсюда":
                    jump bl_get_out_a_p
                "Пришить ублюдка":
                    jump bl_kill_the_bastard_a_p

            window show


        label bl_negotiation_a_p:
            $ pmanip+=1
            show p w bl an with fastdissolve
            p "Где твоя решительность или мне проводить тебя за ручку?!"
            p w bl an "Пойдем, проведу тебе экскурсию в новый мир!"
            "Психопат начал стемительно сокращать расстояние между ними."
            hide p
            show sec mad
            sec "Иди сюда клоун, я научу тебя манерам."
            hide sec
            play sound "audio/Добавления/fight.mp3"
            play sound "audio/Добавления/opd.mp3"
            "Психопат оказался сильнее, он буквально выпихнул охраника на улицу."
            show sec mad
            scene street3 with fade
            "Вся злость испарилась в секунду, когда нечто вышло из-за дерева. "
            window hide
            play sound "audio/zombie.mp3"
            show зомби 1 with fastdissolve
            pause 2.0
            window show
            sec "ТВОЮ МАТЬ..."
            scene bank with fade
            hide sec
            show p w bl cr
            p w bl cr "Кха-ха-ха-ха это лицо стоило того."
            hide p
            show sec mad 
            sec "Да ты отбитый на голову, смешно ему..."
            hide sec
            "Очередной усталый вздох. Охранник осел на пол и вперил свой взгляд в пол."
            "..."
            sec "..."
            sec mad "В это сложно поверить."
            hide sec
            show p w bl
            p w "Такова реальность. Мир уже не тот, каким был вчера."
            hide p 
            show sec mad
            sec mad "Ладно. Хорошо. Видимо, ты прав. Наступил конец света."
            sec mad "Прелестно."
            sec mad "..."
            sec "Ну и что ты предлагаешь?"
            hide sec
            show p w bl 
            p w bl "Запереть двери и найти еще оружие."
            p w bl "Побудем здесь какое-то время. В безопасности. А потом, нужно думать как найти провизию."
            hide p
            show sec 
            sec "(Сомнительно...)"
            sec "И долго мы тут торчать будем? Еда и вода не бесконечные. Из того, что есть в комнате отдыха, хватит на, дай Бог, 5 дней."
            hide sec
            show p w 
            p w bl an "Значит кто-то без пайка ха..."
            scene black with fade
            "С господином охранником, все-же, удалось договориться."
            "Двое людей приступили к укреплению их пристанища."
            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show p w with fastdissolve
            p w bl e "(Чуствую себя неважно...)"
            hide p with fastdissolve
            "Его новый знакомый готовился ко сну."
            "Сегодняшняя ночь знатно потрепала нервы."
            jump raspr


        label bl_get_out_a_p:
            "Терпение Психопата лопнуло."
            "Еще секунда и он прикончит этого охранника."
            show p w bl
            p w bl an "З@ебал ты меня, дядя."
            p w bl an "Тебе проще верить в то, что все хорошо, ну тогда увидимся на том свете, когда поймешь, что уже поздно."
            hide p
            show sec 
            sec mad "..."
            hide sec
            scene black with fade
            "Психопат слишком самоуверенно зашагал по улице."
            "Повернувшись на охранника, который застыл в дверях, он заметил на его лице гримасу ужаса."
            "Как вдруг..."
            "Из-за угла резко появился зомби!"
            play sound "audio/Добавления/ранение.mp3"
            "Он не стал церемониться и откусил у парня часть затылка."
            "Вот его песенка и спета."

            jump dead_end 


        label bl_kill_the_bastard_a_p:
            show p w bl  with fastdissolve
            p w bl an "(Он - лишь помеха, которую нужно устранить.)"
            hide p
            show sec 
            sec "Ну так вы собираетесь уходить? Или мне применить силу?"
            hide sec
            show p w  bl
            p w bl cr "Пожалуй ты уйдешь сегодня первым..."
            show p power at truecenter with fade
            scene black with fade
            "Он резким движением рассек брюхо мужчине."
            play sound "audio/Добавления/scream.mp3"
            sec "АААААА!!!!СУКАА-АААА!!!!"
            "Мужчина орал от боли."
            "Охранник резко достал нож и нанес удар в бедро Психопату."
            scene black with deathfade
            play sound "audio/уведа.mp3"
            $ phurttummy.grant()
            "Для человека, у которого органы на пол пути вниз, сила удара была неожиданная."
            "Психопат схавтился за ногу."
            "По ощущениям, в артерию он не попал, а значит шанс выжить значительно повышается."
            $ shealth += 1 #ранен
            "..."
            "С этим ударом последние силы покинули мужчину."
            "Он обмяк и перестал дышать."

            play sound "audio/уведа.mp3"
            $ crazy.grant()
            "..."
            $ pslaughter +=1  #- убила мужика
            $ pcrazy+=1
            p "Теперь все-КХа-кхаа-..хорошо. Можно сказать отвоевал это место ха-ха-кха"

            scene restroom with fade
            "{i}Какое-то время спустя{\i}"
            "{i}Комната отдыха{\i}"
            show p w bl with fastdissolve
            p w bl e "(Чуствую себя неважно...)"
            hide p with fastdissolve
            "Он стал готовится ко сну."
            "Сегодняшняя ночь знатно потрепала нервы."
           




       









        label raspr:
            if  pcrazy > palone and pcrazy > pmanip:
                jump end_c_p
            if  palone > pcrazy and palone > pmanip:
                jump end_a_p
            if  pmanip > palone and pmanip > pcrazy:
                jump end_m_p
            else:
                jump end
        return


        label end_c_p:
            scene restroom with fade
            play music "audio/Добавления/doll.mp3"
            play sound "audio/Добавления/syma.mp3"
            "Он не знал сколько времени провел в каморке охраника."
            "Голоса убитых звенели у него в голове."
            "Социальная оторванность и травматический опыт сделали своё."
            scene night with fade
            show p w bl cr
            p w bl "Я хочу почуствовать снова, побыть на вершине пищевой цепи."
            p w bl "Иначе голоса не замолчат, мне нужно убить снова..."

            jump end
        


        label end_a_p:
            play music "audio/Добавления/f1.mp3"
            scene night with fade
            "Больше не было смысла оставаться с людьми, искать убежище человечества."
            "Он просто поселится вдали от всех, как мечтал всю жизнь и будет смиренно ждать смерти."
            scene black with fade
            play sound "audio/Добавления/opd.mp3"
            "Пока в один из дней его покой не нарушит молодой парень, появившийся на пороге его дома весь в крови..."
            jump end

        
        label end_m_p:
            scene night with fade
            play music "audio/Добавления/doll.mp3"
            "Спустя 1.5 года мужчина собрал возле себя выживших людей, он начал сторительсьво коммуны. Все видели в нем лидера, но об истинных намерениях не знал никто."
            show p cr
            "На месте руин я построю новое общество, оно будет совершенным."
            jump end








        












        jump end
    
    label green:
        $ f.info = 1
        scene black
        show f with dissolve
        "Вы выбрали Борца."
        hide f
        show f power at truecenter with dissolve
        'Ваш персонаж обладает уникальной способностью - "Несокрушимая воля".' 
        "В здоровом теле здоровый дух. Вы способны пережить серьезные ранения."
        hide f power
        
        "Помните, что прохождение игры напрямую зависит от выбранного Вами персонажа."
        "Делайте выборы, исходя из его характеристик и оружия."
        "Наслаждайтесь игрой..."
        "{i}...И пусть удача всегда будет с Вами!{\i}"
        "P.S. Не забывайте сохраняться :)"

        stop music fadeout 2.0
        play music "audio/normal.mp3" fadein 1
        scene гостиная with slowdissolve
        "На улице уже стемнело. В этот поздний час гостинная не была поглощенна тьмой лишь благодаря паре тусклых светильников."
        "Слабый свет не мешал недавнему просмотру телевизора."
        "На диване сидел высокий парень."
        "Его атлетичное телосложение сразу навлекало на мысли о том, чем же он занимается?"
        "Может быть он не вылезает из зала, и 10 варенных яиц - его обыденный перекус?"
        "Быть может он спортсмен, который думает только о новых победах и не терпит проигрышей?"
        "Может он сбежал из модельного агенства?"
        "Предположений куча..."
        play sound "audio/уведа.mp3"
        $ who.grant()
        "Но все они улетучатся, когда вы столкнётесь с пронзительным взглядом его холодных голубых глаз, которые скрывают за собой куда больше всего вышеперечисленного..."
        "Парень откинулся на широкую спинку мебели, о чём-то задумался."
        "В это время в комнату вбежал его младший брат."
        show bro sm at right with fastdissolve 
        bro"Хэй, в холодильнике мышь повесилась."
        bro"А я ужасно проголодался после сегодняшней игры."
        scene гостиная with fastdissolve
        "Старший брат усмехнулся."
        show f sm at left with fastdissolve
        show bro sm at right with fastdissolve 
        f "Прямо-таки ужасно?"
        bro "Я голоден, как волк!"
        f "Я заказал пиццу, скоро должны привезти."
        play sound "audio/стук.mp3"
        show bro sm2 at right with fastdissolve 
        bro "Даааааа"
        bro"Я заберу."
        f e "Смотри аккуратнее."
        f sm "Не сьешь курьера."
        show bro sm at right with fastdissolve 
        bro "Пффф..."
        scene гостиная with fastdissolve
        "Оголодавший бейсболист собрался было бежать к входной двери, как на полпути его остановила крепкая хватка брата."
        show f e at left with fastdissolve
        show bro sm at right with fastdissolve 
        f "Стой."
        bro "Да не буду я его есть, не волнуйся."
        scene гостиная with fastdissolve
        "Старший брат приложил указательный палец к своим губам."
        stop music fadeout 2.0
        "Жестом призывая замолкнуть."
        show f at left with fastdissolve
        f "Тссс."
        f "Какие-то странные звуки, не нравится мне это."
        show bro sm at right with fastdissolve 
        bro"Да брось ты."
        bro "Ты когда в последний раз высыпался? Всё время на своих секретных заданиях. Вот тебе и мерещется всякое."
        show f an at left with fastdissolve
        f "Я же сказал притихнуть."
        bro "Пойду проверю, что там такое. Руку мою только отпусти."
        show f at left with fastdissolve
        show bro surprised at right with fastdissolve 
        f "Не пойду, а пойдём. За мной держись, не высовывайся."
        "Младший брат наконец ощутил его настороженность и серьёзность."
        "Лёгкое волнение разлилось по всему телу. Он понял - не время для шуток. Ведь прекрасно знал - чутьё у его брата отменное."
        scene гостиная with fastdissolve
        "Парни неспешно направились к входной двери, стараясь не создавать лишнего шума."
        
       

        scene дверь with dissolve 
        "Старший брат бесшумно провернул замок и медленно потянул дверь за ручку, предварительно бросив взгляд за спину, чтобы удостовериться, что мелкий под его защитой."
        play sound "audio/skrip.mp3"
        scene дверь открыта  with slowdissolve
        "Открыв дверь, он увидел вовсе не курьера."
        show f an at left with fastdissolve
        f "Чёрт..."
        stop music fadeout 2.0
        f "ДЕРЖИСЬ ЗА МНОЙ!"
        show bro shock at right with fastdissolve 
        bro "Что-то мне уже и пиццы не хочется..."
        play sound "audio/hand.mp3"
        scene дверь рука 
        "В полумраке резко возникла чья-то рука."
        play music "audio/tiktok.mp3" fadein 1
        "Борец принял боевую стойку."
        show f at left with fastdissolve
        f "..."
        show bro shock at right with fastdissolve 
        bro "Больше у них пиццу не заказывай..."
        "Не успел он закончить мысль, как из дверного проема показалось...нечто."
        scene дверь открыта with fade
        window hide
        play sound "audio/zombie.mp3"
        show зомби 1 with fastdissolve
        pause 2.0
        window show
        "Нечеловеческий крик был оглушительным."
        "Существо, появившееся в коридоре, одним своим видом чуть не отправило в нокаут младшего."
        "Никогда он не видел ничего подобного."
        hide зомби 1
        "Вдруг, старший брат резко ударил нелюдя в живот, от чего тот отлетел в самый конец коридора. Проход из квартиры был ненадолго расчищен."
        show bro horrified at left with fastdissolve
        show f at left with fastdissolve
        f "БЕЖИМ!"
        scene black with fastdissolve
        "Борец выволок за руку младшего брата и подтолкнул его к лестнечному пролёту, ведущему в подвал."
        show f at left with fastdissolve
        f "Вниз."
        show f an at left with fastdissolve
        f "ЖИВЕЕ."
        scene black with fastdissolve
        "Влетев туда, чудом не свалившись с лестницы, они одновременно захлопнули дверь."
        play sound "audio/замок.mp3"
        scene подвал with fade
        "Борец задвинул щеколду, подпёр дверь старым стулом."
        "Видимо кто-то так и не донёс его до мусорки..."
        "Быстрые шаги монстра раздались совсем рядом. Времени на раздумья не было."
        "Братья посмотрели друг на друга."
        
        show bro horrified at right with fastdissolve
        bro "Это...как это...аху*ть"
        scene подвал with fade
        "Последнее слово он произнёс неверящим полушёпотом."
        show f at left with fastdissolve
        f "Именно..."
        show bro dead at right with fastdissolve
        "Младший застыл и уставился в пол в пустыми глазами. Он был в шоке - тело сковано, разум в астрале."
        show f sad at left with fastdissolve
        f "Я с тобой, слышишь?"
        "Юноша поднял на парня свои потерянные глаза."
        show bro cry at right with fastdissolve
        bro "Аааа?"
        show f sm at left with fastdissolve
        f "Я не дам тебя в обиду, держись под боком, прорвёмся."
        "После недолгого молчания, подросток промолвил:"
        bro"Хорошо..."
        scene подвал with fade
        show f with fastdissolve
        f "(Нужно найти - чем бы эту тварь кончить...)"
        f "(Рано или поздно оно прорвется.)"
        show f 
        f "Слушай, надо поискать, чем можно отбиться."
        bro "..."
        f e "(Чёрт, сильно его огорошило.)"
        bro "..."
        show f
        f "(От него сейчас нет толку. Психика не выдерживает.)"
        scene подвал with fastdissolve
        "Парень сам занялся поиском оружия. Перед глазами маячил всякий бесполезный хлам. От набора хрустального сервиза до раритеных виниловых пластинок. "
        "Как вдруг, прямо под руку, попалась..."
        window hide
        scene black with fade
        show бита at truecenter with dissolve
        pause 2.0
        hide бита with dissolve
        window show
        "Борец взял биту, виртуозно её покрутив."
        play sound "audio/уведа.mp3"
        $ fweapon.grant()
        #ачивка, звуковой сигнал
        scene подвал with fade
        "Тварь была уже близко."
        "Зомби от людей разделяла лишь запертая на ненадежную щеколду дверь."
        "Секунда..."
        "Дверь вышибло."
        show f sad with fastdissolve
        "Молодой человек испуганно поднял глаза в поисках своего младшего брата."
        scene подвал with fade
        "Зомби на огромной скорости падал вниз по лестнице - логичное следствие интенсивного проникновения в подвал."
        "Оживший мертвец приземлился в нескольких метрах от подростка."
        "Обычный человек после подобных финтов свернул бы шею. Но перед ними был не человек."
        "Зомби накинулся на мальчика со спины."
        "Тот даже пискнуть не успел."
        show f w  with fastdissolve
        f "..."
        f "Лиам..."
        scene подвал with deathfade
        "На его животе появлялись рваные раны."
        "Душераздирающие вопли заполнили помещение."
        "Пока зомби вгрызался в плоть юноши, в борце распалялась животная ярость."
        "На его глазах неизвестная тварь раздирала тело родного человека."
        show f w hor with fastdissolve
        f "..."
        f "Что ж..."
        f "Выходные оказались недолгими..."
        play sound "audio/уведа.mp3"
        $ holiday.grant()
        scene black 
        show f power at truecenter with fade #Нокаут

        scene подвал with fade
        show f w hor with fastdissolve
       
        f w  "(Ему уже не помочь.)"
        f w  "(Слишком большой физический урон.)"
        scene bro death with dissolve
        window hide
        pause 2.0
        window show
        "Юноша уже не кричал."
        "Редкие всхипы указывали на то, что конец близок."
        "Сознание покидало его."
        "Так он и умрет. На холодном полу. С выпотрошенным животом."
        "Не так юноша представлял сегодняшний вечер..."
        scene подвал with fade
        show f w with fastdissolve
        f w  "..."
        f w  "........."
        "Борец выглядел непреклонно. Сложно было понять, что творится в его голове. Однако в следующий миг он..."
        window hide
        hide f with fade
        window hide
        menu:
            "Убил зомби":
                jump kill_f_1
            
            "Обездвижил зомби":
                jump stop_f
            
            "Убежал":
                jump run_away_f_1

        window show

        label kill_f_1:
            play music "audio/напряг4.mp3" fadein 1
            scene подвал with fade
            show зомби 1 
            zombie "Кхаааа!!!"
            "Зомби самозабвенно отрывал куски плоти от едва живого юноши."
            "Непохоже, что он торопился: юноша еще дышал, оставаясь на краю сознания."
            "Более того, мерзкий нелюдь в своем безудержном порыве даже не замечал парня."
            scene подвал with fade
            "Борец крепче перехватил биту и плавно, словно хищник, подошёл к своей жертве."
            show f with fastdissolve
            f w hor "Со слухом у тебя, явно, проблемы."
            scene подвал with fade
            "Молниеносным оточенным движением парень прошёлся битой по голове монстра."
            play sound "audio/рык.mp3"
            zombie "АААРГХ!"
            "Зомби взревел. От головы осталась половина."
            show f with fastdissolve
            f w bl "Хах, а ты живучий."
            scene подвал with fade
            "Резкий выпад и бита прошлась по коленям твари."
            "Фатальный удар."
            "Зомби глухо повалился на пол."
            stop music fadeout 2.0
            window hide
            pause(2.0)
            scene подвал with fade
            window show
            "Какое-то время спустя..."
            show f w hor with fastdissolve
            f w bl hor "Два прямых удара, а он даже не попытался увернуться..."
            f w bl "Скучная тварь, с людьми поинтереснее."
            scene подвал with fade
            "Парень покинул подвал."
           
            
            jump after_1_blf



        label stop_f:
            scene подвал with fade
            play music "audio/напряг4.mp3" fadein 1
            show зомби 1 
            zombie "Кхаааа!!!"
            "Зомби самозабвенно отрывал куски плоти от едва живого юноши."
            "Непохоже, что он торопился: юноша еще дышал, оставаясь на краю сознания."
            "Более того, мерзкий нелюдь в своем безудержном порыве даже не замечал парня."
            hide зомби 1
            show f w hor with fastdissolve
            f "(Чёрт...)"
            f w an "(Как же хочется размать его по этому полу.)"
            f w "(Что ж...)"
            f "..."
            f "(Мне  ничего не мешает...)"
            scene подвал with fade
            "Парень украдкой взглянул на биту. Она ему подходила - такая же мощная..."
            "Воздух просвистел от искромётного удара в ноги твари."
            show f w hor with fastdissolve
            f w bl "Извини, в догонялки поиграть не получится."
            stop music fadeout 2.0
            window hide
            pause(20.0)
            scene подвал with fade
            window show
            "Какое-то время спустя..."
            "Борец спокойно прошёл мимо обездвиженного монстра."
            "Обернулся уже у входной двери."
            show f w bl with fastdissolve
            f w bl "Они все заплатят мне своей кровью за тебя."
            play sound "audio/рык.mp3"
            f w bl "..."
            f w bl e "Да да, я про вас говорю..."
            scene подвал with fade
            "Все....."
            "Отчего-то парень был уверен в том, что это не единственная такая тварь."
            "Старший брат покинул подвал, навсегда утратив прерогативу старшего."

            jump after_1_blf



        label run_away_f_1:
            scene подвал with fade
            show зомби 1 
            zombie "Кхаааа!!!"
            "Зомби самозабвенно отрывал куски плоти от едва живого юноши."
            "Непохоже, что он торопился: юноша еще дышал, оставаясь на краю сознания."
            "Более того, мерзкий нелюдь в своем безудержном порыве даже не замечал парня."
            
            "Это был шанс."
            hide зомби 1
            show f w with fastdissolve
            f "(Не так уж ты мне и нравился.)"
            f "(У меня скоро намечается важное задание...)"
            f "(Большой куш.)"
            scene подвал with fade
            "Ничего личного. Работа давно стала для него выше семьи."
            "Не желая встретиться с ним глазами, парень поспешно отвернулся."
            "Зомбак по-прежнему не обращал на него внимания, продолжая мучать юношу."
            "Делал он это нарочно или нет - не его дело."
            "Его дело - выжить."
            "По ступенькам он поднимался бесшумно."
            "Как вдруг..."
            scene black with fade
            play sound "audio/zombie.mp3"
            play music "audio/капец.mp3" fadein 1
            "На лестничном пролёте его поджидала группа таких же монстров."
            "Соориентироваться он не успел. Они молниеносно набросились на него."
            "Карма это? Или неудачное стечение обстоятельств? Неясно..."

            jump dead_end


    

        #После подвала и до улицы
        label after_1_blf:
            play music "audio/normal2.mp3"
            scene дверь открыта with fade
            show f w bl with fastdissolve
            f w bl "..."
            f w bl e "(Занятная ночь.)"
            f w bl an "..."
            f w bl  "(Нужно убираться отсюда.)"
            show f w bl e
            play sound "audio/желудок.mp3"
            "В животе заурчало."
            f w bl  "(Хмм...)"
            f w bl "(Организму нужна подпитка.)"
            f w bl e "(Безопасно ли ещё тут расхаживать?)"
            window hide
            menu:
                "Взять еды":
                    jump blf_with_food
                
                "Сваливать":
                    jump blf_no_food
            window show

        label blf_with_food:
            $ ffood += 1
            scene кухня with fade
            "Лунный свет пробивался через окно."
            "Его блики играли на лакированной столешнице из тёмного дуба."
            "Давно уже перевалило за полночь."
            "Борец тем временем потянулся за дверцу холодильника..."
            show f w bl with fastdissolve
            f "(Тц...)"
            f "(Действительно, мышь повесилась.)"
            f w bl an"..."
            f w bl an"(Чёрт...Если бы я был ближе...)"
            hide f with fastdissolve
            "Борец опустил голову..."
            "В следущую секунду на стене красовалась вмятина от его кулака."
            "Приятная боль, заглушающая внутренние переживания, разлилась по всему телу..."
            play sound "audio/уведа.mp3"
            $ pupupu.grant()
            "Этот парень всегда мог совладать с эмоциями."
            "Он не боялся смерти, работа сталкивала его с ней с завидной регулярностью."
            "Но смерть близкого человека всегда выбивает почву под ногами..."
            "Какой бы крепкой она не была..."
            "Через пару минут борец пришёл в себя и закидал в спортивную чёрную сумку, взятую по пути, несколько снеков и пару банок консерв."
            show f w bl with fastdissolve
            "..."
            "Как выходить?"
            hide f with fastdissolve
            window hide

            menu:
                "Выйти через парадную дверь":
                    jump blf_front_door
                
                "Выйти через заднюю дверь":
                    jump blf_back_door
            window show


        label blf_no_food:
            $ ffood = 0
            show f w bl  with fastdissolve
            f "(Перебьюсь.)"
            show f w bl e  with fastdissolve
            f "(Эти твари могут нагрянуть в любой момент.)"
            f w bl "(Пора убираться отсюда.)"
            hide f with fastdissolve
            "Парень бросил взгляд в сторону лестницы..."
            "По которой несколько минут назад сбегало двое."
            "А поднялся только один..."
            show f w bl  with fastdissolve
            "Чёрт..."
            "Если бы я не отходил от тебя..."
            hide f with fastdissolve
            "Прошло пару минут, прежде чем парень..."
            window hide


            menu:
                "Выйти через парадную дверь":
                    jump blf_front_door
                
                "Выйти через заднюю дверь":
                    jump blf_back_door
            window show



        label blf_front_door:
            scene дверь открыта with fade
            show f w bl with fastdissolve
            "Борец почти добрался до входной двери."
            show f w bl hor
            "Как вдруг..."
            scene дверь открыта
            play sound "audio/zombie.mp3"
            play music "audio/tiktok.mp3" fadein 1
            show зомби мэн with deathfade
            zombie "ХАГГХААГХ!!!!!"
            hide zombie
            scene дверь открыта with fade
            show f w bl hor
            f "Очаровательно..."
            scene дверь открыта
            "Зомби, пригнувшись к полу,  помчался на парня."
            window hide
            menu:
                "Спланировать удар битой":
                    jump blf_noswag
                
                "Встать в более устойчивую позу":
                    jump blf_swag
            window show

            
        label blf_swag:
            scene дверь открыта with fade
            "Борец принял устойчивую стойку, перехватил биту."  
            "Так, что зомби, несущийся к нему на всех порах, не смог сбить его с ног."  
            "В придачу бедолагу нехило огрели битой по голове..."
            scene black with fade
            "..."
            scene дверь открыта with fade
            stop music fadeout 2.0
            play music "audio/normal2.mp3"
            show f w bl with fastdissolve
            f w bl "Ничего личного, приятель."
            show f w bl e with fastdissolve
            f "Ты мне сразу не понравился."
            hide f
            scene black with fade
            "Теперь, парень наконец-то вышел на улицу..."
            jump streetf
            
        label blf_noswag:
            scene дверь открыта with fade
            "Борец просчитал, что лучшим ударом будет - удар в шею."  
            "Но, зомби, несущийся к нему на всех порах, сбил его с ног."
            stop music fadeout 2.0  
            scene black with fade
            "..."
            "Дальше всё, как в тумане..."
            jump dead_end

        label blf_back_door:
            scene черный ход with fade
            show f w bl with fastdissolve
            f w bl sm "Компания тут так себе."
            f "Нужно найти безопасное место."
            scene black with fade
            "Борец покинул дом."
            jump streetf
            


        #Улица    
        label streetf:
            stop music fadeout 2.0
            scene street with fade
            play music "audio/piano.mp3"
            "Ночной воздух сразу окутал своей манящей свежестью."
            "На секунду можно было подумать, что всё произошедшее - всего лишь сон, страшный и сумбурный."
            "Но спёкшаяся кровь на теле не позволяла убежать от реальности, порой такой болезненной..."
            show f w bl with fastdissolve
            f w bl "..."
            f w bl an "Эххх"
            scene street with fade
            "Парень поднял голову. Его голубые глаза заполнились бескрайним небесным океаном..."
            show f w bl with fastdissolve
            f w bl "..."
            f w bl "Нужно двигаться дальше."
            show f w bl sm with fastdissolve
            f w bl sm "Хах."
            f w bl sm "Причём во всех смыслах."
            show f w bl with fastdissolve
            f w bl "..."
            scene street with fade
            play sound "audio/shout.mp3"
            "Вдруг тишину нарушил истошный крик."
            play music "audio/напряг2.mp3" fadein 1
            "Борец повернулся в сторону шума."
            "Из-за угла доносились отчаянные женские вопли."
            show f w bl an with fastdissolve
            f "Смотрю, сегодня многие не спят."
            scene street with fastdissolve
            "Парень тихо двинулся на зов."
            scene tree with fade
            "За углом показалась аллея."
            "На одном из деревьев девушка спасалась от зомби. Она вскорабкалась на дерево, как маленький котёнок, а зомби желал поскорее стряхнуть её к себе."
            show girl with fastdissolve
            girl cry "На помощь!!!"
            girl cry "Пожалуйста...помогите мне!....Кто-нибудь..?!"
            hide girl
            show zombie
            play sound "audio/рык.mp3"
            zombie "ХАААРГХ!"
            hide zombie
            show girl shock 
            girl shock "..."
            scene black 
            show f power at truecenter with fade #Нокаут

            scene tree with fade
            show f w bl with fastdissolve
            f "Бедняга долго не протянет."
            f "Эта тварь голодна и хочет побыстрее набить желудок."
            play sound "audio/уведа.mp3"
            $ cool.grant()
            f "..."
            hide f with fastdissolve

            window hide


            menu:
                "Это же Лайла!":
                    jump heknows
                

                "Пройти мимо":
                    jump mimof
            window show


        label heknows:                    
            scene tree with fade
            "Парень, не теряя ни минуты, звонко просвистел, намеренно привлекая к себе внимание."
            show f w bl with fastdissolve
            f w bl "Эй, тупоголовый, беги сюда."
            f w bl "Я соскучился."
            scene tree with fade
            show zombie
            play sound "audio/рык.mp3"
            zombie "ХАААРГХ!"
            scene tree1 with fade
            "Зомбак оставил девушку, помчался к парню."
            show f w bl with fastdissolve
            f w bl "Вот так, молодец."
            scene tree1 with fade
            scene black 
            stop music fadeout 2.0
            "В следующий миг в мире стало на одну тварь меньше."
            "..."
            play music "audio/piano.mp3"
            scene tree1 with fade
            show girl with fastdissolve
            l shock "А?"
            hide girl
            "Устремив взгляд в сторону своего спасителя, Лайла засияла надеждой."
            show girl sm2  with fastdissolve
            l "Это ты! Боже, как мне повезло."
            scene tree1 with fade
            "Расправившись с монстром, борец направился в сторону девушки."
            show f w bl with fastdissolve
            f w bl "Прыгай, Лайла, я поймаю."
            scene tree1 with fade
            "Приземление было мягким."
            show f w bl at left with fastdissolve
            f w bl sm "Ты в порядке?"
            show girl at right with  fastdissolve
            l sm "...Да."
            l sm "Спасибо тебе. Я думала, это конец."
            l "..."
            show girl at right
            l "Кто бы мог подумать, что эта ночь обернётся таким кошмаром."
            l "Где Лиам?"
            scene tree1 with fade
            "..."
            "Лиам..."
            show f w bl at left with fastdissolve
            f "..."
            f "Его больше нет."
            show girl at right with  fastdissolve
            l shock "Ах... Мне так жаль... "
            l "Знаешь, Кетти тоже больше никогда не вернётся..."
            scene street with fade
            "Кетти...Так звали старшую сестру Лайлы. Сегодняшняя ночь забрала и её..."
            "Спустя пару минут..."
            
            show girl at right with  fastdissolve
            l "У тебя есть план? Что нам теперь делать?"
            hide girl
            show f w bl at left with fastdissolve
            f w bl "Нужно найти укрытие."
            f w bl "Здание с хорошей защитой. Крепкие двери, небольшие окна. Что-то типо того."
            hide s
            show girl at right with  fastdissolve
            l "Если так подумать... Дальше по улице есть банк."
            show f w bl at left with fastdissolve
            f w bl "Бинго."
            f w bl "Туда и отправимся. Дай мне свою руку, Лайла. Пойдём в тени, привлекать внимание нам ни к чему..."
            scene black with fade
            "Парень с девушкой направились в банк." 
            "Удача наконец-то оказалась на их стороне - зомби по дороге они не встретили..."
            "..."
            "Когда они подошли к зданию, то обнаружили, что дверь заперта."
            l "Блин, закрыто."
            f "Это же банк. Дверь закрыта, значит есть вероятность, что там охранник, а не кучка безмозглых..."
            "Парень сильно постучался."
            play sound "audio/стук2.mp3"
            "..."
            "Тишина."
            "Затем они обнаружили кнопку вызова."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            l "Пожалуйста, помогите нам!"
            voice "..."
            voice "Что у вас случилось?"
            "Прозвучал утомлённый мужской вздох."
            f  "Беседа сложилась бы куда лучше в другой обстановке. Впустите нас."
            f "А после почешем языками."
            l "Мне кажется, они уже близко..."
            voice "Ладно..."
            "Далее прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."
            
            jump f_bank_with_l

        

        label mimof:
            scene tree with fade
            "Парень скучающе посмотрел на представшую картину."
            "Его холодный взгляд не выражал ни капли жалости."
            "Он спокойно повернулся и ушёл. Бросил девушку на растерзание."
            "Видел, как её руки дрожат от усталости. От силы она продержится ещё пять минут..."
            "Он бы с лёгкостью спас её. Его физическая подготовка была на высоте, бойцовские навыки были отточены ожесточёнными тренировками."
            "Но..."
            "Зачем?"
            "Сегодня ночью он утратил сострадательность..."
            "Возможно, навсегда..."
            scene black with fade
            stop music fadeout 2.0
            "Парень держал путь в банк." 
            "Знал,что это отличное место, чтобы переждать нашествие неизвестных тварей..."
            "..."
            play music "audio/piano.mp3"
            "Когда он подошёл к зданию, то обнаружил, что дверь заперта."
            f "(Прекрасно. Дверь закрыта, значит есть вероятность, что там охранник, а не кучка безмозглых...)"
            "Парень сильно постучался."
            play sound "audio/стук2.mp3"
            "..."
            "Тишина."
            "Решил позвонить."
            play sound "audio/beep.mp3"
            "{i}пиип-пиип-пиип{\i}"
            "Прозвучал грубый голос."
            voice "Режим работы банка - с 9 до 21. Приходите утром."
            f  "Нужна помощь. В городе ЧП."
            voice "..."
            voice "Что происходит?"
            "Прозвучал утомлённый мужской вздох."
            f  "Беседа сложилась бы куда лучше в другой обстановке. Откройте дверь."
            f "А после почешем языками."
            voice "Ладно..."
            "Далее прозвучал звуковой сигнал. Тяжелая дверь наконец открылась."
            
            jump s_bankf
            
            
        
        
        
        
        
    
        #Банк
        label f_bank_with_l:
            scene bank with fade
            "Первое, что увидели вошедшие - пронзительный взгляд охранника."
            show sec mad with fastdissolve
            sec mad "..."
            hide sec mad
            show f w bl with fastdissolve
            f w bl "..."
            hide f w
            show girl shock with fastdissolve
            l shock "..."
            l shock "Понимаете, мы..."
            hide girl
            show sec mad
            sec mad "..."
            hide sec mad
            show girl shock
            l shock "Мы..мы...эмм-м, да. Мы п-попали в сложную ситуацию. Эти..зомби, они..."
            hide girl
            show sec at right with fastdissolve
            sec"..."
            sec sm "Что?"
            sec sm "Вы думаете, это очень смешно?"
            sec "Врываться в государственное учреждение и нести бред в мою ночную смену - это такие шуточки у вас?"
            show f w bl at left with fastdissolve
            f w bl e "Думаю, вам стоит не перебивать, а дослушать."
            sec "Молодой человек, что с вашей одеждой?"
            scene bank with fade
            "Борец смерил охранника суровым взглядом."
            show girl
            l an "Так вот... зомби"
            hide girl 
            show sec 
            sec "Довольно. На выход."
            hide sec
            show f w bl at left with fastdissolve
            f "Долго же до вас доходит."
            f w bl sm "Тормоз, вас же так зовут?"
            show sec at right with fastdissolve
            sec "Что простите?"
            f w bl sm "..."
            f w bl sm "(Ну и что с ним делать?)"


            window hide

            menu:
                "Договориться":
                    jump negotiationf
                "Уйти":
                    jump get_outf

            window show


        label negotiationf:
            show f w bl at left with fastdissolve
            f w bl e "Попробую объяснить доходчивее."
            f "На улице творится какая-то чертовщина. Вы сидите здесь в полном неведении, но так уверены, что мы несём чушь."
            f w bl e "Выглядите глупо."
            hide sec
            show girl at right with fastdissolve
            l "Почитайте новости, если не верите нам. На удивление, с интернетом всё в порядке." 
            l "Видимо люди для этих тварей интереснее кабеля." 
            f w bl sm "Хах."
            scene bank with fade
            "Очередной усталый вздох. Он разве что глаза не закатил."
            "..."
            "Мужчина достал телефон и несколько минут изучал ленту новостей."
            "По тому, как его глаза расширились, стало ясно - в новостях подтвердились их слова."
            play sound "audio/уведа.mp3"
            $ honey.grant()
            show sec 
            sec "..."
            sec mad "В это сложно поверить."
            hide sec
            show girl 
            l "Такова реальность. Мир уже не тот, каким был вчера."
            hide girl 
            show sec at right with fastdissolve
            sec mad "Ладно. Хорошо. Видимо, вы правы. Наступил конец света."
            show f w bl at left with fastdissolve
            f w bl sm "Неужели, вы, правда, так считаете?"
            sec mad "..."
            sec "Простите ребята, что так грубо отнёсся к вам."
            sec "Привык к постоянным ночным розыгрышам."
            hide f
            show girl at left with fastdissolve
            l sm "Ничего страшного. Наши слова, действительно, больше походили на абсурд, чем на правду."
            scene bank with fade
            "Некоторое время спустя..."
            show sec mad at right with fastdissolve
            sec "Что будем делать?"
            show f w bl at left with fastdissolve
            f "Поиграем в карты?"
            hide sec
            show girl at right with fastdissolve
            l sm "Пффф, прекрати."
            f "Нужно укрепить входы и выходы, проверить окна."
            f "Эту ночь мы точно проведём здесь."
            f "Дальше по обстоятельствам."
            hide girl
            show sec at right with fastdissolve
            sec "Понял."
            sec sm "Ну, за работу!"
            sec sm "Кстати, у меня есть несколько комплектов новой одежды. Оставлю её в комнате, вам не помешает переодеться."
            scene bank with fade
            "Новоиспечённая команда принялась за дело."
            stop music fadeout 2.0
            scene black with fade
            scene restroom with fade
            "Некоторое время спустя..."
            play music "audio/меланхолия.mp3"
            "..."
            show f at left with fastdissolve
            f "Как же я устал..."
            f "Постоянные задания..."
            f e "Работа, работа, работа."
            f "Тццц"
            f e "До сих пор плечо ноет после неудачного приземления пару недель назад."
            f sm "Зато, как я его огрел после этого..."
            scene restroom with fade
            "Борец погрузился в мысли о прошлом. Его захлёстывала радость и грусть, боль и воодушевление."
            "Но одна эмоция заглушала все остальные - скорбь тяжким грузом лежала на сердце..."
            show f at left with fastdissolve
            f sad "Чёрт, прости меня...прости......прости"
            f sad "..."
            scene restroom with fade
            "Полушёпот, состоящий из одного слова, наполнил комнату."
            "Внутри стало так пусто... Предательски чего-то не хватало."
            "..."
            show girl at right with fastdissolve
            l sm "Я не помешала? Смотри, какого мы котёнка нашли при обходе здания. Мэттью сказал, что он милашка."
            show f at left with fastdissolve
            f sm "Он и вправду очарователен."
            f sm "..."
            scene restroom with fade
            "В эту ночь близкого человека потерял не только парень, посчитавший котёнка очаровательным, но и девушка, в чьих руках был этот тёплый живой комочек."
            "Сегодня две души утратили свои бесценные частички. Эта пустота будет с ними до конца жизни... "
            "Или они смогут восполнить её?"
            "Да, чем-то другим, но от этого не менее тёплым..."
            "Парень посмотрел на девушку..."
            "С детсва их семьи дружили. Он часто играл с Лайлой в песочнице, пока Лиам и Кетти играли в догонялки."
            "Между четырьмя возникли пламенные дружеские узы..."
            "С возрастом они потухли - все стали поглощены своими делами, новыми заботами взрослой жизни."
            "Но сейчас прежняя искра была готова воспылать вновь..."
            show girl at right with fastdissolve
            l shock "Эх, если бы его можно было оставить..."
            if ffood==1:
                show f at left with fastdissolve
                f "А почему бы и нет. У меня в сумке есть пару консерв. Поделимся с ним."
                l sm "Правда?"
                scene restroom with fade
                "Парень кивнул."
                show girl at right with fastdissolve
                show f at left with fastdissolve
                l sm2 "Урааа"
                f sm "..."
                scene restroom with fade
                "Девушка подсела к парню на диван и молниеносно задремала у него на плече, котёнок тоже сладко посапывал..."
                stop music fadeout 2.0
                "За чёрной полосой всегда следует белая..."
                jump end1
            else:
                show f at left with fastdissolve
                f "У нас мало провизии, долго он с нами не продержится."
                play sound "audio/уведа.mp3"
                $ kitty.grant()
                l sm "Эхх...Ну ничего, Мэттью сказал, что знает, к кому можно будет его пристроить."
                scene restroom with fade
                "Парень кивнул."
                show girl at right with fastdissolve
                show f at left with fastdissolve
                scene restroom with fade
                "Девушка подсела к парню на диван и молниеносно задремала у него на плече."
                stop music fadeout 2.0
                "За чёрной полосой всегда следует белая..."
                jump end2
                
            label end1:
                play music "audio/финиш1.mp3"
                scene black with fade
                centered "Ранним утром спецслужбы обнаружили нашу четвёрку и забрали их под свою защиту."
                centered "Погода в этот ранний час была прекрасная, а в воздухе витало ощущение светлого будущего..."
                play sound "audio/уведа.mp3"
                $ finale.grant()
                centered "Конец основной истории."
            return
        

            label end2:
                play music "audio/финиш1.mp3"
                scene black with fade
                centered "Ранним утром спецслужбы обнаружили нашу тройку и забрали их под свою защиту."
                centered "Погода в этот ранний час была прекрасная, а в воздухе витало ощущение светлого будущего..."
                play sound "audio/уведа.mp3"
                $ finale.grant()
                centered "Конец основной истории."
            return
       



        
        label get_outf:
            "Терпение Борца лопнуло..."
            show f w bl  at left with fastdissolve
            f w bl e  "Пошли отсюда."
            hide sec
            show girl at right with fastdissolve
            l shock "..."
            f w bl e "До него, видимо, давно ничего не доходило."
            l "Пойдём. Берегите себя..."
            hide f
            hide girl
            show sec with fastdissolve
            stop music fadeout 2.0
            sec mad "..."
            scene black with fade
            scene street with fade
            play music "audio/меланхолия.mp3"
            "Девушка и парень отправились на поиски нового пристанища."
            "Ночь была тёплой. Луна, вместе с уличными фонарями, освещала дорогу."
            "Зомби видно не было, казалось, что их и вовсе не существует."
            "Аккуратно шагая по пустым кварталам, молодые люди дошли до..."
            scene black 
            scene street3 with fade
            "..."
            show f w bl at left with fastdissolve
            f w bl  "..."
            show girl at right with fastdissolve
            l sm "Это было..."
            f w bl "Тихо."
            scene street3 with fade
            "Лайла замолкла на полуслове..."
            show f w bl at left with fastdissolve
            f w bl "Иди за мной."
            show girl at right with fastdissolve
            l "Ага..."
            scene street3 with fade
            "Она крадучись последовала за парнем."
            "Как вдруг..."
            play sound "audio/zombie.mp3"
            show f w bl at left with fastdissolve
            play music "audio/напряг4.mp3"
            f  w bl an "Чёрт."
            show girl at right with fastdissolve
            l shock "Это..."
            scene street3 with fade
            "Борец закрыл Лайлу своей спиной..."
            "К ним навстречу летел юноша, за которым, не отставая, мчался зомбак..."
            show b cr1 at right with fastdissolve
            "ПОМОГИТЕ!!!"
            show f w bl at left with fastdissolve
            window hide

            menu:
                "Помочь":
                    jump help_yes
                "Уйти прочь":
                    jump help_no
            window show

        label help_yes:
            show f w bl at left with fastdissolve
            f "Беги сюда."
            scene street3 with fade
            "Парень в фиолетовой форме, как вихрь промчался мимо борца и пополнил число стоящих за спиной."
            show b an at right with fastdissolve
            b "Давай, замочи его, полчаса за мной гонялся."
            scene street3 with fade
            "Борец на секунду бросил взгляд на юношу. Зомби ещё добегал до своего ужина."
            show f w bl at left with fastdissolve
            f w bl sm "Так мы нарушили вашу ночную пробежку?"
            show b at right with fastdissolve
            b sm "Не не не."
            show зомби мэн with deathfade
            zombie "ХАГГХААГХ!!!!!"
            scene street3 with fade
            "Резкий поворот, быстрый удар, искра, буря, безумие."
            stop music fadeout 2.0
            "Дальше всё, как в тумане..."
            scene black with fade
            jump end3



        label end3:
            play music "audio/финиш3.mp3"
            centered "Как оказалось - спасённый юноша отделился от группы при нападении зомби."
            centered "Люди вышли на улицу в поисках дополнительной провизии, но столкнулись с огромной группой голодных тварей."
            centered "Кто-то уцелел, кто-то нет..."
            centered "В знак благодарности юноша предложил присоединится своим спасителям к его команде."
            centered "Тяжёлые времена сплочают."
            centered "Борец с Лайлой не отказались от предложения..."
            centered "А уже этим утром, сидя на кухне большого частного дома, они слушали новости о том, что спецслужбы выехали за гражданами в их район..."
            play sound "audio/уведа.mp3"
            $ finale.grant()
            centered "Конец основной истории."
        return

        label help_no:
            play music "audio/куст.mp3"
            hide b
            show f w bl at left with fastdissolve
            f "Лайла, прыгай в кусты!"
            show girl at right with fastdissolve
            l shock "Чего?"
            scene street3 with fade
            "Борец за шкирку затащил её в ближайшие кусты."
            "Вдруг за их спинами раздался подозрительный шорох..."
            show girl at right with fastdissolve
            show f w bl at left with fastdissolve
            l "Это...эт..о"
            show zombie
            play sound "audio/рык.mp3"
            f "Бл*ть."
            jump dead_end

        

            
        label s_bankf:
            scene bank with fade
            "Зайдя, парень первым делом встретился с серьёзным пронзительным взглядом..."
            "Соревнования в гляделки можно считать открытыми."
            show sec with fastdissolve
            sec "..."
            hide sec
            show f w bl with fastdissolve
            f w bl "..."
            hide f w bl
            show sec  with fastdissolve
            sec mad "..."
            hide sec
            show f w bl with fastdissolve
            f w bl e "..."
            hide f w bl
            show sec  with fastdissolve
            sec mad "Вы что-то хотели?"
            hide sec
            show f w bl with fastdissolve
            f "Да нет, просто захотелось на вас посмотреть."
            f "Говорю же, ЧП. Новости совсем не читаете?"
            hide f w bl
            scene bank with fade
            "Охранник и не подумал взять в руки телефон."
            show f w bl with fastdissolve
            f w bl e "(Ну и что с ним делать?)"
            window hide

            menu:
                "Договориться":
                    jump negotiation_alonef
                "Свалить отсюда":
                    jump get_out_alonef
                "Пришить его":
                    jump kill_the_bastard_alonef

            window show



        label negotiation_alonef:
            show f w bl with fastdissolve
            f "Советую вам всё же открыть новости..."
            hide f w bl
            show sec  with fastdissolve
            sec mad "..."
            hide sec
            show f w bl with fastdissolve
            f w bl e "Или мне помочь?"
            scene bank with fade
            "Тяжело вздохнув, охранник всё же открыл первый попавшийся новостной паблик. Сказать, что выражение его лица было удивлённым - ничего не сказать..."
            play sound "audio/уведа.mp3"
            $ honey.grant()
            show sec at right with fastdissolve
            show f w bl at left with fastdissolve
            sec "Так это правда?" 
            f w bl sm "Она самая."
            sec "Пффф, чувствую себя отвратно. Прости, что принял тебя за очередного шутника."
            f w bl sm "Да ладно. Излишки профессии, понимаю."
            stop music fadeout 2.0
            scene black with fade
            scene restroom with fade
            "Некоторое время спустя..."
            play music "audio/меланхолия.mp3"
            "..."
            "Борец сидел в комнате отдыха, погружённый в пучину собственных мыслей..."
            "Ощущение пустоты не покидало его с подвала..."
            "В ту злосчастную минуту, когда жизнь разделилась на до и после, эмоции захлестнули неистово. "
            "Они бы сожгли его до последней капли..."
            "Однако парень умел отключать свои чувства, предоставляя бразды правления холодному рассудку..."
            "Его нельзя назвать бессердечным."
            "Когда сталкиваешься с чем-то чересчур часто впечатления меркнут, становятся блёклыми, как старая фотоплёнка. Не потому, что стали менее значимыми, а потому, что утратили новизну...."
            "Человек привыкает ко многому..."
            "Борец давно привык к смерти..."
            "Но в этот раз всё было иначе. Погиб последний, близкий его душе, человек, и эмоции прорвались наружу..."
            "Однако, он смог взять их под контроль."
            "Высказал смерти своё пренебрежение... там..."
            "...в парке..."
            "..."
            show sec at right with fastdissolve
            sec "Эй, я зайду?"
            show f at left with fastdissolve
            f "Заходи."
            sec sm "У меня неплохие новости."
            sec "Эта зараза ещё не дошла до западной части страны. Там и  планируют обосноваться."
            scene restroom with fade
            "Повисло молчание."
            "Каждый задумался о чём-то своём..."
            "Охранник почесал затылок, он принял решение."
            show sec at right with fastdissolve
            stop music fadeout 2.0
            sec "Нуу, пойдём."
            show f at left with fastdissolve
            f e "И куда же?"
            sec "За едой и в машину."
            scene black with fade
            play music "audio/финиш.mp3"
            centered "Как оказалось - у охранника были связи в западной службе безопасности."
            centered "Которые оперативно предоставили безопасный маршрут до будущей главной вооружённой базы..."
            centered "Мир уже не будет прежним..."
            centered "Но утренние новости, переданные по машинной магнитоле, заставили двух мужчин улыбнуться."
            centered "А одного задуматься о собственном искуплении..."
            play sound "audio/уведа.mp3"
            $ finale.grant()
            centered "Конец основной истории."
        return



        label get_out_alonef:
            scene bank with fade
            "Терпение Борца лопнуло."
            "Спорить дальше - желания не было."
            "Парень развернулся и ушёл."
            scene street with fade
            "Он долго бродил по улицам..."
            "Лунный свет согревал его разбитую душу..."
            "Брат...Девушка, которую он беспощадно бросил..."
            scene black 
            scene street with fade
            "Казалось тьма поглотила его..."
            "Однако после каждой ночи восходит яркое солнце..."
            scene black with fade
            play music "audio/пупупу.mp3"
            centered "Продолжая шататься по улицам,"
            centered "Парень наткнулся на малюток. Брат с сестрой обнимали своих родителей."
            centered "Которые отдали за них свои жизни, желая сохранить самое драгоценное..."
            centered "Новые твари уже были на подходе."
            centered "Однако это неважно..."
            centered "..."
            centered "Борец спас детей."
            centered "..."
            centered "Даже самые тёмные души могут стать светлыми...."
            play sound "audio/уведа.mp3"
            $ finale.grant()
            centered "Конец основной истории."
        return
            
    


        label kill_the_bastard_alonef:
            stop music fadeout 2.0
            scene bank with fade
            "Борец незаметно сократил дистанцию, насколько это было возможно."
            show f w bl with fastdissolve
            show sec with fastdissolve
            "В следующий миг парень оказался за спиной охранника. Годы тренировок не прошли даром."
            scene black with fade
            "Он отбросил биту в сторону."
            "Красота движений завораживала, как огонь завораживает летящего мотылька..."
            "Парень молниеносно скрутил мужчине шею. Охранник даже пискнуть не успел. Смерть наступила быстро, безболезненно..."
            scene bank with fade
            show f w bl at left with fastdissolve
            "Не пойми неправильно, приятель."
            scene black with fade
            scene night with fade
            "..."
            play music "audio/экшен.mp3"
            "Некоторое время спустя..."
            "Борец сидел на крыльце банка и курил сигарету..."
            "Дым насквозь пропитывал ночной воздух горечью и мистикой, прежде чем полностью раствориться в лунном сиянии."
            "Прохладный ветер шелестел сочной тёмно-синей листвой."
            "Привкус крови был не только на губах, но и в душе..."
            "Винил ли он себя?"
            scene black with fade
            centered "Терзали ли его муки совести?"
            centered "Кто знает..."
            centered "Известно лишь то, что парень знал про этих тварей куда больше, чем могло показаться." 
            centered "Работа у него действительно интересная..."
            play sound "audio/уведа.mp3"
            $ finale.grant()
            centered "Конец основной истории."
        return
    return


    label end:
        
        play sound "audio/уведа.mp3"
        $ finale.grant()

        scene black with fade

        centered "Конец основной истории."

    return
return
