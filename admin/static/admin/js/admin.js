/**
 * Message
 *
 * @param text
 * @param level
 * @constructor
 */
var Message = function(text,level) {
    var _this = this;
    _this.level = (typeof level === 'undefined') ? 'debug' : level;
    _this.text = (typeof text === 'undefined') ? 'Geen melding' : text;
    _this.fire = function(){
        $('.messages').html('<li class="' + _this.level + '">' + _this.text + '</li>');
        setTimeout(function(){
            $('.messages li').fadeOut('slow');
        },2000);
    }
}

/**
 * When the DOM is ready
 */
$('document').ready(function(){

    // Fancybox
    $('.view').click(function() {
        var imageUrl = $(this).attr('href');
         $.fancybox.open([
            {
                href : imageUrl,
                title : '1st title'
            }
        ], {
            padding : 0
        });
        return false;
    })

    // Slide page menu
    $('#toggle-page-tree').click(function() {

        if($(this).hasClass('button-pressed')) {
            $('#page-menu').animate({
                'left': '-230px'
            },'fast');
            $(this).removeClass('button-pressed');
        }
        else {
            $('#page-menu').animate({
                'left': '70px'
            },'fast');
            $(this).addClass('button-pressed');
        }

        // Disable the link
        return false;
    })

});