from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, FEVER
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER,
                                   PEASANT_SON)

kirillovo_deaths_1854 = death_records(
    "ЦГАРМ",
    "57",
    "6",
    "378",
    "Кириллово",
    "Казанская церковь",
    1854,
    *page("?", *death_month(Month.JUNE, death(25, Gender.MALE, 9, 11, deceased=person("Петр", "Григорьев", last_name_orig="Мальчиков"), age=46, cause_of_death=FEVER))),
    # Дописано при сплошном проходе (02.10.2026) по скану (альбом pk 1326)
    *page("?",
          *death_month(Month.JUNE,
                       # Никита — сын Андрея Ивлиевича Романова и Татьяны Несторовны Мальчиковой, род. 3.04.1854
                       death(26, Gender.MALE, 11, 13,
                             deceased=person("Никита", status=PEASANT_SON), age="2 мес",
                             relatives=[relative(person("Андрей", "Ивліевъ", "Романовъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="кадр 70 альбома",
                             reviewed=False),
                       ),
          *death_month(Month.JULY,
                       # Марфа — дочь Даниила Ивановича Янина из Гоголева Бора, род. 4.07.1854
                       death(25, Gender.FEMALE, 14, 16,
                             deceased=person("Марѳа", status=PEASANT_DAUGHTER, residence="Гоголев Бор"), age="12 дн",
                             relatives=[relative(person("Даніилъ", "Ивановъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="кадр 73 альбома",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
