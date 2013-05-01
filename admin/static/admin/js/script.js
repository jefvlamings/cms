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
 * Page
 *
 * @param id
 * @constructor
 */
var Page = function(id){
    var _this = this;
    _this.id = id;
    _this.delete = function() {
        $.ajax({
            type: "GET",
            url: "/admin/delete/" + _this.id
        }).done(function(msg) {
            if(msg === "1"){

                // Fire a success message
                var message = new Message('Pagina verwijderd','success');
                message.fire();

                // Delete list item from the page tree
                _this.removeFromPageTree()
            }
            else{
                // Fire an error message
                var message = new Message('Pagina kon niet verwijderd worden','error');
                message.fire();
            }
        });
    }
    _this.publish = function() {
        $.ajax({
            type: "GET",
            url: "/admin/publish/" + _this.id
        }).done(function(msg) {
            if(msg === "1"){

                // Fire a success message
                var message = new Message('Pagina gepubliceerd','success');
                message.fire();
            }
            else{
                // Fire an error message
                var message = new Message('Pagina kon niet gepubliceerd worden','error');
                message.fire();
            }
        });
    }
    _this.unpublish = function() {
        $.ajax({
            type: "GET",
            url: "/admin/unpublish/" + _this.id
        }).done(function(msg) {
            if(msg === "1"){

                // Fire a success message
                var message = new Message('Pagina verborgen','success');
                message.fire();
            }
            else{
                // Fire an error message
                var message = new Message('Pagina kon niet verborgen worden','error');
                message.fire();
            }
        });
    }
    _this.removeFromPageTree = function() {
        $('#page-tree #' + _this.id).closest('li').fadeOut('slow',function(){
            $(this).remove();
        });
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

    // Delete
    $('#page-tree .delete').click(function(){

        // Get the pageId
        var pageId = $(this).closest('li').attr('id');

        // Is the user sure of is action?
        var confirm = window.confirm('Ben u zeker dat deze pagina wilt verwijderen?');

        // Delete if confirmed
        if (confirm === true){
            var page = new Page(pageId);
            page.delete();
        }

       // Disable the link
       return false;
    });

    // Publish
    $('.publish-button').click(function(){

        // Get the page Id
        var pageId = $(this).closest('form').attr('id');
        var page = new Page(pageId);

        if($(this).hasClass('published')){
            // Unpublish the page
            page.unpublish();
            $(this).removeClass('published');
        }
        else{
            // Publish the page
            page.publish();
            $(this).addClass('published');
        }

        // Disable the link
        return false;
    });

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