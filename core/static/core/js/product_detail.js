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
    $('.add_to_cart').click(function (e) {
        e.preventDefault();
        var product_id = $(this).attr('data-id');
        var data = {
            product_id: product_id
        };
        $.ajax(
            'cart:add-to-cart',
            {
                type: "GET",
                data: data,
                success: function (data) {
                    $('#cart_count').html(data.cart_total)
                }
            })
    });
    $( "#add-t-cart-button" ).on( "click", function( event ) {
        event.preventDefault();
        var data = $("#add-to-cart-form").serialize();
         $.ajax(
            'cart:add-to-cart',
            {
                type: "GET",
                data: data,
                success: function (data) {
                    $('#cart_count').html(data.cart_total)
                }
            })
        });

    });