from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.causes_of_death import ALCOHOL
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

emmanuilovka_deaths_1913 = death_records(
    "ГАРО",
    "?",
    "?",
    "?",
    "Эммануиловка",
    "?",
    1913,
    *page(
        "?",
        *death_month(
            Month.DECEMBER,
            death(
                11,
                Gender.MALE,
                8,
                10,
                deceased=person("Степан", "Михайлов", "Мальчиков"),
                age=35,
                cause_of_death=ALCOHOL,
                comment=" дата под вопросом по источнику; МК Эммануиловка 1913 (ГАРО)",
            ),
        ),
    ),
    defaults=RecordDefaults(residence="Эммануиловка", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)

kirillovo_deaths_1913 = emmanuilovka_deaths_1913
