from log import set_log

log = set_log.Logger('./log_record/all.log', level='info')  #
with open("./file_destination/demo1.csv", "r", encoding='UTF-8') as f:
    text = f.readlines()
    # log.logger.info(text)

for i in range(1, len(text)):  # 从第二行开始读取
    print(text[i].strip())  # .strip()去掉前后所有不可见字符
