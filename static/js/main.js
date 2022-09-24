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

        // let loadMoreBtn = document.querySelector('#load-more');
        // let currentItem = 4;

        // loadMoreBtn.onclick = () => {
        //     let boxes = [...document.querySelectorAll('.card-video__block [class^="col-"]')];
        //     for (var i = currentItem; i < currentItem + 4; i++) {
        //         boxes[i].style.display = 'inline-block';
        //     }
        //     currentItem += 4;

        //     if (currentItem >= boxes.length) {
        //         loadMoreBtn.style.display = 'none';
        //     }
        // }

        var loadMore = document.querySelector('.load-more');

        var currentItem = 4;
        loadMore.addEventListener('click', (e) => {
            var boxes = [...document.querySelectorAll('.card-video__block [class^="col-"]')];
            e.target.classList.add('show-loader');

            for (let i = currentItem; i < currentItem + 4; i++) {
                setTimeout(function time() {
                    e.target.classList.remove('show-loader');
                    if (boxes[i]) {
                        boxes[i].style.display = 'block';
                    }
                }, 3000);
            }
            currentItem += 4;

            if (currentItem >= boxes.length) {
                event.target.classList.add('loaded');
            }
        });

    });
}(jQuery));