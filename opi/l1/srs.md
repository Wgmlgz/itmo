# Software Requirements Specification

## Introduction

### Purpose

**Office.com** — это онлайн-платформа от Microsoft, предоставляющая доступ к версиям **Word, Excel, PowerPoint** и **OneNote** через браузер. Пользователи могут создавать, редактировать и обмениваться документами, сохранять их в облаке **OneDrive** для доступа с любого устройства и работать над файлами вместе в реальном времени. Платформа поддерживает бесплатное и платное использование, предлагая дополнительные функции для подписчиков.

## Document Conventions

- **Бекенд**: Часть программного обеспечения, работающая на сервере. Она обрабатывает логику приложения, взаимодействует с базой данных и подготавливает данные для фронтенда.
- **Библиотека**: Коллекция предопределённого функционала, которую можно добавить к проекту для расширения его возможностей или упрощения разработки.
- **Фреймворк**: Набор инструментов и библиотек, предоставляющих готовую структуру для разработки приложений, упрощая создание и поддержку кода.
- **Фронтенд**: Часть программного обеспечения, с которой напрямую взаимодействует пользователь. Она включает в себя пользовательский интерфейс и элементы управления.
- **CSS** (Cascading Style Sheets): Язык стилей, используемый для задания внешнего вида веб-страницы, созданной с помощью HTML.
- **Data Flow Diagram (DFD)**: Графическое представление потока данных между процессами, системами и хранилищами в рамках некоторой системы.
- **HTML** (HyperText Markup Language): Стандартный язык разметки, используемый для создания и структурирования контента на веб-сайтах.
- **JS** (JavaScript): Язык программирования, применяемый для создания интерактивных элементов на веб-сайтах.
- **Azure**: Облачная платформа от Microsoft, предоставляющая сервисы для хостинга, вычислений, хранения данных и многих других задач, поддерживающих работу Office.com.
- **SharePoint**: Платформа для создания веб-сайтов от Microsoft. Используется в Office.com для управления документами и совместной работы.
- **OneDrive**: Облачное хранилище от Microsoft, интегрированное с Office.com, позволяющее пользователям хранить файлы и документы в облаке и обеспечивающее доступ к ним с любого устройства.
- **Microsoft Graph API**: Сервис, позволяющий работать с данными, хранящимися в облаке Microsoft, включая информацию о пользователях, файлы, документы и многое другое, доступные через Office.com.
- **Software Requirements Specification (SRS)**: Документ, описывающий все функциональные и нефункциональные требования к программному продукту.
- **UseCase** (Сценарий использования): Описание последовательности действий, выполняемых системой, для достижения конкретной цели пользователя.

## Intended Audience and Reading Suggestions

Студенты 1-4 курса бакалавриата технических ВУЗов.

## Project Scope

Сверхбольшой масштаб проекта: “...к сверхбольшим - больше 100 млн. USD…”.

## References

- [Use Case (сценарий использования)](https://habr.com/ru/articles/699522/)
- [Информация о SRS](https://habr.com/ru/articles/52681/)
- [Информация о RUP](https://qaevolution.ru/metodologiya-menedzhment/rup/)
- [Классификация проектов](https://clck.ru/38qJ3n)
- [DFD диаграммы](https://habr.com/ru/articles/668684/)
- [office.com](https://www.office.com/)
- [Прецеденты](https://clck.ru/38qekT)

## Overall Description

### Product Features

В данном разделе представлен обзор ключевых функций Office.com на высоком уровне, включая:

- **Доступ к Office приложениям через браузер**: Пользователи могут использовать версии Word, Excel, PowerPoint, и OneNote без необходимости установки программного обеспечения.
- **Совместная работа в реальном времени**: Возможность одновременной работы над документами с коллегами и просмотра изменений в реальном времени.
- **Хранение в облаке OneDrive**: Файлы сохраняются в облаке, обеспечивая доступ к ним с любого устройства и местоположения.
- **Шаблоны и инструменты форматирования**: Предоставляются различные шаблоны и инструменты для упрощения создания профессионально выглядящих документов.
- **Интеграция с Microsoft 365**: Плотная интеграция с другими сервисами Microsoft для расширенного функционала, включая Outlook, Teams и SharePoint.

Для визуализации общего взаимодействия системы предлагается разместить DFD-диаграмму, демонстрирующую ключевые потоки данных между компонентами системы и пользователями.

### Operating Environment

Office.com разработан для работы в разнообразных операционных системах, таких как Windows, macOS, и Linux, через современные веб-браузеры (например, Google Chrome, Mozilla Firefox, Safari и Microsoft Edge). Продукт оптимизирован для обеспечения высокой производительности и совместимости в различных сетевых условиях. Он требует подключения к интернету и поддерживает интеграцию с различными облачными хранилищами, в частности с OneDrive и SharePoint. Для максимальной эффективности рекомендуется использование последних версий браузеров и операционных систем.

### Design and Implementation Constraints

Разработка Office.com подчиняется следующим ограничениям:

- **Язык программирования и база данных**: Основная разработка ведется с использованием JavaScript для фронтенда и C# для бекенда, с базой данных Azure SQL.
- **Стандарты кодирования**: Применяются внутренние стандарты Microsoft для обеспечения высокого качества кода и удобства поддержки.
- **Стандарты обмена данными**: Используется формат JSON для обмена данными между клиентом и сервером.
- **Совместимость**: Продукт разрабатывается с учетом обеспечения совместимости с последними версиями основных браузеров.
- **Бизнес-логика**: Соблюдение правил и ограничений, наложенных бизнес-моделью Office.com, включая уровни доступа и подписки на сервисы.

### User Documentation

Для Office.com предусмотрены следующие виды документации для пользователей:

- **Руководства пользователя**: Подробные инструкции по использованию каждого из приложений Office в браузере, включая советы по оптимизации рабочего процесса.
- **Часто задаваемые вопросы (FAQ)**: Раздел с ответами на общие вопросы пользователей о функциях и возможностях сервиса.
- **Видеоуроки**: Серия обучающих видео, покрывающих ключевые функции и оптимальные практики работы с Office.com.
- **Форум поддержки**: Платформа для общения пользователей с командой поддержки и друг с другом по вопросам использования продукта.
- **Блог**: Статьи с советами, руководствами и новостями о последних обновлениях и функциях Office.com.

### Assumptions and Dependencies

- **Предположения**:

  - Пользователи имеют стабильное интернет-соединение для доступа к сервисам Office.com.
  - Пользователи используют современные веб-браузеры, которые поддерживают необходимые веб-стандарты для корректной работы приложений.
  - Операционные системы пользователей обновлены до последних версий для обеспечения совместимости и безопасности.

- **Зависимости**:
  - Работоспособность и доступность сервисов Office.com зависят от поддержки облачной инфраструктуры Microsoft Azure.
  - Обновления и новые функции могут требовать адаптации со стороны пользователей и потенциальных изменений в используемых ими настройках или оборудовании.
  - Интеграция с другими сервисами Microsoft, такими как OneDrive и SharePoint, предполагает зависимость от их доступности и обновлений.

## Functional requirements

### Для пользователя

- **U1**: Доступ к приложениям Word, Excel, PowerPoint, и OneNote через браузер.
- **U2**: Возможность совместной работы и реального времени редактирования документов.
- **U3**: Интеграция с облачным хранилищем OneDrive для хранения документов.
- **U4**: Поддержка различных форматов документов для загрузки и скачивания.
- **U5**: Возможность использования шаблонов и инструментов форматирования.
- **U6**: Персонализированные настройки интерфейса пользователя.
- **U7**: Поддержка многоязычного контента.
- **U8**: Интеграция с социальными сетями для обмена документами.
- **U9**: Возможность комментирования и обратной связи в документах.
- **U10**: Расширенные опции безопасности для защиты документов.

### Для владельцев

- **O1**: Управление пользователями, включая создание, редактирование и удаление учетных записей.
- **O2**: Настройка уровней доступа и политик безопасности.
- **O3**: Мониторинг и аналитика использования ресурсов и активности пользователей.
- **O4**: Обновление и добавление новых функций и сервисов.

## Нефункциональные требования

### Usability requirements (требование к удобству использования)

- **N1**: Адаптивный дизайн, поддерживающий различные устройства и разрешения экрана.
- **N2**: Интуитивно понятный интерфейс пользователя.

### Performance requirements (требование к производительности)

- **N3**: Время загрузки страницы не более 3 секунд при скорости интернет-соединения 10 Мбит/с.
- **N4**: Поддержка минимум 1000 одновременных сессий пользователей без снижения производительности.

### Security & safety requirements (требование безопасности & сохранности)

- **N5**: Реализация протоколов безопасности для защиты данных и транзакций.
- **N6**: Шифрование паролей и пользовательских данных.
- **N7**: Резервное копирование и восстановление данных.

### Software quality attributes (атрибуты качества программного обеспечения)

- **N8**: Ведение логов ошибок и системных событий.
- **N9**: Документация для API и разработчиков на английском языке.

### External interface requirements (требования к внешнему интерфейсу)

- **N10**: REST API для интеграции с внешними сервисами.
- **N11**: Поддержка многоязычности интерфейса и документации.

## Атрибуты и оценка часов

| Номер требования | Статус     | Кол-во часов | Стабильность |
| ---------------- | ---------- | ------------ | ------------ |
| U1               | Одобрено   | 120          | Средняя      |
| U2               | Одобрено   | 200          | Низкая       |
| U3               | Одобрено   | 80           | Средняя      |
| U6               | Предложено | 80           | Средняя      |
| U7               | Одобрено   | 70           | Высокая      |
| U8               | Предложено | 90           | Средняя      |
| U9               | Предложено | 100          | Средняя      |
| U10              | Одобрено   | 120          | Низкая       |
| N1               | Одобрено   | 100          | Высокая      |
| N3               | Одобрено   | 40           | Высокая      |
| N5               | Одобрено   | 160          | Средняя      |
| N6               | Одобрено   | 120          | Средняя      |
| N7               | Предложено | 100          | Высокая      |
| N8               | Одобрено   | 60           | Высокая      |
| N9               | Предложено | 90           | Средняя      |
| N10              | Одобрено   | 150          | Средняя      |
| N11              | Одобрено   | 150          | Средняя      |