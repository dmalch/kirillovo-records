from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, NATURAL
from verso.ru.dsl.statuses import (HIEREUS, KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE,
                                   PEASANT_DAUGHTER, PRIVATE_SOLDIER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Альбом «1859 (ЦГАРМ 57-6-386)», pk 1295,
# ч. 3 — кадры 51–72.
kirillovo_deaths_1859 = death_records(
    "ЦГА республики Мордовия", "57", "6", "386", "Кириллово", "Казанская",
    1859,
    *page("?",
          *death_month(Month.JANUARY,
                       # мать — Александра Андреевна Мальчикова (брак 1845 №35); вторая волна, 07.11.2026
                       death(10, Gender.FEMALE, 20, 22,
                             deceased=person("Екатерина", status=PEASANT_DAUGHTER), age="2 мес",
                             relatives=[relative(person("Михаилъ", "Денисовъ", "Стюхинъ", status=PRIVATE_SOLDIER, comment="«уволенный по билету рядовой»"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                             comment="кадр 53 альбома",
                             reviewed=False),
                       ),
          *death_month(Month.JUNE,
                       # муж Елены Несторовны Мальчиковой (брак 1843)
                       death(34, Gender.MALE, 19, 21,
                             deceased=person("Александръ", "Трофимовъ", "Калягинъ"), age=50,
                             cause_of_death=CONSUMPTION,
                             priest=person("Андрей", last_name_orig="Глазуновъ", status=HIEREUS),
                             comment="кадр 60 альбома; возраст читается неуверенно",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=KAZENNYJ_PEASANT_MALE,
        status_female=KAZENNYJ_PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
