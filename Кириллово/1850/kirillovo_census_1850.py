from verso.ru.dsl import (CensusRole, Month, RecordDefaults, census_records, household, member,
                          page, person)
from verso.ru.dsl.statuses import STATE_PEASANT_FEMALE, STATE_PEASANT_MALE

# РС 9 (Девятая ревизия) 1850 года, с. Кириллово
# Архив: ГАТО, ф. 12 оп. 1 д. 1768 —
# «Ревизские сказки с. Кириллово Спасского уезда за 1850 год, ч. 1»
census = census_records(
    "ГАТО",
    "12",
    "1",
    "1768",
    "Кириллово",
    1850,
    # Семья № 234 (= сем. 301 по РС 8 1834), л. 109 — Трифоновы
    # Тимофей Трифонов умер в 1840, его сын Тимофей — в 1849; из мужчин остался
    # только внук Денис Петров с двумя сыновьями.
    # Пётр Тимофеев в сказке не значится: отдан в рекруты в 1833 (РС 8 1834,
    # семья 301) и тем выбыл из подушного оклада. Восстановлен скрытым членом,
    # иначе Денис остаётся без отца (CPL002).
    # Аксинья Платонова и её дочь Аксинья — те же, что в РС 8 1834 (25 лет и
    # 9 месяцев); возраст вдовы в сказке занижен на шесть лет.
    *page("109",
    household("234",
              member(1, person("Тимофей", "Трифоновъ"), CensusRole.HEAD,
                     previous_age=59, departure_year=1840, departure_reason="умер"),
              member(2, person("Тимофей"), CensusRole.SON, previous_age=21, departure_year=1849, departure_reason="умер"),
              member(3, person("Денисъ", "Петровъ"), CensusRole.GRANDSON, ref_member=1, parent_member=6, age=23, previous_age=7,
                     comment="в документе «Тимофея Трифонова внукъ»"),
              member(4, person("Леонтій"), CensusRole.SON, ref_member=3, age=4),
              member(5, person("Гаврил"), CensusRole.SON, ref_member=3, age=2),
              member(6, person("Петр"), CensusRole.SON, hidden=True,
                     comment="отдан в рекруты в 1833 (РС 8 1834, семья 301); в РС 9 не значится — восстановлен как отец Дениса"),
              member(7, person("Марфа", "Платонова"), CensusRole.WIFE, ref_member=2, age=35),
              member(8, person("Аксинья"), CensusRole.DAUGHTER, ref_member=2, age="16.5"),
              member(9, person("Авдотья"), CensusRole.DAUGHTER, ref_member=2, age=2),
              member(10, person("Пелагея", "Иванова"), CensusRole.WIFE, ref_member=3, age=23)),
            ),
    # Семья № 411 (= сем. 523 по РС 8 1834) — Мальчиковы (Дмитрий Давыдов)
    # Дмитрий Давыдов умер в 1846; Нестер умер в 1843; Василий исключён в Саратов в 1847.
    # Из живых остались вдова Нестера Василиса и её дочери.
    *page("181",
    household("411",
              member(1, person("Дмитрій", "Давыдовъ", "Мальчиковъ"), CensusRole.HEAD,
                     previous_age=61, departure_year=1846, departure_reason="умер"),
              member(2, person("Нестеръ"), CensusRole.SON, previous_age=35, departure_year=1843, departure_reason="умер"),
              member(3, person("Василій"), CensusRole.SON, previous_age=32, departure_year=1847, departure_reason="исключён в Саратовскую губернию"),
              member(4, person("Григорій"), CensusRole.SON, ref_member=3, previous_age=10, departure_year=1847, departure_reason="исключён в Саратовскую губернию"),
              member(5, person("Василиса", "Савельева"), CensusRole.WIFE, ref_member=2, age=59),
              member(6, person("Татьяна"), CensusRole.DAUGHTER, ref_member=2, age=17),
              member(7, person("Пелагея"), CensusRole.DAUGHTER, ref_member=2, age=13)),
    # Семья № 412 (= сем. 524 по РС 8 1834) — Мальчиковы (Павел Давыдов)
    # Павел умер в 1840; Михаил умер в 1841; Федор умер в 1849.
    # Дети Федора (Петр и Дарья) остались в хозяйстве; они племянники Ильи.
    household("412",
              member(1, person("Павелъ", "Давыдовъ", "Мальчиковъ"), CensusRole.HEAD,
                     previous_age=59, departure_year=1840, departure_reason="умер"),
              member(2, person("Михайла"), CensusRole.SON, previous_age=34, departure_year=1841, departure_reason="умер"),
              member(3, person("Федоръ"), CensusRole.SON, previous_age=21, departure_year=1849, departure_reason="умер"),
              member(4, person("Петръ"), CensusRole.SON, ref_member=3, age=13),
              member(5, person("Илья"), CensusRole.SON, age=29, previous_age=13),
              member(6, person("Николай"), CensusRole.SON, age=26, previous_age=10),
              member(7, person("Василій"), CensusRole.SON, ref_member=6, age=5, birth_day=9, birth_month=Month.APRIL, birth_year=1845, comment="сын от первой жены"),
              member(8, person("Дарья"), CensusRole.DAUGHTER, ref_member=3, age=8),
              member(9, person("Авдотья", "Платонова"), CensusRole.WIFE, ref_member=5, age=35),
              member(10, person("Агафья", "Иванова", comment="2-я жена Николая Павлова"), CensusRole.WIFE, ref_member=6, age=45)),
    # Семья № 413 (= сем. 525 по РС 8 1834) — Мальчиковы (Иван Федосеев)
    # Иван Федосеев умер в 1834; Иван Иванов умер в 1843.
    # Григорий Иванов (1й сын Ивана Иванова) отдан в рекруты в 1836.
    # Степан и Константин Ивановы отданы в рекруты в 1848.
    # Из живых: Андрей Иванов (глава) + сыновья рекрута Григория.
    household("413",
              member(1, person("Иванъ", "Федосѣевъ", "Мальчиковъ"), CensusRole.HEAD,
                     previous_age=78, departure_year=1834, departure_reason="умер"),
              member(2, person("Андрей"), CensusRole.SON, age=68, previous_age=52),
              member(3, person("Иванъ"), CensusRole.SON, previous_age=38, departure_year=1843, departure_reason="умер"),
              member(4, person("Григорий"), CensusRole.SON, ref_member=3,
                     previous_age=21, departure_year=1836, departure_reason="отдан в рекруты"),
              member(5, person("Андрей"), CensusRole.SON, ref_member=4, age=21, previous_age=5),
              member(6, person("Никита"), CensusRole.SON, ref_member=4, previous_age=3, departure_year=1839, departure_reason="умер"),
              member(7, person("Василій"), CensusRole.SON, ref_member=4, age=14),
              # Сыновья Ивана Иванова (№ 3), не Григория (№ 4): «Степан и Константин Ивановы» выше, в РС
              # 1834 сем. 525 — сыновья Ивана (№ 10–11), а Григорию в 1834 было 21 при 11-летнем Степане.
              # Константину РС 1834 пишет 2 года, эта сказка — 9 по прошлой ревизии; см. previous_age_error.
              member(8, person("Степанъ"), CensusRole.SON, ref_member=3, previous_age=11, departure_year=1848, departure_reason="отдан по найму в рекруты"),
              member(9, person("Костантинъ"), CensusRole.SON, ref_member=3, previous_age=9, departure_year=1848, departure_reason="отдан в рекруты",
                     previous_age_error="прошлый «9» (л. 181об, кадр 182 — так в подлиннике) не сходится с самой РС 1834: сем. 525 № 11, «Ивана Иванова 3й сынъ Костентинъ», новорожденный, 2 года (л. 200, кадр 201) — ошибка переноса; оба чтения сверены по сканам 30.09.2026")),
          ),
    # Семья № 414 (Яков Максимов Позняков / Мальчиков)
    # В РС 8 1834 числился как жилец (LODGER) в сем. 525;
    # к 1850 образовал отдельный двор.
    *page("182",
    household("414",
              member(1, person("Яковъ", "Максимовъ", comment="Позняков / Мальчиков"), CensusRole.HEAD, age=37, previous_age=21),
              member(2, person("Константинъ"), CensusRole.SON, age=17, previous_age=1),
              member(3, person("Матвей"), CensusRole.SON, age=16, birth_day=15, birth_month=Month.SEPTEMBER, birth_year=1834),
              member(4, person("Семенъ"), CensusRole.SON, age=11, birth_day=18, birth_month=Month.MAY, birth_year=1839),
              member(5, person("Герасимъ"), CensusRole.SON, age="7 мес", birth_day=4, birth_month=Month.MARCH, birth_year=1850),
              member(7, person("Елена", "Кирѣева"), CensusRole.WIFE, age=38),
              member(8, person("Татьяна"), CensusRole.DAUGHTER, age=8)),
              ),
    # Семья № 420 (= сем. 532 + 533 + 534 по РС 8 1834) — Мальчиковы (Григорий Иванов)
    # Григорий Иванов умер в 1841; Михаил Андрианов умер в 1837;
    # Аким Григорьев отдан в рекруты в 1837.
    # Его сын Петр Акимов (16 л. 2 мес.) остался в хозяйстве — племянник Емельяна.
    *page("184",
    household("420",
              member(1, person("Григорій", "Ивановъ", "Мальчиковъ"), CensusRole.HEAD,
                     previous_age=55, departure_year=1841, departure_reason="умер"),
              member(2, person("Емельянъ"), CensusRole.SON, age=55, previous_age=39),
              member(3, person("Емельянъ"), CensusRole.SON, ref_member=2, age=29, previous_age=13),
              member(4, person("Степанъ", comment="от 1-й жены"), CensusRole.SON, ref_member=3, age=5, birth_day=2, birth_month=Month.AUGUST, birth_year=1845),
              member(5, person("Дмитрій"), CensusRole.SON, ref_member=2, age=26, previous_age=10),
              member(6, person("Семенъ"), CensusRole.SON, ref_member=2, age=24, previous_age=8),
              member(7, person("Евдокимъ"), CensusRole.SON, ref_member=2, age=17, previous_age=1),
              member(8, person("Андріанъ"), CensusRole.SON, age=48, previous_age=32),
              member(9, person("Казма", comment="1й сын Андриана"), CensusRole.SON, ref_member=8, age=27, previous_age=11),
              member(10, person("Никита"), CensusRole.SON, ref_member=9, age=6, birth_day=5, birth_month=Month.APRIL, birth_year=1844),
              member(11, person("Матвей"), CensusRole.SON, ref_member=9, age="1 мес", birth_day=15, birth_month=Month.AUGUST, birth_year=1850),
              member(12, person("Казма", comment="2й сын Андриана"), CensusRole.SON, ref_member=8, age=25, previous_age=9),
              member(13, person("Михайла", comment="3й сын Андриана"), CensusRole.SON, ref_member=8, previous_age="1.5", departure_year=1837, departure_reason="умер"),
              member(14, person("Акимъ", comment="3й сын Григория"), CensusRole.SON, ref_member=1, previous_age=27, departure_year=1837, departure_reason="отдан в рекруты"),
              member(15, person("Петръ"), CensusRole.SON, ref_member=14, age="16 лет 2 месяца", previous_age="2 месяца"),
              member(16, person("Петръ", comment="4й сын Григория"), CensusRole.SON, ref_member=1, age=39, previous_age=23),
              member(17, person("Михайла"), CensusRole.SON, ref_member=16, age=3, birth_day=30, birth_month=Month.AUGUST, birth_year=1847),
              member(18, person("Аграфена", "Семенова"), CensusRole.WIFE, ref_member=2, age=56),
              member(19, person("Федора", "Иванова", comment="2-я жена Емельяна Емельянова"), CensusRole.WIFE, ref_member=3, age=26),
              member(20, person("Авдотья", comment="дочь от 1-й жены"), CensusRole.DAUGHTER, ref_member=3, age=8),
              member(22, person("Варвара", "Леонтьева"), CensusRole.WIFE, ref_member=5, age=38),
              member(23, person("Елена", comment="дочь Дмитрия Емельянова"), CensusRole.DAUGHTER, ref_member=5, age="6 недель"),
              member(24, person("Акулина", "Семенова"), CensusRole.WIFE, ref_member=6, age=30),
              member(25, person("Варвара", "Яковлева"), CensusRole.WIFE, ref_member=8, age=51),
              member(26, person("Устинья", comment="дочь Андриана"), CensusRole.DAUGHTER, ref_member=8, age=22),
              member(27, person("Федосья", comment="дочь Андриана"), CensusRole.DAUGHTER, ref_member=8, age=19),
              member(28, person("Матрена", comment="дочь Андриана"), CensusRole.DAUGHTER, ref_member=8, age=15),
              member(29, person("Пелагея", "Михайлова", comment="жена 1-го Казьмы Андрианова"), CensusRole.WIFE, ref_member=9, age=30),
              member(30, person("Дарья", comment="дочь Казьмы Андрианова"), CensusRole.DAUGHTER, ref_member=9, age=3),
              member(31, person("Анисья", "Петрова", comment="жена 2-го Казьмы Андрианова"), CensusRole.WIFE, ref_member=12, age=25),
              member(32, person("Прасковья"), CensusRole.DAUGHTER, ref_member=12, age="1"),
              member(33, person("Аксинья", "Васильева"), CensusRole.WIFE, ref_member=16, age=41),
              member(34, person("Февронья", comment="дочь Петра Григорьева"), CensusRole.DAUGHTER, ref_member=16, age=15),
              member(35, person("Елена", comment="дочь Петра Григорьева"), CensusRole.DAUGHTER, ref_member=16, age=13),
              member(36, person("Настасья", comment="дочь Петра Григорьева"), CensusRole.DAUGHTER, ref_member=16, age=9)),
          ),
    # Семья № 431 (= сем. 553 по РС 8 1834) — Мальчиковы (Герасим Федоров)
    # Герасим Федоров умер в 1838.
    # Пелагея и Александра Семеновы — дочери рекрута Семена Герасимова (выбыл 1833);
    # остаются в хозяйстве как племянницы Василия.
    *page("188",
    household("431",
              member(1, person("Герасимъ", "Федоровъ", "Мальчиковъ"), CensusRole.HEAD,
                     previous_age=48, departure_year=1838, departure_reason="умер"),
              member(2, person("Василій"), CensusRole.SON, age=47, previous_age=31),
              member(3, person("Андрѣй", comment="от 1-й жены"), CensusRole.SON, ref_member=2, age=31, previous_age=15),
              member(4, person("Карпъ", comment="от 1-й жены"), CensusRole.SON, ref_member=2, age=20, previous_age=4),
              member(5, person("Іон"), CensusRole.SON, age=35, previous_age=19),
              member(6, person("Марфа", "Акимова", comment="2-я жена Василия Герасимова"), CensusRole.WIFE, ref_member=2, age=46),
              member(7, person("Прасковья", "Ермолаева"), CensusRole.WIFE, ref_member=3, age=30),
              member(8, person("Авдотья"), CensusRole.DAUGHTER, ref_member=3, age=3),
              member(9, person("Марья", comment="от 1-й жены Василия"), CensusRole.DAUGHTER, ref_member=2, age=20),
              member(10, person("Акулина", "Раманова"), CensusRole.WIFE, ref_member=5, age=38),
              member(11, person("Василиса"), CensusRole.DAUGHTER, ref_member=5, age=11),
              member(12, person("Дарья"), CensusRole.DAUGHTER, ref_member=5, age=8),
              member(13, person("Федосья"), CensusRole.DAUGHTER, ref_member=5, age="2 мес"),
              member(14, person("Пелагѣя", "Семіонова"), CensusRole.NIECE, ref_member=2, age=18, parent_member=16),
              member(15, person("Александра", "Семіонова"), CensusRole.NIECE, ref_member=2, age=16, parent_member=16),
              member(16, person("Семенъ", "Герасимовъ", "Мальчиковъ"), CensusRole.SON, hidden=True,
                     comment="отдан в рекруты в 1833, в списки РС 1834 и 1850 не включён; "
                             "Назван в обеих сказках: РС 8 1834, семья 553 — его жена Марья (член 14, «жена "
                             "рекрута Семена Герасимова») и дочь Пелагея (член 16, 3 года) остались в хозяйстве")),
            ),
    defaults=RecordDefaults(
        status_male=STATE_PEASANT_MALE,
        status_female=STATE_PEASANT_FEMALE,
    ),
    prev_revision_year=1834,
    record_month=Month.OCTOBER,
    record_day=1,
)
