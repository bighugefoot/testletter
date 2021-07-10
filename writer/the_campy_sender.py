import thecampy

User_Id = "judacompany.email@gmail.com"
User_Passward = 'q1w2e3r4!'
my_soldier = thecampy.Soldier('이동준',20010624,20210614, '12사단')
def send(작성자, 제목, 내용 ) :
        real_title= "작성자이름:"+ 작성자 +","+"제목:"+제목
        msg = thecampy.Message(real_title, 내용)
        tc = thecampy.client()
        tc.login(User_Id, User_Passward)
        tc.get_soldier(my_soldier)

        tc.send_message(my_soldier, msg)