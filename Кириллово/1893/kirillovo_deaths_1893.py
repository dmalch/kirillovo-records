from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLD, COLIC, DECREPITUDE, DROPSY
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIFE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-306, альбом
# Photos «1893 (ГАПО 182-5-306)» (pk 1204), ч. 3 — лл. 32об–46об (первые записи — смерти 31.12.1892), 56 муж. / 54 жен.;
# л. 32 — шмуцтитул; прочитана целиком 25.10.2026; импорта не было. Левая половина л. 32об оторвана и подшита косо. Вся
# запись — на левой странице, причина — на правой. Погребали свящ. Александр Васильев Писарев и Василий Георгиевич Кутин.
# 21.09.1893 погребена Гликерия, 11 л., дочь Андрея Платоновича Бубенчикова (ж. №45; отец женился 1.11.1893, брак №15 —
# поручитель Федор Самсонович Янин) — не выписана.
kirillovo_deaths_1893 = death_records(
    "ГАПО",
    "182",
    "5",
    "306",
    "Кириллово",
    "Казанская церковь",
    1893,
    *death_month(Month.JANUARY,
                 # Анна, дочь Герасима Яковлевича Мальчикова, р. 30.01.1890 (рожд. 1890 ж. №6)
                 death(4, Gender.FEMALE, 2, 3,
                       deceased=person("Анна", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Герасимъ", "Яковлевъ", "Мальчиковъ"), Relationship.FATHER)],
                       comment="возраст и причина на оторванном крае листа",
                       page="32об",
                       reviewed=False),
                 # Параскева, жена Петра Дмитриевича Янина (кто он — не установлено)
                 death(5, Gender.FEMALE, 12, 14,
                       deceased=person("Параскева", status=PEASANT_WIFE), age=41,
                       relatives=[relative(person("Петръ", "Димитріевъ", "Янинъ"), Relationship.HUSBAND)],
                       cause_of_death=COLD,
                       page="33об",
                       reviewed=False),
                 ),
    *death_month(Month.FEBRUARY,
                 # Фекла, дочь Ильи Андреевича «Малахаева», р. 20.09.1892 (рожд. 1892 ж. №48)
                 death(14, Gender.FEMALE, 31, 1,
                       d_month=Month.JANUARY,
                       deceased=person("Ѳекла", status=PEASANT_DAUGHTER), age="4 мес",
                       relatives=[relative(person("Илія", "Андреевъ", "Малахаевъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       comment="умерла 31 января, погребена 1 февраля; записана под «Февраль»; цифра возраста неясна",
                       page="35об",
                       reviewed=False),
                 ),
    *death_month(Month.MARCH,
                 # Илья Павлович Мальчиков (жених 1840, восприемник 1844–1850)
                 death(21, Gender.MALE, 5, 7,
                       deceased=person("Илія", "Павловъ", "Мальчиковъ"), age=72,
                       cause_of_death=DECREPITUDE,
                       page="37об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Андрей Григорьевич Мальчиков («Юлинъ»)
                 death(31, Gender.MALE, 10, 12,
                       deceased=person("Андрей", "Григорьевъ", "Юлинъ", comment="= Андрей Григорьевич Мальчиков"), age=57,
                       cause_of_death=DROPSY,
                       comment="причина у края («отъ водян[ки]»)",
                       page="40об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Самсон Наумович Янин, вдовец (вторая жена Мария Федоровна ум. 1888)
                 death(50, Gender.MALE, 27, 29,
                       deceased=person("Самсонъ", "Наумовъ", "Янинъ", comment="«вдовъ»"), age=63,
                       cause_of_death=DECREPITUDE,
                       page="44об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
