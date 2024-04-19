import pywhatkit
from datetime import datetime

today = datetime.now()

phone_number = '+5516992210406'
group = 'Hegk6ZpOcI0E3ptoCj9c40'
waiting_time_to_send = 15
close_tab = True
waiting_time_to_close = 5

pywhatkit.sendwhatmsg_to_group_instantly(group, "teste", waiting_time_to_send, close_tab,
                                         waiting_time_to_close)
