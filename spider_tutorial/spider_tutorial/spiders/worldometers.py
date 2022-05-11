import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    #Permite dominios con la raiz
    allowed_domains = ['www.worldometers.info/']
    #link de la pagina inicio del scrapy
    start_urls = ['http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        titulo = response.xpath('//h1/text()').get()
        paises = response.xpath('//td/a/text()').getall()

        # return sin destruir las variables locales de una función
        yield{
            'titulo':titulo,
            'paises': paises,

        }
