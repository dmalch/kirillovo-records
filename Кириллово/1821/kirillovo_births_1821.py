from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_LEGAL_WIFE, ECON_PEASANT_MALE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (фамилий в книге нет —
# опознаны по имени и отчеству, см. Кириллово/families/). Остальные записи года не внесены.
# Альбом «1821 (ЦГАРМ 57-6-102)», 21 кадр: ч. 1 лл. 316–327об (120 м. / 88 ж.).
kirillovo_births_1821 = birth_records(
    "ЦГА республики Мордовия", "57", "6", "102", "Кириллово", "Успенская",
    1821,
    *page("317об",
          *birth_month(Month.FEBRUARY,
                       # отец — вероятно, Григорий Иванович Мальчиков; восприемник Дмитрий Давыдович Мальчиков
                       birth(13, Gender.FEMALE, 24, 26,
                             child=person("Анна"),
                             father=person("Григорій", "Ивановъ"),
                             god_parent1=person("Димитрій", "Давыдовъ"),
                             god_parent2=person("Неонила", "Антонова")),
                       ),
          ),
    *page("320об",
          *birth_month(Month.JUNE,
                       # Нестор Дмитриевич Мальчиков; восприемница — его сестра Гликерия Дмитриевна
                       birth(38, Gender.FEMALE, 8, 12,
                             child=person("Акилина"),
                             father=person("Несторъ", "Дмитріевъ"),
                             god_parent1=person("Иванъ", "Ивановъ"),
                             god_parent2=person("Гликерія", "Дмитріева")),
                       ),
          ),
    *page("327",
          *birth_month(Month.NOVEMBER,
                       # Василий Герасимович Мальчиков (жена Устинья Фомина, брак 1817 №2); сын Андрей —
                       # в РС 8 1834 «~1819»; восприемник Василий Дмитриевич Мальчиков
                       birth(112, Gender.MALE, 26, 27,
                             child=person("Андрей"),
                             father=person("Василій", "Герасимовъ"),
                             god_parent1=person("Василій", "Дмитріевъ"),
                             god_parent2=person("Наталья", "Ѳомина")),
                       ),
          ),
    *page("327об",
          *birth_month(Month.DECEMBER,
                       # восприемник Емельян Григорьевич — Мальчиков или Шаурин (в 1831 #139 есть «Емельянъ Григорьевъ Шауринъ»)
                       birth(117, Gender.MALE, 9, 11,
                             child=person("Даніилъ"),
                             father=person("Федоръ", "Семеновъ"),
                             god_parent1=person("Емеліянъ", "Григорьевъ"),
                             god_parent2=person("Агаѳья", "Парфенова")),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_FEMALE,
        status_mother=ECON_PEASANT_LEGAL_WIFE,
    ),
)
