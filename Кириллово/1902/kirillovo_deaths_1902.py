from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLD, COLIC, DIARRHEA, HEADACHE, OLD_AGE, WEAKNESS
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON, SOLDIER,
                                   WIDOW)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-307, альбом
# Photos «1902 (ГАПО 182-5-307)» (pk 1253), ч. 3 — лл. 240об–266об, 65 муж. / 74 жен. (по ведомости на л. 278об),
# прочитана целиком 25.10.2026; л. 239об — пустой, л. 240 — шмуцтитул; файл «л.240об.-250» — апрельский лист между лл.
# 249об и 250об; импортная ж. №68 сверена. Счёт общий. Вся запись — на левой странице, причина — на правой. Погребали
# свящ. Александр Васильев Писарев и Павел Богословский. 27.03.1902 (м. №13) погребен Михаил Константинович «Чекинъ», 30,
# — фамилия «Чекинъ», не Мальчиков; не выписан.
kirillovo_deaths_1902 = death_records(
    "ГАПО",
    "182",
    "5",
    "307",
    "Кириллово",
    "Казанская церковь",
    1902,
    *death_month(Month.FEBRUARY,
                 # Анна, дочь Николая Гавриловича Спиряева и Параскевы Никитичны Мальчиковой, р. 30.01.1902 (рожд. ж. №12)
                 death(11, Gender.FEMALE, 27, 28,
                       deceased=person("Анна", status=PEASANT_DAUGHTER), age="1 мес",
                       relatives=[relative(person("Николай", "Гавриловъ", "Спиряевъ"), Relationship.FATHER)],
                       cause_of_death=WEAKNESS,
                       comment="возраст читается неуверенно («1 мѣс.»?)",
                       page="242об",
                       reviewed=False),
                 ),
    *death_month(Month.MARCH,
                 # Матрона Гавриловна Мальчикова, р. 2.11.1899 (рожд. 1899 ж. №77), дочь Гавриила Васильевича «Юлина» (ум.
                 # 1900); мать Матрона Семеновна вышла за Федора Тимофеевича (брак 1901 №9)
                 death(15, Gender.FEMALE, 4, 5,
                       deceased=person("Матрона", status=PEASANT_DAUGHTER, comment="«падчерица»; = Матрона Гавриловна Мальчикова"), age=2,
                       relatives=[relative(person("Ѳеодоръ", "Тимоѳеевъ", "Шевлягинъ", status=SOLDIER, comment="«запасный рядовой»; отчим; в браке 1901 №9 фамилия прочитана «Шерденинъ»"), Relationship.STEP_FATHER)],
                       cause_of_death=COLD,
                       page="243об",
                       reviewed=False),
                 ),
    *death_month(Month.MAY,
                 # Анастасия Петровна Мальчикова — чья жена или вдова, не записано
                 death(36, Gender.FEMALE, 7, 8,
                       deceased=person("Анастасія", "Петрова", "Мальчикова"), age=55,
                       cause_of_death=OLD_AGE,
                       comment="причина читается неуверенно",
                       page="250об",
                       reviewed=False),
                 # Василий, сын Степана Степановича Мальчикова, р. 6.03.1901 (рожд. 1901 м. №23)
                 death(30, Gender.MALE, 20, 21,
                       deceased=person("Василій", status=PEASANT_SON), age="1 лет 6 мес",
                       relatives=[relative(person("Стефанъ", "Стефановъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       comment="в подлиннике «1½ г.»; имя отца записано дважды («Стефана) Стефана»)",
                       page="251об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Михаил, сын Ивана Тимофеевича Шевлягина и Пелагии Сергеевны «Сырцовой», р. 8.11.1896 (рожд. 1896 м. №69)
                 death(40, Gender.MALE, 9, 10,
                       deceased=person("Михаилъ", status=PEASANT_SON), age=5,
                       relatives=[relative(person("Иванъ", "Тимоѳеевъ", "Шевлягинъ"), Relationship.FATHER)],
                       cause_of_death=HEADACHE,
                       page="255об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Параскева, дочь Степана Степановича Мальчикова, р. 11.10.1896 (рожд. 1896 ж. №69)
                 death(46, Gender.FEMALE, 7, 8,
                       deceased=person("Параскева", status=PEASANT_DAUGHTER), age=5,
                       relatives=[relative(person("Стефанъ", "Стефановъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       comment="«(сынъ) дочь» — так в подлиннике; причина читается неуверенно",
                       page="256об",
                       reviewed=False),
                 ),
    *death_month(Month.SEPTEMBER,
                 # Пелагия Семеновна Мальчикова, вдова Сергея Дементьевича Ладыгина («Сѣрковъ», ум. 26.04.1901)
                 death(52, Gender.FEMALE, 25, 26,
                       deceased=person("Пелагія", "Семенова", "Сѣркова", status=WIDOW, comment="= Пелагия Семеновна Мальчикова, вдова Сергея Дементьевича Ладыгина"),
                       age=75,
                       cause_of_death=OLD_AGE,
                       page="259об",
                       reviewed=False),
                 ),
    *death_month(
        Month.DECEMBER,
        # импорт; сверено по скану 25.10.2026 (л. 264об): «½ г.», р. 14.04.1902 (рожд. ж. №29)
        death(
            68,
            Gender.FEMALE,
            4,
            5,
            deceased=person("Ирина", "Михайлова", "Мальчикова"),
            relatives=[relative(person("Михаил", "Константинов", "Мальчиков"), Relationship.FATHER)],
            cause_of_death=COLIC,
            age="6 мес",
            comment=" дата под вопросом по источнику; сверено по скану 25.10.2026: возраст «½ г.»",
            page="264об",
        ),
    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
