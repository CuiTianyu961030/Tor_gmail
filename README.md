# Tor_gmail
## 使用说明
###注意事项
由于Tor只返回riseup、gmail、yohoo邮箱邮件，脚本需要使用gmail邮箱。
Gmail邮箱设置开启IMAP和STMP服务后运行脚本。运行脚本时需输入gmail邮箱的账号和密码。向bridges@torproject.org发送的次数不能太频繁，否则会收到3小时后才能再发的邮件提醒。

### 运行说明

* Tor_send_gmail.py为向bridges@torproject.org发送邮件的脚本，运行时依次输入gmail邮箱的账号和密码。Gmail邮箱会自动向bridges@torproject.org发送一封主题为get bridges，内容也为get bridges的邮件。之后gmail邮箱会自动收到bridges@torproject.org返回的邮件。


* Tor_recieve_gmail.py为从gmail邮箱中读取收件箱内最新的邮件内容，运行时需在Tor_send_gmail.py执行完后再执行，并依次输入gmail邮箱的账号和密码，获取得到mailfile文件，包含邮件的具体内容。
