from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_GIRL, ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE, HIEREUS

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (опознаны по имени и
# отчеству — фамилий в книге нет). Ч. 2 — лл. 408–413 (архивная нумерация), 53 брака.
kirillovo_marriages_1829 = marriage_records(
    "ЦГА республики Мордовия", "57", "6", "131", "Кириллово", "Казанская",
    1829,
    *page("408",
          *marriage_month(Month.JANUARY,
                          # жених — Евсигней Евсеевич Мальчиков (РС 1811, двор 468); поручители — Нестор Дмитриевич
                          # и Адриан Григорьевич Мальчиковы
                          marriage(3, 20,
                                   groom=person("Евсигней", "Евсѣевъ"), groom_marriage_num=1,
                                   bride=person("Ефимія", "Кирилова"),
                                   witness1=person("Несторъ", "Дмитріевъ"),
                                   witness2=person("Андреянъ", "Григорьевъ"),
                                   witness3=person("Миронъ", "Петровъ"),
                                   priest=person("Андрей", "Савельевъ", status=HIEREUS),
                                   reviewed=False),
                          ),
          ),
    *page("408об",
          *marriage_month(Month.FEBRUARY,
                          # жених — возможно, Карп Антонович Янин (~1813, «Сырцов»); поручитель Алексей Алимов был
                          # поручителем и у Лукьяна Михайловича Янина (1821 №11). Опознание слабое
                          marriage(6, 4,
                                   groom=person("Карпъ", "Антоновъ"), groom_marriage_num=1,
                                   bride=person("Февронія", "Андреянова", comment="отчество невесты читается неуверенно («Андраѳову»?)"),
                                   witness1=person("Григорій", "Ивановъ"),
                                   witness2=person("Алексѣй", "Алимовъ"),
                                   witness3=person("Кирилъ", "Никитинъ"),
                                   priest=person("Василій", "Тимоѳеевъ", "Богдановъ", status=HIEREUS),
                                   reviewed=False),
                          # жених — Дмитрий Андреевич Мальчиков, второбрачный (первая жена — Агафья Парфенова, 1827 №30)
                          marriage(10, 6,
                                   groom=person("Дмитрій", "Андреевъ"), groom_marriage_num=2,
                                   bride=person("Марія", "Ивлѣева"),
                                   witness1=person("Вавилъ", "Елисеевъ"),
                                   witness2=person("Зотъ", "Павловъ"),
                                   witness3=person("Антонъ", "Елисеевъ"),
                                   priest=person("Василій", "Тимоѳеевъ", "Богдановъ", status=HIEREUS),
                                   reviewed=False),
                          ),
          ),
    *page("409об",
          *marriage_month(Month.MAY,
                          # жених — Аким Григорьевич Мальчиков (р. 1807); его жена до сих пор была неизвестна
                          marriage(19, 24,
                                   groom=person("Акимъ", "Григорьевъ"), groom_marriage_num=1,
                                   bride=person("Екатерина", "Григорьева"),
                                   witness1=person("Поликарпъ", "Никитинъ"),
                                   witness2=person("Иванъ", "Ивановъ"),
                                   witness3=person("Терентій", "Васильевъ"),
                                   priest=person("Алексѣй", last_name_orig="Соколовъ", status=HIEREUS),
                                   reviewed=False),
                          ),
          ),
    *page("410",
          *marriage_month(Month.MAY,
                          # жених — Григорий Иванович «2-й» Мальчиков (РС 8: ~1813, жена Прасковья ~1809);
                          # поручитель Нестор Дмитриевич
                          marriage(24, 31,
                                   groom=person("Григорій", "Ивановъ"), groom_marriage_num=1,
                                   bride=person("Параскева", "Яковлева"),
                                   witness1=person("Поликарпъ", "Никитинъ"),
                                   witness2=person("Несторъ", "Дмитріевъ"),
                                   witness3=person("Ефремъ", "Дмитріевъ"),
                                   priest=person("Алексѣй", last_name_orig="Соколовъ", status=HIEREUS),
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
