from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, PLEURISY
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_SON

kirillovo_deaths_1846 = death_records(
    "ЦГАРМ",
    "57",
    "1",
    "418",
    "Кириллово",
    "Казанская церковь",
    1846,
    *page(
        "?",
        *death_month(
            Month.APRIL,
            death(
                10,
                Gender.MALE,
                15,
                17,
                deceased=person("Ермолай", "Кузьмин", last_name_orig="Мальчиков"),
                age=1,
                relatives=[relative(person("Казьма", "Андреянов", last_name_orig="Мальчиков"), Relationship.FATHER)],
                cause_of_death=COLIC,
            ),
        ),
        *death_month(
            Month.SEPTEMBER,
            death(
                26,
                Gender.MALE,
                25,
                27,
                deceased=person("Федор"),
                age=1,
                relatives=[relative(person("Дмитрий", "Михайлов", last_name_orig="Янин"), Relationship.FATHER)],
                cause_of_death=PLEURISY,
            ),
        ),
    ),
    # Вторая волна (07.11.2026): дети замужних дочерей Мальчиковых и Яниных, найденные по имени мужа (альбом
    # «1846 (ЦГАРМ 57-1-418)», pk 1291; номера листов на кадрах не видны — «?», в comment кадр альбома)
    *page("?",
          *death_month(Month.SEPTEMBER,
                       # Василий — сын Алексея Емельяновича и Февронии Герасимовны Мальчиковой, род. 14.04.1846
                       # (рожд. м. №36)
                       death(27, Gender.MALE, 28, 30,
                             deceased=person("Василій", status=PEASANT_SON), age=0.25,
                             relatives=[relative(person("Алексѣй", "Емельяновъ", "Лапшинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="возраст «3хъ мѣсяцевъ» — так в подлиннике, по рождению 5½ мес.; погребалъ іерей Іоаннъ Ремезовъ; кадр 63 альбома",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
