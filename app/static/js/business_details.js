$(document).ready(function() {
    // Show the first section
    $('.form-section').first().addClass('active');

    // Handle navigation buttons
    $('.next-section').click(function() {
        var nextSection = $(this).data('next');
        $(this).closest('.form-section').removeClass('active');
        $('#' + nextSection).addClass('active');
        $('html, body').animate({ scrollTop: $('#' + nextSection).offset().top }, 800);
    });

    $('.prev-section').click(function() {
        var prevSection = $(this).data('prev');
        $(this).closest('.form-section').removeClass('active');
        $('#' + prevSection).addClass('active');
        $('html, body').animate({ scrollTop: $('#' + prevSection).offset().top }, 800);
    });
});