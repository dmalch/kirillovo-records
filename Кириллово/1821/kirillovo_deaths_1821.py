from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import NATURAL, SMALLPOX
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Ч. 3 — лл. 332–335.
kirillovo_deaths_1821 = death_records(
    "ЦГА республики Мордовия", "57", "6", "102", "Кириллово", "Успенская",
    1821,
    *page("333",
          *death_month(Month.MARCH,
                       # отец — Герасим Федорович Мальчиков
                       death(12, Gender.FEMALE, 27, None,
                             deceased=person("Ефросинья", status=PEASANT_DAUGHTER), age=3,
                             relatives=[relative(person("Герасимъ", "Федоровъ"), Relationship.FATHER)],
                             cause_of_death=SMALLPOX),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
