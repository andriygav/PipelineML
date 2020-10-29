==========
PipelineML
==========

===========
Instalation
===========
Подробная инструкция доступна на сайте <https://docs.metaflow.org/getting-started/install>`_.

Устанавка из PyPi:

.. code-block:: bash

  pip install metaflow

=======
Примеры
=======

HelloWorld
----------

Простой пример из документации <https://docs.metaflow.org/getting-started/tutorials>`_ загружен в файл `helloworld.py`.

Для отображения графа используется команда:

.. code-block:: bash

  python3.6 helloworld.py show
  
  
После выполнения получаем следующий выход, который описывает последовательность выполнения команд пайплайна:

.. code-block:: bash

  Metaflow 2.2.4 executing HelloFlow for user:andrey

  A flow where Metaflow prints 'Hi'.
  Run this flow to validate that Metaflow is installed correctly.

  Step start
      This is the 'start' step. All flows must have a step named 'start' that
      is the first step in the flow.
      => hello

  Step hello
      A step for metaflow to introduce itself.
      => end

  Step end
      This is the 'end' step. All flows must have an 'end' step, which is the
      last step in the flow.

Для запуска самого пайплайна используется следующая команда:

.. code-block:: bash

  python3.6 helloworld.py run
  
Результат данного выполения следующий:

.. code-block:: bash
  
  Metaflow 2.2.4 executing HelloFlow for user:andrey
  Validating your flow...
      The graph looks good!
  Running pylint...
      Pylint is happy!
  2020-10-29 11:32:23.236 Workflow starting (run-id 1603960343227632):
  2020-10-29 11:32:23.241 [1603960343227632/start/1 (pid 58354)] Task is starting.
  2020-10-29 11:32:23.752 [1603960343227632/start/1 (pid 58354)] HelloFlow is starting.
  2020-10-29 11:32:23.810 [1603960343227632/start/1 (pid 58354)] Task finished successfully.
  2020-10-29 11:32:23.820 [1603960343227632/hello/2 (pid 58359)] Task is starting.
  2020-10-29 11:32:24.381 [1603960343227632/hello/2 (pid 58359)] Metaflow says: Hi!
  2020-10-29 11:32:24.438 [1603960343227632/hello/2 (pid 58359)] Task finished successfully.
  2020-10-29 11:32:24.444 [1603960343227632/end/3 (pid 58364)] Task is starting.
  2020-10-29 11:32:24.952 [1603960343227632/end/3 (pid 58364)] HelloFlow is all done.
  2020-10-29 11:32:25.006 [1603960343227632/end/3 (pid 58364)] Task finished successfully.
  2020-10-29 11:32:25.007 Done!

Как видно, в логах доступна вся информация о том, что происходит с пайплайном выполнения.


LinearModel
-----------

В качестве примера использования mataflow для машинного обучения примеду пример подбора гиперапараметров для линейной модели. Пример представлен в файле `linear.py`.

Сначала рассмотрим наш сам граф вычислений:

.. code-block:: bash

  python3.6 linear.py show
  
.. code-block:: bash

  Metaflow 2.2.4 executing LinearModelFlow for user:andrey

  Попытка создать пайплайн для обучения линейной модели с подбором гиперпараметров.

  Step start
      Здесь мы генерим синтетические данные, но можно можно и загружать с файла
      => model

  Step model
      Определяем гиперпараметры модели
      => model_fit

  Step model_fit
      Обучаем модель
      => join

  Step join
      Объединяем результаты разных моделек
      => end

  Step end
      Конец обучения

Видим, что наша модель состоит из нескольких этапов:
- Загрузка данных (start)
- Задание гиперпараметров модели, которые нужно перебрать (model)
- Обучение модели для разных гиперпараметров (model fit)
- Объединение результатов разных моделей, и выбор лучшей модели (join)
- Вывод результата (end)
  
Теперь рассмотрим как выглядит сам процесс выполнения:

.. code-block:: bash
  
  python3.6 linear.py run
  
.. code-block:: bash
  
  Metaflow 2.2.4 executing LinearModelFlow for user:andrey
  Validating your flow...
      The graph looks good!
  Running pylint...
      Pylint is happy!
  2020-10-29 11:40:11.557 Workflow starting (run-id 1603960811550605):
  2020-10-29 11:40:11.564 [1603960811550605/start/1 (pid 59920)] Task is starting.
  2020-10-29 11:40:13.843 [1603960811550605/start/1 (pid 59920)] Task finished successfully.
  2020-10-29 11:40:13.852 [1603960811550605/model/2 (pid 59931)] Task is starting.
  2020-10-29 11:40:15.068 [1603960811550605/model/2 (pid 59931)] Foreach yields 10 child steps.
  2020-10-29 11:40:15.068 [1603960811550605/model/2 (pid 59931)] Task finished successfully.
  2020-10-29 11:40:15.076 [1603960811550605/model_fit/3 (pid 59942)] Task is starting.
  2020-10-29 11:40:15.082 [1603960811550605/model_fit/4 (pid 59943)] Task is starting.
  2020-10-29 11:40:15.088 [1603960811550605/model_fit/5 (pid 59944)] Task is starting.
  2020-10-29 11:40:15.096 [1603960811550605/model_fit/6 (pid 59945)] Task is starting.
  2020-10-29 11:40:15.107 [1603960811550605/model_fit/7 (pid 59946)] Task is starting.
  2020-10-29 11:40:15.115 [1603960811550605/model_fit/8 (pid 59947)] Task is starting.
  2020-10-29 11:40:15.122 [1603960811550605/model_fit/9 (pid 59948)] Task is starting.
  2020-10-29 11:40:15.128 [1603960811550605/model_fit/10 (pid 59949)] Task is starting.
  2020-10-29 11:40:15.134 [1603960811550605/model_fit/11 (pid 59950)] Task is starting.
  2020-10-29 11:40:15.140 [1603960811550605/model_fit/12 (pid 59951)] Task is starting.
  2020-10-29 11:40:19.755 [1603960811550605/model_fit/8 (pid 59947)] fit model with C=1.395612425086089
  2020-10-29 11:40:19.836 [1603960811550605/model_fit/10 (pid 59949)] fit model with C=5.294490050470026
  2020-10-29 11:40:19.862 [1603960811550605/model_fit/9 (pid 59948)] fit model with C=2.718281828459045
  2020-10-29 11:40:19.892 [1603960811550605/model_fit/11 (pid 59950)] fit model with C=10.312258501325761
  2020-10-29 11:40:19.913 [1603960811550605/model_fit/7 (pid 59946)] fit model with C=0.7165313105737892
  2020-10-29 11:40:19.921 [1603960811550605/model_fit/5 (pid 59944)] fit model with C=0.18887560283756183
  2020-10-29 11:40:19.925 [1603960811550605/model_fit/12 (pid 59951)] fit model with C=20.085536923187664
  2020-10-29 11:40:19.956 [1603960811550605/model_fit/6 (pid 59945)] fit model with C=0.36787944117144233
  2020-10-29 11:40:20.099 [1603960811550605/model_fit/3 (pid 59942)] fit model with C=0.04978706836786395
  2020-10-29 11:40:20.108 [1603960811550605/model_fit/4 (pid 59943)] fit model with C=0.09697196786440505
  2020-10-29 11:40:20.400 [1603960811550605/model_fit/10 (pid 59949)] Task finished successfully.
  2020-10-29 11:40:20.425 [1603960811550605/model_fit/8 (pid 59947)] Task finished successfully.
  2020-10-29 11:40:20.452 [1603960811550605/model_fit/7 (pid 59946)] Task finished successfully.
  2020-10-29 11:40:20.475 [1603960811550605/model_fit/11 (pid 59950)] Task finished successfully.
  2020-10-29 11:40:20.484 [1603960811550605/model_fit/9 (pid 59948)] Task finished successfully.
  2020-10-29 11:40:20.500 [1603960811550605/model_fit/5 (pid 59944)] Task finished successfully.
  2020-10-29 11:40:20.509 [1603960811550605/model_fit/12 (pid 59951)] Task finished successfully.
  2020-10-29 11:40:20.533 [1603960811550605/model_fit/6 (pid 59945)] Task finished successfully.
  2020-10-29 11:40:20.560 [1603960811550605/model_fit/3 (pid 59942)] Task finished successfully.
  2020-10-29 11:40:20.564 [1603960811550605/model_fit/4 (pid 59943)] Task finished successfully.
  2020-10-29 11:40:20.571 [1603960811550605/join/13 (pid 60005)] Task is starting.
  2020-10-29 11:40:21.871 [1603960811550605/join/13 (pid 60005)] Task finished successfully.
  2020-10-29 11:40:21.878 [1603960811550605/end/14 (pid 60016)] Task is starting.
  2020-10-29 11:40:22.997 [1603960811550605/end/14 (pid 60016)] {'C=0.04978706836786395': {'score': 0.82}, 'C=0.09697196786440505': {'score': 0.82}, 'C=0.18887560283756183': {'score': 0.82}, 'C=0.36787944117144233': {'score': 0.82}, 'C=0.7165313105737892': {'score': 0.82}, 'C=1.395612425086089': {'score': 0.82}, 'C=2.718281828459045': {'score': 0.82}, 'C=5.294490050470026': {'score': 0.82}, 'C=10.312258501325761': {'score': 0.82}, 'C=20.085536923187664': {'score': 0.82}}
  2020-10-29 11:40:23.308 [1603960811550605/end/14 (pid 60016)] Task finished successfully.
  2020-10-29 11:40:23.309 Done!

