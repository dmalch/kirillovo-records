from verso.ru.dsl import Gender, Month, RecordDefaults, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, HIEREUS, MAIDEN

# SELECTIVE EXTRACT: Only Мальчиков-family related entries from 1872 metric book.
# Archive reference unknown for this period; using placeholder.
# No page numbers available in source extract.
# No clergy names recorded in source extract.

kirillovo_births_1872 = birth_records(
    "ГАПО",
    "182",
    "5",
    "732",
    "Кириллово",
    "Казанская церковь",
    1872,
    *birth_month(
        Month.FEBRUARY,
        # сверено по скану 05.10.2026 (л. 73об, ж. №12): совпадает; отец ясно «Аѳонасій Ивановъ Мальчиковъ» (в браке
        # 1869 №3 с Марфой Андреевной Мальчиковой его фамилия читалась «Мякининъ»); крестил иерей Павел Кротков
        birth(
            12,
            Gender.FEMALE,
            13,
            13,
            child=person("Агафья"),
            father=person("Афанасий", "Иванов", last_name_orig="Мальчиков"),
            mother=person("Марфа", "Андреева"),
            god_parent1=person("Александр", "Трофимов", last_name_orig="Баранов"),
            god_parent2=person("Ксения", "Андреева"),
            comment="Ребёнок записан как «Агафья Афанасьева Мальчикова»; дата (под вопросом в источнике)",
        ),
    ),
    # Дописано при сплошном проходе (05.10.2026) по скану (альбом «1872 (ГАПО 182-5-732)», pk 1348) — записи первой
    # волны, которых не было в импорте. Ч. 1 — лл. 69об–93, 120 рождений, прочитана целиком. Книга пишет «казенный
    # крестьянинъ», умолчания файла остались от импорта («экономический»). Вся запись — на левой странице разворота.
    *birth_month(Month.JANUARY,
                 # мать — Евдокия Емельяновна Мальчикова (брак 1860); Михаил умер 11.03.1872 (смерть м. №9)?
                 birth(1, Gender.MALE, 1, 1,
                       child=person("Михаилъ"),
                       father=person("Матѳей", "Стефановъ", "Ѳетисовъ"),
                       mother=person("Евдокія", "Емельянова"),
                       god_parent1=person("Гавріилъ", "Алексѣевъ", "Сапроновъ"),
                       god_parent2=person("Ирина", "Стефанова", "Ѳетисова", status=MAIDEN),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="69об",
                       reviewed=False),
                 ),
    *birth_month(Month.JUNE,
                 # «Алексѣй Ивановъ Янинъ» с женой Параскевой Феодосиевной = Алексей Даниилович Янин? (Гоголев Бор; в 1871
                 # — «Прокопіевъ»); Акилина умерла 24.06.1872 (смерть ж. №17)
                 birth(28, Gender.FEMALE, 2, 2,
                       child=person("Акилина"),
                       father=person("Алексѣй", "Ивановъ", "Янинъ", residence="Гоголев Бор", comment="так в подлиннике; = Алексей Даниилович Янин? (в Гоголевом Бору есть и Алексей Прокофьевич Слѣповъ — восприемник 1878)"),
                       mother=person("Параскева", "Ѳеодосѣева"),
                       god_parent1=person("Флоръ", "Сидоровъ", "Даронинъ", residence="Гоголев Бор"),
                       god_parent2=person("Параскева", "Ѳедорова", "Киселева", residence="Гоголев Бор"),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="79об",
                       reviewed=False),
                 # Михаил Андреянович Янин («Сырцевъ»)
                 birth(29, Gender.FEMALE, 2, 4,
                       child=person("Акилина"),
                       father=person("Михаилъ", "Андреяновъ", "Сырцевъ", comment="= Михаил Андреянович Янин"),
                       mother=person("Параскева", "Даніилова"),
                       god_parent1=person("Лазарь", "Егоровъ", "Сапроновъ"),
                       god_parent2=person("Пелагія", "Герасимова", "Киселева", status=MAIDEN),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="79об",
                       reviewed=False),
                 ),
    *birth_month(Month.JULY,
                 # Константин Яковлевич Поздняков (= Мальчиков); восприемница — его дочь Анастасия
                 birth(34, Gender.FEMALE, 10, 10,
                       child=person("Марія"),
                       father=person("Константинъ", "Яковлевъ", "Поздняковъ", comment="= Константин Яковлевич Мальчиков"),
                       mother=person("Ксенія", "Митрофанова"),
                       god_parent1=person("Петръ", "Ѳедоровъ", "Дыркинъ"),
                       god_parent2=person("Анастасія", "Константинова", "Позднякова", status=MAIDEN, comment="в подлиннике «Настасія»"),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="82об",
                       reviewed=False),
                 # Яков Андреевич Янин (Гоголев Бор); восприемница — его сестра Агафья Андреевна Морозова, урожд. Янина
                 birth(37, Gender.FEMALE, 20, 20,
                       child=person("Акилина"),
                       father=person("Яковъ", "Андреевъ", "Янинъ", residence="Гоголев Бор"),
                       mother=person("Матрена", "Иванова"),
                       god_parent1=person("Герасимъ", "Григорьевъ", status="дьячок Казанской церкви", comment="фамилия не дописана («Бого…»)"),
                       god_parent2=person("Агаѳія", "Андреева", "Морозова", residence="Гоголев Бор", comment="= Агафья Андреевна Янина (брак 1865)"),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="82об",
                       reviewed=False),
                 # Андрей Константинович Мальчиков (брак 1860 с Анастасией Леонтьевной Бубенчиковой)
                 birth(36, Gender.MALE, 24, 26,
                       child=person("Илія"),
                       father=person("Андрей", "Константиновъ", "Мальчиковъ", status="солдат в бессрочном отпуску"),
                       mother=person("Анастасія", "Леонтьева", comment="в подлиннике «Настасія»"),
                       god_parent1=person("Антонъ", "Сидоровъ", "Назаровъ"),
                       god_parent2=person("Евдокія", "Ѳотіева", "Мальчикова"),
                       priest=person("Павелъ", "Ѳеофановъ", "Кротковъ", status=HIEREUS),
                       page="83об",
                       reviewed=False),
                 ),
    *birth_month(Month.AUGUST,
                 # Герасим Яковлевич Поздняков (= Мальчиков)
                 birth(38, Gender.MALE, 5, 6,
                       child=person("Иванъ"),
                       father=person("Герасимъ", "Яковлевъ", "Поздняковъ", comment="= Герасим Яковлевич Мальчиков"),
                       mother=person("Дарія", "Савельева"),
                       god_parent1=person("Иванъ", "Силантьевъ", "Богачевъ", status="рядовой солдат в бессрочном отпуску"),
                       god_parent2=person("Татіана", "Трофимова", status=MAIDEN),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="84об",
                       reviewed=False),
                 ),
    *birth_month(Month.SEPTEMBER,
                 # Козьма Андреянович Мальчиков; восприемница — Гликерия Степановна, жена его сына Матфея
                 birth(48, Gender.FEMALE, 30, 30,
                       child=person("Наталія"),
                       father=person("Козьма", "Андріановъ", "Мальчиковъ", comment="в подлиннике «Косма»"),
                       mother=person("Пелагія", "Андреева"),
                       god_parent1=person("Никита", "Аѳанасьевъ", "Егоровъ"),
                       god_parent2=person("Гликерія", "Стефанова", "Мальчикова"),
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="86об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
