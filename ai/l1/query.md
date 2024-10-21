# Примеры запросов

- Простые запросы к базе знаний для поиска фактов:

```prolog
% Является ли V персонажем?
?- character(v).
% Ответ: true.

% Кто является членом банды Moxes?
?- member_of(X, moxes).
% Ответ: X = judy_alvarez.

```

- Запросы, использующие логические операторы (и, или, не):

```prolog
% Кто находится в Найт-Сити и является врагом Арасаки?
?- is_in(X, night_city), enemy_of(X, arasaka).
% Ответ: X = v.

% Найти персонажей, которые не являются членами какой-либо банды
?- character(X), not(member_of(X, _)).
% Ответ: Персонажи без указанных банд.

% Персонажи, которые являются друзьями V или работают на Арасака
?- (friend_of(X, v); works_for(X, arasaka)).
% Ответ: X = johnny_silverhand; X = jackie_welles; X = judy_alvarez; X = panam_palmer; X = saburo_arasaka; и т.д.
```

- Запросы, использующие переменные для поиска объектов с определенными характеристиками:

```prolog
% Кто использует смарт-оружие?
?- uses_smart_weapon(X).
% Ответ: X = v.

% Какие виды оружия используются персонажами, находящимися в Бэдлендс?
?- is_in(X, badlands), uses_weapon(X, Weapon).
% Ответ: X = panam_palmer, Weapon = tech_sniper_rifle.
```

Запросы, которые требуют выполнения правил для получения результата:

```prolog
% Являются ли V и Джонни Сильверхенд союзниками?
?- ally(v, johnny_silverhand).
% Ответ: true.

% Кто опасен?
?- dangerous(X).
% Ответ: Члены банд Tyger Claws, Valentinos, Sixth Street.

% Кто использует технологическое оружие?
?- uses_tech_weapon(X).
% Ответ: X = panam_palmer.
```

- Дополнительные запросы:

```prolog
% Найти всех персонажей, которые используют мощное оружие.
?- uses_weapon(X, Weapon), weapon(Weapon).
% Возвращает всех персонажей и оружие, которое они используют.

% Кто из персонажей работает для корпорации Arasaka и использует смарт-оружие?
?- works_for(X, arasaka), uses_smart_weapon(X).
% Возвращает персонажей из Arasaka, использующих смарт-оружие.

% Найти всех врачей и их пациентов.
?- doctor_of(Doctor, Patient).
% Ответ: Doctor = viktor_vector, Patient = v.

% Определить, кто является отцом Yorinobu Arasaka.
?- father_of(Father, yorinobu_arasaka).
% Ответ: Father = saburo_arasaka.

% Идентифицировать всех персонажей, которые являются братьями или сестрами.
?- sibling(X, Y).
% Ответ: X = yorinobu_arasaka, Y = hanako_arasaka.
```
