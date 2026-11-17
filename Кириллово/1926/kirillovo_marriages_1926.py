from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)

# Импорт из таблицы (2 записи). Сверено и дополнено 30.10.2026 по скану: ГАПО Р-2854-17-14, альбом Photos
# «1926 (ГАПО Р-2854-17-14)» (pk 1035, 828 кадров — лл. 126–574), «Запись о браке» Кирилловского ВИКа 1926 г., № 1
# (9 января) – № 448 (9 декабря), прочитана целиком; акт на листе. Импортные на месте: № 44 л. 169, № 60 л. 184.
# Не выписан: № 63 (л. 187, 13 февраля) Яков Васильевич Поздняков, р. 20.10.1901 × Аграфена Ивановна Чиркова —
# брат? Федора Васильевича Позднякова (муж Евфросинии «Сырцовой»); родство с Константиновичами не установлено.
kirillovo_marriages_1926 = marriage_records(
    "ГАПО", "2854", "17", "14", "Кириллово", "",
    1926,
    *page("?",
          *marriage_month(Month.FEBRUARY,
                          marriage(44, 6,
                                   groom=person("Иван", "Васильев", last_name_orig="Верхов"),
                                   groom_marriage_num=1,
                                   groom_age=22,
                                   bride=person("Евдокия", "Васильева", last_name_orig="Мальчикова"),
                                   bride_marriage_num=1,
                                   bride_age=19,
                                   comment="Гражданская регистрация (ЗАГС)"),
                          marriage(60, 13,
                                   groom=person("Егор", "Иванов", last_name_orig="Мальчиков"),
                                   groom_marriage_num=1,
                                   groom_age=25,
                                   bride=person("Екатерина", "Егорова", last_name_orig="Дремкова"),
                                   bride_marriage_num=1,
                                   bride_age=20,
                                   comment="Гражданская регистрация (ЗАГС)"),
                          ),
          ),
    *marriage_month(Month.AUGUST,
                    # жених — Степан Семенович «Юлин» = Стефан, сын Семена Васильевича Мальчикова «Юлина» (1899 №74, р. 9.12
                    # ст. ст. = 21.12 н. ст.; здесь — «25 декабря»)
                    marriage(178, 26,
                             groom=person("Степан", "Семенов", "Юлин", comment="= Стефан Семенович Мальчиков «Юлин», р. 1899 (1899 №74)"),
                             groom_marriage_num=1, groom_age=26,
                             bride=person("Мария", "Васильева", "Корнева"),
                             bride_marriage_num=2, bride_age=28,
                             comment="Гражданская регистрация (ЗАГС); жених р. 25.12.1899, холост, хлебопашец, с. Кириллово; невеста 28 лет, вдова, с. Красная Дубрава",
                             page="303",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(
        residence="Кириллово",
    ),
    civil=True,
)
