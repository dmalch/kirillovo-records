from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_GIRL, ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE, HIEREUS

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (опознаны по имени и
# отчеству — фамилий в книге нет). Ч. 2 — лл. 356–360 (47 браков).
kirillovo_marriages_1826 = marriage_records(
    "ЦГАРМ", "57", "6", "118", "Кириллово", "Казанская",
    1826,
    *page("358",
          *marriage_month(Month.FEBRUARY,
                          # жених — Архип Павлович Мальчиков, невеста — его жена по ИР 1828 «Стефанида Яковлева»;
                          # поручители — Нестор Дмитриевич и, вероятно, Адриан («Андрей») Григорьевич Мальчиковы
                          marriage(25, 15,
                                   groom=person("Архипъ", "Павловъ"), groom_marriage_num=1,
                                   bride=person("Стефанида", "Яковлева"),
                                   witness1=person("Несторъ", "Дмитріевъ"),
                                   witness2=person("Андрей", "Григорьевъ"),
                                   witness3=person("Антонъ", "Елисеевъ"),
                                   priest=person("Николай", "Стефановъ", status=HIEREUS),
                                   reviewed=False),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_MAIDEN,
        status_bride=ECON_PEASANT_GIRL,
        status_groom=ECON_PEASANT_MALE,
    ),
)
