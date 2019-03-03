import re

from django import forms

from product.models import Comment


# class AddReviewForm(forms.Form):
#     text = forms.CharField(widget=forms.widgets.Textarea(attrs={'class': 'textarea', 'rows': 8}), required=True)
#
#     def save(self, user, product, parent):
#         comment = Comment.objects.create(
#             text=self.cleaned_data['text'],
#             author=user,
#             product=product,
#             parent=parent
#         )
#         return comment

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
