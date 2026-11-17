from verso.ru.dsl import (Month, RecordDefaults, Relationship, marriage, marriage_month,
                          marriage_records, page, person, relative)
from verso.ru.dsl.statuses import ECON_PEASANT_GIRL, ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE, HIEREUS

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (опознаны по имени и
# отчеству). Ч. 2 — лл. 418–424об, 34 брака. Разворот л. 421об–422 (браки №21–24) и
# л. 424об (№33–34) докачаны 20.10.2026 (сканы Яндекс.Архива 419 и 422) и прочитаны.
kirillovo_marriages_1831 = marriage_records(
    "ЦГАРМ", "57", "1", "402", "Кириллово", "Казанская",
    1831,
    *page("419об",
          *marriage_month(Month.FEBRUARY,
                          # жених — Петр Григорьевич Мальчиков (р. 1810); его жена до сих пор была неизвестна;
                          # поручители — Поликарп Никитин (кум Мальчиковых) и Василий Дмитриевич
                          marriage(10, 13,
                                   groom=person("Петръ", "Григорьевъ"), groom_marriage_num=1,
                                   bride=person("Ксенія", "Васильева"),
                                   witness1=person("Поликарпъ", "Никитинъ"),
                                   witness2=person("Василій", "Дмитріевъ"),
                                   witness3=person("Карпъ", "Яковлевъ"),
                                   priest=person("Яковъ", "Даниловъ", "Мизеровъ", status=HIEREUS),
                                   reviewed=False),
                          # поручитель Нестор Дмитриевич Мальчиков; жених — его кум (1829 №201)
                          marriage(11, 18,
                                   groom=person("Пимонъ", "Леонтьевъ"), groom_marriage_num=1,
                                   bride=person("Марѳа", "Артемова"),
                                   witness1=person("Несторъ", "Дмитріевъ"),
                                   witness2=person("Даніилъ", "Игнатовъ"),
                                   witness3=person("Филиппъ", "Андреевъ"),
                                   priest=person("Яковъ", "Даниловъ", "Мизеровъ", status=HIEREUS),
                                   reviewed=False),
                          ),
          ),
    *page("424об",
          *marriage_month(Month.NOVEMBER,
                          # поручители — Нестор Дмитриевич и Адриан («Андрей», как в 1824 и в ИР 1828) Григорьевич
                          # Мальчиковы
                          marriage(33, 13,
                                   groom=person("Иванъ", "Дорофеевъ", "Живодеровъ"), groom_marriage_num=1,
                                   bride=person("Екатерина", "Александрова"),
                                   witness1=person("Несторъ", "Дмитріевъ", "Мальчиковъ"),
                                   witness2=person("Андрей", "Григорьевъ", "Мальчиковъ"),
                                   witness3=person("Ефимъ", "Михайловъ", "Гераскинъ"),
                                   relatives=[relative(person("Александръ", "Тихоновъ", "Сибуревъ", comment="отчество читается неуверенно"), Relationship.FATHER, "невеста")],
                                   priest=person("Яковъ", "Даниловъ", "Мизеровъ", status=HIEREUS),
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
