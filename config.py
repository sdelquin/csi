import os

EDITIONS = {
    '2015': {
        'EVENT_DATETIME': '14/11/2015T21:00',
        'DAYS_TO_SIGNUP': 10,
        'EMBEDMAP_SRC': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1\
d3506.6425042707415!2d-16.321722999999995!3d28.490310999999995!2m3!1f0!2f0!3f0\
!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xc41cc578c377601%3A0x77541f49aeeb2ba6!2sRe\
staurante+El+Esquinazo!5e0!3m2!1ses!2ses!4v1524158792823',
    },
    '2016': {
        'EVENT_DATETIME': '19/11/2016T21:00',
        'DAYS_TO_SIGNUP': 10,
        'EMBEDMAP_SRC': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1\
d876.6589320132223!2d-16.323250170802883!3d28.49051499890464!2m3!1f0!2f0!3f0!3\
m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xc41cdc0281494ef%3A0x49044255fdfe2584!2sStef\
anos+la+Laguna!5e0!3m2!1ses!2ses!4v1477222434193'
    },
    '2017': {
        'EVENT_DATETIME': '1/12/2017T21:30',
        'DAYS_TO_SIGNUP': 10,
        'EMBEDMAP_SRC': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1\
d3506.74496976701!2d-16.315167300000002!3d28.4872261!2m3!1f0!2f0!3f0!3m2!1i102\
4!2i768!4f13.1!3m3!1m2!1s0xc41cdb8ecfcdfef%3A0xa8b007bc2f9ce09!2sLa+Tasca+de+A\
rana!5e0!3m2!1ses!2ses!4v1534508486248'
    }
}

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DATAFILE = os.path.join(BASE_PATH, 'data/assistants_{}.csv')
