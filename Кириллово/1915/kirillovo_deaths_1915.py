from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON,
                                   PEASANT_WIFE, WIDOW)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-574, альбом
# Photos «1915 (ГАПО 182-5-574)» (pk 1219), ч. 3 — лл. 219об–246об (м. №1–64, ж. №1–66), прочитана целиком 26.10.2026;
# импорта не было. Листы сшиты не по порядку: л. 229об — ноябрь, л. 230об — октябрь, л. 231об — апрель. Погребали свящ.
# Николай Расказовский и Григорий Феодоровский.
kirillovo_deaths_1915 = death_records(
    "ГАПО",
    "182",
    "5",
    "574",
    "Кириллово",
    "Казанская церковь",
    1915,
    *death_month(Month.APRIL,
                 # Александра, дочь Ефрема Михайловича «Кистенева», р. 20.04.1914 (рожд. 1914 ж. №29)
                 death(16, Gender.FEMALE, 1, 2,
                       deceased=person("Александра", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Ефремъ", "Михайловъ", "Кистеневъ"), Relationship.FATHER)],
                       age=1,
                       page="226об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Марфа, дочь Ивана Тимофеевича Коверкина (мать — Анна Климентьевна, рожд. ж. №10?)
                 death(34, Gender.FEMALE, 6, 7,
                       deceased=person("Марѳа", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Иванъ", "Тимоѳеевъ", "Коверкинъ"), Relationship.FATHER)],
                       comment="мать — Анна Климентьевна (Мальчикова?); возраст у края",
                       page="236об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Феврония Климентьевна, жена Федора Самсоновича Янина (урожд. Мальчикова?)
                 death(43, Gender.FEMALE, 9, 10,
                       deceased=person("Ѳевронія", "Климентьева", status=PEASANT_WIFE, comment="урожд. Мальчикова, дочь Климентия Антоновича? не установлено"),
                       relatives=[relative(person("Ѳеодоръ", "Самсоновъ", "Янинъ"), Relationship.HUSBAND)],
                       comment="возраст у края",
                       page="238об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # вдова Анастасия Леонтьевна «Кистенева» — чья вдова, не установлено
                 death(52, Gender.FEMALE, 4, 5,
                       deceased=person("Анастасія", "Леонтьева", "Кистенева", status=WIDOW, comment="чья вдова — не установлено"),
                       age=75,
                       page="230об",
                       reviewed=False),
                 ),
    *death_month(Month.NOVEMBER,
                 # Василий, сын Сергея Гавриловича «Юлина», р. 11.08.1914 (рожд. 1914 м. №66)
                 death(53, Gender.MALE, 16, 17,
                       deceased=person("Василій", status=PEASANT_SON),
                       relatives=[relative(person("Сергѣй", "Гавриловъ", "Юлинъ"), Relationship.FATHER)],
                       comment="возраст у края («1…»)",
                       page="243об",
                       reviewed=False),
                 ),
    *death_month(Month.DECEMBER,
                 # Никита Козьмич Мальчиков, вдовец (жена Дарья Порфирьевна ум. 1909)
                 death(56, Gender.MALE, 5, 6,
                       deceased=person("Никита", "Косминъ", "Мальчиковъ", comment="«вдовъ»"),
                       age=75,
                       page="244об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
