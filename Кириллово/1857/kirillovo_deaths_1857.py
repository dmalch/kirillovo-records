from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, FEVER, NATURAL, THROAT
from verso.ru.dsl.statuses import (HIEREUS, KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE,
                                   PEASANT_DAUGHTER, PEASANT_SON, WIDOW)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. ЦГАРМ 57-6-406, Яндекс.Архив ad78aa12-…,
# ч. 3 Кириллова — сканы 715–749.
kirillovo_deaths_1857 = death_records(
    "ЦГАРМ", "57", "6", "406", "Кириллово", "Казанская",
    1857,
    *page("?",
          *death_month(Month.APRIL,
                       # «вдова Ѳеодора Иванова Мальчикова» — чья вдова, не сказано
                       death(29, Gender.FEMALE, 20, 22,
                             deceased=person("Ѳеодора", "Иванова", "Мальчикова", status=WIDOW), age=39,
                             cause_of_death=CONSUMPTION,
                             priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                             comment="скан 725; возраст читается 39 (или 34)",
                             reviewed=False),
                       ),
          *death_month(Month.AUGUST,
                       # Илья — сын Андрея Васильевича Мальчикова, род. 18.07.1857 (рожд. м. №70)
                       death(101, Gender.MALE, 6, 8,
                             deceased=person("Илья", status=PEASANT_SON), age="3 нед",
                             relatives=[relative(person("Андрей", "Васильевъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="скан 740",
                             reviewed=False),
                       # Степан Михайлович Мальчиков — в families/Мальчиковы.md не известен; фамилия читается неуверенно
                       # («Мал…ова»); в 1858 (рожд. м. №72) есть Стефан Михайлов ЕГОРОВ — возможно, он
                       death(109, Gender.MALE, 17, 19,
                             deceased=person("Давыдъ", status=PEASANT_SON), age=1,
                             relatives=[relative(person("Степанъ", "Михайловъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death=THROAT,
                             comment="скан 741",
                             reviewed=False),
                       ),
          ),
    # Вторая волна (07.11.2026): дети дочерей Мальчиковых и Яниных, найдены поиском фамилий мужей по OCR Яндекс.Архива и
    # прочитаны по оригиналам
    *page("?",
          *death_month(Month.JUNE,
                       # Яков — сын Николая Дементьевича Миронова и Евдокии Семеновны Мальчиковой, род. 24.04.1854
                       death(48, Gender.MALE, 13, 15,
                             deceased=person("Яковъ", status=PEASANT_SON), age=3,
                             relatives=[relative(person("Николай", "Дементьевъ", "Мироновъ"), Relationship.FATHER)],
                             cause_of_death=FEVER,
                             priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                             comment="скан 730; «отъ жару»",
                             reviewed=False),
                       ),
          *death_month(Month.JULY,
                       # мать — Елена Несторовна Мальчикова (брак 1843 №28)
                       death(72, Gender.FEMALE, 8, 10,
                             deceased=person("Параскева", status=PEASANT_DAUGHTER), age=1,
                             relatives=[relative(person("Александръ", "Трофимовъ", "Калягинъ"), Relationship.FATHER)],
                             cause_of_death=FEVER,
                             priest=person("Петръ", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                             comment="скан 736; «отъ жару»",
                             reviewed=False),
                       # мать — Ирина Несторовна Мальчикова (брак 1844 №10); Зиновия род. 2.11.1854 (рожд. ж. №92)
                       death(76, Gender.FEMALE, 9, 11,
                             deceased=person("Зиновія", status=PEASANT_DAUGHTER), age=3,
                             relatives=[relative(person("Григорій", "Тимоѳеевъ", "Разореновъ"), Relationship.FATHER)],
                             cause_of_death=THROAT,
                             priest=person("Василій", "Іоакимовъ", "Бѣльскій", status=HIEREUS),
                             comment="скан 737; «отъ боли въ горлѣ»",
                             reviewed=False),
                       # мать — Ульяна Антоновна Янина, вдова Ковалькова, за Евдокимом Зиновьевичем Кузиным с 1854
                       # (брак 1854 №9). Той же болезнью летом 1857 умерли и его дети от первой жены: Марфа 7 л. (1.08),
                       # Григорий 10 л. и Акилина 5½ л. (сканы 739–742) — не внесены
                       death(83, Gender.FEMALE, 26, 28,
                             deceased=person("Васса", status=PEASANT_DAUGHTER), age=2,
                             relatives=[relative(person("Евдокимъ", "Зиновьевъ", "Кузинъ"), Relationship.FATHER)],
                             cause_of_death=THROAT,
                             priest=person("Петръ", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                             comment="скан 738; «отъ боли въ горлѣ»",
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
