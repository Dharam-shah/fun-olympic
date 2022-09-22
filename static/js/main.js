(function ($) {
    $(document).ready(function () {

        $('[data-fancybox]').fancybox();

        // $(window).scroll(function () {
        //     var scrollTop = $(window).scrollTop();
        //     var headerHeight = $('.site-header').innerHeight();
        //     if (scrollTop > headerHeight) {
        //         $('.site-header').addClass('sticky-header')
        //     } else {
        //         $('.site-header').removeClass('sticky-header');
        //     }
        // });

        // slider-col-1
        $(".slider-col-1").slick({
            dots: true,
            arrows: false,
            infinite: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 3000,
            adaptiveHeight: true,
        });

        // slider-col-4
        $(".slider-col-4").slick({
            dots: false,
            arrows: true,
            infinite: false,
            slidesToShow: 4,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 3000,
            responsive: [{
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 3,
                    },
                },
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 1,
                        adaptiveHeight: true,
                    },
                },
            ],
        });

    });
}(jQuery));