from django.db.models import F
from django.http import JsonResponse
from django.views import View

from product.models import Comment


class RatingView(View):

    def get(self, request):

        review_id = request.GET['review_id']
        is_increment = int(request.GET['is_increment'])

        if is_increment:
            Comment.comment_manager.filter(id=review_id).update(rating=F('rating') + 1)
        else:
            Comment.comment_manager.filter(id=review_id).update(rating=F('rating') - 1)

        return JsonResponse({'status': 'success'})

