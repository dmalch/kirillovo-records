from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, NATURAL
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, HIEREUS, PEASANT_SON

# SELECTIVE EXTRACT: Only Мальчиков-family related entries from 1865 metric book.
# Archive reference unknown for this period; using placeholder.
# No page numbers available in source extract.
# No clergy names recorded in source extract.
# Death #68 (female, Праскева): relative is «вдова солдатка Анисия Петрова Мальчикова» — no relationship type stated.
# Since Анисия is the one reporting and she is a widow, she could be mother; relationship inferred as MOTHER.
# Death #89 (male, Иона): no relative listed.

kirillovo_deaths_1865 = death_records(
    "ГАПО",
    "182",
    "5",
    "710",
    "Кириллово",
    "Казанская церковь",
    1865,
    *death_month(
        Month.NOVEMBER,
        death(
            68,
            Gender.FEMALE,
            30,
            None,
            deceased=person("Праскева"),
            age=15,
            relatives=[relative(person("Анисия", "Петрова", last_name_orig="Мальчикова"), Relationship.MOTHER)],
            cause_of_death=CONSUMPTION,
            comment="Родственница — вдова солдатка; дата погребения не указана в источнике; отношение восстановлено как мать",
        ),
    ),
    *death_month(
        Month.DECEMBER,
        death(
            89,
            Gender.MALE,
            1,
            None,
            deceased=person("Иона", "Герасимов", last_name_orig="Мальчиков"),
            age=45,
            cause_of_death=CONSUMPTION,
            comment="Родственник не указан в источнике; дата погребения не указана в источнике",
        ),
    ),
    # Дописано при сплошном проходе (03.10.2026) по оригиналу Яндекс.Архива (сводное дело cffbc917-…)
    *page("?",
          *death_month(Month.MARCH,
                       # Андрей — сын Семена Емельяновича Мальчикова, род. 28.11.1864 (рожд. 1864 м. №121)
                       death(23, Gender.MALE, 18, None,
                             deceased=person("Андрей", status=PEASANT_SON), age="2 мес",
                             relatives=[relative(person("Семенъ", "Емельяновъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                             comment="скан 481; в графе дат одно число",
                             reviewed=False),
                       ),
          ),
    # Вторая волна (07.11.2026): дети дочерей Мальчиковых и Яниных, найдены поиском фамилий мужей по OCR Яндекс.Архива и
    # прочитаны по оригиналам
    *page("?",
          *death_month(Month.DECEMBER,
                       # Ѳедора Емельяновна Мальчикова, жена Ефима Алексеевича Киселева (брак 1839 №17)
                       death(71, Gender.FEMALE, 8, None,
                             deceased=person("Ѳедора", "Емельянова"), age=48,
                             relatives=[relative(person("Еѳимъ", "Алексѣевъ", "Киселевъ"), Relationship.HUSBAND)],
                             cause_of_death=NATURAL,
                             priest=person("Андрей", last_name_orig="Тихонравовъ", status=HIEREUS),
                             comment="скан 497 (ЦГАРМ 57-6-488, Яндекс.Архив cffbc917-…); в графе дат одно число",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
