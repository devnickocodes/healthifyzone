document.addEventListener("DOMContentLoaded", function () {

    const editButtons = document.getElementsByClassName("edit-btn");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const collapsibleSection = document.getElementById("collapseExample");

    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("delete-btn");
    const deleteConfirm = document.getElementById("deleteConfirm");
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

        // delete blog post comments 
        document.addEventListener("click", function (e) {
            if (e.target.classList.contains("delete-btn")) {
                let commentId = e.target.getAttribute("comment_id");
                const slug = e.target.getAttribute("data-slug");
                const deleteUrl = `/${slug}/delete_comment/${commentId}/`;
                deleteConfirm.setAttribute("href", deleteUrl);
                deleteModal.show();
            }
        });
});