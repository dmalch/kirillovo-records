from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, NATURAL, SMALLPOX
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER,
                                   PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Ч. 3 — лл. 364–373.
# Развороты 364об–365 (февраль–март) и 366об–367 (июнь) докачаны с Яндекс.Архива 20.10.2026 и
# прочитаны 21.10.2026. Летом 1833 г. — понос у детей.
kirillovo_deaths_1833 = death_records(
    "ЦГАРМ", "57", "6", "153", "Кириллово", "Казанская",
    1833,
    *page("364об",
          *death_month(Month.FEBRUARY,
                       # Матрона Акимовна Мальчикова, рожд. 07.11.1832 (1832 ж. №72)
                       death(8, Gender.FEMALE, 9, None,
                             deceased=person("Матрона", status=PEASANT_DAUGHTER), age="3 мес",
                             relatives=[relative(person("Акимъ", "Григорьевъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death=SMALLPOX,
                             reviewed=False),
                       ),
          ),
    *page("366об",
          *death_month(Month.JUNE,
                       # дочь Андреяна Денисовича Янина (брак 1827 №36 с Евдокией Ивановой); её рождения в DSL нет.
                       # Не Стефанида 1830 ж. №177 — та дочь Андрея Денисова, ей было бы 2 г. 7 мес.
                       death(26, Gender.FEMALE, 26, None,
                             deceased=person("Стефанида", status=PEASANT_DAUGHTER), age=1,
                             relatives=[relative(person("Андреянъ", "Денисовъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             comment="возраст в подлиннике «году», как у ж. №39",
                             reviewed=False),
                       ),
          ),
    # до 21.10.2026 записано на «366об» — имена файлов альбома были сдвинуты; запись на л. 367об (скан 394)
    *page("367об",
          *death_month(Month.JULY,
                       # Георгий Михайлович, рожд. 08.04.1826 (1826 №44); фамилия в подлиннике «Мелчиковъ»
                       death(23, Gender.MALE, 8, None,
                             deceased=person("Георгій", status=PEASANT_SON), age=6,
                             relatives=[relative(person("Михаилъ", "Павловъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             reviewed=False),
                       ),
          ),
    *page("369",
          *death_month(Month.JULY,
                       # Федор Лукьянович Янин, рожд. 16.02.1833 (рождение м. №11)
                       death(33, Gender.MALE, 23, None,
                             deceased=person("Ѳеодоръ", status=PEASANT_SON), age="7 нед",
                             relatives=[relative(person("Лукьянъ", "Михайловъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="в подлиннике «7 недѣль», хотя от рождения 16 февраля прошло пять месяцев",
                             reviewed=False),
                       # Параскева Васильевна Мальчикова, рожд. 19.10.1832 (1832 ж. №65)
                       death(39, Gender.FEMALE, 28, None,
                             deceased=person("Параскева", status=PEASANT_DAUGHTER), age=1,
                             relatives=[relative(person("Василій", "Дмитріевъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
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
