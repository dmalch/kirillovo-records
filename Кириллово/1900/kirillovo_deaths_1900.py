from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, WEAKNESS
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON, SOLDIER

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-307, альбом
# Photos «1900 (ГАПО 182-5-307)» (pk 1196), ч. 3 — лл. 89об–114об, 71 муж. / 57 жен. (по ведомости на л. 115), прочитана
# целиком 25.10.2026; л. 88об — пустой, л. 89 — шмуцтитул; импорта не было. Вся запись — на левой странице, причина — на
# правой. Погребали свящ. Александр Васильев Писарев и Павел Богословский. Вложены справки пристава 2 стана Спасского уезда
# (4.02.1900 №141, 12.05.1900 №546, октябрь 1900 №1207) — о чужих.
kirillovo_deaths_1900 = death_records(
    "ГАПО",
    "182",
    "5",
    "307",
    "Кириллово",
    "Казанская церковь",
    1900,
    *death_month(Month.JULY,
                 # близнецы Николая Гавриловича Спиряева и Параскевы Никитичны Мальчиковой, р. 2.07.1900 (рожд. м. №57, ж. №29)
                 death(37, Gender.MALE, 25, 29,
                       deceased=person("Сергій", status=PEASANT_SON), age="4 нед",
                       relatives=[relative(person("Николай", "Гавриловъ", "Спиряевъ"), Relationship.FATHER)],
                       cause_of_death=WEAKNESS,
                       page="101об",
                       reviewed=False),
                 death(24, Gender.FEMALE, 27, 28,
                       deceased=person("Ольга", status=PEASANT_DAUGHTER), age="1 мес",
                       relatives=[relative(person("Николай", "Гавриловъ", "Спиряевъ"), Relationship.FATHER)],
                       cause_of_death=WEAKNESS,
                       comment="возраст у корешка («1 м.»?)",
                       page="100об",
                       reviewed=False),
                 ),
    *death_month(Month.DECEMBER,
                 # Параскева, дочь Григория Степановича Мальчикова, р. 11.10.1900 (рожд. ж. №48) — здесь отец «Бурлинъ»:
                 # Бурлины = Мальчиковы («Бурлинъ (Мальчиковъ тожъ)», брак 1895 №16)
                 death(47, Gender.FEMALE, 5, 6,
                       deceased=person("Параскева", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Григорій", "Стефановъ", "Бурлинъ", comment="= Григорий Степанович Мальчиков"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       comment="возраст у корешка («3 н.»?)",
                       page="109об",
                       reviewed=False),
                 # Гавриил Васильевич Мальчиков («Юлинъ»), сын Василия Григорьевича
                 death(69, Gender.MALE, 29, 30,
                       deceased=person("Гавріилъ", "Васильевъ", "Юлинъ", status=SOLDIER, comment="«запасный рядовой»; = Гавриил Васильевич Мальчиков"),
                       age=32,
                       cause_of_death=CONSUMPTION,
                       page="113об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
