from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLD, COLIC, NATURAL
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   HIEREUS, PEASANT_DAUGHTER, PEASANT_SON, RETIRED_SOLDIER, WIDOW)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-732,
# альбом Photos «1874 (ГАПО 182-5-732)» (pk 3711), ч. 3 — лл. 229об–247, 43 муж. / 45 жен., прочитана целиком
# 19.10.2026. Вся запись — на левой странице, причина — в той же строке. Погребали свящ. Василий Иоаннов Ремезов и
# (с августа) свящ. Гавриил Александров Спиридонов.
kirillovo_deaths_1874 = death_records(
    "ГАПО",
    "182",
    "5",
    "732",
    "Кириллово",
    "Казанская церковь",
    1874,
    *death_month(Month.JANUARY,
                 # «отставной рядовой Григорій Ивановъ Юлинъ» — Григорий Иванович «2-й» Мальчиков (~1813, РС 8; отдан в
                 # рекруты 1836), отец Андрея, Никиты и Василия Григорьевичей, которых книги этих лет пишут «Юлиными»
                 death(2, Gender.MALE, 26, 28,
                       deceased=person("Григорій", "Ивановъ", "Юлинъ", status=RETIRED_SOLDIER, comment="«отставной рядовой»; «Юлинъ» — так в подлиннике; он же: Григорий Иванович Мальчиков"),
                       age=60,
                       cause_of_death=NATURAL,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="230об",
                       reviewed=False),
                 ),
    *death_month(Month.FEBRUARY,
                 # Акилина, дочь Матвея Михайловича Лощинина и Евдокии Козьминичны Мальчиковой, р. 11.06.1873 (рожд. 1873
                 # ж. №19 штата Ремезова)
                 death(7, Gender.FEMALE, 11, 12,
                       deceased=person("Акилина", status=PEASANT_DAUGHTER, residence="Гоголев Бор"), age=0.5,
                       relatives=[relative(person("Матвѣй", "Михайловъ", "Лощининъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       comment="возраст в подлиннике «½»",
                       page="230об",
                       reviewed=False),
                 ),
    *death_month(Month.APRIL,
                 # «Антона Иванова Хрипунова сынъ Даніилъ»: Хрипуновы — прозвание Яниных; но Антон Иванович Янин
                 # («Хрипуновъ») умер 4.11.1861, 60 л. — здесь другой Антон Иванович или описка; не установлено
                 death(11, Gender.MALE, 26, 28,
                       deceased=person("Даніилъ", status=PEASANT_SON), age=4,
                       relatives=[relative(person("Антонъ", "Ивановъ", "Хрипуновъ", comment="«Хрипуновъ» — так в подлиннике; он же: Янин? Антон Иванович Янин умер в 1861"),
                                           Relationship.FATHER)],
                       cause_of_death=COLD,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="233об",
                       reviewed=False),
                 ),
    *death_month(Month.JUNE,
                 # Ирина, дочь Федора «Сырцева» (Федор Иванович «Сырцевъ/Хрипуновъ» 1858, 1865? место в Яниных не
                 # установлено); её рождения в книге нет
                 death(19, Gender.FEMALE, 1, 2,
                       deceased=person("Ирина", status=PEASANT_DAUGHTER), age="3 мес",
                       relatives=[relative(person("Ѳеодоръ", None, "Сырцевъ", comment="отчества нет; «Сырцевъ» — прозвание Яниных"),
                                           Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="236об",
                       reviewed=False),
                 # «вдова Параскева Яковлева Мальчикова» — Прасковья Яковлевна, жена Григория Ивановича «2-го» (рожд. 1832:
                 # «Григорій Ивановъ Мальчиковъ» × «Параскева Яковлева»; ~1809 по РС 8), овдовела 26.01.1874 (смерть м. №2)
                 death(21, Gender.FEMALE, 25, 26,
                       deceased=person("Параскева", "Яковлева", "Мальчикова", status=WIDOW), age=65,
                       cause_of_death=NATURAL,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="236об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Тихон, сын Алексея Данииловича Янина (Гоголев Бор), р. 16.05.1874 (рожд. м. №26)
                 death(22, Gender.MALE, 10, 11,
                       deceased=person("Тихонъ", status=PEASANT_SON, residence="Гоголев Бор"), age="2 мес",
                       relatives=[relative(person("Алексѣй", "Даниловъ", "Янинъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="238об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
