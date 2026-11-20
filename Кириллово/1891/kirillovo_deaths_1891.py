from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, FEVER, HEADACHE, WHOOPING_COUGH
from verso.ru.dsl.statuses import (HIEREUS, PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE,
                                   PEASANT_SON, PEASANT_WIFE, PRIVATE_SOLDIER, WIDOW)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей), и импортные записи.
# ГАПО 182-5-305, альбом Photos «1891 (ГАПО 182-5-305)» (pk 1307), ч. 3 — лл. 94об–131об, 118 муж. / 123 жен.,
# прочитана целиком 25.10.2026. Январь–февраль — в кадрах «л.94об» … «л.99об», с марта — в кадрах «л.100об» … «л.131»
# (по имени файлов они в альбоме раньше); с л. 119об по л. 131об на бланки подклеены листы без печатной шапки. Вся
# запись — на левой странице, причина — на правой. Погребал свящ. Александр Васильев Писарев. 6.09.1891 умер Федор
# Спиридонович Поздняков (м. №95) — муж Параскевы Герасимовны, отец посмертного Иакова (рожд. м. №74), — не выписан.
kirillovo_deaths_1891 = death_records(
    "ГАПО",
    "182",
    "5",
    "305",
    "Кириллово",
    "Казанская церковь",
    1891,
    *death_month(Month.JANUARY,
                 # Георгий Константинович «Малахаевъ» — Егор Константинович Мальчиков? («Малахаевы» — Константиновичи);
                 # не установлено
                 death(2, Gender.MALE, 3, 5,
                       deceased=person("Георгій", "Константиновъ", "Малахаевъ"), age=51,
                       cause_of_death=CONSUMPTION,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="94об",
                       reviewed=False),
                 ),
    *death_month(Month.FEBRUARY,
                 # вдова Мария Назаровна «Сырцева» — жена Федора Ивановича, в 1865 «Сырцева», в 1866 «Позднякова», в 1874
                 # «Ѳомина»; место в Яниных не установлено
                 death(11, Gender.FEMALE, 21, 23,
                       deceased=person("Марія", "Назарова", "Сырцева", status=WIDOW),
                       cause_of_death=HEADACHE,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="возраст в дыре листа; причина «отъ [го]ловной боли»",
                       page="97об",
                       reviewed=False),
                 ),
    *death_month(Month.APRIL,
                 # Трофим, сын Лаврентия Андреевича Чекмурина, р. 8.04.1891 (рожд. м. №26 — восприемница Матрона Семеновна
                 # Юлина)
                 death(31, Gender.MALE, 14, 14,
                       deceased=person("Трофимъ", status=PEASANT_SON), age="3 дн",
                       relatives=[relative(person("Лаврентій", "Андреевъ", "Чекмуринъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="возраст читается «3 дн.»; по рождению 8.04 ему 6 дней",
                       page="103об",
                       reviewed=False),
                 ),
    *death_month(Month.MAY,
                 # импорт; сверено по скану 25.10.2026 (л. 107об): «крестьянина Алексѣя Герасимова Мальчикова сынъ
                 # Гавріилъ», 1 г., «отъ кашлюши»
                 death(
                     40,
                     Gender.MALE,
                     8,
                     9,
                     deceased=person("Гавриил"),
                     age=1,
                     relatives=[relative(person("Алексей", "Герасимов", last_name_orig="Мальчиков"), Relationship.FATHER)],
                     cause_of_death=WHOOPING_COUGH,
                     page="107об",
                 ),
                 ),
    *death_month(Month.JULY,
                 # импорт; сверено по скану 25.10.2026 (л. 114об): «крестьянина Василія Константинова Мальчикова дочь
                 # Доминика», «отъ колики»; возраст в корешке
                 death(
                     63,
                     Gender.FEMALE,
                     13,
                     14,
                     deceased=person("Домника"),
                     age=0.5,
                     relatives=[relative(person("Василий", "Константинов", last_name_orig="Мальчиков"), Relationship.FATHER)],
                     cause_of_death=COLIC,
                     comment="Возраст в МК в корешке; по рождению 4.01.1891 — ½ года",
                     page="114об",
                 ),
                 ),
    *death_month(Month.AUGUST,
                 # Евдокия, дочь Ивана Яковлевича Седова, р. 3.08.1890 (рожд. 1890 ж. №52 — восприемница Евдокия Васильевна
                 # Мальчикова)
                 death(86, Gender.FEMALE, 21, 22,
                       deceased=person("Евдокія", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Иванъ", "Яковлевъ", "Сѣдовъ"), Relationship.FATHER)],
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="возраст и причина в корешке",
                       page="121об",
                       reviewed=False),
                 # Ирина, дочь Якова Федоровича Сапронова, р. 10.04.1889 (рожд. 1889 ж. №17 — восприемница Параскева
                 # Никитична Мальчикова)
                 death(87, Gender.FEMALE, 23, 24,
                       deceased=person("Ирина", status=PEASANT_DAUGHTER), age=3,
                       relatives=[relative(person("Яковъ", "Ѳеодоровъ", "Сапроновъ"), Relationship.FATHER)],
                       cause_of_death="отъ золотухи",
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="по рождению 10.04.1889 ей 2 г. 4 мес.",
                       page="122об",
                       reviewed=False),
                 ),
    *death_month(Month.SEPTEMBER,
                 # Ксения, дочь Гавриила Васильевича Мальчикова («Юлинъ»), р. 14.01.1891 (рожд. ж. №7)
                 death(112, Gender.FEMALE, 30, 1,
                       b_month=Month.OCTOBER,
                       deceased=person("Ксенія", status=PEASANT_DAUGHTER), age="7 мес",
                       relatives=[relative(person("Гавріилъ", "Васильевъ", "Юлинъ", comment="он же: Гавриил Васильевич Мальчиков"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="в подлиннике «7½» (мес.); запись под октябрём; по рождению ей 8½ мес.",
                       page="127об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Домна Васильевна Мальчикова, жена Василия Леонтьевича Белова (брак 1886 №18)
                 death(114, Gender.FEMALE, 13, 15,
                       deceased=person("Домника", "Васильева", status=PEASANT_WIFE, comment="она же: Домна Васильевна Мальчикова"),
                       age=23,
                       relatives=[relative(person("Василій", "Леонтіевъ", "Бѣловъ", status=PRIVATE_SOLDIER, comment="«рядовой»"), Relationship.HUSBAND)],
                       cause_of_death=FEVER,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="128об",
                       reviewed=False),
                 ),
    *death_month(Month.NOVEMBER,
                 # Петр, сын Василия Леонтьевича Белова и Домны Васильевны Мальчиковой, р. 10.06.1891 (рожд. м. №42)
                 death(114, Gender.MALE, 28, 29,
                       deceased=person("Петръ", status=PEASANT_SON), age="5 мес",
                       relatives=[relative(person("Василій", "Леонтіевъ", "Бѣловъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="в подлиннике «5½ мѣс.»",
                       page="130об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
