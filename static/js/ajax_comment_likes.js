$(document).ready(function() {
    $(document).on('click', '.likes', function (e) {
        e.preventDefault();
        var $button = $(this);
        var commentId = $button.data('commentid');
        var likesCount = parseInt($button.data('likescount'));
        var likeUrl = $button.data('like-url');

        $.ajax({
            type: 'POST',
            url: likeUrl,
            data: {
                commentid: commentId,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            success: function (json) {
                $button.find('.comment-likes-count').text(json['result']);
                $button.data('likescount', json['result']);
                $button.find('.fa-heart').toggleClass('liked', json['result'] > likesCount);
            },
            error: function (xhr, errmsg, err) {
                alert('Failed to like the comment. Please try again later.');
            }
        });
    });
});
