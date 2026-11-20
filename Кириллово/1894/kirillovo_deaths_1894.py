from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, SCARLET_FEVER, WEAKNESS
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON,
                                   PRIVATE_SOLDIER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-306, альбом
# Photos «1894 (ГАПО 182-5-306)» (pk 1231), ч. 3 — лл. 80об–95об, прочитана целиком 25.10.2026; импорта не было. Вся
# запись — на левой странице, причина — на правой. Погребали свящ. Александр Васильев Писарев и Василий Георгиевич
# Кутин.
kirillovo_deaths_1894 = death_records(
    "ГАПО",
    "182",
    "5",
    "306",
    "Кириллово",
    "Казанская церковь",
    1894,
    *death_month(Month.JANUARY,
                 # Иван, сын Егора Михайловича Янина («Сырцевъ»), р. 21.06.1891 (рожд. 1891 м. №50)
                 death(3, Gender.MALE, 29, 30,
                       deceased=person("Іоаннъ", status=PEASANT_SON), age="2 лет 6 мес",
                       relatives=[relative(person("Егоръ", "Михайловъ", "Сырцевъ", comment="он же: Егор Михайлович Янин"), Relationship.FATHER)],
                       cause_of_death=SCARLET_FEVER,
                       comment="в подлиннике «2½ г.»",
                       page="80об",
                       reviewed=False),
                 ),
    *death_month(Month.MAY,
                 # Дмитрий, сын Ивана Ильича Ковалькова, р. 3.05.1894 (рожд. м. №24 — восприемница Татьяна Прокопьевна
                 # Юлина)
                 death(18, Gender.MALE, 21, 22,
                       deceased=person("Димитрій", status=PEASANT_SON), age="3 нед",
                       relatives=[relative(person("Иванъ", "Ильинъ", "Ковальковъ"), Relationship.FATHER)],
                       cause_of_death=WEAKNESS,
                       page="84об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Иван, сын Степана Васильевича Мальчикова («Юлинъ»), р. 19.02.1893 (рожд. 1893 м. №13)
                 death(26, Gender.MALE, 19, 20,
                       deceased=person("Іоаннъ", status=PEASANT_SON), age="1 лет 6 мес",
                       relatives=[relative(person("Стефанъ", "Васильевъ", "Юлинъ", status=PRIVATE_SOLDIER, comment="«отставной рядовой»; он же: Степан Васильевич Мальчиков"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       comment="в подлиннике «1½ г.»",
                       page="87об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Елена, дочь Матвея Васильевича «Сырцева» (поручитель 1892 бр. №18); место в Яниных не установлено
                 death(31, Gender.FEMALE, 19, 20,
                       deceased=person("Елена", status=PEASANT_DAUGHTER), age="3 нед",
                       relatives=[relative(person("Матвѣй", "Васильевъ", "Сырцевъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       comment="возраст читается неуверенно",
                       page="90об",
                       reviewed=False),
                 ),
    *death_month(Month.SEPTEMBER,
                 # Феодосия, дочь Андрея Ивановича Крысанова, р. 27.05.1894 (рожд. ж. №29 — восприемница Пелагия Михайловна
                 # Юлина)
                 death(36, Gender.FEMALE, 28, 29,
                       deceased=person("Ѳеодосія", status=PEASANT_DAUGHTER), age="4 мес",
                       relatives=[relative(person("Андрей", "Ивановъ", "Крысановъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       page="91об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Акилина, дочь Василия Акимовича Жарикова и Дарьи Сергеевны Ладыгиной, р. 14.06.1894 (рожд. ж. №36)
                 death(38, Gender.FEMALE, 3, 4,
                       deceased=person("Акилина", status=PEASANT_DAUGHTER), age="4 мес",
                       relatives=[relative(person("Василій", "Акимовъ", "Жариковъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       page="92об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
