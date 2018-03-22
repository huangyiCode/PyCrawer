from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# from address
from_addr = '18392974435@163.com'

from_addr_pwd = 'huangyi111'

to_addr = '978140188@qq.com'

smtp_server = 'smtp.163.com'
# Don't replay!..Don't replay!..Don't replay!
msg = MIMEText('Don\'t reply!..Don\'t reply!..Don\'t reply!', 'plain', 'utf-8')
msg['From'] = _format_addr('Three body<%s>' % from_addr)
msg['To'] = _format_addr('Manager<%s>' % to_addr)
msg['Subject'] = Header('Received MSG', 'utf-8').encode()

# Send MSG

server = smtplib.SMTP(smtp_server, 25)
server.login(from_addr, from_addr_pwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
