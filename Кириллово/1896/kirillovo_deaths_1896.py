from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, COUGH, DIARRHEA, PARALYSIS
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON, PEASANT_WIFE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-306, альбом
# Photos «1896 (ГАПО 182-5-306)» (pk 1207), ч. 3 — лл. 200об–218об, 46 муж. / 47 жен., прочитана целиком 25.10.2026;
# л. 199об — пустой бланк ч. 2, л. 200 — шмуцтитул; импорта не было. Вся запись — на левой странице, причина — на
# правой. Погребали свящ. Александр Васильев Писарев и Василий Георгиевич Кутин. На л. 215об поверх правой страницы
# подшит оторванный лист с погребениями ж. №43–45 ноября (не наши). 1.09.1896 погребен Иоанн, 1 нед., сын Антона
# Ивановича «Сѣркова» (= Ладыгина; рожд. м. №54) — не выписан, см. рождения 1896.
kirillovo_deaths_1896 = death_records(
    "ГАПО",
    "182",
    "5",
    "306",
    "Кириллово",
    "Казанская церковь",
    1896,
    *death_month(Month.MARCH,
                 # Михаил Адрианович (Андреянович) Янин
                 death(14, Gender.MALE, 19, 20,
                       deceased=person("Михаилъ", "Адріановъ", "Сырцевъ", comment="= Михаил Андреянович Янин"), age=68,
                       cause_of_death=PARALYSIS,
                       page="203об",
                       reviewed=False),
                 ),
    *death_month(Month.APRIL,
                 # Мария Егоровна Янина («Сырцова»), жена Ефима Михайловича Стюхина (брак 1867 №6)
                 death(10, Gender.FEMALE, 7, 9,
                       deceased=person("Марія", "Егорова", status=PEASANT_WIFE, comment="= Мария Егоровна Янина"), age=45,
                       relatives=[relative(person("Евфимій", "Михайловъ", "Стюхинъ"), Relationship.HUSBAND)],
                       cause_of_death=PARALYSIS,
                       page="204об",
                       reviewed=False),
                 ),
    *death_month(Month.JUNE,
                 # Гликерия, дочь Михаила Васильевича Мальчикова («Юлинъ»), р. 8.05.1896 (рожд. ж. №26)
                 death(17, Gender.FEMALE, 26, 27,
                       deceased=person("Гликерія", status=PEASANT_DAUGHTER), age="1 мес",
                       relatives=[relative(person("Михаилъ", "Васильевъ", "Юлинъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       comment="в подлиннике «1½ мѣс.»",
                       page="207об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Василий Константинович Мальчиков — сын Константина Яковлевича? не установлено
                 death(29, Gender.MALE, 2, 3,
                       deceased=person("Василій", "Константиновъ", "Мальчиковъ"), age=34,
                       cause_of_death=PARALYSIS,
                       page="210об",
                       reviewed=False),
                 # Трофим, сын Ивана Михайловича Богачева и Марии Андреевны Мальчиковой («Юлина»), р. 9.04.1895 (рожд. 1895
                 # м. №21)
                 death(30, Gender.MALE, 9, 10,
                       deceased=person("Трофимъ", status=PEASANT_SON), age="1 лет 6 мес",
                       relatives=[relative(person("Иванъ", "Михайловъ", "Богачевъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       comment="в подлиннике «1½ г.»",
                       page="211об",
                       reviewed=False),
                 # Акилина, дочь Андрея Матвеевича Мальчикова, р. 17.06.1896 (рожд. ж. №37)
                 death(27, Gender.FEMALE, 9, 11,
                       deceased=person("Акилина", status=PEASANT_DAUGHTER), age="5 нед",
                       relatives=[relative(person("Андрей", "Матвѣевъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       page="211об",
                       reviewed=False),
                 # Матрона, дочь Николая Гавриловича Спиряева и Параскевы Никитичны Мальчиковой, р. 7.11.1895 (рожд. 1895 ж.
                 # №77)
                 death(29, Gender.FEMALE, 22, 24,
                       deceased=person("Матрона", status=PEASANT_DAUGHTER), age="9 мес",
                       relatives=[relative(person("Николай", "Гавріиловъ", "Спиряевъ"), Relationship.FATHER)],
                       cause_of_death=COUGH,
                       page="212об",
                       reviewed=False),
                 ),
    *death_month(Month.SEPTEMBER,
                 # Сергей, сын Федора Трофимовича Паршина и Феодосии Николаевны «Малахаевой», р. 7.09.1896 (рожд. м. №56)
                 death(36, Gender.MALE, 23, 24,
                       deceased=person("Сергій", status=PEASANT_SON), age="2 нед",
                       relatives=[relative(person("Ѳеодоръ", None, "Паршинъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       comment="причина у корешка («отъ ко[ли]ки»?)",
                       page="212об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
