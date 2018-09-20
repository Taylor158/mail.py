# mail.py
from email.mime.text import Mi
import smtplib
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
