from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, NATURAL
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER,
                                   PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Ч. 3 — лл. 425–432об (по
# декабрь; 74 м. / 71 ж. по ведомости), ведомость и подписи причта — л. 433. Развороты лл. 425об–427
# (погребения января–июня) и 431об–433 (октябрь–декабрь) докачаны 20.10.2026 (сканы Яндекс.Архива
# 424–425, 430–431) и прочитаны.
kirillovo_deaths_1831 = death_records(
    "ЦГАРМ", "57", "1", "402", "Кириллово", "Казанская",
    1831,
    *page("426об",
          *death_month(Month.APRIL,
                       # «у Андрея Григорьева дочь Евдокія», без фамилии. Андреем Григорьевым книга 1824 и ИР 1828
                       # зовут Адриана Григорьевича Мальчикова, но в ИР 1828 (Великий пост) у него только Козма и
                       # Косма, а дочь Устина родилась в октябре 1828 — трёхлетней Евдокии там нет. Опознание слабое
                       death(23, Gender.FEMALE, 15, None,
                             deceased=person("Евдокія", status=PEASANT_DAUGHTER), age=3,
                             relatives=[relative(person("Андрей", "Григорьевъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             reviewed=False),
                       ),
          ),
    *page("427",
          *death_month(Month.JUNE,
                       # Матрона Марковна Янина из Гоголева Бора, рожд. 26.03.1831 (рождение ж. №45)
                       death(31, Gender.FEMALE, 4, None,
                             deceased=person("Матрона", status=PEASANT_DAUGHTER, residence="Гоголев Бор"), age="3 мес",
                             relatives=[relative(person("Марка", "Алексѣевъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             reviewed=False),
                       ),
          ),
    *page("427об",
          *death_month(Month.JUNE,
                       # близнец, рожд. 19.05.1831 (рождение №76)
                       death(32, Gender.FEMALE, 6, None,
                             deceased=person("Мавра", status=PEASANT_DAUGHTER), age="7 нед",
                             relatives=[relative(person("Лукіянъ", "Михайловъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             reviewed=False),
                       ),
          ),
    *page("428",
          *death_month(Month.JULY,
                       # близнец, рожд. 19.05.1831 (рождение №75)
                       death(32, Gender.MALE, 25, None,
                             deceased=person("Михаилъ", status=PEASANT_SON), age="2 мес",
                             relatives=[relative(person("Лукьянъ", "Михайловъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             reviewed=False),
                       ),
          ),
    *page("432",
          *death_month(Month.NOVEMBER,
                       # вторая Ксения Васильевна Мальчикова, рожд. 22.01.1830 (рождение 1830 ж. №19); первая
                       # (рожд. 20.01.1828) жива в РС 8 1834 — «Аксинья», 6 л.
                       death(69, Gender.FEMALE, 18, None,
                             deceased=person("Ксенія", status=PEASANT_DAUGHTER), age=2,
                             relatives=[relative(person("Василій", "Дмитріевъ", "Мальчиковъ"), Relationship.FATHER)],
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
