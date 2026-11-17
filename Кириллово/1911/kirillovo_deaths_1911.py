from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.statuses import (MAIDEN, PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE,
                                   PEASANT_SON, PEASANT_WIFE)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-302, альбом
# Photos «1911 (ГАПО 182-5-302)» (pk 1302), ч. 3 — лл. 208об–231об (м. №6–72, ж. №2–59), прочитана 26.10.2026; страница
# январских погребений (м. №1–5, ж. №1) не сфотографирована — на л. 208 видны только их причины. Импорта не было. Возраст
# в этом году вписан в основную графу. Погребали свящ. Александр Васильев Писарев и Николай Расказовский.
kirillovo_deaths_1911 = death_records(
    "ГАПО",
    "182",
    "5",
    "302",
    "Кириллово",
    "Казанская церковь",
    1911,
    *death_month(Month.APRIL,
                 # Иаков, сын Григория Ефимовича Стюхина, р. 9.10.1910 (рожд. 1910 м. №85)
                 death(17, Gender.MALE, 1, 2,
                       deceased=person("Іаковъ", status=PEASANT_SON),
                       relatives=[relative(person("Григорій", "Ефимовъ", "Стюхинъ"), Relationship.FATHER)],
                       comment="возраст у сгиба",
                       page="212об",
                       reviewed=False),
                 # Алексей, сын Игната Михайловича Мальчикова, р. 11.03.1911 (рожд. м. №23)
                 death(22, Gender.MALE, 12, 13,
                       deceased=person("Алексѣй", status=PEASANT_SON),
                       relatives=[relative(person("Игнатъ", "Михайловъ", "Мальчиковъ"), Relationship.FATHER)],
                       comment="возраст у сгиба",
                       page="213об",
                       reviewed=False),
                 ),
    *death_month(Month.MAY,
                 # Александра, дочь Григория Семеновича «Назарова», р. 18.04.1910 (рожд. 1910 ж. №28)
                 death(18, Gender.FEMALE, 4, 5,
                       deceased=person("Александра", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Григорій", "Семеновъ", "Назаровъ"), Relationship.FATHER)],
                       comment="возраст у сгиба",
                       page="214об",
                       reviewed=False),
                 # Михаил, сын Михаила Матвеевича Мальчикова, р. 22.05.1911 (рожд. м. №52)
                 death(31, Gender.MALE, 30, 31,
                       deceased=person("Михаилъ", status=PEASANT_SON),
                       relatives=[relative(person("Михаилъ", "Матвѣевъ", "Мальчиковъ"), Relationship.FATHER)],
                       comment="возраст у сгиба",
                       page="216об",
                       reviewed=False),
                 ),
    *death_month(Month.JUNE,
                 # Симеон, сын девицы Параскевы Николаевны Мальчиковой, р. 8.04.1911 (рожд. м. №35)
                 death(35, Gender.MALE, 15, 16,
                       deceased=person("Симеонъ", status=PEASANT_SON),
                       relatives=[relative(person("Параскева", "Николаева", "Мальчикова", status=MAIDEN), Relationship.MOTHER)],
                       comment="возраст у сгиба",
                       page="217об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Андрей, сын Ивана Николаевича «Кистенева» (= Малахаева)
                 death(46, Gender.MALE, 20, 21,
                       deceased=person("Андрей", status=PEASANT_SON),
                       relatives=[relative(person("Иванъ", "Николаевъ", "Кистеневъ"), Relationship.FATHER)],
                       comment="возраст у сгиба",
                       page="220об",
                       reviewed=False),
                 # Анна Флоровна, жена Василия Васильевича Мальчикова (отст. рядовой; дети 1890–1899)
                 death(35, Gender.FEMALE, 31, 1, b_month=Month.AUGUST,
                       deceased=person("Анна", "Ѳлорова", status=PEASANT_WIFE),
                       relatives=[relative(person("Василій", "Васильевъ", "Мальчиковъ"), Relationship.HUSBAND)],
                       age=55,
                       page="223об",
                       reviewed=False),
                 ),
    *death_month(Month.SEPTEMBER,
                 # Матвей Егорович Янин («Сырцовъ»), вдовец Агриппины Филипповны (ум. 1899)
                 death(58, Gender.MALE, 8, 9,
                       deceased=person("Матвѣй", "Егоровъ", "Сырцовъ", comment="«вдовый»; = Матвей Егорович Янин"),
                       age=73,
                       page="225об",
                       reviewed=False),
                 ),
    # Вторая волна (08.11.2026): дети замужних дочерей Мальчиковых, найденные по имени мужа
    *death_month(Month.DECEMBER,
                 # Сергий — сын Федора Трофимовича Паршина и Феодосии Николаевны «Малахаевой», р. 6.09.1909 (рожд. м. №76)
                 death(70, Gender.MALE, 17, 18,
                       deceased=person("Сергій", status=PEASANT_SON), age=3,
                       relatives=[relative(person("Ѳеодоръ", "Трофимовъ", "Паршинъ", comment="в подлиннике «Трафимовъ»"), Relationship.FATHER)],
                       comment="возраст «3» (по рождению 2¼ г.); причина у сгиба не читается; погребалъ свящ. Николай Расказовскій",
                       page="230об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
