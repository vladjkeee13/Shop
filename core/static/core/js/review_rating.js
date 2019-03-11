 $(document).ready(function () {

    var url = "/set-rating/";

    $('.increment').click(function () {
       var data = {
           'review_id': $(this).data('id'),
           'is_increment': 1
       };
       var self = $(this);
       $.get(url, data, function () {
           var rating_element = self.next();
           var curr_val = parseInt(rating_element.text());
           rating_element.text(curr_val + 1);
       });
    });

    $('.decrement').click(function () {
       var data = {
           'review_id': $(this).data('id'),
           'is_increment': 0
       };
       var self = $(this);
       $.get(url, data, function () {
           var rating_element = self.prev();
           var curr_val = parseInt(rating_element.text());
           rating_element.text(curr_val - 1);
       });
    });

    });