from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          page, person)
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE,
                                   HIEREUS, SOLDIER, SOLDIER_WIFE)

# SELECTIVE EXTRACT: Only Мальчиков-family related entries from 1862 metric book.
# Archive reference unknown for this period; using placeholder.
# No page numbers available in source extract.
# No clergy names recorded in source extract.

kirillovo_marriages_1862 = marriage_records(
    "ЦГАРМ",
    "57",
    "6",
    "457",
    "Кириллово",
    "Казанская церковь",
    1862,
    *marriage_month(
        Month.JANUARY,
        marriage(
            2,
            28,
            groom=person("Никита", "Степанов", last_name_orig="Голубев"),
            groom_marriage_num=2,
            bride=person("Ольга", "Евпалова", last_name_orig="Горбатова", residence="с. Кирилово"),
            groom_age=50,
            bride_age=45,
            witness1=person("Лукьян", "Михайлов", last_name_orig="Янин"),
            witness2=person("Андрей", "Моисеев", last_name_orig="Позняков"),
            witness3=person("Иван", "Степанов", last_name_orig="Бачков"),
            witness4=person("Ефрем", "Григорьев", last_name_orig="Царев"),
        ),
        marriage(
            7,
            28,
            groom=person("Ко?тей?", "Григорьев", last_name_orig="Митюшин", comment="имя жениха неразб"),
            groom_marriage_num=1,
            bride=person("Татьяна", "Савастьянова", residence="с. Кириллово"),
            groom_age=25,
            bride_age=24,
            witness1=person("Абрам", "Фетисов"),
            witness2=person("Ермолай", comment="Ермолай Т?лов"),
            witness3=person("Константин", "Яковлев", last_name_orig="Позняков"),
            witness4=person("Федор", "Антонов", last_name_orig="Янин"),
        ),
    ),
    *marriage_month(
        Month.APRIL,
        marriage(
            17,
            29,
            groom=person("Поликарп", "Андреев", last_name_orig="Калинин"),
            groom_marriage_num=3,
            bride=person("Екатерина", "Павлова", last_name_orig="Жиркова"),
            bride_marriage_num=1,
            witness1=person("Косма", "Андрианов", last_name_orig="Мальчиков"),
            witness2=person("Прокопий", "Иванов", last_name_orig="Маршев"),
            witness3=person("Никифор", "Парфенов", last_name_orig="Калинкин"),
            witness4=person("Алексей", "Захаров", comment="Фамилия не указана"),
            comment="Фамилия жениха неточно (Калинин?); место жительства невесты — с. Кириллово; фамилия 2-го поручителя неточно (Маршев?)",
        ),
    ),
    # Дописано при сплошном проходе (02.10.2026) по скану (альбом «1862 (ЦГАРМ 57-6-457)», pk 1338)
    *page("?",
          *marriage_month(Month.SEPTEMBER,
                          # поручитель по невесте — Самсон Наумович Янин
                          marriage(29, 9,
                                   groom=person("Антонъ", "Михайловъ", "Булановъ", status=SOLDIER, comment="«отставной рядовый»"),
                                   groom_marriage_num=1, groom_age=35,
                                   bride=person("Евфросинія", "Константинова", "Лошкашкина", status=SOLDIER_WIFE, comment="фамилия читается неуверенно; в 1861 (рожд. м. №53, жена Егора Лошкашкина) и 1863 (рожд. м. №107) — «Артемова»"),
                                   bride_marriage_num=2, bride_age=39,
                                   witness1=person("Иванъ", "Ильинъ", "Аникинъ", side=Side.GROOM),
                                   witness2=person("Степанъ", "Даниловъ", "Малахинъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                                   witness3=person("Самсонъ", "Наумовъ", "Янинъ", side=Side.BRIDE),
                                   witness4=person("Назаръ", "Никитинъ", "Голубевъ", side=Side.BRIDE),
                                   priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                                   comment="кадр 53 альбома",
                                   reviewed=False),
                          ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE, status_bride=ECON_PEASANT_MAIDEN),
)
