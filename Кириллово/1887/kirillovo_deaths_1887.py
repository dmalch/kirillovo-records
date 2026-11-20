from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, NOT_IN_DOCUMENT, PLEURISY
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   HIEREUS, PEASANT_DAUGHTER, PEASANT_SON, SOLDIER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей), и импортные записи.
# ГАПО 182-5-305, альбом Photos «1887 (ГАПО 182-5-305)» (pk 1333), ч. 3 — лл. 400об–416об (первая запись — смерть
# 30.12.1886, погребение 1.01.1887), прочитана 24.10.2026. Вся запись — на левой странице, причина — на правой. Погребал
# свящ. Александр Васильев Писарев. Записей м. №47–52 и ж. №37–39 (конец октября – ноябрь) в наборе нет — кадр
# «л.415об.-416» начинается с № 53/40; последние записи декабря (после м. №57) тоже не сняты: л. 417 — подшитое отношение
# Спасского окружного суда (24.09.1887, № 725). 11 и 20 июня погребены близнецы Акилина и Феврония, дочери Ивана
# Ермолаевича Дремкова (рожд. ж. №30–31; ж. №22, №24) — не выписаны.
kirillovo_deaths_1887 = death_records(
    "ГАПО",
    "182",
    "5",
    "305",
    "Кириллово",
    "Казанская церковь",
    1887,
    *death_month(Month.JANUARY,
                 # импорт; сверено по скану 24.10.2026 (л. 401об): Павел, р. 19.12.1886 (рожд. 1886 м. №62)
                 death(6, Gender.MALE, 7, 9,
                       deceased=person("Павел", status=PEASANT_SON), age="3 нед",
                       relatives=[relative(person("Василий", "Константинов", last_name_orig="Мальчиков"), Relationship.FATHER)],
                       cause_of_death=PLEURISY,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="401об"),
                 # импорт; сверено по скану 24.10.2026 (л. 402об)
                 death(5, Gender.FEMALE, 11, 13,
                       deceased=person("Пелагея", status=PEASANT_DAUGHTER), age="4 мес",
                       relatives=[relative(person("Иван", "Николаев", last_name_orig="Мальчиков"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="402об"),
                 ),
    *death_month(Month.FEBRUARY,
                 # Агафия, дочь Николая Константиновича Мальчикова («Малахаевъ»), р. 3.02.1887 (рожд. ж. №12)
                 death(10, Gender.FEMALE, 17, 19,
                       deceased=person("Агаѳія", status=PEASANT_DAUGHTER), age="2 нед",
                       relatives=[relative(person("Николай", "Константиновъ", "Малахаевъ", comment="он же: Николай Константинович Мальчиков"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="возраст у дыры листа",
                       page="403об",
                       reviewed=False),
                 ),
    *death_month(Month.MARCH,
                 # Иоанн, сын Егора Михайловича Янина («Сырцевъ»), р. 22.02.1887 (рожд. м. №15)
                 death(11, Gender.MALE, 2, 4,
                       deceased=person("Іоаннъ", status=PEASANT_SON),
                       relatives=[relative(person("Егоръ", "Михайловъ", "Сырцевъ", comment="он же: Егор Михайлович Янин"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="возраст в дыре листа",
                       page="404об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Анна, дочь Степана Сергеевича Ладыгина, р. 22.07.1887 (рожд. ж. №39)
                 death(33, Gender.FEMALE, 26, 27,
                       deceased=person("Анна", status=PEASANT_DAUGHTER), age="1 мес",
                       relatives=[relative(person("Стефанъ", "Сергѣевъ", "Ладыгинъ", status=SOLDIER, comment="«уволенный въ запасъ арміи рядовой»"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="412об",
                       reviewed=False),
                 ),
    *death_month(Month.NOVEMBER,
                 # Евдоким, сын Егора Аникеевича Зосимова и Марии Михайловны (Яниной?), р. 26.07.1887 (рожд. м. №43)
                 death(55, Gender.MALE, 24, 26,
                       deceased=person("Евдокимъ", status=PEASANT_SON), age="4 мес",
                       relatives=[relative(person("Егоръ", "Аникѣевъ", "Зосимовъ", status=SOLDIER, comment="«уволенный по болѣзни рядовой»"), Relationship.FATHER)],
                       cause_of_death=NOT_IN_DOCUMENT,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="правая страница (причина) закрыта подшитым л. 417",
                       page="416об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
