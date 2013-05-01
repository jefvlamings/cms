/**
 * MediaItem
 *
 * @param id
 * @constructor
 */
var MediaItem = function(id) {
    var _this = this;

    /* -- FUNCTIONS -- */
    _this.delete = function() {
        var request = $.ajax({
            url: '/admin/media/delete/' + id,
            type: "POST",
            crossDomain: false,
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", _this.csrfToken);
            }
        });
        request.done(function() {
            new Message('Bestand verwijderd','success').fire();
            _this.removeBox();
        })
        request.fail(function() {
            new Message('Bestand kon niet verwijderd worden','error').fire();
        })
    };
    _this.removeBox = function() {
        _this.box.fadeOut();
        _this.box.queue(function() {
            _this.box.remove();
        });
    }

    /* -- PROPERTIES -- */
    _this.box = $('.media-item[data-file-id="' + id + '"]');
    _this.form = $('#fileupload');
    _this.csrfToken = _this.form.find('input[name=csrfmiddlewaretoken]').val();
}

/**
 * When the DOM is ready to rock 'n roll
 */
$(document).ready(function() {

    // Initialize the jQuery File Upload widget:
    $('#fileupload').fileupload();

    $('.media-item .delete').click(function() {
        var id = $(this).closest('.media-item').attr('data-file-id');
        var mediaItem = new MediaItem(id)
        mediaItem.delete();
        return false;
    });

})
