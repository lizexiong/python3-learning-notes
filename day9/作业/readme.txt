day9���������ļ���

day9_work1_select.py
����˵����
    select ��socketserver����ϸ����˵���ļ���


day9_wrok2_salt
�����ܣ�
    ģ��saltstack����Զ��ִ�� ������ؽ���� Զ��ִ���ļ��ϴ�������

����ִ�����
1�� Զ��ִ������
    salts.py  web_server cmd.run "df -hl"
    args:
        web_server   ������������, �����з�������������ʹ��  \*
        cmd.run       ִ��cmd����ģ��
2:  Զ��ִ���ļ��ϴ�������
    salts.py  web_server  ftp.run httpd
    args:
         web_server    ������������
         ftp.run          ִ�е�ftpģ��
         httpd            package��
         
����Ŀ¼�ṹ��
ay9_work2_salt/
������ conf                                 ����Ŀ¼
��   ������ hosts.yaml                      ���������ļ���Ϣ
��   ������ settings.py                      ϵͳ�����ļ�
������ file_source                       �ϴ������ļ�Ŀ¼
��   ������ httpd.conf                      
��   ������ my.cnf
������ logs                                 ϵͳ��־Ŀ¼
��   ������ syslog.log                        ϵͳ��־
������ module                            ģ��Ŀ¼
��   ������ common.py                     ����ģ��
��   ������ parser.py                          ymal�ļ�����ģ��
������ package                          �ϴ��������ð�Ŀ¼
��   ������ httpd.sls                           
��   ������ mysql.sls
������ salts.py                            ϵͳ�������ļ�
������ script                               �����ģ��Ŀ¼
��   ������ cmd.py                            ִ������ģ��   cmd.run
��   ������ ftp.py                              �ļ����� ģ��  ftp.run
������ sshkey                             ��Կ���Ŀ¼
    ������ id_rsa
    ������ id_rsa.pub
