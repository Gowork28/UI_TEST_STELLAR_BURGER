# Тестирование UI для сервиса Stellar Burger

Stellar Burger - это космический сервис онлайн - заказа бургера. 
Можно выбрать булку, начинку и соус. После оформления заказа пользователь получает номер заказа. 

В этом проекте реализованы автоматизированные UI тесты для функций сервиса Stellar Buger. Проверки проходили с помощью сравнения с макетами.

## Проверенные функции

- **Переходы по клику** - проверка корректности переходов по клику на разделы Конструктор и Лента Заказов  
- **Всплывающее окно ингрекдиента** - проверка открытия и закрытия окна с деталями ингредиента
- **Cчётчик ингредиента** - проверка увеличения счётчика при добавлении ингредиента в заказ
- **Счётчики количетсва заказов** - проверка увеличения счётчиков Выполнено за всё время и Выполнено за сегодня при создании нового заказа
- **Раздел В работе** - проверка отображения номера заказа в разделе В работе после его оформления

## Стек:
<div align="left">
  <img src="https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white" alt="PyCharm"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/DevTools-FF6C37?style=for-the-badge&logo=googlechrome&logoColor=white" alt="DevTools"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS"/>
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium"/>
  <img src="https://img.shields.io/badge/Allure-FF8C00?style=for-the-badge&logo=allure&logoColor=white" alt="Allure"/>
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest"/>
</div>

## Инструкция по запуску:

1. Установите зависимости:
pip install -r requirements.txt

2. Запустить все тесты и записать отчет:
pytest tests --alluredir=allure_results

3. Посмотреть отчет по прогону html
allure serve allure_results
