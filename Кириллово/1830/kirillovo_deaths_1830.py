from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, NATURAL
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Ч. 3 — лл. 291–296
# (архивная нумерация), 67 м. / 55 ж.
kirillovo_deaths_1830 = death_records(
    "ЦГАРМ", "57", "6", "134", "Кириллово", "Казанская",
    1830,
    *page("293",
          *death_month(Month.MAY,
                       # Варвара Лукьяновна Янина, рожд. 05.12.1829 (1829 №204)
                       death(17, Gender.FEMALE, 30, None,
                             deceased=person("Варвара", status=PEASANT_DAUGHTER), age="6 мес",
                             relatives=[relative(person("Лукіянъ", "Михайловъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="возраст в подлиннике «полугоду»",
                             reviewed=False),
                       ),
          *death_month(Month.JUNE,
                       # вероятно, Параскева Андреевна, жена Ивана Феодосиевича Мальчикова (ИР 1828: 77 л.);
                       # в табели года эта смерть — единственная женская в 75 лет. Опознание по имени — сверить с РС 8
                       death(18, Gender.FEMALE, 7, None,
                             deceased=person("Параскева", "Андреева"), age=75,
                             reviewed=False),
                       ),
          ),
    *page("294",
          *death_month(Month.AUGUST,
                       # Евдокия Михайловна Мальчикова, рожд. 05.08.1829 (1829 №132)
                       death(30, Gender.FEMALE, 21, None,
                             deceased=person("Евдокія", status=PEASANT_DAUGHTER), age="6 мес",
                             relatives=[relative(person("Михаилъ", "Павловъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="возраст в подлиннике «полугоду», хотя от рождения прошёл год",
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
