from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, book,
                          page, person)
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_GIRL, ECON_PEASANT_MALE,
                                   ECON_PEASANT_ZHONKA, PRIEST, SEXTON)

kirillovo_births_1790 = birth_records(
    "ГАРО", "627", "298", "24", "Кириллово", "Успенская",
    1790,
    # Книга 439 — Николай Стефанов
    *book("439", person("Николай", "Стефанов"),
          *page("66",
                *birth_month(Month.AUGUST,
                             birth(1, Gender.FEMALE, 4, 18,
                                   child=person("Евдокия"),
                                   father=person("Влас", "Алексеев", status=SEXTON),
                                   god_parent1=person("Яков", "Михайлов"),
                                   god_parent2=person("Параскева", "Иванова", status=ECON_PEASANT_GIRL)),
                             ),
                ),
          ),
    # Книга 462 — Стефан Казмин
    *book("462", person("Стефан", "Казмин"),
          *page("273", case="25",
                *birth_month(Month.JUNE,
                             birth(1, Gender.MALE, 3, 6,
                                   child=person("Тимофей"),
                                   father=person("Иван", "Степанов", status=SEXTON),
                                   god_parent1=person("Николай", "Степанов", status=PRIEST),
                                   god_parent2=person("Марфа", "Федорова", status=ECON_PEASANT_ZHONKA)),
                             ),
                ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_FEMALE
    ),
)
