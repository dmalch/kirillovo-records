from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_GIRL, ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE, HIEREUS

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (опознаны по имени и
# отчеству — фамилий в книге нет). Ч. 2 — лл. 328–331 (51 брак).
kirillovo_marriages_1821 = marriage_records(
    "ЦГА республики Мордовия", "57", "6", "102", "Кириллово", "Успенская",
    1821,
    *page("328об",
          *marriage_month(Month.FEBRUARY,
                          # жених — Лукьян Михайлович Янин; поручитель Денис Егорович Янин
                          marriage(11, 4,
                                   groom=person("Лукьянъ", "Михайловъ"), groom_marriage_num=1,
                                   bride=person("Пелагія", "Антонова"),
                                   witness1=person("Петръ", "Дмитріевъ"),
                                   witness2=person("Алексей", "Алимовъ"),
                                   witness3=person("Денисъ", "Егоровъ"),
                                   priest=person("Николай", "Стефановъ", status=HIEREUS)),
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
