from django.core.management.base import BaseCommand

from urllib.request import urlopen

from bs4 import BeautifulSoup


from timetable.models import TimeTable

class Command(BaseCommand):
    help = "collect timetable"   

    # определяем логику команд
    def handle(self, *args, **options):

        # собираем html
        html = urlopen('https://www.tripadvisor.ru/RestaurantsNear-g294448-d318808-Minsk_Sea-Minsk.html')
        # преобразуем в soup-объект
        soup = BeautifulSoup(html, 'html.parser')
        

        # собираем все посты
        posts = soup.find_all('div', class_= 'near_listing')
        
       
        
        for d in posts:
            #url = d.find('a', class_='Link_colors_inherit').text
            
            title = d.find('div', class_='location_name').text   # check if url in db
            address = d.find('span', class_= 'format_address').text
            #pictureRest=d.find()
            

            
            try:
                # сохраняем в базе данных
                TimeTable.objects.create(
                    #url=url,
                   title=title,
                    address=address)
                print('%s added' % (title,))
            except:
                print('%s already exists' % (title,))

        self.stdout.write( 'timetable complete' )

        

        
        

        