$(document).ready(function() {
    $(document).on('click', '.article-likes', function (e) {
        e.preventDefault();
        var $button = $(this);
        var articleId = $button.data('articleid');
        var likesCount = parseInt($button.data('likescount'));
        var likeUrl = $button.data('like-url');

        $.ajax({
            type: 'POST',
            url: likeUrl,
            data: {
                articleid: articleId,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            success: function (json) {
                $button.find('.article-likes-count').text(json['result']);
                $button.data('likescount', json['result']);
                $button.find('.fa-heart').toggleClass('liked', json['result'] > likesCount);
            },
            error: function (xhr, errmsg, err) {
                alert('Failed to like the article. Please try again later.');
            }
        });
    });
});
