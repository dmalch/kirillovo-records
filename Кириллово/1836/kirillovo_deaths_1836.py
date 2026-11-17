from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, NATURAL
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER,
                                   PEASANT_SON, SOLDIER_WIFE)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Ч. 3 — лл. 111–117об,
# ведомость л. 118. Разворот л. 115об–116 (погребения м. 30–33, ж. 33–42) докачан 20.10.2026
# (скан Яндекс.Архива 120) и прочитан; лл. 118об–119 (скан 123) пусты.
kirillovo_deaths_1836 = death_records(
    "ЦГА республики Мордовия", "57", "6", "168", "Кириллово", "Казанская",
    1836,
    *page("112",
          *death_month(Month.FEBRUARY,
                       # Гликерия — дочь Константина Кузьмича Стрекалина и Настасьи Андреевны Мальчиковой
                       # (род. 1833, ж. №31, отец там «Константинъ Ивановъ Малахаевъ»)
                       death(12, Gender.FEMALE, 2, None,
                             deceased=person("Гликерія", status=PEASANT_DAUGHTER), age=2,
                             relatives=[relative(person("Константинъ", "Казминъ", "Малахеевъ", comment="отчество читается «Кармина/Казмина»"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             reviewed=False),
                       ),
          ),
    *page("112об",
          *death_month(Month.MARCH,
                       # Сидор — сын Константина Кузьмича Стрекалина (род. 1835, м. №28, отец там тоже «Мальчиковъ»)
                       death(9, Gender.MALE, 15, None,
                             deceased=person("Сидоръ", status=PEASANT_SON), age=1,
                             relatives=[relative(person("Константинъ", "Казминъ", "Мальчиковъ", comment="отчество читается «Кармина/Казмина»"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="возраст «году»",
                             reviewed=False),
                       ),
          ),
    *page("113",
          *death_month(Month.MARCH,
                       # Прохор Федорович Янин из Гоголева Бора
                       death(11, Gender.MALE, 27, None,
                             deceased=person("Сидоръ", status=PEASANT_SON, residence="Гоголев Бор"), age=1,
                             relatives=[relative(person("Прохоръ", "Ѳедоровъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="возраст «году»",
                             reviewed=False),
                       ),
          ),
    *page("116",
          *death_month(Month.OCTOBER,
                       # солдатка Марфа Васильевна — жена рекрута Максима Ивановича Мальчикова, мать Якова
                       # Максимовича «Познякова» (ИР 1828: «Иванова сноха солдатка», 36 л. → ~1792)
                       death(42, Gender.FEMALE, 15, None,
                             deceased=person("Марѳа", "Васильева", "Мальчикова", status=SOLDIER_WIFE), age=45,
                             cause_of_death=CONSUMPTION,
                             reviewed=False),
                       ),
          ),
    *page("117",
          *death_month(Month.NOVEMBER,
                       # Кирилл Антонович Янин
                       death(36, Gender.MALE, 4, None,
                             deceased=person("Кузма", status=PEASANT_SON), age="3 нед",
                             relatives=[relative(person("Кириллъ", "Антоновъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
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
