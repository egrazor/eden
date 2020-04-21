document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['interaction', 'dayGrid', 'timeGrid', 'list', 'bootstrap'],
        header: {
            right: 'listWeek, today prev, next',
            center: 'title',
            left: 'dayGridMonth, timeGridWeek, timeGridDay'
        },
        buttonText: {
            today: 'сегодня',
            month: 'месяц',
            week: 'неделя',
            day: 'день',
            list: 'список событий'
        },
        defaultView: 'timeGridWeek',
        allDaySlot: false,
        firstDay: 1,
        themeSystem: 'standart',
        locale: 'ru',
        eventTimeFormat: {
            hour: 'numeric',
            minute: '2-digit',
            meridiem: false,
        },
        events: '/calendar/all_events/',

        dateClick: function(info) {
            $('#dialog').dialog('open');
        },
    });

    calendar.render();
});

$(function(){

    $('.datetimepicker').datetimepicker({
        format: "d.m.Y H:i",
        minTime: "08-00",
        maxTime: "20-00",
        lang: 'ru',
    });

    $('#dialog').dialog({
        autoOpen: false,
        show: {
            effect: 'fold',
            duration: 300
        },
        hide: {
            effect: 'clip',
            duration: 300
        },
        minHeight: 300,
        minWidth: 400,
        title: 'Добавить событие'
    });
});