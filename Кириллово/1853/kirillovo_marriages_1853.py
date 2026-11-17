from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE

kirillovo_marriages_1853 = marriage_records(
    "ЦГАРМ",
    "57",
    "6",
    "430",
    "Кириллово",
    "Казанская церковь",
    1853,
    *page(
        "?",
        *marriage_month(
            Month.JANUARY,
            marriage(
                1,
                7,
                groom=person("Петр", "Акимов", last_name_orig="Мальчиков"),
                groom_marriage_num=1,
                bride=person("Марина", "Агапова", last_name_orig="Лапшина"),
                bride_marriage_num=1,
                witness1=person("Семен", "Емельянов", last_name_orig="Мальчиков"),
                witness2=person("Трофим", "Пимонов", last_name_orig="Бубенчиков"),
                witness3=person("Григорий", "Феодоров", last_name_orig="Чекин"),
                witness4=person("Даниил", "Артамонов", last_name_orig="Лапшин"),
            ),
            marriage(
                2,
                7,
                groom=person("Семен", "Константинов", last_name_orig="Романов"),
                groom_marriage_num=2,
                bride=person("Гликерия", "Иванова", last_name_orig="Юлина"),
                bride_marriage_num=2,
                witness1=person("Андрей", "Иванов", last_name_orig="Калнинин", comment="Андрей Иванов Калнинин"),
                witness2=person("Терентий", "Васильев", last_name_orig="Кондаков"),
                witness3=person("Андриан", "Григорьев", last_name_orig="Мальчиков"),
                witness4=person("Арефий", "Павлов", comment="Арефий? Павлов ?"),
            ),
        ),
        *marriage_month(
            Month.OCTOBER,
            marriage(
                25,
                30,
                groom=person("Хритон", "Иосифов", last_name_orig="Фетисов"),
                groom_marriage_num=2,
                bride=person("Евдокия", "Иванова", last_name_orig="Спаряева"),
                bride_marriage_num=1,
                witness1=person("Семен", "Емельянов", last_name_orig="Мальчиков"),
                witness2=person("Иван", "Матвеев", last_name_orig="Бурлин"),
                witness3=person("Иван", last_name_orig="Фетисов"),
                witness4=person("Степан", "Иосифов", last_name_orig="Фетисов"),
            ),
        ),
    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
