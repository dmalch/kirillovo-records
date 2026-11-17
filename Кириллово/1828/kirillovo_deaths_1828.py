from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, NATURAL, SMALLPOX
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER,
                                   PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Ч. 3 — лл. 339–348
# (архивная нумерация; пустые листы книги архив не считал).
kirillovo_deaths_1828 = death_records(
    "ЦГАРМ", "57", "1", "400", "Кириллово", "Казанская",
    1828,
    *page("340",
          *death_month(Month.JANUARY,
                       # сын Архипа Павловича Мальчикова (женат 15.02.1826)
                       death(11, Gender.MALE, 22, None,
                             deceased=person("Вонифантій", status=PEASANT_SON), age="6 нед",
                             relatives=[relative(person("Архипъ", "Павловъ"), Relationship.FATHER)],
                             cause_of_death=SMALLPOX,
                             reviewed=False),
                       ),
          ),
    *page("345об",
          *death_month(Month.JULY,
                       # дочь Павла Давыдовича Мальчикова (~1820); в ИР 1828 не названа
                       death(73, Gender.FEMALE, 7, None,
                             deceased=person("Евдокія", status=PEASANT_DAUGHTER), age=8,
                             relatives=[relative(person("Павелъ", "Давыдовъ"), Relationship.FATHER)],
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
