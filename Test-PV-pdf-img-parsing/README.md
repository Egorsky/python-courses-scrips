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
-------
This project provides parsing of two documents:
images photo_2020-12-11_16-55-23.jpg and Section PD3.Advanced PD5_11962.pdf
Tesseract and cv2 were used to parse the table image.
Cv2 was used to recognize and then remove vertical and horizontal lines.
Tesseract for optical text recognition. Based on the parsing, a string was created, saved as txt.
Camelot was used for parsing the pdf document to create a dataframe based on tabular data
from page 4.
To recognize and read text from page 5, tika and the Parser module are used.
Page 5 has been converted to string format. Each line of text from pdf is written as a separate object
on the list.
