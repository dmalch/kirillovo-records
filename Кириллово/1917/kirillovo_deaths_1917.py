from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import KILLED
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIFE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-574, альбом
# Photos «1917 (ГАПО 182-5-574)» (pk 1184), ч. 3 — л. 351 шмуцтитул, лл. 351об–371об (м. №1–43, ж. №1–52), прочитана
# целиком 26.10.2026; импорта не было. Погребали свящ. Николай Расказовский и Григорий Феодоровский.
kirillovo_deaths_1917 = death_records(
    "ГАПО",
    "182",
    "5",
    "574",
    "Кириллово",
    "Казанская церковь",
    1917,
    *death_month(Month.JANUARY,
                 # Анна, дочь Ивана Тимофеевича Коверкина (мать — Анна Климентьевна, Мальчикова?)
                 death(3, Gender.FEMALE, 6, 7,
                       deceased=person("Анна", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Иванъ", "Тимоѳеевъ", "Коверкинъ"), Relationship.FATHER)],
                       comment="мать — Анна Климентьевна (Мальчикова?); возраст на правой странице",
                       page="351об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Параскева Алексеевна, жена Михаила Егоровича «Кистенева» (= Малахаева)
                 death(37, Gender.FEMALE, 6, 7,
                       deceased=person("Параскева", "Алексѣева", status=PEASANT_WIFE),
                       relatives=[relative(person("Михаилъ", "Егоровъ", "Кистеневъ", comment="он же: Михаил Егорович Малахаев"), Relationship.HUSBAND)],
                       age=57,
                       page="364об",
                       reviewed=False),
                 ),
    *death_month(Month.NOVEMBER,
                 # Георгий «Кистенев» — убит (8.11.1917; в тот же день убит Михаил Дмитриевич Курочкин)
                 death(40, Gender.MALE, 8, 9,
                       deceased=person("Георгій", None, "Кистеневъ", comment="отчество не записано"),
                       cause_of_death=KILLED,
                       comment="возраст у корешка («2…»)",
                       page="369об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
