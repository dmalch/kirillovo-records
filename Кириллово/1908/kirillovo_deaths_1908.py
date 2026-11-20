from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.statuses import MAIDEN, PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON, PEASANT_WIFE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-298, альбом
# Photos «1908 (ГАПО 182-5-298)» (pk 1255), ч. 3 — л. 179 шмуцтитул, лл. 179об–205об, 75 муж. / 71 жен., прочитана целиком
# 26.10.2026; л. 204об — лист другого причта (свящ. Алексей Антонов); импорта не было. Возраст и причина у сгиба, почти не
# читаются. Погребали свящ. Александр Васильев Писарев и Павел Богословский.
kirillovo_deaths_1908 = death_records(
    "ГАПО",
    "182",
    "5",
    "298",
    "Кириллово",
    "Казанская церковь",
    1908,
    *death_month(Month.FEBRUARY,
                 # Иоанн, сын Петра Федоровича Янина («Сырцовъ»), р. 29.03.1907 (рожд. 1907 м. №17)
                 death(7, Gender.MALE, 8, 9,
                       deceased=person("Іоаннъ", status=PEASANT_SON),
                       relatives=[relative(person("Петръ", "Ѳеодоровъ", "Сырцовъ", comment="он же: Петр Федорович Янин"), Relationship.FATHER)],
                       comment="возраст («1…») и причина в сгибе",
                       page="181об",
                       reviewed=False),
                 ),
    *death_month(Month.APRIL,
                 # Мария, дочь Григория Семеновича «Назарова» и Параскевы Николаевны, р. 29.03.1908 (рожд. ж. №21)
                 death(27, Gender.FEMALE, 25, 26,
                       deceased=person("Марія", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Григорій", "Семеновъ", "Назаровъ"), Relationship.FATHER)],
                       comment="возраст и причина в сгибе",
                       page="187об",
                       reviewed=False),
                 # Матрона Козьминична Мальчикова, девица (восприемница 1899–1903)
                 death(29, Gender.FEMALE, 29, 30,
                       deceased=person("Матрона", "Космина", "Мальчикова", status=MAIDEN),
                       comment="возраст и причина в сгибе",
                       page="188об",
                       reviewed=False),
                 ),
    *death_month(Month.MAY,
                 # Анна Михайловна, жена Николая Петровича Мальчикова (дети 1881, 1883)
                 death(33, Gender.FEMALE, 12, 13,
                       deceased=person("Анна", "Михайлова", status=PEASANT_WIFE),
                       relatives=[relative(person("Николай", "Петровъ", "Мальчиковъ"), Relationship.HUSBAND)],
                       comment="возраст и причина в сгибе",
                       page="189об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Параскева, дочь Владимира Дмитриевича «Кистенева» (брак 1907 №19)
                 death(62, Gender.FEMALE, 17, 18,
                       deceased=person("Параскева", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Владиміръ", "Димитріевъ", "Кистеневъ"), Relationship.FATHER)],
                       comment="возраст и причина в сгибе; рождение не найдено",
                       page="201об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
