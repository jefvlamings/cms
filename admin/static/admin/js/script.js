/**
 * Message
 *
 * @param text
 * @param level
 * @constructor
 */
var Message = function(text,level) {
    this.level = (typeof level === 'undefined') ? 'debug' : level;
    this.text = (typeof text === 'undefined') ? 'Geen melding' : text;
    this.fire = function(){

        $('.messages').html('<li class="' + this.level + '">' + this.text + '</li>');

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
    this.id = id;
    this.delete = function() {
        $.ajax({
            type: "GET",
            url: "/admin/delete/" + this.id
        }).done(function(msg) {
            if(msg === "1"){

                // Delete list item from the page tree
                $('#' + this.id).fadeOut('slow',function(){
                    $(this).remove();
                });

                // Fire a success message
                var message = new Message('Pagina verwijderd','success');
                message.fire();
            }
            else{
                // Fire an error message
                var message = new Message('Pagina kon niet verwijderd worden','error');
                message.fire();
            }
        });
    }
    this.publish = function() {
        $.ajax({
            type: "GET",
            url: "/admin/publish/" + this.id
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
    this.unpublish = function() {
        $.ajax({
            type: "GET",
            url: "/admin/unpublish/" + this.id
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
}

/**
 * Delete a page
 *
 * @param id
 */
function deletePage(id){

    // Is the user sure of is action?
    var confirm = window.confirm('Ben u zeker dat deze pagina wilt verwijderen?');

    // Delete if confirmed
    if (confirm === true){


    }
}

/**
 * When the DOM is ready
 */
$('document').ready(function(){

    // Get the page Id
    var pageId = $('form').attr('id');

    // Delete
    $('.delete').click(function(){

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

});