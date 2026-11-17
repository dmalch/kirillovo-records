from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, MEASLES
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON,
                                   PEASANT_WIFE, RETIRED_SOLDIER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-303, альбом
# Photos «1898 (ГАПО 182-5-303)» (pk 1230), ч. 3 — лл. 114об–146об, 81 муж. / 98 жен. (по ведомости на л. 147об),
# прочитана целиком 25.10.2026; л. 113об — пустой, л. 114 — шмуцтитул; импорта не было. Счёт общий. Вся запись — на левой
# странице, причина — на правой. Погребали свящ. Александр Васильев Писарев и Павел Богословский. С апреля по июнь в селе
# корь (апрель — 32 погребения). На л. 144об вложена записка пристава 2 стана Спасского уезда от 8.10.1908 (№2021) о
# погребении мальчика Алексея Позднякова, 7 л., — бумага 1908 г., попавшая не в свою книгу; не выписана. 25.10.1898
# погребен Иван Матвеевич Бурлин (75; Бурлины — «Мальчиковы тожъ»? не установлено), 8.10.1898 — Евдокия Хрисанфовна
# Позднякова (80; чья — не установлено); не выписаны.
kirillovo_deaths_1898 = death_records(
    "ГАПО",
    "182",
    "5",
    "303",
    "Кириллово",
    "Казанская церковь",
    1898,
    *death_month(Month.FEBRUARY,
                 # Василий, сын Василия Васильевича Мальчикова и Анны Фроловны (р. ок. 1892)
                 death(5, Gender.MALE, 15, 16,
                       deceased=person("Василій", status=PEASANT_SON), age=6,
                       relatives=[relative(person("Василій", "Васильевъ", "Мальчиковъ", status=RETIRED_SOLDIER, comment="«отставной рядовой»"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       comment="возраст — «6», без единицы",
                       page="116об",
                       reviewed=False),
                 ),
    *death_month(Month.APRIL,
                 # Феодора, дочь Егора Михайловича Янина («Сырцовъ»)
                 death(25, Gender.FEMALE, 23, 24,
                       deceased=person("Ѳеодора", status=PEASANT_DAUGHTER), age=5,
                       relatives=[relative(person("Егоръ", "Михайловъ", "Сырцовъ"), Relationship.FATHER)],
                       cause_of_death=MEASLES,
                       page="123об",
                       reviewed=False),
                 # Екатерина, дочь Матвея «Сырцова», р. 23.11.1897? (рожд. 1897 ж. №32 — там отец Матвей Васильевич)
                 death(28, Gender.FEMALE, 27, 28,
                       deceased=person("Екатерина", status=PEASANT_DAUGHTER), age="5 мес",
                       relatives=[relative(person("Матвѣй", "Матвѣевъ", "Сырцовъ", comment="«Матвѣевъ» — так в подлиннике; в рожд. 1899 м. №14 — тоже Матвей Матвеевич (жена Александра Сергеевна), в рожд. 1897 ж. №32 — Матвей Васильевич (жена Александра Степановна): один человек или два — не установлено"), Relationship.FATHER)],
                       cause_of_death=MEASLES,
                       page="124об",
                       reviewed=False),
                 ),
    *death_month(Month.MAY,
                 # Георгий, сын Василия Сергеевича Ладыгина («Сѣрковъ»; сын Пелагии Семеновны Мальчиковой)
                 death(22, Gender.MALE, 1, 1,
                       deceased=person("Георгій", status=PEASANT_SON), age=1,
                       relatives=[relative(person("Василій", "Сергѣевъ", "Сѣрковъ", comment="= Василий Сергеевич Ладыгин"), Relationship.FATHER)],
                       cause_of_death=MEASLES,
                       page="126об",
                       reviewed=False),
                 # Иван, сын Ивана Михайловича Богачева и Марии Андреевны Мальчиковой, р. 17.07.1897 (рожд. 1897 м. №19 штата
                 # Кутина)
                 death(36, Gender.MALE, 23, 24,
                       deceased=person("Іоаннъ", status=PEASANT_SON), age="11 мес",
                       relatives=[relative(person("Иванъ", "Михайловъ", "Богачевъ"), Relationship.FATHER)],
                       cause_of_death=MEASLES,
                       page="131об",
                       reviewed=False),
                 ),
    *death_month(Month.JUNE,
                 # Варвара Трофимовна (Щетинина), жена Михаила Константиновича Мальчикова (брак 1894 №18)
                 death(59, Gender.FEMALE, 18, 19,
                       deceased=person("Варвара", "Трофимова", status=PEASANT_WIFE), age=23,
                       relatives=[relative(person("Михаилъ", "Константиновъ", "Мальчиковъ"), Relationship.HUSBAND)],
                       cause_of_death=CONSUMPTION,
                       comment="в браке 1894 №18 — 25 лет",
                       page="135об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
