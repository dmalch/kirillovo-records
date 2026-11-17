from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import NATURAL
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Ч. 3 — лл. 391–395об
# (31 м. / 43 ж.), ведомость л. 396.
kirillovo_deaths_1838 = death_records(
    "ЦГАРМ", "57", "6", "181", "Кириллово", "Казанская",
    1838,
    *page("395",
          *death_month(Month.NOVEMBER,
                       # Федосья Андреевна Мальчикова (ИР 1828: 21 г.), с 1830 г. замужем в Гоголевом Бору
                       death(38, Gender.FEMALE, 6, None,
                             deceased=person("Ѳеодосія", "Андреева", residence="Гоголев Бор"), age=30,
                             relatives=[relative(person("Матвѣй", "Дорофеевъ", "Романовъ"), Relationship.HUSBAND)],
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
