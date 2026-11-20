from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLD, COLIC, OLD_AGE
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON, PEASANT_WIFE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-303, альбом
# Photos «1899 (ГАПО 182-5-303)» (pk 1238), ч. 3 — лл. 195об–211об, прочитана целиком 25.10.2026; л. 194об — пустой
# бланк ч. 2, л. 195 — шмуцтитул; импорта не было. Счёт общий. Вся запись — на левой странице, причина — на правой.
# Погребали свящ. Александр Васильев Писарев и Павел Богословский. На л. 205 подшита справка пристава 2 стана Спасского
# уезда (июнь 1899, №641) о погребении девочки Авдотьи … 7 л. — не наша.
kirillovo_deaths_1899 = death_records(
    "ГАПО",
    "182",
    "5",
    "303",
    "Кириллово",
    "Казанская церковь",
    1899,
    *death_month(Month.JANUARY,
                 # Агриппина Филипповна, жена Матвея Егоровича Янина («Сырцовъ»)
                 death(2, Gender.FEMALE, 4, 6,
                       deceased=person("Агриппина", "Филиппова", status=PEASANT_WIFE), age=50,
                       relatives=[relative(person("Матѳей", "Егоровъ", "Сырцовъ", comment="он же: Матвей Егорович Янин"), Relationship.HUSBAND)],
                       cause_of_death=COLD,
                       page="195об",
                       reviewed=False),
                 # Параскева Даниловна «Сырцова» — чья жена или дочь, не установлено
                 death(7, Gender.FEMALE, 26, 27,
                       deceased=person("Параскева", "Данилова", "Сырцова"), age=60,
                       cause_of_death=OLD_AGE,
                       page="196об",
                       reviewed=False),
                 ),
    *death_month(Month.APRIL,
                 # Филипп, сын Ивана Герасимовича Мальчикова, р. 5.10.1898 (рожд. 1898 м. №64)
                 death(17, Gender.MALE, 3, 3,
                       deceased=person("Филиппъ", status=PEASANT_SON), age="6 мес",
                       relatives=[relative(person("Иванъ", "Герасимовъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       comment="в подлиннике «½»",
                       page="201об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Алексей, сын Матвея Матвеевича «Сырцова», р. 10.03.1899 (рожд. м. №14)
                 death(26, Gender.MALE, 6, 6,
                       deceased=person("Алексѣй", status=PEASANT_SON), age="4 мес",
                       relatives=[relative(person("Матѳей", "Матѳеевъ", "Сырцовъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       page="206об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
