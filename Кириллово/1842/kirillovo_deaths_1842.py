from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, NATURAL, PLEURISY, THROAT
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE, PEASANT_DAUGHTER,
                                   PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Ч. 3 — кадры 61–91
# альбома «1842 (ЦГАРМ 57-1-409)», кадр N = л. (662+N)об по штампу; 79 м. / 106 ж.
kirillovo_deaths_1842 = death_records(
    "ЦГАРМ", "57", "1", "409", "Кириллово", "Казанская",
    1842,
    *page("724об",
          *death_month(Month.JANUARY,
                       # Карп Алексеевич — из Гоголевских Алексеевичей Яниных (в families/Янины.md не известен)
                       death(6, Gender.MALE, 15, 17,
                             deceased=person("Семенъ", status=PEASANT_SON, residence="Гоголев Бор"), age=13,
                             relatives=[relative(person("Карпъ", "Алексѣевъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=THROAT,
                             comment="«отъ горлотьи»",
                             reviewed=False),
                       ),
          ),
    *page("727об",
          *death_month(Month.MARCH,
                       # Варвара Емельяновна Янина, вышла за Ивана Петрова в 1820 (брак №11); вдовец женился
                       # вторично 10.06.1842 (брак №37)
                       death(12, Gender.FEMALE, 14, 16,
                             deceased=person("Варвара", "Емельянова"), age=47,
                             relatives=[relative(person("Иванъ", "Петровъ", "Позняковъ"), Relationship.HUSBAND)],
                             reviewed=False),
                       ),
          ),
    *page("732об",
          *death_month(Month.APRIL,
                       # Иван Денисович Янин (не Палкин — у Ивана Денисовича Палкина свои записи в той же книге)
                       death(30, Gender.FEMALE, 8, 10,
                             deceased=person("Евфимія", status=PEASANT_DAUGHTER, comment="в подлиннике «Ерфимія»"), age=0.5,
                             relatives=[relative(person("Иванъ", "Денисовъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             reviewed=False),
                       ),
          ),
    *page("734об",
          *death_month(Month.APRIL,
                       # Домника — дочь Елены Нестеровны Мальчиковой, род. 14.01.1840 (рожд. ж. №7)
                       death(38, Gender.FEMALE, 15, 17,
                             deceased=person("Домника", status=PEASANT_DAUGHTER), age=1,
                             relatives=[relative(person("Иванъ", "Терентьевъ", "Александринъ"), Relationship.FATHER)],
                             cause_of_death=PLEURISY,
                             reviewed=False),
                       ),
          ),
    *page("735об",
          *death_month(Month.APRIL,
                       death(40, Gender.FEMALE, 16, 18,
                             deceased=person("Ирина", "Яковлева"), age=55,
                             relatives=[relative(person("Иванъ", "Ивановъ", "Мальчиковъ"), Relationship.HUSBAND)],
                             reviewed=False),
                       # Устинья Фомина — восприемница 1837–1838 («Устиния Фомина Мальчикова»)
                       death(44, Gender.FEMALE, 18, 20,
                             deceased=person("Устинья", "Ѳомина", comment="в подлиннике «Устина»"), age=50,
                             relatives=[relative(person("Василій", "Герасимовъ", "Мальчиковъ"), Relationship.HUSBAND)],
                             reviewed=False),
                       ),
          ),
    *page("739об",
          *death_month(Month.MAY,
                       # Герасим Федорович Мальчиков, хозяин сем. 553 РС 1834; в families/Мальчиковы.md — «ум. 1838» по РС 1850
                       death(47, Gender.MALE, 1, 3,
                             deceased=person("Герасимъ", "Ѳедоровъ", "Мальчиковъ"), age=60,
                             reviewed=False),
                       # Трифон — сын Федора Антоновича Янина («Хрипунова»), род. 14.04.1842 (рожд. м. №20)
                       death(50, Gender.MALE, 5, 7,
                             deceased=person("Трифонъ", status=PEASANT_SON), age="3 нед",
                             relatives=[relative(person("Ѳедоръ", "Антоновъ", comment="фамилия не записана; Янин"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="в подлиннике возраст «3» без единицы; по рождению 14.04 — три недели",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=KAZENNYJ_PEASANT_MALE,
        status_female=KAZENNYJ_PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
