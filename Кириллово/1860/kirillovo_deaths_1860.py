from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, NATURAL
from verso.ru.dsl.statuses import (HIEREUS, KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE,
                                   PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. ЦГАРМ 57-6-440, Яндекс.Архив 2fd60b33-…,
# ч. 3 Кириллова — сканы 659–680. «Денисъ Егоровъ Позняковъ», 80 л., ум. 19.02.1860 (скан 661) — не взят: Денис
# Егорович Янин или Позняков — не решено.
kirillovo_deaths_1860 = death_records(
    "ЦГА республики Мордовия", "57", "6", "440", "Кириллово", "Казанская",
    1860,
    *page("?",
          *death_month(Month.MARCH,
                       # Ксения Ивановна (Познякова, брак 1854 №30), жена Евдокима Емельяновича Мальчикова; родила 7.02.1860
                       death(9, Gender.FEMALE, 26, 28,
                             deceased=person("Ксенія", "Иванова"), age=26,
                             relatives=[relative(person("Евдокимъ", "Емельяновъ", "Мальчиковъ"), Relationship.HUSBAND)],
                             cause_of_death=CONSUMPTION,
                             priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                             comment="скан 663",
                             reviewed=False),
                       ),
          *death_month(Month.APRIL,
                       # Василий — сын Петра Акимовича Мальчикова, род. 22.03.1859 (рожд. 1859 м. №25)
                       death(16, Gender.MALE, 7, 9,
                             deceased=person("Василій", status=PEASANT_SON), age=1,
                             relatives=[relative(person("Петръ", "Акимовъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                             comment="скан 664",
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
