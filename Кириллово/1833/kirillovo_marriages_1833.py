from verso.ru.dsl import (Month, RecordDefaults, Relationship, marriage, marriage_month,
                          marriage_records, page, person, relative)
from verso.ru.dsl.statuses import ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE, HIEREUS

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Ч. 2 — лл. 354–363, браки
# №1–6 сильно выцвели. Развороты с браками №10–15 (лл. 355об–356) и №35–40 (лл. 359об–360)
# докачаны с Яндекс.Архива 20.10.2026 и прочитаны 21.10.2026: на втором волны нет.
kirillovo_marriages_1833 = marriage_records(
    "ЦГА республики Мордовия", "57", "6", "153", "Кириллово", "Казанская",
    1833,
    *page("355об",
          *marriage_month(Month.JANUARY,
                          # Федор Павлович Мальчиков (р. 20.10.1812); жена Пелагия Ивановна — мать его детей 1840-х
                          marriage(12, 22,
                                   groom=person("Ѳеодоръ", "Павловъ", "Мальчиковъ"), groom_marriage_num=1,
                                   bride=person("Пелагія", "Иванова", residence="Поляна"),
                                   witness1=person("Андреянъ", "Андреевъ", "Мальчиковъ", comment="отчество так в подлиннике; не описка ли за Андреяна Григорьева"),
                                   witness2=person("Пимонъ", "Леонтьевъ", "Данковъ", comment="фамилия читается неуверенно"),
                                   relatives=[relative(person("Иванъ", "Акимовъ", "Лабинъ", residence="Поляна", comment="фамилия читается неуверенно"),
                                                       Relationship.FATHER, "невеста")],
                                   priest=person("Андрей", "Савельевъ", status=HIEREUS),
                                   reviewed=False),
                          ),
          ),
    *page("357",
          *marriage_month(Month.JANUARY,
                          # невеста — Елена Несторовна Мальчикова; поручитель — её дядя Василий Дмитриевич
                          marriage(20, 30,
                                   groom=person("Петръ", "Герасимовъ", "Козловъ", residence="Гоголев Бор"), groom_marriage_num=1,
                                   bride=person("Елена", "Нестерова"),
                                   witness1=person("Василій", "Дмитріевъ", "Мальчиковъ"),
                                   witness2=person("Евстафій", "Андреевъ", "Кедровъ", comment="фамилия читается неуверенно"),
                                   witness3=person("Андреянъ", "Григорьевъ", "Чубаровъ", comment="фамилия читается неуверенно"),
                                   relatives=[relative(person("Несторъ", "Дмитріевъ", "Мальчиковъ"), Relationship.FATHER, "невеста")],
                                   priest=person("Иоаннъ", "Михайловъ", status=HIEREUS),
                                   reviewed=False),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_MAIDEN,
        status_bride=ECON_PEASANT_MAIDEN,
        status_groom=ECON_PEASANT_MALE,
    ),
)
