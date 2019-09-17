from django import forms

class contact(forms.Form):

    name = forms.CharField(widget = forms.TextInput(attrs = {
       'placeholder' : 'Name *',
        'name' : 'name',
        'class' : 'form-control mb-30',
    }))
    email = forms.EmailField(widget = forms.EmailInput(attrs = {
        'placeholder' : 'Email *',
        'name' : 'email',
        'class' : 'form-control mb-30',
    }))

    phone = forms.CharField(widget = forms.TextInput(attrs = {
        'placeholder' : 'Phone',
        'name' : 'phone',
        'class' : 'form-control mb-30',
    }),required = False)

    organization = forms.CharField(widget = forms.TextInput(attrs = {
        'placeholder' : 'Organization',
        'name' : 'organization',
        'class' : 'form-control mb-30',
    }),required = False)

    message = forms.CharField(widget = forms.Textarea(attrs = {
        'placeholder' : 'Message *',
        'name' : 'message',
        'class' : 'form-control mb-30',
        'rows' : '8',
        'cols' : '80',
    }))

    plan = forms.CharField(widget = forms.TextInput(attrs = {
        'placeholder' : 'Plan (Check pricing)',
        'name' : 'plan',
        'class' : 'form-control mb-30',
    }),required = False)

    ref_code = forms.CharField(widget = forms.TextInput(attrs = {
        'required' : False,
        'placeholder' : 'Refferral Code',
        'name' : 'ref_code',
        'class' : 'form-control mb-30',
    }),required = False)


class par_reg(forms.Form):

    name = forms.CharField(widget = forms.TextInput(attrs = {
       'placeholder' : 'Name',
        'name' : 'name',
        'class' : 'form-control mb-30',
    }))

    email = forms.EmailField(widget = forms.EmailInput(attrs = {
        'placeholder' : 'Email',
        'name' : 'email',
        'class' : 'form-control mb-30',
    }))

    phone = forms.CharField(widget = forms.TextInput(attrs = {
        'placeholder' : 'Phone or mobile number for contact ',
        'name' : 'phone',
        'class' : 'form-control mb-30',
    }))

    mobile = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Mobile number (for receiving payments through google pay)',
        'name': 'mobile',
        'class': 'form-control mb-30',
    }))

    platform = forms.CharField(widget = forms.TextInput(attrs = {
        'placeholder' : 'ex. Youtube , Instagram, facebook',
        'name' : 'platform',
        'class' : 'form-control mb-30',
    }))

    user_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'User name or channel name',
        'name': 'user_name',
        'class': 'form-control mb-30',
    }))



    audience_num = forms.CharField(widget = forms.TextInput(attrs = {
        'placeholder' : 'Number of subscribers or followers',
        'name' : 'audience_num',
        'class' : 'form-control mb-30',
    }))

    link = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'link of channel or account',
        'name': 'link',
        'class': 'form-control mb-30',
    }))


    message = forms.CharField(widget = forms.Textarea(attrs = {
        'placeholder' : 'Want to tell us someting?',
        'name' : 'message',
        'class' : 'form-control mb-30',
        'rows' : '8',
        'cols' : '80',
    }),required = False)