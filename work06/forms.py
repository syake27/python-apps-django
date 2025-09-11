from django import forms


class reiwaform(forms.Form):
    year = forms.IntegerField(label="令和何年ですか？")


class bmiForm(forms.Form):
    height = forms.FloatField(label="身長(m)を入力してください")
    weight = forms.FloatField(label="体重(kg)を入力してください")


class warikanForm(forms.Form):
    total_amount = forms.IntegerField(label="合計金額を入力してください")
    people = forms.IntegerField(label="人数を入力してください")


class chokinFrom(forms.Form):
    chokin_amount = forms.IntegerField(label="毎月いくら貯金しますか？")


class calculatorForm(forms.Form):
    number1 = forms.FloatField(label="1つ目の数字を入力してください")
    number2 = forms.FloatField(label="2つ目の数字を入力してください")
