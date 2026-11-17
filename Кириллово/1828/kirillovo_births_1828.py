from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_LEGAL_WIFE, ECON_PEASANT_MALE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (фамилий в книге нет —
# опознаны по имени и отчеству, см. Кириллово/families/ и ИР 1828). Остальные записи не внесены.
# Альбом «1828 (ЦГАРМ 57-1-400)», 28 кадров; ч. 1 — лл. 323–335 (архивная нумерация),
# счёт сквозной, 182 рождения.
kirillovo_births_1828 = birth_records(
    "ЦГА республики Мордовия", "57", "1", "400", "Кириллово", "Казанская",
    1828,
    *page("324",
          *birth_month(Month.JANUARY,
                       # Аксинья Васильевна Мальчикова (РС 8 1834: ~1828), дочь Василия Дмитриевича;
                       # восприемники — Дмитрий Андреевич и Гликерия Дмитриевна Мальчиковы
                       birth(18, Gender.FEMALE, 20, 22,
                             child=person("Ксенія"),
                             father=person("Василій", "Дмитріевъ"),
                             god_parent1=person("Дмитрій", "Андреевъ"),
                             god_parent2=person("Гликерія", "Дмитріева"),
                             reviewed=False),
                       ),
          ),
    *page("326об",
          *birth_month(Month.APRIL,
                       # Марья Васильевна Мальчикова (РС 8: ~1829), дочь Василия Герасимовича и Устиньи Фоминой;
                       # восприемники — её дядя по матери Панкратий Фомин и тётка Ирина Герасимовна
                       birth(54, Gender.FEMALE, 6, 8,
                             child=person("Марѳа"),
                             father=person("Василій", "Герасимовъ"),
                             god_parent1=person("Панкратій", "Ѳоминъ"),
                             god_parent2=person("Ирина", "Герасимова"),
                             comment="в РС 8 1834 у Василия Герасимовича дочь «Марья» ~1829 — сверить имя",
                             reviewed=False),
                       ),
          ),
    *page("331об",
          *birth_month(Month.SEPTEMBER,
                       # Устинья Адриановна Мальчикова (РС 8: ~1828); восприемники — Дмитрий Андреевич и
                       # Федосья Андреевна Мальчиковы
                       birth(137, Gender.FEMALE, 28, 30,
                             child=person("Устина"),
                             father=person("Андреянъ", "Григорьевъ"),
                             god_parent1=person("Дмитрій", "Андреевъ"),
                             god_parent2=person("Ѳеодосья", "Андреева"),
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
