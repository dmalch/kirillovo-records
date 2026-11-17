from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)

kirillovo_marriages_1919 = marriage_records(
    "ГАПО", "2854", "17", "15", "Кириллово", "",
    1919,
    *page("?",
          *marriage_month(Month.NOVEMBER,
                          marriage(72, 17,
                                   groom=person("Афанасий", "Михайлов", last_name_orig="Мальчиков"),
                                   groom_marriage_num=1,
                                   groom_age=19,
                                   bride=person("Анастасия", "Алексеева", last_name_orig="Углова"),
                                   bride_marriage_num=1,
                                   bride_age=22,
                                   comment="Гражданская регистрация (ЗАГС)"),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
    ),
    civil=True,
)
