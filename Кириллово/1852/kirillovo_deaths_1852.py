from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import DIARRHEA, NATURAL, THROAT
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, HIEREUS, PEASANT_SON

kirillovo_deaths_1852 = death_records(
    "ЦГАРМ",
    "57",
    "1",
    "427а",
    "Кириллово",
    "Казанская церковь",
    1852,
    *page(
        "?",
        *death_month(
            Month.AUGUST,
            death(
                40,
                Gender.MALE,
                22,
                24,
                deceased=person("Петр", "Родионов", last_name_orig="Янин", residence="д. Гоголев Бор"),
                age="2 мес",
                relatives=[relative(person("Родион", "Алексеев", last_name_orig="Янин" ), None)],
                cause_of_death=DIARRHEA,
            ),
        ),
        *death_month(
            Month.OCTOBER,
            death(53, Gender.MALE, 28, 30, deceased=person("Андрей", "Иванов", last_name_orig="Мальчиков"), age=75, cause_of_death=NATURAL),
        ),
    ),
    # Вторая волна (07.11.2026): дети дочерей Мальчиковых и Яниных, найдены поиском фамилий мужей по OCR Яндекс.Архива и
    # прочитаны по оригиналам
    *page("?",
          *death_month(Month.AUGUST,
                       # Петр — сын Гавриила Ивановича Романова и Мелании Романовны Яниной, род. 21.11.1851
                       death(37, Gender.MALE, 12, 14,
                             deceased=person("Петръ", status=PEASANT_SON, residence="Гоголев Бор"), age="6 мес",
                             relatives=[relative(person("Гавріилъ", "Ивановъ", "Романовъ"), Relationship.FATHER)],
                             cause_of_death=THROAT,
                             priest=person("Василій", "Іоакимовъ", "Бѣльскій", status=HIEREUS),
                             comment="скан 662 (Яндекс.Архив d625e949-…); возрастъ «½ года»; «отъ гортани»",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
