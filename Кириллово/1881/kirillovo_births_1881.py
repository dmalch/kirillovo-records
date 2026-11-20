from verso.ru.dsl import Gender, Month, RecordDefaults, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   HIEREUS, MAIDEN, SOLDIER, SOLDIER_WIFE, UNTER_OFFICER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их замужние дочери). ГАПО 182-5-300,
# альбом Photos «1881 (ГАПО 182-5-300)» (pk 1269), ч. 1 — лл. 2–47об; прочитана целиком 12.10.2026. Запись на
# развороте: родители — на левой странице, восприемники — на правой. Левой страницы первого разворота (л. 1об, записи
# начала января) в наборе нет; записей июля–сентября (муж. № 38–56, жен. № 47–84) нет в самом деле: за л. 28 (июнь)
# сразу идёт л. 29 со старым номером «49» (октябрь) — двадцать листов книги утрачены до архивной нумерации. Крестил
# настоятель, священник Василий Иоаннов Ремезов (с псаломщиком диаконом Матфеем Рождественским). Книга пишет
# «государственный крестьянинъ». Мальчиковы — то «Мальчиковъ», то «Мамчиковъ»; Яковлевичи и их дети — «Поздняковы»,
# Янины Гоголева Бора — «Алешины».
kirillovo_births_1881 = birth_records(
    "ГАПО",
    "182",
    "5",
    "300",
    "Кириллово",
    "Казанская церковь",
    1881,
    *birth_month(Month.APRIL,
                 # Николай Петрович Мальчиков (р. 1856, сын Петра Акимовича) и Анна Михайловна; восприемники — Широковы
                 birth(31, Gender.FEMALE, 5, 6,
                       child=person("Ирина"),
                       father=person("Николай", "Петровъ", "Мальчиковъ"),
                       mother=person("Анна", "Михайлова"),
                       god_parent1=person("Ѳеодоръ", "Михайловъ", "Широковъ"),
                       god_parent2=person("Агаѳія", "Иванова", "Широкова"),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="16об",
                       reviewed=False),
                 ),
    *birth_month(Month.JUNE,
                 # Матфей Козьмич Мальчиков (брак 1870 №38 с Гликерией Степановной Широковой)
                 birth(44, Gender.FEMALE, 9, 10,
                       child=person("Акилина"),
                       father=person("Матвѣй", "Козминъ", "Мальчиковъ", status=SOLDIER, comment="в подлиннике «безсрочно-отпускной рядовой Матвѣй Казминъ Мамчаковъ»; он же: Матфей Козьмич Мальчиков"),
                       mother=person("Гликерія", "Стефанова"),
                       god_parent1=person("Петръ", "Ивановъ", "Щетининъ"),
                       god_parent2=person("Параскева", "Ильина", "Щетинина", status=MAIDEN),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       comment="номер переправлен",
                       page="28об",
                       reviewed=False),
                 ),
    *birth_month(Month.OCTOBER,
                 # восприемница — солдатка Ксения Карповна Белова, урожд. Янина
                 birth(62, Gender.MALE, 22, 24,
                       child=person("Яковъ"),
                       father=person("Иванъ", "Никитинъ", "Бѣловъ"),
                       mother=person("Ирина", "Ермолаева"),
                       god_parent1=person("Иванъ", "Никитинъ", "Бѣловъ", comment="так в подлиннике — восприемник назван так же, как отец (в 1879 у их сына Петра — Максим Никитин Белов)"),
                       god_parent2=person("Ксенія", "Карпова", "Бѣлова", status=SOLDIER_WIFE, comment="она же: Ксения Карповна Янина"),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="33об",
                       reviewed=False),
                 # Яков Андреевич «Алешинъ» (= Янин?) и вторая жена Евдокия Никифоровна (брак 1.10.1878); восприемница —
                 # Феодосия Филипповна, жена Семена Родионовича «Алешина»
                 birth(93, Gender.FEMALE, 30, 31,
                       child=person("Матрена"),
                       father=person("Яковъ", "Андреевъ", "Алешинъ", residence="Гоголев Бор", comment="«Алешинъ» — так в подлиннике; он же: Яков Андреевич Янин?"),
                       mother=person("Евдокія", "Никифорова"),
                       god_parent1=person("Филиппъ", "Климовъ", "Богачевъ", status=UNTER_OFFICER, residence="Гоголев Бор"),
                       god_parent2=person("Ѳеодосія", "Филиппова", "Алешина", residence="Гоголев Бор"),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="34об",
                       reviewed=False),
                 ),
    *birth_month(Month.NOVEMBER,
                 # восприемник — Федор Самсонович Янин (сын Самсона Наумовича)
                 birth(99, Gender.FEMALE, 10, 11,
                       child=person("Матрена"),
                       father=person("Мамонтъ", "Трофимовъ", "Чимикинъ"),
                       mother=person("Анна", "Іонова"),
                       god_parent1=person("Ѳеодоръ", "Самсоновъ", "Янинъ"),
                       god_parent2=person("Екатерина", "Сергѣева", "Чубукова", comment="фамилия читается неуверенно"),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="39об",
                       reviewed=False),
                 # Михаил Петрович Мальчиков (жена Матрена Андреевна); восприемник — Матфей Козьмич Мальчиков. Григорий умер
                 # 1.12.1881
                 birth(74, Gender.MALE, 17, 18,
                       child=person("Григорій"),
                       father=person("Михаилъ", "Петровъ", "Мальчиковъ"),
                       mother=person("Матрена", "Андреева"),
                       god_parent1=person("Матвѣй", "Козминъ", "Мальчиковъ", status=SOLDIER, comment="«рядовой»; он же: Матфей Козьмич Мальчиков"),
                       god_parent2=person("Анна", "Михайлова", "Шаркова", comment="фамилия читается неуверенно"),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="41об",
                       reviewed=False),
                 ),
    *birth_month(Month.DECEMBER,
                 # мать Анастасия Константиновна — дочь Константина Яковлевича Мальчикова («Позднякова»; восприемница
                 # 1872)? Восприемник — Василий Константинович «Поздняковъ» (= Мальчиков), брат матери?
                 birth(107, Gender.FEMALE, 11, 12,
                       child=person("Ульяна"),
                       father=person("Аѳанасій", "Яковлевъ", "Кобельковъ"),
                       mother=person("Анастасія", "Константинова", comment="она же: Анастасия Константиновна Мальчикова?"),
                       god_parent1=person("Василій", "Константиновъ", "Поздняковъ", comment="он же: Василий Константинович Мальчиков"),
                       god_parent2=person("Татіана", "Трофимова", "Позднякова", status=MAIDEN),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="46об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
