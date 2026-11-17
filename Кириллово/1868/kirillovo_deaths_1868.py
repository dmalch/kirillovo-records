from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, FEVER, NATURAL
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, HIEREUS, PEASANT_SON, SOLDIER,
                                   SOLDIER_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. ГАПО 182-5-711, альбом Photos
# «1868 (ГАПО 182-5-711)» (pk 3482), ч. 3 — лл. 203об–222, 82 погребения; прочитана целиком 03.10.2026. В графе дат
# одно число (смерти); лист — в comment.
kirillovo_deaths_1868 = death_records(
    "ГАПО",
    "182",
    "5",
    "711",
    "Кириллово",
    "Казанская церковь",
    1868,
    *page("?",
          *death_month(Month.JANUARY,
                       # Сидор (Исидор) — сын Игната Ивановича Ладыгина и Пелагии Несторовны Мальчиковой, крещ. 12.05.1867
                       # (рожд. 1867 м. №57)
                       death(4, Gender.MALE, 16, 18,
                             deceased=person("Исидоръ", status=PEASANT_SON, comment="в подлиннике «Сидоръ»"), age="6 мес",
                             relatives=[relative(person("Игнатъ", "Ивановъ", "Ладыгинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             priest=person("Андрей", last_name_orig="Тихомировъ", status=HIEREUS),
                             comment="л. 203об; возраст «полгода»",
                             reviewed=False),
                       ),
          *death_month(Month.APRIL,
                       # «деревни Гоголева Бора изъ казенныхъ Захаръ Григорьевъ» без фамилии — Захар Григорьевич Янин из
                       # Гоголева Бора (поручитель 1863)? Не установлено
                       death(17, Gender.MALE, 30, None,
                             deceased=person("Захаръ", "Григорьевъ", residence="Гоголев Бор", comment="фамилии нет; = Захар Григорьевич Янин?"),
                             age=70,
                             priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                             comment="л. 209об",
                             reviewed=False),
                       ),
          *death_month(Month.OCTOBER,
                       # Мария Агаповна — жена Петра Акимовича Мальчикова, мать Пелагии (рожд. 1868 ж. №22)
                       death(37, Gender.FEMALE, 12, None,
                             deceased=person("Марія", "Агапова"), age=32,
                             relatives=[relative(person("Петръ", "Акимовъ", "Мальчиковъ", comment="имя написано стёрто, читается неуверенно"), Relationship.HUSBAND)],
                             cause_of_death=FEVER,
                             priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                             comment="л. 219об; «отъ горячки»",
                             reviewed=False),
                       ),
          ),
    # Вторая волна (08.11.2026): дети замужних дочерей Мальчиковых и Яниных, найденные по имени мужа
    *page("208об",
          *death_month(Month.APRIL,
                       # Петр — сын Матвея Ивановича Каверкина и Феодоры Федоровны, род. 27.08.1867 (рожд. м. №89)
                       death(14, Gender.MALE, 7, None,
                             deceased=person("Петръ", status=PEASANT_SON), age="6 мес",
                             relatives=[relative(person("Матѳей", "Ивановъ", "Каверкинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="возраст «6 мѣсяц» читается неуверенно (по рождению 7 мес.); погребалъ дьячекъ Николай Трофимовъ",
                             reviewed=False),
                       ),
          ),
    *page("210об",
          *death_month(Month.MAY,
                       # мать — Феврония Петровна Мальчикова (брак 1852 с Трофимом Пимоновичем Бубенчиковым)
                       death(19, Gender.MALE, 30, None,
                             deceased=person("Спиридонъ", status=SOLDIER_SON, comment="имя читается неуверенно"), age=0.5,
                             relatives=[relative(person("Трофимъ", "Пимоновъ", "Бубенчиковъ", status=SOLDIER, comment="«безсрочно-отпускной солдатъ»"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             priest=person("Андрей", last_name_orig="Тихомировъ", status=HIEREUS),
                             comment="съ дьячкомъ Герасимомъ Григорьевымъ",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE,
                            cause_of_death=NATURAL),
)
