document.addEventListener("DOMContentLoaded", function () {

    const editButtons = document.getElementsByClassName("edit-btn");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const leaveCommentButton = document.querySelector(".leave-comment-btn");
    const collapsibleSection = document.getElementById("collapseExample");

    // Update article comment

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("comment_id");
            let slug = e.target.getAttribute("data-slug");
            let commentContent = document.getElementById(`comment${commentId}`).innerText;
            commentText.value = commentContent;
            submitButton.innerText = "Update";
            commentForm.setAttribute("action", `/${slug}/edit_comment/${commentId}/`);

            // Open the collapsible section when an edit button is clicked
            // which remains open in case the user would like to edit more than
            //one comment
            let collapse = new bootstrap.Collapse(collapsibleSection);
            collapse.show();
        });
    }
});