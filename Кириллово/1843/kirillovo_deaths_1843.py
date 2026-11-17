from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import NATURAL
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE

kirillovo_deaths_1843 = death_records(
    "ЦГАРМ",
    "57",
    "1",
    "411",
    "Кириллово",
    "Казанская церковь",
    1843,
    *page(
        "?",
        *death_month(Month.JANUARY, death(1, Gender.MALE, 31, None, deceased=person("Иван", "Иванов", last_name_orig="Мальчиков"), age=60, cause_of_death=NATURAL)),
        *death_month(
            Month.JUNE,
            death(
                18,
                Gender.FEMALE,
                2,
                None,
                deceased=person("Анна", "Михайлова"),
                age=30,
                relatives=[relative(person("Александр", "Трофимов", last_name_orig="Калягин"), Relationship.HUSBAND)],
                cause_of_death=NATURAL,
                comment="исправлено по скану 02.10.2026: «Александра Трофимова Калягина жена Анна Михайлова»",
                reviewed=False,
            ),
        ),
        *death_month(
            Month.JULY,
            death(
                21,
                Gender.MALE,
                4,
                None,
                deceased=person("Марк", "Алексеев", last_name_orig="Янин", residence="Гоголев Бор"),
                age=37,
                comment="исправлено по скану 02.10.2026: месяц — ИЮЛЬ (в импорте «4 сентября 1844»); "
                        "запись идёт между №20 (3 июля) и №22 (5 июля); от натуральной, погребал иерей Александр Халев",
                reviewed=False,
            ),
        ),
    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
