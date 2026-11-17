from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_GIRL, ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE, HIEREUS

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (опознаны по имени и
# отчеству — фамилий в книге нет). Ч. 2 — лл. 285–289об (архивная нумерация), 49 браков.
kirillovo_marriages_1830 = marriage_records(
    "ЦГАРМ", "57", "6", "134", "Кириллово", "Казанская",
    1830,
    *page("286",
          *marriage_month(Month.JANUARY,
                          # невеста из Кириллова — вероятно, Федосья Андреевна Мальчикова (ИР 1828: 21 г.; восприемница
                          # 1824–1829). Жених из Гоголева Бора; опознание по имени — проверить
                          marriage(15, 31,
                                   groom=person("Матѳей", "Дорофеевъ", residence="Гоголев Бор"), groom_marriage_num=1,
                                   bride=person("Ѳеодосья", "Андреева"),
                                   witness1=person("Егоръ", "Агаѳоновъ", residence="Гоголев Бор"),
                                   witness2=person("Иванъ", "Тимоѳеевъ", residence="Гоголев Бор"),
                                   witness3=person("Григорій", "Ульяновъ", residence="Гоголев Бор"),
                                   priest=person("Василій", "Тимоѳеевъ", "Богдановъ", status=HIEREUS),
                                   reviewed=False),
                          ),
          ),
    *page("288",
          *marriage_month(Month.MAY,
                          # жених — Яков Максимович («Позняков») Мальчиков; невеста — его жена по РС 8 Елена Кириллова
                          marriage(33, 18,
                                   groom=person("Яковъ", "Максимовъ"), groom_marriage_num=1,
                                   bride=person("Елена", "Кирилова"),
                                   witness1=person("Антонъ", "Ивановъ"),
                                   witness2=person("Моисей", "Стефановъ"),
                                   witness3=person("Дмитрій", "Ѳедоровъ"),
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
