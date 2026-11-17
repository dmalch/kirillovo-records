from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import (DYACHOK, ECON_PEASANT_FEMALE, ECON_PEASANT_LEGAL_WIFE,
                                   ECON_PEASANT_MALE)

# Выборка первой волны: записи, где есть (или считались) Мальчиковы или Янины (фамилий в книге нет —
# опознаны по имени и отчеству, см. Кириллово/families/). Остальные записи года не внесены.
# Альбом «1827 (ЦГАРМ 57-6-124)», 27 кадров, ПЕРЕПУТАННЫХ: листы — по собственной нумерации
# книги (правый верхний угол; архивная — 508 и далее). Ч. 1 — лл. 1–12, счёт сквозной, 191 рождение.
kirillovo_births_1827 = birth_records(
    "ЦГА республики Мордовия", "57", "6", "124", "Кириллово", "Казанская",
    1827,
    *page("3об",
          *birth_month(Month.APRIL,
                       # восприемник Михаил Емельянович (Янин) — крёстный детей Ильи Петрова 1820 №21 и 1822 №24
                       birth(40, Gender.FEMALE, 8, 9,
                             child=person("Марья"),
                             father=person("Илья", "Петровъ"),
                             god_parent1=person("Михаилъ", "Емельяновъ"),
                             god_parent2=person("Ѳекла", "Васильева"),
                             reviewed=False),
                       ),
          ),
    *page("4об",
          *birth_month(Month.MAY,
                       # возможно, Константин Иванович Мальчиков, сын Ивана Ивановича (РС 8 1834: ~1832, но
                       # отдан в рекруты в 1848 — при рождении в 1827 ему был бы 21 год); восприемница — вероятно,
                       # Федосья Андреевна Мальчикова (ИР 1828: ~1807). Опознание по имени — проверить
                       birth(58, Gender.MALE, 20, 23,
                             child=person("Константинъ"),
                             father=person("Иванъ", "Ивановъ"),
                             god_parent1=person("Поликарпъ", "Никитинъ"),
                             god_parent2=person("Ѳеодосья", "Андреева"),
                             reviewed=False),
                       # отец — Григорий Иванович ШИРОКОВ, не Мальчиков: в 1832 г. (ж. №79) «Григорія Иванова Широкова» дочь
                       # крестят те же дьячок (позже дьякон) Петр Савельев и Дарья Иванова Широкова; Елена умерла 14.12.1827 (погребение ж. №76)
                       birth(59, Gender.FEMALE, 20, 23,
                             child=person("Елена"),
                             father=person("Григорій", "Ивановъ"),
                             god_parent1=person("Петръ", "Савельевъ", status=DYACHOK),
                             god_parent2=person("Дарья", "Иванова"),
                             reviewed=False),
                       ),
          ),
    *page("5",
          *birth_month(Month.JUNE,
                       # восприемник Семен Герасимов — возможно, Семен Герасимович Мальчиков (рекрут до 1834;
                       # жена Марья). Опознание слабое; Федор умер 17.07.1827, 6 нед.
                       birth(63, Gender.MALE, 1, 5,
                             child=person("Ѳеодоръ"),
                             father=person("Трофимъ", "Егоровъ"),
                             god_parent1=person("Семенъ", "Герасимовъ"),
                             god_parent2=person("Марья", "Леонтьева"),
                             reviewed=False),
                       ),
          ),
    *page("8",
          *birth_month(Month.AUGUST,
                       # восприемник Адриан Григорьевич Мальчиков
                       birth(116, Gender.MALE, 15, 18,
                             child=person("Андрей"),
                             father=person("Кононъ", "Николаевъ"),
                             god_parent1=person("Андреянъ", "Григорьевъ"),
                             god_parent2=person("Ксенія", "Семенова"),
                             reviewed=False),
                       ),
          ),
    *page("9",
          *birth_month(Month.SEPTEMBER,
                       # Денис Егорович Янин; те же восприемники, что у его сына Егора 1824 №172
                       birth(132, Gender.FEMALE, 3, 4,
                             child=person("Марѳа"),
                             father=person("Денисъ", "Егоровъ"),
                             god_parent1=person("Сергѣй", "Кириловъ"),
                             god_parent2=person("Анна", "Тимоѳеева"),
                             reviewed=False),
                       ),
          ),
    *page("10",
          *birth_month(Month.OCTOBER,
                       # восприемник — Петр Григорьевич Мальчиков: в 1831 г. (#144) та же пара крестит у того же
                       # Григория Федорова, и там он назван «Петръ Григорьевъ Мальчиковъ»
                       birth(154, Gender.FEMALE, 7, 9,
                             child=person("Евдокія"),
                             father=person("Григорій", "Ѳеодоровъ"),
                             god_parent1=person("Петръ", "Григорьевъ"),
                             god_parent2=person("Евдокія", "Ѳеодорова"),
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
