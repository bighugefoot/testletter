import thecampy

User_Id = "yjd9200@naver.com"
User_Passward = 'yjd9200!@'
my_soldier = thecampy.Soldier('유재덕',20000410,20210706, '5사단')
def send(작성자, 제목, 내용 ) :
        real_title= "작성자이름:"+ 작성자 +","+"제목:"+제목
        msg = thecampy.Message(real_title, 내용)
        tc = thecampy.client()
        tc.login(User_Id, User_Passward)
        tc.get_soldier(my_soldier)

        tc.send_message(my_soldier, msg)