from bottle import get,post,run,request,template
 
 
@get("/")
def index():
    return template("index") 
#### ����� �ͻ������� ����˾ͷ���һ�� index.html ���ƽ�����ͻ���
@post("/cmd")
def cmd():
    adss=request.body.read().decode()#### ���յ� �ͻ��� ������������
    print("�����˰�ť:"+adss)
    main(adss)  #### ��ֵ�������� ʵ�ֶ�Ӧ����
    return "OK"
run(host="0.0.0.0")  #### ��������� 