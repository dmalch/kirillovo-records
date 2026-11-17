from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import NATURAL, PLEURISY
from verso.ru.dsl.statuses import KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE, PEASANT_SON

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Ч. 3 — кадры 59–73 альбома
# «1845 (ЦГАРМ 57-1-415)», pk 1329; номера листов на кадрах не видны. Кадры 74–75 — обложка дела 415А.
kirillovo_deaths_1845 = death_records(
    "ЦГАРМ", "57", "1", "415", "Кириллово", "Казанская",
    1845,
    *page("?",
          *death_month(Month.JULY,
                       # Петр — сын Даниила Ивановича Янина из Гоголева Бора, род. 28.06.1845 (рожд. м. №59, отец там
                       # «Янинъ»); здесь фамилия «Косолановъ» (ср. брак 1840 №18 — «Даниил Иванов Косолапов»)
                       death(16, Gender.MALE, None, 24,
                             deceased=person("Петръ", status=PEASANT_SON, residence="Гоголев Бор"), age="1 мес",
                             relatives=[relative(person("Даніилъ", "Ивановъ", "Косолановъ", comment="так в подлиннике; Янин"), Relationship.FATHER)],
                             cause_of_death=PLEURISY,
                             comment="день смерти не виден, 24 — день погребения; кадр 67 альбома",
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
