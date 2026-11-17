from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, SMALLPOX
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_SON

kirillovo_deaths_1837 = death_records(
    "ЦГАРМ",
    "57",
    "6",
    "172",
    "Кириллово",
    "Казанская церковь",
    1837,
    *page(
        "?",
        *death_month(
            Month.SEPTEMBER,
            death(
                34,
                Gender.MALE,
                24,
                None,
                deceased=person("Василий"),
                age=2,
                relatives=[relative(person("Андреян", "Денисов", last_name_orig="Янин"), Relationship.FATHER)],
                cause_of_death=SMALLPOX,
            ),
        ),
        *death_month(
            Month.OCTOBER,
            death(
                48,
                Gender.FEMALE,
                21,
                None,
                deceased=person("Настасья", "Акимова", last_name_orig="Мальчикова"),
                age=1,
                relatives=[relative(person("Аким", "Григорьев", last_name_orig="Мальчиков"), Relationship.FATHER)],
                cause_of_death=SMALLPOX,
            ),
            death(
                38,
                Gender.MALE,
                22,
                None,
                deceased=person("Михаил", "Андрианов", last_name_orig="Мальчиков"),
                age=4,
                relatives=[relative(person("Андриан", "Григорьев", last_name_orig="Мальчиков"), Relationship.FATHER)],
                cause_of_death=SMALLPOX,
            ),
            death(
                49,
                Gender.FEMALE,
                24,
                None,
                deceased=person("Акилина", "Петрова", last_name_orig="Мальчикова"),
                age=1,
                relatives=[relative(person("Петр", "Григорьев", last_name_orig="Мальчиков"), Relationship.FATHER)],
                cause_of_death=SMALLPOX,
            ),
        ),
        *death_month(
            Month.NOVEMBER,
            death(
                45,
                Gender.MALE,
                26,
                None,
                deceased=person("Иван", "Васильев", last_name_orig="Мальчиков"),
                age=0.5,
                relatives=[relative(person("Василий", "Дмитриев", last_name_orig="Мальчиков"), Relationship.FATHER)],
                cause_of_death=SMALLPOX,
            ),
        ),
    ),
    # Дописано при сплошном проходе по скану (альбом «1837 (ЦГАРМ 57-6-172)», pk 1360)
    *page("688об",
          *death_month(Month.FEBRUARY,
                       # Иван — сын Семена Агаповича Крапивникова и Акилины Павловны Мальчиковой (род. 1836, м. №87)
                       death(2, Gender.MALE, 23, None,
                             deceased=person("Иванъ", status=PEASANT_SON), age=0.5,
                             relatives=[relative(person("Семенъ", "Агаповъ", "Крапивниковъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
