from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLD, COLIC, DIARRHEA, FEVER, OLD_AGE, WEAKNESS
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   HIEREUS, MAIDEN, PEASANT_DAUGHTER, PEASANT_SON, PEASANT_WIFE,
                                   UNTER_OFFICER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей), и импортные записи.
# ГАПО 182-5-305, альбом Photos «1889 (ГАПО 182-5-305)» (pk 1268), ч. 3 — лл. 244об–266, 60 муж. / 57 жен. (ведомость на
# л. 267об), прочитана целиком 24.10.2026. Вся запись — на левой странице, причина — на правой; номера у левого края
# первых листов оборваны. Погребал свящ. Александр Васильев Писарев. Кадр «л.250» — тот же л. 249об с подклеенной справкой
# земского врача (о смерти Михаила Семеновича Куранова, м. №19); кадр «л.255об.» — повторный снимок л. 255об. 10.12.1889
# погребён Григорий Тимофеевич Разоренов, 68 (м. №57) — муж Ирины Нестеровны Мальчиковой, умершей 23.11; 5.11 — Косьма,
# сын Ивана Спиридоновича Бочкова (м. №51; рожд. м. №68 — восприемник Василий Семенович Мальчиков) — не выписаны.
kirillovo_deaths_1889 = death_records(
    "ГАПО",
    "182",
    "5",
    "305",
    "Кириллово",
    "Казанская церковь",
    1889,
    *death_month(Month.MARCH,
                 # Дарья, дочь Ивана Васильевича Харитонова, р. 4.03.1889 (рожд. ж. №11 — восприемник Дмитрий Андреевич
                 # «Малахаевъ»)
                 death(4, Gender.FEMALE, 25, 26,
                       deceased=person("Дарія", status=PEASANT_DAUGHTER), age="3 нед",
                       relatives=[relative(person("Иванъ", None, "Харитоновъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="247об",
                       reviewed=False),
                 ),
    *death_month(Month.APRIL,
                 # Александра, дочь Захара Ивановича Пякина, р. 17.04.1889 (рожд. ж. №18 — восприемница Дарья Сергеевна
                 # Ладыгина)
                 death(8, Gender.FEMALE, 22, 24,
                       deceased=person("Александра", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Захаръ", None, "Пякинъ"), Relationship.FATHER)],
                       cause_of_death=WEAKNESS,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="возраст ушёл в корешок",
                       page="248об",
                       reviewed=False),
                 ),
    *death_month(Month.MAY,
                 # импорт; сверено по скану 24.10.2026 (л. 249об): отчество отца в записи не названо; Александра,
                 # р. 23.04.1889 (рожд. ж. №19)
                 death(9, Gender.FEMALE, 5, 6,
                       deceased=person("Александра", status=PEASANT_DAUGHTER), age="2 нед",
                       relatives=[relative(person("Михаил", "Петров", last_name_orig="Мальчиков"), Relationship.FATHER)],
                       cause_of_death=WEAKNESS,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="причина — на л. 250 (кадр с подклеенной справкой)",
                       page="249об"),
                 ),
    *death_month(Month.JUNE,
                 # импорт; сверено по скану 24.10.2026 (л. 250об): отчество отца в записи не названо
                 death(21, Gender.MALE, 2, 4,
                       deceased=person("Николай", status=PEASANT_SON), age=22,
                       relatives=[relative(person("Степан", last_name_orig="Мальчиков"), Relationship.FATHER)],
                       cause_of_death=COLD,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="Отчество отца в МК не указано",
                       page="250об"),
                 # импорт; сверено по скану 24.10.2026 (л. 253об): «дочь Ѳеодора Янина», 3 года
                 death(22, Gender.FEMALE, 28, 29,
                       deceased=person("Стефанида", "Федорова", last_name_orig="Янина", status=PEASANT_DAUGHTER), age=3,
                       relatives=[relative(person("Федор", last_name_orig="Янин"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="253об"),
                 ),
    *death_month(Month.AUGUST,
                 # импорт; сверено по скану 24.10.2026 (л. 255об): Екатерина, р. 15.11.1888 (рожд. 1888 ж. №69) — ей
                 # 8½ мес., в записи «1»
                 death(27, Gender.FEMALE, 6, 7,
                       deceased=person("Екатерина", "Федорова", last_name_orig="Янина", status=PEASANT_DAUGHTER), age=1,
                       relatives=[relative(person("Федор", last_name_orig="Янин"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="возраст «1» — так в подлиннике; по рождению 15.11.1888 ей 8½ мес.",
                       page="255об"),
                 # Симеон, сын Якова Логиновича Строева и Анны Николаевны Мальчиковой, р. 1.02.1889 (рожд. м. №11)
                 death(42, Gender.MALE, 26, 27,
                       deceased=person("Симеонъ", status=PEASANT_SON), age="6 мес",
                       relatives=[relative(person("Яковъ", None, "Строевъ", status=UNTER_OFFICER, comment="«запасный унтеръ-офицеръ»"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       comment="возраст в подлиннике «½»",
                       page="258об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Надежда, дочь Матвея Егоровича Янина («Сырцевъ»), р. 1871
                 death(44, Gender.FEMALE, 27, 29,
                       deceased=person("Надежда", None, "Сырцева", status=MAIDEN), age=18,
                       relatives=[relative(person("Матвѣй", None, "Сырцевъ", comment="он же: Матвей Егорович Янин?"), Relationship.FATHER)],
                       cause_of_death=FEVER,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="261об",
                       reviewed=False),
                 ),
    *death_month(Month.NOVEMBER,
                 # Ирина Нестеровна Мальчикова, жена Григория Тимофеевича Разоренова (брак 1844); муж умер 10.12.1889
                 death(56, Gender.FEMALE, 23, 25,
                       deceased=person("Ирина", "Нестерова", "Разоренова", status=PEASANT_WIFE, comment="она же: Ирина Нестеровна Мальчикова"),
                       age=70,
                       cause_of_death=OLD_AGE,
                       priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                       page="263об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
