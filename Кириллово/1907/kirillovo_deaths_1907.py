from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-298, альбом
# Photos «1907 (ГАПО 182-5-298)» (pk 1335), ч. 3 — лл. 123об–138об, прочитана 26.10.2026 до м. №55 (20 августа); дальше в
# деле л. 139 — следующий год, погребений 20 августа — 31 декабря 1907 в наборе нет. Импорта не было. Возраст и причина у
# сгиба, почти не читаются. Погребали свящ. Александр Васильев Писарев и Павел Богословский. 16.08 (ж. №40) погребена
# «Иакинѳа Герасимова Мала…ова дочь Пелагія» — фамилия не дочитана, не взята.
kirillovo_deaths_1907 = death_records(
    "ГАПО",
    "182",
    "5",
    "298",
    "Кириллово",
    "Казанская церковь",
    1907,
    *death_month(Month.JANUARY,
                 # Стефан, сын Павла Егоровича Янина («Сырцовъ»), р. 10.12.1906 (рожд. 1906 м. №89)
                 death(1, Gender.MALE, None, 1,
                       deceased=person("Стефанъ", status=PEASANT_SON),
                       relatives=[relative(person("Павелъ", "Егоровъ", "Сырцовъ", comment="фамилия читается неуверенно; он же: Янин?"), Relationship.FATHER)],
                       comment="умер 31.12.1906, погребён 1.01.1907; возраст и причина в сгибе",
                       page="123об",
                       reviewed=False),
                 # Семен Максимович «Дунаевъ» — Максимовичи «Дунаевы» = Мальчиковы?
                 death(4, Gender.MALE, 28, 29,
                       deceased=person("Семенъ", "Максимовъ", "Дунаевъ", comment="Максимовичи «Дунаевы» — Мальчиковы?; Семен Максимович Дунаев женат 1906 №35 и записан отцом в рожд. 1907 ж. №64 и 1908 м. №74 — тёзка?"),
                       comment="возраст и причина в сгибе",
                       page="124об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Александра, дочь Павла Егоровича «Кистенева» (= «Малахаевъ»?)
                 death(36, Gender.FEMALE, 28, 29,
                       deceased=person("Александра", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Павелъ", "Егоровъ", "Кистеневъ", comment="он же: Павел Георгиевич Кистенев (поручитель 1906 №6)?"), Relationship.FATHER)],
                       comment="возраст и причина не видны",
                       page="136об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Василий, сын Павла Степановича Мальчикова, р. 30.07.1907 (рожд. м. №68)
                 death(54, Gender.MALE, 17, 18,
                       deceased=person("Василій", status=PEASANT_SON),
                       relatives=[relative(person("Павелъ", "Стефановъ", "Мальчиковъ"), Relationship.FATHER)],
                       comment="правая страница закрыта подклеенным листком — возраст и причина не видны",
                       page="138об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
