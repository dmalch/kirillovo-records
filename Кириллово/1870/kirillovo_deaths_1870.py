from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import FEVER, NATURAL, SMALLPOX
from verso.ru.dsl.statuses import (DEACON, HIEREUS, PEASANT_DAUGHTER, STATE_PEASANT_FEMALE,
                                   STATE_PEASANT_MALE)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-711,
# альбом Photos «1870 (ГАПО 182-5-711)» (pk 3559), ч. 3 — лл. 42об–63об, 144 погребения; прочитана целиком
# 05.10.2026. Не взята: ж34 (21 авг., л. 54об) — «Семена Стефанова Карасева дочь Анисія», 7 л., отъ горячки; мать
# не названа (Семен Степанович Карасев женат с 1844 на Екатерине Васильевне Мальчиковой).
kirillovo_deaths_1870 = death_records(
    "ГАПО",
    "182",
    "5",
    "711",
    "Кириллово",
    "Казанская церковь",
    1870,
    *death_month(Month.MAY,
                 # = Адриан Григорьевич Мальчиков (~1802 по РС 8; хозяин двора 533 в 1834)
                 death(24, Gender.MALE, 25, 26,
                       deceased=person("Андреянъ", "Григорьевъ", "Мальчиковъ"), age=60,
                       cause_of_death=NATURAL,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                       page="48об",
                       reviewed=False),
                 ),
    *death_month(Month.JUNE,
                 # Наталья Матвеевна Фетисова, р. 22.08.1864 (рожд. 1864 ж. №78); мать — Евдокия Емельяновна Мальчикова
                 death(20, Gender.FEMALE, 1, 1,
                       deceased=person("Наталія", status=PEASANT_DAUGHTER), age=5,
                       relatives=[relative(person("Матѳей", "Стефановъ", comment="фамилии нет; он же: Матвей Степанович Фетисов"), Relationship.FATHER)],
                       cause_of_death=SMALLPOX,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="49об",
                       reviewed=False),
                 # Евдокия Михайловна Тихонова (Гоголев Бор), р. 1853; мать — Варвара Андреевна Янина (брак 1852 №39)
                 death(24, Gender.FEMALE, 23, 24,
                       deceased=person("Евдокія", status=PEASANT_DAUGHTER, residence="Гоголев Бор"), age=17,
                       relatives=[relative(person("Михаилъ", "Григорьевъ", "Тихоновъ"), Relationship.FATHER)],
                       cause_of_death=FEVER,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="50об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Ѳекла, дочь Петра Акимовича Мальчикова, р. 22.09.1861 (рожд. 1861 ж. №66)
                 death(52, Gender.FEMALE, 10, 11,
                       deceased=person("Ѳекла", status=PEASANT_DAUGHTER), age=9,
                       relatives=[relative(person("Петръ", "Акимовъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=SMALLPOX,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="59об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=STATE_PEASANT_MALE, status_female=STATE_PEASANT_FEMALE),
)
