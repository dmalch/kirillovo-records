from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import HIEREUS, PEASANT_FEMALE, PEASANT_MALE, SOLDIER

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-305, альбом
# Photos «1890 (ГАПО 182-5-305)» (pk 1324), ч. 2 — лл. 167об–176об, 28 браков (январь 8, апрель 1, май 2, июнь 2,
# октябрь 3, ноябрь 12); л. 167 — шмуцтитул; прочитана целиком 25.10.2026; импорта не было. Жених и невеста — на левой
# странице, поручители — на правой. Венчал свящ. Александр Васильев Писарев. Брак №23 (Иван Матвеевич Никин) — невеста
# «Ксенія Михайлова Маликова», не Мальчикова.
kirillovo_marriages_1890 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "305",
    "Кириллово",
    "Казанская церковь",
    1890,
    *marriage_month(Month.NOVEMBER,
                    # Максим Михайлович Янин («Сырцевъ»), сын Михаила Андреяновича; поручитель по жениху — Василий Семенович
                    # Мальчиков
                    marriage(17, 4,
                             groom=person("Максимъ", "Михайловъ", "Сырцевъ", status=SOLDIER, comment="«запасный рядовой»; он же: Максим Михайлович Янин"),
                             groom_marriage_num=1, groom_age=24,
                             bride=person("Стефанида", "Ильина", "Баенкова", comment="«Керенскаго уѣзда села Татарской Лаки солдатская дочь»; фамилия читается неуверенно"),
                             bride_marriage_num=1, bride_age=21,
                             witness1=person("Егоръ", "Аникѣевъ", "Зосимовъ", status=SOLDIER, side=Side.GROOM),
                             witness2=person("Василій", "Семеновъ", "Мальчиковъ", status=SOLDIER, side=Side.GROOM),
                             witness3=person("Аѳанасій", "Степановъ", "Сычевъ", side=Side.BRIDE),
                             witness4=person("Егоръ", "Ермолаевъ", "Даньковъ", side=Side.BRIDE, comment="«Татарской Лаки крестьянинъ»; фамилия читается неуверенно"),
                             priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                             page="172об",
                             reviewed=False),
                    # поручитель по жениху — Прокопий Андреевич Мальчиков («Юлинъ»)
                    marriage(26, 11,
                             groom=person("Іоаннъ", "Максимовъ", "Дунаевъ"),
                             groom_marriage_num=1, groom_age=18,
                             bride=person("Марія", "Іоаннова", "Ларина", comment="«рядоваго дочь»"),
                             bride_marriage_num=1, bride_age=18,
                             witness1=person("Прокопій", "Андреевъ", "Юлинъ", side=Side.GROOM, comment="он же: Прокопий Андреевич Мальчиков"),
                             witness2=person("Ермолай", "Степановъ", "Сапроновъ", status=SOLDIER, side=Side.GROOM, comment="«запасный ефрейторъ»"),
                             witness3=person("Иванъ", "Ивановъ", "Ларинъ", side=Side.BRIDE),
                             witness4=person("Яковъ", "Егоровъ", "Ларинъ", side=Side.BRIDE),
                             priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                             page="175об",
                             reviewed=False),
                    # Андрей Николаевич «Малахаевъ» — сын Николая Константиновича Мальчикова («Малахаева»)? не установлено;
                    # поручитель по жениху — Иван Козьмич? Мальчиков
                    marriage(27, 11,
                             groom=person("Андрей", "Николаевъ", "Малахаевъ"),
                             groom_marriage_num=1, groom_age=20,
                             bride=person("Екатерина", "Андреева", "Бубенчикова"),
                             bride_marriage_num=1, bride_age=22,
                             witness1=person("Иванъ", "Козминъ", "Мальчиковъ", side=Side.GROOM, comment="отчество читается неуверенно"),
                             witness2=person("Петръ", "Исаевъ", "Зенкинъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness3=person("Петръ", "Степановъ", "Бочковъ", status=SOLDIER, side=Side.BRIDE, comment="«запасный рядовой»"),
                             witness4=person("Петръ", "Егоровъ", "Лапонкинъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                             page="175об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
