from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COUGH, OLD_AGE, WEAKNESS
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, SOLDIER

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-293, альбом
# Photos «1904 (ГАПО 182-5-293)» (pk 1389), ч. 3 — лл. 124об–146об, 62 муж. / 56 жен., прочитана целиком 26.10.2026; л. 124 —
# шмуцтитул; импорта не было. Вся запись — на левой странице; графа возраста у сгиба. Погребали свящ. Александр Васильев
# Писарев и Павел Богословский. 28.05.1904 (ж. №23) погребена «Семена Васильева Рокина дочь Агафія» — фамилия другая, не
# взята; 26.01 (м. №2) — Иван Платонович «Юдинъ», 70, не Юлин.
kirillovo_deaths_1904 = death_records(
    "ГАПО",
    "182",
    "5",
    "293",
    "Кириллово",
    "Казанская церковь",
    1904,
    *death_month(Month.JUNE,
                 # Агафия, дочь Семена Васильевича Мальчикова («Юлинъ»), р. 5.02.1904 (рожд. ж. №12)
                 death(27, Gender.FEMALE, 8, 9,
                       deceased=person("Агафія", status=PEASANT_DAUGHTER), age="6 мес",
                       relatives=[relative(person("Семенъ", "Васильевъ", "Юлинъ", status=SOLDIER, comment="«запасный рядовой»; = Семен Васильевич Мальчиков"), Relationship.FATHER)],
                       comment="в подлиннике «½ г.»",
                       page="135об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Андрей Васильевич Мальчиков (жених 1842 №…, 21 г.)? — фамилия читается неуверенно
                 death(40, Gender.MALE, 27, 28,
                       deceased=person("Андрей", "Васильевъ", "Мальчиковъ", comment="фамилия читается неуверенно («Ма…чиковъ»); = Андрей Васильевич Мальчиков (брак 1842)?"),
                       age=85,
                       cause_of_death=OLD_AGE,
                       page="136об",
                       reviewed=False),
                 ),
    *death_month(Month.SEPTEMBER,
                 # Елисавета, дочь Михаила Егоровича «Кистенева» (= «Малахаевъ»), р. 10.09.1904 (рожд. ж. №69)
                 death(39, Gender.FEMALE, 10, 12,
                       deceased=person("Елисавета", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Михаилъ", "Егоровъ", "Кистеневъ", comment="= Михаил Егорович Малахаев"), Relationship.FATHER)],
                       cause_of_death=WEAKNESS,
                       comment="возраст в сгибе («2 …»); день смерти совпадает с днём рождения — так в подлиннике",
                       page="139об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Мария, дочь Михаила Константиновича Мальчикова, р. 11.10.1904 (рожд. ж. №78)
                 death(44, Gender.FEMALE, 11, 12,
                       deceased=person("Марія", status=PEASANT_DAUGHTER), age="1 дн",
                       relatives=[relative(person("Михаилъ", "Константиновъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=WEAKNESS,
                       comment="возраст в сгибе читается неуверенно",
                       page="141об",
                       reviewed=False),
                 ),
    *death_month(Month.NOVEMBER,
                 # Феодосия, дочь Дмитрия Андреевича «Стрекалина» (= «Малахаевъ», «Кистеневъ»), р. 29.05.1904 (рожд. ж. №41)
                 death(52, Gender.FEMALE, 16, 17,
                       deceased=person("Ѳеодосія", status=PEASANT_DAUGHTER), age="6 мес",
                       relatives=[relative(person("Димитрій", "Андреевъ", "Стрекалинъ", comment="= Дмитрий Андреевич Малахаев"), Relationship.FATHER)],
                       cause_of_death=COUGH,
                       comment="в подлиннике «½ г.»; причина читается неуверенно («…кашли»)",
                       page="143об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
