from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLD, COLIC, CONSUMPTION, DIARRHEA, DROPSY
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON,
                                   PEASANT_WIFE, SOLDIER, UNTER_OFFICER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-306, альбом
# Photos «1895 (ГАПО 182-5-306)» (pk 1188), ч. 3 — лл. 133об–151об, 55 муж. / 71 жен., прочитана целиком 25.10.2026;
# л. 133 — шмуцтитул; импорта не было. Вся запись — на левой странице, причина — на правой. Погребали свящ. Александр
# Васильев Писарев и Василий Георгиевич Кутин. 1.07.1895 погребена Екатерина, ½ г., дочь «находящегося на военной
# службе Ивана Евс…ова Стюхина» (сын Ефима Михайловича? отчество не разобрать) — не выписана.
kirillovo_deaths_1895 = death_records(
    "ГАПО",
    "182",
    "5",
    "306",
    "Кириллово",
    "Казанская церковь",
    1895,
    *death_month(Month.JANUARY,
                 # Христина Акимовна, вторая жена Петра Акимовича Мальчикова
                 death(3, Gender.FEMALE, 24, 26,
                       deceased=person("Христина", "Акимова", status=PEASANT_WIFE), age=57,
                       relatives=[relative(person("Петръ", "Акимовъ", "Мальчиковъ"), Relationship.HUSBAND)],
                       comment="причина у корешка («…душіе»?)",
                       page="133об",
                       reviewed=False),
                 ),
    *death_month(Month.MARCH,
                 # Тимофей, сын Ефима Михайловича Стюхина и Марии Егоровны Яниной (р. ок. 1876 — книг 1873–76 нет)
                 death(9, Gender.MALE, 18, 19,
                       deceased=person("Тимоѳей", status=PEASANT_SON), age=19,
                       relatives=[relative(person("Евфимъ", "Михайловъ", "Стюхинъ"), Relationship.FATHER)],
                       cause_of_death=COLD,
                       page="134об",
                       reviewed=False),
                 ),
    *death_month(Month.APRIL,
                 # Александра, дочь Ивана Тимофеевича Шевлягина и Пелагии Сергеевны «Сырцовой», р. 18.04.1895 (рожд. ж. №18)
                 death(11, Gender.FEMALE, 19, 20,
                       deceased=person("Александра", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Иванъ", "Тимоѳеевъ", "Шевлягинъ"), Relationship.FATHER)],
                       comment="возраст «1 д.»? читается неуверенно; «отъ слабости»",
                       page="136об",
                       reviewed=False),
                 ),
    *death_month(Month.MAY,
                 # Максим Михайлович Янин («Сырцевъ», брак 1890 №17); вдова Стефанида вышла 23.10.1895 (брак №12)
                 death(18, Gender.MALE, 30, 1,
                       b_month=Month.JUNE,
                       deceased=person("Максимъ", "Михайловъ", "Сырцевъ", status=SOLDIER, comment="«запасный рядовой»; он же: Максим Михайлович Янин"),
                       cause_of_death=CONSUMPTION,
                       comment="записан под июнем; возраст под ниткой переплета («2…»)",
                       page="138об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Матрона, дочь Ивана Ермолаевича Егорова, р. 20.03.1895 (рожд. ж. №13 — восприемница Дарья Порфирьевна
                 # Мальчикова)
                 death(43, Gender.FEMALE, 12, 13,
                       deceased=person("Матрона", status=PEASANT_DAUGHTER), age="3 мес",
                       relatives=[relative(person("Иванъ", "Ермолаевъ", "Егоровъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       page="142об",
                       reviewed=False),
                 # Иван, сын Ивана Степановича Широкова, р. 19.09.1893 (рожд. 1893 м. №54 — восприемник Михаил
                 # Константинович Мальчиков)
                 death(25, Gender.MALE, 12, 13,
                       deceased=person("Іоаннъ", status=PEASANT_SON), age="1 лет 6 мес",
                       relatives=[relative(person("Иванъ", "Степановъ", "Широковъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       comment="в подлиннике «1½»",
                       page="142об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Гликерия, дочь Семена Васильевича Мальчикова («Юлинъ»), р. 15.05.1895 (рожд. ж. №24)
                 death(49, Gender.FEMALE, 4, 5,
                       deceased=person("Гликерія", status=PEASANT_DAUGHTER), age="2 мес",
                       relatives=[relative(person("Семенъ", "Васильевъ", "Юлинъ", status=SOLDIER, comment="«находящійся на дѣйствительной службѣ рядовой»"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       comment="в подлиннике «2½ мѣс.»",
                       page="143об",
                       reviewed=False),
                 # Алексей Герасимович «Поздняковъ», запасный унтер-офицер — Алексей Герасимович Мальчиков? (Яковлевичи —
                 # то «Мальчиковы», то «Поздняковы»); не установлено
                 death(31, Gender.MALE, 4, 5,
                       deceased=person("Алексѣй", "Герасимовъ", "Поздняковъ", status=UNTER_OFFICER, comment="«запасный унтеръ-офицеръ»"),
                       age=25,
                       cause_of_death="отъ застарѣлой золотухи",
                       page="144об",
                       reviewed=False),
                 ),
    *death_month(Month.SEPTEMBER,
                 # Пелагия, дочь Петра Козьмича Щетинина, р. 8.05.1895 (рожд. ж. №23 — восприемник Андрей Николаевич
                 # Малахаев)
                 death(56, Gender.FEMALE, 19, 20,
                       deceased=person("Пелагія", status=PEASANT_DAUGHTER), age="4 мес",
                       relatives=[relative(person("Петръ", "Косьминъ", "Щетининъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       page="146об",
                       reviewed=False),
                 ),
    *death_month(Month.NOVEMBER,
                 # Петр Дмитриевич Янин (жена Параскева ум. 1893; сын Иван р. 10.09.1895)
                 death(51, Gender.MALE, 14, 15,
                       deceased=person("Петръ", "Димитріевъ", "Янинъ"), age=45,
                       cause_of_death=DROPSY,
                       page="149об",
                       reviewed=False),
                 ),
    *death_month(Month.DECEMBER,
                 # Никита, сын Дмитрия Андреевича «Малахаева», р. 26.05.1895 (рожд. м. №33)
                 death(55, Gender.MALE, 25, 26,
                       deceased=person("Никита", status=PEASANT_SON), age="7 мес",
                       relatives=[relative(person("Димитрій", "Андреевъ", "Малахаевъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       page="151об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
