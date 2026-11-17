from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_GIRL, ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE, HIEREUS

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (опознаны по имени и
# отчеству — фамилий в книге нет). Ч. 2 — лл. 336–338, 28 браков.
kirillovo_marriages_1828 = marriage_records(
    "ЦГА республики Мордовия", "57", "1", "400", "Кириллово", "Казанская",
    1828,
    *page("336",
          *marriage_month(Month.JANUARY,
                          # жених — Семен Герасимович Мальчиков (рекрут до 1834; в РС 8 его жена Марья ~1804
                          # «невестка» в семье 553)
                          marriage(4, 22,
                                   groom=person("Семенъ", "Герасимовъ"), groom_marriage_num=1,
                                   bride=person("Марія", "Дмитріева"),
                                   witness1=person("Ѳома", "Ѳеодоровъ"),
                                   witness2=person("Никита", "Павловъ"),
                                   witness3=person("Сергѣй", "Григорьевъ"),
                                   priest=person("Андрей", "Савельевъ", status=HIEREUS),
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
