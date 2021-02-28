import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from auto_gfw import generate_vmess


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'chengshuai232052@163.com'
password = '05545714184'
smtp_server = 'smtp.163.com'
to_addr = '1486361198@qq.com'

#mail_context = '''
#<html><body><h1>{0}</h1>
#<p>send by <a href="http://www.python.org">Python</a></p>
#</body></html>
#'''.format(generate_vmess())


msg = MIMEText(generate_vmess(), 'plain', 'utf-8')
msg['From'] = _format_addr('Raspberry Robot <%s>' % from_addr)
msg['To'] = _format_addr('1486361198 <%s>' % to_addr)
msg['Subject'] = Header('iShadow', 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25)
#server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
