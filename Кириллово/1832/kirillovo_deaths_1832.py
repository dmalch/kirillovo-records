from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, NATURAL, SMALLPOX
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER,
                                   PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Ч. 3 — лл. 447–458
# (архивная нумерация), 63 м. / 63 ж.; летом и осенью — оспа.
kirillovo_deaths_1832 = death_records(
    "ЦГА республики Мордовия", "57", "6", "148", "Кириллово", "Казанская",
    1832,
    *page("451",
          *death_month(Month.JULY,
                       # Козма Емельянович, рожд. 28.10.1830 (1830 №157); фамилия отца в подлиннике «Мелчиковъ»
                       death(28, Gender.MALE, 29, None,
                             deceased=person("Козма", status=PEASANT_SON), age=2,
                             relatives=[relative(person("Емельянъ", "Григорьевъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             reviewed=False),
                       ),
          *death_month(Month.AUGUST,
                       # Прокопий Емельянович, рожд. 08.07.1832 (рождение м. №26)
                       death(29, Gender.MALE, 2, None,
                             deceased=person("Прокопій", status=PEASANT_SON), age="3 нед",
                             relatives=[relative(person("Емельянъ", "Григорьевъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death=SMALLPOX,
                             reviewed=False),
                       ),
          ),
    *page("452об",
          *death_month(Month.SEPTEMBER,
                       # сын Карпа Антоновича Янина, рожд. 04.06.1831 (1831 №85) — запись подтверждает, что тот Карп
                       # Антонов — Янин
                       death(40, Gender.MALE, 1, None,
                             deceased=person("Леонтій", status=PEASANT_SON), age=1,
                             relatives=[relative(person("Карпъ", "Антоновъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="номер на кадре обрезан — восстановлен по соседним (м. 38 … 41); имя в подлиннике «Деонтій»",
                             reviewed=False),
                       ),
          ),
    *page("456об",
          *death_month(Month.NOVEMBER,
                       # Анна Петровна, рожд. 31.01.1832 (рождение ж. №5)
                       death(56, Gender.FEMALE, 18, None,
                             deceased=person("Анна", status=PEASANT_DAUGHTER), age="6 нед",
                             relatives=[relative(person("Петръ", "Григорьевъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death=SMALLPOX,
                             comment="в подлиннике «6ти недѣль», хотя от рождения 31 января прошло больше девяти месяцев",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
