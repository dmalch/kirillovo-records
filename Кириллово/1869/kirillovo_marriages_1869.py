from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          page, person)
from verso.ru.dsl.statuses import (DEACON, ECON_PEASANT_FEMALE, ECON_PEASANT_MAIDEN,
                                   ECON_PEASANT_MALE, HIEREUS, WIDOW)

# SELECTIVE EXTRACT: Only Мальчиков-family related entries from 1869 metric book.
# Archive reference unknown for this period; using placeholder.
# No page numbers available in source extract.
# No clergy names recorded in source extract.
# Record 12: Герасим Яковлев Мальчиков is the groom.
# Witnesses 1 and 3 have uncertain surnames (Шавельгин?, Вавалкин?).

kirillovo_marriages_1869 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "711",
    "Кириллово",
    "Казанская церковь",
    1869,
    *marriage_month(
        Month.FEBRUARY,
        # сверено по скану 03.10.2026 (л. 109об): совпадает; венчали иерей Василий Ремезов и диакон Матфей Рождественский
        marriage(
            12,
            7,
            groom=person("Герасим", "Яковлев", last_name_orig="Мальчиков"),
            groom_marriage_num=1,
            bride=person("Дарья", "Савельева", last_name_orig="Кашелева"),
            bride_marriage_num=1,
            witness1=person("Федор", "Иванов", last_name_orig="Шавельгин", comment="Фамилия неточна: «Шавельгин?»"),
            witness2=person("Ефим", "Спиридонов"),
            witness3=person("Яков", last_name_orig="Вавалкин", comment="Отчество не указано; фамилия неточна: «Вавалкин?»"),
            witness4=person("Антон", "Афанасьев", last_name_orig="Егоров"),
            groom_age=18,
            bride_age=20,
        ),
    ),
    # Дописано при сплошном проходе (03.10.2026) по скану (альбом «1869 (ГАПО 182-5-711)», pk 1284; лист в comment) —
    # записи первой волны, которых не было в импорте. Ч. 2 — лл. 106об–117об (40 браков), прочитана целиком; импортный
    # №12 сверен (л. 109об) и совпал.
    *page("?",
          *marriage_month(Month.JANUARY,
                          # поручитель по невесте — Константин Яковлевич Поздняков (= Мальчиков)
                          marriage(2, 12,
                                   groom=person("Аѳанасій", "Стефановъ", "Сычевъ", comment="фамилия читается неуверенно"),
                                   groom_marriage_num=1, groom_age=22,
                                   bride=person("Гликерія", "Ермолаева"), bride_marriage_num=1, bride_age=18,
                                   witness1=person("Михаилъ", "Нестеровъ", "Дорошкинъ", side=Side.GROOM),
                                   witness2=person("Никифоръ", "Ивановъ", "Пузыревъ", side=Side.GROOM, comment="читается неуверенно"),
                                   witness3=person("Тимоѳей", "Семеновъ", "Каворкинъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                                   witness4=person("Константинъ", "Яковлевъ", "Поздняковъ", side=Side.BRIDE, comment="= Константин Яковлевич Мальчиков (1859)"),
                                   priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                                   deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                                   comment="л. 106об",
                                   reviewed=False),
                          # невеста «Марѳа Андреева Мальчихова» — Мальчикова? (дочь Андрея Григорьевича?) не установлено
                          marriage(3, 12,
                                   groom=person("Аѳанасій", "Ивановъ", "Мякининъ", comment="фамилия читается неуверенно"),
                                   groom_marriage_num=1, groom_age=19,
                                   bride=person("Марѳа", "Андреева", "Мальчикова", comment="в подлиннике «Мальчихова»"),
                                   bride_marriage_num=1, bride_age=18,
                                   witness1=person("Даніилъ", "Ѳедоровъ", "Бородинъ", side=Side.GROOM),
                                   witness2=person("Александръ", "Борисовъ", "Трафимовъ", side=Side.GROOM, comment="читается неуверенно"),
                                   witness3=person("Василій", "Филипповъ", "Абакумовъ", side=Side.BRIDE),
                                   witness4=person("Никита", "Тимоѳеевъ", "Ѳоминъ", side=Side.BRIDE),
                                   priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                                   comment="л. 106об",
                                   reviewed=False),
                          # поручитель по невесте — Козьма Андреянович Мальчиков
                          marriage(4, 12,
                                   groom=person("Михаилъ", "Семеновъ", comment="фамилия не разобрана («Пр…ановъ»)"), groom_marriage_num=1,
                                   bride=person("Ѳеодосія", "Петрова", "Макушина", comment="фамилия читается неуверенно"),
                                   bride_marriage_num=1, bride_age=19,
                                   witness1=person("Григорій", "Ѳедоровъ", "Погуляевъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                                   witness2=person("Петръ", "Ѳедоровъ", "Дуркинъ", side=Side.GROOM, comment="читается и «Дыркинъ»"),
                                   witness3=person("Козьма", "Андреяновъ", "Мальчиковъ", side=Side.BRIDE, comment="в подлиннике «Казьма»"),
                                   witness4=person("Иванъ", "Матвѣевъ", "Бурлинъ", side=Side.BRIDE),
                                   priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                                   comment="л. 106об; возраст жениха не разобран",
                                   reviewed=False),
                          ),
          *marriage_month(Month.FEBRUARY,
                          # Прокофий Иванович Мальчиков
                          marriage(15, 12,
                                   groom=person("Прокофій", "Ивановъ", "Мальчиковъ"), groom_marriage_num=1, groom_age=20,
                                   bride=person("Анисія", "Тимоѳеева", "Абаева"), bride_marriage_num=1, bride_age=18,
                                   witness1=person("Яковъ", "Васильевъ", "Паршинъ", side=Side.GROOM),
                                   witness2=person("Леонтій", "Никитинъ", side=Side.GROOM),
                                   witness3=person("Стефанъ", "Ивановъ", "Петровъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                                   witness4=person("Иванъ", "Андреевъ", "Смирновъ", side=Side.BRIDE),
                                   priest=person("Андрей", last_name_orig="Тихомировъ", status=HIEREUS),
                                   deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                                   comment="л. 110об",
                                   reviewed=False),
                          ),
          *marriage_month(Month.JUNE,
                          # поручитель по жениху — Семен Емельянович Мальчиков
                          marriage(24, None,
                                   groom=person("Гавріилъ", "Ивановъ", "Спиряевъ"), groom_marriage_num=1, groom_age=18,
                                   bride=person("Христина", "Никифорова", "Рябова", residence="Чернышево", comment="фамилия читается неуверенно"),
                                   bride_marriage_num=1, bride_age=17,
                                   witness1=person("Димитрій", "Ивановъ", "Спиряевъ", side=Side.GROOM),
                                   witness2=person("Семенъ", "Емельяновъ", "Мальчиковъ", side=Side.GROOM, comment="в подлиннике «Амельяновъ»"),
                                   witness3=person("Тимоѳей", "Стефановъ", side=Side.BRIDE, comment="фамилия не разобрана"),
                                   witness4=person("Василій", "Стефановъ", "Канюковъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                                   priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                                   comment="л. 112об; день венчания не написан",
                                   reviewed=False),
                          ),
          *marriage_month(Month.OCTOBER,
                          # жених — «Стефанъ Амельяновъ Бурлинъ», вторым браком: тот ли Стефан Емельянович, что «Мальчиковъ»
                          # в рожд. 1869 м. №25 (жена Марфа Андреевна)? Поручители — Козьма Андреянович и Матвей Козьмич
                          # Мальчиковы. В 1879 (рожд. м. №101) жена Степана Емельяновича Мальчикова — Параскева Ивановна:
                          # по-видимому, он и есть
                          marriage(26, 15,
                                   groom=person("Стефанъ", "Емельяновъ", "Бурлинъ", comment="в подлиннике «Амельяновъ»"),
                                   groom_marriage_num=2, groom_age=25,
                                   bride=person("Параскева", "Иванова", "Куранова", status=WIDOW), bride_marriage_num=2, bride_age=27,
                                   witness1=person("Яковъ", "Ивановъ", side=Side.GROOM, comment="фамилия не разобрана («Б…»)"),
                                   witness2=person("Козьма", "Андреяновъ", "Мальчиковъ", side=Side.GROOM, comment="в подлиннике «Казьма»"),
                                   witness3=person("Иванъ", "Ивановъ", "Бурлинъ", side=Side.BRIDE),
                                   witness4=person("Матѳей", "Козьминъ", "Мальчиковъ", side=Side.BRIDE, comment="в подлиннике «Казьминъ»"),
                                   priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                                   deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                                   comment="л. 113об; возраст невесты читается неуверенно",
                                   reviewed=False),
                          # Петр Акимович Мальчиков — вдовец Марии Агаповны (ум. 12.10.1868); невеста почти не читается. В 1879
                          # (рожд. м. №63) его жена — Христина Акимова: вероятно, она
                          marriage(28, 27,
                                   groom=person("Петръ", "Акимовъ", "Мальчиковъ"), groom_marriage_num=2, groom_age=39,
                                   bride=person("?", "Акимова", status=WIDOW, comment="«…Якимова Ше…нина», «… уѣзда деревни Кругл…» — не разобрано"),
                                   bride_marriage_num=2, bride_age=28,
                                   witness1=person("Ермолай", "Аѳанасьевъ", side=Side.GROOM, comment="фамилия не разобрана; = Ермолай Афанасьевич Егоров (Тавостин)?"),
                                   witness3=person("Матѳей", "Аѳанасьевъ", "Егоровъ", side=Side.BRIDE),
                                   witness4=person("?", "Лазаревъ", "Червяковъ", side=Side.BRIDE, comment="имя не разобрано"),
                                   priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                                   deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                                   comment="л. 113об",
                                   reviewed=False),
                          ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE, status_bride=ECON_PEASANT_MAIDEN),
)
