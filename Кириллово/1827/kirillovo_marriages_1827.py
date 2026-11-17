from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_GIRL, ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE, HIEREUS

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (опознаны по имени и
# отчеству — фамилий в книге нет). Ч. 2 — лл. 13–16об по нумерации книги, 40 браков.
kirillovo_marriages_1827 = marriage_records(
    "ЦГАРМ", "57", "6", "124", "Кириллово", "Казанская",
    1827,
    *page("15об",
          *marriage_month(Month.NOVEMBER,
                          # жених — Дмитрий Андреевич Мальчиков (РС 1811: 2 г.; ИР 1828: 19 л.); поручители —
                          # Емельян Григорьевич и Нестор Дмитриевич Мальчиковы
                          marriage(30, 9,
                                   groom=person("Димитрій", "Андреевъ"), groom_marriage_num=1,
                                   bride=person("Агаѳья", "Парфенова", comment="в подлиннике «Андрееву» заключено в скобки, далее «Парфенову»"),
                                   witness1=person("Поликарпъ", "Никитинъ"),
                                   witness2=person("Емельянъ", "Григорьевъ"),
                                   witness3=person("Несторъ", "Димитріевъ"),
                                   priest=person("Николай", "Стефановъ", status=HIEREUS),
                                   reviewed=False),
                          ),
          ),
    *page("16",
          *marriage_month(Month.NOVEMBER,
                          # жених — Адриан Денисович Янин; поручитель Михаил Емельянович (Янин)
                          marriage(36, 11,
                                   groom=person("Андреянъ", "Денисовъ"), groom_marriage_num=1,
                                   bride=person("Евдокія", "Иванова"),
                                   witness1=person("Крысанъ", "Семеновъ"),
                                   witness2=person("Герасимъ", "Ивановъ"),
                                   witness3=person("Михаилъ", "Емельяновъ"),
                                   priest=person("Василій", "Тимоѳеевъ", status=HIEREUS),
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
