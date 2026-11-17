from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, HEADACHE, MEASLES
from verso.ru.dsl.statuses import (HIEREUS, PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE,
                                   PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-305, альбом
# Photos «1892 (ГАПО 182-5-305)» (pk 1370), ч. 3 — лл. 37об–51об, 56 муж. / 40 жен., прочитана целиком 25.10.2026; л. 37 —
# шмуцтитул; импорта не было. Вся запись — на левой странице, причина — на правой. Погребал свящ. Александр Васильев
# Писарев, с ноября и свящ. Василий Георгиевич Кутин; в декабре в селе корь. Кадр «л.54об.-55» — титул книги на 1893 г.
kirillovo_deaths_1892 = death_records(
    "ГАПО",
    "182",
    "5",
    "305",
    "Кириллово",
    "Казанская церковь",
    1892,
    *death_month(Month.MAY,
                 # Александра, дочь Семена Ивановича Назарова, р. 17.04.1892 (рожд. ж. №19 — восприемник Дмитрий Малахаев)
                 death(14, Gender.FEMALE, 2, 3,
                       deceased=person("Александра", status=PEASANT_DAUGHTER), age="2 нед",
                       relatives=[relative(person("Симеонъ", "Ивановъ", "Назаровъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="единица возраста в подлиннике неясна («1 …»); по рождению ей 2 недели",
                       page="41об",
                       reviewed=False),
                 # Кирилл, сын Григория Трофимовича Щетинина, р. 14.03.1892 (рожд. м. №9 — восприемник Дмитрий Малахаев)
                 death(15, Gender.MALE, 19, 20,
                       deceased=person("Кириллъ", status=PEASANT_SON), age="2 мес",
                       relatives=[relative(person("Григорій", "Трофимовъ", "Щетининъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="41об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Максим, сын Ивана Матвеевича Фетисова, р. 13.08.1891 (рожд. 1891 м. №65 — восприемник Василий Степанович
                 # Мальчиков)
                 death(31, Gender.MALE, 29, 30,
                       deceased=person("Максимъ", status=PEASANT_SON), age="11 мес",
                       relatives=[relative(person("Иванъ", "Матвѣевъ", "Ѳетисовъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="45об",
                       reviewed=False),
                 # Гавриил, сын Николая Ильича Ковалькова, р. 15.07.1892 (рожд. м. №35 — восприемница Пелагия Михайловна
                 # Юлина)
                 death(32, Gender.MALE, 29, 30,
                       deceased=person("Гавріилъ", status=PEASANT_SON), age="2 нед",
                       relatives=[relative(person("Николай", "Ильинъ", "Ковальковъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="45об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Михаил, сын Якова Антоновича Егорова, р. 7.11.1890 (рожд. 1890 м. №66 — восприемник Герасим Яковлевич
                 # Мальчиков)
                 death(34, Gender.MALE, 15, 16,
                       deceased=person("Михаилъ", status=PEASANT_SON),
                       relatives=[relative(person("Яковъ", "Антоновъ", "Егоровъ"), Relationship.FATHER)],
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="возраст и причина у корешка",
                       page="45об",
                       reviewed=False),
                 # Андрей Константинович «Малахаевъ», отставной рядовой — Андрей Константинович Мальчиков, отец Дмитрия
                 # и Ильи Андреевичей «Малахаевых»? не установлено
                 death(36, Gender.MALE, 21, 23,
                       deceased=person("Андрей", "Константиновъ", "Малахаевъ", status="отставной рядовой"), age=55,
                       cause_of_death=HEADACHE,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="46об",
                       reviewed=False),
                 ),
    *death_month(Month.NOVEMBER,
                 # Параскева, дочь Василия Сергеевича Ладыгина («Сѣрковъ»)
                 death(34, Gender.FEMALE, 26, 27,
                       deceased=person("Параскева", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Василій", "Сергѣевъ", "Сѣрковъ", comment="= Василий Сергеевич Ладыгин"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="возраст в дыре листа",
                       page="48об",
                       reviewed=False),
                 # Андрей, сын Егора Федоровича Янина («Сырцевъ»), р. 12.10.1892 (рожд. м. №61)
                 death(44, Gender.MALE, 30, 1,
                       b_month=Month.DECEMBER,
                       deceased=person("Андрей", status=PEASANT_SON),
                       relatives=[relative(person("Егоръ", "Ѳеодоровъ", "Сырцевъ", comment="= Егор Федорович Янин"), Relationship.FATHER)],
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="записан под «Декабрь»; возраст и причина в дыре листа",
                       page="48об",
                       reviewed=False),
                 ),
    *death_month(Month.DECEMBER,
                 # Иван, сын Андрея Николаевича «Малахаева», р. 13.08.1892 (рожд. м. №44)
                 death(53, Gender.MALE, 21, 22,
                       deceased=person("Іоаннъ", status=PEASANT_SON), age="3 мес",
                       relatives=[relative(person("Андрей", "Николаевъ", "Малахаевъ"), Relationship.FATHER)],
                       cause_of_death=MEASLES,
                       priest=person("Василій", "Георгіевъ", "Кутинъ", status=HIEREUS),
                       comment="возраст читается неуверенно; по рождению 13.08.1892 ему 4 мес.",
                       page="50об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
