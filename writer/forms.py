from django import forms
from writer.models import 인편


#https://dev-yakuza.posstree.com/ko/django/form/
class 인편작성폼(forms.ModelForm):
    class Meta:
        model = 인편
        fields = ('작성자', '제목', '내용')



