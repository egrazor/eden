document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
        plugins: ['interaction', 'dayGrid', 'timeGrid', 'list', 'resourceTimeline', 'bootstrap'],
        header: {
            right: 'prev, next today',
            center: 'left',
        },
        footer: {
            right: 'list',
            right: 'dayGridMonth, timeGridWeek, timeGridDay',
            left: 'resourceTimelineWeek, resourceTimelineDay,'
        },
        buttonText: {
            today: 'сегодня',
            month: 'месяц',
            week: 'неделя',
            day: 'день',
            list: 'список событий',
            resourceTimelineWeek: 'неделя (по аудиториям)',
            resourceTimelineDay: 'день (по аудиториям)',
        },
        defaultView: 'timeGridWeek',
        allDaySlot: false,
        firstDay: 1,
        themeSystem: 'bootstrap',
        // добавил новую строку
        locale: 'ru',
        eventTimeFormat: {
            hour: 'numeric',
            minute: '2-digit',
            meridiem: false,
        },
        minTime: "08:00",
        maxTime: "20:00",
        aspectRatio: 1.0,
        events: '/calendar/events/',
        resources: '/calendar/resources/',

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