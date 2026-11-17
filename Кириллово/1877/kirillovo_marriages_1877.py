from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (DEACON, GOSUDARSTVENNYJ_PEASANT_FEMALE,
                                   GOSUDARSTVENNYJ_PEASANT_MALE, HIEREUS)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. ГАПО 182-5-734, альбом Photos
# «1877 (ГАПО 182-5-734)» (pk 1352), ч. 2 — лл. 1об–8, 29 браков (январь 10, апрель 3, ноябрь 16); прочитана целиком
# 05.10.2026. Книга пишет «государственный крестьянинъ». Венчал настоятель, священник Василий Иоаннов Ремезов, с
# псаломщиком диаконом Матфеем Рождественским и и.д. псаломщиков Николаем Трофимовым Леонтовым и Герасимом
# Григорьевым Богословским. Не взят: № 27 (11 нояб.) — невеста Екатерина Семеновна Карасева, 18 л. (дочь Семена
# Степановича Карасева и Екатерины Васильевны Мальчиковой? её рождения в DSL нет).
kirillovo_marriages_1877 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "734",
    "Кириллово",
    "Казанская церковь",
    1877,
    *marriage_month(Month.APRIL,
                    # невеста — Ксения Андреевна Мальчикова (восприемница 1875); жених — сын Игната Ивановича Ладыгина
                    # и Пелагии Несторовны Мальчиковой (брак 1854)?
                    marriage(11, 6,
                             groom=person("Иванъ", "Игнатовъ", "Ладыгинъ"), groom_marriage_num=1, groom_age=18,
                             bride=person("Ксенія", "Андреева", "Мальчикова", comment="в подлиннике «Мальчкова»"),
                             bride_marriage_num=1, bride_age=18,
                             witness1=person("Александръ", "Трофимовъ", "Берновъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Герасимъ", "Александровъ", "Кадлевъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness3=person("Сергѣй", "Дементьевъ", "Сырковъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             witness4=person("Михаилъ", None, "Парамоновъ", side=Side.BRIDE, comment="отчества нет, фамилия читается неуверенно («Пары…новъ»)"),
                             priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                             deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                             page="2об",
                             reviewed=False),
                    # поручитель по невесте — Семен Наумович Янин
                    marriage(12, 17,
                             groom=person("Василій", "Антоновъ", "Булановъ"), groom_marriage_num=1, groom_age=18,
                             bride=person("Параскева", "Васильева", "Чибочкина"), bride_marriage_num=1, bride_age=18,
                             witness1=person("Стефанъ", "Кирсановъ", "Сеякинъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Никифоръ", "Никитинъ", "Голубевъ", side=Side.GROOM),
                             witness3=person("Стефанъ", "Ивановъ", "Чирковъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             witness4=person("Семенъ", "Наумовъ", "Янинъ", side=Side.BRIDE),
                             priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                             deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                             page="3об",
                             reviewed=False),
                    ),
    *marriage_month(Month.NOVEMBER,
                    # невеста «Варвара Егорова Малахова» — Варвара, дочь Егора Константиновича Мальчикова («Малахѣева»),
                    # р. 1.12.1859; поручитель по невесте — Климент Антонович Мальчиков
                    marriage(21, 6,
                             groom=person("Петръ", "Христофоровъ", "Богачевъ", comment="«присоединенный къ Православной церкви изъ раскола старообрядческаго»"),
                             groom_marriage_num=1, groom_age=20,
                             bride=person("Варвара", "Егорова", "Малахова", comment="= Варвара Егоровна Мальчикова (р. 1859)?"),
                             bride_marriage_num=1, bride_age=19,
                             witness1=person("Яковъ", "Стефановъ", "Мешечковъ", side=Side.GROOM),
                             witness2=person("Антипъ", "Ефимовъ", "Костиковъ", status="военный писарь в бессрочном отпуску", side=Side.GROOM),
                             witness3=person("Андрей", "Кондратьевъ", side=Side.BRIDE, comment="фамилия не разобрана («К…инъ»)"),
                             witness4=person("Климентъ", "Антоновъ", "Мальчиковъ", side=Side.BRIDE),
                             priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                             deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                             page="5об",
                             reviewed=False),
                    # невеста — Екатерина Сергеевна Ладыгина (р. 26.11.1855), дочь Пелагии Семеновны Мальчиковой; поручители —
                    # Самсон Наумович Янин и её брат «Андрей Сергѣевъ Дементьевъ» (= Андрей Сергеевич Ладыгин)
                    marriage(22, 6,
                             groom=person("Захаръ", "Ивановъ", "Пякинъ", comment="фамилия читается неуверенно"),
                             groom_marriage_num=1, groom_age=18,
                             bride=person("Екатерина", "Сергѣева", "Ладыгина"), bride_marriage_num=1, bride_age=22,
                             witness1=person("Никифоръ", "Никитинъ", "Голубевъ", side=Side.GROOM),
                             witness2=person("Самсонъ", "Наумовъ", "Янинъ", side=Side.GROOM),
                             witness3=person("Герасимъ", "Александровъ", "Кадлевъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             witness4=person("Андрей", "Сергѣевъ", "Дементьевъ", side=Side.BRIDE, comment="«Дементьевъ» — по деду; = Андрей Сергеевич Ладыгин"),
                             priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                             deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                             page="5об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
