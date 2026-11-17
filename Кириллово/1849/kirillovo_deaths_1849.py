from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, NATURAL, SMALLPOX
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE, PEASANT_DAUGHTER,
                                   PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. ЦГАРМ 57-6-325, Яндекс.Архив
# 7ed02b94-…, ч. 3 Кириллова — сканы 429–451, разворот л. (скан − 9)об–(скан − 8).
kirillovo_deaths_1849 = death_records(
    "ЦГА республики Мордовия", "57", "6", "325", "Кириллово", "Казанская",
    1849,
    *page("421об",
          *death_month(Month.JANUARY,
                       # Дмитрий Емельянович Мальчиков — в families/Мальчиковы.md не известен (сын Емельяна Григорьевича?)
                       death(1, Gender.MALE, 1, 3,
                             deceased=person("Александръ", status=PEASANT_SON), age=1,
                             relatives=[relative(person("Димитрій", "Емельяновъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death=SMALLPOX,
                             comment="скан 430",
                             reviewed=False),
                       ),
          ),
    *page("431об",
          *death_month(Month.JUNE,
                       # «женка Ирина Григорьева Мальчикова» — муж не назван; Ирина Григорьевна, жена Емельяна
                       # Емельяновича (рожд. 1848 ж. №9)?
                       death(32, Gender.FEMALE, 2, 4,
                             deceased=person("Ирина", "Григорьева", "Мальчикова", comment="«казенная крестьянка женка»"), age=31,
                             cause_of_death=CONSUMPTION,
                             comment="скан 440",
                             reviewed=False),
                       ),
          ),
    *page("434об",
          *death_month(Month.AUGUST,
                       # Иоанн — сын Даниила Ивановича Янина из Гоголева Бора, род. 28.07.1849 (рожд. м. №41)
                       death(42, Gender.MALE, 3, 5,
                             deceased=person("Іоаннъ", status=PEASANT_SON, residence="Гоголев Бор"), age="2 нед",
                             relatives=[relative(person("Даніилъ", "Ивановъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="скан 443",
                             reviewed=False),
                       ),
          ),
    *page("436об",
          *death_month(Month.SEPTEMBER,
                       # Марья Давыдовна, жена Федора Антоновича Янина (брак 1840)
                       death(44, Gender.FEMALE, 16, 18,
                             deceased=person("Марія", "Давыдова"), age=35,
                             relatives=[relative(person("Ѳеодоръ", "Антоновъ", "Янинъ"), Relationship.HUSBAND)],
                             cause_of_death=CONSUMPTION,
                             comment="скан 445",
                             reviewed=False),
                       ),
          ),
    # Вторая волна (07.11.2026): дети дочерей Мальчиковых и Яниных, найдены поиском фамилий мужей по OCR Яндекс.Архива и
    # прочитаны по оригиналам
    *page("424об",
          *death_month(Month.JANUARY,
                       # отец — Александр Трофимович Калягин; первая жена Анна Михайловна Янина (брак 1832 №21,
                       # ум. 1843), вторая — Елена Несторовна Мальчикова (брак 1843 №28). Стефанида 9 лет — дочь
                       # первой жены, если возраст в годах
                       death(14, Gender.FEMALE, 25, 27,
                             deceased=person("Стефанида", status=PEASANT_DAUGHTER), age=9,
                             relatives=[relative(person("Александръ", "Трофимовъ", "Калягинъ"), Relationship.FATHER)],
                             cause_of_death=None,
                             comment="скан 433; в графе лѣтъ «9» без единицы; причина читается «коликаго»?; погребалъ "
                                     "іерей Іоаннъ Реморовъ съ пономаремъ Петромъ Савельевымъ",
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
