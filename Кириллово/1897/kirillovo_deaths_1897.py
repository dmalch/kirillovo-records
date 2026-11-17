from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, WEAKNESS
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON, WIDOW

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-303, альбом
# Photos «1897 (ГАПО 182-5-303)» (pk 1210), ч. 3 — лл. 47об–69об, прочитана целиком 25.10.2026; л. 46об — пустой, л. 47 —
# шмуцтитул; л. 70об — пустой бланк; импорта не было. Два штата, у каждого свой счёт с № 1: штат свящ. Писарева (лл.
# 47об–56об) и штат свящ. Кутина (лл. 58об–69об; с ноября погребает свящ. Павел Богословский); л. 57об в наборе нет. Вся
# запись — на левой странице, причина — на правой. 11.09.1897 погребен Иван Дементьевич «Сѣрковъ» (Ладыгин, 62) и
# 22.04.1897 — Иулиания Дементьевна Ладыгина — дети Дементия, не Сергеевичи; не выписаны.
kirillovo_deaths_1897 = death_records(
    "ГАПО",
    "182",
    "5",
    "303",
    "Кириллово",
    "Казанская церковь",
    1897,
    *death_month(Month.FEBRUARY,
                 # Василий, сын Михаила Константиновича Мальчикова и Варвары Трофимовны Щетининой (брак 1894 №18)
                 death(1, Gender.MALE, 5, 6,
                       deceased=person("Василій", status=PEASANT_SON),
                       relatives=[relative(person("Михаилъ", "Константиновъ", "Мольчиковъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       comment="«Мольчиковъ» — так в подлиннике; возраст у корешка («1 мѣс.»?)",
                       page="47об",
                       reviewed=False),
                 ),
    *death_month(Month.JUNE,
                 # Дарья, дочь Егора Михайловича Янина («Сырцовъ»), р. 15.03.1897 (рожд. ж. №4)
                 death(14, Gender.FEMALE, 20, 21,
                       deceased=person("Дарія", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Егоръ", "Михайловъ", "Сырцовъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       comment="возраст ушёл в корешок",
                       page="51об",
                       reviewed=False),
                 # Пелагия, дочь Василия Степановича Мальчикова, р. 8.10.1896 (рожд. 1896 ж. №68)
                 death(15, Gender.FEMALE, 23, 24,
                       deceased=person("Пелагія", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Василій", "Степановъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       comment="возраст ушёл в корешок",
                       page="51об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Ермолай, сын вдовы Марии Ермолаевны Мальчиковой (чья вдова — не установлено)
                 death(8, Gender.MALE, 11, 12,
                       deceased=person("Ермолай", status=PEASANT_SON), age=2,
                       relatives=[relative(person("Марія", "Ермолаева", "Мальчикова", status=WIDOW), Relationship.MOTHER)],
                       cause_of_death=WEAKNESS,
                       page="52об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
