from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, NATURAL
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER,
                                   PEASANT_SON, WIDOW)

kirillovo_deaths_1850 = death_records(
    "ЦГАРМ",
    "57",
    "1",
    "425а",
    "Кириллово",
    "Казанская церковь",
    1850,
    *page(
        "?",
        *death_month(Month.APRIL, death(5, Gender.FEMALE, 1, 3, deceased=person("Анисия", "Яковлева", last_name_orig="Мальчикова", status=WIDOW), age=73, cause_of_death=NATURAL)),
        *death_month(
            Month.SEPTEMBER,
            death(
                47,
                Gender.MALE,
                14,
                16,
                deceased=person("Андрей", "Ионов", last_name_orig="Мальчиков"),
                age=18,
                relatives=[relative(person("Ион", "Герасимов", last_name_orig="Мальчиков"), Relationship.FATHER)],
                cause_of_death=DIARRHEA,
                comment="возраст 18 или 1 г?",
            ),
        ),
    ),
    # Дописано при сплошном проходе (02.10.2026) по сканам Яндекс.Архива (57-1-425а)
    *page("?",
          *death_month(Month.MARCH,
                       # Григорий — сын Дмитрия Михайловича Янина, род. 2.02.1850 (рожд. м. №11)
                       death(5, Gender.MALE, 7, 9,
                             deceased=person("Григорій", status=PEASANT_SON),
                             relatives=[relative(person("Димитрій", "Михайловъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="в графе возраста «1/2» (полтора месяца?); по рождению 2.02.1850 — пять недель; скан 651",
                             reviewed=False),
                       ),
          *death_month(Month.JUNE,
                       # Акилина — дочь Карпа Антоновича Янина («Сырцевъ»), род. 5.06.1850 (рожд. ж. №51)
                       death(18, Gender.FEMALE, 27, 27,
                             deceased=person("Акилина", status=PEASANT_DAUGHTER),
                             relatives=[relative(person("Карпъ", "Антоновъ", "Сырцевъ", comment="так в подлиннике; Карп Антонович Янин"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="возраст — «…мцъ», число не читается; по рождению 5.06.1850 — три недели; скан 656",
                             reviewed=False),
                       ),
          *death_month(Month.AUGUST,
                       # Иоанн — сын Егора Денисовича Янина («Сырцевъ»), род. 29.05.1850 (рожд. м. №43)
                       death(38, Gender.MALE, 19, 21,
                             deceased=person("Іоаннъ", status=PEASANT_SON), age="3 мес",
                             relatives=[relative(person("Егоръ", "Денисовъ", "Сырцевъ", comment="так в подлиннике; Егор Денисович Янин"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="на полях — позднейшая помета «1853 г. … по отнош.»; скан 665",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
