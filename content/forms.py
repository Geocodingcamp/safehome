from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

class ForRentForm(forms.Form):
    mobile = forms.IntegerField(required=True)
    myhomelink = forms.URLField(required=True)
    myhomeid = forms.IntegerField(required=True)
    sslink = forms.URLField(required=True)
    ssid = forms.IntegerField(required=True)
    area = forms.IntegerField(required=True)
    price = forms.IntegerField(required=True)
    address = forms.CharField(required=True)
    limitations = forms.CharField(required=True)

class ForSaleForm(forms.Form):
    mobile = forms.IntegerField(required=True)
    myhomelink = forms.URLField(required=True)
    myhomeid = forms.IntegerField(required=True)
    sslink = forms.URLField(required=True)
    ssid = forms.IntegerField(required=True)
    area = forms.IntegerField(required=True)
    price = forms.IntegerField(required=True)
    percentage = forms.IntegerField(required=True)
    address = forms.CharField(required=True)