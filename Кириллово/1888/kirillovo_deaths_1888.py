from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, SUFFOCATION, THROAT
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   HIEREUS, MAIDEN, PEASANT_DAUGHTER, PEASANT_SON, PEASANT_WIFE)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей), и импортная запись.
# ГАПО 182-5-305, альбом Photos «1888 (ГАПО 182-5-305)» (pk 1303), ч. 3 — лл. 326об–349об (первая запись — смерть
# 30.12.1887), 66 муж. / 51 жен., прочитана целиком 24.10.2026. Вся запись — на левой странице, причина — на правой.
# Погребал свящ. Александр Васильев Писарев. 4.06.1888 погребён Марк, сын Михаила Васильевича Сигунова (рожд. м. №24 —
# восприемник Василий Константинович Мальчиков; смерть м. №28), 15.03 — Мария, дочь Ивана Федоровича Платончикова (рожд.
# ж. №11; смерть ж. №12) — не выписаны.
kirillovo_deaths_1888 = death_records(
    "ГАПО",
    "182",
    "5",
    "305",
    "Кириллово",
    "Казанская церковь",
    1888,
    *death_month(Month.MARCH,
                 # импорт; сверено по скану 24.10.2026 (л. 331об): Мария Федоровна, урожд. Курочкина, вторая жена Самсона Наумовича
                 # Янина (брак 1875 №21; первая, по браку 1852 №26, — Ксения Лукьяновна); возраст — «56» или «86»
                 death(11, Gender.FEMALE, 1, 3,
                       deceased=person("Мария", "Федорова", status=PEASANT_WIFE),
                       age=56,
                       relatives=[relative(person("Самсон", last_name_orig="Янин"), Relationship.HUSBAND)],
                       cause_of_death=SUFFOCATION,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="возраст читается и как «86»; по браку 1875 №21 (ей 52) ей было бы около 65",
                       page="331об"),
                 ),
    *death_month(Month.MAY,
                 # Александра Михайловна Янина («Сырдцева»), дочь Михаила Андреяновича
                 death(16, Gender.FEMALE, 8, 10,
                       deceased=person("Александра", "Михайлова", "Сырдцева", status=MAIDEN, comment="она же: Александра Михайловна Янина"),
                       age=18,
                       relatives=[relative(person("Михаилъ", None, "Сырдцевъ", comment="он же: Михаил Андреянович Янин"), Relationship.FATHER)],
                       cause_of_death=THROAT,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="причина в подлиннике «отъ горловой боли»",
                       page="334об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Акилина, дочь Михаила Васильевича Мальчикова («Юлинъ»), р. 11.06.1888 (рожд. ж. №35)
                 death(26, Gender.FEMALE, 24, 25,
                       deceased=person("Акилина", status=PEASANT_DAUGHTER), age="1 мес",
                       relatives=[relative(person("Михаилъ", "Васильевъ", "Юлинъ", comment="он же: Михаил Васильевич Мальчиков"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="339об",
                       reviewed=False),
                 ),
    *death_month(Month.SEPTEMBER,
                 # Александр, сын Евфимия Михайловича Стюхина и Марии Егоровны Яниной, р. 23.08.1888 (рожд. м. №63)
                 death(48, Gender.MALE, 7, 8,
                       deceased=person("Александръ", status=PEASANT_SON), age="2 нед",
                       relatives=[relative(person("Евфимій", None, "Стюхинъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="343об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Василий Григорьевич Мальчиков («Юлинъ»)
                 death(57, Gender.MALE, 14, 16,
                       deceased=person("Василій", "Григорьевъ", "Юлинъ", comment="«Юлинъ» — так в подлиннике; он же: Василий Григорьевич Мальчиков"),
                       age=50,
                       cause_of_death="отъ катарра желудка",
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="345об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
