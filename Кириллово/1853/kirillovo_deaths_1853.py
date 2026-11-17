from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, NATURAL
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER, PEASANT_SON

kirillovo_deaths_1853 = death_records(
    "ЦГАРМ",
    "57",
    "6",
    "430",
    "Кириллово",
    "Казанская церковь",
    1853,
    *page(
        "?",
        *death_month(
            Month.JUNE,
            death(
                22,
                Gender.FEMALE,
                10,
                12,
                deceased=person("Татьяна", "Петрова", last_name_orig="Мальчикова"),
                age=5 / 12,
                relatives=[relative(person("Петр", "Акимов", last_name_orig="Мальчиков"), Relationship.FATHER)],
                cause_of_death=DIARRHEA,
            ),
            death(
                25,
                Gender.FEMALE,
                18,
                20,
                deceased=person("Мария", "Климентьева", last_name_orig="Мальчикова"),
                age=1,
                relatives=[relative(person("Климент", "Антонов", last_name_orig="Мальчиков"), Relationship.FATHER)],
                cause_of_death=COLIC,
            ),
        ),
        *death_month(
            Month.JULY,
            death(
                35,
                Gender.MALE,
                25,
                27,
                deceased=person("Иван", "Дмитриев", last_name_orig="Мальчиков"),
                age="1 нед",
                relatives=[relative(person("Дмитрий", "Емельянов", last_name_orig="Мальчиков"), Relationship.FATHER)],
                cause_of_death=COLIC,
            ),
        ),
        *death_month(Month.AUGUST, death(48, Gender.MALE, 5, 7, deceased=person("Василий", comment="Василий — фамилия не указана"), age=75, cause_of_death=NATURAL)),
    ),
    # Дописано при сплошном проходе (02.10.2026) по скану (альбом pk 1314) — летом 1853 холера
    *page("?",
          *death_month(Month.AUGUST,
                       # Екатерина Васильевна Мальчикова, жена Семена Степановича Карасева
                       death(39, Gender.FEMALE, 2, 4,
                             deceased=person("Екатерина", "Васильева"), age=30,
                             relatives=[relative(person("Семенъ", "Стефановъ", "Карасевъ"), Relationship.HUSBAND)],
                             cause_of_death="эпидемическая холера",
                             comment="кадр 80 альбома",
                             reviewed=False),
                       # Михаил — сын Федора Антоновича Янина («Хрипуновъ»), род. 22.09.1848 (рожд. м. №82)
                       death(52, Gender.MALE, 7, 9,
                             deceased=person("Михаилъ", status=PEASANT_SON), age=5,
                             relatives=[relative(person("Ѳеодоръ", "Антоновъ", "Хрипуновъ", comment="так в подлиннике; Федор Антонович Янин"), Relationship.FATHER)],
                             cause_of_death="холера",
                             comment="кадр 82 альбома",
                             reviewed=False),
                       ),
          ),
    # Вторая волна (07.11.2026): дети дочерей Мальчиковых и Яниных, найдены поиском фамилий мужей по OCR Яндекс.Архива и
    # прочитаны по оригиналам
    *page("?",
          *death_month(Month.JUNE,
                       # мать — Евдокия Семеновна Мальчикова (брак 1850 №30); Афанасий род. 28.04.1853 (рожд. м. №34)
                       death(26, Gender.MALE, 1, 3,
                             deceased=person("Аѳанасій", status=PEASANT_SON), age="10 нед",
                             relatives=[relative(person("Николай", "Дементьевъ", "Мироновъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="скан 689 (Яндекс.Архив 22c876be-…); возрастъ «10½ недѣль»; погребалъ іерей Іоаннъ Реморовъ",
                             reviewed=False),
                       # мать — Ирина Несторовна Мальчикова (брак 1844 №10); Федор род. 22.05.1853 (рожд. м. №43)
                       death(29, Gender.MALE, 11, 13,
                             deceased=person("Ѳеодоръ", status=PEASANT_SON), age="2 мес",
                             relatives=[relative(person("Григорій", "Тимоѳеевъ", "Разореновъ"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             comment="скан 690; возрастъ «2½ мѣсяцевъ»; погребалъ іерей Василій Бѣльскій",
                             reviewed=False),
                       # мать — Екатерина Васильевна Мальчикова (брак 1844 №30, ум. 2.08.1853 холерой)
                       death(42, Gender.MALE, 27, 29,
                             deceased=person("Иванъ", status=PEASANT_SON), age=1,
                             relatives=[relative(person("Семенъ", "Стефановъ", "Карасевъ"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             comment="скан 694; погребалъ іерей Іоаннъ Реморовъ",
                             reviewed=False),
                       ),
          *death_month(Month.AUGUST,
                       # Елена — дочь Алексея Емельяновича «Пимкина» и Февронии Герасимовны Мальчиковой, род. 17.05.1851
                       # (рожд. ж. №40)
                       death(56, Gender.FEMALE, 15, 17,
                             deceased=person("Елена", status=PEASANT_DAUGHTER), age=2,
                             relatives=[relative(person("Алексѣй", "Емельяновъ", "Пимкинъ"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             comment="скан 702; месяц по соседним записям (холера в августе); погребалъ іерей Іоаннъ Реморовъ",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
