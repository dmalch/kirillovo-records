from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLD, OLD_AGE, WEAKNESS
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON, PEASANT_WIFE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-293, альбом
# Photos «1903 (ГАПО 182-5-293)» (pk 1266), ч. 3 — лл. 48об–68об, 54 муж. / 49 жен., прочитана целиком 26.10.2026; л. 48 —
# шмуцтитул, л. 69об — пустой, л. 70об — ведомость; импорта не было. Вся запись — на левой странице; графа возраста — у
# сгиба, женский столбец почти не виден. Погребали свящ. Александр Васильев Писарев и Павел Богословский.
kirillovo_deaths_1903 = death_records(
    "ГАПО",
    "182",
    "5",
    "293",
    "Кириллово",
    "Казанская церковь",
    1903,
    *death_month(Month.MARCH,
                 # Василий, сын Федора Трофимовича Паршина и Феодосии Николаевны «Малахаевой», р. 25.02.1903 (рожд. м. №7)
                 death(9, Gender.MALE, 7, 8,
                       deceased=person("Василій", status=PEASANT_SON), age="2 нед",
                       relatives=[relative(person("Ѳеодоръ", "Трофимовъ", "Паршинъ"), Relationship.FATHER)],
                       cause_of_death=WEAKNESS,
                       page="51об",
                       reviewed=False),
                 # Игнатий, сын Никиты Козьмича Мальчикова
                 death(10, Gender.MALE, 10, 11,
                       deceased=person("Игнатій", status=PEASANT_SON),
                       relatives=[relative(person("Никита", "Косминъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=COLD,
                       comment="возраст в сгибе листа не читается",
                       page="52об",
                       reviewed=False),
                 # Вера Давыдовна, жена Климентия Антоновича Мальчикова (в 1871 — «Ильинъ», в 1873 — «Степановъ»)
                 death(14, Gender.FEMALE, 19, 20,
                       deceased=person("Вѣра", "Давыдова", status=PEASANT_WIFE),
                       relatives=[relative(person("Климентъ", "Антоновъ", "Мальчиковъ"), Relationship.HUSBAND)],
                       cause_of_death=OLD_AGE,
                       comment="возраст в сгибе листа не читается",
                       page="53об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
