/*------------------------------------*\
    Custom JavaScript
\*------------------------------------*/
(function($) {
    "use strict";
    $(window).load(function() {
        /* -------------------------------------------------------------
            Preloader
        ------------------------------------------------------------- */
        if ($('.preloader').length){
            $(".loader-inner,.loader-logo").fadeOut();
            $(".preloader").delay(300).fadeOut("slow");
        }


        /* -------------------------------------------------------------
            Animation for Elements
        ------------------------------------------------------------- */
        $('[data-animation]').each(function() {
            var anime = $(this);
            anime.addClass('animated');
            anime.waypoint(function() {
                anime.addClass(anime.data('animation'));
                anime.addClass('visible');
            }, {
                triggerOnce: true,
                offset: '90%'
            });
        });
    })


    $(document).ready(function() {

        /* -------------------------------------------------------------
            Curency Dripdown
        ------------------------------------------------------------- */
        $('.language-dropdown #lang_sel > ul > li:has(ul) > a,.currency-dropdown ul.wcml_currency_switcher li:first-child').append('<span class="caret"></span>');

        /* -------------------------------------------------------------
            Revolution Slider
        ------------------------------------------------------------- */
        if ($('#rev_slider').length){
            $("#rev_slider").revolution({
                sliderType: "standard",
                sliderLayout: "fullscreen",
                fullScreenOffsetContainer: ".redchili-top",
                responsiveLevels: [1240, 1024, 778, 480],
                gridwidth: [1240, 1024, 778, 480],
                gridheight: [868, 768, 960, 720],
                delay: 9000,
                spinner: "off",
                navigation : {
                    bullets:{
                        style:"",
                        enable:true,
                        hide_onleave:false,
                        tmp:'',      
                        h_align:"center",
                        v_align:"bottom",
                        h_offset:0,
                        v_offset:30,
                        space:14,
                    }
                }
            });
        }

        
        /* -------------------------------------------------------------
            Mega Menu Dropdown
        ------------------------------------------------------------- */
        $('#main-navbar .dropdown').on('mouseenter',function(){
             $(this).find('.dropdown-menu').first().stop(true, true).delay(300).slideDown();
        });
        $('#main-navbar .dropdown').on('mouseleave',function(){
             $(this).find('.dropdown-menu').first().stop(true, true).delay(100).slideUp();
        });

        
        /* -------------------------------------------------------------
            Search Form
        ------------------------------------------------------------- */
        $(".search-open").on('click', function(){
            $("#search-form").fadeToggle("slow", "linear");
        });
        $('body').on('click', function(event) {
            if (!$(event.target).closest('.search-open').length && !$(event.target).closest('#search-form').length) {
                $("#search-form").fadeOut("slow");
            }
        });

        $(".search-open2").on('click', function(){
            $("#search-form2").fadeToggle("slow", "linear");
        });
        $('body').on('click', function(event) {
            if (!$(event.target).closest('.search-open2').length && !$(event.target).closest('#search-form2').length) {
                $("#search-form2").fadeOut("slow");
            }
        });
        /* -------------------------------------------------------------
            Home Image Gallery Popup
        ------------------------------------------------------------- */
        if ($('.gallery-img').length){
            $('.gallery-img').magnificPopup({
                delegate: 'a',
                type: 'image',
                gallery: { enabled: true },
                removalDelay: 500,
                callbacks: {
                    beforeOpen: function() {
                        this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
                        this.st.mainClass = this.st.el.attr('data-effect');
                    }
                },
                closeOnContentClick: true,
                midClick: true
            });
        }
        /* -------------------------------------------------------------
            Home Latest Blog Same Height 
        ------------------------------------------------------------- */
        if($('.redchili-latestblog').width() > 767){
            var highestLatestBlog = 0;
            $('.latest-blog',this).each(function(){
                if($(this).height() > highestLatestBlog) {
                    highestLatestBlog = $(this).height()+1; 
                }

            })
            $('.latest-blog',this).height(highestLatestBlog);
        }

        /* -------------------------------------------------------------
            Client Review Carousel
        ------------------------------------------------------------- */
        if ($('.client-review-carousel').length){
            $('.client-review-carousel').owlCarousel({
                loop: true,
                items:1,
                dots: true,
                margin: 10,
                responsiveClass: true
            });
        }


        /* -------------------------------------------------------------
            Sidebar - Price Filter
        ------------------------------------------------------------- */
        if ($('#price-filter-range').length){
            $("#price-filter-range").slider({
                range: true,
                min: 0,
                max: 500,
                values: [75, 300],
                slide: function(event, ui) {
                    $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
                }
            });
            $("#amount").val("$" + $("#price-filter-range").slider("values", 0) + " - $" + $("#price-filter-range").slider("values", 1));
        }

        /* -------------------------------------------------------------
            Sidebar - Category Toggle
        ------------------------------------------------------------- */
        $('li.cat-item:has(ul.children)').addClass('list-parent');
        
        $('.rc-widget-area .cat-item').each(function(){
            if ($(this).find('ul.children').length > 0) {
                $(this).append('<i class="closed fa fa-angle-down"></i>');
            }
            $(this).find('ul.children').hide();
        });
        $( "body" ).on( "click", '.cat-item .closed', function(){
            $(this).parent().find('ul.children').show(500);
            $(this).removeClass('closed').removeClass('fa-angle-down').addClass('opened').addClass('fa-angle-up');
        });
        $( "body" ).on( "click", '.cat-item .opened', function(){
            $(this).parent().find('ul.children').hide(500);
            $(this).removeClass('opened').removeClass('fa-angle-up').addClass('closed').addClass('fa-angle-down');
        });

        /* -------------------------------------------------------------
            Widget - Opening Time
        ------------------------------------------------------------- */
        $(".opening-time-1:has(span)").addClass('off-time');
        $(".opening-time-2:has(span)").addClass('off-time');


        /* -------------------------------------------------------------
            Accordion
        ------------------------------------------------------------- */
        if ($('#accordion').length){
            $("#accordion").accordion({
                collapsible: true,
                icons: false,
                heightStyle: "content"
            });
        }


        /* -------------------------------------------------------------
            Reservation - Time and Date Picker
        ------------------------------------------------------------- */
        if ($('.datepicker').length){
            $('.datepicker').pickadate();
        }
        if ($('.timepicker').length){
            $('.timepicker').pickatime();
        }


        /* -------------------------------------------------------------
            Recipe Filter
        ------------------------------------------------------------- */
        if ($('.recipes-list').length){
            var $recipeFilter = $('.recipes-list').isotope({
                itemSelector: '.recipes-list-item',
                masonry: {
                    columnWidth: '.recipes-list-item'
                    }
                });
            $('.recipe-category-list .selectpicker').on( 'change', function() {
                var filterValue = this.value;
                $recipeFilter.isotope({ filter: filterValue });
            });

            $recipeFilter.imagesLoaded().progress( function() {
              $recipeFilter.isotope('layout');
            });
        }
        

        /* -------------------------------------------------------------
            Gallery Filter
        ------------------------------------------------------------- */
        if ($('.gallery-img-filter').length){
            var $galleryFilter = $('.gallery-img-filter').isotope({
                itemSelector: '.gallery-img',
                masonry: {
                    columnWidth: '.gallery-img'
                    }
                });
            $('.gallery-filter-list').on( 'click', 'li', function() {
                var filterValue = $(this).attr('data-filter');
                $('.gallery-filter-list').find('.is-checked').removeClass('is-checked');
                $(this).addClass('is-checked');
                $galleryFilter.isotope({ filter: filterValue });
            });

            $galleryFilter.imagesLoaded().progress( function() {
              $galleryFilter.isotope('layout');
            });
        }



        /* -------------------------------------------------------------
            Recommended Product Carousel
        ------------------------------------------------------------- */
        if ($('.products-carousel').length){
            $('.products-carousel').owlCarousel({
                loop: true,
                dots: true,
                margin: 10,
                responsiveClass: true,
                responsive: {
                    0: {
                        items: 1,
                        nav: true
                    },
                    500: {
                        items: 2,
                        nav: false
                    }
                }
            })
        }


        /* -------------------------------------------------------------
            Single Product Image Carousel
        ------------------------------------------------------------- */
        if ($('.big-images').length){
            var $sync1 = $(".big-images"),
                $sync2 = $(".slider-thumbs"),
                flag = false,
                duration = 300;

            $sync1
                .owlCarousel({
                    items: 1,
                    margin: 10,
                    nav: false,
                    dots: false
                })
            $sync2
                .owlCarousel({
                    margin: 15,
                    items: 2,
                    nav: true,
                    navText: [
                        "<i class='fa fa-angle-left'></i>",
                        "<i class='fa fa-angle-right'></i>"
                    ]
                })
                .on('click', '.owl-item', function() {
                    $sync1.trigger('to.owl.carousel', [$(this).index(), duration, true]);
                })
        }


        /* -------------------------------------------------------------
            Cart Count increment & decrement
        ------------------------------------------------------------- */
        $("#increment").on('click', function() {
            var $n = $("#number");
            $n.val(Number($n.val()) + 1);
        });
        $("#decrement").on('click', function() {
            var $n = $("#number");
            if (Number($n.val()) != 1) {
                $n.val(Number($n.val()) - 1);
            }
        });


        /* -------------------------------------------------------------
            Checkout Page Steps
        ------------------------------------------------------------- */
        if ($('#checkout-step').length){
            $("#checkout-step").steps({
                headerTag: "h3",
                bodyTag: "section",
                transitionEffect: "fade",
                transitionEffectSpeed: 100,
                stepsOrientation: "vertical",
                labels: {
                    finish: "CONFIRM ORDER"
                },
                onFinished: function (event, currentIndex) {}
            });
        }


        /* -------------------------------------------------------------
            Checkout Page Modification for HTML syntex
        ------------------------------------------------------------- */
        if ($('.user-info').length){
            $(".user-info").appendTo('.add-user-info');
            $(".add-user-info .user-info").show();
        }


        /* -------------------------------------------------------------
            Newsletter Overlay
        ------------------------------------------------------------- */
        if ($('#myModal').length){
            setTimeout(function(){
                $('#myModal').modal('show');
            }, 60000);
        }


        /* -------------------------------------------------------------
            Scroll To Top
        ------------------------------------------------------------- */
        $.scrollUp({
            scrollText: '<i class="fa fa-angle-up"></i>'
        });


        /* -------------------------------------------------------------
            Comment form inner linking
        ------------------------------------------------------------- */
        $('a[href^="#commentform"]').on('click',function (e) {
            e.preventDefault();
            var target = this.hash;
            var $target = $(target);
            $('html, body').stop().animate({
                 'scrollTop': $target.offset().top
            }, 900, 'swing');
        });

        /* -------------------------------------------------------------
            Responsive video on blog page
        ------------------------------------------------------------- */
        $(".blog-content").fitVids();

    });
})(jQuery);
