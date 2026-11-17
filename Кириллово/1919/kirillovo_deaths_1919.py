from verso.ru.dsl import Gender, Month, RecordDefaults, death, death_month, death_records, person
from verso.ru.dsl.causes_of_death import DIARRHEA, SMALLPOX

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО Р-2854-17-41,
# альбом Photos «1919 (ГАПО Р-2854-17-41)» (pk 3699), смерти — лл. 85–94об, прочитаны целиком 27.10.2026; импорта не
# было. Книга ЗАГС — реестр без номеров: день смерти, пол, имя и фамилия (у взрослых и отчество), причина, возраст,
# семейное положение; родителей и родственников нет, поэтому ребёнка с родителями не связать — только по пометке «умер …»
# в книге рождений. Зимой 1919 г. — оспа, летом — понос, осенью — «испанка». Лл. 91об–92 — вторая серия с января по
# ноябрь (в первой графе «Выписк… …ства»?), лл. 93–94об — Гоголев Бор; записей волны там нет.
kirillovo_deaths_1919 = death_records(
    "ГАПО",
    "2854",
    "17",
    "41",
    "Кириллово",
    "",
    1919,
    *death_month(Month.JANUARY,
                 death(None, Gender.FEMALE, 13, None,
                       deceased=person("Евдокия", None, "Мальчикова"),
                       comment="Гражданская регистрация (ЗАГС); лист выцвел и в пятнах: причина «ст…» (старость?), возраст и семейное положение не дочитаны",
                       page="85",
                       reviewed=False),
                 death(None, Gender.FEMALE, 22, None,
                       deceased=person("Анастасия", None, "Мальчикова"),
                       age="6 мес", cause_of_death=SMALLPOX,
                       comment="Гражданская регистрация (ЗАГС); родители не названы",
                       page="85об",
                       reviewed=False),
                 ),
    *death_month(Month.SEPTEMBER,
                 death(None, Gender.FEMALE, 14, None,
                       deceased=person("Варвара", "Павлова", "Мальчикова"),
                       age="9 мес", cause_of_death=DIARRHEA,
                       comment="Гражданская регистрация (ЗАГС); дочь Павла …; рождение (≈ декабрь 1918) не найдено",
                       page="91",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово"),
    civil=True,
)
