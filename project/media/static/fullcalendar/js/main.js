document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['interaction', 'dayGrid', 'timeGrid', 'list', 'bootstrap'],
        header: {
            right: 'today prev, next',
            center: 'title',
            left: 'dayGridMonth, timeGridWeek, timeGridDay'
        },
        defaultView: 'timeGridWeek',
        allDaySlot: false,
        themeSystem: 'standart',
        events: '/fullcalendar/all_events',
    });

    calendar.render();
});