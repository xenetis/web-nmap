$(document).ready(function() {
    const sidebarToggle = $('#sidebarToggle');
    if (sidebarToggle.length) {
        if (localStorage.getItem('webnmap|sidebar-toggle') === 'true') {
            $('body').toggleClass('webnmap-sidenav-toggled');
        }
        sidebarToggle.on('click', function(event) {
            event.preventDefault();
            $('body').toggleClass('webnmap-sidenav-toggled');
            localStorage.setItem('webnmap|sidebar-toggle', $('body').hasClass('webnmap-sidenav-toggled'));
        });
    }

    const datatablesSimple = $('#datatablesSimple');
    if (datatablesSimple.length) {
         new simpleDatatables.DataTable(datatablesSimple.get(0));
    }

    $(document).on('click', '.delete-btn', function(){
        var deleteButton = $(this)
        $('#deleteConfirmBtn').click(function() {
            deleteButton.parent("form").submit();
            $('#deleteModal').modal('hide');
        });
        $('#deleteModal .modal-body strong').html(deleteButton.attr('name'));
        $('#deleteModal').modal('show');
    });
});