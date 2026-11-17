from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import NATURAL
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, ECON_PEASANT_WIDOW,
                                   PEASANT_SON)

kirillovo_deaths_1760 = death_records(
    "ГА Рязанской области", "627", "255", "2", "Кириллово", "Успенская",
    1760,
    *page("101об",
          *death_month(Month.MARCH,
                       death(1, Gender.MALE, 14, None,
                             deceased=person("Иоаким", "Ефтифиев"), age=60),
                       ),
          *death_month(Month.APRIL,
                       death(2, Gender.MALE, 26, None,
                             deceased=person("Афанасий", status=PEASANT_SON), age=19,
                             relatives=[relative(person("Григорий", "Михайлов"), Relationship.FATHER)]),
                       ),
          ),
    *page("102",
          *death_month(Month.MAY,
                       death(3, Gender.FEMALE, 27, None,
                             deceased=person("Анна", "Евдокимова", status=ECON_PEASANT_WIDOW), age=51),
                       ),
          *death_month(Month.NOVEMBER,
                       death(3, Gender.MALE, 28, None,
                             deceased=person("Михаил", status=PEASANT_SON), age=39,
                             relatives=[relative(person("Михайло", "Кирсанов"), Relationship.FATHER)]),
                       ),
          *death_month(Month.DECEMBER,
                       death(4, Gender.MALE, 23, None,
                             deceased=person("Тихон", "Кирсанов"), age=60),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
