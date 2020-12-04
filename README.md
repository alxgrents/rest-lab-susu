### Лабораторная работа по предмету "Введение в сервис-ориентированные архитектуры"
### 5. Приложение на основе REST


#### Цель

Вам необходимо разработать REST API и клиента для текстовой Online-RPG «Valar Morghulis» («VM») по мотивам «Игры Престолов».

#### Задание: разработать REST-сервис (и клиента для него) для игры «Valar Morghulis» («VM»). Прототип сервиса игры должен поддерживать предоставление и редактирование следующей информации: 

<p>Player – персонаж игры:
  
- id – уникальный идентификатор персонажа (int);
- name – Имя персонажа (не более 30 символов);
- playerclass – Класс персонажа (Knight, Wizard, Thief, Paladin);
- email;
- level – уровень персонажа;
- position – положение персонажа на карте (идентификатор локации).</p>
<p>ItemType - виды предметов в игре:

- id - уникальный идентификатор ItemType (INT);
- name - название ItemType (меч, шлем ...);</p>
<p>Item - отдельные предметы в игре, принадлежащие игрокам:

- itemType - тип элемента;
- quality - качество предмета (100 - идеальное, 0 - сломан);
- owner - игрок-владелец предмета.</p>
<p>Location – локация в игре

- locationId – краткое название-идентификатор локации (не более 10 символов)
- description – текст с описанием локации
- locationType – тип локации (Forest, Desert, Dungeon, River, Ocean)</p>
<p>Messages – сообщения между игроками

- messageId – идентификатор сообщения;
- playerFrom – игрок, отправивший сообщение;
- playerTo – игрок, получивший сообщение;
messageText – текст сообщения (не более 1000 символов).</p>
