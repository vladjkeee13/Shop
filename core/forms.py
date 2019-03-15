import re

from django import forms

from core.models import MyUser
from product.models import Comment


class AddReviewForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.widgets.Textarea(attrs={'class': 'textarea', 'rows': 8})
        }

    def clean_text(self):
        text = self.cleaned_data['text']
        if not re.match(r'([A-z]+)|([0-9]+)', text):
            raise forms.ValidationError('Please, use only English language!')
        return text

    def save(self, *args, **kwargs):

        user = kwargs.pop('user')
        product = kwargs.pop('product')
        parent = kwargs.pop('parent')

        comment = super(AddReviewForm, self).save(commit=False)

        comment.author = user
        comment.product = product
        comment.parent = parent
        comment.save()

        return comment


class SearchForm(forms.Form):

    name = forms.CharField(required=False)
    lowest_price = forms.DecimalField(max_digits=9, decimal_places=2, required=False)
    highest_price = forms.DecimalField(max_digits=9, decimal_places=2, required=False)

    def _filter_by_name(self, queryset):
        return queryset.filter(name__icontains=self.cleaned_data['name'])

    def _filter_by_lowest_price(self, queryset):
        return queryset.filter(price__lte=self.cleaned_data['lowest_price'])

    def _filter_by_highest_price(self, queryset):
        return queryset.filter(price__gte=self.cleaned_data['highest_price'])

    def get_search_queryset(self, queryset):

        for field_name in self.fields:
            if field_name in self.cleaned_data and self.cleaned_data[field_name]:
                queryset = getattr(self, f'_filter_by_{field_name}')(queryset)

        return queryset


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'password_check', 'first_name', 'last_name', 'phone', 'email', 'avatar')

    def clean(self):

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']
        email = self.cleaned_data['email']

        if MyUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Юзер с таим именем уже зарегестрирован')

        if password != password_check:
            raise forms.ValidationError('Пароли не совпадают')

        if MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким емаилом уже зарегестрирован!')


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not MyUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким логином не зарегестрирован в системе!')

        user = MyUser.objects.get(username=username)

        if user and not user.check_password(password):
            raise forms.ValidationError('Неверный пароль!')
