from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, NATURAL, SCARLATINA
from verso.ru.dsl.statuses import (HIEREUS, KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE,
                                   PEASANT_DAUGHTER, PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-732,
# альбом Photos «1873 (ГАПО 182-5-732)» (pk 1270), ч. 3 — прочитана целиком 19.10.2026. Книга ведётся по двум штатам,
# у каждого свой счёт с № 1: штат свящ. Василия Иоаннова Ремезова — лл. 158об–168об (28 муж. / 32 жен.), штат иерея
# Павла Феофанова Кроткова — лл. 170об–181 (32 муж. / 29 жен.). Вся запись — на левой странице, причина — на правой.
kirillovo_deaths_1873 = death_records(
    "ГАПО",
    "182",
    "5",
    "732",
    "Кириллово",
    "Казанская церковь",
    1873,
    # --- штат свящ. Василия Ремезова ---
    *death_month(Month.JULY,
                 # Козьма Андреянович Мальчиков
                 death(11, Gender.MALE, 20, 23,
                       deceased=person("Козма", "Андріановъ", "Мальчиковъ", comment="в подлиннике «Мамчиковъ»"), age=55,
                       cause_of_death=NATURAL,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="162об",
                       reviewed=False),
                 ),
    *death_month(Month.SEPTEMBER,
                 # Федор, сын Сергея Карповича Янина («Хрипуновъ»; в 1871 — «Сырцевъ»)
                 death(18, Gender.MALE, 20, 21,
                       deceased=person("Ѳедоръ", status=PEASANT_SON), age=2,
                       relatives=[relative(person("Сергѣй", "Карповъ", "Хрипуновъ", comment="«Хрипуновъ» — так в подлиннике; = Сергей Карпович Янин"),
                                           Relationship.FATHER)],
                       cause_of_death=SCARLATINA,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="164об",
                       reviewed=False),
                 # Анна, дочь Семена Родионовича Янина («Алешинъ», Гоголев Бор), р. 28.01.1873 (рожд. ж. №3 штата Ремезова)
                 death(24, Gender.FEMALE, 25, 26,
                       deceased=person("Анна", status=PEASANT_DAUGHTER, residence="Гоголев Бор"), age=0.5,
                       relatives=[relative(person("Семенъ", "Родіоновъ", "Алешинъ", comment="«Алешинъ» — так в подлиннике; = Семен Родионович Янин"),
                                           Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       comment="возраст в подлиннике «½»",
                       page="164об",
                       reviewed=False),
                 ),
    # --- штат иерея Павла Кроткова (свой счёт с № 1) ---
    *death_month(Month.AUGUST,
                 # Мария, дочь Ивана Климентовича Мальчикова
                 death(13, Gender.FEMALE, 2, 4,
                       deceased=person("Марія", status=PEASANT_DAUGHTER), age=1,
                       relatives=[relative(person("Иванъ", "Климентовъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Павелъ", "Ѳеофановъ", "Кротковъ", status=HIEREUS),
                       page="176об",
                       reviewed=False),
                 ),
    *death_month(Month.SEPTEMBER,
                 # Дарья, дочь Сергея Дементьевича Ладыгина («Серковъ») и Пелагии Семеновны Мальчиковой, р. 14.04.1873 (рожд.
                 # ж. №13 штата Кроткова)
                 death(24, Gender.FEMALE, 21, 24,
                       deceased=person("Дарья", status=PEASANT_DAUGHTER), age="4 мес",
                       relatives=[relative(person("Сергій", "Дементьевъ", "Серковъ", comment="«Серковъ» — так в подлиннике; = Сергей Дементьевич Ладыгин"),
                                           Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Павелъ", "Ѳеофановъ", "Кротковъ", status=HIEREUS),
                       comment="возраст «4 м.» исправлен по другой цифре; по рождению — 5 мес",
                       page="178об",
                       reviewed=False),
                 ),
    *death_month(Month.DECEMBER,
                 # Иван, сын Ивана Ивановича Мальчикова, р. 4.01.1873 (рожд. м. №2 штата Кроткова)
                 death(31, Gender.MALE, 25, 27,
                       deceased=person("Иванъ", status=PEASANT_SON), age=1,
                       relatives=[relative(person("Иванъ", "Ивановъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Павелъ", "Ѳеофановъ", "Кротковъ", status=HIEREUS),
                       page="180об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=KAZENNYJ_PEASANT_MALE, status_female=KAZENNYJ_PEASANT_FEMALE),
)
