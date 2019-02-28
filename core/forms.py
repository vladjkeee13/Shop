from django import forms

from product.models import Comment


class AddReviewForm(forms.Form):
    text = forms.CharField(widget=forms.widgets.Textarea(attrs={'class': 'textarea', 'rows': 8}), required=True)

    def save(self, user):
        comment = Comment.objects.create(
            text=self.cleaned_data['text'],
            author=user
        )
        return comment
