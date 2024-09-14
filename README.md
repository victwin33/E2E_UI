# E2E_UI

## **Описание:**

Этот скрипт написан на Python и выполняет E2E тест для проверки сценария покупки товара на сайте:
https://www.saucedemo.com


### Инструкция по установке и запуску теста.

#### Клонируйте репозиторий:
1. git clone https://github.com/victwin33/E2E_UI_test.git
2. cd Е2Е_UI

##### Установите зависимости:
pip install -r requirements.txt

#### Запустите скрипт

* Установите зависимости
``` shell
pip3 install -r requirements.txt
```
* Запустить тест из директории test
```shell
pytest test --alluredir=allure_results
```
* Посмотреть отчет в веб версии пройденного прогона
``` shell
allure serve allure_results
```