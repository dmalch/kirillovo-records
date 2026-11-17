from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, HIEREUS, PEASANT_DAUGHTER

kirillovo_deaths_1844 = death_records(
    "ЦГАРМ",
    "57",
    "6",
    "261",
    "Кириллово",
    "Казанская церковь",
    1844,
    *page(
        "?",
        *death_month(
            Month.FEBRUARY,
            death(4, Gender.MALE, 11, 14, deceased=person("Ефим", "Иванов", last_name_orig="Лапшин"), age=19, cause_of_death=CONSUMPTION),
        ),
        *death_month(
            Month.SEPTEMBER,
            death(
                25,
                Gender.FEMALE,
                21,
                23,
                deceased=person("Параскева"),
                age=2,
                relatives=[relative(person("Карп", "Антонов", last_name_orig="Янин"), Relationship.FATHER)],
                cause_of_death=COLIC,
            ),
        ),
    ),
    # Вторая волна (07.11.2026): дети дочерей Мальчиковых и Яниных, найдены поиском фамилий мужей по OCR Яндекс.Архива и
    # прочитаны по оригиналам
    *page("?",
          *death_month(Month.MAY,
                       # мать — Ксения Антоновна Янина (брак 1841 №23); Матрона род. 3.04.1844 (рожд. ж. №17)
                       death(14, Gender.FEMALE, 20, 22,
                             deceased=person("Матрона", status=PEASANT_DAUGHTER), age="6 мес",
                             relatives=[relative(person("Иванъ", "Ѳоминъ", "Мекининъ"), Relationship.FATHER)],
                             cause_of_death=None,
                             priest=person("Андрей", "Савельевъ", status=HIEREUS),
                             comment="скан 630; возрастъ «полугоду» — по рожденію ей 1½ мѣс.; причина читается «коликого»?",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
