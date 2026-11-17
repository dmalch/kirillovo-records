from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, MEASLES, NATURAL
from verso.ru.dsl.statuses import (ECON_PEASANT_DAUGHTER_MAIDEN, ECON_PEASANT_FEMALE,
                                   ECON_PEASANT_MALE, PEASANT_DAUGHTER, PEASANT_SON, SOLDIER_WIFE)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Ч. 3 — лл. 181–188об,
# ведомость л. 189; летом 1835 г. корь и понос у детей.
kirillovo_deaths_1835 = death_records(
    "ЦГА республики Мордовия", "57", "1", "404", "Кириллово", "Казанская",
    1835,
    *page("181об",
          *death_month(Month.FEBRUARY,
                       # Ирина Ивановна Мальчикова (РС 8: ~1818; ИР 1828: 8 л.)
                       death(4, Gender.FEMALE, 9, None,
                             deceased=person("Ирина", status=ECON_PEASANT_DAUGHTER_MAIDEN), age=15,
                             relatives=[relative(person("Иванъ", "Ивановъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death="скоропостижно",
                             comment="«скоропостижно», освидетельствована земским судом",
                             reviewed=False),
                       ),
          *death_month(Month.MARCH,
                       # отец «Петръ Павловъ Ма…чиковъ» — Петр Павлович в семье Мальчиковых не известен; скорее
                       # Маинов: в 1837 (рожд. м. №73) «Петръ Павловъ Маиновъ» с женой Марфой Дмитриевной, в 1839
                       # (смерть м. №53) умер Павел Максимов Маинов, 75 л.
                       death(6, Gender.MALE, 7, None,
                             deceased=person("Василій", status=PEASANT_SON), age="2 нед",
                             relatives=[relative(person("Петръ", "Павловъ", "Мальчиковъ", comment="фамилия читается «Ма…чиковъ», середина слова не видна"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             reviewed=False),
                       ),
          ),
    *page("182об",
          *death_month(Month.MAY,
                       # мать — вероятно, солдатка Марфа Васильевна, жена рекрута Максима Ивановича Мальчикова
                       # (ИР 1828: «Иванова сноха солдатка Марѳа Васильева» с сыном Тихоном «по году»); здесь
                       # Тихон — незаконнорождённый и трёх лет, так что это, скорее, другой её сын
                       death(13, Gender.MALE, 11, None,
                             deceased=person("Тихонъ"), age=3,
                             relatives=[relative(person("Марѳа", "Васильева", status=SOLDIER_WIFE), Relationship.MOTHER)],
                             cause_of_death=MEASLES,
                             comment="незаконнорождённый сын солдатки",
                             reviewed=False),
                       ),
          ),
    *page("185об",
          *death_month(Month.AUGUST,
                       # отец — вероятно, Лукьян Михайлович Янин; запись почти не читается
                       death(24, Gender.FEMALE, 5, None,
                             deceased=person("?", status=PEASANT_DAUGHTER, comment="имя не прочитано"),
                             relatives=[relative(person("Лукьянъ", "Михайловъ", "Янинъ", comment="отчество и фамилия читаются неуверенно"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             comment="номер записи на кадре не виден — поставлен по соседним; возраст не прочитан",
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
