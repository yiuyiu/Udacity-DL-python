# coding=utf-8
import media #引入电影类
titanic = media.Movie('TITANIC','https://img3.doubanio.com/view/photo/l/public/p457760035.webp',\
                      'https://www.youtube.com/watch?v=CHekzSiZjrY') 
farewell_to_my_concubine = media.Movie('Farewell to My Concubine',\
                      'https://img3.doubanio.com/view/photo/l/public/p1910813120.webp',\
                      'https://www.youtube.com/watch?v=cC-_SLiRnJE')
the_last_emperor = media.Movie('The Last Emperor',\
                      'https://img3.doubanio.com/view/photo/l/public/p452088641.webp',\
                      'https://www.youtube.com/watch?v=A4cH6g1wD5g')
movies = [titanic,farewell_to_my_concubine,the_last_emperor]

import fresh_tomatoes #引入电影页模板
fresh_tomatoes.open_movies_page(movies)