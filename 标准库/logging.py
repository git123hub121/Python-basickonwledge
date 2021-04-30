import	os
import	platform
import	logging
if	platform.platform().startswith('Windows'):
    logging_file	=	os.path.join(os.getenv('HOMEDRIVE'),
                                      os.getenv('HOMEPATH'),
                                      'test.log')
else:
    logging_file	=	os.path.join(os.getenv('HOME'),
                                      'test.log')

print("Logging	to",	logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s	:	%(levelname)s	:	%(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start	of	the	program")
logging.info("Doing	something")
logging.warning("Dying	now")

# os模块用以和操作系统交互
# platform模块用以获取平台——操作系统——的信息
# logging模块用来记录（Log）信息