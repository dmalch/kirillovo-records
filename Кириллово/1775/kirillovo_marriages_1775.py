from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_GIRL, ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE

kirillovo_marriages_1775 = marriage_records(
    "ГАРО", "627", "255", "20", "Кириллово", "Успенская",
    1775,
    *page("2",
          *marriage_month(Month.JANUARY,
                          marriage(1, 9,
                                   groom=person("Леонтий", "Анофриев"), groom_marriage_num=1,
                                   bride=person("Евдокия", "Иванова"),
                                   witness1=person("Данила", "Никитин"),
                                   witness2=person("Егуп", "Михайлов")),
                          marriage(2, 11,
                                   groom=person("Тимофей", "Родионов"), groom_marriage_num=1,
                                   bride=person("Федосья", "Никитина"),
                                   witness1=person("Зот", "Яковлев"),
                                   witness2=person("Василий", "Стефанов")),
                          marriage(3, 18,
                                   groom=person("Петр", "Прокопиев"), groom_marriage_num=1,
                                   bride=person("Агрипина", "Степанова"),
                                   witness1=person("Гаврил", "Фетисов"),
                                   witness2=person("Меркурий", "Александров")),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_MAIDEN,
        status_bride=ECON_PEASANT_GIRL
    ),
)
