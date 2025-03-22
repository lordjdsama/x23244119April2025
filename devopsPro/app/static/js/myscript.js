$(document).ready(function () {
    // Plus button
    $('.plus-cart').click(function () {
        var id = $(this).attr("pid").toString();
        var $this = $(this);

        $.ajax({
            type: "GET",
            url: "/pluscart/",
            data: {
                prod_id: id
            },
            success: function (data) {
                $this.closest("div.my-3").find("span#quantity").text(data.quantity);
                $('#amount').text("Rs. " + data.amount);
                $('#totalamount').text("Rs. " + data.totalamount);
            }
        });
    });

    // Minus button
    $('.minus-cart').click(function () {
        var id = $(this).attr("pid").toString();
        var $this = $(this);

        $.ajax({
            type: "GET",
            url: "/minuscart/",
            data: {
                prod_id: id
            },
            success: function (data) {
                $this.closest("div.my-3").find("span#quantity").text(data.quantity);
                $('#amount').text("Rs. " + data.amount);
                $('#totalamount').text("Rs. " + data.totalamount);
            }
        });
    });
    
    $('.remove-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var $this = $(this);

    $.ajax({
        type: "GET",
        url: "/removecart/",
        data: {
            prod_id: id
        },
        success: function (data) {
            $this.closest(".row").remove(); // Remove the cart item block
            $('#amount').text("Rs. " + data.amount);
            $('#totalamount').text("Rs. " + data.totalamount);
        }
    });
});

});
