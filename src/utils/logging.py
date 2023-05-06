import logging

# 로그 찍을 때 필요한 함수
def log():

    # logger 생성
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)


    # handler 생성
    handler = logging.FileHandler("info_log")
    handler.setLevel(logging.INFO)

    # formatter 생성
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # logger에 handler 추가
    logger.addHandler(handler)

    return logger