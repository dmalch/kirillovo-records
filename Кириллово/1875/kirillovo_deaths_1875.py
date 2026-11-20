from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, SMALLPOX
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   HIEREUS, PEASANT_DAUGHTER, PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-732,
# альбом Photos «1875 (ГАПО 182-5-732)» (pk 1262), ч. 3 — лл. 280об–299об, 64 муж. / 60 жен., прочитана целиком
# 24.10.2026; импорта не было. Вся запись — с возрастом и причиной — на левой странице. Погребал настоятель свящ.
# Василий Иоаннов Ремезов (в июне–августе — и свящ. Поликарп Архангельский, в ноябре–декабре — свящ. Афанасий Васильев
# Богоявленский). Летом и осенью — оспа.
kirillovo_deaths_1875 = death_records(
    "ГАПО",
    "182",
    "5",
    "732",
    "Кириллово",
    "Казанская церковь",
    1875,
    *death_month(Month.JANUARY,
                 # Иоанн, сын Никиты Козьмича Мальчикова
                 death(7, Gender.MALE, 6, 7,
                       deceased=person("Іоаннъ", status=PEASANT_SON), age="6 мес",
                       relatives=[relative(person("Никита", "Казминъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       comment="возраст в подлиннике «½»",
                       page="280об",
                       reviewed=False),
                 ),
    *death_month(Month.MARCH,
                 # Домника, дочь Михаила Андреяновича Янина («Сырдцевъ»)
                 death(13, Gender.FEMALE, 1, 4,
                       deceased=person("Домника", status=PEASANT_DAUGHTER), age=1,
                       relatives=[relative(person("Михаилъ", "Андріановъ", "Сырдцевъ", comment="он же: Михаил Андреянович Янин"), Relationship.FATHER)],
                       cause_of_death=SMALLPOX,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="284об",
                       reviewed=False),
                 ),
    *death_month(Month.APRIL,
                 # Варвара, дочь Ивана Романовича Мальчикова
                 death(18, Gender.FEMALE, 21, 22,
                       deceased=person("Варвара", status=PEASANT_DAUGHTER), age="5 нед",
                       relatives=[relative(person("Иванъ", "Романовъ", "Мальчиковъ", comment="в подлиннике «Мамчиковъ»"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       comment="подписал только псаломщик диакон Матфей Рождественский",
                       page="286об",
                       reviewed=False),
                 ),
    *death_month(Month.SEPTEMBER,
                 # Анастасия, дочь Михаила Петровича Мальчикова
                 death(40, Gender.FEMALE, 26, 27,
                       deceased=person("Анастасія", status=PEASANT_DAUGHTER), age="6 мес",
                       relatives=[relative(person("Михаилъ", "Петровъ", "Мальчиковъ", comment="в подлиннике «Мамчиковъ»"), Relationship.FATHER)],
                       cause_of_death=SMALLPOX,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       comment="возраст в подлиннике «½»",
                       page="293об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
