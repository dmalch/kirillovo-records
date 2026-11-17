from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DROPSY
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   HIEREUS, PEASANT_DAUGHTER, PEASANT_SON, PEASANT_WIFE)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-296,
# альбом Photos «1885 (ГАПО 182-5-296)» (pk 1272), ч. 3 — лл. 165об–192об, 56 муж. / 39 жен. (сходится с ведомостью на
# л. 194об), прочитана целиком 19.10.2026. Вся запись — на левой странице, причина — на правой. Погребал настоятель, свящ.
# Василий Иоаннов Ремезов. Л. 191 — подклеенное предписание благочинного (17.10.1885, № 2930) похоронить крестьянина
# Красной Дубравы Михаила Тарасова Строева, раздавленного колесом на железной дороге. 30.07.1885 погребён Дементий
# Семенович Серков, 84 л. (м. №40) — свёкор Пелагии Семеновны Мальчиковой, не выписан.
kirillovo_deaths_1885 = death_records(
    "ГАПО",
    "182",
    "5",
    "296",
    "Кириллово",
    "Казанская церковь",
    1885,
    *death_month(Month.MAY,
                 # Наталия, дочь Герасима Яковлевича Мальчикова
                 death(20, Gender.FEMALE, 3, 4,
                       deceased=person("Наталія", status=PEASANT_DAUGHTER), age=3,
                       relatives=[relative(person("Герасимъ", "Яковлевъ", "Мальчиковъ", comment="в подлиннике «Мамчиковъ»"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="177об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Ксения Митрофановна, жена Константина Яковлевича Мальчикова («Поздняковъ» 1872–74)
                 death(31, Gender.FEMALE, 17, 18,
                       deceased=person("Ксенія", "Митрофанова", status=PEASANT_WIFE), age=52,
                       relatives=[relative(person("Константинъ", "Яковлевъ", "Мальчиковъ", comment="в подлиннике «Мамчиковъ»"), Relationship.HUSBAND)],
                       cause_of_death=DROPSY,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="186об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Алексей, сын Михаила Петровича Мальчикова, р. 6.10.1885 (рожд. м. №80)
                 death(54, Gender.MALE, 7, 8,
                       deceased=person("Алексѣй", status=PEASANT_SON), age="2 дн",
                       relatives=[relative(person("Михаилъ", "Петровъ", "Мальчиковъ", comment="в подлиннике «Мамчковъ»"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       comment="возраст в подлиннике «2 дня»",
                       page="189об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
