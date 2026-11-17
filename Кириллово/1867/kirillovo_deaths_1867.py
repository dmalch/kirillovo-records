from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import CONSUMPTION, NATURAL, SCARLATINA
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, HIEREUS,
                                   PEASANT_DAUGHTER, SOLDIER, SOLDIER_WIFE)

# Вторая волна (08.11.2026): дети и жёны замужних дочерей Мальчиковых и Яниных, найденные по имени мужа.
# Альбом Photos «1867 (ГАПО 182-5-710)» (pk 1322), ч. 3 — лл. 313об–324об (январь – 12 мая); дальше в альбоме
# листов нет. Прочитана по графе умерших ради второй волны; Пелагии Несторовны Ладыгиной в ней нет.
kirillovo_deaths_1867 = death_records(
    "ГАПО",
    "182",
    "5",
    "710",
    "Кириллово",
    "Казанская церковь",
    1867,
    *page("314об",
          *death_month(Month.JANUARY,
                       # Татьяна — дочь Григория Тимофеевича Разоренова и Ирины Несторовны Мальчиковой (брак 1844)
                       death(5, Gender.FEMALE, 24, None,
                             deceased=person("Татьяна", status=PEASANT_DAUGHTER), age=8,
                             relatives=[relative(person("Григорій", "Тимоѳеевъ", "Разореновъ"), Relationship.FATHER)],
                             cause_of_death=SCARLATINA,
                             priest=person("Василій", last_name_orig="Грандовъ", status=HIEREUS),
                             comment="съ діакономъ Василіемъ Пертовскимъ и дьячкомъ Михаиломъ Богдановымъ",
                             reviewed=False),
                       ),
          ),
    *page("324об",
          *death_month(Month.MAY,
                       # Васса Ионовна — жена Григория Меркурьевича Чекмурина (брак 1859)
                       death(32, Gender.FEMALE, 10, None,
                             deceased=person("Васса", "Іонова", status=SOLDIER_WIFE, comment="«служащаго въ военномъ полку Григорія Меркурьева жена»"), age=27,
                             relatives=[relative(person("Григорій", "Меркурьевъ", status=SOLDIER, comment="фамилия не написана — Чекмурин"), Relationship.HUSBAND)],
                             cause_of_death=CONSUMPTION,
                             priest=person("Андрей", last_name_orig="Тихомировъ", status=HIEREUS),
                             comment="съ діакономъ Матѳеемъ Рождественскимъ и дьячкомъ Николаемъ Трофимовымъ Яхонтовымъ",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE, cause_of_death=NATURAL),
)
