В данном проекте представлен парсинг двух документов: 
изображения photo_2020-12-11_16-55-23.jpg и РазделПД3.Подр.ПД5_11962.pdf
Для парсинга изображения таблицы был использован tesseract и сv2. 
Cv2 использовался для распознания и последующего удаления вертикальных и горизонтальных строк.
Tesseract для оптического распознания текста. На основе парсинга создана строка сохранённая как txt.
Для парсинга доумента pdf использован Camelot для создания датафрейма на основе табличнх данных
со страницы 4.
Для распознавания и считвания текста со страницы 5 использован tika и модуль Parser.
Cтраница 5 переведена в строковый формат. Каждая строка текста из pdf записана как отдельный объект
в списке.