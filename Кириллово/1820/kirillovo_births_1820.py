from verso.ru.dsl import (Gender, Month, RecordDefaults, birth, birth_month, birth_records, page,
                          person)
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_LEGAL_WIFE, ECON_PEASANT_MALE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (фамилий в книге нет —
# опознаны по имени и отчеству, см. Кириллово/families/). Остальные записи года не внесены.
# Альбом «1820 (ЦГАРМ 57-6-100)», кадры — развороты; ч. 1 на лл. 81–91, разворота
# л. 91об–92 (конец декабря) в альбоме нет.
kirillovo_births_1820 = birth_records(
    "ЦГАРМ", "57", "6", "100", "Кириллово", "Успенская",
    1820,
    *page("83об",
          *birth_month(Month.MARCH,
                       # восприемник Михаил Емельянович (Янин) — крёстный и детей Ильи Петрова 1817 №175, 1822 №24
                       birth(21, Gender.MALE, 4, 7,
                             child=person("Кандратій"),
                             father=person("Илья", "Петровъ"),
                             god_parent1=person("Михаилъ", "Емельяновъ"),
                             god_parent2=person("Екатерина", "Парамонова")),
                       ),
          ),
    *page("86",
          *birth_month(Month.JUNE,
                       # восприемник Денис Егорович (Янин) — крёстный и сына Марка Иванова 1817 №23
                       birth(34, Gender.FEMALE, 18, 20,
                             child=person("Акилина"),
                             father=person("Марка", "Ивановъ"),
                             god_parent1=person("Денисъ", "Егоровъ"),
                             god_parent2=person("Акилина", "Иванова")),
                       # восприемник Денис Егорович (Янин); отец Егор Прокофьев — возможно, отец самого Дениса
                       birth(56, Gender.MALE, 25, 29,
                             child=person("Петръ"),
                             father=person("Егоръ", "Прокофьевъ"),
                             god_parent1=person("Денисъ", "Егоровъ"),
                             god_parent2=person("Матрона", "Прокофьева")),
                       ),
          ),
    *page("87",
          *birth_month(Month.JULY,
                       # Илья Павлович Мальчиков (РС 1834: ~1821); восприемники — Герасим Федорович и,
                       # вероятно, Ирина Григорьевна Мальчиковы
                       birth(64, Gender.MALE, 17, 20,
                             child=person("Илья"),
                             father=person("Павелъ", "Давидовъ"),
                             god_parent1=person("Герасимъ", "Ѳедоровъ"),
                             god_parent2=person("Ирина", "Григорьева")),
                       ),
          ),
    *page("90об",
          *birth_month(Month.DECEMBER,
                       # отец — вероятно, Михаил Павлович Мальчиков (женат с 1818); в той же книге (ж. № 70)
                       # восприемником записан и другой Михаил Павлов, отставной солдат
                       birth(71, Gender.FEMALE, 4, 6,
                             child=person("Варвара"),
                             father=person("Михаилъ", "Павловъ"),
                             god_parent1=person("Артемъ", last_name_orig="Кочетовъ"),
                             god_parent2=person("Лукерья", comment="отчество не записано")),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_FEMALE,
        status_mother=ECON_PEASANT_LEGAL_WIFE,
    ),
)
