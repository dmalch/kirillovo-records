from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (DYACHOK, ECON_PEASANT_FEMALE, ECON_PEASANT_LEGAL_WIFE,
                                   ECON_PEASANT_MALE)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (фамилий в книге нет —
# опознаны по имени и отчеству, см. Кириллово/families/). Остальные записи года не внесены.
# Альбом «1826 (ЦГАРМ 57-6-118)», 23 кадра; ч. 1 — лл. 345–355об, счёт сквозной, 171 рождение.
kirillovo_births_1826 = birth_records(
    "ЦГАРМ", "57", "6", "118", "Кириллово", "Казанская",
    1826,
    *page("347",
          *birth_month(Month.JANUARY,
                       # Семен Емельянович Мальчиков (РС 8 1834: ~1826); восприемница — вероятно, его тётка
                       # Ирина Григорьевна
                       birth(29, Gender.MALE, 29, 31,
                             child=person("Семенъ"),
                             father=person("Емельянъ", "Григорьевъ"),
                             god_parent1=person("Василій", "Семеновъ"),
                             god_parent2=person("Ирина", "Григорьева"),
                             reviewed=False),
                       ),
          ),
    *page("347об",
          *birth_month(Month.APRIL,
                       # Егор Михайлович Мальчиков (ИР 1828: ~1823 — роспись старит его на три года);
                       # восприемница — тётка отца Гликерия Дмитриевна
                       birth(44, Gender.MALE, 8, 9,
                             child=person("Георгій"),
                             father=person("Михаилъ", "Павловъ"),
                             god_parent1=person("Артемій", "Андреевъ"),
                             god_parent2=person("Гликерія", "Димитріева"),
                             reviewed=False),
                       ),
          ),
    *page("352об",
          *birth_month(Month.OCTOBER,
                       # восприемница Васса Емельянова — та же, что у дочери того же Ивана Петрова 1824 №86
                       # (возможно, Василиса Емельяновна Янина); опознание слабое
                       birth(123, Gender.FEMALE, 14, 17,
                             child=person("Параскева"),
                             father=person("Иванъ", "Петровъ"),
                             god_parent1=person("Петръ", "Савельевъ", status=DYACHOK),
                             god_parent2=person("Васса", "Емельянова"),
                             reviewed=False),
                       ),
          ),
    *page("354",
          *birth_month(Month.NOVEMBER,
                       # восприемник Емельян Григорьевич — Мальчиков или Шаурин (1831 #139); крёстный и других детей Федора Семенова
                       # (1821 №117, 1824 №63)
                       birth(153, Gender.FEMALE, 26, 28,
                             child=person("Екатерина"),
                             father=person("Ѳеодоръ", "Семеновъ"),
                             god_parent1=person("Емельянъ", "Григорьевъ"),
                             god_parent2=person("Анна", "Карпова"),
                             reviewed=False),
                       ),
          ),
    *page("355",
          *birth_month(Month.DECEMBER,
                       # восприемник Нестор Дмитриевич Мальчиков
                       birth(169, Gender.FEMALE, 17, 19,
                             child=person("Ульяна"),
                             father=person("Филиппъ", "Андреевъ"),
                             god_parent1=person("Несторъ", "Димитріевъ"),
                             god_parent2=person("Марѳа", "Артемова"),
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_FEMALE,
        status_mother=ECON_PEASANT_LEGAL_WIFE,
    ),
)
