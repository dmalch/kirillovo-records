from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import (COLIC, CONSUMPTION, DIARRHEA, DROPSY, FEVER, MEASLES,
                                          NATURAL)
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, HIEREUS, MAIDEN,
                                   PEASANT_DAUGHTER, ZHONKA)

kirillovo_deaths_1851 = death_records(
    "ЦГАРМ",
    "57",
    "1",
    "427",
    "Кириллово",
    "Казанская церковь",
    1851,
    *page(
        "?",
        *death_month(
            Month.APRIL,
            death(
                44,
                Gender.MALE,
                23,
                25,
                deceased=person("Иван", "А?иев", last_name_orig="Мальчиков", comment="Иван А?иев Мальчиков? — отчество частично нечитаемо"),
                age=35,
                cause_of_death=DROPSY,
            ),
            death(
                37,
                Gender.FEMALE,
                11,
                13,
                deceased=person("Марина", "Иванова", last_name_orig="Янина", status=ZHONKA),
                age=75,
            ),
            death(
                48,
                Gender.MALE,
                27,
                29,
                deceased=person("Карп", "Антонов", last_name_orig="Янин"),
                age=38,
                cause_of_death=FEVER,
            ),
        ),
        *death_month(
            Month.JULY,
            death(
                54,
                Gender.FEMALE,
                10,
                12,
                deceased=person("Анна", "Дмитриева", last_name_orig="Янина"),
                age="6 мес",
                relatives=[relative(person("Дмитрий", "Михайлов", last_name_orig="Янин"), Relationship.FATHER)],
                cause_of_death=COLIC,
            ),
        ),
        *death_month(Month.OCTOBER, death(74, Gender.FEMALE, 10, 12, deceased=person("Татьяна", "Нестерова", last_name_orig="Мальчикова", status=MAIDEN), age=18, cause_of_death=CONSUMPTION)),
    ),
    # Дописано при сплошном проходе (02.10.2026) по сканам Яндекс.Архива (57-1-427, каталог 3099f368-…)
    *page("?",
          *death_month(Month.JULY,
                       # «женка» (жена солдата) Агафья Стефановна Сырцева — из Яниных-Сырцевых; чья жена — не сказано
                       death(52, Gender.FEMALE, 5, 7,
                             deceased=person("Агаѳія", "Стефанова", "Сырцева", status=ZHONKA), age=56,
                             cause_of_death=NATURAL,
                             comment="скан 72",
                             reviewed=False),
                       # Ксения Антоновна Янина, жена Ивана Фомича Мекинина (здесь «Ивлюковъ»)
                       death(55, Gender.FEMALE, 13, 15,
                             deceased=person("Ксенія", "Антонова"), age=34,
                             relatives=[relative(person("Иванъ", "Ѳоминъ", "Ивлюковъ", comment="так в подлиннике; в 1848 — «Мекининъ»"), Relationship.HUSBAND)],
                             cause_of_death=CONSUMPTION,
                             comment="скан 73",
                             reviewed=False),
                       ),
          *death_month(Month.AUGUST,
                       # Родион Алексеевич Янин из Гоголева Бора
                       death(62, Gender.FEMALE, 17, 19,
                             deceased=person("Анна", status=PEASANT_DAUGHTER, residence="Гоголев Бор"), age=1,
                             relatives=[relative(person("Родіонъ", "Алексѣевъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             comment="скан 76",
                             reviewed=False),
                       ),
          ),
    # Вторая волна (07.11.2026): дети дочерей Мальчиковых и Яниных, найдены поиском фамилий мужей по OCR Яндекс.Архива и
    # прочитаны по оригиналам
    *page("?",
          *death_month(Month.MARCH,
                       # Пелагия — дочь Гавриила Ивановича Романова и Мелании Романовны Яниной, род. 9.10.1849
                       death(15, Gender.FEMALE, 2, 4,
                             deceased=person("Пелагія", status=PEASANT_DAUGHTER, residence="Гоголев Бор"), age=1,
                             relatives=[relative(person("Гавріилъ", "Ивановъ", "Романовъ"), Relationship.FATHER)],
                             cause_of_death=MEASLES,
                             priest=person("Александръ", "Григорьевъ", "Халевъ", status=HIEREUS),
                             comment="скан 59 (57-1-427)",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
