# mask the email_id given except first end last characters and replace the rest with * and return the masked email_id

from loguru import logger

email_id = "rohitkumar87@gmail.com"
logger.info(email_id)

email_head = email_id.split("@")[0]
email_tail = email_id.split("@")[1]

new_email_head = ""
logger.info(email_head[-1])

# for char in email_head:
#     if char == email_head[0] or char == email_head[-1]:
#         new_email_head = new_email_head + char        
#         logger.info(char)
#     else:
#         new_email_head = new_email_head + "*"
#         # logger.info(char)

for i in range(len(email_head)):
    if i == 0 or i == len(email_head) - 1:
        new_email_head = new_email_head + email_head[i]
    else:
        new_email_head = new_email_head + "*"

new_email_id = new_email_head + "@" + email_tail

logger.info(new_email_id)


