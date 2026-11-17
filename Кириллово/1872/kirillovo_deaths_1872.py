from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC
from verso.ru.dsl.statuses import (HIEREUS, KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE,
                                   PEASANT_DAUGHTER, PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-732,
# альбом Photos «1872 (ГАПО 182-5-732)» (pk 1348), ч. 3 — лл. 105об–118, 64 погребения; прочитана целиком 05.10.2026.
# Не взят: м10 (18 марта, л. 107об) — «крестьянина Петра Акимова сынъ младенецъ Михаилъ», ½ года: фамилии нет, а
# Петр Акимович бывает и Мальчиков, и Малашин; рождения Михаила в октябре–ноябре 1871 в книге нет.
kirillovo_deaths_1872 = death_records(
    "ГАПО",
    "182",
    "5",
    "732",
    "Кириллово",
    "Казанская церковь",
    1872,
    *death_month(Month.MARCH,
                 # «крестьянина Стефана Фетисова сынъ младенецъ Михаилъ» — Михаил, сын Матвея Степановича Фетисова и
                 # Евдокии Емельяновны Мальчиковой, р. 1.01.1872 (рожд. м. №1)? Отца писец назвал по деду?
                 death(9, Gender.MALE, 11, 12,
                       deceased=person("Михаилъ", status=PEASANT_SON), age="6 мес",
                       relatives=[relative(person("Стефанъ", None, "Ѳетисовъ", comment="так в подлиннике; = Матвей Степанович Фетисов?"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       comment="возраст в подлиннике «½»",
                       page="107об",
                       reviewed=False),
                 ),
    *death_month(Month.JUNE,
                 # Акилина, дочь Алексея Данииловича Янина (Гоголев Бор), р. 2.06.1872 (рожд. ж. №28)
                 death(17, Gender.FEMALE, 24, 26,
                       deceased=person("Акилина", status=PEASANT_DAUGHTER, residence="Гоголев Бор"), age="1 мес",
                       relatives=[relative(person("Алексѣй", None, "Янинъ", comment="отчества нет; = Алексей Даниилович Янин?"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="111об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=KAZENNYJ_PEASANT_MALE, status_female=KAZENNYJ_PEASANT_FEMALE),
)
