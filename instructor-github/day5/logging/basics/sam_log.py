import logging 


fmt = "%(asctime)s %(filename)s : %(message)s    -- from : %(name)s"
logging.basicConfig(level=logging.DEBUG, filename = 'app.log', format=fmt)

l = logging.getLogger('colruyt '+__file__)



l.debug('a note for debug')
l.info('a note for info')
l.warning('a note for warn')



