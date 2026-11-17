from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DROPSY, FEVER, NATURAL
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, HIEREUS, PEASANT_SON

kirillovo_deaths_1858 = death_records(
    "ЦГАРМ",
    "57",
    "6",
    "421",
    "Кириллово",
    "Казанская церковь",
    1858,
    *page(
        "?",
        *death_month(
            Month.MARCH,
            death(
                7,
                Gender.FEMALE,
                17,
                19,
                deceased=person("Варвара", "Яковлева", last_name_orig="Мальчикова"),
                age=85,
                relatives=[relative(person("Андриян", "Григорьев", last_name_orig="Мальчиков"), Relationship.HUSBAND)],
                cause_of_death=NATURAL,
            ),
        ),
        *death_month(
            Month.DECEMBER,
            death(
                55,
                Gender.FEMALE,
                9,
                11,
                deceased=person("Пелагея", "Михайлова", last_name_orig="Мальчикова", comment="В МК: [Куранова]"),
                age=40,
                relatives=[relative(person("Казьма", "Андриянов", last_name_orig="Мальчиков"), Relationship.HUSBAND)],
                cause_of_death=FEVER,
            ),
        ),
    ),
    # Дописано при сплошном проходе (02.10.2026) по скану (альбом «1858 (ЦГАРМ 57-6-421)», pk 1308; кадры альбома
    # в comment) — записи первой волны, которых не было в импорте из таблицы
    *page("?",
          *death_month(Month.APRIL,
                       # Варвара Несторовна Мальчикова МЕНЬШАЯ (~1825, РС8), жена Феофилакта Агаповича Пухова: старшая
                       # (р. 1818), жена Петра Лаврентьевича Стрекалина, рожает ещё в 1859 (рожд. ж. №78)
                       death(13, Gender.FEMALE, 18, 20,
                             deceased=person("Варвара", "Нестерова"), age=33,
                             relatives=[relative(person("Ѳеофилактъ", "Агаповъ", "Пуховъ"), Relationship.HUSBAND)],
                             cause_of_death=DROPSY,
                             priest=person("Василій", "Іоакимовъ", "Бѣльскій", status=HIEREUS),
                             comment="кадр 57 альбома",
                             reviewed=False),
                       ),
          *death_month(Month.AUGUST,
                       # Ѳеодор — сын Артемия Максимовича Романова из Гоголева Бора, род. 1.06.1858 (рожд. м. №51)
                       death(32, Gender.MALE, 5, 7,
                             deceased=person("Ѳеодоръ", status=PEASANT_SON, residence="Гоголев Бор", comment="читается и «Ѳеодотъ»"),
                             age="2 мес",
                             relatives=[relative(person("Артемій", "Максимовъ", "Романовъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             priest=person("Василій", "Іоакимовъ", "Бѣльскій", status=HIEREUS),
                             comment="кадр 64 альбома",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
