from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, COUGH
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   HIEREUS, PEASANT_DAUGHTER, PEASANT_SON, SOLDIER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-296,
# альбом Photos «1884 (ГАПО 182-5-296)» (pk 1286), ч. 3 — лл. 66об–99об, 77 муж. и 54 жен.; прочитана целиком
# 12.10.2026; заверено 2 января 1885 г. Вся запись — на левой странице, причина смерти — на правой. Погребал настоятель,
# священник Василий Иоаннов Ремезов. 11.01.1884 умер и погребён 12-го псаломщик диакон Матфей Кондратьевич
# Рождественский, 55 л.
kirillovo_deaths_1884 = death_records(
    "ГАПО",
    "182",
    "5",
    "296",
    "Кириллово",
    "Казанская церковь",
    1884,
    *death_month(Month.APRIL,
                 # Яков, сын Василия Сергеевича Ладыгина («Сѣрковъ»), р. 21.10.1883 (рожд. 1883 м. №88)
                 death(18, Gender.MALE, 11, 12,
                       deceased=person("Яковъ", status=PEASANT_SON), age=0.5,
                       relatives=[relative(person("Василій", "Сергѣевъ", "Сѣрковъ", comment="«Сѣрковъ» — так в подлиннике; = Василий Сергеевич Ладыгин"),
                                           Relationship.FATHER)],
                       cause_of_death=COUGH,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="74об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Козма, сын Федора Климентовича Мальчикова, р. 3.07.1884 (рожд. м. №60)
                 death(30, Gender.MALE, 8, 10,
                       deceased=person("Козма", status=PEASANT_SON), age="1 нед",
                       relatives=[relative(person("Ѳеодоръ", "Климовъ", "Мальчиковъ", status=SOLDIER, comment="«запаснаго рядоваго»"),
                                           Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="78об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Мария, дочь Михаила Петровича Мальчикова (её рождения в DSL нет)
                 death(39, Gender.FEMALE, 21, 22,
                       deceased=person("Марія", status=PEASANT_DAUGHTER), age=0.5,
                       relatives=[relative(person("Михаилъ", "Петровъ", "Мальчиковъ", comment="в подлиннике «Мальчковъ»"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="88об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
