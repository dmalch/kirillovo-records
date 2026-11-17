from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_GIRL, ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE, HIEREUS

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (опознаны по имени и
# отчеству — фамилий в книге нет). Ч. 2 — лл. 93–97 (54 брака).
kirillovo_marriages_1820 = marriage_records(
    "ЦГА республики Мордовия", "57", "6", "100", "Кириллово", "Успенская",
    1820,
    *page("93об",
          *marriage_month(Month.JANUARY,
                          # невеста — вероятно, Варвара Емельяновна (Янина), восприемница 1814–1823;
                          # поручитель Лаврентий Федорович — Мальчиков (РС 1811, двор 468, внук Феодосия Петровича)
                          marriage(11, 23,
                                   groom=person("Иванъ", "Петровъ"), groom_marriage_num=1,
                                   bride=person("Варвара", "Емельянова"),
                                   witness1=person("Лаврентій", "Ѳедоровъ"),
                                   witness2=person("Терентій", "Васильевъ"),
                                   witness3=person("Корнила", "Никитенъ"),
                                   priest=person("Николай", "Стефановъ", status=HIEREUS)),
                          ),
          ),
    *page("94",
          *marriage_month(Month.JANUARY,
                          # поручитель Герасим Федорович Мальчиков (МК 1814: «Герасимъ Ѳедоровъ Мальчиковъ»)
                          marriage(13, 23,
                                   groom=person("Ѳока", "Марковъ"), groom_marriage_num=2,
                                   bride=person("Марина", "Маркова"),
                                   witness1=person("Герасимъ", "Ѳедоровъ"),
                                   witness2=person("Макаръ", "Стратоновъ"),
                                   witness3=person("Евсей", "Ѳеодоровъ"),
                                   priest=person("Андрей", "Савельевъ", status=HIEREUS)),
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
