from verso.ru.dsl import Month, RecordDefaults, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MAIDEN, ECON_PEASANT_MALE

# SELECTIVE EXTRACT: Only Мальчиков-family related entries from 1863 metric book.
# Archive reference unknown for this period; using placeholder.
# No page numbers available in source extract.
# No clergy names recorded in source extract.
# Records 11 and 32 have Мальчиков as поручитель (witness); record 40 has Мальчиков as groom.
# Bride ages unknown (marked'?' in source) — use w_day=0 not applicable here;
# bride ages are omitted in source, not the wedding day.

kirillovo_marriages_1863 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "710",
    "Кириллово",
    "Казанская церковь",
    1863,
    *marriage_month(
        Month.JANUARY,
        marriage(
            11,
            25,
            groom=person("Иеамил?", "Кириллов", last_name_orig="Амес?", comment="Имя жениха неточно: «Иеамил?»; фамилия неточна: «Амес?»"),
            groom_marriage_num=1,
            bride=person("Марина", "Сергеева", last_name_orig="Матышева", comment="Фамилия неточна: «Матышева?»"),
            witness1=person("Илья", "Павлов", last_name_orig="Мальчиков"),
            witness2=person("Савелий", "Игнатов", last_name_orig="Сафронов"),
            witness3=person("Никита", "Павлов", last_name_orig="Белов"),
            witness4=person("Афанасий", "Семенов", last_name_orig="Мартынов", comment="Фамилия неточна: «Мартынов?»"),
            comment="Возраст невесты не указан в источнике",
        ),
    ),
    *marriage_month(
        Month.JUNE,
        marriage(
            32,
            30,
            groom=person("Иван", "Григорьев", last_name_orig="Разоренов"),
            groom_marriage_num=1,
            bride=person("Марина", "Ильина", last_name_orig="Щетинина"),
            witness1=person("Илья", "Павлов", last_name_orig="Мальчиков"),
            witness2=person("Василий", "?", last_name_orig="Шитиков", comment="Отчество неразборчиво: «Иераолмав»"),
            witness3=person("Карп", "Иванов", last_name_orig="Щетинин"),
            witness4=person("Иван", "Яковлев", last_name_orig="Поздняков"),
            comment="Возраст невесты не указан в источнике",
        ),
    ),
    *marriage_month(
        Month.NOVEMBER,
        marriage(
            35,
            1,
            groom=person("Яков", "Андреев", last_name_orig="Янин", residence="д. Гоголев Бор"),
            groom_marriage_num=1,
            bride=person("Матрона", "Родионова", last_name_orig="Богачева", residence="д. Гоголев Бор"),
            bride_marriage_num=1,
            groom_age=19,
            bride_age=17,
            witness1=person("Родион", "Яковлев", last_name_orig="Янин", residence="д. Гоголев Бор"),
            witness2=person("Никифор", "Петров", comment="Самалов?"),
            witness3=person("Степан", "Родионов", last_name_orig="Богачев"),
            witness4=person("Матвей", "Иванов", comment="Моровин?"),
        ),
        marriage(
            45,
            8,
            groom=person("Даниил", "Ефимов", last_name_orig="Юдин"),
            groom_marriage_num=1,
            bride=person("Евдокия", "Сергеева", residence="д. Гоголев Бор", comment="фамилия невесты неразб: ?нкина"),
            bride_marriage_num=1,
            groom_age=18,
            witness1=person("Василий", "Лаврентьев", last_name_orig="Глушилин"),
            witness2=person("Родион", "Яковлев", last_name_orig="Янин", residence="д. Гоголев Бор"),
            witness3=person("Василий", "Егоров", last_name_orig="Козлов"),
            witness4=person("Захар", "Григорьев", last_name_orig="Янин", residence="д. Гоголев Бор"),
        ),
        marriage(
            46,
            8,
            groom=person("Петр", "Иванов", last_name_orig="Муханов"),
            groom_marriage_num=1,
            bride=person("Татьяна", "Михайлова", last_name_orig="Романова", residence="д. Гоголев Бор"),
            groom_age=21,
            bride_age=21,
            witness1=person("Григорий", "Филиппов", last_name_orig="Царьков"),
            witness2=person("Андрей", "Яковлев", last_name_orig="Янин", residence="д. Гоголев Бор"),
            witness3=person("Матвей", "Дорофеев", last_name_orig="Романов"),
            witness4=person("Василий", "Степанов", last_name_orig="Назаров"),
        ),
        marriage(
            40,
            6,
            groom=person("Никита", "Казьмин", last_name_orig="Мальчиков", comment="Отчество неточно: «Казмин?»"),
            groom_marriage_num=1,
            bride=person("Дарья", "Панфилова", last_name_orig="Гришаева", comment="Отчество неточно: «Панфилова?»; фамилия неточна: «Гришаева»"),
            witness1=person("Матвей", "Афанасьев", last_name_orig="Егоров"),
            witness2=person("Иван", "Платонов", last_name_orig="Куранов", comment="Фамилия неточна: «Куранов?»"),
            witness3=person("Тимофей", "Григорьев", last_name_orig="Фомин"),
            witness4=person("?", "Афанасьев", last_name_orig="Егоров", comment="Имя неразборчиво: «Еромлай» в источнике"),
            comment="Возраст невесты не указан в источнике; дата (под вопросом в источнике)",
        ),
    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE, status_bride=ECON_PEASANT_MAIDEN),
)
