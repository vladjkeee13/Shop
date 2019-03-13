import re

from django import forms

from product.models import Comment, Category


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
        print(self.cleaned_data['category'])
        for field_name in self.fields:
            if field_name in self.cleaned_data and self.cleaned_data[field_name]:
                queryset = getattr(self, f'_filter_by_{field_name}')(queryset)

        return queryset
