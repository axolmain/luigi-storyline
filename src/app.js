document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('overlay');
    const closeSidebarBtn = document.getElementById('close-sidebar-btn');
    const openSidebarBtn = document.getElementById('open-sidebar-btn');

    // Open sidebar
    openSidebarBtn.addEventListener('click', () => {
        sidebar.style.transform = 'translateX(0)';
        overlay.style.display = 'block';
        openSidebarBtn.style.display = 'none'; // Hide the open button
    });

    // Close sidebar
    closeSidebarBtn.addEventListener('click', () => {
        sidebar.style.transform = 'translateX(-100%)';
        overlay.style.display = 'none';
        openSidebarBtn.style.display = 'block'; // Show the open button
    });

    // Close sidebar by clicking the overlay
    overlay.addEventListener('click', () => {
        sidebar.style.transform = 'translateX(-100%)';
        overlay.style.display = 'none';
        openSidebarBtn.style.display = 'block'; // Show the open button
    });
});
