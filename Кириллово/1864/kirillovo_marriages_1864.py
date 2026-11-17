from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          page, person)
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE,
                                   HIEREUS, WIDOW)

# SELECTIVE EXTRACT: Only Мальчиков-family related entries from 1864 metric book.
# Archive reference unknown for this period; using placeholder.
# No page numbers available in source extract.
# No clergy names recorded in source extract.
# Record 1 (January): no record number in source — assigned None.

kirillovo_marriages_1864 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "710",
    "Кириллово",
    "Казанская церковь",
    1864,
    *marriage_month(
        Month.JANUARY,
        marriage(
            None,
            10,
            groom=person("Степан", "Емельянов", last_name_orig="Мальчиков"),
            groom_marriage_num=1,
            bride=person("Марфа", "Андреева", last_name_orig="Бурлина"),
            bride_marriage_num=1,
            witness1=person("Андриан", "Григорьев", last_name_orig="Мальчиков", comment="В источнике отчество: «Григорьевич»"),
            witness2=person("Семеон", "Емельянов", last_name_orig="Мальчиков"),
            witness3=person("Петр", "Матвеев", last_name_orig="Банников"),
            witness4=person("Григорий", "Прокопьев", last_name_orig="Жигулев"),
            groom_age=20,
            bride_age=19,
            comment="Номер записи не указан в источнике",
        ),
    ),
    *marriage_month(
        Month.FEBRUARY,
        # ⚠ Сверено по скану 12.10.2026 (альбом «1864 (ЦГАРМ 57-6-477)», pk 1344, кадр 43): жених — «Яковъ Степановъ
        # Мешечковъ», НЕ Мальчиков (в 1880 та же пара — «Яковъ Стефановъ Мешечковъ» и Евдокія Петрова, рожд. м. №3);
        # фамилия невесты — «Ман…чакова» (перенос, неуверенно), поручители — Онтиковы. Импортное чтение не исправлено:
        # жених опубликован на familio как родня (familio_kin.py) — снять его оттуда решает владелец
        marriage(
            20,
            12,
            groom=person("Яков", "Степанов", last_name_orig="Мальчиков"),
            groom_marriage_num=1,
            bride=person("Евдокия", "Петрова", last_name_orig="Мальчикова", comment="В скобках указано «Оньтикова?»"),
            bride_marriage_num=1,
            witness1=person("Аврам", "Петров", last_name_orig="Оньтиков"),
            witness2=person("Федор", "Петров", last_name_orig="Оньтиков"),
            witness3=person("Никита", "Федоров", last_name_orig="Оньтиков"),
            witness4=person("Илья", "Нестеров", last_name_orig="Щетинин", comment="Фамилия неточна: «Щетинин?»"),
            groom_age=19,
            bride_age=16,
        ),
    ),
    # Дописано при сплошном проходе (03.10.2026) по скану (альбом «1864 (ЦГАРМ 57-6-477)», pk 1344) — браки первой
    # волны, которых не было в импорте. Брак Степана Емельяновича (10 янв) — кадр 40, номера на листе не проставлены.
    *page("?",
          *marriage_month(Month.FEBRUARY,
                          # поручитель по невесте — Семен Емельянович Мальчиков
                          marriage(21, 12,
                                   groom=person("Петръ", "Яковлевъ", "Кодряковъ", comment="фамилия читается неуверенно"),
                                   groom_marriage_num=1, groom_age=18,
                                   bride=person("Екатерина", "Васильева", "Шаркова"), bride_marriage_num=1, bride_age=17,
                                   witness1=person("Лаврентій", "Артемовъ", "Бѣловъ", side=Side.GROOM),
                                   witness2=person("Михаилъ", "Нестеровъ", "Дорошкинъ", side=Side.GROOM),
                                   witness3=person("Семенъ", "Емельяновъ", "Мальчиковъ", side=Side.BRIDE),
                                   witness4=person("Степанъ", "Митрофановъ", "Верховъ", side=Side.BRIDE),
                                   priest=person("Василій", "Іоакимовъ", "Бѣльскій", status=HIEREUS),
                                   comment="кадр 43 альбома",
                                   reviewed=False),
                          # поручитель по невесте — Илья Павлович Мальчиков
                          marriage(23, 14,
                                   groom=person("Семенъ", "Васильевъ", "Козельковъ", comment="фамилия читается неуверенно"),
                                   groom_marriage_num=1, groom_age=19,
                                   bride=person("Марѳа", "Михайлова", "Сапронова"), bride_marriage_num=1, bride_age=18,
                                   witness1=person("Ѳедотъ", "Захаровъ", "Поручиковъ", side=Side.GROOM),
                                   witness2=person("Яковъ", "Карповъ", "Кабельковъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                                   witness3=person("Илья", "Павловъ", "Мальчиковъ", side=Side.BRIDE),
                                   witness4=person("Архипъ", "Ефимовъ", "Сапроновъ", side=Side.BRIDE),
                                   priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                                   comment="кадр 45 альбома",
                                   reviewed=False),
                          # поручитель по невесте — Родион Яковлевич Янин из Гоголева Бора
                          marriage(31, 21,
                                   groom=person("Василій", "Степановъ", residence="Гоголев Бор", comment="фамилии в записи нет"),
                                   groom_marriage_num=2, groom_age=40,
                                   bride=person("Домна", "Тарасова", status=WIDOW, residence="Красная Дубрава"),
                                   bride_marriage_num=2, bride_age=31,
                                   witness1=person("Андріанъ", "Наумовъ", "Романовъ", side=Side.GROOM, residence="Гоголев Бор"),
                                   witness2=person("Данила", "Лазаревъ", "Глушицынъ", side=Side.GROOM, residence="Гоголев Бор"),
                                   witness3=person("Аѳанасій", side=Side.BRIDE, residence="Гоголев Бор", comment="отчество и фамилия не разобраны («Юматовъ Р…»)"),
                                   witness4=person("Родіонъ", "Яковлевъ", "Янинъ", side=Side.BRIDE, residence="Гоголев Бор"),
                                   priest=person("Андрей", last_name_orig="Глазуновъ", status=HIEREUS),
                                   comment="кадр 46 альбома",
                                   reviewed=False),
                          ),
          *marriage_month(Month.OCTOBER,
                          # поручитель по жениху — Семен Емельянович Мальчиков
                          marriage(46, 27,
                                   groom=person("Димитрій", "Ивановъ", "Спиряевъ"), groom_marriage_num=1, groom_age=19,
                                   bride=person("Акилина", "Иванова", status=WIDOW, comment="«Пензенской губ. … села …» — место не разобрано"),
                                   bride_marriage_num=2, bride_age=23,
                                   witness1=person("Семенъ", "Емельяновъ", "Мальчиковъ", side=Side.GROOM),
                                   witness2=person("Николай", "Алексѣевъ", side=Side.GROOM, comment="фамилия не разобрана («Ав…кушевъ»)"),
                                   witness3=person("Иванъ", side=Side.BRIDE, comment="отчество и фамилия не разобраны"),
                                   witness4=person("Андрей", "Ефремовъ", "Спиряевъ", side=Side.BRIDE),
                                   priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                                   comment="кадр 49 альбома",
                                   reviewed=False),
                          ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE, status_bride=ECON_PEASANT_MAIDEN),
)
