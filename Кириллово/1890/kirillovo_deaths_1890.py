from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, COUGH, DIARRHEA, FEVER, WEAKNESS
from verso.ru.dsl.statuses import (HIEREUS, PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE,
                                   PEASANT_SON, UNTER_OFFICER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей), и импортные записи.
# ГАПО 182-5-305, альбом Photos «1890 (ГАПО 182-5-305)» (pk 1324), ч. 3 — лл. 178об–200об, прочитана целиком 25.10.2026.
# Лист 178об–179 рваный (январь); шмуцтитул ч. 3 подшит после него (кадр «л.179об.-180»); кадр «л.183аоб.-184» — апрель–
# май, в альбоме стоит перед кадром «л.183об.-183а»; декабрь — на лл. 199об и 200об, низ л. 199об оборван. Вся запись —
# на левой странице, причина — на правой. Погребал свящ. Александр Васильев Писарев.
kirillovo_deaths_1890 = death_records(
    "ГАПО",
    "182",
    "5",
    "305",
    "Кириллово",
    "Казанская церковь",
    1890,
    *death_month(Month.MARCH,
                 # Василий, сын Матвея Матвеевича Янина («Сырцевъ»), р. 6.03.1889 (рожд. 1889 м. №20)
                 death(8, Gender.MALE, 10, 11,
                       deceased=person("Василій", status=PEASANT_SON), age=1,
                       relatives=[relative(person("Матвѣй", None, "Сырцевъ", comment="= Матвей Матвеевич Янин"), Relationship.FATHER)],
                       cause_of_death=COUGH,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="181об",
                       reviewed=False),
                 # импорт; сверено по скану 25.10.2026 (л. 182об): «крестьянина Михаила Мальчикова сынъ Стефанъ», 5 дней
                 death(
                     11,
                     Gender.MALE,
                     28,
                     29,
                     deceased=person("Стефан"),
                     age=5 / 365,
                     relatives=[relative(person("Михаил", "Петров", last_name_orig="Мальчиков"), Relationship.FATHER)],
                     cause_of_death=WEAKNESS,
                     comment="Возраст в МК: 5 дней; отчество отца [Петров] восстановлено по контексту",
                     page="182об",
                 ),
                 ),
    *death_month(Month.JUNE,
                 # Анна, дочь Лаврентия Андреевича Оркишкина, р. 23.01.1890 (рожд. ж. №5 — восприемница Матрона Семеновна
                 # Юлина)
                 death(22, Gender.FEMALE, 18, 19,
                       deceased=person("Анна", status=PEASANT_DAUGHTER), age="5 мес",
                       relatives=[relative(person("Лаврентій", None, "Оркишкинъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="единица возраста у корешка; по рождению ей без малого 5 мес.",
                       page="185об",
                       reviewed=False),
                 # импорт; сверено по скану 25.10.2026 (л. 186об): «крестьянина Ивана Мальчикова дочь Гликерія», 1 мѣс.
                 death(
                     25,
                     Gender.FEMALE,
                     24,
                     25,
                     deceased=person("Гликерия"),
                     age=0.08,
                     relatives=[relative(person("Иван", "Климов", last_name_orig="Мальчиков"), Relationship.FATHER)],
                     cause_of_death=DIARRHEA,
                     comment="Возраст в МК: 1 месяц (≈ 0.08 года); отчество отца [Климов] восстановлено по контексту",
                     page="186об",
                 ),
                 ),
    *death_month(Month.JULY,
                 # сын Егора Михайловича Янина («Сырцевъ»); в рождениях 1890 Захарии нет — у Егора Михайловича р. 23.03.1890
                 # Лазарь (рожд. м. №15); один ли это ребёнок, не установлено
                 death(28, Gender.MALE, 6, 7,
                       deceased=person("Захарій", status=PEASANT_SON), age="3 мес",
                       relatives=[relative(person("Егоръ", None, "Сырцевъ", comment="= Егор Михайлович Янин?"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="189об",
                       reviewed=False),
                 # Феврония, дочь Якова Логиновича Строева и Анны Николаевны Мальчиковой, р. 23.06.1890 (рожд. ж. №39)
                 death(34, Gender.FEMALE, 7, 8,
                       deceased=person("Ѳевронія", status=PEASANT_DAUGHTER), age="2 нед",
                       relatives=[relative(person("Яковъ", None, "Строевъ", status=UNTER_OFFICER, comment="«запасный унтеръ-офицеръ»"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="189об",
                       reviewed=False),
                 # Ольга, дочь Михаила Егоровича Тиманова, р. 5.07.1890 (рожд. ж. №43 — восприемница Домна Васильевна Белова)
                 death(41, Gender.FEMALE, 22, 23,
                       deceased=person("Ольга", status=PEASANT_DAUGHTER), age="2 нед",
                       relatives=[relative(person("Михаилъ", None, "Тимановъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="191об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # импорт; сверено по скану 25.10.2026 (л. 195об): «крестьянина Михаила Мальчикова жена Матрона Андреева», 39
                 death(
                     57,
                     Gender.FEMALE,
                     31,
                     1,
                     b_month=Month.SEPTEMBER,
                     deceased=person("Матрона", "Андреева", last_name_orig="Мальчикова"),
                     age=39,
                     relatives=[relative(person("Михаил", "Петров", last_name_orig="Мальчиков"), Relationship.HUSBAND)],
                     cause_of_death=FEVER,
                     comment="День погребения — 1-е (следующего месяца, сентября); отчество мужа [Петров] восстановлено по контексту",
                     page="195об",
                 ),
                 ),
    *death_month(Month.NOVEMBER,
                 # Акилина, дочь Гавриила Васильевича Мальчикова («Юлинъ»), р. 5.06.1889 (рожд. 1889 ж. №29)
                 death(63, Gender.FEMALE, 20, 21,
                       deceased=person("Акилина", status=PEASANT_DAUGHTER), age=1,
                       relatives=[relative(person("Гавріилъ", None, "Юлинъ", comment="= Гавриил Васильевич Мальчиков"), Relationship.FATHER)],
                       cause_of_death=None,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="причина на рваном краю листа («отъ ка…»)",
                       page="198об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
