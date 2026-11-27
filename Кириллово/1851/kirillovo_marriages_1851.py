from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, SOLDIER_WIDOW

kirillovo_marriages_1851 = marriage_records(
    "ЦГАРМ",
    "57",
    "1",
    "427",
    "Кириллово",
    "Казанская церковь",
    1851,
    *page(
        "?",
        *marriage_month(
            Month.JULY,
            marriage(
                15,
                1,
                groom=person("Конон", "Николаев", last_name_orig="Макушин"),
                groom_marriage_num=2,
                bride=person("Феврония", "Иванова", last_name_orig="Митрошина", status=SOLDIER_WIDOW, comment="вдова солдатка"),
                bride_marriage_num=2,
                witness1=person("Андрей", "Григорьев", last_name_orig="Мальчиков"),
                witness2=person("Иосиф", "Сидоров", last_name_orig="Верхов"),
                witness3=person("Петр", "Григорьев", last_name_orig="Мальчиков"),
                witness4=person("Дмитрий", "Митрофанов", last_name_orig="Верхов"),
            ),
        ),
    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
